"""discriminate.py 两层口径回归测试 · 合成 fixture（不走真实语料）

锁体裁对体裁纪律（docs/methodology-two-level-style-model.md §三）：
- 只在共享体裁格之间比较；非共享格上的差异不参与任何检验
- FDR 族 = 体裁格，各族内分别 BH 校正
- 指纹 pooled = 同体裁格内其余各库篇目合并（无该格的库不进 rest）
运行：python3 -m unittest discover tests
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import discriminate as disc  # noqa: E402


def make_cells():
    """libA/libB 共享 R 格（有差异）；libA 独有的 E 格与 libC 差异更大（非共享）。"""
    return {
        "libA": {"R": {"mattr": [0.60, 0.61, 0.62], "word_count": [1000, 1100, 1200]},
                 "E": {"mattr": [0.90, 0.91, 0.92]}},
        "libB": {"R": {"mattr": [0.80, 0.81, 0.82], "word_count": [1000, 1100, 1200]}},
        "libC": {"E": {"mattr": [0.30, 0.31, 0.32]}},
    }


class TestCellPairwise(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.families = disc.cell_pairwise(make_cells())

    # 共享格差异进入比较：R 格含 libA×libB 且 mattr 差异显著
    def test_shared_cell_compared(self):
        r = self.families["R"]
        self.assertIn(("mattr", "libA", "libB"), r)
        self.assertLess(r[("mattr", "libA", "libB")], 0.05)
        # 同格无差异指标不显著
        self.assertGreater(r[("word_count", "libA", "libB")], 0.05)

    # 非共享格差异不参与跨格比较：E 格只有 libA×libC；libB 无 E 格不出现
    def test_non_shared_cell_excluded(self):
        e = self.families["E"]
        libs_in_e = {l for (_, a, b) in e for l in (a, b)}
        self.assertEqual(libs_in_e, {"libA", "libC"})
        self.assertNotIn("libB", libs_in_e)
        # libA vs libB 在 E 格上差异最大，但无此检验键
        self.assertNotIn(("mattr", "libA", "libB"), e)

    # FDR 族分列：R/E 各自成族，族内校正互不稀释
    def test_families_split_by_genre(self):
        # R 族只含 R 格检验（2 指标 × 1 对），E 格检验不在其中
        self.assertEqual(len(self.families["R"]), 2)
        self.assertEqual(len(self.families["E"]), 1)
        key = ("mattr", "libA", "libB")
        p = self.families["R"][key]
        q_split = disc.bh_fdr(self.families["R"])[key]
        # 族内校正：m = R 族检验数 2（而非含 E 族的 3）——q = p × 2/1
        self.assertAlmostEqual(q_split, min(p * 2, 1.0), places=6)


class TestCellFingerprint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fp = disc.cell_fingerprint(make_cells())

    # 指纹检验在共享格上做：libA 的 R 格指纹存在
    def test_fingerprint_on_shared_cell(self):
        self.assertIn(("libA", "R", "mattr"), self.fp)
        self.assertLess(self.fp[("libA", "R", "mattr")]["p"], 0.05)

    # pooled = 同格其余各库合并：libC 的 E 格指纹 rest 只含 libA（libB 无 E 格）
    def test_pooled_excludes_libs_without_cell(self):
        e = self.fp[("libC", "E", "mattr")]
        self.assertEqual(e["n_rest"], 3)  # 仅 libA 的 3 篇，libB 不进入
        r = self.fp[("libA", "R", "mattr")]
        self.assertEqual(r["n_rest"], 3)  # 仅 libB 的 3 篇

    # 无共享格的库不出指纹：libC 只有 E 格且 libA 有 E——有指纹；
    # 若 libA 无 E 格则 libC 无任何指纹键
    def test_no_shared_cell_no_fingerprint(self):
        cells = make_cells()
        del cells["libA"]["E"]
        fp = disc.cell_fingerprint(cells)
        self.assertFalse(any(l == "libC" for (l, g, k) in fp))


if __name__ == "__main__":
    unittest.main()
