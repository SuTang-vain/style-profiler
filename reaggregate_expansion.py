#!/usr/bin/env python3
"""体裁平衡扩容后的顶层重聚合（Phase B1，2026-09-15 执行；扩容采录与 router v2 打标于 2026-09-14 完成）

铁律：绝不重跑 analyze()/profiler.py 于任何语料文件——重跑会以规则层
genre_guess 覆盖 genre 字段，毁掉 LLM 路由回填的 genre.unified。本脚本只读
output/<lib>/ 下现有 per-article JSON（analyze() 结果的持久化形状），直接交给
profiler.aggregate()（中位数 + 四分位口径）重算顶层数值键，不写任何单篇 JSON。

等价性验证（--check，写回前必须先过）：
  1. fixture 基准：kezhongke-v10 子集（10 篇）重算 == output/kezhongke-v10/_aggregate.json
     ——该目录是历史子集快照，只读对照，绝不重算/写回。
  2. 旧值全量对照：各库旧篇子集（genre.unified.source 以 llm-routing-v1 开头；
     英文库 10 篇、kezhongke 23 篇）重算 == git HEAD 版 _aggregate.json（扩容前
     旧聚合），aggregate() 产出的每个键逐键比对（全量，非抽样）。

写回（--write）：
  顶层数值键 + genre_distribution/genre_files 以新全量（20×7 + 24）重算值替换；
  two_level 键原样保留（随后由 aggregate_two_level.py 全量刷新，格集合会变）；
  追加 "_meta_expansion" 注记键（日期、篇数变化、router v2；databricks 附量具变更注记）。
  genre_distribution 等旧口径键保留 legacy 语义（仍按 genre.genre），两层分布在
  two_level 键内，不混口径。

用法:
    python3 reaggregate_expansion.py --check    # 只验证，不写
    python3 reaggregate_expansion.py --write    # 验证通过才写回
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from profiler import aggregate, AGGREGATE_KEYS  # noqa: E402
from aggregate_two_level import load_articles  # noqa: E402  同口径文章识别（genre+sentences 形状）

OUTPUT = ROOT / "output"
LIBS = {  # lib: (扩容前篇数, 扩容后篇数)
    "anthropic": (10, 20), "cerebras": (10, 20), "databricks": (10, 20),
    "eleuther": (10, 20), "google-research": (10, 20), "kezhongke": (23, 24),
    "microsoft-research": (10, 20), "openai": (10, 20),
}
V10_DIR = OUTPUT / "kezhongke-v10"  # 历史子集快照：只读对照，不重算

AGG_PRODUCED_KEYS = {spec[0] for spec in AGGREGATE_KEYS} | {"genre_distribution", "genre_files"}

DATABRICKS_INSTRUMENT_NOTE = (
    "量具变更：新 10 篇因官网订阅表单改版缺少国家下拉样板（约 500 词/篇），"
    "word_count 新旧篇目系统性不可比——聚合值跨量具版本，方向：新篇偏轻。"
    "篇幅及其衍生均值类读数按带偏口径使用，必要时回看单篇 JSON 分组。")


def meta_expansion(lib):
    n_before, n_after = LIBS[lib]
    m = {
        "date": "2026-09-15",
        "event": "体裁平衡扩容（2026-09-14 完成采录与路由）后 Phase B1 顶层重聚合（中位数口径）",
        "n_articles": f"{n_before}→{n_after}",
        "router": "llm-routing-v2-expansion（仅新篇目回填 genre.unified；旧篇标签与旧 JSON 未动）",
        "method": "消费现有 per-article JSON 经 profiler.aggregate() 重算；未重跑 analyze()",
        "equivalence_check": "kezhongke-v10 fixture 全键一致 + 本库 llm-routing-v1 旧子集对 HEAD 旧聚合逐键一致",
    }
    if lib == "databricks":
        m["instrument_change"] = DATABRICKS_INSTRUMENT_NOTE
    return m


def _diff(path, a, b, out):
    """递归比对两个字典/标量；out 收集差异路径说明。"""
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                out.append(f"{path}.{k}: 旧聚合缺键（新={b[k]!r}）")
            elif k not in b:
                out.append(f"{path}.{k}: 旧聚合多出键（旧={a[k]!r}）")
            else:
                _diff(f"{path}.{k}", a[k], b[k], out)
    elif a != b:
        out.append(f"{path}: 旧={a!r} 新算={b!r}")


def check_fixture():
    """fixture 等价性：v10 子集重算 vs 历史快照（逐键）。"""
    recomputed = aggregate(load_articles(V10_DIR))
    stored = json.loads((V10_DIR / "_aggregate.json").read_text(encoding="utf-8"))
    diffs = []
    _diff("kezhongke-v10", stored, recomputed, diffs)
    return diffs


def check_old_subset(lib):
    """旧值对照：v1 旧篇子集重算 vs HEAD 旧聚合（aggregate 产出的键逐键）。"""
    articles = load_articles(OUTPUT / lib)
    old = [a for a in articles
           if str(a.get("genre", {}).get("unified", {}).get("source", "")).startswith("llm-routing-v1")]
    n_before = LIBS[lib][0]
    if len(old) != n_before:
        return [f"{lib}: 旧子集篇数 {len(old)} != 预期 {n_before}"]
    recomputed = aggregate(old)
    head = subprocess.run(["git", "show", f"HEAD:output/{lib}/_aggregate.json"],
                          capture_output=True, text=True, cwd=ROOT, check=True).stdout
    stored = json.loads(head)
    diffs = []
    for k in sorted(AGG_PRODUCED_KEYS):
        if k not in stored and k not in recomputed:
            continue
        _diff(k, stored.get(k), recomputed.get(k), diffs)
    return [f"{lib}: {d}" for d in diffs]


def run_check():
    all_diffs = check_fixture()
    for lib in LIBS:
        all_diffs += check_old_subset(lib)
    if all_diffs:
        print("等价性验证 FAILED：")
        for d in all_diffs:
            print(" ", d)
        return False
    print("等价性验证 OK：kezhongke-v10 fixture 全键一致；8 库旧子集重算与 HEAD 旧聚合逐键一致")
    return True


def write_back(lib):
    agg_path = OUTPUT / lib / "_aggregate.json"
    existing = json.loads(agg_path.read_text(encoding="utf-8"))
    fresh = aggregate(load_articles(OUTPUT / lib))
    # 先摘除 aggregate() 口径内的陈旧键（新全量下已无值的指标），再覆盖新值；
    # two_level 与其他注记键原样保留
    for k in AGG_PRODUCED_KEYS:
        existing.pop(k, None)
    existing.update(fresh)
    existing["_meta_expansion"] = meta_expansion(lib)
    agg_path.write_text(json.dumps(existing, ensure_ascii=False, indent=1), encoding="utf-8")
    n = fresh.get("word_count") or fresh.get("cjk_chars")
    print(f"[{lib}] n={LIBS[lib][0]}→{LIBS[lib][1]} "
          f"word/cjk median={n['median'] if n else '—'} genre_distribution={fresh['genre_distribution']}")


def main():
    ap = argparse.ArgumentParser(description="扩容后顶层重聚合（从 per-article JSON，绝不重跑 analyze）")
    ap.add_argument("--check", action="store_true", help="只跑等价性验证")
    ap.add_argument("--write", action="store_true", help="验证通过后写回 8 库 _aggregate.json")
    args = ap.parse_args()
    if not run_check():
        sys.exit(1)
    if args.write:
        for lib in LIBS:
            write_back(lib)
        print("写回完成；下一步：python3 aggregate_two_level.py 刷新 two_level 键")


if __name__ == "__main__":
    main()
