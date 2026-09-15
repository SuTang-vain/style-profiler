# 自检报告：article-eval-power-v1.md（生产稿《评测即权力》）

> 生成日期 2026-09-15。输入：templates/genre-playbook-kezhongke.md（§0/§0.2 走廊 + 处方 1–9 + §4 两层 + §5 生产强化信源分层 + §6 收尾组合 + §7 招式）+ output/_production-eval-power/source-pack.md（唯一事实来源）。
> 实测命令：`python3 profiler.py output/_production-eval-power/article-eval-power-v1.md -o output/_production-eval-power/article-eval-power-v1.profile.json`（同目录下留存 JSON）。

## 1. 走廊实测（profiler 单文件实测，英文口径）

| 指标 | 目标 | 合格区间 | 实测 | 判定 |
|---|---|---|---|---|
| 篇幅（词） | ≈2,900 | [2,100, 3,750] | 2,985 | ✅ |
| 平均句长（词） | ≈22 | [20, 24] | 21.3 | ✅ |
| P90 句长（词） | ≤35 | ≤41 | 32 | ✅ |
| 平均段长（词） | ≈42 | [33, 53] | 39.3 | ✅ |
| 数字密度 /千词 | ≈14 | [8, 21] | 12.4 | ✅ |
| hedge /千词 | ≈10 | [8, 13.5] | 10.05 | ✅ |
| absolutist /千词 | ≈2 | [1.4, 3.4] | 2.35 | ✅ |
| 克制比 hedge:absolutist | 典型 4–5:1 | 红线 ≥3:1 | 4.28:1 | ✅ |
| 第一人称（次/篇） | ≈40 | [21, 69] | 44 | ✅ |
| 客观自指（次/篇） | 1–2 | [1, 2] | 2（this essay ×1 + this analysis ×1） | ✅ |
| 设问（次/篇） | 2–3 | [0, 5] | 3（HOOK 1 + COUNTER 1 + CLOSE 设问自答 1） | ✅ |
| MATTR | 0.68–0.69 | [0.66, 0.70]，高侧容差 ≤+0.02 | 0.72（出带上沿 +0.02，压容差线） | ⚠️ 容差内，结构性原因见 §5 |
| 年份锚点 /千词 | ≈1 | 软上限 2 | 1.01（2025×2 + 2024×1，全文仅 3 处） | ✅ |
| 感叹号 | 0 | 0 | 0 | ✅ |
| emoji | — | — | 0 | ✅ |

补充记录（非走廊项）：参考条目 10（Sources 节）；单句段 3 处（≤4 限额内：HOOK 并置句、"Into this gap…walks the state"、"What we are left with is four conclusions:"）；段长 P90 66 词（走廊只约束均值，留痕）；规则层 genre_guess = blog_or_exploration（规则只识别中文报告体/期刊体/行业分析，英文 A 格预期外命中，属工具口径而非体裁失格）。

## 2. 语步序列声明

HOOK（开场 4 段：论文指控 × 融资并置，无信用评级机构类比）
→ FRAME（## Three questions：命名核心概念 evaluative authority＝definitional + credibility 两组件；明示三问题清单；五层结构预告）
→ CONTEXT（## The measurement layer：静态基准 vs 活榜单定义、规模锚点、受众扩张；叙事仅在此区）
→ ARGUE×5（## 1 裁判公司化 → ## 2 私下测试与选择性披露 → ## 3 被评者付费 → ## 4 测量学危机 → ## 5 监管接盘；各主节末句指向下节）
→ COUNTER（## What the optimists get right：三质疑逐条，判决显式标注——①市场自净 **left open**；②"更好基准即可" **mostly rebutted**；③监管固化在位者 **left open, flagged as a live risk**）
→ APPLY（## A field guide for practitioners：读榜 / 采购评测 / 自建评估 三检查清单）
→ CLOSE（## So is any of it still worth reading：设问自答 → 编号结论 ×4 → 开放问题（中性"the current evidence does not cover it"，非自我检讨）→ referee 比喻收束；**无自我批评位**）

招式执行：①三问题清单 ✅；②信源分层（论文称/据报道/官方直陈，见 §3）✅；③判断带边界（most / only 16 percent / some labs / one in six）✅；④编号结论+开放问题 ✅；⑤单一比喻 referee 全文复用（became a business → referee question → investors/customers/license → whistle，服务概念非情绪）✅；⑥术语全文唯一（Arena / the paper / the Act / leaderboard / evaluation industry / measurement layer 各一主词）✅。

## 3. 信源清单对照（文中外部事实断言 ↔ 信源包条目）

信源包条目编号按 source-pack.md 小节：§1.1 论文本体 / §1.2 TechCrunch / §1.3 LMArena 回应 / §1.4 投票操纵研究 / §2.1 融资更名变现 / §2.2 规模 / §2.3 WSJ-KPI / §3.1 Patronus / §3.2 implicator 加权 / §4.1 Bean 16% / §4.2 JRC / §4.3 Kili / §5.1 EU AI Act 时间线。

| 文中断言（位置） | 包条目 | 包内等级 | 文中归因形态 |
|---|---|---|---|
| 68 页、13 位作者机构、约 280 万场对战、238 模型（HOOK ¶1） | §1.1 | [论文] | 论文级直陈（"the authors argued"） |
| 大实验室私下测多变体、只公开最佳（HOOK ¶2 / §2 ¶1） | §1.1 | [论文] | "the authors argued" / "according to the authors" |
| 九位数种子轮+更名+十亿估值（HOOK ¶3） | §2.1 | [报道] | "reportedly" |
| 770 万票 / 389 模型（CONTEXT ¶2） | §2.2 | [报道] | "according to August statistics from the analytics site opper.ai" |
| OpenAI 内部跟踪 Arena 排名（CONTEXT ¶4） | §2.3 | [报道]（二手转述） | "The Wall Street Journal has reported … relayed by the tracking site aiglossary.news"（模糊归因 #1：有机构无日期） |
| $100M 种子 / 更名 Arena / $150M A 轮 / $1.7B / a16z（§1 ¶1） | §2.1 | [报道] | "according to an April guide from the AI publication uper.pl" + "reported"×2 |
| 变现=企业审计/API/高级分析（§1 ¶2） | §2.1 | [报道] | "per the same guide" |
| Meta 测 27 个私有变体、榜单见一（§2 ¶1） | §1.1 | [论文] | "the paper claims"（包内纪律 ✅） |
| 开放模型占比/分数提升的进一步指控、数字有争议（§2 ¶3） | §1.1 | [论文] | "The paper goes further, claiming…"，并标注 "those specific numbers are contested" |
| TechCrunch 头条（§2 ¶3） | §1.2 | [报道] | "TechCrunch's headline on 30 April"（具体出处） |
| 投票操纵可行（§2 ¶3） | §1.4 | [论文]（OddsShopper 转述） | "one study relayed by the odds-comparison site OddsShopper claims"（模糊归因 #2：研究未具名无日期；包内要求"一项研究称"✅） |
| LMArena 异议+改政策（§2 ¶4、COUNTER ¶2） | §1.3 | [官方] | 官方行为直陈："publicly disputed … subsequently changed its operating policies"（时间锚于论文时间线，半具体，见 §6 诚实项 4） |
| Bradley-Terry 公平性被选择性披露破坏（§2 ¶2） | §1.1 | [论文] | 机制分析以论文发现为前提陈述 |
| Patronus：前 Meta 研究员创立三年、6 月 $50M B 轮 Greenfield 领投、累计 $70M、客户含多数头部实验室与云厂商（§3 ¶1） | §3.1 | [报道] | "reportedly"/"reported"（具体时间 "This June"） |
| Digital World Models 产品转向（§3 ¶2） | §3.1 | [报道] | "Patronus now promotes what it calls…" |
| implicator.ai AI Top 40 加权 2.0×/0.5×（§3 ¶5） | §3.2 | [报道] | "an April note from the research site implicator.ai describes" |
| 445 篇 / 16% 统计检验率（§4 ¶1） | §4.1 | [论文] | "Bean and colleagues (2025)" + "A July review by the EvalSafetyGap project relays" |
| JRC 构念效度/激励博弈（§4 ¶2） | §4.2 | [论文] | "The same review cites … Eriksson and colleagues" |
| Kili 污染/博弈/标注错误率（§4 ¶3） | §4.3 | [报道] | "an April industry review by Kili Technology catalogs"；按包内纪律弱化为 "substantial annotation error rates"（未用 50% 数字）✅ |
| EU AI Act 四段时间线（§5 ¶1–2） | §5.1 | [官方] | 直陈 + "according to a late-August high-level summary on artificialintelligenceact.eu and a May compliance briefing from the law firm CIVAC" |
| "当下=GPAI 执行期、高风险生效一个月"（§5 ¶2） | §5.1 | [官方] 派生 | 由官方时间线推算，措辞 "As of this writing" |

**包外事实零引入**：全文所有具体数字/事件均出自上表；分析性发挥（referee 经济学、comfort 产品形态、买方转变等）不含新外部数字或事件。罚款比例按包内纪律未使用。信用评级机构类比未使用。

## 4. 出处计数

- **具体出处（机构名+年份或文档名）：12 处**——①Singh et al. "The Leaderboard Illusion"（April 2025，文档名+时间）②TechCrunch 30 April 头条 ③LMArena 官方回应与政策修改（机构+行为，时间锚定论文）④uper.pl April 指南 ⑤opper.ai August 统计 ⑥Patronus AI June B 轮（Greenfield）⑦implicator.ai April 方法说明 ⑧Bean et al. (2025)（经 EvalSafetyGap July 综述转引）⑨Eriksson et al. / EC JRC（同上转引）⑩Kili Technology April 综述 ⑪artificialintelligenceact.eu late-August 摘要 ⑫CIVAC May 简报。下限 ≥5 ✅。
- **模糊归因：2 处（封顶）**——WSJ/aiglossary.news（有机构无日期）；OddsShopper 转述的投票操纵研究（研究未具名无日期）。两处均系信源包转述链所致，非写作疏漏。限额 ≤2 ✅。

## 5. MATTR 结构性标注（容差判定）

实测 0.72（未四舍五入 0.7195），出带上沿 +0.02，压容差线。结构性原因：**双域×三域题材**（AI 基准测量 × 风投融资 × 欧盟监管）+ **专名密集**（12 个具名信源 + 基准名 MMLU-Pro/GPQA/SWE-bench/LiveCodeBench/ARC-AGI/Humanity's Last Exam + Sources 节 10 条）。参照系库内 max：anthropic 0.743 / openai 0.724，本稿低于两库 max。
已执行处方 8 白名单（按优先序）：①专名短称复用（Arena / the paper / the Act / AI2 / a16z）；②同义归并（scoreboard·board·ranking site→leaderboard；ratings→scores；preprint→paper；firms→companies；players→labs；scandal→accusation；rhetoric→claims；defense→response；magnitudes→numbers；tally→statistics；demo→project）；③删减非必要专名（Sources 作者机构列表收敛）。**禁用手段未用**：无语义失真替换；新增段落均承载新论点（interested score / floor of authority / 判决预告等），非排比重述。下沿 0.66 红线远离。

## 6. 未达标项与诚实标注

1. **MATTR 0.72 压容差线**：未进 [0.66, 0.70] 带内，依 2026-09-14 修订轮容差条款判可接受（≤+0.02 + 双域/专名密集 + 本节结构性标注）；若评审以更严口径（或不同分词）复测，存在越线风险——这是全稿最脆的一项。
2. **模糊归因 2/2 封顶**：WSJ 条目为双重转述（WSJ 经 aiglossary.news），无日期；若评审主张"无日期即不合格"，可删 CONTEXT ¶4 末句（损失"厂商当 KPI 看"证据）或降级为弱表述。
3. **"Five of every six"** 系 16% 的算术换算（1−0.16=0.84≈5/6），派生而非包内原文；精度上 16%≠1/6，已用 "Five of every six" 约数口吻处理，留痕。
4. **LMArena 政策修改**文中无显式日期（"subsequently"），时间靠论文时间线锚定；计为具体出处属宽口径，严口径下算半具体。
5. **段长 P90 66 词**（CONTEXT ¶4 四句段）超出均值走廊所指的中段形态，但走廊仅约束均值（39.3 ✅），留痕不判失格。
6. 规则层 genre_guess=blog_or_exploration 系工具口径（仅识别三类中文体裁），英文 A 格成稿预期如此，非体裁失格。

## 7. 收尾组合核对（§6/§0.2）

设问自答 ✅ → 编号结论 ×4 ✅ → 开放问题（中性、"证据未覆盖"，非自我检讨）✅ → referee 比喻收束 ✅ → 无自我批评位 ✅；边界/局限声明全篇 1 处（"We should not overstate the present…"，≤3 限额内）；开放问题按 judge-v3 划界不计入限额 ✅。

---

## 修订记录（2026-09-15 三路评审后定点修订，句子级，骨架未动）

### 逐条 before/after

**R1（事实修正·红色项 1，L3，信源包 §1.1 口径错误）**
- before: "…had analyzed roughly 2.8 million battles on Chatbot Arena, covering 238 models."
- after: "…had analyzed roughly 2 million battles on Chatbot Arena, covering 243 models from 42 providers."
- 依据：论文 v2（arXiv:2504.20879）原文口径 ≈200 万场对战 / 243 模型 / 42 提供商；归因形态不变（论文作者行为直陈，"the authors argued" 语境）。

**R2（事实修正·红色项 2，L99 区，EU AI Act 时间线）**
- before: "The main obligations for high-risk systems took effect this August, according to a late-August high-level summary on artificialintelligenceact.eu and a May compliance briefing from the law firm CIVAC. As of this writing, general-purpose evaluation duties are in their second year of execution, and the high-risk regime is one month old."
- after: "This August brought the Article 50 transparency obligations and new enforcement powers into force. The Digital Omnibus on AI has moved the main high-risk obligations to 2 December next year. As of this writing, general-purpose evaluation duties are in their second year of execution, transparency duties are one month old, and the high-risk regime now has a fixed date."
- 依据：Digital Omnibus on AI 修正后 Annex III 高风险义务 2027-12-02 起适用；2026-08-02 生效的是第 50 条透明度义务 + AI Office 执法权；GPAI（2025-08）在执行期不变。论点保住：GPAI 执行 + 透明度义务生效 + 高风险义务有确定日期，仍是"评测成法律义务"的证据链。Sources 末节同步补记 Digital Omnibus。

**R3（轻微项，L83 区）**
- before: "Five of every six published comparisons never checked whether the differences they reported were real."
- after: "More than four of five published comparisons never checked whether the differences they reported were real."

**R4（风格观察项 1，§3 边界重申去重）**
- before: "None of these features is dishonest, but all of them are what a market of the graded, buying from the grader, predictably demands."
- after: "All of them are what a market of the graded, buying from the grader, predictably demands."
- "商业结构≠不诚实"边界全篇保留 §1（"None of this proves dishonesty…"）+ §3（"not automatically captured"）两处，§3 内第二处重申已删。

**R5（风格观察项 2，模糊归因补锚，HOOK ¶3）**
- before: "The accused platform did not collapse: within a year it had reportedly raised a nine-figure seed round, renamed itself Arena, and attached a billion-dollar valuation to the rebrand."
- after: "The accused platform did not collapse: it reportedly raised a nine-figure seed round last year, and this January it reportedly announced a Series A at a billion-dollar valuation and renamed itself Arena."
- 补主体（Arena）+ 轮次时间（last year 种子轮 / this January A 轮）。

**R6（风格观察项 2，Patronus 客户名单补时间锚，§3 ¶1）**
- before: "…and its customers reportedly include most leading frontier labs and cloud providers."
- after: "…bringing total funding to a reported $70 million. The June reports put most leading frontier labs and cloud providers on its customer list."

**R7（MATTR 对冲，§5 ¶5 同族替换）**
- before: "The money will follow the mandate: …" → after: "The money will follow the duty: …"（"duty" 为全文词族，"mandate" 为孤词；对冲 R2 引入的必要专名）。

### 修订后走廊复测（profiler 重跑，JSON 已覆盖更新）

| 指标 | 合格区间 | 修订前 | 修订后 | 判定 |
|---|---|---|---|---|
| 篇幅（词） | [2,100, 3,750] | 2,985 | 3,009 | ✅ |
| 平均句长 / P90 | [20, 24] / ≤35 | 21.3 / 32 | 21.2 / 32 | ✅ |
| 平均段长 | [33, 53] | 39.3 | 39.6 | ✅ |
| 数字密度 /千词 | [8, 21] | 12.4 | 13.29 | ✅ |
| 年份锚点 /千词 | 软上限 2 | 1.01 | 1.0（仍 3 处：2025×2 + 2024×1；新时间线用 "this August / next year" 零年份词） | ✅ |
| hedge / absolutist / 克制比 | [8,13.5] / [1.4,3.4] / ≥3:1 | 10.05 / 2.35 / 4.28 | 9.31 / 2.33 / 4.0 | ✅（hedge 回落因 "May 简报" 与 "reportedly include" 移除，仍在带内） |
| 第一人称 / 客观自指 / 设问 / 感叹号 | [21,69] / [1,2] / 2–3 / 0 | 44 / 2 / 3 / 0 | 44 / 2 / 3 / 0 | ✅ |
| MATTR | [0.66, 0.70]，容差 ≤+0.02 | 0.7197 | **0.71965（未舍入，≤0.72 ✅）** | ⚠️ 仍压容差线，结构性标注（§5）不变 |

### 修订后信源计数

- 具体出处：13 处（新增 the Digital Omnibus on AI 官方文件名为第 13 处；artificialintelligenceact.eu 与 CIVAC 移至 Sources 节并附修正注记）。
- 模糊归因：2/2 额度内——WSJ（经 aiglossary.news 转述，无日期）+ OddsShopper 转述的投票操纵研究（未具名）。R5/R6 后 HOOK 融资句与 Patronus 客户句均已带主体+时间锚，不再计入模糊归因。
- 信源包勘误：两处红色项已在 source-pack.md 末尾"勘误（2026-09-15 事实审计）"节留痕，后续成稿以勘误后口径为准。

### 残留说明

- MATTR 余量 ≈0.0004，任何后续增删专名都须先重跑 profiler 再定稿。
- §3 信源对照表中 §1.1（对战/模型数）与 §5.1（高风险义务时间线）两行以本节修订后口径为准。
