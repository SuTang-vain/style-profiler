# 独立风格评审：draft-v4-a-genre.md（两层风格模型盲测复验）

> 评审角色：独立风格评审（judge-style），与 judge-kezhongke-en-v2/v3 同角色。
> 盲测纪律：未读取 output/_p2-revalidation/generation-selfcheck.md 与 draft-v4-a-genre.json；定量数据为本评审独立运行 `profiler.py` 所得（2026-09-14）。
> 评审依据：templates/genre-playbook-kezhongke.md（§0.2 处方走廊与可读性处方 7 条、§0.2 收尾组合、§5/§7 签名装置、感叹号红线、§2–§3 语步骨架 A 类）。
> 参照系校准：抽读 corpus/anthropic/building-effective-agents.md、demystifying-evals-for-ai-agents.md 与 corpus/openai/gdpval.md、harness-engineering.md 各开头 ~500 词。

## 一、独立定量核查（profiler.py 实测 vs §0.2 走廊）

| 指标 | 走廊（目标 [区间]） | 实测 | 判定 |
|---|---|---|---|
| 篇幅（词） | ≈2,900 [2,100, 3,750] | 3,102 | ✅ 带内 |
| 平均句长（词） | ≈22 [20, 24] | 22.1 | ✅ 贴目标 |
| P90 句长（词） | ≤35 [≤41] | 34 | ✅ |
| 平均段长（词） | ≈42 [33, 53] | 49.7 | ✅ 带内偏高 |
| 数字密度 /千词 | ≈14 [8, 21] | 12.57 | ✅ 带内 |
| hedge /千词 | ≈10 [8, 13.5] | 11.93 | ✅ 带内 |
| absolutist /千词 | ≈2 [1.4, 3.4] | 2.26 | ✅ |
| 克制比 | 典型 4–5:1（红线 <3:1） | 5.3:1 | ✅ |
| 第一人称（次/篇） | ≈40 [21, 69] | 39 | ✅ 贴目标 |
| 客观自指 | 1–2 [1, 2] | 2 | ✅ |
| 设问（次/篇） | 2–3 [0, 5] | 3 | ✅ |
| MATTR | 0.68–0.69 [0.66, 0.70]，贴下沿 | 0.713 | ⚠️ 出带上沿 +0.013 |
| 感叹号 | 0 | 0 | ✅ 红线守住 |

注：最长"76 词句"系引文内句点导致的分句器粘连（"…we would rate it." 后接新句）；真实最长为 46 词的列举句，全部 >35 词句均靠冒号/分号/破折号组织，可一口气读完。

## 二、维度判定表

### 可读性处方 7 条

| # | 维度 | 判定 | 证据（≤40 字） |
|---|---|---|---|
| 1 | 长句拆分（句长 22、P90≤35） | 兑现 | 均值 22.1、P90 34；>35 词 10 句皆可一口气读完 |
| 2 | 段长回落 [33,53] + 单句段 ≤4 | 兑现（贴上限） | 段均 49.7；单句转折段恰 4 处（"The money comes first." 等） |
| 3 | 概念显式命名 | 兑现 | "A benchmark issuer is… Rating shopping means…" FRAME 段固定句式命名，全程复用 |
| 4 | 数字纪律取中 | 兑现 | 12.57/千词；关键判断皆有数字锚（$14B/49%、27 variants、44%→90%） |
| 5 | 边界声明中性化、≤3 处 | 兑现 | 仅 2 处且中性："the claim here is narrower than a denial of progress"；"remains unmeasured at scale"；无 "we should have" 式自我检讨 |
| 6 | 人称预算 [21,69] | 兑现 | 39 次，贴目标 40 |
| 7 | 语言逻辑显性化 | 兑现 | 8 个主节中 7 节末句为指针句（"the next mechanism is why the grades themselves keep rising"→下节 The Inflation Machine） |

处方 7 备注：'the grade stops being a product… it becomes a service sold to the graded' 出现 2 次（L21/L35）。系刻意回环扣题（机制论点复述），非无承接排比重申，亦非边界表述重复；记为可接受的修辞设计，不扣分但留意。

### 收尾组合（设问自答→编号结论→开放问题→比喻收束，无自我批评位）

| 环节 | 判定 | 证据 |
|---|---|---|
| 设问自答 | 兑现 | "So will the evaluation industry end the way the rating agencies did…? Probably not in that form" |
| 编号结论 | 兑现 | "1) The conflicts are structural… 2) The inflation is measurable… 3) Regulation will lag…" |
| 开放问题（中性，不计限额） | 兑现 | "Can an honest grader make money in this market, and will anyone pay for one…?" |
| 比喻收束 | 兑现 | "printing its grades again, in a different font… wait for the cows"（回扣开场 cows 引文 + license/ink 印刷比喻） |
| 无自我批评位 | 兑现 | 收尾局限写"证据未覆盖什么"，无"我们做错了什么" |

### 签名装置

| 装置 | 判定 | 证据 |
|---|---|---|
| 概念显式命名、术语唯一 | 兑现 | benchmark issuer / rating shopping / evaluation industry 全文唯一，无一文多译 |
| 单一比喻复用（服务概念） | 兑现 | license→ink→press→cows 印刷/执照比喻系统贯穿，小节末回收（"The money comes first."） |
| 信源分层 | 兑现（偏弱） | 分层属性有标注："According to the SEC's own later reports"、"outside researchers, not lab spokespeople"；但 "According to reporting last year" 无具体出处，"co-created by that same company" 未挂来源 |
| 判断带边界 | 兑现 | "Most procurement teams… will never read"、"two remain genuinely open"、hedge:absolutist 5.3:1 |
| 编号结论+开放问题 | 兑现 | 见收尾组合 |

### 红线

| 红线 | 判定 | 证据 |
|---|---|---|
| 感叹号 0 | 兑现 | 实测 0 |
| 无"业内普遍认为"式无出处断言 | 基本守住 | 唯一灰区为上述两处笼统出处 |

## 三、语步核验（对照 §2 通用骨架 / A 分析评论类）

识别序列：

```
HOOK     ¶1–2   场景并置（2007 S&P 内邮 "structured by cows" × 2025 leaderboard 27 variants）
FRAME    ¶3–4   "this essay argues… It answers three questions" + 三概念固定命名
CONTEXT/ ¶5–10  The License to Grade（机构史叙事作类比证据基座，叙事集中在该节）
ARGUE
ARGUE×3  §Who Pays the Grader / The Inflation Machine / Shopping for the Grade（每论断挂数字锚）
ARGUE    §The Regulator Arrives Late（EU AI Act、3% 全球营收上限）
COUNTER  §Four Objections, Two Verdicts（独立反驳节，2 rebutted / 2 left-open，显式标注处理结果）
APPLY    §A Buyer's Discipline（四项判据，"fails two or more should not enter a procurement decision"）
CLOSE    §The Ending Is Not Written Yet（设问自答→编号结论×3→证据缺口+开放问题→比喻收束）
```

对照结论：与 §2 骨架逐位吻合——FRAME 预告（三问题清单）在开场三段内完成；ARGUE 主体占比约 2/3；COUNTER 独立节且如实留下 2 条 left-open；APPLY 判据清单；CLOSE 形态完整且无重复段。
两点结构性备注：① HOOK 采用场景并置，严格按 §2 注释"仅行业分析用场景并置"，A 类借用属灰区，但执行克制（2 段即收）且直接服务类比论证，判为可接受借用；② "The License to Grade" 节叙事比重高，但叙事集中于类比我史基座一节，论证节叙事比归零，符合"叙事只允许出现在 CONTEXT"的精神。

## 四、总判定

**像（置信度：高）。**

定量走廊 13 项中 12 项带内（仅 MATTR 0.713 微出上沿）；可读性处方 7 条全部兑现；收尾组合四环节齐备且无自我批评位；签名装置五项全部兑现；感叹号红线守住；语步骨架与 A 类逐位吻合。COUNTER 的 2 rebutted / 2 left-open 与 §5 单篇标注实证的处理比例精确一致，收尾比喻回扣开场引文，属高完成度执行。

## 五、与"中间带"的偏离方向

**带内，偏 anthropic 侧，未出带。**

- 概念驱动：FRAME 段固定句式命名概念、全程复用（anthropic 式 definitional discipline，对照 building-effective-agents 的 workflows/agents 定义法）；
- 数字克制：12.57/千词，低于中点 ≈14.5，远离 openai 的 20.69；
- hedge 11.93 高于两库 median（10.52/9.57），克制比 5.3:1 贴 anthropic 侧；
- 人称 39 次居中略偏 anthropic（30/53）；
- 无 openai 式发布体特征（无使命宣言开场、无产品节奏、无目录导航条）。

## 六、最弱两个维度

1. **MATTR / 术语统一性锚点（处方 3 关联）**：实测 0.713，出带上沿（0.70）+0.013；playbook 要求"贴带下沿"，术语复用未把词汇多样性压进走廊。方向性小问题，但系唯一出带定量项。
2. **信源分层（签名装置 3）**：分层属性标注存在但锚点笼统——"According to reporting last year" 不给出处、"co-created by that same company" 无来源句；对照库内"据报道+具体出处"正反例纪律，是签名装置中执行最薄的一项。
