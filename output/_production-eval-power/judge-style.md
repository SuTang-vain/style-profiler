# judge-style · article-eval-power-v1.md（judge-kezhongke-en 系列口径）

- **评审对象**：output/_production-eval-power/article-eval-power-v1.md（目标：anthropic × openai 中间带 + kezhongke 签名装置；A 分析评论类，英文成稿）
- **评审日期**：2026-09-15
- **方法声明**：独立评审——未读取 generation-selfcheck.md 与 article-eval-power-v1.profile.json；定量指标由 `python3 profiler.py` 对成稿独立实测；参照系校准抽读 corpus/anthropic/（building-effective-agents、demystifying-evals-for-ai-agents）与 corpus/openai/（gdpval、harness-engineering）各 2 篇开头 ~500 词。

## 0. 参照系校准印象

- **anthropic 开头**：判断先行、定义克制（"draw an important architectural distinction"）、数字稀疏、段中句长均匀、hedge 自然嵌入（"Consistently, the most successful…"）。
- **openai 开头**：数字前置轰炸（"0 lines""1/10th the time""1,500 pull requests""3.5 PRs per engineer per day"）、短段快节奏、使命叙事、设问小节标题。
- **中间带读数**：成稿应在数字密度/段长/人称上居中，判断带 hedge，结构显性。

## 1. §0.2 定量走廊核验（独立实测）

| 指标 | 实测 | 走廊 | 判定 |
|---|---|---|---|
| 篇幅（词） | 2,985 | ≈2,900 [2,100, 3,750] | 带内贴目标 |
| 平均句长（词） | 21.3 | ≈22 [20, 24] | 带内 |
| P90 句长（词） | 32 | ≤35 / ≤41 | 带内（max 36，仅 2 句 >35） |
| 平均段长（词） | 39.3 | ≈42 [33, 53] | 带内 |
| 数字密度 /千词 | 12.4 | ≈14 [8, 21] | 带内近目标 |
| hedge /千词 | 10.05 | ≈10 [8, 13.5] | 带内贴目标 |
| absolutist /千词 | 2.35 | ≈2 [1.4, 3.4] | 带内 |
| 克制比 | ≈4.3:1 | 典型 4–5:1，红线 <3:1 | 带内 |
| 第一人称（次/篇） | 44 | ≈40 [21, 69] | 带内 |
| 客观自指（次/篇） | 2 | 1–2 [1, 2] | 带内（"This essay argues""This analysis offers"） |
| 设问（次/篇） | 3 | 2–3 [0, 5] | 带内贴目标 |
| MATTR | 0.72 | [0.66, 0.70] | 出带上沿 +0.02，恰贴高侧容差上限；双域（评测业×法律）+专名密集（MMLU-Pro/GPQA/SWE-bench/Bradley-Terry/EU AI Act…），按容差条款判可接受，余量为零 |
| 年份锚点 /千词 | 1.01 | ≈1，软上限 2 | 软约束内 |
| 感叹号 | 0 | 0（红线） | 守线 |
| 单句段 | 0 | ≤4 | 带内 |

## 2. 可读性处方 1–9 逐条判定

| 处方 | 判定 | 证据（引文 ≤40 字） |
|---|---|---|
| 1 长句拆分 | 兑现 | 均值 21.3/P90 32；最长 36 词两句均为冒号平衡结构，可一口气读完 |
| 2 段长回落 | 兑现 | 段长 39.3 ∈ [33,53]；单句段 0 |
| 3 概念显式命名 | 兑现 | "what we will call evaluative authority"，FRAME 段命名，全文复用 ×7 |
| 4 数字纪律取中 | 兑现 | 12.4/千词；定性判断均挂数字锚（"only 16 percent""27 private variants"） |
| 5 边界声明中性化、限额化 | 兑现 | 边界声明 3 处（§1/§3/§5），均为事实语域，无 "we should have" 式自我检讨 |
| 6 人称预算硬约束 | 兑现 | 44 ∈ [21,69]，贴目标 40 |
| 7 语言逻辑显性化 | **部分** | 主题句/承接/指针句齐；但"结构≠不诚实"边界重申 3 处（见 §5 专项） |
| 8 MATTR 高侧处置 | 兑现（容差贴限） | 0.72 = 上沿 +0.02，双域专名密集题材，容差条款内；无修正余量 |
| 9 主题词对偶负面清单 | 兑现 | "the graded" 自造名词化 ×4 ≤5 阈值；无单句词族 ≥3 叠加 |

## 3. 收尾组合 / 签名装置 / 红线

| 项 | 判定 | 证据（引文 ≤40 字） |
|---|---|---|
| 收尾组合（设问自答→编号结论→开放问题→比喻收束，无自我批评位） | 兑现 | "So should we stop reading leaderboards? No — but…"；编号结论 ×4；开放问题 "the current evidence does not cover it"（中性）；收束 "stop mistaking the whistle for the truth" |
| 概念显式命名 | 兑现 | 见处方 3 |
| 单一比喻复用 | 兑现 | referee→whistle 脊柱："The referee became a business"→"the referee question"→"the whistle for the truth"；服务概念非情绪 |
| 信源分层 | **部分** | 具体出处 ≥8 处（TechCrunch 30 April / opper.ai August / uper.pl April / implicator.ai April / EvalSafetyGap July / CIVAC May…）+ 10 条 Sources 实体化，达标；但模糊归因严格计数 3–4 处，超 ≤2 限额："had reportedly raised a nine-figure seed round"（无机构）、"The Wall Street Journal has reported"（无时间）、"one study relayed by … OddsShopper"（无时间）、"customers reportedly include"（无机构无时间） |
| 判断带边界 | 兑现 | "structural — not proven fraud""most published comparisons"；克制比 4.3:1 |
| 编号结论 + 开放问题 | 兑现 | 4 条编号 + 1 条开放问题，不收死 |
| 红线：感叹号 0 | 兑现 | 实测 0 |

## 4. A 类语步序列核验（HOOK→…→CLOSE 逐位对照）

| 骨架位 | 成稿落点 | 判定 |
|---|---|---|
| HOOK（场景并置） | 开头 4 段：68 页论文 × 估值上调并置 + 设问 "how did judging models become such a powerful position" | 兑现（叙事比高，符合场景 HOOK） |
| FRAME（框架预告） | "Three questions" 节：概念命名 + 两组件区分 + 明示三问题 + 五层路线图 | 兑现（HOOK 后即 FRAME，预告完整） |
| CONTEXT（概念定义/背景） | "The measurement layer"：静态基准 vs 实时榜单二分定义 + 饱和机制背景 | 兑现（叙事集中于此节） |
| ARGUE×n（主体 ≈2/3） | §1 裁判变生意 → §2 私下测试 → §3 被评者付费 → §4 科学底子薄 → §5 国家入场，五节均论断挂证据+归因 | 兑现（占比与证据配比符合） |
| COUNTER（独立反驳节） | "What the optimists get right"：三质疑逐条裁决 2 left-open / 1 mostly rebutted | 兑现（未解决不装已解决，如实标注） |
| APPLY（判断标准清单） | "A field guide for practitioners"：read/procure/build 三检查 | 兑现（可执行判据式） |
| CLOSE（编号结论+开放收尾） | 设问自答 → 编号结论 ×4 → 开放问题 → 比喻收束；无重复段 | 兑现 |
| 附：信源实体化 | Sources 节 10 条（机构+时间） | 兑现 |

语步序列与通用骨架逐位吻合，无缺位、无倒置、无 CLOSE 区重复段。

## 5. 处方 7 语言逻辑专项检查

- **段首主题句=结论**：兑现。例："The corporate turn is recent and fast""The EU AI Act is converting evaluation from a market tool into a legal duty""Three objections circulate … each deserves a verdict, not a shrug"。
- **段间承接显性**：兑现。连接词+指代链并用："Ownership, though, is only the surface""If the leaderboard's problem is privileged access, the next layer is…""Yet even an honest vendor … faces a deeper problem""Into this gap … walks the state"。
- **每主节末句指向下一节**：兑现，八个主节末句全部为指针句（"the first place to look is the leaderboard itself"→§1 等），子节级未滥用。
- **同一边界重申 ≤1 次**：**未兑现（本稿最弱点）**。"商业结构 ≠ 不诚实"同一边界出现 3 处：§1 "None of this proves dishonesty, because paid audits can be real audits"；§3 "a vendor paid by the graded is not automatically captured"；§3 隔一段再重申 "None of these features is dishonest"。§3 内两段相邻重申形同 v2 §23–25 反例的缩小版。
- **边界声明中性且 ≤3 处**：兑现（3 处、事实语域、集中 ARGUE 节群；COUNTER 裁决与 CLOSE 开放问题按划界不计入）。
- 附带观察：§4 "In other words, most published comparisons cannot tell…" 为同段换述，有显式连接词承接，不违排比重申禁令，但属冗余边缘。

## 6. 偏离方向

**带内，略偏 openai（未出带）**。偏 openai 侧：段长 39.3 几乎贴 openai 库中位 40.2（远离 anthropic 44.75）；小节开头数字前置节奏（$100M/$150M/$1.7B、$50M/$70M、16 percent）；设问 3 = openai 中位；第一人称 44 过两库中点（≈41.5）向 openai 53 侧。拉回 anthropic 侧：hedge 10.05 近 anthropic 10.52、数字密度 12.4 居中、定义性 FRAME 与带边界裁决。净方向：中间带内偏 openai 半步，不构成出带。

## 7. 总判定

**像（置信度：高）**。

- 定量走廊 14 项：13 项带内，MATTR 贴高侧容差上限（+0.02，双域专名密集题材，条款内可接受）。
- 语步骨架逐位吻合，收尾组合完整且无自我批评位；签名装置五件套全部在场， referee/whistle 单一比喻复用执行干净。
- 两处扣分为"部分"而非"未兑现"，均不触及红线与骨架：
  1. **最弱维 1 — 处方 7 重申纪律**："结构≠不诚实"边界 3 处重申（§1 一次 + §3 相邻两段两次），撞"同一论断边界表述不得重复超过一次"条款。
  2. **最弱维 2 — 信源分层模糊归因限额**：严格计数 3–4 处超 ≤2 限额（hook 段无机构 "reportedly"、WSJ 无时间、OddsShopper 无时间、Patronus 客户名单无出处）；≥5 具体出处与 Sources 实体化已达标，作对冲。
- 观察项（不扣分）：MATTR 0.72 容差余量为零，下轮修订若再引入新专名须先走处方 8 白名单。
