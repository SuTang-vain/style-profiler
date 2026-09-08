# Measuring style without trusting the meter: building a deterministic profiler for institutional writing

Over the past year, we have been building a tool that measures how organizations write. The profiler reads blog posts from seven institutions and extracts a statistical portrait of each one's style, and the most reliable parts of it turned out to be the simplest ones: deterministic counters rather than model judgments.

The motivation was comparative. When we began this work in early 2026, research groups, labs, and engineering organizations had each developed a recognizable way of writing, and we wanted to describe those differences with numbers that a skeptic could reproduce. A claim like "this blog hedges more than that one" should be checkable by hand, not taken on the authority of a model's impression.

In this post, we share what we learned while building and hardening the tool, and offer practical advice for anyone constructing measurement systems of their own. Most of what went wrong went wrong quietly, and the quiet failures are the ones worth describing.

## What does the profiler measure?

The profiler computes a fixed set of roughly two dozen deterministic metrics for each document: average sentence length, paragraph length, the density of hedging language, the density of numbers, vocabulary richness, and similar surface statistics. Given the same input, a metric returns the same output, which makes each one possible to regression-test and possible to defend.

The corpus itself is modest by design: ten or so posts per institution, chosen to represent sections rather than to chase popular pieces. Small samples put pressure on each measurement, which is one more reason the metrics have to be boring. A portrait built from a handful of documents cannot afford a counter that hallucinates a third of its hits.

Documents are then aggregated at the institution level using medians and quartile ranges rather than means. A single long or unusual post should not drag an institution's portrait with it, and medians make the aggregate robust to exactly that kind of outlier. This choice cost us some familiarity, since means are what readers expect, but it has made the portraits noticeably more stable as the corpus grows.

We draw an architectural distinction between the statistical layer and the judgment layer. The statistical layer counts things that can be counted without interpretation, and we trust its output because a person can verify it by hand. The judgment layer covers questions like genre and argumentative structure, and we treat its output as provisional until a human reviews it.

This separation may sound obvious in retrospect, but it erodes easily in practice. When a large language model scores a draft, the score cannot be diffed, pinned to a test, or replayed after a refactor, so we believe model judgment should sit above the deterministic layer rather than inside it.

Across the tool's development, one failure shape kept recurring: a metric answers a slightly different question than the one you asked, and it answers confidently. We refer to this as measurement contamination. The remainder of this post describes three forms it took in our system, what each one cost, and what we changed as a result.

## Failure mode 1: the counter that matched substrings

The first failure mode is substring contamination, in which a counter treats partial matches as evidence. It tends to appear whenever text is matched literally and the writing system does not mark word boundaries, so the conditions for it are easy to miss during design.

Our hedge detector kept a vocabulary of hedging expressions, including a single Chinese character, pronounced "yue", that means approximately. The original matcher searched for each vocabulary entry as a substring. That choice seemed reasonable for a language without whitespace, where segmentation is a project of its own, and for a long time nothing appeared wrong.

The same character, however, also sits inside longer words, including the common word for "constraint", where it carries no hedging meaning at all. A paragraph about constrained optimization looked, to the counter, like a thicket of hesitant prose. The metric was not crashing; it was lying fluently.

We found the problem by reading the hit list rather than the code. Each counter can print the exact spans it matched, and scrolling that list made the contamination obvious within minutes: entry after entry was a fragment of a longer, innocent word. After we switched to word-boundary matching, the median hedge density across one corpus moved from 4.75 to 2.69 hits per thousand words, suggesting that roughly 43 percent of what we had counted as hedges were not hedges. The documents we measured had not changed; only the question the counter answered had.

The lesson generalizes beyond one vocabulary entry. The dangerous bugs in a measurement tool are typically not the ones that throw errors, but the ones that return plausible numbers, because a plausible number ends the investigation before it starts.

We now treat hit-list auditing as a routine step rather than an emergency one. Any counter whose matches cannot be printed and skimmed by a person is, in our view, not yet finished, no matter how clean its aggregate output looks.

## Failure mode 2: the ruler that stretched

The second failure mode is the length confound, in which a metric varies mechanically with how much text it is given. It appears whenever a ratio accumulates state as it reads, and it can quietly tilt any comparison that depends on the metric.

Type-token ratio, the proportion of distinct words in a document, is a natural way to measure vocabulary richness. It also drifts downward as documents grow longer, since writers reuse words, so a long essay and a short note by the same author can look like the work of two different writers. When we compared raw type-token ratio across seven institutions, we were largely comparing document lengths rather than writing styles.

The fix was to measure richness through a fixed-width sliding window instead, a variant often called the moving-average type-token ratio, so that each document is judged through frames of equal size. With length held constant this way, the apparent gap between the most and least lexically diverse institutions narrowed from 0.204 to 0.070, a reduction of roughly threefold, while the ranking of the institutions did not move.

One could argue that the original 0.204 gap was a genuine stylistic signal, and we considered that reading seriously. If it were genuine, though, it should survive equal-length measurement, and roughly two thirds of it did not. The likelier interpretation is that most of the apparent difference was the ruler, not the text.

The residual gap may still be real, and the unchanged ranking suggests the underlying signal was exaggerated rather than invented. We now treat a metric as incomplete until it declares its invariances, meaning the properties it should not respond to, because an invariance that can be stated can usually be tested.

Length was the obvious invariance to declare for richness, but the exercise turned up others as we worked through the list. A hedge-density metric should not respond to document topic, a sentence-length metric should not respond to punctuation conventions, and so on. Writing these declarations down forced several design conversations we had previously postponed, and a few of them changed the metrics themselves.

## Failure mode 3: the validator that only said PASS

The third failure mode is the silent validator, in which a checker cannot see part of its input yet reports success across the whole. It appears whenever a parser accepts a narrower format than the one it is asked to check, and it is arguably the most dangerous of the three, because its output is designed to end scrutiny.

Parsers drift out of sync in an ordinary way. A table format gains a convention, bolded headers or merged cells, one commit at a time, while the parser's idea of the format stays frozen. Nothing announces the divergence, since both sides keep working.

Our regression harness recomputed each metric and compared the results against expected values stored in a markdown table. The table parser skipped any cell containing bold text, and since mismatches can only be reported for cells that are compared, the harness printed a full column of PASS while part of the table remained invisible to it.

A validator that cannot fail is worse than no validator at all, because it converts the absence of checking into the appearance of assurance. Once we repaired the parser, the harness immediately surfaced six drifting values, most of them stale expectations that had not been updated after earlier metric fixes, and each one is now pinned by its own test.

The uncomfortable part was reviewing the historical record. Months of green runs had to be reinterpreted retroactively, since a PASS printed by a blind checker says nothing about the run it came from. We could not re-verify those runs individually, so we treated the entire stretch as unverified and re-established expectations from scratch on the current code.

## Why detection was difficult

All three failures shared a single root cause on our side: we trusted green output. The harness reported health, the counters returned plausible numbers, and each signal was read as evidence that the system worked, when in several cases it was only evidence that the system was running.

Could we have caught these earlier with better tests alone? Probably not, because our test suite had a structural blind spot: no check had been shown to fail. We had demonstrated that the tests passed, but not that they could fail, and a test that has never been red is closer to a hope than a guarantee.

To state it plainly: these bugs did not change any published conclusion, since the rankings we reported survived each fix. They did, however, change how much confidence those conclusions deserved, and we should have priced that uncertainty into the numbers from the beginning.

We should also be clear that these patterns aren't prescriptive. They are the failure modes we happened to meet in one measurement tool, and while we suspect they generalize, your system will likely have quieter variants of its own that a list like this cannot anticipate.

For readers of numbers we have already published, our advice is simple: treat any single metric as a hint and any comparison as provisional until the measurement survives a second, independent instrument. The rankings held in our case, but we would rather our readers hold that conclusion because they checked than because we said so.

## What we changed

As we continue to develop the profiler, we are changing the way we build and validate measurement code. Here is what we changed:

- Word-boundary matching for counting: our counters now match on token boundaries, with real segmentation for Chinese text. Vocabulary entries can no longer hide inside unrelated words.
- Declared invariances for metrics: each metric documents what it should not respond to, starting with document length. The regression suite tests those invariances directly rather than assuming them.
- Demonstrated failure before trust: a check must first be shown failing against a known-bad input before we rely on it. Our suite of twenty regression tests has now seen red at least once each.

The profiler, its vocabularies, and its test suite are available in the project repository for anyone who wants to inspect or rerun the measurements. We expect the tool to keep changing as we profile more institutions, and we intend for the failure-first rule to keep pace with whatever we add next.

If you maintain a measurement system of your own, we suspect the highest-value hour you can spend this week is not on a new metric but on an old one: pick the check you trust most, and try to make it fail on purpose. In our experience, the first attempt is often surprisingly easy, and what it reveals is usually worth the discomfort.

## Summary

Success in measuring style isn't about finding the cleverest metric. It's about building metrics you can defend: counters whose hits you can read, ratios whose blind spots you have named, and validators you have personally watched fail.

When building measurement tools, we try to follow three core principles:

- Prefer deterministic checks over judgments, so that any number can be replayed and any disagreement settled by hand.
- Name what a metric ignores, because an undeclared invariance will eventually be mistaken for a result.
- Require each test to fail once before you trust it, since a green light you have not seen turn red carries little information.

Measurement tools earn trust the way measurements do: slowly, and mostly by surviving attempts to break them. We are still early in that process, and we expect to remain in it for a while.

<!-- self-check: python3 profiler.py output/_p1-validation-samples/draft-anthropic.md（2026-09-08 终版实测）对照 templates/genre-playbook-anthropic.md §三预算表（median，P25–P75）：
✅ word_count 2103（P25–P75 2098–3145；贴 P25 下缘；reading_time 7.0=P25）
✅ avg_sentence_len 22.2（19.6–23.8；median 22.45）
✅ p90_sentence_len 35（30–41，硬上限 45）
✅ avg_paragraph_len 45.3（36.6–53.1；median 44.75；one_line_paragraphs=0，无单句段）
✅ number_per_1k 4.76（3.27–17.0；数字集中投向影响面披露：4.75→2.69 / 0.204→0.070 / six / twenty）
✅ precise_per_1k 2.38（0.47–3.95）
✅ year_per_1k 0.48（0.34–1.91；1 处 "early 2026"）
✅ links 0 / reference_entries 0 / citation_marks 0（median 均 0）
✅ hedge_per_1k 13.31（8.3–13.56，贴 P75 内缘；hedge:absolutist ≈ 5.6:1 ≥ 4.5:1）
✅ absolutist_per_1k 2.38（1.37–3.37；5 处：never×3 / must×1 / cannot-fail 类 1）
✅ quantifier_per_1k 5.71（4.29–7.51）
✅ first_person 57（21–69，"责任者 we"）
✅ exclamations 0（硬约束）/ questions 2（0–5；1 处小节标题设问 + 1 处自我批评节设问）
✅ cjk_chars 0（子串污染叙事改用罗马化 "yue" 表述，未引汉字原字符）
⚠️ objective_selfref 3（median 1.5，P75 2，min–max 0–15）——"this post"×2 + "this work"×1，略超 P75 但远在实测 max 内
⚠️ mattr 0.708（P25–P75 0.67–0.70，min–max 0.635–0.743）——略超 P75，命名概念复用（measurement contamination / silent validator）未压低 MATTR，与 playbook §三注记一致
⚠️ ttr 0.372（P25–P75 0.31–0.35）——长度敏感指标，playbook 标注"仅作参考"，不作达标判据
语步核对（§二 engineering-playbook 偏差版）：CONTEXT 开场（HOOK 缺席）→ FRAME 定义辨析+概念命名句（"We refer to this as measurement contamination"）→ ARGUE×3 模式清单三段式（定义→出现条件→示例）→ COUNTER 双层（"To state it plainly"澄清 + Why-detection 自我批评节 + aren't prescriptive 边界声明）→ APPLY 三条改进清单+资源指向 → CLOSE 成功重定义（"isn't about..."句式）+三原则清单+无感叹号展望句。禁令遵守：无外链、无参考文献、无感叹号、无单句段节拍器、无数字驱动机理论证。
-->
