# 《Databricks AI Research Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2026-01 至 2026-08，AI RESEARCH 栏目全量）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/databricks/ ｜ 统计：output/databricks/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**企业研究团队的"工程化评测"文体**：集体署名（"The Databricks AI Research Team"）抹去个人声音；内容以自建系统/基准（KARL、MemAlign、MemEx、OfficeQA Pro V2）为核心，每个项目 = 动机 + 方法 + 评测 + 落点建议的固定骨架。词汇多样性六库最高（TTR 0.46；MATTR 0.71 等长窗口校正后居次高，Google 0.73 最高）：句式直白、术语不循环堆砌，与 EleutherAI 形成两极。第一人称中位（21.5）落在"我们做了 X"的工程叙述区间。
⚑ 例证："As GenAI adoption grows, we increasingly rely on LLM Judges to scale agent evaluation and optimization across industries."（memalign——企业语境开场，动机先行）

## 2. 量化基线（10 篇，median）· 六库对照表

| 指标 | Cerebras | EleutherAI | **Databricks** | OpenAI | Anthropic | 壳中客(中·v10) |
|---|---|---|---|---|---|---|
| 篇幅（词/字） | 1,313 | 2,772 | **2,076** | 3,164 | 2,640 | 4,830 字 |
| 平均句长（词/字） | 18.8 | 25.7 | **26.2** | 22.3 | 22.5 | 34.5 字 |
| 数字密度 /千词(字) | 40.1 | 44.1 | **24.4** | 20.7 | 8.25 | 17.1 |
| 精确数字 /千词(字) | 3.1 | 14.1 | **4.0** | 0.9 | 1.5 | 5.6 |
| 限定语 /千词(字) | 7.9 | 10.6 | **5.5** | 9.6 | 10.52 | 2.69† |
| 断言绝对化 /千词(字) | 1.82 | 1.2 | **1.11** | 1.8 | 2.3 | 1.08 |
| 第一人称 | 10.5 | 61.5 | **21.5** | 53.0 | 30.0 | 6.0 |
| 客观自指 | 0.5 | 1.5 | **0.0** | 1.0 | 1.5 | 2.0 |
| 外链 /千词(字) | 0 | 0 | 0 | 0 | 0 | 0 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 |
| TTR | 0.42 | 0.26 | **0.46** | 0.33 | 0.34 | 0.35 |
| MATTR（w=150） | 0.70 | 0.65 | **0.71** | 0.68 | 0.69 | 0.74 |
| **指纹**（discriminate.py，vs 余六库 pooled，7 库限定） | — | — | **TTR 最高**（内参指标（q=0.002）；MATTR 7/7 终态定稿：0.71 次高（Google 0.73 最高）且对 OpenAI（0.68）显著高——"词汇直白"成立但非库群唯一极值；TTR 行按内参保留） | — | — | — | — |

> 指纹解读：六库中最直白的用词——术语不循环堆砌、句式多变，与 EleutherAI 的术语密集构成光谱两极；等长窗口（MATTR）校正后差距收窄约 2/3 但序保持，词汇直白是文体成分而非篇幅假象。
> † 壳中客限定语为 2026-09-07 词表修复后 v10 口径（原 4.8 含"约→约束"子串污染）；本列其余数值同为 v10（10 篇）口径，24 篇 v0.1 口径见壳中客档案，两者不可混排。

## 3. 结构信号（rubric 00/01 抽样）

- 固定骨架：动机段（企业痛点点名）→ 系统/基准自建 → 评测（多为自建 benchmark 或对比）→ 落点（"想了解完整报告点这里"——tech report 外链是标配）；
- **评测报告（evaluation-report）占比最高**：OfficeQA Pro V2、3x Faster Search、KARL 均为基准+方法型；
- 标注："AI RESEARCH" 栏目是官方分层（对应壳中客 genre-map 覆盖机制——可直接复用）；
- 内部链接（related posts/tech report）密度高，但被 innerText 抹平，文本化指标看不见——需 cdp 复查。

> **3 篇聚合修正（2026-09-08）**：memalign + memory-scaling + officeqa 聚合后 COUNTER=7 处——orchard 单篇的"零 COUNTER"仅对系统文子类成立；memory-scaling 含完整反驳节（What Gets in the Way + 议程化回应）。详见 `output/_moves-aggregate.md`。

## 4. 待人工裁决项

- ⚑ "企业研究文体"与 OpenAI research-narrative 的关系：是子体裁还是独立体裁，需 rubric 00 定夺；
- tech report 外链多，但 profiler 外链指标为 0——正文提取方式（innerText）丢链接，需评估是否影响档案完整性；
- 全量语步标注未做。

## 5. 语料清单

agentic-reasoning-in-practice / memalign / enhancing-agent-retrieval-chart-extraction / officeqa-pro-v2 / 3x-faster-search-parallel-test-time-scaling / memex / pushing-frontier-data-agents-genie / memory-scaling-ai-agents / meet-karl / scaling-small-llms-nvidia-mps

## 6. 校准日志

- 2026-09-08：跨库数值同步（逐格对照 output/ 各库单篇 JSON 及 _aggregate.json，统计层以 JSON 为准）。① 篇幅行改用单篇 JSON 重算 median：Cerebras 2,036→1,313、EleutherAI 4,673→2,772、Databricks 4,199→2,076、OpenAI 2,819→3,164、Anthropic 2,622→2,640、壳中客 3,905→4,830 字；② OpenAI/Anthropic 两列系 v2 重采口径：MATTR "待重算‡" 补 0.68/0.69 并删 ‡ 注记，OpenAI 第一人称 59.0→53.0、平均句长 22.2→22.3、数字密度 16.1→20.7、精确数字 1.1→0.9、限定语 8.8→9.6、断言绝对化 1.6→1.8、客观自指 0.5→1.0、TTR 0.31→0.33；Anthropic 第一人称 42.5→30.0、限定语 9.6→10.52、数字密度 7.4→8.25、精确数字 1.6→1.5、断言绝对化 2.1→2.3、客观自指 2.0→1.5、TTR 0.35→0.34；③ 壳中客列标明为 v10（10 篇）口径（表头加注 ·v10）：限定语 2.7→2.69、断言绝对化 1.1→1.08，第一人称 6.0/客观自指 2.0 与 v10 JSON 一致未变，24 篇 v0.1 口径不混入本表；④ 散文修正：第 1 节 "MATTR 0.71…仍最高"→居次高（Google 0.73 最高，与指纹行及 google-research _aggregate.json 一致）、指纹行 OpenAI MATTR 0.677→0.68（openai _aggregate.json median）、指纹解读 "五库"→"六库"（与六库对照表一致）。Cerebras/EleutherAI 两列逐格核对与本库（Databricks）各格均与各自 _aggregate.json 一致，未改。