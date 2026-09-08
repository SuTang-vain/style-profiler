#!/usr/bin/env python3
"""档案数值一致性校验：档案第 2 节表格 vs 统计层实测 median

背景（2026-09-08 总体评估发现的盲区）：MSR 档案画像曾写"篇幅最长 5,660 词"
而实测 median 1,634——第 1 节文字与第 2 节表格/统计层脱节，且无机制拦截。
本脚本把核对制度化：档案表格中本库列的每个数值，必须与 output/<lib>/ 单篇
JSON 汇总的 median 一致（±0.51 容差：覆盖整数舍入 0.5 与两位小数，容千分位逗号）。

用法: python3 check_profiles.py          # 校验全部档案
      python3 check_profiles.py -v        # 逐项打印（含 PASS/SKIP）
退出码: 0=全部一致；1=存在 FAIL（以统计层为准修正档案后重跑）
注: 壳中客档案基于 24 篇旧口径存档（重跑欠账中），SKIP 并提示。
2026-09-08 修复：单元格/指标名匹配前先剥离装饰字符（* ` † ‡）——此前 **8.8**、
2.7† 等加粗/注记单元格正则不匹配被静默跳过，造成误报 PASS；并新增跳过计数：
每表显式报告"N 行：校验 M 值，跳过 K"，跳过数 >0 时不得声称"全部一致"。
"""
import json, re, statistics, sys
from pathlib import Path

# 档案 lib 目录 → (表头本库列匹配子串, 指标名映射表之外的提示)
LIBS = {
    "kezhongke": "壳中客",  # 24 篇重跑口径（2026-09-08）；单库表取"中位数"列
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
    ("篇幅", "", "word_count"),
    ("平均句长", "sentences", "avg_sentence_len"),
    ("P90句长", "sentences", "p90_sentence_len"),
    ("平均段长", "paragraphs", "avg_paragraph_len"),
    ("数字密度", "evidence", "number_per_1k"),
    ("精确数字", "evidence", "precise_per_1k"),
    ("年份锚点", "evidence", "year_per_1k"),
    ("外链", "evidence", "links_per_1k"),
    ("限定语", "stance", "hedge_hits"),
    ("hedge", "stance", "hedge_hits"),
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

# 单元格装饰字符：加粗 **、行内代码 `、脚注 † ‡ —— 匹配数值/指标名前剥离
DECOR = re.compile(r"[*`†‡]")

def strip_decor(s):
    return DECOR.sub("", s).strip()

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
                if col_idx is None and any(k in cells[1:2] for k in ("中位数", "median")):
                    col_idx = 1  # 单库表（指标|中位数|P25–P75|说明）
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
        checked = 0
        skipped = []  # [(指标名, 原因)]
        for metric_name, cell in rows:
            if not cell.strip():
                continue  # 空单元格不占跳过名额
            name = strip_decor(metric_name)
            m = re.match(r"[0-9][0-9,\.]*", strip_decor(cell))
            if not m:
                skipped.append((name, "非数值/注记"))
                if verbose:
                    print(f"  SKIP  {lib}/{name}: 非数值/注记单元格 {cell!r}")
                continue
            declared = float(m.group(0).replace(",", ""))
            hit = next(((g, k) for pre, g, k in METRIC_MAP if name.startswith(pre)), None)
            if hit and hit[1] == "word_count" and lib == "kezhongke":
                hit = ("", "cjk_chars")  # 中文库篇幅=字符数
            if hit is None:
                skipped.append((name, "指标未映射"))
                if verbose:
                    print(f"  SKIP  {lib}/{name}: 指标未映射 {cell!r}")
                continue
            actual = measured_median(lib, hit[0], hit[1])
            if actual is None:
                skipped.append((name, "统计层无实测值"))
                if verbose:
                    print(f"  SKIP  {lib}/{name}: 统计层无实测值")
                continue
            checked += 1
            ok = abs(declared - actual) <= 0.51  # 容整数舍入（0.5）+ 两位小数
            if verbose:
                print(f"  {'PASS' if ok else 'FAIL'}  {lib}/{name}: 档案={declared} 实测={round(actual,2)}")
            if not ok:
                fails.append(f"{name}: 档案={declared} 实测={round(actual, 2)}")
        skip_note = f"，跳过 {len(skipped)}" + (
            "（" + "、".join(f"{n}·{r}" for n, r in skipped) + "）" if skipped else ""
        )
        summary = f"{len(rows)} 行：校验 {checked} 值{skip_note}"
        if fails:
            n_fail += 1
            print(f"[FAIL] {lib}（{summary}）:")
            for x in fails:
                print(f"       {x}")
        elif skipped:
            n_pass += 1
            print(f"[PASS] {lib}（{summary}；已校验值全部一致，跳过项未计入）")
        else:
            n_pass += 1
            print(f"[PASS] {lib}（{len(rows)} 行表格全部一致）")
    print(f"\n合计: {n_pass} PASS / {n_fail} FAIL / {n_skip} SKIP（kezhongke 旧口径欠账未入校验）")
    sys.exit(1 if n_fail else 0)

if __name__ == "__main__":
    main()
