# 《Google Research Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：20 篇（2026-09-14 体裁平衡扩容 10→20；原 10 篇：2026-08 至 2026-09，research.google/blog 栏目分层采样）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/google-research/ ｜ 统计：output/google-research/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**机构科学家的"应用研究叙事"**：研究覆盖从基因组预测、果蝇脑连接组到甲烷监测——题材跨学科，但骨架统一：动机（科学问题）→ 方法（模型/管线）→ 量化评估 → 开放展望。命名制双作者署名（"Ayush Jain and Rajat Sen, Research Scientists"）。与 OpenAI 的侦探叙事不同，这里没有"失败→反转"的戏剧弧——是"问题→方案→验证"的正向推进。
⚑ 例证："What if pathology foundation models could do more with less?"（GigaPath——设问式动机开场）

## 2. 量化基线（20 篇，median；2026-09-15 扩容重聚合）· 七库对照表

| 指标 | Cerebras | Eleuther | Databricks | OpenAI | Anthropic | **GoogleRes** | MSR |
|---|---|---|---|---|---|---|---|
| 篇幅（词） | 1,199.5 | 2,106 | 2,476.5 | 1,601.5 | 2,195 | **1,422** | 1,634 |
| 平均句长 | 17.95 | 25.1 | 23.75 | 22.4 | 23.8 | 22.7 | 22.55 |
| 数字密度 /千词 | 33.68 | 41.42 | 24.38 | 17.77 | 8.84 | 15.86 | 19.2 |
| 精确数字 /千词 | 3.09 | 9.86 | 4.0 | 0.9 | 0.6 | 3.01 | 3.42 |
| 限定语 /千词 | 5.54 | 8.8 | 5.28 | 10.16 | 10.52 | **4.56** | 7.22 |
| MATTR(150) | 0.71 | **0.66** | 0.71 | 0.68 | 0.69 | 0.72 | 0.72 |
| 第一人称 | 9.0 | 27.5 | 30.5 | 40 | 30 | **18.0** | 10.0 |
| 年份锚点 /千词 | 1.98 | 1.52 | 0.0 | 1.23 | 0.82 | 1.04 | 0.83 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

> 指纹（discriminate.py，vs 余六库 pooled）：**限定语最低**（4.4 vs 库群 ~8.2，p=0.004，q=0.004，过 FDR）——跨库最"少声明"的稳健叙述，与 Anthropic 的高限定语（10.52）形成两极。**2026-09-14 两层口径复核：体裁构成校正后未过 FDR，但同格方向保持且仍是本库新口径最显著信号**（R 格内限定语 4.19 vs 同格 pooled 10.17，p=0.011，q=0.311，探索性）。**2026-09-15 扩容复核（n=20，FDR 族分列口径不变）**：最显著信号保持限定语低 @R格（4.68 vs pooled 10.01，p=0.011→0.004，q=0.311→0.148——明显收敛），仍未过 FDR；旧口径对照（5b）保持限定语最低（q<0.001 过 FDR，仅对照）。扩容后本库限定语中位 4.4→4.56。

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
- 2026-09-14：两层口径复核（discriminate.py 体裁对体裁改造）。旧指纹"限定语最低"体裁构成校正后未过 FDR（R 格内 p=0.011，q=0.311），但同格方向保持且仍是本库新口径最显著信号（4.19 vs 同格 pooled 10.17），按纪律保留原行并加构成成分注记，扩容后优先复验。
- 2026-09-15：扩容重聚合（Phase B1）。语料 10→20 篇（2026-09-14 体裁平衡扩容，新篇 router=llm-routing-v2-expansion；旧 JSON 未重跑，genre.unified 不受影响）。顶层重算（profiler.aggregate()，等价性双验证通过），§2 表刷新：篇幅 1,462→1,422、句长 22.9→22.7、数字密度 19.7→15.86、精确数字 5.6→3.01、限定语 4.4→4.56、MATTR 0.73→0.72、第一人称 19.5→18.0、年份锚点 1.0→1.04；其余六列同步扩容后口径。two_level：N3/R7 → N5/R13（无新格类）。discriminate（FDR 族分列口径不变）：最显著信号保持限定语低 @R格（4.68 vs pooled 10.01，p=0.011→0.004，q=0.311→0.148），仍未过 FDR；旧口径对照保持限定语最低（q<0.001，仅对照）。