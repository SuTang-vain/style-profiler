# Evaluation Is Power: The Business, the Science, and the Law of Judging AI

In April 2025, a 68-page paper landed in the AI world with an uncomfortable claim about the field's most-watched leaderboard. Thirteen researchers from Cohere Labs, AI2, Princeton, Stanford, and other institutions had analyzed roughly 2 million battles on Chatbot Arena, covering 243 models from 42 providers.

Some of the largest labs, the authors argued, had been allowed to test many unreleased variants in private and to publish only the one that scored best. The leaderboard the public saw was, in part, a highlight reel.

The accused platform did not collapse: it reportedly raised a nine-figure seed round last year, and this January announced a Series A at a billion-dollar valuation and renamed itself Arena. The accusation read less like a threat than like a pricing event.

An accusation of privileged access, answered by a higher valuation — how did judging models become such a powerful position, and such a well-paid one?

## Three questions

This essay argues that the answer is what we will call evaluative authority: the power to define what counts as a better model, and to be believed when you say so. That authority was once scattered across academic benchmarks and blog posts. It is now concentrating inside a small evaluation industry, and we think the incentives around it bend the numbers long before anyone commits fraud.

The power sits in the defining, the money in the being believed, and the story of the last two years is the two merging inside single companies.

We will answer three questions.

1) How evaluative authority became a business, and who pays for it.

2) Where exactly the incentives distort the measurement itself.

3) What practitioners — those of us who read leaderboards, buy evaluation, or build our own — should do differently.

What the measurement layer is comes first. The argument then moves through five layers: the leaderboard's corporate turn, the privileges of private testing, the evaluator's client list, the fragile science underneath, and the law now converting all of it into obligation. The optimists get their hearing before the field guide for working practitioners closes the piece.

## The measurement layer

Start with what the measurement layer actually is: on one side sit static benchmarks such as MMLU-Pro, GPQA, SWE-bench, LiveCodeBench, and ARC-AGI, each claiming to capture some slice of capability. On the other side sit live leaderboards, where humans or models judge outputs and scores update continuously.

Arena's text leaderboard alone has accumulated more than 7.7 million votes across 389 models, according to August statistics from opper.ai, a site that tracks the rankings industry. What began as a research project is now the industry's leaderboard of record.

The shift matters because of why it happened: static benchmarks saturate once they are public, because training corpora absorb them and their scores stop discriminating. Live leaderboards promised a moving target — fresh prompts, fresh voters, no fixed answer key to leak — and that promise concentrated our attention on one leaderboard. The buyer's problem is that both sides of the measurement layer now come with an interested party attached: the benchmark has its authors, and the leaderboard has its owners.

The audience has widened well beyond researchers: enterprise buyers shortlist vendors on these scores, coverage treats rank moves as news, and the labs themselves watch the leaderboard as an internal KPI. The Wall Street Journal has reported that OpenAI closely tracks its Arena position — an account relayed by aiglossary.news, a site that tracks AI industry coverage.

A score that moves procurement, coverage, and internal targets is no longer a description of the market but infrastructure for it, and infrastructure, once load-bearing, attracts owners.

The natural question for us is who those owners are and what they sell, and the first place to look is the leaderboard itself.

## 1. The referee became a business: the corporate turn

The corporate turn is recent and fast: according to an April guide from uper.pl, an AI industry publication, the company raised a reported $100 million seed round last year. This January the company rebranded as Arena and announced a reported $150 million Series A at a $1.7 billion valuation, with a16z among the investors.

The revenue plan matters more than the round sizes: Arena's monetization, per the same guide, runs through enterprise audits, API access, and premium analytics. The referee is no longer a volunteer project; it sells services, and its buyers include the very labs it ranks.

None of this proves dishonesty, because paid audits can be real audits. But the commercial structure changes what a leaderboard is: every design decision — which models get tested, which results get displayed, which features ship — is now also a product decision made under investor expectations.

There is also a quieter economic logic underneath: trust in a score aggregates. The more buyers watch one leaderboard, the more its rank moves deals, and the more rational it is for the next buyer to watch the same leaderboard.

And the audience keeps treating the score as neutral ground truth: when a frontier lab watches its rank as a KPI, the leaderboard stops describing the race and starts steering it — it is Goodhart's law, on a leaderboard. None of this makes the score useless — it makes the score interested, and an interested score deserves the same care we give any other claim from any other business.

Ownership, though, is only the surface of the problem, and the deeper question is who gets to test what — and who decides what the public sees.

## 2. Private tests, public scores: privileged access

The Leaderboard Illusion documents a two-tier testing regime: according to the authors, large labs could run many unreleased variants through the leaderboard privately, then submit only the strongest for public ranking. Meta, the paper claims, tested 27 private variants of Llama 4 before release, and the leaderboard saw one.

The statistical damage is subtle but real, because Arena's scores rest on the Bradley-Terry model, whose fairness depends on matchups sampling the field honestly. Selective disclosure breaks that premise: a lab that publishes only its winning variants is reporting luck plus selection, not quality alone.

The paper goes further, claiming effects on how open models fare and how far scores inflate, and those specific numbers are contested — we will return to the dispute in a moment. The coverage traveled fast: TechCrunch's headline on 30 April described a study accusing LM Arena of helping top labs game its benchmark. Separately, one study relayed by the odds-comparison site OddsShopper claims that coordinated voting can move a model's rank outright — independent evidence for the same structural point.

LMArena's response deserves honest weight: the company publicly disputed several of the paper's headline numbers and subsequently changed its operating policies. Both facts matter, because the dispute suggests some accusations may be overstated, while the policy changes concede the mechanism was real enough to fix.

Our read is narrower than the paper's claims and harder than the company's response. Whatever the true numbers, a structure in which some labs rehearse in private and publish selectively is a structure whose scores we cannot audit from outside. We believe the capability to rehearse in private is itself the finding and the exact percentages are secondary.

It is worth noting what would settle this — pre-registered submissions, public logs of private tests, or an independent audit — because none of these exists today. Until one does, every arena score carries an invisible asterisk whose size we cannot check.

This is also why the dispute over percentages, real as it is, can mislead us: the percentage is a question about one paper, while the capability is a question about the structure, and structures outlast papers.

If the leaderboard's problem is privileged access, the next layer is privileged interest — the companies that sell evaluation to the evaluated.

## 3. The evaluated pay the evaluator: the client list

Consider Patronus AI, an evaluation vendor founded by former Meta researchers three years ago. This June it raised a reported $50 million Series B led by Greenfield, bringing total funding to $70 million. The June reports put most leading frontier labs and cloud providers on its customer list.

The product direction is telling: Patronus now promotes what it calls Digital World Models, digital twins of enterprise software in which agents get stress-tested before deployment. The buyer of the stress test is the builder of the agent — the graded, in other words, commission the grading.

Here we should be careful about what this does and does not imply: a vendor paid by the graded is not automatically captured, since carmakers pay for crash testing too. But the incentive gradient points toward comfort — toward tests clients can pass, metrics clients already optimize, and findings that embarrass no one who pays. This is not an argument for refusing their products; it is an argument for reading the contract before reading the score.

Comfort has a recognizable product shape: fixed public test sets the client can rehearse, aggregate scores without confidence intervals, and reports that rank the client against anonymized peers. All of them are what a market of the graded, buying from the grader, predictably demands.

The market, notably, has started pricing that distrust: an April note from the research site implicator.ai describes an AI Top 40 index that weights benchmarks by perceived trustworthiness. SWE-bench, LiveCodeBench, GPQA, ARC-AGI, and Humanity's Last Exam carry a 2.0-times weight in that index, while Chatbot Arena and MMLU-Pro are cut to 0.5. A private aggregator now discounts the field's most famous leaderboard by half, and that is a market verdict on evaluative authority, priced in public.

Yet even an honest vendor with perfect incentives faces a deeper problem: the instruments themselves are weaker than their public authority suggests.

## 4. The science underneath is thinner than it looks: fragile instruments

A July review by the EvalSafetyGap project relays one statistic worth reading twice. Of 445 benchmark papers surveyed by Bean and colleagues (2025), only 16 percent used uncertainty estimates or statistical tests when comparing systems. More than four of five published comparisons never checked whether the differences they reported were real.

The same review cites a European Commission Joint Research Centre survey by Eriksson and colleagues. That survey questions whether many benchmarks measure the capability they advertise — the construct-validity problem — and catalogs how incentives invite gaming of whatever is measured.

Practitioners see the cracks up close: an April industry review by Kili Technology catalogs contamination of static benchmarks, gaming, and substantial annotation error rates in widely used datasets. A benchmark can be famous, heavily cited, and quietly rotten at the item level.

Put the three together and the crisis is not fraud but rigor. Most of the field's quantitative authority rests on comparisons that would not pass a first-year statistics seminar, and the measurement layer demands a trust it has not fully earned.

The rigor is missing for reasons we know well, because uncertainty testing costs time, complicates launch narratives, and can turn a victory into a tie. The incentives we described above do not stop at the leaderboard; they reach down into methodology itself.

Into this gap — concentrated authority, aligned incentives, fragile instruments — walks the state.

## 5. The state walks in: the law

The EU AI Act is converting evaluation from a market tool into a legal duty. The regulation entered into force in August 2024, prohibited-practice rules applied from February 2025, and obligations for general-purpose models — technical documentation and evaluation disclosure — have applied since August 2025.

August 2026 brought the Article 50 transparency obligations and new enforcement powers into force. The Digital Omnibus on AI has moved the main high-risk obligations to 2 December 2027. As of this writing, general-purpose evaluation duties are in their second year of execution, transparency duties are one month old, and the high-risk regime now has a fixed date.

The significance is not bureaucratic: once evaluation is legally mandated, demand stops being optional, and the question of who performs it — under what conflicts, with what methods — becomes a question of law. Evaluative authority is on its way to becoming licensed authority.

A legal duty also changes who the buyer is. When evaluation is voluntary, the buyer is a curious engineering team; when it is mandatory, the buyer is a compliance function with a budget and a deadline, shopping for defensibility rather than insight. Vendors will build for the second buyer, because the second buyer always pays.

The money will follow the duty: compliance budgets are stickier than curiosity budgets, and vendors who can sell audit-grade measurement will inherit a guaranteed floor of demand. Whether that floor produces better measurement is a separate question, and one the optimists answer faster than we do. A guaranteed floor of demand is also a floor of authority.

We should not overstate the present, because obligations on paper are not yet outcomes in court and supervisory capacity remains thin. But the direction is set, and the strongest objections to our argument deserve a direct hearing.

## What the optimists get right

Three objections circulate among people who know this industry well, and each deserves a verdict, not a shrug. Two of the three stay open, as we will see, and that is itself part of the answer.

The first objection says the market self-corrects: Arena disputed the paper's numbers and reformed its policies, and distrust is already priced, as the implicator.ai weighting shows. So could the market simply fix this on its own? Our verdict: left open, because policy changes addressed one mechanism while the revenue structure stays unchanged, and no independent audit verifies what happens inside private testing today. Self-correction is claimed, not demonstrated.

The second objection says every metric gets gamed, so the remedy is better benchmarks rather than suspicion of measurement itself. Our verdict: mostly rebutted, because the 16 percent figure shows the weakness sits upstream of gaming — most comparisons lack statistical grounding even with no adversary in the room. Better benchmarks help, but they leave the interest structure untouched.

The third objection warns that regulation will entrench incumbents, because only large labs can afford compliance-grade evaluation. Our verdict: left open, flagged as a live risk. The evidence so far does not settle whether the Act creates a diverse audit market or a small licensed oligopoly, and we should watch the first enforcement cycles before judging.

Until those cycles arrive, practitioners cannot wait for the referee question to resolve itself; we need a working posture now.

## A field guide for practitioners

The practical question is what we do on Monday morning, while the structural questions stay open. This analysis offers three checks — one for each way we touch the measurement layer: reading its outputs, buying its services, or building our own.

1) When we read leaderboards, ask who could test privately, how many variants were run, and whether the disclosure policy is public. If it is not, we must assume rehearsal happened and treat any single ranking as a marketing sample with a selection process, not as a measurement of the field.

2) When we procure evaluation, ask the vendor who else pays them. If the answer is the graded, negotiate adversarial terms — pre-registered test sets, held-out items the client never sees, and contractual rights to disclose failures.

3) When we build our own harness, run it on tasks drawn from our real workload and do the statistics the field skips — confidence intervals, paired comparisons, corrections for multiple testing. Given that only about one in six published benchmark papers checks significance, a competent internal harness already has more rigor than most public numbers.

Each check stands alone, but the compound is the point: a team that discounts leaderboards, buys evaluation on adversarial terms, and trusts its own harness has quietly built its own small measurement layer. That is where evaluative authority should live for us — close to the work and far from the marketing.

None of the three requires permission from the industry we have described, and that may be the most useful fact in this piece.

## So should we stop reading leaderboards

So should we stop reading leaderboards? No — but we should read them the way we read a weather forecast funded by umbrella sellers: a useful signal from an interested source.

What we are left with is four conclusions:

1) Evaluative authority is now a business, and its customers are frequently the evaluated.

2) The strongest documented distortion is structural — private testing plus selective disclosure — not proven fraud, and the accused platform disputes the specific numbers.

3) The science beneath the scores is weaker than their public authority: only 16 percent of benchmark papers test whether their comparisons are real.

4) The law is converting evaluation from a choice into a duty, which will entrench whoever sells compliance-grade measurement.

One question stays open, and the current evidence does not cover it: whether independent, public measurement infrastructure will emerge before the licensed private kind locks in. Nothing in the record so far answers it either way.

The referee now has investors, customers, and a license, but that does not make the game unplayable, and it does not excuse us from doing our own measuring. It means we should stop mistaking the whistle for the truth.

## Sources

- Singh et al., "The Leaderboard Illusion" (paper), from Cohere Labs, AI2, Princeton, Stanford, and other institutions.
- TechCrunch, "Study accuses LM Arena of helping top AI labs game its benchmark" (30 April).
- LMArena, public response disputing headline numbers, and subsequent operating-policy changes.
- uper.pl, guide covering the Arena seed round, Series A, rebrand, and monetization lines (April).
- opper.ai, leaderboard statistics (August).
- Patronus AI, Greenfield-led Series B announcement (June); company materials on Digital World Models.
- implicator.ai, AI Top 40 methodology note (April).
- Bean et al., survey of benchmark papers; Eriksson et al., European Commission Joint Research Centre review — both as relayed by the EvalSafetyGap review (July).
- Kili Technology, industry review of benchmark quality (April).
- artificialintelligenceact.eu, high-level summary of the EU AI Act (late August); CIVAC, compliance briefing (May); the Digital Omnibus on AI, which moved the main high-risk obligations to December next year.
