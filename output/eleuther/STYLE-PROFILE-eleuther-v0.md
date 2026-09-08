# 《EleutherAI Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2024-08 至 2026-07，研究深潜 + research-update 混合）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/eleuther/ ｜ 统计：output/eleuther/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**非营利社区的"论文化博客"**：多作者署名（两位起，最多五人）继承论文作者制；把研究过程本身当作内容——包括 research update 式的"进行中报告"。数字精确癖全库最强（精确数字 14.1/千词，是 OpenAI 的 15 倍）：每个定性判断配一个具体测量。人称"we"密度甚至超过 OpenAI（61.5 vs 53）——但这里的 we 是研究共同体而非侦探叙事主体。
⚑ 例证："The outcome thus depends on competing quantities - advanced AI will be better at evading m…"（dynamical-models——理论建构+数量关系陈述）

## 2. 量化基线（10 篇，median）· 六库对照表

| 指标 | Cerebras | **EleutherAI** | Databricks | OpenAI | Anthropic | 壳中客(中·v10) |
|---|---|---|---|---|---|---|
| 篇幅（词/字） | 1,313 | **2,772** | 2,076 | 3,164 | 2,640 | 4,830 字 |
| 平均句长（词/字） | 18.8 | **25.7** | 26.2 | 22.3 | 22.5 | 34.5 字 |
| 数字密度 /千词(字) | 40.1 | **44.1** | 24.4 | 20.7 | 8.25 | 17.1 |
| 精确数字 /千词(字) | 3.1 | **14.1** | 4.0 | 0.92 | 1.46 | 5.6 |
| 限定语 /千词(字) | 7.9 | **10.6** | 5.5 | 9.6 | 10.52 | 2.69† |
| 断言绝对化 /千词(字) | 1.82 | 1.2 | 1.1 | 1.76 | 2.32 | 1.08 |
| 第一人称 | 10.5 | **61.5** | 21.5 | 53.0 | 30.0 | 6.0 |
| 客观自指 | 0.5 | 1.5 | 0.0 | 1.0 | 1.5 | 2.0 |
| 外链 /千词(字) | 0 | 0 | 0 | 0 | 0 | 0 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 |
| TTR | 0.42 | **0.26** | 0.46 | 0.33 | 0.34 | 0.35 |
| MATTR（w=150） | 0.70 | **0.65** | **0.71** | 0.68 | 0.69 | 0.74 |
| **指纹**（discriminate.py，vs 余六库 pooled） | — | **MATTR 最低**（0.65 vs ~0.70，p<0.001，q<0.001，过 FDR） | — | — | — | — |

> 指纹解读（2026-09-07 更新）：TTR 差距经等长窗口校正后缩水约 2/3（0.204→0.070）但序保持——EleutherAI 仍是词汇复用最密集的"论文化博客"，术语循环是文体成分而非纯篇幅效应；原"精确数字最高"指纹（14.1 vs ~3.0，q<0.05）依然成立但退居次显著。
> † 壳中客列整体为 v10 口径（2026-09-07 词表修复后；限定语原 v0.1 值 4.8 含"约→约束"子串污染）。

## 3. 结构信号（rubric 01 全量标注：mad_research_update_2，47 段 → 39 标注）

- **语步骨架**：FRAME → ARGUE×33 → CLOSE（ARGUE 占标注段 85%——纯实验报告文体）
- 特征：**无 HOOK、无 COUNTER、无 APPLY**；CONTEXT 仅 1 处（实验设计变更）；**零叙事**（narrative 占比 0%）——"我们做了什么、测得什么"直陈到底；
- 结构标点：结果前置（P8 摘要型结果段）→ 分节实验（方法→结果→图注）→ 边界声明（"unclear if this is a robust relationship"）→ 负面收束（"deprioritising" + "may revisit"）；
- **图注段 13 处**（全段落 1/3）——图形证据是论证主体，文本是图的注释；
- **对照修正**：本文件为"研究进度报告"而非探索体英文版——无概念自造、无版本号（探索体核心信号在 dynamical-models 等理论文）。
  探索体英文对应物应改寻他篇；rubric 00 若扩展，宜命名英文第五子体裁为 research-report（进度报告体）；
- 完整标注：`output/eleuther/annotations/mad_research_update_2.moves.jsonl`

> **3 篇聚合（2026-09-08）**：autointerp + common-pile 补齐后 ARGUE 83%、叙事 0%——"纯论证"画像稳固；common-pile 含质疑-回应单元（性能质疑→对比回应）。详见 `output/_moves-aggregate.md`。

## 4. 待人工裁决项

- ⚑ 探索体英文对应物的定位：mad_research_update_2 实证为 research-report（进度报告），非探索体；探索体信号应在 dynamical-models（理论建构）等篇验证；
- 巨文 dynamical-models（113KB）对 median 的影响（句长/篇幅指标），是否该篇单独分组；
- 语步全量标注已完成 1 篇（mad_research_update_2），其余 9 篇待标注。

## 5. 语料清单

aletheia-retrospective / dynamical-models-of-ai-governability / reward-hacking-indicators / deep-ignorance / attention-probes / common-pile / mad_research_update_2 / generating-text-using-nl-to-simulate-activations / tyche-poser-comparison / autointerp

## 6. 校准日志

- 2026-09-08：同步校准（openai/anthropic 列系 v2 重采口径；全部数值以 output/ 各库单篇 JSON 及 _aggregate.json 为准，eleuther 列经 10 篇单篇 JSON 逐格复核无漂移）。① 篇幅行改权威中位值：cerebras 2,036→1,313、eleuther 4,673→2,772、databricks 4,199→2,076、openai 2,819→3,164、anthropic 2,622→2,640、壳中客 3,905→4,830 字；② openai 列：句长 22.2→22.3、数字密度 16.1→20.7、精确数字 1.1→0.92、hedge 8.8→9.6、绝对化 1.6→1.76、第一人称 59.0→53.0、客观自指 0.5→1.0、TTR 0.31→0.33、MATTR 待重算‡→0.68；③ anthropic 列：数字密度 7.4→8.25、精确数字 1.6→1.46、hedge 9.6→10.52、绝对化 2.1→2.32、第一人称 42.5→30.0、客观自指 2.0→1.5、TTR 0.35→0.34、MATTR 待重算‡→0.69，‡ 注记删除；④ 壳中客列整体标明 v10 口径（表头改"中·v10"，† 注记保留）：hedge 2.7→2.69、绝对化 1.1→1.08；⑤ 散文与指纹行：精确数字"是 OpenAI 的 13 倍"→15 倍（14.1/0.92≈15.3）、人称对比（61.5 vs 59→53）、对照组"余四库"→"余六库"、MATTR pooled ~0.71→~0.70（余六库 60 篇 pooled median=0.70）、精确数字 pooled ~2.3→~3.0（pooled median=2.95）。