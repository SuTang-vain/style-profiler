# Databricks AI Research Blog · 撰写引导 playbook 初稿

> 2026-09-08 初稿。来源：output/databricks/_aggregate.json（10 篇统计）+ STYLE-PROFILE-databricks-v0.md + annotations/ 3 篇语步标注（memalign / memory-scaling / officeqa-pro-v2）+ corpus/databricks/ 本地语料短例证。
> 用途：回答"要写一篇符合该库风格的文章，具体怎么写"。与《Databricks 风格档案 v0》配套；档案散文与本文件冲突时，以 output/ 下 JSON 为准。
> 证据分级约定：[统计层]=全库 10 篇可信；[标注-3篇]=3 篇语步标注聚合（已达 ≥3 篇最低线，但只覆盖 10 篇中的 3 篇）；[推断]=仅档案散文支持。

## 1. 体裁/子体裁路由特征表

[统计层] profiler 把 10 篇全部判为 blog_or_exploration，无既有子体裁切分。
[标注-3篇]+[推断] 候选子体裁（**待裁决**，需 rubric 00 复核后并入基线）：

| 候选子体裁 | 识别特征 | 代表篇目 | 证据 |
|---|---|---|---|
| **发布文（系统/基准 release）** | "Today, we are releasing/introducing X" 成果前置开场；自建系统命名（MemAlign/OfficeQA/KARL/Genie）；评测图表紧跟；APPLY 落点为开源/HF/产品可用 | officeqa-pro-v2、memalign、meet-karl、3x-faster-search | [标注-3篇]（3 篇中 2 篇为此型） |
| **概念倡议文（research agenda）** | 提出并命名新概念轴（memory scaling）；开篇即预设质疑；独立反驳节（"What Gets in the Way"）+ 议程化回应；CLOSE 重申提案+开放问题 | memory-scaling | [标注-3篇]（3 篇中 1 篇，单篇候选，需补标确认） |
| **工程实验笔记** | 第一人称工程口吻更松弛（"We really enjoyed pushing the limits"）；负收益/适用边界明示（"rarely a general-purpose win"）；篇幅短（<1,000 词） | scaling-small-llms-nvidia-mps | [推断]（未标注） |
| **产品落地演示文** | 场景化长问题开场；落点为"available to all our customers"+文档链接 | agentic-reasoning、pushing-frontier-genie | [推断]（未标注） |

写作前路由：先确认写的是哪一型——**发布文是默认型**（10 篇中至少 6 篇疑似，3 篇标注中占 2）；只有当你要提出新概念轴时才走概念倡议文，此时反驳节是必备件。

## 2. 通用语步骨架

[标注-3篇] 3 篇 130 段聚合：ARGUE 76%、COUNTER 7 处、HOOK 0、APPLY 6 处、叙事段 0%。

```
CONTEXT（企业痛点点名，1-2 段；可省略，直接进 FRAME）
→ FRAME（成果前置："Today, we are releasing/introducing X" + 结构预告 "Below, we describe..."）
→ ARGUE×n（占全文约 3/4：概念定义 → 方法/组件 → 评测设置 → 结果详述；
   图注段落是合法 ARGUE，图表即论证主体）
→ COUNTER（0-1 处：发布文多为内化让步一句话；概念倡议文独立成节+议程化回应）
→ APPLY（可用性落点：开源/Hugging Face/产品入口/tech report 外链）
→ CLOSE（主张收束 或 重申提案+开放问题；无煽情、无叙事闪回）
```

要点：
- **无 HOOK**（0/130 段）：不要趣闻轶事开场，第一段就进企业痛点或成果声明。唯一例外是 memex 的 "In 1945, Vannevar Bush imagined..." 历史引子[推断，未标注篇目]。
- **ARGUE 密度高且纯**：叙事段 0%——不写"我们怎么想到的"过程故事，只写"系统是什么、证据是什么"。
- **COUNTER 可选但有定式**：出现时用"承认让步"或"议程化回应"（"not arguments against memory scaling"），不要开放式存疑。

## 3. 定量预算表

[统计层] 全部抄自 output/databricks/_aggregate.json（10 篇，median / P25–P75）：

| 指标 | median | P25–P75 | 写作口径 |
|---|---|---|---|
| 篇幅（词）※ | ≈2,076 | ≈1,753–2,757 | 目标 1,800–2,800 词；短篇实验笔记可至 700–900 |
| 阅读时长（分钟） | 7.0 | 6.0–9.0 | 对照项 |
| 平均句长（词） | 26.2 | 21.9–32.4 | 长句为常态，允许 30+ 词的复合句 |
| P90 句长（词） | 35.5 | 33–38 | 每篇要有若干 35 词以上长句 |
| 平均段长（词） | 45.9 | 43.4–51.7 | 短段落，约 2 句一段；不用单句段 |
| 数字密度 /千词 | 24.4 | 15.1–35.4 | 每千词 15-35 个数字 token |
| 精确数字 /千词 | 4.0 | 2.7–7.0 | 每千词至少 3 个小数/精确值（如 $0.03、+0.33 点） |
| 年份锚点 /千词 | 0.54 | 0–1.9 | 少提年份；历史跨度只在语料介绍时用 |
| 限定语 /千词 | 5.5 | 4.3–6.6 | 中等限定，不堆砌 may/perhaps |
| 绝对化断言 /千词 | 1.1 | 0.5–2.6 | 压低 always/never 类词 |
| 数量词 /千词 | 6.0 | 3.5–7.1 | — |
| 第一人称（次/篇） | 21.5 | 12–29 | 每篇约 20 次 we/our，工程叙述口吻 |
| 客观自指（this paper 等） | 0 | 0–1 | 基本不用 "this paper/post" 自指 |
| 设问句（个/篇） | 2.5 | 1–4 | 可用 1-4 个设问引节 |
| 感叹号 | 0 | 0–1 | 默认不用 |
| 外链 /千词 | 0 | 0 | ⚠️ 提取假象（innerText 丢链接），实际 tech report/HF 外链是标配，见 §5 |
| TTR / MATTR | 0.46 / 0.71 | 0.39–0.48 / 0.70–0.73 | 词汇直白：术语不循环堆砌，同义换说是加分项 |

※ 篇幅行说明：_aggregate.json 无 word_count 行，此行由各篇 JSON 的 word_count 现算（739/901/1720/1853/2015/2137/2627/2800/3426/3478）。**与档案 §2 的"4,199 词"冲突，以本篇 JSON 为准**（阅读时长 7.0 分钟 median 亦佐证 2,076 词量级）。冲突已记录，待档案 v1 修正。

## 4. 收尾形态与正反例

[标注-3篇] 收尾两种定型：

**A. 发布文收尾 = APPLY 可用性落点（+致谢块）**：最后一节给入口，不写感悟。
- 正例："publicly available on Hugging Face"（officeqa，34 字符）
- 正例："offered in open-source MLflow"（memalign，29 字符）
- 正例："available to all our customers"（agentic-reasoning，30 字符）
- 致谢/作者长名单块置于文末，是体裁标配（10 篇均见）[统计层，语料确认]。

**B. 概念倡议文收尾 = CLOSE 三连：重申提案 → 生产要求 → 开放问题**。
- 正例："We propose Memory Scaling"（memory-scaling，25 字符）
- 正例："The remaining work is substantial"（同上，33 字符）——承认工作量但不收回主张。

反例（不符合该库）：
- 教训格言化收束（OpenAI 式 "X is not just about A—it's about B"）——该库 0 例；
- 叙事闪回/情感收束——叙事段占比 0% [标注-3篇]；
- 感叹号收尾——median 0 [统计层]。

## 5. 操作化模式（该库固定写作招式）

[标注-3篇]+[统计层]

1. **成果前置宣告**：第一段或第二段用 "Today, we are releasing/introducing X"（40/34 字符）直接报成果，背景放后面（officeqa 先宣告再补 "Seven months ago, we introduced..."）。相当于该库的"倒金字塔开头"。
2. **速度×成本双报**：任何性能主张必须同时给倍数/绝对值和成本——"adapts in seconds with <50 examples"（35 字符）配 "costing only $0.01-0.12 per stage"（33 字符）；"highest quality while requiring $0.03"。只报准确率不报成本 = 不像该库。
3. **图表即段落**：图注独立成段参与论证（3 篇标注中图注段 10+ 处），图本身就是 ARGUE，不是装饰。写作时每节至少安排一处"图注段"。
4. **例题/例证分级展示**：给读者看输入长什么样——officeqa 按低/中/高难度各给一道例题并解析；memalign 用表格列出 judge vs SME 评估对照（"We see two charges on your account"）。
5. **概念命名并大写提案**：新概念给专名并明确定义句（"performance improves as memories accumulate"），文末大写重申（"We propose Memory Scaling"）。
6. **治理/边界自带一句**：企业语境下主动给治理特性（"delete or overwrite past records directly"）或边界声明（memalign 脚注坦白推理时多耗 0.8–1s），不等读者挑刺。
7. **资源外链落点**：tech report / Hugging Face / 开源入口链接是收尾标配——profiler 外链指标为 0 是提取假象[统计层已知]，写作时必须放。

## 6. 就绪度评估

**结论：部分能。** 定量预算与通用骨架可直接指导写作；子体裁路由与特有语步尚未定稿，写非"发布文"型文章时依据单薄。

缺口清单：
1. 标注覆盖 3/10：已达 ≥3 篇聚合最低线，但四个候选子体裁中两个（工程实验笔记、产品落地演示文）零标注，概念倡议文仅 1 篇；
2. 子体裁未裁决：§1 四候选全部"待裁决"，混体裁统计可能洗掉信号（rubric 00 警告）；
3. _aggregate.json 缺 word_count 行，篇幅预算靠现算；档案 §2"4,199 词"与 JSON 冲突未修；
4. 外链/内部链接指标全 0 为 innerText 提取假象，"资源外链落点"招式无法用统计校验密度；
5. rubric 02（论证标注）未做，论证结构（证据类型、反驳深度）无数据。

最小补全动作：
1. 补标 3 篇覆盖空白候选体裁（建议 scaling-small-llms-nvidia-mps + agentic-reasoning + pushing-frontier-genie），使每候选子体裁 ≥1 篇；
2. rubric 00 复核 10 篇，把 §1 候选子体裁转正或合并；
3. 修正档案 §2 篇幅行（4,199 → ≈2,076 median），并在 _aggregate.json 补 word_count 聚合行。
