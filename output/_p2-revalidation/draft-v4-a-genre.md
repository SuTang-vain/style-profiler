# The Evaluation Industry Is Replaying the History of Credit Rating Agencies

In April 2007, an analyst at Standard & Poor's wrote in an internal email that later surfaced in a Senate exhibit: a deal "could be structured by cows and we would rate it." His agency was one of three agencies that, by official designation, decided what safe meant for most of the bond market, and within 18 months the grades those agencies had printed on mortgage securities sat at the center of the 2008 financial crisis.

In the spring of 2025, third-party researchers examining the most-watched AI leaderboard reported that a frontier lab had privately tested 27 variants of a flagship model and released only the one that ranked highest. The leaderboard was not a regulator; it was a small organization recently spun out of a university project, reportedly raising about $100 million at a valuation near $600 million while labs competed for rank on its table. Nobody involved called it a rating agency, but those of us who build, buy, or regulate AI systems should take the parallel seriously.

The parallel is not decorative: this essay argues that the AI evaluation industry — the organizations that publish benchmarks, leaderboards, and model ratings — is replaying the institutional history of the credit rating agencies. It answers three questions: how the money is arranged between the graders and the graded; why the grades inflate and why shopping for them works; and why oversight lags, plus what we can do in the meantime.

Three terms carry the argument, and they stay fixed throughout. A benchmark issuer is any organization that publishes a test, a score, or a ranking that buyers use to compare models. Rating shopping means selecting, influencing, or privately previewing the grader most likely to return a favorable grade. The evaluation industry is all of it together — issuers, labs, sponsors, and the market in which grades on AI systems are produced and bought. We are both the audience for these grades and, increasingly, their sponsors.

The replay starts, as it did the first time, with who pays.

## The License to Grade

The modern rating system was created by regulation, not by markets. In 1975 the Securities and Exchange Commission designated, in practice, three agencies — Moody's, Standard & Poor's, and Fitch — as Nationally Recognized Statistical Rating Organizations. A growing body of rules was tied to their grades: banks, pension funds, and insurers were required or nudged to hold securities that the designated graders called safe.

According to the SEC's own later reports, the designation converted private opinion into public license; demand for a rating no longer depended on being right, only on its official standing. That is the first ingredient of the replay: a grade whose value comes from the buyer's need to have one, not from the grade's record of being right. We should hold that definition in mind, because it describes most of what our leaderboards now sell.

The money followed the license. The agencies had once charged investors for their ratings, but by the mid-seventies they were charging issuers — the very institutions whose securities they graded. At the structured-finance peak, that business generated roughly 40 percent of Moody's revenue, according to later congressional findings, and the three agencies together covered about 95 percent of the rated market.

When a grader's largest buyers are the institutions it grades, the grade stops being a product sold to readers; it becomes a service sold to the graded. Nothing about this requires bad faith. It requires only an arrangement of money and permission, and that arrangement is the one our field has been quietly building.

The failure, when it came, arrived after years of visible warnings. The agencies held investment-grade ratings on Enron until days before its bankruptcy, and they stamped the safest grade on tens of thousands of mortgage securities before beginning mass downgrades in the middle of 2007. The largest legal claims — about $1.4 billion against Standard & Poor's in a 2015 settlement, and about $864 million paid by Moody's two years later — sent no executive to jail, and the issuer-pays model survived.

Dodd-Frank, passed after the crisis, ordered studies and removed some statutory references to ratings, but the license, the revenue model, and the market share all survived the crisis they helped make. None of this required villains, which is precisely why we should expect the pattern to repeat, and why we should study the first crisis before living through the second. The money comes first.

## Who Pays the Grader

Start with the flow of money, because every later failure follows from it. We like to describe our benchmarks as public goods: datasets, harnesses, and leaderboards maintained by universities or small nonprofits. In practice, the boundary between the graders and the graded is already weak.

According to reporting last year, Meta paid roughly $14 billion for about a 49 percent stake in Scale AI, a company that both sells services to frontier labs and operates its own model evaluations. One widely covered benchmark, introduced in early 2025 with some 3,000 questions, was co-created by that same company and an AI-safety nonprofit, with a prize pool of about $500,000. The grader and the graded are no longer separate institutions; increasingly, they are investors in one another.

The rating agencies did not need envelopes of cash, and neither does this market: the conflict travels through ordinary commercial channels — fees, sponsorships, private testing arrangements, and a steady migration of benchmark authors into the labs their benchmarks rank. Each transaction is defensible on its own, and none of us should be surprised that each one is defended.

The pattern is the point: a grader that depends on the graded for funding, data, or talent faces pressure to produce grades the graded can use. The grade stops being a measurement; it becomes a service sold to the graded. The pressure rarely needs to be spoken aloud, and it operates whether or not anyone intends it — we should not expect to find it written into any contract.

The most instructive evidence so far is a 2025 paper on the largest community-run leaderboard. Its authors — outside researchers, not lab spokespeople — reported that a small set of major labs received preferential access, including more private variants and more returned data; one lab, by the paper's account, tested 27 private variants before its flagship release. The operators disputed some of the analysis and later revised some policies, but the pattern the paper described does not depend on any one operator's intent. It is the issuer-pays model rebuilt from access rather than invoices.

Money explains why the graders bend; the next mechanism is why the grades themselves keep rising.

## The Inflation Machine

Ratings inflate when the buyer of the grade prefers a high one. In the agency era, the share of securities with the safest grade expanded until it covered products that were not safe, and the evaluation industry is compressing the same history into a few years. We have spent those years celebrating each new record on the leaderboard.

MMLU, a benchmark released in 2020 with some 15,000 questions across 57 subjects, was hard enough that GPT-3 scored roughly 44 percent. Frontier models now report around 90 percent on it, and the benchmark is widely described as saturated. SWE-bench, introduced in 2023, went from about 2 percent solved to more than 70 percent on its verified subset within roughly two years. On paper, capability soared — and some of it genuinely did.

But part of every climb is the grade getting easier to earn, and three mechanisms do the inflating; each has an agency precedent.

The first is teaching to the test. Training data absorbs the test items, deliberately or through web-scale collection, the way structured products were once built precisely against the agencies' published models. The second is selection: a lab can run many evaluations and headline the best one, just as an issuer could preview many agencies and publish the highest grade.

The third is drift: a benchmark built to separate last year's models cannot separate this year's, so the scale silently re-centers. A score of 90 percent stops meaning what it meant when the benchmark was young. Each mechanism is measurable in principle; in practice, labs report their own scores, and we rarely see the attempts that were not headlined.

The honest reading of current leaderboards is therefore narrow. They measure movement on specific, increasingly exploited tests, most of them self-administered, under reporting norms that no outside party enforces. Independent evaluations do find real capability gains; the claim here is narrower than a denial of progress. When we buy on these numbers, we are buying the grader's incentives along with the grade.

The precision of a leaderboard rank is not evidence on the gap between two models, and treating a two-point lead as a reason to buy is roughly as disciplined as treating the safest grade as a physical constant. Inflated grades would matter less if buyers could not shop for them — and buyers can.

## Shopping for the Grade

Shopping was the crisis mechanism in its purest form. An issuer of structured products could take the same deal to more than one agency, compare the grades their models implied, and hire the lenient one. Senate investigators later published the bargaining across more than 600 pages of exhibits: bankers threatening to walk, analysts adjusting assumptions.

The agencies' published methodologies, intended as transparency, doubled as engineering specifications: design the deal to the model, and the model returns the grade. That lesson was not lost on anyone who sells a product that gets graded.

The evaluation equivalent is already routine in our field; it simply looks more respectable. A lab preparing a release can choose among dozens of benchmarks, run them privately, tune the announcement to the strong results, and say nothing about the rest. When released scores disappoint, the explanation is prompt formatting or harness settings — sometimes true, in general unverifiable from outside.

Where a leaderboard permits private testing, the preview-before-publish loop becomes literal. The flagship case from last year — dozens of variants tried on the leaderboard, only the winner shipped — was legal and disclosed in fine print, and it was damaging precisely because it was routine.

Rating shopping works, and we should be honest about why: the lab wants a grade that moves the market, and the market reads ranks rather than methodologies. Most procurement teams, most journalists, and most executives will never read the contamination analysis or the harness notes; they will see a number and a rank. The agencies learned this at the peak — once a grade becomes a formality in someone else's process, its meaning matters less than its presence. We are rebuilding that formality in our own procurement processes.

Which raises the question the industry prefers to defer: where is the regulator in all of this?

## The Regulator Arrives Late

Regulation, in the agency story, arrived late and arrived shallow, and we have little reason to expect our own regulators to move faster. The reform act passed two years before the crisis gave the SEC authority over the agencies but barred it from regulating the substance of their methodologies — oversight of everything except the thing that mattered.

After the crisis, Dodd-Frank tightened disclosure, created an Office of Credit Ratings, and ordered statutory reliance on ratings removed. A decade later, the most consequential ideas — including a proposal to assign agencies to deals rather than let issuers choose — had been studied and shelved. The agencies settled, paid, and continued; the license was never in danger.

The evaluation industry sits where the agencies sat two decades before their collapse: systemically important, commercially entangled, and essentially unsupervised as an industry. The European Union's AI Act, whose obligations for general-purpose models began applying in August 2025, leans heavily on provider-led evaluation and conformity assessment, under which the graded party runs or commissions the test. Violations can in principle draw fines of up to 3 percent of global revenue, but the grade itself — the benchmark score — sits outside the law's reach.

Voluntary commitments announced in 2023 have thinned as administrations and priorities changed. No jurisdiction assigns liability to a benchmark issuer whose grade proves wrong, and no standard defines what an evaluator must disclose about funding, access, or private testing. We have no equivalent of the Senate exhibit, and we may not get one before the damage is priced in.

The lag is not an accident of slow regulators; it is produced by the same entanglement it fails to police. Regulators need the industry's expertise to understand the industry's products, and that expertise lives inside the graded labs. The rating agencies had decades between designation and crisis; we are on a compressed timeline, because procurement decisions already depend on these grades while the norms are still being written.

If the replay is this faithful, the standard objections deserve a hearing of their own.

## Four Objections, Two Verdicts

Four objections to the analogy are worth taking seriously. Two of them do not survive contact with the record; two remain genuinely open and are marked as such.

The first objection holds that no issuer-pays conflict exists, because labs do not mail checks to benchmark authors. The mechanism does not require invoices. Sponsorship, equity, private access, and talent flows bind grader to graded as reliably as fees once did, and the record is already thicker at this stage than anything documented about the agencies in their first two decades. This objection is rebutted.

The second holds that AI evaluations are transparent and reproducible in a way the old structured-product models were not, so deception cannot hide. Reproducibility covers the harness, not the training data, and the critical question — did the model see the test — is precisely the one an outside party cannot audit. Transparency of method also coexisted with shopping in the agency era; the published criteria were the shopping list. This objection is rebutted as well.

The third objection argues that competition among evaluators will discipline them, since reputation is a grader's only asset. The same argument was made for the agencies, and it failed for a specific reason: the buyer of the grade was not the party harmed by its inflation — pension funds, not investment banks, held the toxic paper. In AI, the harmed party is likewise the downstream buyer of the model, not the lab that commissioned the grade. Whether reputational discipline can work under that split incentive remains unresolved, and we leave this one open.

The fourth objection calls the analogy too pessimistic, pointing to independent auditors and third-party evaluations that are growing faster than any regulator of the agency era. The trend is real: academic harnesses, red-team networks, and a few genuinely independent evaluators now exist. But their funding base is small next to the marketing money their findings might contradict, and no evidence yet answers whether they can scale before the grades they check settle into procurement requirements. We leave this one open as well.

With these questions open, we cannot wait for the evidence to finish arriving. A working discipline is needed now.

## A Buyer's Discipline

The practical translation is a short list: four tests we can apply to any evaluation before we let its grade near a decision. None of the four requires new institutions; all four require only that we read a model grade the way a bond buyer should have read the safest grade.

First, follow the money: who funds the grader, through sponsorships, equity, service contracts, or private testing arrangements. A benchmark issuer whose funding comes from the graded is a marketing instrument until shown otherwise, and its grades should be read as advertising rather than measurement.

Second, ask who grades: whether the scores were self-administered and self-reported, or run by a party with no stake in the outcome. Self-reported numbers are claims, not measurements, and any claim that an independent party has not reproduced must be discounted.

Third, check the headroom: whether the test can still separate the top of the field, and whether its items stayed out of training data. A saturated or contaminated benchmark measures the past, and grades near its ceiling carry little information about the differences that matter to us.

Fourth, ask who is liable: if the grade proves wrong — the model fails in deployment, the rank reverses under independent testing — who bears the loss. A grader with no downside is a grader whose incentives point toward the graded, not toward the buyer.

A grade that fails one of these tests deserves a discount, and a grade that fails two or more should not enter a procurement decision at all. That sounds harsh, but it is only the discipline the bond market skipped, and it brings the argument back to the question we opened with.

## The Ending Is Not Written Yet

So will the evaluation industry end the way the rating agencies did, in a single season of mass downgrades? Probably not in that form: AI grades are not wired into capital requirements, and there is no leverage to unwind. But the mechanism does not need the same ending to impose the same costs on us.

A market that buys grades instead of measurements misallocates money, attention, and trust, and it does so quietly, quarter by quarter, while we read the ranks, until the gap between the grade and the graded thing becomes impossible to ignore; three conclusions follow.

1) The conflicts are structural, not personal. The agencies were staffed by competent professionals, and the labs and leaderboard operators mostly are too; incentives, not character, are what replays.

2) The inflation is measurable and already visible: scores climbing toward every ceiling, test items leaking into training data, private previews preceding public ranks. We should treat single-number capability claims as marketing until they are independently reproduced.

3) Regulation will lag by the same mechanism as last time, so the first credible discipline may come from buyers — and we are the buyers. Procurement that applies the four tests is the only downgrade threat the current system can feel.

What this essay's evidence does not cover: the private contracts between labs and evaluation vendors, where disclosure is too thin to map the money precisely; the base rate of contamination across major benchmarks, which remains unmeasured at scale; and the question that will decide the ending. Can an honest grader make money in this market, and will anyone pay for one before the first real scandal forces the issue?

In 1975, the government printed a small number of licenses and called the printed grades safety. Fifty years later, we know what such a license is worth when the licensee pays for the ink. The AI industry is printing its grades again, in a different font, on a faster press, and this time we are the readers. For now, we still get to choose whether to read the fine print or wait for the cows.
