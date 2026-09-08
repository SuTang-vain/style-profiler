# 《Google Research Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2026-08 至 2026-09，research.google/blog 栏目分层采样）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/google-research/ ｜ 统计：output/google-research/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**机构科学家的"应用研究叙事"**：研究覆盖从基因组预测、果蝇脑连接组到甲烷监测——题材跨学科，但骨架统一：动机（科学问题）→ 方法（模型/管线）→ 量化评估 → 开放展望。命名制双作者署名（"Ayush Jain and Rajat Sen, Research Scientists"）。与 OpenAI 的侦探叙事不同，这里没有"失败→反转"的戏剧弧——是"问题→方案→验证"的正向推进。
⚑ 例证："What if pathology foundation models could do more with less?"（GigaPath——设问式动机开场）

## 2. 量化基线（10 篇，median）· 七库对照表

| 指标 | Cerebras | Eleuther | Databricks | OpenAI | Anthropic | **GoogleRes** | MSR |
|---|---|---|---|---|---|---|---|
| 篇幅（词） | 1,313 | 2,772 | 2,076 | 3,164 | 2,640 | **1,462** | 1,634 |
| 平均句长 | 18.8 | 25.7 | 26.1 | 22.3 | 22.4 | 22.9 | 22.6 |
| 数字密度 /千词 | 40.1 | 44.1 | 24.4 | 20.7 | 8.25 | 19.7 | 26.9 |
| 精确数字 /千词 | 3.1 | 14.1 | 4.0 | 0.9 | 1.5 | 5.6 | 7.5 |
| 限定语 /千词 | 7.9 | 10.6 | 5.5 | 9.6 | 10.52 | **4.4** | 7.5 |
| MATTR(150) | 0.70 | **0.65** | 0.71 | 0.68 | 0.69 | 0.73 | 0.70 |
| 第一人称 | 10.5 | 61.5 | 21.5 | 53.0 | 30.0 | 19.5 | 9.0 |
| 年份锚点 /千词 | 2.0 | 1.2 | 0.5 | 1.2 | 0.6 | 1.0 | 0.9 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

> 指纹（discriminate.py，vs 余六库 pooled）：**限定语最低**（4.4 vs 库群 ~8.2，p=0.004，q=0.004，过 FDR）——跨库最"少声明"的稳健叙述，与 Anthropic 的高限定语（10.52）形成两极。

## 3. 结构信号（rubric 01 全量标注：connectomics 篇，27 段 → 15 标注）

- **语步骨架**：FRAME（成果声明前置）→ CONTEXT → ARGUE×6（数据锚定+图注）→ CONTEXT → ARGUE×2 → APPLY×2（推广：鱼类/斑马鱼）→ ARGUE → CLOSE（愿景）
- 特征：**零叙事、零 COUNTER**——无失败/反转弧，无反方观点；正向"成果→方法→推广"推进；
- **图注段 4/15 为 ARGUE 证据**（图形证据占比高，同 EleutherAI 文体）；
- **APPLY 是合作科学体的扩展轴**——"已经推广到 XX"（鱼类→斑马鱼→鼠）而非 OpenAI 式的"教训"或 Cerebras 式的"教程"；
- 完整标注：`output/google-research/annotations/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain.moves.jsonl`

> **3 篇聚合修正（2026-09-08）**：timesfm-3 + empty-shelves 聚合后出现设问 HOOK（"is it because they never learned them or..."）——connectomics 单篇的"无 HOOK"仅对成果发布文子类成立。详见 `output/_moves-aggregate.md`。

## 4. 待人工裁决项

- ⚑ 与壳中客"探索体"的对照：行星预测引擎/GlucoFM 等"模型+科学应用"文是否构成英文"应用报告体"；
- connectomics 篇已全量语步标注（其余 9 篇待标）；
- "机构合作科学体"（institutional-collaboration-science）信号在本库最强——零叙事+图注驱动+APPLY 扩展轴的组合是否升为 rubric 00 英文子体裁待定。

## 5. 语料清单

transfer-learning-genomic-prediction / connectomics-fruit-fly / methane-emissions / timesfm-3 / planetary-prediction-engine / glucofm / agenthands / biomarkers-wearable / mobility-place / empty-shelves-recall

## 6. 校准日志

- 2026-09-08：跨库数值同步（逐格对照 output/ 各库单篇 JSON 及 _aggregate.json，统计层以 JSON 为准）。① 篇幅行改用单篇 JSON 重算 median：OpenAI 2,819→3,164、Anthropic 2,622→2,640、MSR 1,673→1,634（本库 1,462 复核一致未变）；② OpenAI/Anthropic 两列系 v2 重采口径：MATTR "待重采†" 补 0.68/0.69 并删 † 注记，OpenAI 平均句长 22.1→22.3、数字密度 16.1→20.7、精确数字 1.1→0.9、限定语 8.8→9.6、第一人称 59.0→53.0、年份锚点 2.0→1.2；Anthropic 数字密度 7.4→8.25、精确数字 1.6→1.5、限定语 9.6→10.52、第一人称 42.5→30.0、年份锚点 0.3→0.6（平均句长 22.4 复核一致未变）；③ 既有漂移修正（与本次重采无关）：Cerebras MATTR 0.71→0.70、Databricks MATTR 0.72→0.71、MSR 平均句长 22.8→22.6、数字密度 26.6→26.9、精确数字 7.3→7.5、限定语 7.4→7.5；④ 散文修正：指纹行 p/q 0.005→0.004（与重算后 _group-discrimination.txt 一致）、库群对照 ~7.9→~8.2（余六库 60 篇 hedge_hits pooled median 8.19）、Anthropic 高限定语 9.6→10.52。本库（GoogleRes）列逐格核对与 google-research/_aggregate.json 一致，未改。