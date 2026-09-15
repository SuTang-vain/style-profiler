# 信源包：评测即权力（2026-09-15 采集，agent-reach/WebSearch）

> 用途：生产稿《评测即权力》的事实地基。每条含声明 + 出处 + 可引用等级。
> 等级：**[论文]** 同行/预印本可核验；**[报道]** 媒体转述需"据报道"归因；**[官方]** 公司/机构自述。

## 1. 核心事件：Leaderboard Illusion（2025-04）

- [论文] Singh et al., "The Leaderboard Illusion"（2025-04，68 页；Cohere Labs + AI2 + Princeton + Stanford + Waterloo + UW 等 13 人）。分析约 280 万场 Arena 对战、238 个模型，发现：
  - 大实验室获**未公开的私下测试权**：可测多个未发布变体、只公开最佳成绩；**Meta 在 Llama 4 发布前测了 27 个私有变体**，榜单只见其一。
  - 私有变体机制 + 选择性披露扭曲了 Bradley-Terry 评分的公平性。
  - （论文另有开放模型占比/分数提升幅度的具体指控，LMArena 对这些数字有异议——引用时须带"论文称"归因。）
- [报道] TechCrunch 2025-04-30 报道（标题 "Study accuses LM Arena of helping top AI labs game its benchmark"）。
- [官方] LMArena 回应：对部分头条数字有异议，并随后修改了运营政策（"policy changes"）。
- [论文] 另有《Improving Your Model Ranking on Chatbot Arena by Vote Rigging》一文证明投票操纵可行（OddsShopper 转述，引用须"一项研究称"）。

## 2. 裁判商业化：Arena 的公司化

- [报道] LMArena 2025 年获 **$100M 种子轮**；2026-01-28 更名 **Arena**，同时宣布 **$150M A 轮、估值 $1.7B**，投资方含 a16z；变现方向：企业审计、API、高级分析（uper.pl 2026-04-27 指南文汇总；融资细节建议成稿时用"据报道"）。
- [报道] 规模：文本榜单累计 **>770 万票、389 个模型**（opper.ai 2026-08-17）。
- [报道] WSJ（经 aiglossary.news 转述）：OpenAI 内部密切跟踪 LMArena 排名变化——厂商把榜单当 KPI。

## 3. 评测供应商的利益结构

- [报道] Patronus AI（前 Meta 研究员 2023 年创立）：**2026-06-25 获 $50M B 轮**（Greenfield 领投，总融资 $70M），客户含"多数头部前沿实验室与云厂商"；产品转向 Digital World Models（企业软件的数字孪生里压力测试 agent）。→ 评测商的客户正是被评者。
- [报道] 评测聚合层的二次加权：implicator.ai 的 AI Top 40 把 SWE-bench/LiveCodeBench/GPQA/ARC-AGI/HLE 列 Tier 1（2.0×），Chatbot Arena 与 MMLU-Pro 降至 0.5×——榜单的信任层级已在市场定价中体现（2026-04-03）。

## 4. 测量学危机的学术定量

- [论文] Bean et al. (2025)：445 篇基准论文综述，**仅 16% 在比较结果时使用不确定性估计或统计检验**（经 EvalSafetyGap 综述 2026-07 转引）。
- [论文] 欧盟委员会 JRC 综述（Eriksson et al.）指出 AI 评测的构念效度、激励与博弈问题（同上转引）。
- [报道] Kili Technology 2026-04 行业综述：静态基准的污染、博弈与标注错误率问题（其"标注错误率超 50%"的说法建议弱化为"标注错误率可观"）。

## 5. 监管时间线：评测从市场工具变成法律义务

- [官方] EU AI Act 分期生效：2024-08-01 生效；2025-02 禁止性条款；**2025-08 GPAI（通用模型）义务生效**（技术文档、评测披露）；**2026-08 高风险系统主要义务生效**（artificialintelligenceact.eu 2026-08-31 高层摘要 + CIVAC 2026-05-27）。→ 2026-09 当下：GPAI 评测义务已在执行期，高风险义务刚生效一个月。

## 6. 写作注意（信源纪律）

- "27 个私有变体"——归因"论文称"，LMArena 对数字有异议，须给双方位置（这本身就是文章要的"评级机构争议"结构）。
- 融资金额/估值来自二级转述，用"据报道"。
- EU AI Act 罚款等具体数字（如全球营收百分比）成稿时若用，须注明"条例规定上限"而非既成事实。
- 不要用 v4 盲测稿的信用评级机构类比做主轴（本稿由用户定为新稿；类比可作一个 referenced frame 但需另立骨架——权力结构/利益闭环/测量学/监管四支柱）。

## 勘误（2026-09-15 事实审计）

- **§1 条目 1 数字口径有误**：原记"分析约 280 万场 Arena 对战、238 个模型"。论文 v2（arXiv:2504.20879）原文口径为**约 200 万场对战、243 个模型、42 家提供商**。生产稿 article-eval-power-v1.md 已按论文原文修正（L3）。
- **§5 条目时间线有误**：原记"2026-08 高风险系统主要义务生效"。EU AI Act 已被 **Digital Omnibus on AI** 修正：**Annex III 高风险义务 2027-12-02 起适用**；2026-08-02 实际生效的是**第 50 条透明度义务与 AI Office 执法权**。GPAI 义务（2025-08 起）在执行期，不变。生产稿 §5 第二段已按修正后时间线改写（L99 区）。
- 留痕说明：错误口径来自本包采集时的二手综述（artificialintelligenceact.eu 2026-08-31 摘要 + CIVAC 2026-05-27 简报对 omnibus 修正的覆盖滞后）；后续成稿引用 EU AI Act 时间线时须以 Digital Omnibus on AI 修正后口径为准。
