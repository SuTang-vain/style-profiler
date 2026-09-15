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

## 预算节再生成流程（2026-09-15 起，gen_budgets.py）

8 份 playbook 的 §x.1 机构层表 / §x.2 delta 表已由 **AUTO 标记区生成器化**，聚合层重跑后不再手工刷新数值：

**标记约定**（8 份 playbook 均已插入）：
- `<!-- AUTO:INSTITUTION begin/end -->` 包住机构层表（表头+全部行）。生成器按行首指标名关键词扫描匹配 two_level 指标键，**只重写「两层机构值 / 全库朴素 median / 跨体裁 range」三列**；「判定」「写作指令」两列人工 prose 逐字保留。指标行在 JSON 缺席 → 数值列标 `--` 并 stdout 提示；JSON 有而表格缺 → 追加行（判定列 `待人工判定`）并 stdout 提示。
- `<!-- AUTO:CELLS begin/end -->` 包住 delta 表整表。格值（±delta）= two_level.cells − institution，代码计算；格集合（列）不变时保留现有行序/列序与既有数字格式，增减时整表按 JSON 列序重建。
- `<!-- AUTO:LAYOUT begin/end -->`（紧随 AUTO:CELLS 之后）为「排版（参考，非硬约束）」小节：structure.tables / code_blocks 逐篇 JSON 实算全库 median + 各出值格 median。
- 标记区外内容（差异简注 blockquote、人称硬约束、分体裁写作含义、§x.3 留痕表、叙事段占比参考行等）一律不动。

**命令**：
```
python3 gen_budgets.py            # 全部 8 库，重写 AUTO 区并打印变更报告
python3 gen_budgets.py --lib NAME # 单库
python3 gen_budgets.py --check    # 只报告漂移不写文件（退出码 0=无漂移）
python3 check_profiles.py         # STYLE-PROFILE 校验 + 两层 AUTO 区逐格回核（两层合计单列）
```

**格集合变更（新格出值 / 旧格消失）时的人工复核点**（生成器 stdout 会以 ⚠️ 显著提示）：
1. §x.1「判定」列：新进格可能改变 range 与签名候选命中关系，逐行复核判定档位；
2. §x.2「分体裁写作含义」prose：新格补条目、消失格删引用；
3. 机构层表追加的 `待人工判定` 行：人工填判定与写作指令后保留（生成器下轮按行键匹配，不会覆盖）；若确认该指标不入表（如英文库 cjk_chars 恒 0），删行即可——生成器下轮会再次追加并提示，属已知行为；
4. 差异简注 blockquote：对照生成器 stdout 打印的 top-N 相对差异清单，核对现有简注是否仍成立（不重写，人工更新）。

kezhongke 中文口径特判：篇幅行 = cjk_chars（篇幅（中文字符）），word_count 键视为已覆盖，不触发追加行（SUPPRESS_APPEND）。
