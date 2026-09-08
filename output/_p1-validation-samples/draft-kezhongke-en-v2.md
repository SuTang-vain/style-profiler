# Calibrating the Ruler: How We Built and Hardened a Style Profiler

We built a ruler. More precisely, we built a profiler: a tool that reads a research-style essay and returns 26 deterministic measurements — sentence length, paragraph length, number density, hedge frequency, vocabulary diversity, and the other raw material that a house style is made of. This is partly the build log of that ruler, and mostly the log of its recalibration.

This essay answers three questions. The first is why the judge has to be a deterministic counter rather than a model. The second is where, concretely, the ruler lost calibration — three defects, three distinct mechanisms. The third is how the judge itself is kept honest once the counters are fixed.

The essay proceeds in five layers: phenomenon, mechanism, prescription, diagnosis, decision. The three defects have names, and we will use these names throughout: **substring pollution**, **length leakage**, and **the blind validator**.

One discipline applies throughout as well: every claim carries the grade of evidence behind it — the statistical layer (a 24-essay aggregate), the annotation layer (hand-labeled data, a much smaller set), or archive prose. Where the evidence is thin, the text says so rather than smoothing it over.

## 1. The phenomenon layer: a judge that only counts

The profiler exists to answer a simple question — what the writing of a given institution actually looks like, statistically — and to answer it the same way every time. We pointed it at the public blogs of 7 AI institutions. For each essay, we extracted a vector of measurements: mean sentence length, numbers per thousand words, first-person frequency, rhetorical questions, hedge and absolutist markers, and more.

The method descends from genre analysis in the Swales tradition and from argument mining, but the statistical layer is deliberately dumber than both of them: it counts, and it does not judge.

Those measurements feed two products: a style baseline for each institution — medians and quartiles rather than means — and a pre-publication check that compares a draft against that baseline before it ships, and both consumers must be able to assume the ruler is stable. That is why the three defects below mattered beyond their individual blast radii.

Deterministic has a precise meaning here: the same input produces the same output on every run, and every number in the profile can be recounted by hand. If the profiler reports a hedge density of 4.75 per thousand characters, an analyst can open the essay, recount the hits one by one, and get 4.75. That property is not a convenience; it is roughly the entire foundation on which the rest of the tool stands.

The obvious alternative — asking a large model to grade the essay directly — fails on exactly this point. A model's score may drift between two runs of the same text and cannot be diffed, and what cannot be diffed cannot be regression-tested.

This is not a claim that model judgments are worthless; it is the narrower claim that they are unsuitable as the stable reference against which a baseline is built. You cannot calibrate against a moving target, and a mood, however articulate, is a moving target.

A bounded conclusion follows, and we state it with its boundary attached: determinism is not correctness, and a deterministic counter can be wrong in exactly the same way, every time. But being reproducibly wrong is what makes correction possible at all — correction is impossible without something stable to correct. A ruler first has to carry markings before anyone can check whether the markings are true.

Three of our markings turned out to be wrong.

## 2. The mechanism layer: three named defects

### 2.1 Substring pollution: the counter that counted ghosts

The first anomaly surfaced in the hedge counts. The statistical layer tracks what the Chinese source essays call 限定语 (hedges) — markers like approximately, reportedly, perhaps, that bound the strength of a claim. Our counts for the Chinese corpus looked oddly high, and they looked high in essays whose prose did not seem hesitant. The discovery path matters: we found the problem by reading the hit list, not by reading the code; the code looked fine, and the hits did not.

The mechanism was substring matching. The wordlist contained the single character 约 (approximately), and the matcher counted any occurrence of that character as a hedge — including its occurrence inside 约束 (constraint), a word for restriction that carries no hedging force whatsoever. In essays about constrained optimization, every mention of a constraint was silently counted as an expression of uncertainty. No exception was raised, no test failed, and no log line recorded the substitution; the matcher had not crashed, only returned a plausible-looking number that was, in large part, an artifact.

In the matcher's defense, the shortcut was not clearly reckless at the time: Chinese text has no spaces, and proper segmentation is a project of its own. For the multi-character terms that made up most of our early wordlists, substring matching behaves reasonably well.

The pollution stayed largely invisible while the corpus was English-heavy, and it became visible only when Chinese essays — dense with words like 约束, 简约, 契约 — entered the sample. An assumption that is mostly harmless in one language can become a systematic liar in another. We kept the shortcut longer than we should have, because nothing in the output told us to look.

The fix we adopted was word-boundary matching: single-character terms now count only when they match a segmentation token exactly, not when they appear as a substring inside a longer word. After the fix, the median hedge density across the 24-essay aggregate fell from 4.75 to 2.69 per thousand characters, and roughly 43% of what we had counted as hedges were not hedges at all; the essays themselves had not changed, only the ruler had.

The lesson generalizes beyond this bug, and we state it with a boundary: in a measurement tool, the most damaging defects tend to be the quiet ones. A crash is visible, but a wrong number that looks like a right number enters every downstream conclusion without announcing itself. Determinism had been doing its job the whole time — the same wrong answer, every run — which appears to be exactly why the wrongness survived long enough to be trusted.

### 2.2 Length leakage: the ruler that stretched

The second failure was subtler, because the metric involved is standard. Type-token ratio — distinct words divided by total words — is a common measure of vocabulary diversity. It is also mechanically length-dependent: the longer a text runs, the more its vocabulary repeats, so the ratio falls as length grows.

A long essay inevitably reuses its own terminology toward the later sections, while a short note by the same author looks artificially diverse by comparison. This is textbook knowledge, and also easy to forget — and forgetting it quietly tilts every comparison the tool makes.

When we compared raw type-token ratios across the 7 institutions, we were, to a significant extent, comparing essay lengths.

The ruler was measuring itself.

The repair was to replace the ratio with its moving-average variant, MATTR: we compute diversity inside a sliding window of 150 tokens, and we average the window scores. Every text contributes equal-length frames, so length stops leaking into the measurement — that is what we mean by length leakage, and windowing is how we closed it.

The numbers after the repair are the part worth remembering: the apparent cross-institution diversity gap shrank from 0.204 to 0.070, and roughly two-thirds of the visible difference had been the ruler, not the text.

The ranking, notably, did not move — the institution that looked most lexically diverse before the fix still looks most diverse after it. The correction changed the magnitude of the claim, not its direction, which suggests the original comparison was pointing at something real but reporting it through a stretched scale.

Is the remaining 0.070 a genuine stylistic difference, or residue that the window could not remove? We left this question open, and this essay leaves it open too: the window suppresses length dependence but may not eliminate it, and attributing the residual gap would require evidence we do not currently have.

One operational lesson did survive and entered the regression suite: every metric should declare an invariance — something it is not supposed to respond to — and that declaration is itself testable. Length-invariance is now a tested property rather than an assumption.

### 2.3 The blind validator: a wall of PASS

The third failure lived in the harness, not the metrics. Our regression harness re-computes profiles and diffs them against the expected values we store in markdown tables, and for months it reported an unbroken wall of PASS. The green was real, in the narrow sense that the validator had not found a single mismatch.

It was also meaningless, and the reason took an embarrassingly long time to see.

The parser that read the expectation tables silently skipped bold cells: a value wrapped in emphasis was not extracted, not compared, and therefore could not mismatch. Part of the table was simply invisible to the checker, and the checker did not consider this worth mentioning. The wall of PASS reported, with apparent confidence, the results of comparisons that had not run.

We discovered this the usual way for this class of bug: someone corrupted an expectation table on purpose, and the suite came back green. A validator that stays green when its inputs are deliberately broken is not validating anything; it is reciting. That single experiment reframed months of clean reports from evidence of health into evidence of blindness.

We had built the checker to answer "did anything change", and it could not even say how much it had checked.

Once we fixed the parser, the validator immediately caught 6 numeric drifts, most of them stale expected values — numbers left behind when a metric's definition had changed while the table had not been updated to match. Each of the 6 was pinned into the suite as an explicit regression test, so those drifts now fail loudly instead of aging quietly into the baseline.

The lesson here is the sharpest of the three, and we allow it one strong word: a validator that can never fail is worse than no validator, because it manufactures confidence without doing the work. A checker has to report what it checked — the comparisons attempted, not merely the verdicts returned — and a silent skip must count as failure rather than as a pass with missing data.

## 3. The prescription layer: four acceptance tests

We can compress the three defects into a checklist, which is likely the most portable part of the essay. Whatever you are measuring — prose style, model behavior, anything where a counter stands between you and a claim — a measurement instrument earns trust by passing four acceptance tests.

1. **Wordlist hits must respect token boundaries.** Any term counted by bare substring match — above all, single-character or very short terms — will eventually count ghosts. A matcher that cannot say this hit was a whole word produces a count that is preliminary at best.

2. **Every metric must declare an invariance, and pass it.** If a metric is not supposed to respond to length, window it and test that it does not; if it is not supposed to respond to language, file size, or formatting, say so and test that too. An undeclared sensitivity is an unpriced risk.

3. **A validator reports what it checked.** Coverage of the check is part of the result, and any silent skip — any input the checker declined to compare — counts as a failure, because the alternative is a green wall with holes in it.

4. **Every check demonstrates failure before it is trusted to pass.** A test that has not yet been seen red is perhaps not a test at all — it may be a tautology. We break the instrument deliberately, we watch the check catch it, and only then do we let it guard the build.

Missing any one of the four is enough to make the judge untrustworthy. That is not a rhetorical flourish; it is the direct summary of the three cases above, each of which violated exactly one of the first three criteria, and all of which now live under the fourth.

## 4. The diagnosis layer: who checks the checker

Who checks the checker? Stepping back, the three failures share a signature worth naming: none of them was a model hallucination. Each was an engineering assumption — substring matching is good enough, type-token ratio behaves like a stable metric, a parser reads what is on the page. Each of these assumptions turned out to be wrong in a way the tooling had no incentive to reveal.

A deterministic judge can still lie systematically, but it lies consistently, which makes the lie harder to notice and easier to defend in a meeting.

Our containment is a regression suite, and the suite now holds 20 tests covering the repaired behaviors: word-boundary matching, length-invariance of the diversity metric, parser coverage of the expectation tables, and the 6 pinned drifts.

The entry rule comes straight from the fourth acceptance test — each of the 20 has been seen red. A green suite assembled this way means something; a green suite assembled by writing tests against passing code mostly means that the code and the tests share the same assumptions.

The honest answer to that question is layered: the regression suite checks the metrics, and the hand-recountable property of the statistical layer checks the suite, because we can recompute any number from the raw text by hand. The annotation layer — the hand-labeled structural data on which the genre skeletons rest — checks nothing automatically, which is itself a finding we record rather than resolve.

As of September 2026, those annotations cover 3 of the 24 essays, 12.5% of the corpus, so skeletons inferred from them remain provisional and the playbooks built on top inherit that provisionality. The honest posture is to keep the grading visible at the point of use, which is what the evidence tags above attempt. A reader can then weight each claim by the layer that produced it, which is the same discipline we ask of the tool itself.

That posture deserves its own boundary, because the suite locks down known failure modes and says approximately nothing about unknown ones. A future wordlist could carry a pollution of a shape nobody has yet imagined, and the window parameter of the diversity metric has a sensitivity our tests only partially probe.

We believe the suite is a ratchet rather than a proof of correctness: it makes the repaired mistakes expensive to reintroduce, which is a narrower and more defensible claim than it may initially look.

## 5. The decision layer: what travels and what does not

Can this method be carried over, as-is, to scoring other kinds of writing? Probably not. The baselines, the wordlists, and most of the budgets were built on one corpus of one language and one broad genre. A different genre or a different language likely needs its own statistical layer rebuilt from its own essays.

What does transfer is the discipline: determinism first, declared invariances, validators that report coverage, checks that have been seen red, none of which depends on what is being counted. The ruler does not travel; the habit of calibrating rulers does.

1. Determinism comes before cleverness: we can repair a reproducible counter that is wrong, but an impressive judge whose verdicts drift between runs cannot be repaired, because there is nothing stable to repair.

2. Every metric is vulnerable to at least two classes of pollution — its wordlist and its length behavior. Both classes stay invisible until someone reads the hits and plots the sensitivities, so declare the invariance and then test it.

3. The judge needs supervision of its own: a checker that cannot fail manufactures confidence, and the only known antidote is a suite whose every member has demonstrated that it can fail. A suite that has never been seen red cannot be trusted to pass.

Three open questions remain, and we leave them open deliberately rather than smoothing them into the conclusion.

1. The residual diversity gap of 0.070 awaits an attribution — real style or window residue — that our current evidence cannot supply.

2. The sensitivity of these results to the window parameter is only partially mapped, and a fuller sweep may shift some of the smaller numbers reported here.

3. The corpus underlying the playbooks is Chinese, while their first output language is now English, so every English-language quantitative budget in use today is a derived estimate rather than a measured one.

The last gap includes the budget this draft was written against. The corridor we aimed at is a prescription stitched from two other publications' statistics, not a measurement of our own English corpus, and this draft is its first live test. That gap is likely to stay open until English essays are collected and the baselines are rerun.

As for the ruler: we have recalibrated it three times, and we will need to recalibrate it again. Each repair teaches the suite to watch a new place, and watching a new place tends to reveal the next flaw. The markings are better than they were. Whether they are true remains a question the tool, by design, keeps answerable — by keeping every number recountable, every check breakable, and every conclusion tagged with the evidence it stands on.

<!--
self-check（2026-09-09，python3 profiler.py output/_p1-validation-samples/draft-kezhongke-en-v2.md，lang=en 判定正确；question_sentences 与 OBJ_SELFREF_EN 均为修复后口径，工具输出直接可用）：

§0.2 走廊逐项（本批主角，逐项对照）：
- 篇幅 = 2,847 词 —— 达标（目标 ≈2,900，区间 [2,100, 3,750]，贴目标下沿）。
- 平均句长 = 20.3 词 —— 达标（目标 ≈22，区间 [20, 24] 下沿；为压 P90 拆长句的代价，见简报）。
- P90 句长 = 34 词 —— 达标（目标 ≤35，区间 ≤41）。
- 平均段长 = 43.3 词 —— 达标（目标 ≈42，区间 [33, 53]；v1 主缺陷修复：66.6 → 43.3）。
- 数字密度 = 14.75/千词 —— 达标（目标 ≈14，区间 [8, 21]）。
- hedge = 11.59/千词 —— 达标（目标 ≈10，区间 [8, 13.5]）。
- absolutist = 2.46/千词 —— 达标（目标 ≈2，区间 [1.4, 3.4]；7 命中：must ×4 集中于处方判据与校验器教训、never ×2、impossible ×1）。
- 克制比 hedge:absolutist = 4.71:1 —— 达标（典型带 4–5:1，红线 ≥3:1；v1 为 8.7:1，过度克制已校正）。
- 第一人称 = 42 —— 达标（目标 ≈40，区间 [21, 69]；处方 6 硬约束，按节预分配见 outline；profiler 英文口径实际只计小写 we/our/us，I/my 词表项对 lower 文本永不命中——口径缺陷记入简报）。
- 客观自指 = 2 —— 达标（目标 1–2；"this essay" ×2，v1 同口径为 7）。
- 设问 = 3 —— 达标（目标 2–3：2.2 left-open 设问 / 4 小节设问 / 5 设问自答）。
- MATTR = 0.681 —— 达标（目标带 0.68–0.69，区间 [0.66, 0.70]）。
- 感叹号 = 0 —— 达标（红线）。

可读性处方执行：
1. 长句拆分：成稿无超 35 词句子（P90=34）。
2. 段长回落：段长均值 43.3；单句段恰好 4 处（上限 ≤4）："Three of our markings turned out to be wrong." / "The ruler was measuring itself." / "It was also meaningless..." / "We had built the checker..."。
3. 概念显式命名：三失效模式在 FRAME 段命名（substring pollution / length leakage / the blind validator）并全程复用；五层章节标题保留功能分层签名但均挂具体副题（修 v1 命名抽象缺陷）。
4. 数字纪律取中：14.75/千词，四处数字锚各配出处层（24 篇统计层聚合），未堆密度。
5. COUNTER 并入边界声明：2.2 残余 0.070 left-open；4 节"套件是棘轮不是正确性证明"；5 节自我批评段（§0.2 走廊本身是处方层，本稿为其首次实测）。
6. 人称硬约束：42 次，按节预分配执行（outline 有分配表）。

壳中客签名核查：
- 语步骨架：FRAME×4（开场 4 段：定位/三问题清单/结构预告+概念命名/证据分级声明）→ CONTEXT/ARGUE（现象层）→ ARGUE+COUNTER（机制层三节）→ APPLY（处方层四判据）→ ARGUE+COUNTER（诊断层）→ CLOSE（决策层）—— §2 通用骨架兜底（博客体 [推断] 外衣，路由与证据等级声明见 outline）。
- 招式：①明示三问题清单 ✓；②信源分层转化为内部证据分级（statistical/annotation/archive）✓；③判断带边界贯穿（roughly/to a significant extent/most/narrower...）✓；④编号结论 ×3 + 开放问题 ×3 ✓；⑤单一比喻（ruler/calibration/markings）全文复用、小节与全文结尾回收 ✓。
- 术语唯一：限定语 (hedge)、约/约束（字符示例）首现括注后无变体；三失效模式名称全程唯一。
- 收尾形态：[推断] 组合收尾（设问自答 → 编号结论 → 开放问题 → 自我批评 → 比喻收束），CLOSE 区无重复段；无感叹号、无外链、无参考文献表、无 CTA。
- 加粗克制：7 处（三失效模式首现名 + 四判据引导词）；bullet/编号清单仅用于判据与结论（两库中间排版惯例）。

体裁路由与证据等级：博客体（[推断]，骨架"待裁决"）——维持 v1 选择以控制变量；§2 通用语步骨架（[标注-3篇]）作硬约束兜底；收尾为 [推断] 组合。声明全文见 outline-kezhongke-en-v2.md。

与 v1 同口径对照（profiler 实测）：段长 66.6→43.3；句长 18.8→20.3；第一人称 12→42；客观自指 7→2；克制比 8.7→4.7；篇幅 2,711→2,847；MATTR 0.681→0.681（不变）；设问 3→3；感叹号 0→0。

已知口径备注（供 P2）：profiler 英文第一人称词表 " I "/" my " 大写项永不命中（文本先 lower）；we'll/we're 等缩约式因尾随空格要求不计入——本稿写作时已规避缩约式。
-->
