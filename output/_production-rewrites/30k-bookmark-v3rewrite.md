---
type: note
domain: 科研
status: active
date: 2026-09-04
privacy: internal
tags: [信息库, 科研]
rewrite: v3-style 2026-09-14
---

# How to Be Good at Research: A Deep Reading of a 30,000-Bookmark Essay

*Research methodology in the AI era — Kezhongke (壳中客), a nonprofit research community. Sources linked inline; research current as of September 2026.*

On June 10, 2026, a long-form essay titled "how to be good at research" appeared on X. It had no news hook, covered no new model or paper, and its author, vivek, is not a public figure. Within weeks it had drawn 12.7k likes, 2,197 retweets, and the number that matters most: 30,350 bookmarks.

That last figure is roughly 2.4 times the likes, and the ratio suggests more than a like: in the attention economy of X, a like is a gesture, while a bookmark is a filing decision. Thirty thousand people put the essay in the drawer labeled "use later."

What makes a research-methodology essay with no news in it earn reference treatment?

To answer it, we read the full text, we checked every citation it makes, and we placed it in the lineage of classic research-craft literature. We call that lineage the craft literature throughout: the talks, guides, and essays through which the research community transmits its method. It runs from Hamming's 1986 lecture at Bell Labs to Olah and Carter's "Research Debt" in 2017.

This essay answers three questions: what the essay argues, where its reasoning holds and where it has structural flaws, and what kind of document it is. The last answer determines how you should use it.

Two names carry the argument: the first is the essay's own unit of skill, the muscle, of which it names seven. The second is ours: the essay as a map of tacit knowledge, a term the rest of this essay carries. One discipline applies throughout: we state each judgment with its source attached, and where the evidence is thin, the text says so; we start with what the essay argues.

## What the essay argues: the seven muscles

The thesis fits in one sentence: research ability is not a gift but a stack of smaller skills, and nearly every one can be deliberately trained. Most people reverse-engineer the profession from its visible outputs — papers, threads, announcements — and what they learn is to look like a researcher.

That reversal is the essay's quiet target: the visible profession teaches posture, while the craft itself teaches method. The body of the essay splits the stack into 7 sections, one muscle each, and we take them in the essay's order.

**Muscle one: pick your own problems** — the essay opens with Hamming's habit at Bell Labs, and he would ask whoever sat near him at lunch what the important problems in their field were. Then he would ask why they were not working on them, and people changed tables.

The question stings because most of us do not choose problems. We absorb them from an advisor, from whatever a big lab announced last quarter, from the paper everyone is quote-tweeting this week.

An absorbed problem leaves you holding the conclusion without the reasoning: you know a famous lab cares, but not why, not what it expects to find, not what would make it walk away. When the lab pivots, you find out a year later.

According to John Schulman's guide to ML research, the essay splits the work into two modes. One reads the literature and hunts for improvements; the other chooses an outcome you genuinely want to exist and reasons backwards to the experiments, and Schulman argues for the second. The quiet reason is that a goal you actually care about drags you into territory no survey covers — originality is a byproduct of goal-driven work.

**Muscle two: upgrade your inputs** — shared reading lists produce shared ideas. If your information diet is the arXiv trending page plus whatever survives the group-chat filter, you will likely reach the same conclusions as everyone else, at the same time. Conclusions shared by the whole field are worth approximately nothing.

The alternative has two layers, and the first is to go old: the field reruns its own past on a delay, with mixture of experts from 1991 and LSTMs from 1997. Sutton's thousand-word "Bitter Lesson" of 2019 predicts the field's shape better than surveys ten times its length.

The second layer is to go sideways: interpretability borrows shamelessly from neuroscience, and eval design is mechanism design wearing a lab coat. A working sense of how GPUs move memory tells you which architecture papers are doomed before the benchmarks do.

The plainest layer is to read the paper, not the thread summarizing it. The appendix is where the bodies are buried, and the limitations section is usually the most honest paragraph in the document.

**Muscle three: write everything down** — Paul Graham observed that an idea can feel fully formed right up until you try to put it into words. The page finds the gaps your head papers over — the untested assumption, the step that does not follow, the two claims that quietly contradict each other.

Darwin made it procedural: any fact that cut against his theory got written down on the spot, because he had caught his memory deleting inconvenient evidence faster than the convenient kind. So the essay's 5-field experiment log: hypothesis, setup, expectation, result, updated belief.

**Muscle four: tighten the loop** — the stories told about Alec Radford rarely involve a single stroke of genius; they involve volume. More runs per day, more wrong ideas discarded per week, a model of reality that updated faster than anyone else's.

That yields the essay's key sentence — "research speed is mostly the speed at which you discover you're wrong" — which makes tooling a first-class research activity, essential rather than ancillary. Launching a run should be one command, comparing two runs should take seconds. The highest-yield step in Karpathy's recipe is overfitting a single batch for 30 seconds before training at scale — half your bugs, gone.

**Muscle five: stare at the outputs** — a descending loss curve is not analysis; it is reassurance. Experiments throw off far more information than you consume — transcripts, failure cases, the strange tail of the distribution — and most of it dies unread in a logs folder.

Andrew Ng has taught the same unglamorous move for roughly a decade: pull 100 failures, read all of them, sort them into piles, attack the biggest pile. One transcript of genuinely strange behavior teaches more than the next decimal of accuracy.

**Muscle six: wander on purpose** — your first subfield is an accident of timing, so treat it like one: pay tuition in interpretability, in evals, in RL, in systems, before deciding where you live. Somewhere in the field there is a corner where your specific weirdness is an unfair advantage.

The exploratory posture has an operational form too: run the disposable version of every idea, and let most of them die young. Tune baselines until it hurts, and ablate until you know which component carries the result — "it's usually one, and it's usually not the one in the title," the essay notes.

**Muscle seven: find your people** — Hamming observed that colleagues with closed doors got more done in any given year. Colleagues with open doors did the work that mattered, because the interruptions carried information about what the world actually needed.

Generosity compounds: replicate a result and publish what you find, release the tool you built for yourself, explain something hard in plain language. The returns arrive sideways, months later, as the collaboration or reference or role you couldn't have applied for. That is the stack the thirty thousand bookmarkers filed away, and why this stack earned reference treatment is the question we turn to next.

## Why the argument works: tacit knowledge made explicit

Why would thirty thousand researchers file away an essay that contains no new results?

The answer may lie less in any single claim than in the essay's documentary form. Every claim is anchored to a checkable primary source: Hamming's "You and Your Research" talk, Schulman's guide, Karpathy's recipe, Olah and Carter's "Research Debt," Ng's error-analysis methodology, Darwin's record-keeping habit, Feynman's commencement address.

The result is not a collage of secondhand motivation. We read it as a compressed restatement of the research community's canonical craft literature — tacit knowledge scattered across talks, blogs, and interviews, organized into a structured checklist.

The anchors are not all of one kind, so a note on source layering is in order: eight of the references are linked primary sources, listed in the Sources section, and we rechecked each one. A few others — Darwin's habit, Ng's teaching, Feynman's address, and the stories about Radford — travel unlinked, so we treat them as community-transmitted accounts rather than verified citations.

That form seems to explain the bookmarks: mentorship is supposed to transmit these things, but mentorship is a lottery. Draw an advisor who is willing and able to teach and you learn; otherwise you reverse-engineer from visible outputs, and what you reverse-engineer is the performance, not the capability.

The essay appears to hit this structural gap precisely: it delivers, publicly and at no cost, the transmission the lottery failed to deliver. According to Olah and Carter, writing in "Research Debt" in 2017, fields choke on undigested ideas, and a clear explanation is a genuine contribution rather than a service job. The essay is itself an instance of that claim.

Its second strength is operability. Every piece of advice carries an explicit action and a feedback mechanism: predict, then check; cover the results and guess; the 5-field log; the 30-second overfit; the 100 failures.

This is the structure of deliberate practice — a target, feedback, correction — rather than the empty "read more, think harder" advice. Operability also explains why the essay works as a reference document: a checklist survives bookmarking in a way an argument does not, because each line can be used without reading the whole essay.

A strong form and an actionable checklist do not by themselves make an argument true, so the essay's structural boundaries deserve equal documentation, and we record them next.

## Where the argument has flaws: four structural limits

Four flaws are worth recording, and we record each with its status: what has an answer and what remains open. **Flaw one: survivorship bias runs through the whole piece** — every example is a methodological retrospective of a winner: Radford's volume, Karpathy's manual procedures, Darwin's record-keeping. Plenty of researchers who stared at outputs failed anyway, and plenty who tightened their loops iterated fast in a wrong direction.

The essay cannot answer "what is the conditional success rate of this method," because it sampled only successes. This is not the essay's defect alone — it is the structural limit of the craft genre — and we leave it open: no revision from inside the genre can fix it.

**Flaw two: zero empirical evidence** — not a single controlled study or quantitative result supports the efficacy of any recommendation. "Predict-and-correct trains taste" sounds plausible, but it has never been tested, and at the evidence level it is indistinguishable from a hundred other plausible-sounding self-improvement claims.

The essay's evidence grade is therefore the same as Hamming's talk itself — wise, unverified; it might be true, and the point is that we do not know. The status we assign is a reading rule, not a rebuttal — the essay deserves to be used as a list of hypotheses, not a list of conclusions.

**Flaw three: a strong disciplinary bias, undeclared** — every concrete technique (loss curves, baseline tuning, overfitting one batch, reading transcripts) comes from empirical machine-learning research. It barely transfers to mathematics, where proofs have no experiment loop.

It transfers little to wet-lab disciplines, where "launch a run in one command" meets a 30-month clinical pipeline, and the humanities have no ablation at all. The essay contains no boundary statement, so the reader must perform the transfer judgment alone — a flaw fixable at the reading end, and rule three in the next section is the fix.

**Flaw four: a hidden premise of resource availability** — "more runs per day" presumes compute; "read the paper, not the thread" presumes time; "pay tuition in several subfields" presumes you can afford the tuition. For resource-constrained researchers, the marginal returns of this advice likely diminish quickly; the essay assumes universal feasibility throughout, and we flag the premise as asserted rather than demonstrated.

None of the four flaws cancels the checklist; each one reprices it. Putting the strengths and the limits together yields a precise classification, which we state next.

## What the document is, and how to use it

The classification fits in one line: the essay is a map of tacit knowledge made explicit, not a validity argument. A map compresses terrain someone else has walked; it does not prove the terrain is walkable for you, and it may not even be current. Three rules for using this kind of document follow, one per failure mode a reader could make: believing it, skimming it, or reading it as timeless.

**Rule one: use it as a checklist, not a doctrine** — none of the 7 sections requires faith, and each is worth an N=1 experiment in your own work. Run "predict-before-run" for a month and see whether your hit rate on experimental outcomes improves; that month teaches you more than believing or doubting the claim.

**Rule two: follow its citations to the originals** — the Hamming talk, the Schulman guide, the Karpathy recipe, and "Research Debt" are all linked below, and the essay's most durable value may be curatorial. Its own rule applies to itself: read the paper, not the thread about the paper, and not only the essay about the paper. We would start with the Hamming talk and the Schulman guide, the two that carry the argument.

**Rule three: mind its silence** — the loop this 2026 essay describes (literature, code, experiments, outputs) was, at that very moment, being rewritten by AI on every link. The text says nothing about any of them; it is an accurate old map drawn on new terrain.

That silence has a subject of its own — how the 2024–2026 record re-sorts which of these 7 muscles are appreciating and which depreciating — and the companion piece examines that record.

[[EN-The Research Craft in the Age of AI - Judgment Is the Only Asset Still Compounding|*The Research Craft in the Age of AI: Judgment Is the Only Asset Still Compounding*]].
What the map itself is worth is the question we close with.

## Closing: the map is not the territory

What are 30,350 bookmarks actually worth? Our answer: a filing decision at scale — evidence of a shared gap, not yet evidence of transmitted capability.

Hamming's lunch-table question stings because what it exposes is not a capability gap but a choice gap. Most people have never actually chosen their research problem, just as most people have never actually learned how to do research. We believe the essay's largest contribution is to turn "how to do research" from an untransmittable master-apprentice secret into a public, checkable, deliberately trainable checklist.

Three conclusions follow, and we state each with its boundary attached. They are bounded because the essay's own evidence is bounded.

1. The essay's value is documentary: it compresses the craft literature into 7 trainable muscles, and nearly every claim traces to a named primary source, 8 of which are linked and rechecked.
2. Its evidence grade is hypothesis-level: 0 controlled studies support any of the 7 muscles, so each one earns its place in a research practice through an N=1 test, not through faith.
3. Its scope is bounded and undeclared: the techniques presume empirical machine learning, plus compute and time, and outside that scope the transfer judgment belongs to the reader.

Three open questions remain, and we leave them open deliberately. They state what the evidence does not yet cover, not what the essay got wrong.

1. The conditional success rate of these methods remains unmeasured: no controlled comparison exists, and none is likely to arrive soon, because the treatment is a practice rather than a pill.
2. How AI assistance re-sorts the 7 muscles remains unsettled: the 2024–2026 record is still accumulating, and the companion piece tracks it.
3. Whether the 30,350 bookmarkers' research actually improved remains unknown: the real evaluation happens in their work roughly 3 years from now, and it is unclear whether anyone will measure it.

As for the map: a map is not the territory, and a checklist is not capability. The Darwin procedure the essay quotes — write down the evidence against you on the spot — implies that a methodology essay realizes its value only through being used, tested, and argued against. Thirty thousand bookmarks are a starting point; the rest happens off the page.

---

**Sources**

- [vivek: how to be good at research (X long-form, June 10, 2026)](https://x.com/itsreallyvivek/article/2064686372737454155).
- [Richard Hamming: You and Your Research (Bell Labs talk, 1986)](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html).
- [John Schulman: An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html).
- [Andrej Karpathy: A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/).
- [Chris Olah & Shan Carter: Research Debt (Distill, 2017)](https://distill.pub/2017/research-debt/).
- [Rich Sutton: The Bitter Lesson (2019)](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).
- [Paul Graham: Writes and Write-Nots](https://paulgraham.com/writes.html).
- [Jacobs & Jordan et al.: Adaptive Mixtures of Local Experts (1991, the MoE origin paper)](https://www.cs.toronto.edu/~hinton/absps/jjnh91.pdf).

---

*Kezhongke (壳中客) is a nonprofit research community. The companion piece, "The Research Craft in the Age of AI," examines how the 2024–2026 evidence re-sorts this same skill stack. If you have run your own N=1 experiment against this checklist, we would like to hear your hit rate.*

<!--
self-check（2026-09-14；python3 /Users/tangyaoyue/DEV/style-profiler/profiler.py ＜本文件＞；超 35 词句子用复刻 profiler 切句口径的独立脚本逐句核验）

路由声明（playbook §1）：行业分析。证据：场景 HOOK（2026-06-10 X 帖+互动数据并置）+ FRAME 明示三问清单 + COUNTER 独立节（4 缺陷逐条）+ APPLY 判据节（3 使用规则）+ 系列预告/信源征集收尾——命中 §1 路由操作指令「场景 HOOK + 问题清单 + 系列预告 → 行业分析」，规则层可识别；骨架证据等级 [标注-1篇]（fde-role-renaissance 单篇标注外推，见 playbook §1 表）。profiler genre_guess 对本英文稿返回 blog_or_exploration，系规则关键词为中文的口径空档，以人工路由为准。本文证据分级：8 条一手信源内嵌保留（文末 Sources，URL 逐字）+ 4 条未链接转述（Darwin/Ng/Feynman/Radford，正文已显式标注为 community-transmitted accounts）。

§0.2 走廊逐项（13/13 达标）：
- 篇幅 = 2,837 词 —— 达标（目标 ≈2,900，区间 [2,100, 3,750]，贴目标）。
- 平均句长 = 20.8 词 —— 达标（目标 ≈22，区间 [20, 24]）。
- P90 句长 = 31 词 —— 达标（目标 ≤35，区间 ≤41）。
- 平均段长 = 43.2 词 —— 达标（目标 ≈42，区间 [33, 53]，贴目标）。
- 数字密度 = 19.03/千词 —— 达标（目标 ≈14，区间 [8, 21]；54 token：原文互动数据/年份/结构化数字全保留；行业分析题材按处方 4 在带内取高位）。
- hedge = 11.98/千词 —— 达标（目标 ≈10，区间 [8, 13.5]；34 命中：about 7 / remains 4 / roughly 3 / likely 3 / may 3 / according to 2 / could 2 / suggests+suggest 1+1（子串双计）/ early 2（两处均为 nearly 的子串命中，词表子串口径已知 artifact）/ approximately 1 / might 1 / seems 1 / appears 1 / unclear 1 / we believe 1）。
- absolutist = 2.47/千词 —— 达标（目标 ≈2，区间 [1.4, 3.4]；7 命中：never 3 / everyone 2 / must 1 / essential 1）。
- 克制比 = 34:7 = 4.86:1 —— 达标（典型带 4–5:1；红线为克制比 ＜3:1）。
- 第一人称 = 27 —— 达标（目标 ≈40，区间 [21, 69]；文献评述题材的 we 叙事需求弱于 build-log 题材，按节预分配后落带内中段；profiler 大写 I/my 词表项永不命中为已知工具缺陷，本篇未用第一人称单数）。
- 客观自指 = 2 —— 达标（"this essay" ×2：FRAME 三问清单段 + FRAME 术语命名段 "the rest of this essay carries"；vivek 原文全文统一称 "the essay"，本稿自称仅 2 处，见术语纪律）。
- 设问 = 3 —— 达标（HOOK 末 / §2 首 / §5 首设问自答；其余位置含 Sources 与引文 0 个 "?"）。
- MATTR = 0.700 —— 达标（区间 [0.66, 0.70] 含端点，本稿贴上沿：信源区 8 条专名+引文清单使 lexical diversity 天然偏高；经 12 处同义单例词归一（canon/afterlife/lockstep/spine/formula/invisible/warranted/unpacks/answered 等 → 固定术语）自 0.707 压至带内；对 judge-v3 所指「术语统一拉低 MATTR」方向性冲突的处置：保术语唯一签名，MATTR 贴线达标）。
- 感叹号 = 0 —— 达标（红线）。

处方 5 执行（边界声明 ≤3 处、中性事实句、集中 COUNTER 位与收尾）：
- 自我检讨语气扫描（人工+脚本）："should have" 0 / "embarrassing" 0 / "we regret" 0 / "our mistake" 0 / "we failed to" 0。
- COUNTER 位 4 条缺陷为评论对象（vivek 原文）的结构分析，各带处理状态标签（left open / reading rule not rebuttal / fixable at the reading end / asserted rather than demonstrated），均为中性事实句，非本篇自我批评。
- 收尾开放问题 ×3 属招式 4 签名装置（按 judge-v3 划界不计入 ≤3 限额），引导句 "They state what the evidence does not yet cover, not what the essay got wrong" 明示中性定位。
- 自我批评小节：未设（题材非事故复盘）。

处方 7 执行（语言逻辑显性化）：
- 段首主题句＝该段结论，一段一义；段间承接逐段落实（That last figure / To answer it / The question stings / An absorbed problem / According to / The alternative / The second layer / The plainest layer / Darwin made it procedural / That yields / Andrew Ng has taught the same / The exploratory posture / Generosity compounds / That is the stack / The answer may lie / The result is not / The anchors are not all of one kind / That form seems / The essay appears to hit / Its second strength / This is the structure / A strong form / None of the four flaws / The classification fits in one line / Its own rule / The text says nothing / That silence / What the map itself is worth / Our answer / Three conclusions follow / Three open questions remain / As for the map；序数链 Muscle one→seven / Flaw one→four / Rule one→three / 结论 1→3 / 开放问题 1→3）。
- 同一边界不重复：4 缺陷各陈述一次；信源分层仅 §2 一次（Sources 区引导句与之重复，已删）；map/territory 边界仅收尾一次。
- 每主节末句指向下节：FRAME 末（we start with what the essay argues）→ §1；§1 末（the question we turn to next）→ §2；§2 末（we record them next）→ §3；§3 末（which we state next）→ §4；§4 末（the question we close with）→ §5。
- 单句段节拍器恰好 4 处（HOOK 设问 / §2 设问 / §2→§3 指针句 / §4 系列预告句），达处方上限、无超用。

超 35 词句子逐句核验：
- 方法：复刻 profiler 口径（clean_markdown 剥离后按 [.!?]+(空白|结尾) 切分，len(s.split()) 计词，含数字/em-dash/标题合并/wikilink token），独立脚本复跑。
- 结果：总句数 141，最大句长 35 词，超 35 词 0 句。35 词贴顶 2 句（HOOK 次段首句 / §2 信源分层首句），34 词 3 句（§1 标题合并句 / Muscle one 首句 / Muscle six 首句），均单一论断、无嵌套从句，可一口气读完。
- 迭代记录：初版 3 句超 35（病因：句号在引号内 ." 不触发切句导致跨句合并；wikilink 未独立成句），修复＝引文不置句尾/句号外置/wikilink 独立成段加句点，复跑清零。

壳中客签名核查：
- 语步骨架（行业分析）：HOOK（场景+数据并置）→ CONTEXT（钩子展开 + craft literature 术语定义）→ FRAME（明示三问 + 核心概念命名 muscle/map + 判断带信源纪律声明）→ ARGUE 节群（§1 七肌肉 / §2 为何成立）→ COUNTER 独立节（§3 四缺陷逐条带处理状态）→ APPLY（§4 分类 + 三规则）→ CLOSE（§5：设问自答 → 编号结论 ×3 → 开放问题 ×3 → 比喻收束）；系列预告于 §4 末+文末落款，信源征集于文末落款（N=1 回执邀请）；无自我批评位（2026-09-14 修订版收尾组合）。
- 招式：①明示三问题清单 ✓；②信源分层（一手链接 8 条 / 未链接转述 4 条显式标注 community-transmitted；according to / the essay notes 转述标信源属性）✓；③判断带边界（nearly every / most / roughly / likely / may 等）✓；④编号结论 ×3 + 开放问题 ×3 ✓；⑤单一比喻族 map/terrain/territory 全文复用、结尾回收（As for the map）✓。
- 术语全文唯一：the essay＝vivek 原文；this essay＝本稿（仅 2 处）；the seven muscles＋muscle one…seven；craft literature（CONTEXT 定义后全程复用）；the map（FRAME 命名）；the loop；filing decision；reference treatment。
- 感叹号 0；加粗仅用于 Muscle/Flaw/Rule 结构名（14 处）；无表格；内文外链 0（链接集中于 Sources 区，8 条 URL 全保留）；无引文标记 [n]。
- 人名/数据/引文/出处保真：12.7k likes / 2,197 retweets / 30,350 bookmarks / June 10, 2026 / MoE 1991 / LSTM 1997 / Bitter Lesson 2019（年份自原文 Sources 区移至正文信源标注）/ 5-field log / 30-second overfit / 100 failures / N=1 / 2024–2026 与原文一致；两处逐字引文（"research speed is mostly the speed at which you discover you're wrong" / "it's usually one, and it's usually not the one in the title"）原文照录；companion 双链保留。

信息保真说明（删/并/移/补）：
- 并：like/bookmark 对比与 "use later" 抽屉意象并段；Schulman 双模式与 originality 句并段；§2 可操作性内容重排为「结构 + 后效」两段。
- 删：Sources 区引导句（与 §2 信源分层句同义重复，处方 7）；零事实删除。
- 移：原文末段 "the real evaluation will happen in the bookmarkers' research three years from now" 移入开放问题 3（内容保留）。
- 补（承接/组织性补写，零新事实/人名/数据/引文）：§1 visible profession 与 craft 对照承接句；§2 信源分层句与 checklist 后效句；COUNTER 各缺陷处理状态标签；编号结论/开放问题框架句。

已知口径备注：profiler 英文大写 I/my 不命中（本篇未用第一人称单数）；"nearly" 计入 hedge 词 "early" 子串（×2）、"suggests" 与 "suggest" 双计——词表子串口径已知行为，命中明细如上；标题无句末符并入下一句（已按合并口径逐句防控）；Obsidian wikilink 文本计入句长与词数（30 token，已独立成句）；Sources 列表各行已补句尾句点保证逐条切句。
-->
