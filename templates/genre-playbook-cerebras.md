# Cerebras Blog · 撰写引导 playbook 初稿

> 2026-09-08 初稿。来源：output/cerebras/_aggregate.json（10 篇统计）、output/cerebras/annotations/（3 篇语步标注：never-loop-without-verifiers / how-we-built-our-knowledge-base / the-economics-of-ai-reasoning）、STYLE-PROFILE-cerebras-v0.md（仅作推断层佐证）。
> 用途：回答"要写一篇符合该库风格的文章，具体怎么写"。与《Cerebras Blog 风格档案 v0》配套；档案散文与本文件冲突时，以 output/ 下 JSON 为准。
> 证据分级约定：[统计层] = _aggregate.json 全库可信；[标注-3篇] = 3 篇语步标注（覆盖 3/10，且偏经验/处方类，性能发布文 0 标注，外推受限）；[推断] = 仅档案散文支持，待裁决。

## 一、体裁/子体裁路由特征表（候选，全部待裁决）

[推断] 规则层 10 篇全部为 `blog_or_exploration` 占位（genre_distribution，[统计层]），尚无分子体裁。从档案、标注与篇目归纳四个候选子体裁，**待人工裁决**：

| 候选子体裁 | 识别特征 | 代表篇目 | 证据 |
|---|---|---|---|
| **build-log 工程构建记** | "How we built X" 命名；按子系统分节（Anatomy/Slack/Threads…）；迭代失败叙事点（initially tested…kept encountering…stopped working）；设计哲学收束 | how-we-built-our-knowledge-base | [标注-3篇] 中 1 篇 |
| **prescription 处方式倡导** | 祈使句标题（Never Loop Without…/How to Stop…）；反直觉 HOOK；概念对立命名（Spiralling/Cheating）；处方清单+"Off-limits" 禁令；行动号召收束 | never-loop-without-verifiers, how-to-stop-your-autoresearch-loop-from-cheating | [标注-3篇] 中 1 篇 |
| **economics-analysis 经济学分析** | 全文无小节标题；历史锚定开场（"In 2024, o1…"）；自产数据论证（"1000+ of my AI sessions"）；成本/占比数字驱动；推荐阅读收束 | the-economics-of-ai-reasoning, latency-debt | [标注-3篇] 中 1 篇 |
| **perf-announcement 性能发布/深潜** | 标题含精确性能数字（"up to 750 tokens per second"）；会议/产品锚定（Hot Chips 2026）——**0 篇标注，特征仅从标题与档案推断** | how-cerebras-serves-gpt-5-6-sol, ultrafast-frontier-inference-hot-chips-2026, thinking-inside-the-box, exomebench | [推断]，最需补标 |

## 二、通用语步骨架

[标注-3篇] 三篇聚合（118 标注段，ARGUE 占 76%，COUNTER 0 处，APPLY 3 处，叙事段 14%——见 output/_moves-aggregate.md）：

```
HOOK（数字开场或反直觉开场；economics 类可省略，以历史 CONTEXT 代起）
→ CONTEXT×2–5（历史源流 / 术语定义 / 同期变化 / 团队背景）
→ FRAME（设问转折 "So why now?" / 结构预告 "provides three things" / 双问题框架）
→ ARGUE×n（主体 76%；穿插：数据锚定 → 过程证据 → 对抗推演 → 反例演示 → 正例对照）
   ※ COUNTER 一律不写独立节：把反对意见演一遍（"模型会去 download Terminal-Bench and train on it"），
     作为 ARGUE 的一个推演段内化掉——3 篇 118 段中 COUNTER = 0
→ APPLY×1–3（教学转向 "build up your intuition"；处方清单；Off-limits 禁令）
→ CLOSE（见第四节三种收尾形态）
```

写作指令：每 4–5 个 ARGUE 段插一个"锚"——一个精确数字、一段过程截图式证据，或一次对抗推演；不要让论证悬空超过两屏。

## 三、定量预算表

[统计层] 全部抄自 output/cerebras/_aggregate.json（10 篇）；篇幅一行例外，见表下注。

| 指标 | median | P25–P75 | 写作预算 |
|---|---|---|---|
| 篇幅（词）※ | 1,313 | 1,060–1,799 | 目标 1,300–1,800 词；超过 2,200 词需是 build-log 级系统工程 |
| 阅读时间（分钟） | 4.5 | 4.0–6.0 | 4–6 分钟读完 |
| 平均句长（词） | 18.75 | 15.7–21.9 | 句子控制在 16–22 词，明显短于 Databricks/EleutherAI |
| P90 句长（词） | 31.5 | 27–32 | 最长的句子也别超 32 词 |
| 平均段长（词） | 30.55 | 28.2–33.2 | **该库指纹：全七库最短段落**——一段 1–2 句，约 30 词 |
| 数字密度 /千词 | 40.12 | 15.23–49.0 | 每 100 词约 4 个数字；研究类往 40+ 靠 |
| 精确数字 /千词 | 3.09 | 2.42–16.8 | 区间极宽：性能文 15+，处方文 2–3，按子体裁分配 |
| 年份密度 /千词 | 2.05 | 0.72–3.85 | 历史锚定时用，常态 1–2 个/千词 |
| 限定语 /千词 | 7.89 | 4.48–8.97 | 保持 hedging（roughly/about/mostly），不要写死 |
| 全称量词 /千词 | 9.33 | 7.93–10.56 | every/always/never 类可用，配合限定语平衡 |
| 绝对化断言 /千词 | 1.82 | 0.56–2.56 | 克制；旗帜性断言全文 ≤2 处/千词 |
| 第一人称（次/篇） | 10.5 | 6–21 | **低 we 叙事**：个人署名、克制声音，别学 EleutherAI 的 61.5 |
| 客观自指（次/篇） | 0.5 | 0–1 | "this article" 类最多 1 次 |
| 问句（个/篇） | 1.5 | 0–4 | 设问只做 FRAME 转折，全篇 ≤4 个 |
| 感叹号 | 0 | 0–1 | 默认 0 个 |
| 外链 /千词 | 0 | 0 | 正文零外链、零参考文献条目（median 口径） |
| TTR / MATTR | 0.42 / 0.70 | 0.38–0.44 / 0.69–0.71 | 词汇重复度中等偏高，术语复用是风格而非缺陷 |

> ※ 篇幅：_aggregate.json 无 word_count 汇总字段，此行由 10 个逐篇 JSON 的 word_count 重算（median 1,313，min 780，max 3,229）。档案 §2 表写的"2,036 词"与 JSON 冲突，以 JSON 为准（见文末冲突清单）。

## 四、收尾形态与正反例

[标注-3篇] 三种已观测收尾，按子体裁选用：

1. **时代性升华 + 行动收束**（prescription 类）
   - 正例："While the workflow isn't new, this moment is."
   - 正例："All that's left is for you to go build one."
   - 写法：先承认旧（workflow isn't new），再宣布新（this moment is），最后把动作交给读者。
2. **设计哲学收束**（build-log 类）
   - 正例："meets people where they"（设计原则一句话收尾，无号召）
3. **推荐/工具收束**（economics 类）
   - 正例："I recommend checking this article"
   - 变体（marketing CTA，仅档案支持 [推断]）：latency-debt 结尾 "You can experience the Cerebras inference API for free"——带表情符号，属营销边界个案，是否纳入风格**待裁决**。

反例（不符合该库的收尾，勿写）：
- 参考文献列表、外链附录——reference_entries / links 中位数均为 0 [统计层]；
- 编号结论 + 关注问题（壳中客报告体形态）；Limitations 独立节（OpenAI 评测报告形态）——该库不声明局限，边界靠限定语内嵌；
- 感叹号煽情收束——median 0。

## 五、操作化模式（该库固定招式）

- **速度即世界观** [推断，档案 §1 + 标注佐证]：任何论证的落点都换算成速度/迭代成本。范式："That is fast enough for the agent to treat iteration as cheap instead of precious."——先给机制，再给速度值，最后升维成世界观。
- **数据锚定句** [标注-3篇]：机制论断后紧跟一句精确测量："about 1.2 seconds, running at roughly 1,500 tokens per second"。限定语（about/roughly）与精确数字同句共存，是该库 hedge 7.89/千词与数字密度 40/千词并存的来源。
- **对抗推演代替反驳节** [标注-3篇]：不写 "However, critics argue…"；直接推演攻击路径："download Terminal-Bench and train on it"，然后在下一段给出封堵（"marks the eval set as radioactive"）。
- **概念对立命名** [标注-3篇]：把失败模式命名成一对可传播的词（Spiralling / Cheating），各配一句单句定义（"Spiralling. The loop never learns."）。
- **处方清单 + Off-limits 禁令** [标注-3篇]：APPLY 段用祈使句短清单（"Be annoyingly specific about what counts as done"），并以一条硬禁令封顶（"Off-limits: you may not train on Terminal-bench"）。
- **反直觉/数字 HOOK** [标注-3篇]：开场二选一——反直觉断言（"Loops are the least surprising thing"）或规模数字（"more than 15,000 questions"），禁止场景描写式开场。

## 六、库差异显性化（同题材抗同质化）

[适用声明] 同一题材（如"构建+失败+加固"工程叙事）下，本库风格必须体现在下列结构级独有项与语步密度上，而非仅开场/收尾措辞。若成稿骨架与他库收敛（如"三失败→教训→改进"通稿结构），只换开场/收尾措辞判不合格。依据：output/_p1-cross-review.md §二/§五（2026-09-08 四库同题材盲测）。

**本库结构级独有项**（与他库同题材成稿的区分点）：

1. **短段节拍器** [统计层]：一段 1–2 句、约 30 词（段长 median 30.55，全七库最短，§三）——失败叙事拆成多个单观点短段，一段一个节拍；与他库 40+ 词长段拉开的首要指纹。
2. **对抗推演代替反驳节** [标注-3篇]：反对意见不独立成节，直接推演攻击路径、下一段封堵；语步分布上 COUNTER 独立节 = 0、ARGUE ≈76%（§二）。区别于他库"Bug 编号微弧线/自我批评节"——本库连反驳节都不设。
3. **概念对立命名 + 单句定义段** [标注-3篇]：失败模式命名成一对可传播的对立词，各配一句单句定义（"X。它从不 Y。"句式，§五）——命名而非编号，是本库组织失败叙事的形态。
4. **警句/隐喻单句段收尾** [标注-3篇]：收尾取 §四 三种形态之一，prescription/build-log 类以单句段格言收束（先承认旧、再宣布新）；不写 Limitations 独立节，边界靠限定语内嵌。
5. **零外链零参考文献** [统计层]：正文 links / reference_entries 中位数均为 0（§三）——他库同题材常见的外部引用，在本库一律内化为正文论证。

**写作自检**（成稿后执行）：

- 独有项命中 ≥3/5，其中第 1 条（短段节拍）为硬性项：抽正文 5 段以上，段长 median ≤33 词，否则退回拆段；
- 语步检查：COUNTER 独立节 = 0，且收尾为 §四 三种形态之一；两项缺一即退回。

## 七、就绪度评估

**结论：部分能。** 统计层预算可直接执行（定量指纹完整、含 MATTR 0.70）；但子体裁路由未裁决、标注仅覆盖 3/10 且偏处方/构建类，占语料 4 篇的 perf-announcement 类零标注——照本文件写"性能发布文"会落入推断区。

缺口清单：
1. 子体裁未路由：10 篇 genre 全为 blog_or_exploration 占位，§一 四分类为候选，待人工裁决；
2. 标注覆盖偏科：3/10 篇，perf-announcement 类（gpt-5-6-sol / hot-chips-2026 / thinking-inside-the-box / exomebench）0 篇；
3. _aggregate.json 缺 word_count 汇总字段，篇幅预算靠逐篇 JSON 重算；
4. 档案 §2 "篇幅 2,036 词"与逐篇 JSON（median 1,313）冲突，未裁决；档案 §4 "仅 1 篇已标注"已过时（实际 3 篇），档案未同步；
5. marketing CTA 收尾（latency-debt）是否属库风格，待裁决；
6. 同题材抗同质化为新增约束（§六），未经二轮盲测验证（2026-09-08）。

最小补全动作（按性价比排序）：
1. 补标 2 篇 perf-announcement 类（优先 ultrafast-frontier-inference-hot-chips-2026 + how-cerebras-serves-gpt-5-6-sol）→ 标注达 5/10 且四类齐备；
2. 人工裁决 §一 子体裁路由表与 marketing CTA 边界；
3. 修正档案 §2 篇幅数与 §4 标注进度（档案 v1 时处理）；
4. profiler 将 word_count 纳入 _aggregate.json 汇总字段。

## 附：档案/数据冲突清单（本文件编制时发现）

| # | 位置 | 档案说法 | JSON 证据 | 处置 |
|---|---|---|---|---|
| 1 | 档案 §2 对照表 | Cerebras 篇幅 median 2,036 词 | 逐篇 JSON word_count 重算 median 1,313（_aggregate.json 无该字段） | 以 JSON 为准；列入档案 v1 修订 |
| 2 | 档案 §4 待裁决项 | "语步标注已完成 1 篇，其余 9 篇待标注" | annotations/ 下 3 篇 .moves.jsonl；§3 聚合注记与 _moves-aggregate.md 均为 3 篇 | 档案自相矛盾，§4 表述过时 |
| 3 | 档案 §1 例证 | "treat iteration as cheap instead of precious" | 已核对存在于 corpus 原文（never-loop-without-verifiers 第 39 行） | 无冲突，仅记录已核验 |
