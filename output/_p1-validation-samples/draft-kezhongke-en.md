# Calibrating the Ruler: How We Built and Hardened a Style Profiler

We built a ruler. More precisely, we built a profiler: a tool that reads a research-style blog post and returns a vector of roughly 26 deterministic measurements — sentence length, number density, hedge frequency, vocabulary diversity, and the other statistical raw material that a house style is made of. This essay is partly the build log of that ruler, and mostly the log of its recalibration.

This essay answers three questions. The first is why the judge has to be a deterministic counter rather than a model. The second is where, concretely, the ruler lost calibration — three failures, three distinct mechanisms. The third is how the judge itself is kept honest once the counters are fixed.

The essay proceeds in five layers: phenomenon, mechanism, prescription, diagnosis, decision. The first two layers cover what happened and why it happened; the last three cover what to do about it, how to measure it, and where to stop. One discipline applies throughout: every claim is tagged with the grade of evidence behind it — the statistical layer (a 24-essay aggregate), the annotation layer (hand-labeled moves, a much smaller set), or archive prose (essays about the tool, used here as inference only). Where the evidence is thin, the text says so rather than smoothing it over.

## 1. The phenomenon layer: why a style tool needs a ruler

The profiler exists to answer a deceptively simple question — what the writing of a given institution actually looks like, statistically — and to answer it the same way every time. We pointed it at the public blogs of seven AI institutions and extracted, for each essay, a vector of about 26 dimensions: mean sentence length, paragraph length, numbers per thousand tokens, first-person frequency, rhetorical questions, hedge and absolutist markers, and so on. The method descends from genre analysis in the Swales tradition and from argument mining, but the statistical layer is deliberately dumber than both. It counts, and it does not judge.

Deterministic has a precise meaning here. The same input produces the same output on every run, and every number in the profile can be recounted by hand. If the profiler reports a hedge density of 4.75 per thousand characters, an analyst can open the essay, recount the hits one by one, and get 4.75. That property is not a convenience; it is roughly the entire foundation on which the rest of the tool stands.

The obvious alternative — asking a large model to grade the essay directly — fails on exactly this point. A model's score may drift between two runs of the same text; it cannot be diffed, and what cannot be diffed cannot be regression-tested. This is not a claim that model judgments are worthless. It is the narrower claim that they are unsuitable as the stable reference against which a style baseline is built: you cannot calibrate against a moving target, and a mood, however articulate, is a moving target.

A bounded conclusion follows, and it is worth stating with its boundary attached. Determinism is not correctness. A deterministic counter can be wrong — wrong in exactly the same way, every time — and in isolation that is a weakness. But being reproducibly wrong is what makes correction possible at all. A ruler first has to carry markings before anyone can check whether the markings are true. Most of what follows is the story of finding out that three of ours were not.

## 2. The mechanism layer: three places the ruler lost calibration

### 2.1 The counter that counted ghosts

The first anomaly surfaced in the hedge counts. The statistical layer tracks what the Chinese source essays call 限定语 (hedges) — markers like "approximately", "reportedly", "perhaps" that bound the strength of a claim. Our counts for the Chinese corpus looked oddly high, and they looked high in essays whose prose did not seem hesitant. The discovery path matters: the problem was found by reading the hit list, not by reading the code. The code looked fine. The hits did not.

The mechanism was substring matching. The wordlist contained the single character 约 ("approximately"), and the matcher counted any occurrence of that character as a hedge — including its occurrence inside 约束 ("constraint"), a word about restriction that carries no hedging force whatsoever. In essays about constrained optimization, every mention of a constraint was silently counted as an expression of uncertainty. The matcher had not crashed. It had returned a plausible-looking number that was, in large part, an artifact.

In the matcher's defense, the shortcut was not obviously reckless at the time. Chinese text has no spaces, and proper segmentation is a project of its own; for the multi-character terms that made up most of the early wordlists, substring matching behaves reasonably well. The pollution stayed largely invisible while the corpus was English-heavy, and became visible only when Chinese essays — dense with words like 约束, 简约, 契约 — entered the sample. An assumption that is mostly harmless in one language can become a systematic liar in another.

The fix was word-boundary matching: single-character terms are counted only when they match a segmentation token exactly, not when they appear as a substring inside a longer word. After the fix, the median hedge density across the 24-essay aggregate fell from 4.75 to 2.69 per thousand characters. Roughly 43% of what had been counted as hedges were not hedges at all. The essays themselves had not changed.

The lesson generalizes beyond this bug, and we state it with a boundary: in a measurement tool, the most damaging defects tend to be the quiet ones. A crash is visible; a wrong number that looks like a right number enters every downstream conclusion without announcing itself. Determinism had been doing its job the whole time — the same wrong answer, every run — which appears to be exactly why the wrongness survived long enough to be trusted.

### 2.2 The ruler that stretched

The second failure was subtler, because the metric involved is standard. Type-token ratio — distinct words divided by total words — is a common measure of vocabulary diversity, and it is mechanically length-dependent: the longer a text runs, the more its vocabulary repeats, so the ratio falls as length grows. A long essay by a single author will, toward its later sections, inevitably reuse its own terminology, while a short note by the same author looks artificially diverse by comparison. This is textbook knowledge. It is also easy to forget, and forgetting it quietly tilts every comparison the tool makes.

When we compared raw type-token ratios across the seven institutions, we were, to a significant extent, comparing essay lengths. The ruler was measuring itself. The repair was to replace the ratio with its moving-average variant, MATTR: diversity is computed inside a sliding window of 150 tokens, and the window scores are then averaged. Every text contributes equal-length frames, so length stops leaking into the measurement.

The numbers after the repair are the part worth remembering. The apparent cross-institution diversity gap shrank from 0.204 to 0.070 — roughly two-thirds of the visible difference had been the ruler, not the text. The ranking, notably, did not move: the institution that looked most lexically diverse before the fix still looks most diverse after it. The correction changed the magnitude of the claim, not its direction, which suggests the original comparison was pointing at something real but reporting it through a stretched scale.

Is the remaining 0.070 a genuine stylistic difference, or residue that the window could not remove? We left this question open, and this essay leaves it open too: the window suppresses length dependence but may not eliminate it, and attributing the residual gap would require evidence we do not currently have. One operational lesson did survive and entered the regression suite — every metric should declare an invariance, something it is not supposed to respond to, and that declaration is itself testable. Length-invariance is now a tested property rather than an assumption.

### 2.3 The validator that only said PASS

The third failure was in the harness, not the metrics. The regression harness re-computes profiles and diffs them against expected values stored in markdown tables, and for a while it reported a clean, unbroken wall of PASS. The green was real, in the narrow sense that the validator had not found a single mismatch. It was also meaningless, and the reason took an embarrassingly long time to see.

The parser that read the expectation tables silently skipped bold cells. A value wrapped in emphasis was not extracted, not compared, and therefore could not mismatch. Part of the table was simply invisible to the checker, and the checker did not consider this worth mentioning. The wall of PASS reported, with apparent confidence, the results of comparisons that had not run.

The discovery followed the usual path for this class of bug: someone corrupted an expectation table on purpose, and the suite came back green. A validator that stays green when its inputs are deliberately broken is not validating anything; it is reciting. That single experiment reframed months of clean reports from evidence of health into evidence of blindness.

Once the parser was fixed, the validator immediately caught six numeric drifts. Most of them were stale expected values — numbers left behind when a metric's definition had changed while the table had not been updated to match. Each of the six was pinned into the suite as an explicit regression test, so those drifts now fail loudly instead of aging quietly into the baseline.

The lesson here is the sharpest of the three, and we allow it one strong word: a validator that can never fail is worse than no validator, because it manufactures confidence without doing the work. A checker has to report what it checked — the comparisons attempted, not merely the verdicts returned — and a silent skip must be treated as a failure, not as a pass with missing data.

## 3. The prescription layer: four acceptance tests for a ruler

The three failures compress into a checklist, and the checklist is likely the most portable part of this essay. Whatever you are measuring — prose style, model behavior, anything where a counter stands between you and a claim — a measurement instrument earns trust by passing four acceptance tests:

1. Wordlist hits must respect token boundaries. Any term counted by bare substring match — above all single-character or very short terms — will eventually count ghosts. If your matcher cannot say "this hit was a whole word", the count is preliminary at best.
2. Every metric declares and passes an invariance. If a metric is not supposed to respond to length, window it and test that it does not respond to length. If it is not supposed to respond to language, file size, or formatting, say so and test that too. An undeclared sensitivity is an unpriced risk.
3. A validator reports what it checked. Coverage of the check is part of the result. Any silent skip — any input the checker declined to compare — counts as a failure, because the alternative is a green wall with holes in it.
4. Every check demonstrates failure before it is trusted to pass. A test that has not yet been seen red may not be a test at all; it may be a tautology. Break the instrument deliberately, watch the check catch it, and only then let the check guard the build.

Missing any one of the four is enough to make the judge untrustworthy. That is not a rhetorical flourish; it is the direct summary of the three cases above, each of which violated exactly one of the first three criteria, and all of which now live under the fourth.

## 4. The diagnosis layer: who checks the checker

Stepping back, the three failures share a signature worth naming: none of them was a model hallucination. Each was an engineering assumption — substring matching is good enough, type-token ratio behaves like a stable metric, a parser reads what is on the page — that turned out to be wrong in a way the tooling had no incentive to reveal. A deterministic judge can still lie systematically; it simply lies consistently, which makes the lie harder to notice and easier to defend in a meeting.

The containment is a regression suite, and the suite now holds 20 tests covering the repaired behaviors: word-boundary matching, length-invariance of the diversity metric, parser coverage of the expectation tables, and the six pinned drifts. The suite's entry rule comes straight from the fourth acceptance test — every check demonstrated failure before it was admitted. Each of the 20 has been seen red. A green suite assembled this way means something; a green suite assembled by writing tests against passing code mostly means that the code and the tests share the same assumptions.

Who checks the checker? The honest answer here is layered. The regression suite checks the metrics. The hand-recountable property of the statistical layer checks the suite, because any number can be recomputed from the raw text by a skeptical reader. And the annotation layer — the hand-labeled structural data on which the genre skeletons rest — checks nothing automatically, which is itself a finding we record rather than resolve. Those annotations currently cover a small fraction of the corpus, so skeletons inferred from them remain provisional, and the playbooks built on top inherit that provisionality. The honest posture is to keep the grading visible at the point of use, which is what this essay's evidence tags attempt.

That posture deserves its own boundary. The regression suite locks down known failure modes. It says approximately nothing about unknown ones: a future wordlist could carry a new pollution of a shape nobody has yet imagined, and the window parameter of the diversity metric has a sensitivity the current tests only partially probe. We do not treat the suite as proof of correctness, only as a ratchet — it makes the repaired mistakes expensive to reintroduce, and that is a narrower and more defensible claim than it may initially look.

## 5. The decision layer: conclusions and open questions

Can this method be carried over, as-is, to scoring other kinds of writing? Probably not. The baselines, the wordlists, and most of the budgets were built on one corpus of one language and one broad genre; a different genre or a different language likely needs its own statistical layer rebuilt from its own essays. What does transfer is the discipline — determinism first, declared invariances, validators that report coverage, checks that have been seen red — because none of that depends on what is being counted. The ruler does not travel; the habit of calibrating rulers does.

Three numbered conclusions close the argument:

1. Determinism comes before cleverness. A reproducible counter that is wrong can be repaired; an impressive judge whose verdicts drift between runs cannot be, because there is nothing stable to repair.
2. Every metric is vulnerable to at least two classes of pollution — its wordlist and its length behavior — and both classes stay invisible until someone reads the hits and plots the sensitivities. Declare the invariance, then test it.
3. The judge needs supervision of its own. A checker that cannot fail is manufacturing confidence, and the only known antidote is a suite whose every member has demonstrated that it can.

Three open questions remain, and they are left open deliberately rather than smoothed into the conclusion. First, the residual diversity gap of 0.070 awaits an attribution — real style or window residue — that the current evidence cannot supply. Second, the sensitivity of the results to the window parameter is only partially mapped, and a fuller sweep may shift some of the smaller numbers reported here. Third, and most structural: the corpus underlying this work is Chinese, while the first output language of the playbooks derived from it is now English, so every English-language quantitative budget in use today is a derived estimate rather than a measured one. That gap is likely to stay open until English essays are collected and the baselines are rerun.

As for the ruler: it has been recalibrated three times and it will need recalibrating again, because each repair teaches the suite to watch a new place, and watching a new place tends to reveal the next flaw. Calibration is the part of this work that does not end. The markings are better than they were; whether they are true remains a question the tool, by design, keeps answerable — by keeping every number recountable, every check breakable, and every conclusion tagged with the evidence it stands on.

<!--
self-check（2026-09-08，python3 profiler.py output/_p1-validation-samples/draft-kezhongke-en.md，lang=en 判定正确）：

可迁移硬约束（§0）：
- 感叹号 = 0 —— 达标（红线）。
- 克制比 hedge:absolutist = 35:4 ≈ 8.8:1（12.91/千词 vs 1.48/千词，profiler 英文词表）—— 达标（≥3:1）。注：absolutist 4 命中含 "not obviously reckless" 的否定式用法，词表按子串命中不辨否定，已计入。
- 语步序列 FRAME×3 → CONTEXT/ARGUE（现象层）→ ARGUE×n + COUNTER×2（机制层，两处 left-open）→ APPLY（处方层四条判据）→ ARGUE + COUNTER（诊断层）→ CLOSE（设问自答→编号结论×3→开放问题×3→比喻回收）—— 按 §2 通用骨架执行，逐段对应 outline-kezhongke-en.md。
- 收尾形态：博客体无实证收尾，采用 §2 通用 CLOSE + 招式 4/5 组合（大纲已声明为 [推断] 组合收尾）。
- 招式：①明示三问题清单（开场段 2）✓；②信源分层转化为内部证据分级（statistical/annotation/archive，开场段 3 声明、诊断层落实）✓；③判断带边界（"not obviously reckless""to a significant extent""narrower and more defensible"等贯穿）✓；④编号结论×3 + 开放问题×3 ✓；⑤单一比喻（ruler/calibration/markings）全文复用、小节与全文结尾回收 ✓。
- 术语纪律：限定语（hedges）、约/约束（字符示例）、语步概念以 moves 表述；英文术语全文唯一，中文原生概念首现括注英文译名 ✓。

次数类参考区间（§0 弱迁移，非硬约束）：
- 设问 = 3 —— 在 1–4 区间内。
- 第一人称 = 12 —— 在 1–13 区间内。
- 客观自指：profiler 计 2（其 OBJ_SELFREF_EN 词表命中 "this work"）；§0 指定的 this essay/this analysis 不在该词表内，手工计数 this essay = 5 —— 处于 1–5 区间上沿。口径不一致已记入简报。

篇幅（推导值，非统计层口径）：2,711 词，落在推导区间 2,500–3,800（14 min [12,18] × ~210 wpm）中段偏低侧；profiler 自带 read_min 按 300 wpm 计为 9 分钟，与该推导口径不同，仅备查。

中文口径指标（§4，不适用，仅记录不考核）：句长均值 18.8 词/P90 35 词；段长均值 62 词；数字密度 11.43/千词、精确数字 4.43/千词；年份 0；外链 0；参考条目 0；quantifier 15.49/千词（英文词表，不参与克制比）。

已知 profiler 英文口径缺陷（供 P2）：sentences.question_sentences = 0（英文按 [.!?]+ 切句后分隔符被剥除，再以 ？/? 后缀判定必然为 0），与 stance.questions=3 自相矛盾；英文问句指标当前不可用。
-->
