"""两层风格模型聚合层回归测试 · 合成 fixture（不走真实语料）

锁三层纪律（docs/methodology-two-level-style-model.md §一/§二）：
- 机构层 = 体裁格中位的中位，!= 全库朴素中位（体裁构成偏斜时不被主导体裁绑架）
- 格内 n<3 不出格值；空体裁不计 0
- 缺 genre.unified 的篇目跳过且计数（绝不重跑 analyze 回填）
运行：python3 -m unittest discover tests
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import aggregate_two_level as atl  # noqa: E402


def make_article(name, code, sent_len):
    genre = {"genre": "占位"}
    if code is not None:
        genre["unified"] = {"genre": {"E": "工程类", "A": "分析评论类"}[code],
                            "code": code, "confidence": "high",
                            "source": "llm-routing-v1"}
    return {"file": name, "genre": genre,
            "sentences": {"avg_sentence_len": sent_len}}


class TestTwoLevelSkewedFixture(unittest.TestCase):
    """体裁构成偏斜：8 篇 E 格低值 + 2 篇 A 格高值（A 格 n=2 应缺席）。"""

    @classmethod
    def setUpClass(cls):
        cls.articles = (
            [make_article(f"e{i}.md", "E", v)
             for i, v in enumerate([10, 10, 10, 10, 20, 20, 20, 20])]
            + [make_article(f"a{i}.md", "A", 50) for i in range(2)]
        )
        cls.res = atl.two_level(cls.articles)

    # ① 机构层中位 != 全库朴素中位：E 格内中位 15；朴素中位被 2 篇高值拉成 20，
    #    机构层因 A 格缺席而不被其拉高
    def test_institution_not_naive_median(self):
        inst = self.res["institution"]["avg_sentence_len"]
        naive = self.res["corpus_naive_median"]["avg_sentence_len"]
        self.assertEqual(inst, 15.0)
        self.assertEqual(naive, 20.0)
        self.assertNotEqual(inst, naive)

    # ② n<3 的格不出值（A 格 2 篇缺席；空格不计 0）
    def test_small_cell_absent(self):
        self.assertIn("E", self.res["cells"])
        self.assertEqual(self.res["cells"]["E"]["n"], 8)
        self.assertEqual(self.res["cells"]["E"]["metrics"]["avg_sentence_len"], 15.0)
        self.assertNotIn("A", self.res["cells"])
        # 缺席格不进机构层：机构层只有 E 一格输入，离散度 n_cells=1
        self.assertEqual(self.res["dispersion"]["avg_sentence_len"]["n_cells"], 1)

    # ③ 缺 unified 的篇目被跳过且计数正确，不进入任何格
    def test_missing_unified_skipped(self):
        arts = self.articles + [make_article("legacy.md", None, 999)]
        res = atl.two_level(arts)
        self.assertEqual(res["skipped_no_unified"], 1)
        self.assertEqual(res["skipped_files"], ["legacy.md"])
        self.assertEqual(res["n_articles"], 11)
        # 高值离群篇不影响格值与机构层
        self.assertEqual(res["cells"]["E"]["metrics"]["avg_sentence_len"], 15.0)
        self.assertEqual(res["institution"]["avg_sentence_len"], 15.0)


class TestTwoLevelBalancing(unittest.TestCase):
    """两个格都出值时机构层做体裁平衡：7 篇 E=10 + 3 篇 A=50。"""

    def test_institution_median_of_cell_medians(self):
        arts = ([make_article(f"e{i}.md", "E", 10) for i in range(7)]
                + [make_article(f"a{i}.md", "A", 50) for i in range(3)])
        res = atl.two_level(arts)
        # 朴素中位被 E 主导 = 10；机构层 = median(10, 50) = 30
        self.assertEqual(res["corpus_naive_median"]["avg_sentence_len"], 10.0)
        self.assertEqual(res["institution"]["avg_sentence_len"], 30.0)
        self.assertEqual(res["dispersion"]["avg_sentence_len"]["range"], 40.0)
        self.assertEqual(res["dispersion"]["avg_sentence_len"]["n_cells"], 2)


class TestSignatureCandidates(unittest.TestCase):
    """机构签名候选：格内全距 < 跨机构全距一半，且本库 ≥2 个出值格。"""

    def test_candidate_criterion(self):
        per_lib = {
            "lib-stable": {"institution": {"mattr": 0.70},
                           "dispersion": {"mattr": {"range": 0.02, "n_cells": 3}}},
            "lib-varied": {"institution": {"mattr": 0.60},
                           "dispersion": {"mattr": {"range": 0.20, "n_cells": 3}}},
        }
        atl.signature_candidates(per_lib)
        # 跨机构全距 0.10，阈值 0.05：lib-stable 0.02 入选，lib-varied 0.20 出局
        self.assertIn("mattr",
                      per_lib["lib-stable"]["signature_candidates"]["metrics"])
        self.assertNotIn("mattr",
                         per_lib["lib-varied"]["signature_candidates"]["metrics"])

    def test_single_cell_lib_not_candidate(self):
        per_lib = {
            "lib-one-cell": {"institution": {"mattr": 0.70},
                             "dispersion": {"mattr": {"range": 0.0, "n_cells": 1}}},
            "lib-other": {"institution": {"mattr": 0.60},
                          "dispersion": {"mattr": {"range": 0.10, "n_cells": 2}}},
        }
        atl.signature_candidates(per_lib)
        # 单格库无从谈跨体裁不变量，即使 range=0 也不裁决
        self.assertEqual(
            per_lib["lib-one-cell"]["signature_candidates"]["metrics"], {})


if __name__ == "__main__":
    unittest.main()
