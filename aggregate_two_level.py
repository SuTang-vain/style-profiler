#!/usr/bin/env python3
"""两层风格模型 · 聚合层（机构层不变量 + 体裁格 delta，docs/methodology-two-level-style-model.md）

只消费 output/<lib>/ 下已有的 per-article JSON（绝不重跑 analyze()——
重跑会以规则层 genre_guess 覆盖 genre 字段，毁掉 LLM 路由回填的 unified 标签）。
体裁归属一律读 genre.unified.code（A/E/R/N/P/G）；缺 unified 的篇目跳过并计入
skipped_no_unified。空格纪律：格内 n<3 不出格值；机构层只对出值格取中位；空体裁不计 0。

结果写回 output/<lib>/_aggregate.json 的新键 "two_level"：
  cells              {体裁代码: {genre, n, metrics: {指标: median}}}（n≥3 才出现）
  institution        {指标: 各出值体裁格中位的中位}（体裁平衡化，!= 全库朴素中位）
  dispersion         {指标: {range, iqr}}（跨体裁格离散度，方法论文档 §一 的 IQR/全距）
  corpus_naive_median {指标: 全库朴素中位}（对照列，方法论 §二.2 要求保留）
  signature_candidates 机构签名候选：格内全距 < 该指标跨机构全距一半的指标
                     （§一 起点阈值；候选判定需本库 ≥2 个出值格，单格库无从谈不变量）

用法:
    python3 aggregate_two_level.py                # 全部 8 库
    python3 aggregate_two_level.py --lib openai   # 只写回指定库（可多次）
"""
import argparse
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from profiler import AGGREGATE_KEYS  # noqa: E402

OUTPUT = ROOT / "output"
# kezhongke-v10 是 kezhongke 子集，不做独立两层聚合
LIBS = ["anthropic", "cerebras", "databricks", "eleuther", "google-research",
        "kezhongke", "microsoft-research", "openai"]
MIN_CELL_N = 3


def metric_value(article, key, grp):
    try:
        v = article[grp][key] if grp else article[key]
        return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None
    except (KeyError, TypeError):
        return None


def load_articles(lib_dir):
    """读 per-article JSON；按结构（含 genre+sentences）区分文章与 genre-labels 等辅助文件。"""
    articles = []
    for f in sorted(lib_dir.glob("*.json")):
        if f.name == "_aggregate.json":
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        if isinstance(d, dict) and "genre" in d and "sentences" in d:
            articles.append(d)
    return articles


def _median(xs):
    return round(statistics.median(xs), 2)


def _quartiles(xs):
    """与 profiler.aggregate 相同的索引式 p25/p75 口径。"""
    vs = sorted(xs)
    return (round(vs[int(0.25 * len(vs))], 2),
            round(vs[min(int(0.75 * len(vs)), len(vs) - 1)], 2))


def two_level(articles):
    """articles: per-article 结果 dict 列表。返回 two_level 结构（不含 signature_candidates）。"""
    cells_src, skipped = {}, []
    for a in articles:
        unified = a.get("genre", {}).get("unified")
        code = unified.get("code") if isinstance(unified, dict) else None
        if not code:
            skipped.append(a.get("file", "<unknown>"))
            continue
        cells_src.setdefault(code, {"genre": unified.get("genre"), "articles": []})
        cells_src[code]["articles"].append(a)

    cells = {}
    for code, c in sorted(cells_src.items()):
        if len(c["articles"]) < MIN_CELL_N:
            continue  # n<3 缺席，不出格值
        metrics = {}
        for spec in AGGREGATE_KEYS:
            key, grp = (spec[0], spec[1]) if len(spec) > 1 else (spec[0], "")
            vs = [v for a in c["articles"] if (v := metric_value(a, key, grp)) is not None]
            if vs:
                metrics[key] = _median(vs)
        cells[code] = {"genre": c["genre"], "n": len(c["articles"]), "metrics": metrics}

    institution, dispersion = {}, {}
    metric_names = {k for c in cells.values() for k in c["metrics"]}
    for key in sorted(metric_names):
        cell_vals = [c["metrics"][key] for c in cells.values() if key in c["metrics"]]
        institution[key] = _median(cell_vals)
        p25, p75 = _quartiles(cell_vals)
        dispersion[key] = {"range": round(max(cell_vals) - min(cell_vals), 2),
                           "iqr": round(p75 - p25, 2),
                           "n_cells": len(cell_vals)}

    naive = {}
    for spec in AGGREGATE_KEYS:
        key, grp = (spec[0], spec[1]) if len(spec) > 1 else (spec[0], "")
        vs = [v for a in articles if (v := metric_value(a, key, grp)) is not None]
        if vs:
            naive[key] = _median(vs)

    return {
        "method": "two-level-v1（genre.unified.code 分格；格内中位→体裁中位的中位；n<3 缺席）",
        "n_articles": len(articles),
        "skipped_no_unified": len(skipped),
        "skipped_files": skipped,
        "cells": cells,
        "institution": institution,
        "dispersion": dispersion,
        "corpus_naive_median": naive,
    }


def signature_candidates(per_lib):
    """机构签名候选（方法论 §一 起点阈值）：本库跨体裁格全距 < 该指标跨机构全距的一半。
    跨机构全距取各库 institution 值的全距；候选判定要求本库 ≥2 个出值格。"""
    metrics = {m for r in per_lib.values() for m in r["institution"]}
    cross_range = {}
    for m in metrics:
        insts = [r["institution"][m] for r in per_lib.values() if m in r["institution"]]
        cross_range[m] = round(max(insts) - min(insts), 2) if len(insts) >= 2 else None
    for lib, r in per_lib.items():
        cands = {}
        for m, disp in r["dispersion"].items():
            cr = cross_range.get(m)
            if cr and disp["n_cells"] >= 2 and disp["range"] < cr / 2:
                cands[m] = {"within_lib_range": disp["range"],
                            "cross_institution_range": cr}
        r["signature_candidates"] = {
            "criterion": "within_lib_range < cross_institution_range / 2，且本库出值格 ≥2"
                         "（methodology §一 起点阈值，实施后校准）",
            "metrics": cands,
        }
    return per_lib


def write_back(lib, result):
    agg_path = OUTPUT / lib / "_aggregate.json"
    agg = json.loads(agg_path.read_text(encoding="utf-8"))
    agg["two_level"] = result
    agg_path.write_text(json.dumps(agg, ensure_ascii=False, indent=1), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="两层风格模型聚合（消费现有 per-article JSON，不重跑 analyze）")
    ap.add_argument("--lib", action="append", choices=LIBS,
                    help="只写回指定库（可多次）；跨机构全距仍按全 8 库计算")
    args = ap.parse_args()
    targets = args.lib or LIBS

    per_lib = {}
    for lib in LIBS:  # 全量计算：signature 的跨机构全距需要所有库的机构层
        per_lib[lib] = two_level(load_articles(OUTPUT / lib))
    signature_candidates(per_lib)

    for lib in targets:
        write_back(lib, per_lib[lib])
        r = per_lib[lib]
        cells = " ".join(f"{g}:{c['n']}" for g, c in r["cells"].items())
        print(f"[{lib}] n={r['n_articles']} skipped={r['skipped_no_unified']} "
              f"cells=[{cells}] sig={len(r['signature_candidates']['metrics'])}")


if __name__ == "__main__":
    main()
