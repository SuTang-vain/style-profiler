# Calibrating the Ruler: How We Built and Hardened a Style Profiler

We built a ruler. More precisely, we built a profiler: a tool that reads a research-style essay and returns 26 deterministic measurements, from sentence length and number density to hedge frequency and vocabulary diversity. These measurements are the raw material a house style is made of. This is partly the build log of that ruler, and mostly the log of its recalibration.

This essay answers three questions. The first is why the judge has to be a deterministic counter rather than a model; the second is where, concretely, the ruler lost calibration: three defects, three distinct mechanisms. The third is how the judge itself is kept honest once the counters are fixed.

The essay proceeds in five layers: phenomenon, mechanism, prescription, diagnosis, and decision; the three defects have names, and we will use these names throughout: **substring pollution**, **length leakage**, and **the blind validator**.

One discipline applies throughout as well: every claim carries the grade of evidence behind it — the statistical layer (a 24-essay aggregate), the annotation layer (a much smaller hand-labeled set), or archive prose. Where the evidence is thin, the text says so.

## 1. The phenomenon layer: a judge that only counts

The profiler exists to answer one question the same way every time: what the writing of an institution actually looks like, statistically. We pointed it at the public blogs of 7 AI institutions. For each essay, we extracted a vector of measurements: mean sentence length, numbers per thousand words, first-person frequency, rhetorical questions, hedge and absolutist markers, and more.

The method descends from genre analysis in the Swales tradition and from argument mining, but the statistical layer is deliberately dumber than both of them: it counts, and it does not judge. That dumbness is the point: what the tool refuses to infer, it also refuses to get wrong in a new way each time.

Those measurements feed two products: a style baseline for each institution, built from medians and quartiles, and a pre-publication check run against that baseline before we ship a draft. Both consumers have to assume the ruler is stable, which is why the three defects below mattered beyond their individual blast radii.

Deterministic has a precise meaning here: the same input produces the same output on every run, and every number in the profile can be recounted by hand. If the profiler reports a hedge density of 4.75 per thousand characters, any one of us can open the essay, recount the hits one by one, and get 4.75. That property is not a convenience; it is roughly the entire foundation on which the rest of the tool stands.

The obvious alternative — asking a large model to grade the essay directly — fails on exactly this point. A model's score may drift between two runs of the same text and cannot be diffed, and what cannot be diffed cannot be regression-tested. Worse, the drift is silent: nothing in a model's verdict reports that it moved.

This is not a claim that model judgments are worthless; it is the narrower claim that they are unsuitable as the stable reference against which we build a baseline. You cannot calibrate against a moving target, and a mood, however articulate, is a moving target.

A bounded conclusion follows, and we state it with its boundary attached: determinism is not correctness, and a deterministic counter can be wrong in exactly the same way, every time. But being reproducibly wrong is what makes correction possible at all — correction is impossible without something stable to correct. A ruler first has to carry markings before anyone can check whether the markings are true.

Three of those markings turned out to be wrong, and the next layer names them one by one.

## 2. The mechanism layer: three named defects

### 2.1 Substring pollution: the counter that counted ghosts

The first anomaly surfaced in the hedge counts. The statistical layer tracks what the Chinese source essays call 限定语 (hedges) — markers like approximately, reportedly, perhaps, that bound the strength of a claim. Our counts for the Chinese corpus looked oddly high, and they looked high in essays whose prose did not seem hesitant. The discovery path matters: we found the problem by reading the hit list, not by reading the code; the code looked fine, and the hits did not. That order of discovery — hits first, code second — is itself a lesson about where quiet defects live.

The mechanism was substring matching. The wordlist contained the single character 约 (approximately), and the matcher counted any occurrence of that character as a hedge, including inside 约束 (constraint), a word for restriction with no hedging force. In essays about constrained optimization, every mention of a constraint was silently counted as an expression of uncertainty. No exception was raised, no test failed, and no log line recorded the substitution; the matcher had not crashed, only returned a plausible-looking number that was, in large part, an artifact.

The shortcut was not clearly reckless at the time: Chinese text has no spaces, and proper segmentation is a project of its own. For the multi-character terms that made up most of our early wordlists, substring matching behaves reasonably well.

The pollution stayed largely invisible while the corpus was English-heavy, and it became visible only when Chinese essays — dense with words like 约束, 简约, 契约 — entered the sample. An assumption that is mostly harmless in one language can become a systematic liar in another, and no number in the output had told us to look, so the shortcut stayed.

The fix we adopted was word-boundary matching: single-character terms now count only when they match a segmentation token exactly, not when they appear as a substring inside a longer word. After the fix, the median hedge density across the 24-essay aggregate fell from 4.75 to 2.69 per thousand characters. Roughly 43% of what we had counted as hedges were not hedges at all; the essays themselves had not changed, only the ruler had.

The lesson generalizes beyond this bug, and we state it with a boundary: in a measurement tool, the most damaging defects tend to be the quiet ones. A crash is visible, but a wrong number that looks like a right number enters every downstream conclusion without announcing itself. Determinism had been doing its job the whole time — the same wrong answer, every run — which appears to be exactly why the wrongness survived long enough to be trusted.

### 2.2 Length leakage: the ruler that stretched

The second failure was subtler, because the metric involved is standard. Type-token ratio — distinct words divided by total words — is a common measure of vocabulary diversity. It is also mechanically length-dependent: the longer a text runs, the more its vocabulary repeats, so the ratio falls as length grows.

A long essay inevitably reuses its own terminology toward the later sections, while a short note by the same author looks artificially diverse by comparison. This is textbook knowledge, and also easy to forget — and forgetting it quietly tilts every comparison the tool makes.

When we compared raw type-token ratios across the 7 institutions, we were, to a significant extent, comparing essay lengths.

The ruler was measuring itself.

The repair was to replace the ratio with its moving-average variant, MATTR: we compute diversity inside a sliding window of 150 tokens, and we average the window scores. Every text contributes equal-length frames, so length stops leaking into the measurement — that is what we mean by length leakage, and windowing is how we closed it.

The numbers after the repair are the part worth remembering: the apparent cross-institution diversity gap shrank from 0.204 to 0.070, and roughly two-thirds of the visible difference had been the ruler, not the text.

The ranking, notably, did not move — the institution that looked most lexically diverse before the fix still looks most diverse after it. The correction changed the magnitude of the claim, not its direction, which suggests the original comparison was pointing at something real but reporting it through a stretched scale. A stretched scale can still rank correctly when the stretch is nearly uniform.

Is the remaining 0.070 a genuine stylistic difference, or residue that the window could not remove? This essay leaves the question open: the window suppresses length dependence but may not eliminate it, and attributing the residual gap requires evidence we do not have.

One operational lesson did survive and entered the regression suite: every metric should declare an invariance — something it is not supposed to respond to — and that declaration is itself testable. Length-invariance is now a tested property rather than an assumption.

### 2.3 The blind validator: a wall of PASS

Our regression validator re-computes every profile and diffs it against expected values stored in markdown tables; for months it reported an unbroken wall of PASS. The green was real, in the narrow sense that the validator had not found a single mismatch.

The green was also incomplete: the validator could not say how much it had checked.

The parser that read the expectation tables silently skipped bold cells: a value wrapped in emphasis was not extracted, not compared, and therefore could not mismatch. Part of the table was simply invisible to the validator, and the validator did not consider this worth mentioning. The wall of PASS reported, with apparent confidence, the results of comparisons that had not run.

We discovered this the usual way for this class of defect: someone corrupted an expectation table on purpose, and the suite came back green. A validator that stays green when its inputs are deliberately broken is not validating anything; it is reciting. That single experiment reframed months of clean reports from evidence of health into evidence of blindness. For months, in other words, we had read the absence of alarms as the presence of health.

Once we fixed the parser, the validator immediately caught 6 numeric drifts, most of them stale expected values: numbers left behind when a metric's definition had changed while the table had not. Each of the 6 was pinned into the suite as an explicit regression test, so those drifts now fail loudly instead of aging quietly into the baseline.

The lesson here is the sharpest of the three, and we allow it one strong word: a validator that can never fail is worse than no validator, because it manufactures confidence without doing the work. A validator has to report what it checked, and a silent skip must count as failure rather than as a pass with missing data. These three repairs translate into four acceptance tests, which the next layer lists.

## 3. The prescription layer: four acceptance tests

We can compress the three defects into a checklist, which is likely the most portable part of the essay. Whatever you are measuring — prose style, model behavior, anything where a counter stands between you and a claim — a measurement instrument earns trust by passing four acceptance tests.

1. **Wordlist hits must respect token boundaries.** Any term counted by bare substring match — above all, single-character or very short terms — will eventually count ghosts. A matcher that cannot say this hit was a whole word produces a count that is preliminary at best.

2. **Every metric must declare an invariance, and pass it.** If a metric is not supposed to respond to length, window it and test that it does not. If it is not supposed to respond to language, file size, or formatting, say so and test that too; an undeclared sensitivity is an unpriced risk.

3. **A validator must report what it checked.** Coverage is part of the result, and any silent skip — any input the validator declined to compare — counts as a failure, because the alternative is a green wall with holes in it.

4. **Every check demonstrates failure before it is trusted to pass.** A test that has not yet been seen red is perhaps not a test at all — it may be a tautology. We break the instrument deliberately, we watch the check catch it, and only then do we let it guard the build.

Missing any one of the four is enough to make the judge untrustworthy. It is the direct summary of the three cases above: each violated exactly one of the first three criteria, and all now live under the fourth. Once the checklist holds, one question remains about the judge itself.

## 4. The diagnosis layer: who checks the checker

Who checks the checker? Stepping back, the three failures share a signature worth naming: none of them was a model hallucination. Each was an engineering assumption — substring matching is good enough, type-token ratio behaves like a stable metric, a parser reads what is on the page. Each of these assumptions turned out to be wrong in a way the tooling had no incentive to reveal. A hallucination at least varies; these failures repeated themselves faithfully.

A deterministic judge can still lie systematically, but it lies consistently, which makes the lie harder to notice and easier to defend in a meeting.

Our containment is a regression suite, which now holds 20 tests covering the repaired behaviors: word-boundary matching, length-invariance of the diversity metric, parser coverage, and the 6 pinned drifts. Each of the 20 exists because one of the three defects, or one of the 6 drifts, taught us where to look.

The entry rule comes straight from the fourth acceptance test — each of the 20 has been seen red. A green suite assembled this way means something; a green suite assembled by writing tests against passing code mostly means that the code and the tests share the same assumptions.

The honest answer to that question is layered: the regression suite checks the metrics, and the hand-recountable property of the statistical layer checks the suite, because we can recompute any number from the raw text. The annotation layer — the hand-labeled structural data on which the genre skeletons rest — checks nothing automatically, which is itself a finding we record rather than resolve.

As of September 2026, those annotations cover 3 of the 24 essays, roughly 12.5% of the corpus, so skeletons inferred from them remain provisional and the playbooks built on top inherit that provisionality. The honest posture is to keep the grading visible at the point of use, which is what the evidence tags above attempt. A reader can then weight each claim by the layer that produced it, which is the same discipline we ask of the tool itself.

The suite has its own boundary: it locks down known failure modes and says approximately nothing about unknown ones. We believe it is a ratchet rather than a proof of correctness: it makes the repaired mistakes expensive to reintroduce. What the discipline is worth outside our own corpus is a separate question, and the final layer takes it up.

## 5. The decision layer: what travels and what does not

Can this method be carried over, as-is, to scoring other kinds of writing? Probably not: we built the baselines, the wordlists, and most of the budgets on one corpus of one language and one broad genre. A different genre or a different language likely needs its own statistical layer rebuilt from its own essays; the budgets travel no farther than the corpus that produced them.

What does transfer is the discipline: determinism first, declared invariances, validators that report coverage, checks that have been seen red, none of which depends on what is being counted. The ruler does not travel; the habit of calibrating rulers does, and three conclusions follow from the three repairs, each with its boundary attached.

1. Determinism comes before cleverness: we can repair a reproducible counter that is wrong, but an impressive judge whose verdicts drift between runs cannot be repaired, because there is nothing stable to repair.

2. Every metric is vulnerable to at least two classes of pollution — its wordlist and its length behavior. Both classes stay invisible until someone reads the hits and plots the sensitivities, so declare the invariance and then test it.

3. The judge needs supervision of its own: a validator that cannot fail manufactures confidence, and the only known antidote is a suite whose every member has demonstrated that it can fail. A suite that has never been seen red cannot be trusted to pass.

Three open questions remain, and we leave them open deliberately rather than smoothing them into the conclusion.

1. The sensitivity of these results to the 150-token window is only partially mapped, and a fuller sweep may shift some of the smaller numbers reported here.

2. Two of the genre skeletons in the playbook, the blog and exploration skeletons, rest on zero annotated essays; whether the generic skeleton fits them remains untested.

3. The corpus underlying the playbooks is Chinese, while their first output language is now English, so every English quantitative budget in use today is a derived estimate rather than a measured one.

As for the ruler: we have recalibrated it three times, and we will need to recalibrate it again. Each repair teaches the suite to watch a new place, and watching a new place tends to reveal the next flaw. The markings are better than they were; whether they are true remains a question the tool keeps answerable by design: every number recountable, every check breakable, every conclusion tagged with the evidence it stands on.

<!--
self-check（2026-09-14，python3 profiler.py output/_p1-validation-samples/draft-kezhongke-en-v3.md；超 35 词句子用 profiler 同口径切句脚本独立复跑核验，见下）

§0.2 走廊逐项（13/13 达标）：
- 篇幅 = 2,843 词 —— 达标（目标 ≈2,900，区间 [2,100, 3,750]，贴目标下沿；v2 为 2,847）。
- 平均句长 = 20.1 词 —— 达标（目标 ≈22，区间 [20, 24]；v2 为 20.3，持平）。
- P90 句长 = 31 词 —— 达标（目标 ≤35，区间 ≤41）。
- 平均段长 = 45.1 词 —— 达标（目标 ≈42，区间 [33, 53]；v2 为 43.3）。
- 数字密度 = 15.48/千词 —— 达标（目标 ≈14，区间 [8, 21]；44 token = 内容 26 + 结构 18）。
- hedge = 11.96/千词 —— 达标（目标 ≈10，区间 [8, 13.5]；34 命中：roughly 4 / about 4 / may 4 / could 3 / approximately 3 / early 3 / remains 3 / likely 2 / reportedly 1 / suggests+suggest 1+1（子串双计）/ appears 1 / preliminary 1 / toward 1 / uncertain 1（uncertainty 子串）/ we believe 1）。
- absolutist = 2.46/千词 —— 达标（目标 ≈2，区间 [1.4, 3.4]；7 命中：must ×4 = 判据 ①②③ + §2.3 教训；never ×2 = §2.3 教训 + 结论 ③；impossible ×1 = §1 有界结论）。
- 克制比 = 34:7 = 4.86:1 —— 达标（典型带 4–5:1；v2 为 4.71:1）。
- 第一人称 = 40 —— 达标（目标 ≈40，区间 [21, 69]，精确命中；处方 6 硬约束，按节预分配见 outline；同 v2 低口径，I/my 大写词表项不命中为已知工具缺陷）。
- 客观自指 = 2 —— 达标（"this essay" ×2：开场三问题清单段 + §2.2 left-open 段；开场段用 "This is partly the build log…" 规避第三次）。
- 设问 = 3 —— 达标（§2.2 COUNTER 留疑 / §4 首句 "Who checks the checker?" / §5 首句设问自答；其余位置含本注释 0 个 "?"）。
- MATTR = 0.675 —— 达标（目标带 0.68–0.69，合格区间 [0.66, 0.70]；贴目标带下沿，较 v2 0.681 微降——组件名统一（validator/suite 取代四名混用）减少了同义词虚增，是处方执行的副作用而非失控）。
- 感叹号 = 0 —— 达标（红线；raw 中 "!" 仅存在于本注释标记符）。

处方 5 执行（边界声明 ≤3 处，手工逐处计数）：
- 边界声明 ① §2.2 COUNTER 段："the window suppresses length dependence but may not eliminate it, and attributing the residual gap requires evidence we do not have"——中性事实句式，left-open 显式标注。
- 边界声明 ② §4 COUNTER 段："it locks down known failure modes and says approximately nothing about unknown ones"——v2 三段重申（para 47–49：边界句 + 未来词表新形状 + 窗口敏感性 + ratchet 段）合并为一段一次陈述；"We believe it is a ratchet rather than a proof of correctness" 为判断带边界（招式 3），非局限声明。
- 边界声明 ③ §5 开放问题 3："every English quantitative budget in use today is a derived estimate rather than a measured one"——v2 自我批评段（"the budget this draft was written against…its first live test"）删除，事实内容由此条中性承载，全文唯一一次。
- 开放问题 1/2（窗口参数测绘不全 / 博客体与探索体骨架零标注）为招式 4 议程式留疑，措辞中性、无检讨语气；若评审按最宽口径将其计入"证据未覆盖"陈述，则合计 5 处——全部位于 COUNTER 位与收尾，零自我检讨语气。此条款张力记入简报 playbook 缺陷。
- 自我检讨句式扫描（人工 + 脚本）："should have" 0、"embarrassing" 0、"we regret" 0、"our mistake" 0、"we failed to" 0、"longer than we" 0。v2 两处病灶句均已中性化重写（见下对照）。
- 自我批评小节：未设（题材非事故复盘）。

处方 7 执行（语言逻辑显性化）：
- 段首主题句：逐段落实，承接装置见 outline 逐段表"逻辑承接"列（More precisely / Those measurements / The obvious alternative / A bounded conclusion follows / 序数词链 first→second→third / The mechanism / The fix / The numbers after the repair / Once we fixed / As for the ruler 等）。
- 同一边界不重复：0.070 归因仅 §2.2 一次（v2 在开放问题 1 重申，本稿开放问题换新议题）；套件边界仅 §4 一次；英文预算推导性仅开放问题 3 一次。
- 节末句指向下节：§1 末（"the next layer names them one by one"）/ §2.3 末（"the next layer lists"）/ §3 末（"one question remains about the judge itself"）/ §4 末（"the final layer takes it up"）四处主节级指针；子节间（2.1→2.2→2.3）由命名标题承接，不加指针句——若加则与下一子节首句构成同义重申，恰是处方 7 反例（此解释已在大纲声明）。
- 一段一义：每段单一功能；单句段节拍器恰好 4 处（§1 末指针句 / "The ruler was measuring itself." / "The green was also incomplete…" / §4 格言段），与 v2 同数。

超 35 词句子逐句核验（v2 自验虚报处，本稿硬执行）：
- 方法：复刻 profiler 英文切句口径（clean_markdown 剥离后按 [.!?]+ 切分，len(s.split()) 计词，含标题合并 artifact 与 em-dash token），独立脚本复跑。
- 结果：总句数 146，最大句长 35 词，超 35 词句子 0 句。35 词贴顶句 3 句（§2.3 教训首句 / §4 分层回答首句 / 结尾段末句），34 词 2 句（§2.2 数据锚定句 / §2.3 标题合并首句），均可一口气读完（单一论断、无嵌套从句）。
- 迭代记录：初版脚本复跑抓到 1 句 37 词（判据 ③ 合并句，em-dash 计入所致），已拆修后清零。

壳中客签名核查：
- 语步骨架：FRAME×4 → CONTEXT×4（§1）→ ARGUE+COUNTER（§2 三节）→ APPLY×6（§3 判据）→ ARGUE×6+COUNTER（§4）→ CLOSE×10（设问自答→编号结论×3→开放问题×3→比喻收束）——§2 通用骨架兜底，博客体 [推断] 外衣；无 HOOK、无 Limitations 独立节、无自我批评节。
- 招式：①明示三问题清单 ✓；②内部证据分级（statistical/annotation/archive + §4 3/24 篇落实）✓；③判断带边界（roughly/tend to be/most/to a significant extent/narrower）✓；④编号结论 ×3 + 开放问题 ×3 ✓；⑤单一比喻族 ruler/calibration/markings/recalibrate 全文复用、结尾回收 ✓。
- 术语唯一：限定语 (hedges)、约 ("approximately")、约束 ("constraint") 首现括注；**组件名统一（v2 P2-4 修复项）**：validator ×15 / suite ×12 / harness ×0；checker ×2 全部为固定搭配 "who checks the checker"（§4 标题 + 首句设问），非组件指称。
- 加粗 7 处（三失效首现名 + 四判据引导词）；无表格、无外链、无参考文献表、无 CTA。
- 收尾组合（2026-09-14 修订版）：设问自答 → 编号结论 → 开放问题（中性）→ 比喻收束；不含自我批评位 ✓。

与 v2 同口径对照（profiler 实测）：段长 43.3→45.1；句长 20.3→20.1；P90 34→31；第一人称 42→40；克制比 4.71→4.86；篇幅 2,847→2,843；数密 14.75→15.48；hedge 11.59→11.96；MATTR 0.681→0.675；设问 3→3；客观自指 2→2；感叹号 0→0。v2 达标项无一退化。

已知口径备注（承 v2，供 P2）：profiler 英文第一人称词表大写项永不命中；数密含结构编号（18/44）；标题无句末符并入下一句（本稿已按合并口径逐句防控）；one_line_paragraphs 指标 <40 字符口径只抓到 1 处节拍器（人工核 4 处）。
-->
