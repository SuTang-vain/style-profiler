#!/usr/bin/env python3
"""Anthropic 文章页抓取器：SSR HTML → 与 corpus/anthropic/ 现有格式一致的纯文本 markdown。

用法: python3 scripts/fetch_anthropic.py <url> [out.md]
格式约定（模仿现有语料）:
  # <Title>
  <Section label>      （subjects 标签，如 Announcements / Engineering at Anthropic）
  <Title>
  Published <Mon DD, YYYY>
  <正文：标题/段落/列表项一律平铺为单行，段间空行>
只落本地 corpus/，不入 git。
"""
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36")

SKIP_TEXTS = {"Read more", "Related content"}


def fetch_html(url: str) -> str:
    return subprocess.run(
        ["curl", "-sL", "-A", UA, url], capture_output=True, text=True, check=True
    ).stdout


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def extract(url: str) -> str:
    soup = BeautifulSoup(fetch_html(url), "html.parser")
    article = max(soup.select("article"), key=lambda e: len(e.get_text()), default=None)
    if article is None:
        raise SystemExit(f"no <article> found: {url}")

    # 去掉 Related content 推荐卡片等非正文块
    for junk in article.find_all(True, class_=re.compile(r"LinkGrid|LandingPageSection|RelatedContent|Footer")):
        junk.decompose()

    # 头部元信息
    subj = article.select_one('[class*="PostDetail"][class*="subjects"]') or article.select_one('[class*="subjects"]')
    h1 = article.select_one("h1")
    title = norm(h1.get_text()) if h1 else norm(soup.title.get_text().split("\\")[0])
    category = norm(subj.get_text(separator=", ")) if subj else ""
    date = ""
    for d in article.select('[class*="agate"], [class*="date"], time'):
        t = norm(d.get_text())
        if re.match(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)", t):
            date = t
            break
    if not date:
        m = re.search(r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, 20\d\d)", article.get_text())
        date = m.group(1) if m else ""

    # 正文块：h2/h3/p/li/blockquote 按文档序平铺
    header = article.select_one('[class*="PostDetail"][class*="header"]')
    body_root = article
    lines = []
    for el in body_root.find_all(["h2", "h3", "h4", "p", "li", "blockquote"]):
        if header and header in el.parents:
            continue
        if el.find_parent(["table"]):
            continue
        if el.name == "li" and el.find_parent("li"):
            continue
        t = norm(el.get_text())
        if not t or t in SKIP_TEXTS:
            continue
        if t == title or t == category:
            continue
        if el.name == "li":
            t = re.sub(r"^[-•*]\s*", "", t)
        lines.append(t)

    # 去掉尾部 Related content 之后的推荐块（若漏网）
    out = []
    seen_related = False
    for t in lines:
        if t == "Related content":
            seen_related = True
            continue
        if seen_related:
            continue
        out.append(t)

    parts = [f"# {title}", ""]
    if category:
        parts.append(category)
    parts += [title, ""]
    parts.append(f"Published {date}" if date else "")
    parts.append("")
    parts += [t for t in out]
    text = "\n\n".join(parts)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


if __name__ == "__main__":
    url = sys.argv[1]
    text = extract(url)
    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(text)
        print(f"wrote {sys.argv[2]}: {len(text)} chars", file=sys.stderr)
    else:
        print(text)
