# 事实审计：article-eval-power-v1.md（生产稿）

- 审计员：独立事实审计环节（judge-fact）
- 审计日期：2026-09-15
- 基准：仅以 `source-pack.md`（2026-09-15 采集）为包内事实基准；外部核验用公开检索。
- 未读取生成方材料（generation-selfcheck.md / .profile.json），未做任何 git 操作。

## 一、批准事实清单（自 source-pack.md 提取）

| # | 事实 | 归因等级 |
|---|------|----------|
| F1 | Leaderboard Illusion 论文：2025-04，68 页，Cohere Labs+AI2+Princeton+Stanford+Waterloo+UW 等 13 人 | [论文] |
| F2 | 论文分析约 280 万场对战、238 个模型 | [论文] |
| F3 | 大实验室可私下测多个未发布变体、只公开最佳；Meta 在 Llama 4 前测 27 个私有变体（LMArena 有异议，须给双方位置） | [论文]+争议 |
| F4 | 私有变体+选择性披露扭曲 Bradley-Terry 公平性 | [论文] |
| F5 | TechCrunch 2025-04-30 报道（标题指控 LM Arena 帮助头部实验室操纵基准） | [报道] |
| F6 | LMArena 回应：对部分头条数字有异议，随后修改运营政策 | [官方] |
| F7 | 另有投票操纵论文（OddsShopper 转述，须"一项研究称"） | [论文]/转述 |
| F8 | LMArena 2025 年获 $100M 种子轮；2026-01-28 更名 Arena，宣布 $150M A 轮、估值 $1.7B，含 a16z；变现：企业审计/API/高级分析（uper.pl 2026-04-27，用"据报道"） | [报道] |
| F9 | 文本榜单 >770 万票、389 个模型（opper.ai 2026-08-17） | [报道] |
| F10 | WSJ（经 aiglossary.news 转述）：OpenAI 内部跟踪 LMArena 排名 | [报道] |
| F11 | Patronus AI：前 Meta 研究员 2023 年创立；2026-06-25 获 $50M B 轮（Greenfield 领投，累计 $70M）；客户含多数头部前沿实验室与云厂商；产品转向 Digital World Models | [报道] |
| F12 | implicator.ai AI Top 40：SWE-bench/LiveCodeBench/GPQA/ARC-AGI/HLE 权重 2.0×，Chatbot Arena 与 MMLU-Pro 降至 0.5×（2026-04-03） | [报道] |
| F13 | Bean et al. (2025)：445 篇基准论文，仅 16% 比较结果时用不确定性估计或统计检验（EvalSafetyGap 综述 2026-07 转引） | [论文]/转引 |
| F14 | 欧委会 JRC 综述（Eriksson et al.）：构念效度、激励与博弈问题（同上转引） | [论文]/转引 |
| F15 | Kili Technology 2026-04 行业综述：污染、博弈、标注错误率可观（">50%"已按要求弱化） | [报道] |
| F16 | EU AI Act：2024-08-01 生效；2025-02 禁止条款；2025-08 GPAI 义务；2026-08 高风险主要义务（artificialintelligenceact.eu 2026-08-31 + CIVAC 2026-05-27） | [官方] |
| F17 | 写作纪律：27 变体挂"论文称"且给 LMArena 异议位置；融资挂"据报道"；罚款数字须注明"上限" | — |

## 二、逐条断言判定

判定图例：✅ 一致 ｜ ⚠️ 归因不匹配/轻微问题 ｜ 🔴 包外引入或事实错误 ｜ 🔎 需复核

| 行 | 成稿断言 | 对照 | 判定 |
|----|----------|------|------|
| 3 | 2025 年 4 月、68 页论文、13 位研究者（Cohere Labs, AI2, Princeton, Stanford 等） | F1。外部核验：arXiv:2504.20879 作者恰为 13 人，机构含 Cohere Labs/Cohere、Princeton、Stanford、Waterloo、MIT、AI2、UW；"and other institutions" 覆盖准确 | ✅ |
| 3 | "roughly 2.8 million battles … covering 238 models" | F2 包内一致。**但外部核验失败**：论文 v2 原文两处写明 "2M battles and cover 243 models across 42 providers"（Introduction 与 Appendix D）；多家独立转述（Hexaware、explainx 等）亦为 ~2M/243。**信源包 F2 本身有误**，成稿忠实照抄了错误数字 | 🔴 |
| 5, 51 | 大实验室私下测多个未发布变体、只公开最佳；"Meta, the paper claims, tested 27 private variants of Llama 4" | F3。挂"the paper claims"归因 ✅；外部核验：论文摘要原文确认 27 变体（Meta，Llama-4 发布前） | ✅ |
| 51–57 | 27 变体争议给位 | F3/F17：L51 挂"the paper claims"，L55 指明具体数字"contested"，L57 给出 LMArena 公开异议+政策修改——双方位置齐全 | ✅ |
| 53 | Bradley-Terry 公平性被选择性披露破坏 | F4 ✅（论文机制描述，外部一致） | ✅ |
| 55 | TechCrunch 4 月 30 日标题（研究指控 LM Arena 帮助头部实验室 game 基准） | F5 ✅；外部核验标题一致（2025-04-30） | ✅ |
| 55 | OddsShopper 转述的投票操纵研究 | F7。措辞 "one study relayed by … OddsShopper claims" 符合"一项研究称"纪律 | ✅ |
| 57 | LMArena 公开反驳部分头条数字、随后修改运营政策 | F6 [官方] 自述，成稿平实陈述未夸大 | ✅ |
| 7, 37 | $100M 种子轮（"reported"/"reportedly"）；今年 1 月更名 Arena、$150M A 轮、$1.7B 估值、a16z 在列；变现=企业审计/API/高级分析 | F8。归因合规。外部核验：$100M 种子（2025-05，a16z+UC Investments 领投，texau/TechCrunch 系汇总）；$150M A 轮+$1.7B 估值（Mexico Business News 2026-01-07）；2026 年 1 月更名（opper.ai 确认）✅。注：a16z 参与 **A 轮** 这一细节在抽检样本中未获独立确认（外部确认的是 a16z 领投种子轮），但属包内批准事实 | ✅（附 🔎 小注：a16z A 轮角色） |
| 25 | 文本榜单 >770 万票、389 模型，"according to August statistics from opper.ai" | F9。外部核验：opper.ai 原文 "more than 7.7 million votes across 389 models on the text leaderboard" 逐字吻合 | ✅ |
| 29 | WSJ 报道 OpenAI 密切跟踪 Arena 排名，经 aiglossary.news 转述 | F10。双层归因措辞完整（"The Wall Street Journal has reported, in an account relayed by …"） | ✅ |
| 69 | Patronus：前 Meta 研究员创立（"three years ago"=2023 ✅）；今年 6 月 $50M B 轮 Greenfield 领投、累计 $70M；客户含多数头部前沿实验室与云厂商（"reportedly"） | F11。外部核验：PR Newswire/Morningstar 2026-06-25、TechCrunch 2026-06-25 确认全部要素（创始人 Anand Kannappan & Rebecca Qian、2023 创立、$50M/Greenfield/累计 $70M、客户构成） | ✅ |
| 71 | Digital World Models = 企业软件数字孪生中压力测试 agent | F11。外部核验：与官方公告表述一致 | ✅ |
| 77 | implicator.ai 4 月 AI Top 40：五项 2.0×，Chatbot Arena 与 MMLU-Pro 0.5× | F12。外部核验：implicator.ai 原文确认 Tier 1 五项 2.0×、Chatbot Arena/MMLU-Pro 0.5×（2026-04-03） | ✅ |
| 83 | EvalSafetyGap 7 月综述转引：Bean et al. (2025) 445 篇、仅 16% 用不确定性估计或统计检验 | F13。外部核验：arXiv:2511.04703 / NeurIPS 2025 原文 "16.0% used uncertainty estimates or statistical tests"；EvalSafetyGap（arXiv 2606.30219）转引链一致 | ✅ |
| 83 | "Five of every six published comparisons never checked" | 由 16% 派生：未检验比例为 84.0%，"five of every six"=83.3%，轻微低估 0.7 个百分点。方向正确、属修辞性约数，但生产稿建议改为 "more than four of five" 或直接 "84 percent" | ⚠️ 轻微 |
| 85 | JRC 综述（Eriksson et al.）：构念效度 + 激励博弈 | F14 ✅，转引链已注明（"The same review cites…"） | ✅ |
| 87 | Kili Technology 4 月综述：污染、博弈、"substantial annotation error rates" | F15。已按信源包指示弱化 ">50%"，未出现包外的具体百分比 | ✅ |
| 97 | AI Act 2024-08 生效、2025-02 禁止条款、GPAI 义务"since last August"（=2025-08） | F16。外部核验：2024-08-01 生效、2025-02-02 禁止条款、2025-08-02 GPAI 义务——三点全部准确 | ✅ |
| 99 | **"The main obligations for high-risk systems took effect this August"** 及 L99 "the high-risk regime is one month old" | F16 包内一致（信源包批准 2026-08 高风险生效）。**但外部核验失败**：信源包自引的 artificialintelligenceact.eu 高层摘要页（2026-08-31 按 Digital Omnibus on AI 修正案更新）现明确写明——Annex III 高风险义务 **2027-12-02** 起适用、Annex I 高风险义务 2028-08-02 起适用；2026-08-02 实际生效的是第 50 条透明度义务与 AI Office 执法权。LogicGate、wpseoai、Frontiers（2026-09-09）、欧委会 digital-strategy 页均佐证 Omnibus 推迟了高风险时间线。CIVAC 2026-05-27 简报早于 Omnibus（2026 年中通过），信源包据之作出的"2026-08 高风险生效"已过期 | 🔴 |
| 99 | "general-purpose evaluation duties are in their second year of execution" | GPAI 2025-08-02 起，2026-09 写作时点恰进入第二年，成立 | ✅ |
| 111–117 | 三处反驳中引用的事实（Arena 反驳+改政策、implicator 权重、16%） | 均为前文已核准事实的复用，无新断言 | ✅ |
| 129 | "only about one in six published benchmark papers checks significance" | 16%≈1/6，派生准确 | ✅ |
| 全文 | 包外引入扫描 | 未发现信源包之外的具体数字/事件/主体断言；"carmakers pay for crash testing"等为通用修辞类比，不构成事实断言 | ✅ |

## 三、外部抽检记录（6 项关键断言）

| 断言 | 抽检结果 | 独立来源 |
|------|----------|----------|
| 27 私有变体（Meta/Llama 4） | 真实，论文摘要原文确认 | arxiv.org/abs/2504.20879 |
| LMArena 融资线（$100M 种子 / $150M A / $1.7B / 2026-01 更名） | 真实 | mexicobusiness.news（2026-01-07）、texau.com、opper.ai（2026-08-17） |
| Bean et al. 16% / 445 篇 | 真实（16.0%） | arxiv.org/html/2511.04703、NeurIPS 2025 proceedings |
| Patronus $50M B 轮 / Greenfield / 2026-06-25 / 累计 $70M | 真实 | Morningstar/PR Newswire、TechCrunch（2026-06-25） |
| 论文分析规模 2.8M battles / 238 models | **不成立**：论文原文为 2M battles / 243 models / 42 providers | arxiv.org/html/2504.20879v2（Introduction + Appendix D 两处） |
| EU AI Act 高风险义务 2026-08 生效 | **不成立**：Digital Omnibus 修正后为 2027-12-02（Annex III）/ 2028-08-02（Annex I）；2026-08-02 生效的是透明度义务与 AI Office 执法权 | artificialintelligenceact.eu/high-level-summary（2026-08-31 更新）、digital-strategy.ec.europa.eu、Frontiers（2026-09-09）、LogicGate |

## 四、红色项清单

1. 🔴 **L3："roughly 2.8 million battles … covering 238 models"**
   - 性质：包内一致但信源包事实错误（F2），成稿照抄。
   - 修订建议：改为 "roughly 2 million battles … covering 243 models across 42 providers"（论文 v2 原文口径）。

2. 🔴 **L99："The main obligations for high-risk systems took effect this August" + "the high-risk regime is one month old"**
   - 性质：包内一致但信源包时间线已被立法修正推翻（F16 过期）；连信源包自引的 artificialintelligenceact.eu 现版都不支持该断言。
   - 修订建议：改为反映 Digital Omnibus 修正后的时间线——2026-08-02 生效的是透明度义务（Art. 50）与 AI Office 执法权；Annex III 高风险主要义务推迟至 2027-12-02。同时 L99 "one month old" 与结论段相关表述需同步改写（"监管方向已定"的论点不受影响，反而"义务刚推迟"可作为监督能力薄弱的佐证）。

3. ⚠️ **L83："Five of every six"**（84.0% vs 83.3% 的 0.7pp 低估）——建议改 "more than four of five" 或 "84 percent"。不阻断发布。

## 五、总判定

**需修订后发布（Revise, then publish）。**

理由：全文归因纪律优秀——27 变体争议双方位置齐全（F3/F17 达标）、融资与转述数字全部挂 "reportedly/according to"、论文级断言挂 "the paper claims / the review relays"、无任何包外引入断言。但两处红色项均为**信源包自身的错误被忠实搬运**：论文样本规模（2.8M/238 → 实为 2M/243）与 EU AI Act 高风险义务时间线（2026-08 → 实为推迟至 2027-12）。生产稿发真实站点，这两处都是可被读者用一手来源当场证伪的硬数字，必须先修。修订范围小且局部（两处句子级改动+一处派生表述），改完后无需重走全流程。
