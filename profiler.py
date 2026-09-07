#!/usr/bin/env python3
"""研究性文章风格分析工具 · 统计层（确定性指标）

用法:
    python3 profiler.py article.md                # 单篇 → stdout JSON
    python3 profiler.py article.md -o out.json    # 单篇 → 文件
    python3 profiler.py dir/ -o out/              # 目录批量 → 每篇一个 JSON
    python3 profiler.py dir/ --aggregate corpus.json  # 批量 + 聚合基线

设计原则（对应《把 LLM 的不可控关进可验证的笼子》）:
  统计指标全部确定性计算、可复现、可证伪；
  语步/论证等判断性标注不在本脚本内（见 rubric/ 目录，由 LLM 按 rubric 执行）。
"""
import argparse
import json
import re
import statistics
import sys
from pathlib import Path

try:
    import jieba
    import jieba.analyse
    JIEBA = True
except ImportError:
    JIEBA = False

# ---------- 词典（透明、可编辑；改动应记 changelog） ----------

HEDGES = [
    "据报道", "据官方", "据媒体", "据披露", "据称", "官方口径", "官方给出的",
    "可能", "或许", "疑似", "大约", "接近", "超过", "约", "预计", "初步",
    "一定程度上", "仍需", "待确认", "建议以", "为准", "存在争议", "尚未",
    "未必", "有待", "仍在", "尚不", "暂无", "存疑", "仍建议", "有待核实",
]
ABSOLUTISTS = [
    "必须", "一定", "显然", "毫无疑问", "永远", "唯一",
    "绝对", "肯定", "必然", "彻底", "完全", "无疑", "毋庸置疑",
]
# 全称量词/排行表述单独一档：研究文本中高频出现（"所有客户""最热门岗位"），
# 不构成断言性文风信号，只作参考指标——2026-09-06 调优：原混计导致 absolutist 虚高（见验证报告调优点 1）
QUANTIFIERS = ["所有", "全部", "最", "第一"]

# ---------- 英文适配（2026-09-06：OpenAI 博客外部实测引入） ----------

HEDGES_EN = [
    "reportedly", "according to", "may", "might", "could", "approximately",
    "roughly", "about", "around", "preliminary", "suggests", "suggest",
    "likely", "possibly", "seems", "appears", "we believe", "we expect",
    "we anticipate", "early", "initial", "toward", "remains", "unclear",
    "uncertain", "in progress", "future work", "we hope", "we aim",
]
ABSOLUTISTS_EN = [
    "must", "always", "never", "completely", "entirely", "certainly",
    "obviously", "undeniably", "guaranteed", "impossible", "everyone",
    "no one", "fundamental", "essential", "critical", "vital",
]
QUANTIFIERS_EN = ["all ", "every ", "most ", "first ", "best ", "largest ", "biggest "]
FIRST_PERSON_EN = [" we ", " our ", " us ", " I ", " my "]
OBJ_SELFREF_EN = ["this post", "this paper", "this study", "this report",
                  "this work", "this document", "this update", "this model spec"]
STOPWORDS_EN = set(
    """the a an and or but if then than that this these those of to in on for with as by at from
    is are was were be been being it its it's we our us you your they their he she his her i my me
    not no yes can could will would should shall may might must do does did done have has had
    what which who whom when where why how all any both each few more most other some such only
    own same so too very s t just don now about into over under between out up down off above below
    also more very much many one two three new use used using model models""".split()
)
FIRST_PERSON = ["我们", "我", "笔者", "咱"]
OBJ_SELFREF = ["本文", "本研究", "本报告", "本框架", "本篇", "本指南"]
STOPWORDS = set(
    "的 了 和 是 在 我 有 而 对 与 及 其 这 那 一个 我们 你们 他们 它 没有 就是 "
    "可以 因此 但是 因为 如果 那么 以及 或者 然而 并且 不是 什么 这个 那个 这样 "
    "那样 一些 这些 那些 通过 对于 关于 由于 作为 来自 基于 基于 以上 以下 之间 "
    "进行 进行 使用 使用 可能 可能 已经 目前 目前 其中 其中 更多 更多 自己 自己 "
    "一个 一些 比如 例如 然后 因此 所以 不过 其实 还是 只是 也是 都是 说 要 会 被 把 让 向 从 到 为 于 中 上 下".split()
)

# ---------- Markdown 预处理 ----------

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
CODEBLOCK_RE = re.compile(r"```.*?```", re.S)
HTML_TAG_RE = re.compile(r"<[^>]+>")
LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
EMPH_RE = re.compile(r"(\*\*|__|\*|_|~~)`?")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.M)
SENT_SPLIT_RE = re.compile(r"[。！？!?；;]+")
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")
PRECISE_NUM_RE = re.compile(r"\d+\.\d+|\d+%|\d+万|\d+亿|\d+倍")
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
CITE_MARK_RE = re.compile(r"\[\^?\d{1,3}\](?!\()")
CN_NUM_HEADING_RE = re.compile(r"^(第?[一二两三四五六七八九十]+[、.]|[0-9]+(\.[0-9]+)*[\s、.])")


def clean_markdown(raw: str):
    """返回 (prose_text, meta) —— meta 里保留结构计数。"""
    doc = raw
    doc = FRONTMATTER_RE.sub("\n", doc)
    code_blocks = CODEBLOCK_RE.findall(doc)
    doc = CODEBLOCK_RE.sub("\n", doc)
    links = LINK_RE.findall(doc)
    ext_links = [u for _, u in links if u.startswith("http")]
    imgs = [u for f, u in links if f == "" or u.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))]
    headings = [(len(h), t.strip()) for h, t in HEADING_RE.findall(doc)]

    # 表格检测（markdown 管道表）
    tables = len(re.findall(r"^\|.*\|\s*\n\|[-| :]+\|", doc, re.M))

    doc = LINK_RE.sub(r"\1", doc)
    doc = HTML_TAG_RE.sub("", doc)
    doc = EMPH_RE.sub("", doc)

    lines = doc.split("\n")
    # 段落 = 非空行块
    paras, cur = [], []
    for ln in lines:
        s = ln.strip()
        if s:
            cur.append(s)
        elif cur:
            paras.append("\n".join(cur))
            cur = []
    if cur:
        paras.append("\n".join(cur))
    prose = "\n".join(paras)
    meta = {
        "headings": headings,
        "code_blocks": len(code_blocks),
        "tables": tables,
        "external_links": len(ext_links),
        "images": len(imgs),
        "paragraphs": paras,
    }
    return prose, meta, paras


def count_reference_entries(doc_text: str):
    """统计文末『参考』区块条目数。2026-09-06 调优：兼容加粗标题（**参考来源**）与
    修列表项正则（原 `\\[-\\*\\d]+` 为笔误，FDE 类文章 10 条参考被计为 0）。"""
    lines = doc_text.split("\n")
    start = None
    for i, l in enumerate(lines):
        s = l.strip()
        if re.match(r"^#{1,3}\s", s) and re.search(r"参考|引用|来源|References|Sources", s, re.I):
            start = i + 1
            break
        if re.match(r"^\*\*[^*\n]*(参考|引用|来源)[^*\n]*\*\*:?\s*$", s):
            start = i + 1
            break
    if start is None:
        return 0
    tail = []
    for l in lines[start:]:
        s = l.strip()
        if re.match(r"^#{1,3}\s", s) or s in ("---", "***"):
            break
        tail.append(s)
    items = [l for l in tail if re.match(r"^\s*(?:[-*+]\s|\[\^?\d{1,3}\]|\d{1,2}\s*[.、)]\s)", l)]
    return len(items) if items else sum(1 for l in tail if l.strip())


def sentence_stats(prose: str, lang: str = "zh"):
    if lang == "en":
        sents = [s.strip() for s in re.split(r"[.!?]+(?:\s|$)", prose) if s.strip()]
        lens = [len(s.split()) for s in sents]
    else:
        sents = [s.strip() for s in SENT_SPLIT_RE.split(prose) if s.strip()]
        lens = [len(re.findall(r"[\u4e00-\u9fff]", s)) for s in sents]
    lens = [l for l in lens if l > 0]
    if not lens:
        return {}
    qs = sum(1 for s in sents if s.rstrip().endswith(("？", "?")))
    return {
        "sentence_count": len(sents),
        "avg_sentence_len": round(statistics.mean(lens), 1),
        "median_sentence_len": statistics.median(lens),
        "p90_sentence_len": sorted(lens)[int(0.9 * len(lens)) - 1],
        "question_sentences": qs,
    }


def paragraph_stats(paras, lang: str = "zh"):
    unit = (lambda p: len(p.split())) if lang == "en" else (lambda p: len(re.findall(r"[\u4e00-\u9fff]", p)))
    lens = [unit(p) for p in paras]
    lens = [l for l in lens if l > 0]
    if not lens:
        return {}
    # 单句成段只计正文段落：排除 GB/T 式文献条目（"[n] …[J]." 会误命中，见 v10 重跑验证 2026-09-07）
    cite_entry = re.compile(r"^\[\^?\d{1,3}\]\s")
    single = sum(1 for p in paras
                 if not cite_entry.match(p.strip())
                 and len(p) < 40 and p.rstrip().endswith(("。", "！", "？", "；", ":", "：", ".")))
    return {
        "paragraph_count": len(lens),
        "avg_paragraph_len": round(statistics.mean(lens), 1),
        "median_paragraph_len": statistics.median(lens),
        "p90_paragraph_len": sorted(lens)[int(0.9 * len(lens)) - 1],
        "one_line_paragraphs": single,
    }


def term_stats(prose: str, cjk_chars: int, lang: str = "zh"):
    if lang == "en":
        words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]*", prose)]
        content = [w for w in words if w not in STOPWORDS_EN and len(w) >= 3]
        freq = {}
        for w in content:
            freq[w] = freq.get(w, 0) + 1
        top = sorted(freq.items(), key=lambda x: -x[1])[:15]
        return {
            "ttr": round(len(set(words)) / len(words), 3) if words else None,
            "top_terms": [f"{w}×{c}" for w, c in top],
        }
    if not JIEBA or cjk_chars == 0:
        return {"ttr": None, "top_terms": [], "note": "jieba 不可用，跳过词汇指标"}
    words = [w for w in jieba.lcut(prose) if re.search(r"[\u4e00-\u9fff]", w)]
    if not words:
        return {"ttr": None, "top_terms": []}
    content = [w for w in words if w not in STOPWORDS and len(w) >= 2]
    freq = {}
    for w in content:
        freq[w] = freq.get(w, 0) + 1
    top = sorted(freq.items(), key=lambda x: -x[1])[:15]
    return {
        "ttr": round(len(set(words)) / len(words), 3),
        "top_terms": [f"{w}×{c}" for w, c in top],
    }


def match_examples(paras, terms, limit=3):
    """为词表匹配抓取例句（证据链要求）。"""
    hits = []
    for p in paras:
        for t in terms:
            if t in p:
                hits.append({"term": t, "excerpt": p[:80]})
                if len(hits) >= limit:
                    return hits
    return hits


GENRE_RULES = {
    "报告体": lambda first500, text, m: (
        3 if re.search(r"报告日期|数据截止|报告版本|分析对象", first500) else 0
    ) + (1 if re.search(r"^#{1,3}\s*摘\s*要", text, re.M) else 0),
    "期刊体": lambda first500, text, m: (
        2 if re.search(r"^#{1,3}\s*\d*\.?\s*引言", text, re.M) else 0
    ) + (2 if re.search(r"结论与讨论", text) else 0)
    + (2 if len(re.findall(r"\[\d{1,2}\]", text)) >= 5 else 0)
    + (1 if re.search(r"\[(J|C|M|EB/OL|N)\]", text) else 0),
    "行业分析": lambda first500, text, m: (
        2 if re.search(r"编辑说明|信源征集|系列(第[一二三]|[12]/?3)", text) else 0
    ) + (1 if re.search(r"本文将解答|三个问题", text) else 0),
}


def genre_guess(raw_text, headings, prose, meta):
    first500 = prose[:500]
    scores = {g: min(fn(first500, raw_text, meta), 6) for g, fn in GENRE_RULES.items()}
    best = max(scores, key=scores.get)
    if scores[best] < 2:
        return {"genre": "blog_or_exploration", "scores": scores,
                "note": "规则层只可靠识别 报告体/期刊体/行业分析；其余待 LLM 路由（rubric/00-genre-routing.md）"}
    return {"genre": best, "scores": scores, "note": "规则命中"}


def analyze(path: Path, genre_map=None):
    raw = path.read_text(encoding="utf-8", errors="ignore")
    prose, meta, paras = clean_markdown(raw)
    cjk = len(re.findall(r"[\u4e00-\u9fff]", prose))
    word_count = len(re.findall(r"[A-Za-z][A-Za-z'-]*", prose))
    lang = "zh" if cjk >= word_count or (cjk > 500 and word_count < 2000) else "en"
    # 千字/千词归一化分母：中文按字符、英文按词
    norm = cjk if lang == "zh" else word_count
    per_k = lambda n: round(n * 1000 / norm, 2) if norm else 0

    if lang == "zh":
        hedges, absolutists, quantifiers = HEDGES, ABSOLUTISTS, QUANTIFIERS
        first_person, obj_selfref = FIRST_PERSON, OBJ_SELFREF
    else:
        hedges, absolutists, quantifiers = HEDGES_EN, ABSOLUTISTS_EN, QUANTIFIERS_EN
        first_person, obj_selfref = FIRST_PERSON_EN, OBJ_SELFREF_EN

    numbers = NUMBER_RE.findall(prose)
    precise = PRECISE_NUM_RE.findall(prose)
    title_text = next((t for _, t in meta["headings"] if t.strip()), "")

    res = {
        "file": path.name,
        "lang": lang,
        "title": title_text,
        "cjk_chars": cjk,
        "word_count": word_count,
        "reading_time_min": round((cjk if lang == "zh" else word_count) / 300, 0),
        "structure": {
            "h2_count": sum(1 for h, _ in meta["headings"] if h == 2),
            "h3_count": sum(1 for h, _ in meta["headings"] if h == 3),
            "numbered_headings": sum(1 for _, t in meta["headings"] if CN_NUM_HEADING_RE.match(t)),
            "code_blocks": meta["code_blocks"],
            "tables": meta["tables"],
            "images": meta["images"],
            "has_toc": bool(re.search(r"^(目\s*录|Table of Contents|Contents)$", prose, re.M | re.I)),
        },
        "sentences": sentence_stats(prose, lang),
        "paragraphs": paragraph_stats(paras, lang),
        "evidence": {
            "number_tokens": len(numbers),
            "number_per_1k": per_k(len(numbers)),
            "precise_numbers": len(precise),
            "precise_per_1k": per_k(len(precise)),
            "year_anchors": len(YEAR_RE.findall(prose)),
            "year_per_1k": per_k(len(YEAR_RE.findall(prose))),
            "external_links": meta["external_links"],
            "links_per_1k": per_k(meta["external_links"]),
            "citation_marks": len(re.findall(r"\[\^?\d{1,3}\](?!\()", prose)),
            "reference_entries": count_reference_entries(raw),
        },
        "stance": {
            "hedge_hits": per_k(sum(prose.lower().count(t) for t in hedges)),
            "hedge_examples": match_examples(paras, hedges),
            "absolutist_hits": per_k(sum(prose.lower().count(t) for t in absolutists)),
            "absolutist_examples": match_examples(paras, absolutists),
            "quantifier_hits": per_k(sum(prose.lower().count(t) for t in quantifiers)),
            "first_person_count": sum(prose.count(w) for w in first_person) if lang == "zh"
                                  else sum(prose.lower().count(w) for w in first_person),
            "objective_selfref_count": sum(prose.lower().count(w) for w in obj_selfref) if lang == "en"
                                       else sum(prose.count(w) for w in obj_selfref),
            "exclamations": prose.count("！") + prose.count("!"),
            "questions": prose.count("？") + prose.count("?"),
            "emoji": len(re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", prose)),
        },
        "diction": {
            **term_stats(prose, cjk, lang),
            "en_char_ratio": round(len(re.findall(r"[A-Za-z]", prose)) / max(cjk, 1), 3) if lang == "zh" else None,
            "title_text": title_text,
            "title_len": len(title_text),
            "title_has_colon": bool(re.match(r"^[^：:]+[：:]", title_text)),
        },
        "genre": genre_guess(raw, meta["headings"], prose, meta),
    }
    # 人工覆盖层：已发布文章的元信息头可能承载于 HTML 层（md 源稿缺失），路由前以线上 section 为准
    if genre_map and path.name in genre_map:
        res["genre"] = {"genre": genre_map[path.name], "scores": {},
                        "note": "manual_override（线上 section 侧写）", "rule_genre": res["genre"]["genre"]}
    return res


def aggregate(results):
    """语料级基线：数值指标取中位数 + 四分位（防均值被单篇长文拉偏）。"""
    keys = [
        ("cjk_chars",), ("reading_time_min",),
        ("avg_sentence_len", "sentences"), ("p90_sentence_len", "sentences"),
        ("avg_paragraph_len", "paragraphs"),
        ("number_per_1k", "evidence"), ("precise_per_1k", "evidence"),
        ("year_per_1k", "evidence"), ("links_per_1k", "evidence"),
        ("reference_entries", "evidence"), ("citation_marks", "evidence"),
        ("hedge_hits", "stance"), ("absolutist_hits", "stance"), ("quantifier_hits", "stance"),
        ("first_person_count", "stance"), ("objective_selfref_count", "stance"),
        ("exclamations", "stance"), ("questions", "stance"),
        ("ttr", "diction"), ("en_char_ratio", "diction"),
    ]
    def val(r, key, grp):
        try:
            v = r[grp][key] if grp else r[key]
            return v if isinstance(v, (int, float)) else None
        except (KeyError, TypeError):
            return None

    agg = {}
    for spec in keys:
        key, grp = (spec[0], spec[1]) if len(spec) > 1 else (spec[0], "")
        vs = sorted(v for r in results if (v := val(r, key, grp)) is not None)
        if vs:
            agg[key] = {
                "median": round(statistics.median(vs), 2),
                "p25": round(vs[int(0.25 * len(vs))], 2),
                "p75": round(vs[min(int(0.75 * len(vs)), len(vs) - 1)], 2),
                "min": vs[0], "max": vs[-1],
            }
    genres = {}
    for r in results:
        genres.setdefault(r["genre"]["genre"], []).append(r["file"])
    agg["genre_distribution"] = {g: len(fs) for g, fs in sorted(genres.items(), key=lambda x: -len(x[1]))}
    agg["genre_files"] = genres
    return agg


def main():
    ap = argparse.ArgumentParser(description="研究性文章风格统计层")
    ap.add_argument("path", type=Path, help="单个 md 文件或目录")
    ap.add_argument("-o", "--out", type=Path, help="输出 JSON 文件/目录")
    ap.add_argument("--aggregate", type=Path, help="聚合基线输出路径（目录模式）")
    ap.add_argument("--genre-map", type=Path, help="体裁覆盖映射 JSON（{文件名: 体裁}），用于 md 源稿缺元信息头的已发布文章")
    ap.add_argument("--exclude", action="append", default=[],
                    help="排除的文件名 glob（可多次），如 --exclude 'sub-*' 排除投稿")
    args = ap.parse_args()

    if args.out and args.out.suffix != ".json":
        args.out.mkdir(parents=True, exist_ok=True)

    genre_map = {}
    if args.genre_map and args.genre_map.exists():
        genre_map = json.loads(args.genre_map.read_text(encoding="utf-8"))

    import fnmatch
    files = sorted(args.path.glob("*.md")) if args.path.is_dir() else [args.path]
    files = [f for f in files if not any(fnmatch.fnmatch(f.name, pat) for pat in args.exclude)]
    results = []
    for f in files:
        try:
            r = analyze(f, genre_map=genre_map)
            results.append(r)
            if args.out and args.out.suffix == ".json":
                args.out.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
            elif args.out and args.out.is_dir():
                (args.out / f"{f.stem}.json").write_text(
                    json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
        except Exception as e:  # noqa: BLE001 —— 批量模式下单篇失败不中断
            print(f"[skip] {f.name}: {e}", file=sys.stderr)

    if args.out and args.out.suffix != ".json" and results:
        (args.out / "_aggregate.json").write_text(
            json.dumps(aggregate(results), ensure_ascii=False, indent=1), encoding="utf-8")
    if args.aggregate:
        args.aggregate.write_text(
            json.dumps(aggregate(results), ensure_ascii=False, indent=1), encoding="utf-8")
    if not args.out or args.out.suffix != ".json":
        print(json.dumps(results[0] if len(results) == 1 else aggregate(results),
                         ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
