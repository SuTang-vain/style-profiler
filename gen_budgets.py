#!/usr/bin/env python3
"""playbook 定量预算节生成器：AUTO 标记区内表格 ← two_level JSON

背景（2026-09-15）：8 份 playbook 的 §x.1 机构层预算表 / §x.2 分体裁 delta 预算表
此前每逢聚合层重跑都手工刷新（37d5933 为 8 库 swarm 手工重算），不同步风险高。
本脚本把两表数值生成器化：

- `<!-- AUTO:INSTITUTION begin/end -->` 包住机构层表（表头+全部行）：按行键（指标名
  关键词扫描）匹配，只重写「两层机构值 / 全库朴素 median / 跨体裁 range」三列数值；
  「判定」「写作指令」两列是人工校准 prose，逐字保留。某指标行在 JSON 缺席 → 保留该行、
  数值列标 `--` 并 stdout 提示；JSON 有而表格缺的指标 → 追加行（判定列 `待人工判定`）
  并 stdout 提示。
- `<!-- AUTO:CELLS begin/end -->` 包住 delta 表整表：格值（±delta）由
  two_level.cells − institution 代码重算。格集合（列）不变时保留现有行序/列序与既有
  数字格式；格集合增减时整表按 JSON 列序重建，并显著提示「判定列/写作含义需人工复核」。
- `<!-- AUTO:LAYOUT begin/end -->`（AUTO:CELLS 之后）为「排版（参考，非硬约束）」小节：
  structure.tables / structure.code_blocks 逐篇 JSON 实算全库 median 与各出值格 median
  （格划分 genre.unified.code，n≥3 出值）。
- 数值一致的单元格保留原字符串（容差 ±0.51，与 check_profiles 一致）——格式微调
  （如 5.0 vs 5）不产生 diff；超容差才按规范格式重写并逐条报告（--check 模式只报告
  不写文件，退出码 1=有漂移）。
- 「机构层 vs 朴素 median 差异简注」是人工分析文字，不重写；stdout 打印按当前 JSON
  算出的 top-N 相对差异清单供人工核对。

用法: python3 gen_budgets.py            # 处理全部 8 库
      python3 gen_budgets.py --lib NAME # 单库
      python3 gen_budgets.py --check    # 只报告漂移，不写文件（退出码 0=无漂移）
"""
import argparse
import json
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# lib → playbook 文件名（注意 openai 为复数 playbooks）
LIBS = {
    "kezhongke": "genre-playbook-kezhongke.md",
    "cerebras": "genre-playbook-cerebras.md",
    "databricks": "genre-playbook-databricks.md",
    "eleuther": "genre-playbook-eleuther.md",
    "google-research": "genre-playbook-google-research.md",
    "microsoft-research": "genre-playbook-microsoft-research.md",
    "anthropic": "genre-playbook-anthropic.md",
    "openai": "genre-playbooks-openai.md",
}

# 与 check_profiles 一致的「一致」判定容差：容整数舍入（0.5）与千分位逗号
TOL = 0.51

# 中文库篇幅口径 = cjk_chars（篇幅（中文字符）行承载）；word_count 键视为已覆盖，
# 不触发追加行 / 未覆盖提示
SUPPRESS_APPEND = {"kezhongke": {"word_count"}}

# 行首指标名关键词扫描（按在标签中出现的位置取序）→ two_level 指标键。
# 注意：MATTR 必须先于 TTR 匹配；不用英文关键词（hedge/absolutist），
# 避免误判 openai 的「克制比 hedge:absolutist（派生值）」人工行。
LABEL_RE = re.compile(
    r"(?P<cjk_len>篇幅（中文字符)"
    r"|(?P<word>篇幅)"
    r"|(?P<read>阅读时[长间])"
    r"|(?P<sent>平均句长)"
    r"|(?P<p90>P90 ?句长)"
    r"|(?P<para>平均段长)"
    r"|(?P<num>数字密度)"
    r"|(?P<precise>精确数字)"
    r"|(?P<year>年份)"
    r"|(?P<hedge>限定语)"
    r"|(?P<abs>断言型绝对化|断言绝对化|绝对化断言|绝对化)"
    r"|(?P<quant>全称量词|数量词|量化词)"
    r"|(?P<fp>第一人称)"
    r"|(?P<selfref>客观自[指称])"
    r"|(?P<excl>感叹号)"
    r"|(?P<q>设问|问句|疑问句)"
    r"|(?P<mattr>MATTR(?:\(150\))?)"
    r"|(?P<ttr>TTR)"
    r"|(?P<enratio>中英字符比)"
    r"|(?P<cjk>中文字符|CJK ?字符)"
    r"|(?P<links>外链|链接)"
    r"|(?P<ref>参考文献条目|参考条目|文献条目)"
    r"|(?P<cite>引文标记|文内引用)"
)
GROUP_TO_KEY = {
    "cjk_len": "cjk_chars", "word": "word_count", "read": "reading_time_min",
    "sent": "avg_sentence_len", "p90": "p90_sentence_len", "para": "avg_paragraph_len",
    "num": "number_per_1k", "precise": "precise_per_1k", "year": "year_per_1k",
    "hedge": "hedge_hits", "abs": "absolutist_hits", "quant": "quantifier_hits",
    "fp": "first_person_count", "selfref": "objective_selfref_count",
    "excl": "exclamations", "q": "questions", "mattr": "mattr", "ttr": "ttr",
    "enratio": "en_char_ratio", "cjk": "cjk_chars", "links": "links_per_1k",
    "ref": "reference_entries", "cite": "citation_marks",
}

# 追加行（JSON 有而表格缺的指标）的默认行首标签
DEFAULT_LABEL = {
    "word_count": "篇幅（词）", "cjk_chars": "中文字符（cjk_chars）",
    "reading_time_min": "阅读时长（分钟）", "avg_sentence_len": "平均句长",
    "p90_sentence_len": "P90 句长", "avg_paragraph_len": "平均段长",
    "number_per_1k": "数字密度 /千词", "precise_per_1k": "精确数字 /千词",
    "year_per_1k": "年份 /千词", "links_per_1k": "外链 /千词",
    "reference_entries": "参考条目", "citation_marks": "引文标记 [n]",
    "hedge_hits": "限定语 /千词", "absolutist_hits": "绝对化 /千词",
    "quantifier_hits": "全称量词 /千词", "first_person_count": "第一人称（次/篇）",
    "objective_selfref_count": "客观自指（次/篇）", "exclamations": "感叹号",
    "questions": "设问（次/篇）", "ttr": "TTR", "mattr": "MATTR",
    "en_char_ratio": "中英字符比",
}

DECOR = re.compile(r"[*`†‡]")
NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")
DELTA_CELL_RE = re.compile(r"^(?P<vals>[^（()]*)（(?P<deltas>[^（）()]*)）\s*$")
SIGN_NUM_RE = re.compile(r"^\s*([+±−-]?)\s*(\d[\d,]*(?:\.\d+)?)\s*$")


def strip_decor(s):
    return DECOR.sub("", s).strip()


def scan_label(label):
    """行首标签 → 有序指标键列表（支持「TTR / MATTR」式多指标合并行）。"""
    keys = []
    for m in LABEL_RE.finditer(strip_decor(label)):
        k = GROUP_TO_KEY[m.lastgroup]
        if k not in keys:
            keys.append(k)
    return keys


def fmt_num(v):
    """规范数值格式：整数值去小数、≥1000 加千分位逗号、两位小数去尾零。"""
    v = round(float(v) + 0.0, 2)
    if v == int(v):
        return f"{int(v):,}"
    return f"{v:,.2f}".rstrip("0").rstrip(".")


def fmt_delta(d):
    """delta 格式：±0 / +x / −x（负号用 Unicode minus −，与现表一致）。"""
    d = round(float(d) + 0.0, 2)
    if d == 0:
        return "±0"
    return ("+" if d > 0 else "−") + fmt_num(abs(d))


def fmt_delta_cell(vals, deltas):
    """delta 表单元格：「值（±delta）」；多指标合并行值与 delta 均以 " / " 连接，
    全部 delta 相同（如零值三连行全 ±0）时只写一个。"""
    base = " / ".join(fmt_num(v) for v in vals)
    rd = [round(float(d) + 0.0, 2) for d in deltas]
    if len(rd) > 1 and len(set(rd)) == 1:
        dpart = fmt_delta(rd[0])
    else:
        dpart = " / ".join(fmt_delta(d) for d in rd)
    return f"{base}（{dpart}）"


def parse_plain(cell):
    """机构层表数值列 → [float]（剥离装饰字符；千分位逗号）。"""
    return [float(t.replace(",", "")) for t in NUM_RE.findall(strip_decor(cell))]


def parse_signed(tok):
    m = SIGN_NUM_RE.match(tok)
    if not m:
        return None
    sign, num = m.groups()
    v = float(num.replace(",", ""))
    if sign in ("−", "-"):
        return -v
    return v  # "+" / "±" / 无号 均按字面非负值（±0 → 0）


def parse_delta_cell(cell):
    """「1,782（−178）」→ ([1782.0], [-178.0])；解析失败返回 None。"""
    m = DELTA_CELL_RE.match(strip_decor(cell))
    if not m:
        return None
    vals = [parse_signed(t) for t in m.group("vals").split("/")]
    deltas = [parse_signed(t) for t in m.group("deltas").split("/")]
    if any(v is None for v in vals) or any(d is None for d in deltas):
        return None
    return vals, deltas


def close_values(got, exp):
    """数值列比对：等长逐值比，或单值对多指标（全零合并行「0」= 三指标均 0）。"""
    if len(got) == len(exp):
        return all(abs(a - b) <= TOL for a, b in zip(got, exp))
    if len(got) == 1 and len(exp) > 1:
        return all(abs(got[0] - b) <= TOL for b in exp)
    return False


def reconcile_plain(old, exp, report, ctx):
    """机构层数值列：与 JSON 一致（±TOL）则保留原字符串，否则规范格式重写并记录。"""
    if close_values(parse_plain(old), exp):
        return old
    new = " / ".join(fmt_num(v) for v in exp)
    report["changed"].append(f"{ctx}: {old!r} → {new!r}")
    return new


def reconcile_delta(old, vals, deltas, report, ctx):
    """delta 表单元格：值与 delta 均一致（±TOL）则保留原字符串，否则重生成并记录。"""
    parsed = parse_delta_cell(old)
    if parsed is not None:
        got_v, got_d = parsed
        if close_values(got_v, vals) and close_values(got_d, deltas):
            return old
    new = fmt_delta_cell(vals, deltas)
    report["changed"].append(f"{ctx}: {old!r} → {new!r}")
    return new


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def join_row(cells):
    return "| " + " | ".join(cells) + " |"


def is_sep_row(cells):
    return all(set(c) <= set("-: ") and c for c in cells)


def find_region(lines, name):
    """返回 (begin_idx, end_idx) —— 标记行行号；缺标记时报错指明文件需先插标记。"""
    begin = end = None
    for i, ln in enumerate(lines):
        if ln.strip() == f"<!-- AUTO:{name} begin -->":
            begin = i
        elif ln.strip() == f"<!-- AUTO:{name} end -->":
            end = i
    if begin is None or end is None or end <= begin:
        raise ValueError(f"缺少或错位 AUTO:{name} 标记（需先手工插入标记行）")
    return begin, end


def regen_institution(region_lines, tl, lib, report):
    """机构层表：按行键匹配重写三列数值，判定/写作指令列逐字保留。"""
    out, covered = [], set()
    seen_rows = 0
    for line in region_lines:
        if not line.lstrip().startswith("|"):
            out.append(line)
            continue
        cells = split_row(line)
        if seen_rows == 0 or is_sep_row(cells):
            seen_rows += 1
            out.append(line)  # 表头与分隔行原样保留
            continue
        seen_rows += 1
        keys = scan_label(cells[0])
        if not keys:
            report["manual_rows"].append(cells[0])  # 如 openai 克制比派生值行
            out.append(line)
            continue
        covered.update(keys)
        missing = [k for k in keys if k not in tl["institution"]]
        if missing:
            report["missing_rows"].append(f"{cells[0]}（{', '.join(missing)}）")
            for i in (1, 2, 3):
                if i < len(cells):
                    cells[i] = "--"
            out.append(join_row(cells))
            continue
        exp_cols = [
            [tl["institution"][k] for k in keys],
            [tl["corpus_naive_median"][k] for k in keys],
            [tl["dispersion"][k]["range"] for k in keys],
        ]
        new_cells = list(cells)
        for i, exp in enumerate(exp_cols, start=1):
            if i < len(new_cells):
                new_cells[i] = reconcile_plain(
                    new_cells[i], exp, report, f"机构层表/{cells[0]}/列{i}")
        out.append(join_row(new_cells) if new_cells != cells else line)
    # JSON 有而表格缺的指标 → 追加行（判定列留「待人工判定」）
    suppressed = SUPPRESS_APPEND.get(lib, set())
    for k in sorted(tl["institution"]):
        if k not in covered and k not in suppressed:
            naive = tl["corpus_naive_median"].get(k)
            rng = tl["dispersion"].get(k, {}).get("range")
            row = join_row([DEFAULT_LABEL.get(k, k), fmt_num(tl["institution"][k]),
                            fmt_num(naive) if naive is not None else "--",
                            fmt_num(rng) if rng is not None else "--",
                            "待人工判定", "待人工补写"])
            out.append(row)
            report["appended_rows"].append(k)
    report["institution_rows"] = seen_rows - 2 if seen_rows >= 2 else 0
    return out, covered


def regen_cells(region_lines, tl, lib, report):
    """delta 表：列=机构层+各出值格；格集合不变时保留现有行/列序与格式。"""
    table_idx = [i for i, ln in enumerate(region_lines) if ln.lstrip().startswith("|")]
    if not table_idx:
        raise ValueError("AUTO:CELLS 区内未找到表格")
    out = list(region_lines)
    header = split_row(region_lines[table_idx[0]])
    old_codes = [c.split()[0] for c in header[2:]]  # 跳过「指标」「机构层」两列
    cells = tl["cells"]
    json_codes = list(cells.keys())
    if set(old_codes) != set(json_codes):
        added = [c for c in json_codes if c not in old_codes]
        removed = [c for c in old_codes if c not in json_codes]
        report["cell_set_change"] = f"新增 {added or '无'} / 消失 {removed or '无'}"
        order = json_codes
    else:
        order = old_codes
    # 表头：格名与 n 按 JSON 校对；一致则保留原文
    new_header = header[:2] + [f"{c} {cells[c]['genre']}（n={cells[c]['n']}）"
                               for c in order]
    if new_header != header:
        if not report["cell_set_change"]:
            report["changed"].append(f"delta 表头 n 刷新: {header[1:]} → {new_header[1:]}")
        out[table_idx[0]] = join_row(new_header)
        # 分隔行对齐列数
        if len(table_idx) > 1 and is_sep_row(split_row(region_lines[table_idx[1]])):
            out[table_idx[1]] = "|" + "---|" * len(new_header)
    covered = set()
    n_data_rows = 0
    for i in table_idx[2:]:
        row = split_row(region_lines[i])
        keys = scan_label(row[0])
        if not keys:
            report["manual_rows"].append(f"delta 表 {row[0]}")
            continue
        covered.update(keys)
        n_data_rows += 1
        new_row = list(row)
        missing = [k for k in keys if k not in tl["institution"]]
        if missing:
            report["missing_rows"].append(f"delta 表 {row[0]}（{', '.join(missing)}）")
            new_row[1:] = ["--"] * (len(new_row) - 1)
        else:
            inst = [tl["institution"][k] for k in keys]
            new_row[1] = reconcile_plain(
                new_row[1], inst, report, f"delta 表/{row[0]}/机构层")
            for j, code in enumerate(order, start=2):
                mets = cells[code]["metrics"]
                if any(k not in mets for k in keys):
                    report["missing_rows"].append(
                        f"delta 表 {row[0]}/{code} 格（指标缺席）")
                    cell_txt = "--"
                else:
                    vals = [mets[k] for k in keys]
                    deltas = [v - iv for v, iv in zip(vals, inst)]
                    if j < len(new_row):
                        cell_txt = reconcile_delta(
                            new_row[j], vals, deltas, report,
                            f"delta 表/{row[0]}/{code}")
                    else:
                        # 格集合变更新增列：旧行无此列，直接按规范格式生成
                        cell_txt = fmt_delta_cell(vals, deltas)
                if j < len(new_row):
                    new_row[j] = cell_txt
                else:
                    new_row.append(cell_txt)
        if new_row != row:
            out[i] = join_row(new_row)
    suppressed = SUPPRESS_APPEND.get(lib, set())
    uncovered = [k for k in sorted(tl["institution"])
                 if k not in covered and k not in suppressed]
    if uncovered:
        report["cells_uncovered"] = uncovered
    report["cells_rows"] = n_data_rows
    report["cells_order"] = order
    return out


def compute_layout(root, lib, tl, order):
    """排版参考小节数据：逐篇 JSON structure 键，全库 median + 各出值格 median。"""
    per_article = []
    for f in sorted((root / "output" / lib).glob("*.json")):
        if f.name == "_aggregate.json":
            continue
        r = json.load(open(f))
        if "structure" not in r or "genre" not in r:
            continue  # 跳过 genre-labels.json 等非篇目 JSON
        st = r.get("structure") or {}
        code = (r.get("genre", {}).get("unified") or {}).get("code")
        per_article.append((code, st.get("tables"), st.get("code_blocks")))

    def med(idx, code=None):
        vs = [a[idx] for a in per_article
              if isinstance(a[idx], (int, float)) and (code is None or a[0] == code)]
        return statistics.median(vs) if vs else None

    cols = []  # (code, genre, n, tables_med, code_blocks_med)
    for code in order:
        info = tl["cells"].get(code, {})
        cols.append((code, info.get("genre", code), info.get("n", 0),
                     med(1, code), med(2, code)))
    corpus = (med(1), med(2))
    return cols, corpus, len(per_article)


def render_layout(root, lib, tl, order):
    cols, corpus, n_articles = compute_layout(root, lib, tl, order)

    def cell(v):
        return fmt_num(v) if v is not None else "--"

    lines = [
        f"**排版（参考，非硬约束）**（逐篇 JSON `structure` 键实算，{n_articles} 篇；"
        f"格划分 genre.unified.code、n≥3 出值，与 two_level 同格口径；"
        f"gen_budgets.py 生成，聚合层重跑后随本区刷新）：",
        "",
        "| 指标 | 全库 median | "
        + " | ".join(f"{c} {g}（n={n}）" for c, g, n, _, _ in cols) + " |",
        "|" + "---|" * (2 + len(cols)),
        "| 表格（个/篇） | " + cell(corpus[0]) + " | "
        + " | ".join(cell(t) for _, _, _, t, _ in cols) + " |",
        "| 代码块（个/篇） | " + cell(corpus[1]) + " | "
        + " | ".join(cell(b) for _, _, _, _, b in cols) + " |",
    ]
    return lines


def top_divergence(tl, n=8):
    """机构层 vs 朴素 median 相对差异 top-N（供人工核对差异简注 blockquote）。"""
    rows = []
    for k, iv in tl["institution"].items():
        nv = tl["corpus_naive_median"].get(k)
        if nv is None:
            continue
        d = iv - nv
        rel = abs(d) / abs(nv) if nv else (float("inf") if d else 0.0)
        rows.append((rel, k, nv, iv, d))
    rows.sort(key=lambda r: -r[0])
    return rows[:n]


def process_playbook(text, tl, lib, root):
    """返回 (新文本, report)。report: changed/missing_rows/appended_rows/manual_rows/
    cell_set_change/cells_uncovered + 行数统计。"""
    report = {"changed": [], "missing_rows": [], "appended_rows": [],
              "manual_rows": [], "cell_set_change": None, "cells_uncovered": []}
    lines = text.split("\n")

    b, e = find_region(lines, "INSTITUTION")
    new_region, _ = regen_institution(lines[b + 1:e], tl, lib, report)
    lines = lines[:b + 1] + new_region + lines[e:]

    b, e = find_region(lines, "CELLS")
    new_region = regen_cells(lines[b + 1:e], tl, lib, report)
    lines = lines[:b + 1] + new_region + lines[e:]

    b, e = find_region(lines, "LAYOUT")
    lines = lines[:b + 1] + render_layout(root, lib, tl, report["cells_order"]) + lines[e:]

    return "\n".join(lines), report


def print_report(lib, report, changed_text, tl):
    flag = "改写" if changed_text else "一致"
    print(f"== {lib}（{flag}）==")
    print(f"   机构层表 {report['institution_rows']} 行 / "
          f"delta 表 {report['cells_rows']} 行 × {len(report['cells_order'])} 格")
    if report["cell_set_change"]:
        print(f"   ⚠️ 格集合变更（{report['cell_set_change']}）——"
              f"§x.1 判定列与 §x.2 分体裁写作含义需人工复核！")
    for c in report["changed"]:
        print(f"   重写: {c}")
    for m in report["missing_rows"]:
        print(f"   ⚠️ JSON 缺席，数值列标 `--`: {m}")
    for a in report["appended_rows"]:
        print(f"   ⚠️ JSON 有而表格缺，已追加行（判定列 待人工判定）: "
              f"{a}（{DEFAULT_LABEL.get(a, a)}）")
    if report["cells_uncovered"]:
        print(f"   提示: delta 表未覆盖 JSON 指标（保持现状惯例，不自动加行）: "
              f"{', '.join(report['cells_uncovered'])}")
    if report["manual_rows"]:
        print(f"   人工行保留不动: {', '.join(report['manual_rows'])}")
    divs = top_divergence(tl)
    print(f"   机构层 vs 朴素 median top 差异（供人工核对差异简注，不重写）：")
    for rel, k, nv, iv, d in divs:
        rel_s = f"{rel * 100:.0f}%" if rel != float("inf") else "朴素为 0 不可比"
        print(f"     {k}: 朴素 {fmt_num(nv)} → 机构 {fmt_num(iv)}"
              f"（{'+' if d >= 0 else '−'}{fmt_num(abs(d))}，相对差 {rel_s}）")


def run_lib(root, lib, check=False):
    pb = root / "templates" / LIBS[lib]
    agg = root / "output" / lib / "_aggregate.json"
    if not pb.exists():
        print(f"[SKIP] {lib}: {pb} 不存在")
        return False
    tl = json.load(open(agg))["two_level"]
    text = pb.read_text(encoding="utf-8")
    new_text, report = process_playbook(text, tl, lib, root)
    changed = new_text != text
    print_report(lib, report, changed, tl)
    if changed and not check:
        pb.write_text(new_text, encoding="utf-8")
        print(f"   已写入 {pb.name}")
    elif changed and check:
        print(f"   [DRIFT] {pb.name} 与 JSON 不一致（--check 不写文件）")
    return changed


def main():
    ap = argparse.ArgumentParser(description="playbook 定量预算节生成器（AUTO 标记区 ← two_level JSON）")
    ap.add_argument("--lib", help="只处理单库（如 anthropic）")
    ap.add_argument("--check", action="store_true",
                    help="只报告漂移不写文件；退出码 0=无漂移 1=有漂移")
    args = ap.parse_args()
    libs = [args.lib] if args.lib else list(LIBS)
    drift = []
    for lib in libs:
        if lib not in LIBS:
            print(f"[SKIP] 未知库 {lib}（可选：{', '.join(LIBS)}）")
            sys.exit(2)
        if run_lib(ROOT, lib, check=args.check):
            drift.append(lib)
    if args.check:
        print(f"\n--check 合计: {len(drift)} 库有漂移"
              + (f"（{', '.join(drift)}）" if drift else "，全部一致"))
        sys.exit(1 if drift else 0)


if __name__ == "__main__":
    main()
