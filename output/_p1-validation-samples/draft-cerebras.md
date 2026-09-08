---
title: "How We Built a Deterministic Judge for Style Analysis"
date: 2026-09-08
---

# How We Built a Deterministic Judge for Style Analysis

One Chinese character was quietly responsible for 43 percent of our hedging counts. The character, 约, is the everyday word for approximately, and it taught us what kind of judge we were actually building.

The tool it broke is a style profiler for research articles. It compresses each paper into a statistical fingerprint: how long sentences run, how dense numbers are, how often authors hedge.

Seven institutions so far, seven house styles, reduced to vectors of numbers you can put in a spreadsheet and argue with.

The statistical layer behind those vectors carries about 26 deterministic metrics, with no model, no sampling, no temperature: the same document in, the same 26 numbers out.

We chose determinism on purpose: in 2026, the obvious move was to hand the papers to a large model and ask it to grade style directly.

A model judge cannot be regression-tested, and when its verdict shifts between runs, you cannot diff a mood.

So what breaks first when you replace the model with counters? Two failure modes, one blind validator, and 20 regression tests later, here is what we know.

## The statistical layer

The 26 metrics fall into 4 families: sentence length, number density, hedging, and vocabulary.

Every metric is a counter you can audit by hand. If a profile says an institution hedges 4.75 times per 1,000 words, a skeptic can recount those hits one by one.

Sentence length is measured in words, number density counts numeric tokens per 1,000 words, hedging counts lexicon hits like roughly and about, and vocabulary measures how often the text repeats itself.

None of the 26 is clever on its own, but together they make a profile that is stable enough to compare institutions and boring enough to test.

This is the property that makes verification cheap instead of precious: you do not negotiate with the judge, you check its arithmetic.

Counters still fail, and ours failed in 2 characteristic ways that we named so we could spot them faster the next time.

Inflation. The counter sees things that are not there.

Drift. The ruler changes length with the thing it measures.

## Inflation: the counter that saw ghosts

The hedging lexicon includes 约, and the first matcher worked on substrings rather than words: if the characters appeared anywhere inside a longer word, the counter fired.

The common word for constraint, 约束, contains 约 as its second character, so occurrences of constraint were silently booked as hesitation.

Substring matching looked reasonable at first, because Chinese has no whitespace and real word segmentation is its own project.

It also worked, mostly, in English, where hedges are whole words and whitespace does the segmenting; the contamination only showed once the corpus turned bilingual.

We found the bug by reading the hit list instead of the code: row after row of matches was 约束, the word for limits, wearing the badge of the word for vagueness.

A dry section on constrained optimization looked like a forest of hesitation. The metric did not crash; it lied.

Switching to word-boundary matching dropped the median hedging count from 4.75 to 2.69 per 1,000 words, a fall of roughly 43 percent.

No paper had changed; close to 43 percent of what we had been calling hedging was never hedging. The new median, 2.69, is the number we now defend in profiles, and the hits behind it can be shown one by one.

That is the dangerous kind of bug: it does not throw an error, it returns plausible numbers, and plausible numbers get quoted.

## Drift: the ruler that stretched

Type-token ratio, the oldest lexical-variety statistic in the book, divides distinct words by total words, and it is mechanically dependent on length.

The longer a document runs, the more its words repeat, so the ratio sinks even when the style stays fixed. A long paper looks poorer than a short note by the same author.

Length dependence is documented, unsurprising, and easy to forget; it does not announce itself, it quietly tilts the comparisons you run.

Comparing 7 institutions on the raw ratio mostly compared their document lengths: the ruler was measuring itself.

The fix is MATTR, which slides a window of 150 tokens through the text and averages the ratio across the windows. Documents are measured in identical 150-token frames, so length stops leaking into the score.

The gap between institutions on this metric shrank from 0.204 to 0.070, roughly threefold smaller, and not one ranking moved.

Read that again: roughly two thirds of the apparent difference was ruler, not text, and what survived was 0.070 of signal out of 0.204 of measurement.

You could argue the 0.204 gap was real signal we threw away, but play it forward: if the gap had been style, fixing the ruler would have reshuffled the order. All 7 institutions kept their places.

Every metric now ships with a stated invariance, one property of a document it must not respond to; for lexical variety, that property is length. An invariance you can state is an invariance you can test, and those tests live in the regression suite.

## Does the judge discriminate?

The point of the 26 numbers is telling institutions apart, which we test with leave-one-out classification across the 7 libraries: hold one document out, learn from the rest, guess the source.

Leave-one-out is harsh by design: a held-out document is judged by a classifier that has not seen it, with no memorization to lean on and no second tries.

The judge lands at 71 percent accuracy, about 5 out of 7 documents: comfortably above chance, honestly far from perfect. That still leaves 2 in 7 documents mislabeled, which is why the claim stays modest.

Treat the number with care, because 7 libraries is a small world; the claim is narrow on purpose: the signal exists, the features separate, and the ceiling is still far off.

Had the accuracy hovered near chance, the statistical layer would have been decoration; at 71 percent it is a floor to stand on, not a trophy.

## The validator that only said PASS

The regression harness recomputes the profiles and diffs their numbers against expected values stored in markdown tables; it is the last line of defense.

The table parser skipped cells wrapped in bold markers, so a value set in strong emphasis was never compared and could not mismatch.

The harness reported a clean PASS, green after green, while a slice of the table sat invisible to it.

A silent skip is worse than a loud failure: a loud failure stops the line, a silent one waves it through.

Once the parser handled bold cells, the validator immediately caught 6 numeric drifts that had been sitting in the open, 6 defects hidden by a formatting convention.

Most of the 6 were stale expectations, numbers stored before the metric fixes that had not moved with them; they are pinned by tests now.

A validator that cannot fail is worse than no validator at all, because it manufactures confidence.

A check must now demonstrate failure before we trust its pass, and the 20 regression tests have been seen red at least 1 time.

## What we now require

If you maintain metrics of your own, build up your skepticism the way you build up the metrics; the list is short, and everything on it cost us a bug.

- Count tokens, not substrings; boundaries are the contract.
- Fix the window before comparing lengths: 150 tokens, every document, every time.
- State what a metric must ignore, then test that it ignores it.
- Recompute by hand the numbers you plan to quote.
- Treat every PASS as unverified until you have watched it fail.
- When a fix changes a metric, move the expectations in the same commit.

Off-limits: you may not ship a metric whose failure mode you have never seen.

The 26 metrics were never the hard part; the hard part was earning the right to trust them, and that right is earned the way a witness earns it, under cross-examination.

Determinism did not make the judge smarter; it made the judge answerable, and answerable is what lets a team move fast without breaking its own measurements.

The judge we wanted was never the one that is always right; it is the one we can always check.
