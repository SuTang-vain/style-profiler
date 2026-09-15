"""gen_budgets 预算节生成器 + check_profiles 两层校验回归测试 · 合成 fixture

锁生成器纪律（2026-09-15，templates/ 8 份 playbook AUTO 标记区）：
- 机构层表只重写三个数值列，判定/写作指令人工列逐字保留
- 数值一致（±0.51）的单元格保留原字符串（不产生格式 diff），超容差才重写
- 指标行 JSON 缺席 → 标 `--` 并提示；JSON 有而表格缺 → 追加 待人工判定 行并提示
- 格集合增减 → 显著提示人工复核；--check 模式只报告不写文件
运行：python3 -m unittest discover tests
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import check_profiles as cp  # noqa: E402
import gen_budgets as gb  # noqa: E402


def make_tl():
    return {
        "cells": {
            "A": {"genre": "分析评论类", "n": 3, "metrics": {
                "word_count": 1200, "questions": 3.0, "ttr": 0.4, "mattr": 0.7}},
            "E": {"genre": "工程类", "n": 3, "metrics": {
                "word_count": 800, "questions": 0.0, "ttr": 0.3, "mattr": 0.68}},
        },
        "institution": {"word_count": 1000.0, "questions": 1.5,
                        "ttr": 0.35, "mattr": 0.69},
        "corpus_naive_median": {"word_count": 1100.0, "questions": 1.0,
                                "ttr": 0.36, "mattr": 0.69},
        "dispersion": {
            "word_count": {"range": 400, "iqr": 400, "n_cells": 2},
            "questions": {"range": 3.0, "iqr": 3, "n_cells": 2},
            "ttr": {"range": 0.1, "iqr": 0.1, "n_cells": 2},
            "mattr": {"range": 0.02, "iqr": 0.02, "n_cells": 2},
        },
    }


PLAYBOOK = """## 3. 定量预算

<!-- AUTO:INSTITUTION begin -->
| 指标 | 两层机构值 | 全库朴素 median（对照） | 跨体裁 range | 判定 | 写作指令 |
|---|---|---|---|---|---|
| 篇幅（词） | 999 | 1,100 | 400 | 不变量·硬约束 | 人工写作指令逐字保留 |
| 设问（次/篇） | 1.5 | 1 | 3 | 按 delta | 少量设问 |
<!-- AUTO:INSTITUTION end -->

<!-- AUTO:CELLS begin -->
| 指标 | 机构层 | A 分析评论类（n=3） | E 工程类（n=3） |
|---|---|---|---|
| 篇幅（词） | 1,000 | 1,200（+200） | 800（−200） |
| 设问（次/篇） | 1.5 | 3（+1.5） | 0（−1.5） |
| TTR / MATTR | 0.35 / 0.69 | 0.4 / 0.7（+0.05 / +0.01） | 0.3 / 0.68（−0.05 / −0.01） |
<!-- AUTO:CELLS end -->

<!-- AUTO:LAYOUT begin -->
旧内容
<!-- AUTO:LAYOUT end -->
"""


class GenBudgetsFixtureBase(unittest.TestCase):
    """tmp 根目录：output/fixlib/（_aggregate.json + 3 篇合成篇目）+ 空 templates/。"""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "output" / "fixlib").mkdir(parents=True)
        (root / "templates").mkdir()
        (root / "output" / "fixlib" / "_aggregate.json").write_text(
            json.dumps({"two_level": make_tl()}), encoding="utf-8")
        for i, (t, c) in enumerate([(0, 1), (2, 1), (4, 3)]):
            (root / "output" / "fixlib" / f"a{i}.json").write_text(json.dumps({
                "file": f"a{i}.md", "structure": {"tables": t, "code_blocks": c},
                "genre": {"unified": {"code": "A", "genre": "分析评论类"}},
            }), encoding="utf-8")
        self.root = root
        self._old_libs = dict(gb.LIBS)
        gb.LIBS["fixlib"] = "genre-playbook-fixlib.md"

    def tearDown(self):
        gb.LIBS.clear()
        gb.LIBS.update(self._old_libs)
        self.tmp.cleanup()

    def process(self, text=PLAYBOOK, tl=None):
        return gb.process_playbook(text, tl or make_tl(), "fixlib", self.root)


class TestInstitutionTable(GenBudgetsFixtureBase):
    def test_value_rewrite_and_prose_preserved(self):
        new, report = self.process()
        # 999 超容差 → 规范格式重写为 1,000；朴素 median / range 一致保留原样
        self.assertIn("| 篇幅（词） | 1,000 | 1,100 | 400 | 不变量·硬约束 | "
                      "人工写作指令逐字保留 |", new)
        self.assertTrue(any("篇幅" in c for c in report["changed"]))
        # 全部一致的行整行原样（不改格式）
        self.assertIn("| 设问（次/篇） | 1.5 | 1 | 3 | 按 delta | 少量设问 |", new)

    def test_missing_metric_marks_dash(self):
        tl = make_tl()
        for k in ("institution", "corpus_naive_median", "dispersion"):
            del tl[k]["questions"]
        for cell in tl["cells"].values():
            del cell["metrics"]["questions"]
        new, report = self.process(tl=tl)
        self.assertIn("| 设问（次/篇） | -- | -- | -- | 按 delta | 少量设问 |", new)
        self.assertTrue(any("设问" in m for m in report["missing_rows"]))

    def test_new_metric_appended_for_human_review(self):
        tl = make_tl()
        tl["institution"]["exclamations"] = 0.0
        tl["corpus_naive_median"]["exclamations"] = 0.0
        tl["dispersion"]["exclamations"] = {"range": 0, "iqr": 0, "n_cells": 2}
        new, report = self.process(tl=tl)
        self.assertIn("| 感叹号 | 0 | 0 | 0 | 待人工判定 | 待人工补写 |", new)
        self.assertIn("exclamations", report["appended_rows"])


class TestDeltaTable(GenBudgetsFixtureBase):
    def test_matching_cells_kept_verbatim(self):
        new, report = self.process()
        # 合并行与单行数值一致 → 原字符串保留（格式不规整化）
        self.assertIn("| TTR / MATTR | 0.35 / 0.69 | 0.4 / 0.7（+0.05 / +0.01） | "
                      "0.3 / 0.68（−0.05 / −0.01） |", new)
        self.assertIn("| 设问（次/篇） | 1.5 | 3（+1.5） | 0（−1.5） |", new)
        self.assertFalse(report["cell_set_change"])

    def test_delta_recompute(self):
        tl = make_tl()
        tl["cells"]["A"]["metrics"]["questions"] = 5.0  # delta 1.5 → 3.5
        new, report = self.process(tl=tl)
        self.assertIn("| 设问（次/篇） | 1.5 | 5（+3.5） | 0（−1.5） |", new)

    def test_cell_set_change_warns(self):
        tl = make_tl()
        tl["cells"]["N"] = {"genre": "公告类", "n": 3, "metrics": {
            "word_count": 900, "questions": 1.0, "ttr": 0.33, "mattr": 0.7}}
        new, report = self.process(tl=tl)
        self.assertIn("N", report["cell_set_change"])
        self.assertIn("N 公告类（n=3）", new)  # 新格入列
        self.assertIn("| 设问（次/篇） | 1.5 | 3（+1.5） | 0（−1.5） | 1（−0.5） |",
                      new)
        # 格消失同样提示
        tl2 = make_tl()
        del tl2["cells"]["E"]
        _, report2 = self.process(tl=tl2)
        self.assertIn("E", report2["cell_set_change"])

    def test_uncovered_metric_noticed_not_added(self):
        tl = make_tl()
        tl["institution"]["exclamations"] = 0.0
        tl["corpus_naive_median"]["exclamations"] = 0.0
        tl["dispersion"]["exclamations"] = {"range": 0, "iqr": 0, "n_cells": 2}
        _, report = self.process(tl=tl)
        self.assertIn("exclamations", report["cells_uncovered"])


class TestRunModes(GenBudgetsFixtureBase):
    def test_check_mode_reports_drift_without_writing(self):
        pb = self.root / "templates" / "genre-playbook-fixlib.md"
        pb.write_text(PLAYBOOK, encoding="utf-8")
        drift = gb.run_lib(self.root, "fixlib", check=True)
        self.assertTrue(drift)  # 篇幅 999 与 JSON 不符 = 漂移
        self.assertEqual(pb.read_text(encoding="utf-8"), PLAYBOOK)  # 未写文件
        # 写入模式落盘；再 check 无漂移（幂等）
        gb.run_lib(self.root, "fixlib")
        self.assertIn("| 篇幅（词） | 1,000 |", pb.read_text(encoding="utf-8"))
        self.assertFalse(gb.run_lib(self.root, "fixlib", check=True))

    def test_layout_generated_from_structure(self):
        pb = self.root / "templates" / "genre-playbook-fixlib.md"
        pb.write_text(PLAYBOOK, encoding="utf-8")
        gb.run_lib(self.root, "fixlib")
        new = pb.read_text(encoding="utf-8")
        self.assertNotIn("旧内容", new)
        # 全库 median：tables [0,2,4]→2，code_blocks [1,1,3]→1；A 格 n=3 同为该值
        self.assertIn("| 表格（个/篇） | 2 | 2 | -- |", new)
        self.assertIn("| 代码块（个/篇） | 1 | 1 | -- |", new)


class TestCheckProfilesTwoLevelIntegration(unittest.TestCase):
    """真实仓库集成断言：8 库 playbook AUTO 区逐格回核 two_level JSON 全过。"""

    def test_all_libs_two_level_pass(self):
        import os
        os.chdir(ROOT)  # check_profiles 现有路径约定为仓库根相对
        for lib in cp.LIBS:
            checked, fails, skipped, err = cp.check_two_level(lib)
            self.assertIsNone(err, f"{lib}: {err}")
            self.assertGreater(checked, 0, f"{lib}: 未校验任何值")
            self.assertEqual(fails, [], f"{lib}: {fails}")


if __name__ == "__main__":
    unittest.main()
