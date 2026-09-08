---
title: "Cross-examining the judge: how we built and hardened a style profiler"
date: 2026-09-08
---

# Cross-examining the judge: how we built and hardened a style profiler

In the first baseline report our style profiler produced, 43 percent of the hedging hits across an entire corpus traced back to a single Chinese character: 约, the everyday word for approximately. Roughly two out of every five times the tool reported that an author was hedging, no hedging had occurred.

The tool behind that number is a statistical profiler for research writing. Given an article, it computes 26 deterministic metrics—sentence length, number density, hedging frequency, vocabulary repetition, and two dozen more—and compresses the piece into a vector of figures that can be compared, argued with, and recounted by hand.

We built the profiler to study how institutions write, because the way an organization explains its work is surprisingly stable, and stability is something a counter can measure. So far we have profiled the public engineering and research blogs of 7 organizations, roughly 10 articles each, and each of those articles has passed through the same 26 counters under the same rules, which is what makes the resulting profiles comparable at all.

The profiles turn impressions into claims. Instead of saying that one blog feels cautious and another feels confident, we can say that one hedges 2.69 times per 1,000 words and another seems to hedge 9.57, and then argue about what that difference means.

Those claims are only useful if they survive scrutiny, which is why the engineering of the tool matters as much as the linguistics. A profile that cannot be defended number by number is just an opinion with extra steps.

We chose counters deliberately. In 2026, the obvious way to analyze style is to hand the articles to a large model and ask for a verdict, and early prototypes of this project took that route. But a model judge cannot be regression-tested: when its assessment shifts between runs, there is nothing to diff, nothing to pin down, and no way to tell a genuine improvement from a change in mood.

We wanted the opposite property.

What does it take to trust a number that a machine reports? This post is our answer, told through the three failures that hardened the profiler into something we trust: a matcher that matched far too much, a diversity metric that was secretly measuring length, and a validation harness that could not see bold text. Each failure produced numbers that looked reasonable, and each was wrong in a way that only became visible once we learned where to look.

## What the profiler measures

The 26 metrics fall into a handful of families. Sentence metrics record the mean length and the 90th percentile, in words. Density metrics count numeric tokens, hedging terms such as roughly and about, absolutist phrasing, and first-person markers, normalized per 1,000 words. Vocabulary metrics estimate how heavily a text reuses its own words, which is where one of our bugs was waiting.

Two aggregation rules sit underneath the families. We report medians and quartile ranges rather than means, because one very long essay can drag a mean across an institution's whole profile, and we normalize counts per 1,000 words so that a short note and a long essay can stand on the same scale.

Each metric is deterministic: the same document in, the same 26 numbers out, with no model, no sampling, and no temperature. That property is the entire point, because it makes each figure the profiler has ever reported reproducible by anyone patient enough to recount it.

Determinism also makes verification cheap. When a reviewer questions a specific claim, the disagreement can be settled by a short script in seconds instead of by taste, seniority, or eloquence, and the script's answer will be identical tomorrow.

The output of a profiling run is deliberately plain: one JSON object per article plus an aggregate report per institution, so the entire evidence base behind any claim fits in a folder and can be re-derived with a single command.

We check that property by hand on a schedule. Every so often we pick one published figure—say, a median sentence length of 22.3 words for one institution—and recount it from the raw articles, because a profiler that is only audited when something looks wrong is not really audited at all.

None of the 26 metrics is clever on its own, and we deliberately avoided collapsing them into a single style score. A single number would be easier to quote and harder to audit, and auditability is the property we were unwilling to trade away.

## Bug #1: the eager matcher

The hedging metric is a lexicon counter: it matches the article against a curated list of terms and reports hits per 1,000 words. For English, matching on word boundaries was straightforward, because English helpfully puts spaces between words. For Chinese, the first implementation matched substrings instead.

Why did that seem reasonable at the time? Chinese text has no spaces, proper word segmentation is a project of its own, and the substrings we cared about looked distinctive enough that accidental matches appeared unlikely. The approximation held up through months of English-only profiling in 2025, and it likely would have kept holding if our corpus had stayed monolingual.

It broke in early 2026, within a week of the corpus turning bilingual. The first batch of Chinese-language articles came back with hedging densities 75 percent higher than anything we had measured in English, and the initial reading—this is the embarrassing part—was that we had discovered a genuine stylistic difference between the two corpora.

The discovery survived until we read the raw hit lists, the actual matched strings behind each count. The character 约 appeared far more often than any real hedge should, including in passages that were plainly not hedging at all, and the pattern was too consistent to be noise.

The mechanism was simple once seen. The character 约 is a common morpheme inside words like 约束 (constraint), 简约 (minimal), and 契约 (contract), none of which express approximation. A sober paragraph about constrained optimization read, to our counter, like a thicket of hesitation.

That was the week we started reading hit lists instead of code.

Reading the lists turned out to be a habit worth keeping on its own. For each metric we now sample the raw matches across institutions and skim them the way a reviewer skims quotations, because a count is only as good as the contexts it was counted in.

The repair was to move Chinese matching onto real word boundaries, using a proper segmenter, and to count 约 as a hedge only when it stands alone as a word. The corpus-wide median hedging density fell from 4.75 to 2.69 hits per 1,000 words, which suggests that 43 percent of what we had been calling hedging had never been hedging.

We also re-ran the English corpus under the stricter matcher, expecting no movement, and got it: the English numbers shifted by less than 1 percent, which told us the repair had removed the artifact without disturbing measurements that were already sound.

The size of the correction mattered beyond one metric. Our earlier comparisons had described some institutions as markedly more tentative than others, and roughly half of that tentativeness evaporated once the matcher learned what a word was, so we had to revisit conclusions and not just coefficients.

As a sanity check, we recounted one full article by hand—about 2,500 words, each lexicon term tallied against the list—and the manual tally agreed with the repaired pipeline within a few hits. We then regenerated the published baselines under the fixed matcher, because a correction that leaves the old numbers in place is only half a correction.

The articles had not changed. The counter had.

The new median is a figure we are now willing to defend in public, not because the pipeline is trusted in general, but because this specific claim has been recounted and survived. The lesson generalizes beyond lexicons: the dangerous bugs in a measurement system are not the ones that crash. They are the ones that return a confident, plausible figure, because a plausible figure ends the investigation before it starts.

## Bug #2: the stretching ruler

The second failure lived in the vocabulary family. Type-token ratio, or TTR, is the fraction of distinct words in a text, and it looks like a natural measure of lexical diversity: higher means the author reaches for fresh words, lower means the prose recycles. We adopted it early, because the definition is about 5 words long and the computation is one pass over the tokens.

TTR has a mechanical flaw that is well documented and easy to forget. The longer a document runs, the more it is forced to reuse its own vocabulary—function words first, then the domain terms—so the ratio falls with length whether or not the writing is genuinely repetitive.

A concrete example makes this hard to unsee. Take an author with a stable voice and ask for a 1,000-word note and a 4,000-word essay on the same topic; the essay will usually score lower on TTR, not because its vocabulary is poorer, but because 4,000 words cannot all be distinct.

In practice, this meant our cross-institution comparison was partly a comparison of document lengths. One organization in the corpus publishes essays that average around 3,000 words, while another publishes pieces closer to 1,600, and the raw TTR gap between the most and least diverse institutions looked large. A good portion of it was the ruler measuring itself.

None of this was unknown to us in principle. The length dependence of TTR is textbook material, and we could have recited it on demand; what we had not done was carry the implication into the one place where it mattered, which was the comparison table we published.

The standard repair is the moving-average type-token ratio, or MATTR: slide a fixed window of 150 tokens across the text, compute TTR within each window, and average the windows. Each document, whatever its length, is then measured in equal-sized frames, and document length can no longer leak into the score.

We picked 150 tokens because it is long enough to contain several sentences and short enough to fit inside even our briefest article many times over; the exact value matters less than the fact that it is fixed.

When we re-ran the full corpus under MATTR, the spread between the most and least lexically diverse institutions contracted from 0.204 to 0.070, a threefold reduction. The ordering of the 7 institutions, notably, did not move at all.

The signal survived the repair; the artifact did not.

We also checked the robustness of that conclusion by varying the window, because a window size is still a choice and choices deserve scrutiny. Across a range of plausible windows the ordering stayed put and the spread stayed small, which gave us some confidence that the repair had removed an artifact rather than introduced a new one.

Could the original gap have been real signal that the window threw away? That was our first worry, and it deserves a direct answer. If some institutions genuinely wrote with richer vocabularies, the gap should have survived equal-length measurement, because equal windows strip the length artifact while preserving any true difference in word choice. The gap mostly did not survive, which suggests that two-thirds of what looked like a difference in style was a difference in the ruler.

There is a humbler way to say the same thing: for months, the most striking number in our vocabulary analysis was mostly a measurement of how long our chosen institutions like to write.

The residual spread is the part we are willing to defend: a small, possibly real difference in lexical habit, rather than a large, definitely artificial one. We believe that trade—shrinking a headline number until only the defensible part remains—is what a measurement tool is supposed to do.

We now require new metrics to declare an invariance: a written statement of what the metric must not respond to. The vocabulary score must not respond to document length, density metrics must not respond to formatting conventions, and each declared invariance becomes a test in the regression suite, because anything that can be written down can be checked.

## Bug #3: the harness that only said PASS

Both of those bugs should have been caught by our regression harness, which has existed since fairly early in the project. The harness recomputes each profile from the corpus and diffs the generated markdown tables against checked-in expectations, so any change in any reported number should have produced a visible mismatch.

The expectations live as ordinary markdown tables in the repository, which is usually a virtue: they are readable in code review, they diff cleanly, and a change to a reported number shows up as a change to a line of text that a human can inspect.

The reason the harness missed both bugs is the third failure, and the one we think about most. The harness parsed expectation tables cell by cell, and the parser silently skipped any cell wrapped in bold markup. It skipped those values at comparison time, which means it had no way to mismatch on them, and several of the columns carrying our most important medians happened to be formatted in bold.

Everything passed. Almost nothing was being checked.

The uncomfortable part is how long this lasted. The harness had been running green for months, and each green run quietly raised our confidence in numbers the harness was not actually checking, so the safety net was manufacturing the very certainty it was supposed to test.

The discovery was, again, accidental. While fixing the matcher bug we updated a handful of expected values by hand, noticed that one row of the table seemed invisible to the diff, and traced the invisibility to the parser's handling of bold cells. Once the parser was repaired, the validator immediately reported 6 numeric drifts that had been sitting in the open.

Most of the 6 were stale expectations: numbers recorded before the matcher and vocabulary fixes that nobody had moved in the same commit. A few were genuine defects we would not otherwise have found, and both kinds are now pinned by name in the suite, because a drift you do not write down is a drift you will meet again.

A loud failure would have been better, because a loud failure stops the line and demands attention. A silent skip does the opposite: it converts missing evidence into a passing grade, and the passing grade then discourages anyone from looking again.

That was the week we stopped trusting green.

The new rule is that a check has to demonstrate failure before we trust its pass. Each test in the suite has been deliberately broken at least once—fed an input it is required to reject—and we have watched each one go red before accepting it.

In practice, demonstrating failure is a small ritual: before a new check is merged, we temporarily corrupt the artifact it guards—a swapped column, a stale expectation, a bolded cell—and confirm that the suite goes red for the right reason and with a readable message.

The suite now holds 20 regression tests, up from 9 before the parser fix, and the difference between those two numbers is the cost of an unexamined assumption.

The most dangerous validator is the one that cannot fail, because it produces confidence instead of evidence. A test suite that has yet to be seen red is not an asset; it is an unexamined claim about itself.

## What we now require

The full list of requirements that came out of these 3 failures is short, and none of it is abstract—each item was paid for by a bug:

- **Boundaries are the contract.** Count tokens, not substrings, in any language the tool touches; a matcher without boundaries is a generator of false signal.
- **Declare the invariance.** No metric ships without a written statement of what it has to ignore, plus a test that proves it ignores it.
- **Recompute by hand.** Any number destined for a report gets tallied manually at least 1 time before it is quoted, because quoting is a claim and claims need evidence.
- **No unearned PASS.** A check is trusted only after we have watched it fail on purpose; green before red is just a color.
- **Move expectations with the metric.** When a fix changes a number, the expectations change in the same commit, so the harness stops validating a stale past against a repaired present.

These 20 tests now run on each change, and a new metric enters the profile only after its invariance statement does. This is slower than trusting the first number that comes out of a pipeline, and considerably faster than retracting that number later.

## Earning the right to trust a number

Looking back, the 3 failures share a shape. Each one was quiet, each produced output that seemed credible, and each was found not by watching the tool run but by cross-examining what it produced—reading the hit list, questioning the ruler, breaking the validator on purpose.

A metric is not just a measurement—it is a claim about what can be safely ignored, and the claim is only as good as the testing behind it. Roughly 43 percent of our original hedging counts rested on a claim we had never examined, and the rest of the profile rested on a validator that could not see part of its own evidence.

The 26 metrics were never the hard part of this project. The hard part was earning the right to trust them, and that right is earned the way credibility usually is: under cross-examination, one demonstrated failure at a time. We expect more failures, and we have built the harness that will catch them.

<!-- self-check: python3 profiler.py output/_p1-validation-samples/draft-openai.md（指标测自不含本注释的正文）
子体裁路由：engineering-deep-dive · 调查叙事型（core-dump 变体）。
对照 output/openai/_aggregate.json（median / P25–P75 → 实测）：
- 词数 3164 / 1628–3758 → 2924：达标（IQR 内，略低于 median）
- 平均句长 22.3 / 19.9–24.9 → 22.5：达标（≈median）
- P90 句长 35.5 / 34–38 → 38：擦界达标（压在 P75）
- 平均段长 40.2 / 32.9–43.9 → 43.7：擦界达标（P75 内沿；由多处单句段节拍器拉回区间）
- 数字密度 20.69 / 15.64–27.64 → 17.1：达标
- 精确小数 0.92 / 0.31–2.66 → 2.39：达标（区间内偏高；4.75/2.69/9.57/0.204/0.070/22.3 共 7 处）
- 年份 1.23 / 0.8–1.82 → 1.03：达标（2025/2026/2026 共 3 处）
- hedge 9.57 / 7.99–14.73 → 12.31：达标（median–P75 之间）
- absolutist 1.76 / 1.38–2.93 → 2.05：达标（≈median）
- quantifier 5.9 / 1.9–6.51 → 5.81：达标（≈median）
- 第一人称 53 / 33–90 → 58：达标（≈median）
- this post 自指 1 / 1–2 → 1：达标
- 问句 3 / 1–11 → 3：达标（1 小节标题 + 2 正文）
- 感叹号 0 → 0：达标；外链/参考文献 0 → 0：达标
- MATTR 0.68 / 0.66–0.69 → 0.686：达标
- CJK 字符 0 → 10：未达标（题材必需：主角"约"及 3 个示例词，cerebras 盲测稿同此偏差）
结构：无场景数字反转 HOOK → CONTEXT → FRAME（三失败清单预告）→ Bug#1/#2/#3 各含 initial approach→失败→单句段转折→修复确认→教训，COUNTER 内化为 Bug#2 自我反驳问答；手工重数段落承担费米估算位；APPLY 为 5 条加粗引领 bullet + 制度化承诺；CLOSE 用 X is not just A—it is B 格言式 + 承诺收束。无 CTA、无场景描写、无 Limitations 独立节。 -->
