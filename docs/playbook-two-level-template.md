# playbook 两层改造模板（自 kezhongke 试点抽象，2026-09-14）

> 用途：把单层 playbook（定量预算只有全库 median 一层）改造为"机构层不变量 + 体裁 delta"两层结构。
> 试点实例：templates/genre-playbook-kezhongke.md §4（2026-09-14）。方法论依据：docs/methodology-two-level-style-model.md §一/§四。
> 适用对象：其余 7 库 playbook（新建或改造）均可按本清单套用。

## 前置条件（不满足则先补前置，不要跳过）

1. 该库 per-article JSON 已回填 `genre.unified`（llm-routing-v1 或后续版本）；`python3 aggregate_two_level.py [--lib NAME]` 已跑通，`output/<lib>/_aggregate.json` 存在 `two_level` 键。
2. 确认出值格清单（n≥3）：看 `two_level.cells` 的键与 n；n<3 的格一律标"缺席"，不补 0、不套旧印象。
3. `python3 check_profiles.py` 与 `python3 -m unittest discover tests` 全绿后再动笔。

## 改造步骤

1. **机构层预算节**：表格数据源 = `two_level.institution`（数值）+ `two_level.dispersion`（跨体裁 range）+ `two_level.signature_candidates`（不变量候选，起点阈值待校准）。每行标判定：
   - 不变量·硬约束：候选中跨体裁 range 小且方向无格间冲突的（如 kezhongke：句长/P90/absolutist/量词/MATTR/感叹号）；
   - 起点阈值命中但校准为按 delta：range 相对机构值过大的（kezhongke 实例：限定语 range 4.38 vs 机构值 1.42、第一人称 range 13）——候选判定是起点不是终局，校准理由写进行内；
   - 体裁决定（按 delta）：格间方向性差异显著的（kezhongke：数字密度、精确数字、段长、年份、中英字符比）；
   - 只记录：体裁专用或无稳定方向的（外链、参考条目、引文标记）。
2. **差异简注**：列机构层 vs `two_level.corpus_naive_median` 差异最大的指标（相对差 ≥5% 或绝对差显著），每条注构成原因（哪个格、占全库比例、拉偏方向）。kezhongke 实例 top5：限定语 −41%、数字密度 −24%、阅读时长 −13%、篇幅 −12%、段长 −10%。
3. **体裁 delta 节**：delta = 格中位 − 机构层，逐格列表并标 n；每格写 1–2 条写作含义，**含义方向必须与 JSON 数值方向一致**（数字一律代码计算，不手算）；缺席格统一写法："n<3 缺席，写作时暂用机构层 + 人工判断，标 [小样本]"。
4. **留痕**：旧全库口径预算表整体降为"对照节"原样保留（含原口径警示），注明"自改造日起不作硬约束来源"；若旧表口径与当前 JSON 顶层已不一致（如 kezhongke 旧表系 24 篇 v0.1，顶层已是 23 篇重跑口径），一并注明。
5. **行为层不动**：跨语种口径、处方走廊、语步骨架、红线、签名装置原样保留——两层改造只动定量预算的来源与组织。继承性行为纪律（如人称预分配/豁免声明）保留原文，只把数值指向改为两层节。
6. **联动更新**：缺口清单中与 two_level 相关的条目标"部分缓解"（如 MATTR 口径）；方法论文档 §五路线图勾选对应项。

## kezhongke 试点的三个可复用发现形态

- **"默认体裁"形态**：某格占比近半时（A 格 11/23），机构层各指标被该格居中（delta≈0）——这不是没有体裁差异，而是差异集中在非主导格；写作含义应写"非主导格如何偏离默认"。
- **体裁结构性冲高**：N 格数字密度 +97.8/千字 这类量级差，必须进体裁预算而非全库统一区间——这是 _p2 教训（build-log 预算套分析体裁）的正向兑现。
- **人称的体裁极性**：同一指标在不同格方向相反（N 格清零 vs G 格 +6）——凡 range 内出现方向分裂的指标，一律按 delta 执行，不得作机构层硬约束。
