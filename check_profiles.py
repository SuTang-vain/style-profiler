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
2026-09-15 新增两层校验：8 份 playbook 的 AUTO:INSTITUTION / AUTO:CELLS 标记区
（gen_budgets.py 生成区）逐格回核 _aggregate.json 的 two_level 键——机构值列 vs
institution、对照列 vs corpus_naive_median、range 列 vs dispersion.range、delta 表
格值与 delta 值；容差与剥离规则沿用本脚本既有约定；每库第二行报告，合计单列。
"""
import json, re, statistics, sys
from pathlib import Path

import gen_budgets as gb

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

def check_two_level(lib, verbose=False):
    """playbook AUTO 标记区两层表格逐格回核 two_level JSON。
    返回 (checked, fails, skipped, err)；容差/剥离/合并行规则与 gen_budgets 一致。"""
    pb = Path(f"templates/{gb.LIBS[lib]}")
    if not pb.exists():
        return 0, [], [], f"playbook 不存在（{pb}）"
    tl = json.load(open(f"output/{lib}/_aggregate.json"))["two_level"]
    lines = pb.read_text(encoding="utf-8").split("\n")
    checked, fails, skipped = 0, [], []

    def cmp_cell(label, colname, cell, exp):
        nonlocal checked
        if cell.strip() == "--":
            skipped.append((f"{label}/{colname}", "JSON 缺席标 --"))
            return
        got = gb.parse_plain(cell)
        if gb.close_values(got, exp):
            checked += len(exp)
            if verbose:
                print(f"  PASS  {lib}/{label}/{colname}: 表格={cell!r} JSON={exp}")
        else:
            fails.append(f"{label}/{colname}: 表格={cell!r} JSON="
                         f"{[round(v, 2) for v in exp]}")

    # AUTO:INSTITUTION：机构值 / 朴素 median / range 三列
    try:
        b, e = gb.find_region(lines, "INSTITUTION")
    except ValueError:
        return 0, [], [], "缺 AUTO:INSTITUTION 标记"
    for ln in lines[b + 1:e]:
        if not ln.lstrip().startswith("|"):
            continue
        cells = gb.split_row(ln)
        if gb.is_sep_row(cells) or cells[0] == "指标":
            continue
        keys = gb.scan_label(cells[0])
        if not keys:
            skipped.append((cells[0], "人工行（未映射指标）"))
            continue
        missing = [k for k in keys if k not in tl["institution"]]
        if missing:
            skipped.append((cells[0], f"JSON 缺席 {','.join(missing)}"))
            continue
        exps = {1: [tl["institution"][k] for k in keys],
                2: [tl["corpus_naive_median"][k] for k in keys],
                3: [tl["dispersion"][k]["range"] for k in keys]}
        for ci, colname in ((1, "机构值"), (2, "朴素median"), (3, "range")):
            if ci < len(cells):
                cmp_cell(cells[0], colname, cells[ci], exps[ci])

    # AUTO:CELLS：机构层列 + 各格「值（±delta）」
    try:
        b, e = gb.find_region(lines, "CELLS")
    except ValueError:
        return checked, fails, skipped, "缺 AUTO:CELLS 标记"
    header, codes = None, []
    for ln in lines[b + 1:e]:
        if not ln.lstrip().startswith("|"):
            continue
        cells = gb.split_row(ln)
        if header is None:
            header = cells
            codes = [c.split()[0] for c in cells[2:]]  # 跳过「指标」「机构层」
            continue
        if gb.is_sep_row(cells):
            continue
        keys = gb.scan_label(cells[0])
        if not keys:
            skipped.append((f"delta {cells[0]}", "人工行（未映射指标）"))
            continue
        if any(k not in tl["institution"] for k in keys):
            skipped.append((f"delta {cells[0]}", "JSON 缺席"))
            continue
        inst = [tl["institution"][k] for k in keys]
        cmp_cell(cells[0], "机构层", cells[1], inst)
        for j, code in enumerate(codes, start=2):
            if j >= len(cells):
                break
            if cells[j].strip() == "--":
                skipped.append((f"{cells[0]}/{code}", "格值缺席标 --"))
                continue
            mets = tl["cells"].get(code, {}).get("metrics", {})
            if any(k not in mets for k in keys):
                skipped.append((f"{cells[0]}/{code}", "格 metrics 缺席"))
                continue
            vals = [mets[k] for k in keys]
            deltas = [v - iv for v, iv in zip(vals, inst)]
            parsed = gb.parse_delta_cell(cells[j])
            if parsed is None:
                fails.append(f"delta {cells[0]}/{code}: 单元格无法解析 {cells[j]!r}")
                continue
            got_v, got_d = parsed
            if gb.close_values(got_v, vals) and gb.close_values(got_d, deltas):
                checked += len(vals) * 2
                if verbose:
                    print(f"  PASS  {lib}/{cells[0]}/{code}: {cells[j]!r}")
            else:
                fails.append(
                    f"delta {cells[0]}/{code}: 表格={cells[j]!r} JSON 值="
                    f"{[round(v, 2) for v in vals]} delta={[round(d, 2) for d in deltas]}")
    return checked, fails, skipped, None


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
    # 两层校验：playbook AUTO 标记区 vs two_level JSON（与上面 STYLE-PROFILE 校验独立）
    n2_pass = n2_fail = n2_skip = 0
    for lib in LIBS:
        checked, fails, skipped, err = check_two_level(lib, verbose)
        if err:
            print(f"[SKIP] {lib}·两层: {err}")
            n2_skip += 1
            continue
        skip_note = f"，跳过 {len(skipped)}" + (
            "（" + "、".join(f"{n}·{r}" for n, r in skipped) + "）" if skipped else ""
        )
        if fails:
            n2_fail += 1
            print(f"[FAIL] {lib}·两层（校验 {checked} 值{skip_note}）:")
            for x in fails:
                print(f"       {x}")
        else:
            n2_pass += 1
            print(f"[PASS] {lib}·两层（校验 {checked} 值{skip_note}）")
    print(f"两层校验合计: {n2_pass} PASS / {n2_fail} FAIL / {n2_skip} SKIP")
    sys.exit(1 if (n_fail or n2_fail) else 0)

if __name__ == "__main__":
    main()
