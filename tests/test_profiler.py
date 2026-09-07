"""style-profiler 回归测试 · 锁行为与关系，不锁绝对数值

断言设计原则（对应加固计划 ①a）：
- golden 数值断言仅用于已锁死修复史的项目（如 reference_entries 正则修复）
- 语料会漂移，语料级断言只用关系/上下界（序、median、上限）
- 标 expectedFailure 的是已知 bug 的失败哨兵，修复后转正
运行：python3 -m unittest discover tests（零依赖；jieba 缺失时词汇类测试自动 skip）
"""
import json
import statistics
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import profiler  # noqa: E402

CORPUS = ROOT / "corpus" / "kezhongke"
GENRE_MAP_PATH = CORPUS / "genre-map.json"


def analyze_corpus():
    """跑 v10 语料全量（genre-map 覆盖 + 规则层兜底），返回 {文件名: 结果}。"""
    genre_map = json.loads(GENRE_MAP_PATH.read_text(encoding="utf-8"))
    return {f.name: profiler.analyze(f, genre_map=genre_map)
            for f in sorted(CORPUS.glob("*.md"))}


def genre_of(name, res):
    gm = json.loads(GENRE_MAP_PATH.read_text(encoding="utf-8"))
    return gm.get(name, res["genre"]["genre"])


@unittest.skipUnless(CORPUS.is_dir(), "corpus/kezhongke 不在仓")
class TestKezhongkeGolden(unittest.TestCase):
    """v10 语料（10 篇，五体裁各 2）上的 golden / 关系断言。"""

    @classmethod
    def setUpClass(cls):
        cls.results = analyze_corpus()

    def test_10_articles(self):
        self.assertEqual(len(self.results), 10)

    # 断言 1（修正版）：emoji 全库为 0；感叹号中位数 0 且有界
    # —— 验证报告 #1/#2 的口径是 median=0 / max=2，非全库为 0
    def test_no_emoji_exclamation_bounded(self):
        emojis = [r["stance"]["emoji"] for r in self.results.values()]
        excls = [r["stance"]["exclamations"] for r in self.results.values()]
        self.assertTrue(all(e == 0 for e in emojis), f"emoji 非零: {emojis}")
        self.assertEqual(statistics.median(excls), 0)
        self.assertLessEqual(sum(excls), 4, f"感叹号总量越界: {sum(excls)}")

    # 断言 2：修复史锁定——加粗标题参考节正则修复后 fde-role-renaissance == 10
    def test_fde_reference_entries(self):
        self.assertEqual(
            self.results["fde-role-renaissance.md"]["evidence"]["reference_entries"], 10)

    def _by_genre(self, key_path):
        groups = {}
        for name, r in self.results.items():
            g = genre_of(name, r)
            v = r
            for k in key_path:
                v = v[k]
            groups.setdefault(g, []).append(v)
        return groups

    # 断言 3：报告体数字密度 > 行业分析（验证报告 #3：111.55 vs 10.22）
    def test_report_number_density_gt_industry(self):
        groups = self._by_genre(("evidence", "number_per_1k"))
        self.assertGreater(statistics.mean(groups["报告体"]),
                           statistics.mean(groups["行业分析"]))

    # 断言 4：报告体限定语 > 期刊体（验证报告 #4：5.79 vs 3.1）
    def test_report_hedge_gt_journal(self):
        groups = self._by_genre(("stance", "hedge_hits"))
        self.assertGreater(statistics.mean(groups["报告体"]),
                           statistics.mean(groups["期刊体"]))

    # 断言 5：断言型 absolutist < 全称量词 quantifier（调优点 1 拆分后的正确序）
    def test_absolutist_lt_quantifier(self):
        absol = [r["stance"]["absolutist_hits"] for r in self.results.values()]
        quant = [r["stance"]["quantifier_hits"] for r in self.results.values()]
        self.assertLess(statistics.median(absol), statistics.median(quant))

    # 体裁路由自检：规则层应识别两篇报告体（genre-map 有意不覆盖）
    def test_rule_layer_genre_routing(self):
        gm = json.loads(GENRE_MAP_PATH.read_text(encoding="utf-8"))
        for name in ("deepseek-v4-analysis.md", "glm-5-3-analysis.md"):
            self.assertNotIn(name, gm)
            self.assertEqual(self.results[name]["genre"]["genre"], "报告体")


class TestFixtures(unittest.TestCase):
    """自写小文本的行为契约（无版权问题）。"""

    def _analyze(self, text, name="fixture.md"):
        self._tmp = tempfile.TemporaryDirectory()
        p = Path(self._tmp.name) / name
        p.write_text(text, encoding="utf-8")
        return profiler.analyze(p)

    # 断言 6：单句成段不计 [n] GB/T 文献条目（v10 重跑修复）
    def test_citation_entries_not_one_line_paragraphs(self):
        r = self._analyze(
            "这是正文段落，长度必须足够长，超过四十个字符的阈值，"
            "才不会被单句成段统计计入，此处满足。\n\n"
            "[1] 张三. 某某研究[J]. 某学报, 2024.\n\n"
            "[2] 李四. 另一研究[J]. 某学报, 2023.\n")
        self.assertEqual(r["paragraphs"]["one_line_paragraphs"], 0)

    # 断言 7：中文句长按汉字计，英文按词计
    def test_sentence_length_units(self):
        zh = self._analyze("一二三四五。六七。")
        self.assertEqual(zh["sentences"]["avg_sentence_len"], 3.5)
        en = self._analyze("one two three four. five six.")
        self.assertEqual(en["sentences"]["avg_sentence_len"], 3.0)

    # 断言 8a：小数点不断句（中/英）
    def test_decimal_not_sentence_boundary(self):
        zh = self._analyze("圆周率是3.14，这是一个常数。另一个句子在这。")
        self.assertEqual(zh["sentences"]["sentence_count"], 2)
        en = self._analyze("Llama 3.1 8B is large. It performs well.")
        self.assertEqual(en["sentences"]["sentence_count"], 2)

    # 断言 8b：frontmatter 剔除
    def test_frontmatter_stripped(self):
        r = self._analyze("---\ntitle: 测试\nwords: 9999\n---\n正文只有这一句。")
        self.assertEqual(r["cjk_chars"], 7)

    # 断言 8c：--exclude 生效（CLI 层）
    def test_exclude_glob(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            (d / "keep.md").write_text("正常文章一句。", encoding="utf-8")
            (d / "sub-abc123.md").write_text("投稿一句。", encoding="utf-8")
            out = d / "out"
            subprocess.run(
                [sys.executable, str(ROOT / "profiler.py"), str(d),
                 "-o", str(out), "--exclude", "sub-*"],
                check=True, capture_output=True)
            files = {f.name for f in out.glob("*.json")}
            self.assertIn("keep.json", files)
            self.assertNotIn("sub-abc123.json", files)

    # 断言 9：聚合用 median，单篇长文不拉偏
    def test_aggregate_uses_median(self):
        results = [
            {"cjk_chars": n, "genre": {"genre": "博客体"}, "file": f"f{i}.md",
             "sentences": {"avg_sentence_len": 20.0}}
            for i, n in enumerate([1000, 1100, 1200, 50000])
        ]
        agg = profiler.aggregate(results)
        # 偶数样本 median = 中间两值均值 = 1150；mean 会被拉到 13325
        self.assertEqual(agg["cjk_chars"]["median"], 1150.0)
        self.assertEqual(agg["cjk_chars"]["max"], 50000)

    # 断言 10（失败哨兵，② 修复后转正）：
    # "约束/大约" 等词内的 "约" 不得计入 hedge；jieba token 精确匹配后本测试转绿
    @unittest.expectedFailure
    def test_hedge_substring_no_contamination(self):
        text = "约束机制正在约束模型，这是约束条件。另外提到大约十人。"
        prose = text
        hits = sum(prose.count(t) for t in profiler.HEDGES)
        # 期望：只有 "大约" 1 次命中；"约束" 中的 3 个 "约" 不计
        self.assertEqual(hits, 1)

    # 断言 10b（失败哨兵）："最初/最终" 的 "最" 不得计入 quantifier
    @unittest.expectedFailure
    def test_quantifier_substring_no_contamination(self):
        text = "最初的想法最终被放弃，这是一次最好的实践。"
        hits = sum(text.count(t) for t in profiler.QUANTIFIERS)
        self.assertEqual(hits, 1)

    # 断言 11（TTR 长度污染哨兵）：③ 引入 MATTR 后转正为
    # "同一文本截长/截短时 mattr 稳定而 ttr 漂移"的等长窗口比较测试。
    # 当前仅记录：实测 eleuther vs databricks 的 TTR 差距 0.204，
    # 等长窗口（MATTR w=150）后缩至 0.070，缩水约 66%。


@unittest.skipUnless(profiler.JIEBA, "jieba 不可用，跳过中文词汇指标测试")
class TestJiebaDependent(unittest.TestCase):
    def test_zh_ttr_present(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "zh.md"
            p.write_text("研究方法需要可重复。研究设计应当透明。研究结果必须可证伪。" * 5,
                         encoding="utf-8")
            r = profiler.analyze(p)
            self.assertIsNotNone(r["diction"]["ttr"])
            self.assertGreater(r["diction"]["ttr"], 0)


if __name__ == "__main__":
    unittest.main()
