# 《Databricks AI Research Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2026-01 至 2026-08，AI RESEARCH 栏目全量）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/databricks/ ｜ 统计：output/databricks/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**企业研究团队的"工程化评测"文体**：集体署名（"The Databricks AI Research Team"）抹去个人声音；内容以自建系统/基准（KARL、MemAlign、MemEx、OfficeQA Pro V2）为核心，每个项目 = 动机 + 方法 + 评测 + 落点建议的固定骨架。词汇多样性六库最高（TTR 0.46；MATTR 0.71 等长窗口校正后仍最高）：句式直白、术语不循环堆砌，与 EleutherAI 形成两极。第一人称中位（21.5）落在"我们做了 X"的工程叙述区间。
⚑ 例证："As GenAI adoption grows, we increasingly rely on LLM Judges to scale agent evaluation and optimization across industries."（memalign——企业语境开场，动机先行）

## 2. 量化基线（10 篇，median）· 六库对照表

| 指标 | Cerebras | EleutherAI | **Databricks** | OpenAI | Anthropic | 壳中客(中) |
|---|---|---|---|---|---|---|
| 篇幅（词/字） | 2,036 | 4,673 | **4,199** | 2,819 | 2,622 | 3,905 字 |
| 平均句长（词/字） | 18.8 | 25.7 | **26.2** | 22.2 | 22.5 | 34.5 字 |
| 数字密度 /千词(字) | 40.1 | 44.1 | **24.4** | 16.1 | 7.4 | 17.1 |
| 精确数字 /千词(字) | 3.1 | 14.1 | **4.0** | 1.1 | 1.6 | 5.6 |
| 限定语 /千词(字) | 7.9 | 10.6 | **5.5** | 8.8 | 9.6 | 2.7† |
| 断言绝对化 /千词(字) | 1.82 | 1.2 | **1.11** | 1.6 | 2.1 | 1.1 |
| 第一人称 | 10.5 | 61.5 | **21.5** | 59.0 | 42.5 | 6.0 |
| 客观自指 | 0.5 | 1.5 | **0.0** | 0.5 | 2.0 | 2.0 |
| 外链 /千词(字) | 0 | 0 | 0 | 0 | 0 | 0 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 |
| TTR | 0.42 | 0.26 | **0.46** | 0.31 | 0.35 | 0.35 |
| MATTR（w=150） | 0.70 | 0.65 | **0.71** | 待重算‡ | 待重算‡ | 0.74 |
| **指纹**（discriminate.py，vs 余四库 pooled） | — | — | **TTR 最高**（0.46 vs ~0.35，p=0.001，q=0.001，过 FDR；MATTR 下仍最高 0.71，序保持；内参指标，MATTR 全库覆盖后可能改写，待 OpenAI/Anthropic 重采复核） | — | — | — |

> 指纹解读：五库中最直白的用词——术语不循环堆砌、句式多变，与 EleutherAI 的术语密集构成光谱两极；等长窗口（MATTR）校正后差距收窄约 2/3 但序保持，词汇直白是文体成分而非篇幅假象。
> † 壳中客限定语为 2026-09-07 词表修复后 v10 口径（原 4.8 含"约→约束"子串污染）。
> ‡ OpenAI/Anthropic 正文不入库，MATTR 待语料重采后重算；其 TTR 行为长度敏感指标，跨库比较以 MATTR 为准。

## 3. 结构信号（rubric 00/01 抽样）

- 固定骨架：动机段（企业痛点点名）→ 系统/基准自建 → 评测（多为自建 benchmark 或对比）→ 落点（"想了解完整报告点这里"——tech report 外链是标配）；
- **评测报告（evaluation-report）占比最高**：OfficeQA Pro V2、3x Faster Search、KARL 均为基准+方法型；
- 标注："AI RESEARCH" 栏目是官方分层（对应壳中客 genre-map 覆盖机制——可直接复用）；
- 内部链接（related posts/tech report）密度高，但被 innerText 抹平，文本化指标看不见——需 cdp 复查。

## 4. 待人工裁决项

- ⚑ "企业研究文体"与 OpenAI research-narrative 的关系：是子体裁还是独立体裁，需 rubric 00 定夺；
- tech report 外链多，但 profiler 外链指标为 0——正文提取方式（innerText）丢链接，需评估是否影响档案完整性；
- 全量语步标注未做。

## 5. 语料清单

agentic-reasoning-in-practice / memalign / enhancing-agent-retrieval-chart-extraction / officeqa-pro-v2 / 3x-faster-search-parallel-test-time-scaling / memex / pushing-frontier-data-agents-genie / memory-scaling-ai-agents / meet-karl / scaling-small-llms-nvidia-mps