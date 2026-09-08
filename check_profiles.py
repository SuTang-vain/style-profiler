#!/usr/bin/env python3
"""档案数值一致性校验：档案第 2 节表格 vs 统计层实测 median

背景（2026-09-08 总体评估发现的盲区）：MSR 档案画像曾写"篇幅最长 5,660 词"
而实测 median 1,634——第 1 节文字与第 2 节表格/统计层脱节，且无机制拦截。
本脚本把核对制度化：档案表格中本库列的每个数值，必须与 output/<lib>/ 单篇
JSON 汇总的 median 一致（±0.05 容差，容千分位逗号）。

用法: python3 check_profiles.py          # 校验全部档案
      python3 check_profiles.py -v        # 逐项打印（含 PASS）
退出码: 0=全部一致；1=存在 FAIL（以统计层为准修正档案后重跑）
注: 壳中客档案基于 24 篇旧口径存档（重跑欠账中），SKIP 并提示。
"""
import json, re, statistics, sys
from pathlib import Path

# 档案 lib 目录 → (表头本库列匹配子串, 指标名映射表之外的提示)
LIBS = {
    "cerebras": "Cerebras",
    "eleuther": "Eleuther",
    "databricks": "Databricks",
    "openai": "OpenAI",
    "anthropic": "Anthropic",
    "google-research": "GoogleRes",
    "microsoft-research": "MSR",
}

# 档案表格行首指标名（前缀匹配）→ (group, key)
METRIC_MAP = [
    ("篇幅（词）", "", "word_count"),
    ("平均句长", "sentences", "avg_sentence_len"),
    ("P90句长", "sentences", "p90_sentence_len"),
    ("平均段长", "paragraphs", "avg_paragraph_len"),
    ("数字密度", "evidence", "number_per_1k"),
    ("精确数字", "evidence", "precise_per_1k"),
    ("年份锚点", "evidence", "year_per_1k"),
    ("外链", "evidence", "links_per_1k"),
    ("限定语", "stance", "hedge_hits"),
    ("断言绝对化", "stance", "absolutist_hits"),
    ("断言型绝对化", "stance", "absolutist_hits"),
    ("全称量词", "stance", "quantifier_hits"),
    ("第一人称", "stance", "first_person_count"),
    ("客观自指", "stance", "objective_selfref_count"),
    ("感叹号", "stance", "exclamations"),
    ("问句", "stance", "questions"),
    ("TTR", "diction", "ttr"),
    ("MATTR", "diction", "mattr"),
]

def measured_median(lib, group, key):
    vs = []
    for f in Path(f"output/{lib}").glob("*.json"):
        if f.name == "_aggregate.json":
            continue
        r = json.load(open(f))
        try:
            v = r[group][key] if group else r[key]
        except KeyError:
            v = None
        if isinstance(v, (int, float)):
            vs.append(v)
    return statistics.median(vs) if vs else None

def parse_profile(lib, header_name):
    """返回 [(指标名, 档案数值 str)] —— 第 2 节表格本库列"""
    files = list(Path(f"output/{lib}").glob("STYLE-PROFILE-*.md"))
    if not files:
        return None, "档案文件不存在"
    rows, in_sec2, col_idx = [], False, None
    for line in files[0].read_text(encoding="utf-8").split("\n"):
        if line.startswith("## 2."):
            in_sec2 = True
            continue
        if in_sec2 and line.startswith("## "):
            break
        if in_sec2 and line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if set(cells[0]) <= set("-: ") and len(cells) > 1:
                continue  # 分隔行
            if col_idx is None:
                for i, c in enumerate(cells):
                    if header_name.lower() in c.lower():
                        col_idx = i
                        break
                continue
            if col_idx is not None and len(cells) > col_idx:
                rows.append((cells[0], cells[col_idx]))
    if col_idx is None:
        return None, f"表头未找到本库列（{header_name}）"
    return rows, None

def main():
    verbose = "-v" in sys.argv
    n_pass = n_fail = n_skip = 0
    for lib, header in LIBS.items():
        rows, err = parse_profile(lib, header)
        if err:
            print(f"[SKIP] {lib}: {err}")
            n_skip += 1
            continue
        fails = []
        for metric_name, cell in rows:
            m = re.match(r"[0-9][0-9,\.]*", cell.replace("†", "").strip())
            if not m:
                continue  # 非数值单元格（— / † 注记等）
            declared = float(m.group(0).replace(",", ""))
            hit = next(((g, k) for pre, g, k in METRIC_MAP if metric_name.startswith(pre)), None)
            if hit is None:
                continue
            actual = measured_median(lib, hit[0], hit[1])
            if actual is None:
                continue
            ok = abs(declared - round(actual, 2)) <= 0.051 or abs(declared - actual) <= 0.051
            if verbose:
                print(f"  {'PASS' if ok else 'FAIL'}  {lib}/{metric_name}: 档案={declared} 实测={round(actual,2)}")
            if not ok:
                fails.append(f"{metric_name}: 档案={declared} 实测={round(actual, 2)}")
        if fails:
            n_fail += 1
            print(f"[FAIL] {lib}:")
            for x in fails:
                print(f"       {x}")
        else:
            n_pass += 1
            print(f"[PASS] {lib}（{len(rows)} 行表格全部一致）")
    print(f"\n合计: {n_pass} PASS / {n_fail} FAIL / {n_skip} SKIP（kezhongke 旧口径欠账未入校验）")
    sys.exit(1 if n_fail else 0)

if __name__ == "__main__":
    main()
