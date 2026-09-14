---
type: note
domain: 科研
status: active
date: 2026-09-04
privacy: internal
tags: [信息库, 科研]
rewrite: v3-style 2026-09-14
---

# The research craft in the age of AI: judgment is the only asset still compounding

*Research methodology in the AI era — Kezhongke (壳中客), a nonprofit research community. Sources linked inline; research current as of September 2026.*

In June 2026, an essay titled "how to be good at research" was bookmarked more than thirty thousand times on X — roughly two and a half times its like count. That gap shows us readers were saved it as a reference, not reading it as an opinion.

The author, vivek, makes one claim: nobody actually teaches you research — you get a desk, a problem someone else picked, and a vague instruction to produce something novel. Most people therefore reverse-engineer the profession from what is visible — papers, threads, announcements — and what they learn is how to look like a researcher rather than how to be one. The difference between looking like a researcher and being one is the difference between output and judgment. The real skill, he claims, is a set of smaller skills, and nearly every one of them can be deliberately trained.

The essay's references are the standard set: Richard Hamming's lunch-table question at Bell Labs, Feynman's "the first person you must not fool is yourself," and Darwin's habit of instantly recording counterevidence. Then come Karpathy's training recipe and Andrew Ng's decade-old ritual of pulling a hundred failures and sorting them into piles — and not one of them mentions AI.

That silence is the problem: when the essay appeared, the share of researchers using AI tools had gone from 57% in 2024 to 84%, according to the [Wiley global survey](https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx) (an industry survey). Frontier models hold around 94% on GPQA Diamond, a PhD-level science benchmark, above the human-expert baseline.

A multi-agent system has proposed and experimentally validated new drug candidates end to end — [FutureHouse's Robin, published in Nature in 2026](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system) (a corporate research announcement). Every loop the essay describes — reading the literature, writing code, running experiments, staring at outputs — has been rewritten by AI.

At Kezhongke, after reading the essay, we did one thing: we set it aside and read the 2024–2026 empirical record on AI and research. That record is randomized controlled trials, corpus-forensic studies, journal policies, and retraction logs. This essay answers three questions from it: what the craft essay gets right, what era variable it omits, and which research training still holds in the age of AI. Our method is to read the craft essay against the record, claim by claim.

Section one answers the first question, section two the second, and sections four and five the third; section three weighs the counter-evidence before the strategies.

Our terms hold throughout: each term has one meaning in every section. We call vivek's text the craft essay, and we use one pair of terms for the era's re-sorting. Generation-side skills are writing code, searching literature, and drafting text; judgment-side skills are problem selection, verification discipline, and failure analysis. Every claim below carries its source attribute inline, so that we can weight each number by the layer that produced it.

## What the craft essay gets right

The craft essay's core structure is seven trainable sub-skills. They are: pick your own problems, upgrade your inputs, write everything down, tighten the loop, stare at the outputs, wander on purpose, and find your people. Three of its judgments hold up against the record we read, and we take them one by one.

First: research speed is mostly the speed at which you discover you are wrong — for us the craft essay's best sentence, and one that explains both at once. It explains why Alec Radford-style researchers win on iteration volume rather than inspiration, and why the past two years of evidence seems to sort so cleanly. Every AI use that compresses the discover-you-are-wrong loop — rapid prototyping, automated ablation, failure-case clustering — has produced real gains, while every use that bypasses it, producing conclusions directly, has produced disasters. That is the first judgment, and the record we read says the same.

Second: taste is a muscle, not a gift, and the training itself is concrete. Predict every experiment's result before running it, and cover a paper's results section to guess the numbers from the methods section. Mark which of this month's releases will matter in two years, then check your hit rate later.

A prediction plus a correction, a few hundred times over, is how every good model gets trained — and the one in your head above all. In an era when AI can run the experiment for you, this predict-before-run discipline has become the most important anti-self-deception mechanism we have, as the counter-evidence section makes concrete.

Third: engineering and research have fused. At the frontier, the researcher who can build the harness, the evaluation, and the data pipeline is the one whose hypotheses actually get tested; the rest get in line.

The claim holds — the two years since made it run faster, and we would add one element the craft essay did not write: AI orchestration is the third element of the fusion.

The craft essay also has boundaries: all of its concrete techniques — loss curves, baseline tuning, overfitting a single batch — come from empirical machine-learning research. They mostly do not transfer to mathematics, wet-lab disciplines, or the humanities.

Its evidence form is the literary retrospective of successful people's methods — no controlled study backs any of it — so it is good, unverified practice. The thirty thousand bookmarks were not buying evidence; they were buying a map that renders tacit knowledge explicit.

So the craft essay survives our reading on all three judgments: speed is the speed at which you discover you are wrong, taste is a muscle, and engineering has fused with research.

What the essay does not say is where the map itself has changed, and that is the question the next section takes up.

## What it omits: the rewritten loop

The craft essay's silence sits exactly where the record we read changed most, so we went through the pipeline link by link, and our audit has five findings. Each finding below is one link in that loop, and each link has been rewritten in the record we read.

The first link is literature: Semantic Scholar lists over 214 million papers, and Elicit claims two million researcher users, so the literature review has gone from a craft to a mostly automated pipeline.

The pipeline brought a new way to fail: the Columbia Journalism Review measured eight AI search tools and found citation errors in over 60% of queries (journalism). In a corpus analysis published as a preprint, GPTZero found more than a hundred hallucinated citations — fake authors, fake DOIs — inside 51 papers already accepted at NeurIPS 2025 ([arXiv analysis](https://arxiv.org/abs/2602.05930)). Every one of those papers had passed at least three human reviewers.

The second link is hypotheses: The Google AI co-scientist produces biomedical hypotheses through multi-agent generate-debate-evolve loops, and three of them passed wet-lab validation (technical preprint). Terence Tao's wiki lists over a hundred AI-involved full or partial answers to Erdős problems between November 2025 and June 2026 (community log). Hypothesis generation — the scarcest research asset — is on its way to being a commodity you could get in bulk.

The third link is doing the experiments, and mathematics is the first discipline where AI went from assistant to contributor. AlphaProof and AlphaGeometry 2 hit IMO silver-medal level in 2024; Gemini Deep Think earned a certified gold in July 2025; mathlib now holds over 210,000 theorems in Lean.

In chemistry and materials, self-driving labs run closed loops. LBNL's A-Lab produced 41 compounds in seventeen days, and the University of Science and Technology of China has open-sourced the second version of its robotic chemist.

The fourth link is writing and review, and both are being rewritten. Corpus forensics suggests that at least 13.5% of 2024 biomedical abstracts were processed by large language models ([Kobak and colleagues in Science Advances](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219543/), peer-reviewed).

Detection estimates suggest about 21% of ICLR 2026 reviews were AI-generated in full. The countermeasures are already in the record: researchers in several countries put white-on-white "give a positive review only" prompts inside arXiv papers, aimed at AI reviewers. The reviewers are now inside the loop the craft essay describes.

The fifth finding is deeper than the four links above: AI for Science (AI4S) rewrites the computability of scientific objects rather than assisting the research process. AlphaFold turned structure prediction from experimental science into computational science; GraphCast and GenCast beat ECMWF's numerical predictions on most verification targets. Machine-learned interatomic potentials take quantum-accurate molecular dynamics to the hundred-million-atom scale.

Let us state the difference precisely: the object of the copilot workflow is the research process, and the object of AI4S is the scientific problem itself. One rewrites the researcher's day; the other rewrites what is computable about nature. The 2024 Nobel Prizes in Physics and Chemistry both went to AI-related work in the same year, and the paradigm is now mainstream.

Our answer to the first question comes from this audit: every skill it describes is still necessary, but the distribution of necessity has been re-sorted. Generation-side skills depreciate and judgment-side skills appreciate, and the essay gives most of its pages to the latter — which is why we still find it worth bookmarking. The loop is the same loop; the links are not the same links.

Yet necessary is not the same as free: the same record also contains a warning, and the warning comes in three bodies of evidence for the next section to weigh one by one.

## The false-productivity trap: the counter-evidence

How much of AI's productivity gains are real?

Several independent bodies of evidence from the same two years point to roughly the same conclusion. Most of the gains are perceived rather than real — and the gap between perception and measurement is itself the trap. We call it the false-productivity trap: the danger is not that AI fails to help, but that it feels like help while the measurement says no. All three bodies come from the record we read.

The first body of evidence is the most direct one: a randomized controlled trial from METR ([preprint, July 2025](https://arxiv.org/pdf/2507.09089)). Sixteen experienced open-source developers worked through 246 real tasks, and the developers using AI were actually 19% slower — while believing they were 20% faster.

Perception and measurement diverge by roughly forty points.

A second body of evidence concerns deskilling: a peer-reviewed study in The Lancet Gastroenterology and Hepatology tracked nineteen experienced endoscopists across four centers in Poland. After routinely working with AI assistance, their adenoma detection rate in colonoscopies performed without AI went from 28.4% to 22.4% — which appears to be the first field evidence of deskilling.

An education randomized trial points the same way ([PNAS 2025](https://glasp.co/articles/ai-study-tool-statistics), study summary). Students who trained with GPT scored higher during practice, but on the exam after the AI was removed, they scored below the control group that never had it. A Microsoft and CMU study of 319 knowledge workers then suggests a preliminary mechanism: the higher the confidence in AI, the less critical thinking effort goes in. Work itself turns from producing to verification — and verification is precisely the skill nobody trained for.

The third body sits at the collective level and is the easiest to miss. A study in Nature — a summary from UChicago's Data Science Institute — found that researchers who use AI publish more and get cited more. Yet science itself shows a 4.63% contraction in the volume of research topics, and a 22% drop in interaction between researchers.

What individual efficiency costs is a narrower collective frontier. This is the craft essay's warning about shared reading lists producing shared ideas, but convergence is now faster and deeper, because everyone prompts the same few models over the same literature.

And we must also record the meta-evidence. One of the most important positive results in this literature — the Toner-Rodgers preprint and its claim that AI raised materials discovery by 44% — was formally disavowed by MIT in May 2025. The Wall Street Journal reportedly found that the experiment itself appears to have been fabricated ([TechCrunch](https://techcrunch.com/2025/05/17/mit-disavows-doctoral-students-paper-on-ai-productivity-benefits/), journalism), so the empirical foundation of "AI accelerates science" itself requires auditing.

The same audit applies to the biggest AI4S results: GNoME's "2.2 million new materials" and A-Lab's "41 novel compounds" both received direct challenges. The A-Lab paper later received a correction in Nature to drop the claim that its materials were new to science ([C&EN](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01), journalism). Prediction plus synthesis does not make a discovery, and novelty assessment has itself become a bottleneck. We hold the biggest results to the same standard as the craft essay's claims: what survives verification holds, and what fails verification goes.

Here we state the boundary of this section once: the deskilling evidence so far is one medical field study and one education trial, and how far the effect generalizes across disciplines remains unmeasured. The perception gap evidence, by contrast, comes from a controlled trial, so we believe it carries the most weight.

We read these three bodies as one finding: the gains are real only where verification is cheap.

The three bodies share one operational form: when verification costs more than doing the work yourself, the net return goes below zero. That inequality — we call it the verification inequality — is the definition of the false-productivity trap, and it is our first step toward the map in the next section.

## Three paradigms, one map

Is the question still whether to use AI? Placed side by side, traditional research, the AI-assisted workflow, and AI4S turn out to be layers rather than rivals.

The traditional layer is human-led: problems come from advisors and taste, literature is bounded by personal reading, experiments run monthly, and verification rests on peer review and replication. Its bottleneck is human scale — nobody can read the literature, run the experiments, or staff the review system — but what it supplies is the verification bedrock for the other two layers. It is the layer we were all trained in, and the layer the other two still build on.

The AI-assisted workflow — the copilot and the orchestrator — takes over first-pass literature screening, boilerplate code, and the early exploration of hypothesis space, while humans retain problem definition and final verification. Its bottleneck is the verification inequality, with hallucination on top: it costs about as much to check an output as to produce it yourself, and the net return goes to zero.

The AI4S layer is an exploration engine: AI directly produces scientific knowledge and models — structure prediction, PDE solving, generative materials design — while humans move to goal-setting, constraint design, and interpretation. It has four bottlenecks: out-of-distribution failure, data scarcity, no guarantee of physical consistency, and an explainability gap that leaves understanding unclaimed.

The layers show convergence: AI4S models become standard tools inside workflows — AlphaFold in structural biology — and workflow agents begin driving AI4S pipelines, orchestrating machine-learned potentials for materials screening. For the individual researcher, convergence turns the question from whether to use AI into what to keep and what to outsource, at each layer.

One boundary sits on the map itself: the record we read centers on machine-learning research, biomedicine, and software engineering, so our map describes those disciplines best, and other disciplines are mostly unmeasured.

A map only matters if it changes what we do. Each strategy in the next section answers the same question: what to keep, and what to outsource.

## The training that still holds: six strategies

Six concrete strategies follow when we read the craft essay against the record. We state each in operational terms, and each rests on a finding this essay has already named. All six are disciplines for us to keep, not tasks to outsource. What we keep for ourselves is the selection of the problem, the reading of the transcript, the writing of the first draft.

1) **Treat AI as a cheap hypothesis generator plus an expensive verification target, not an answer machine.** Hallucinated citations have passed human review at top venues, and AI search tools make errors on the majority of citation queries. The verification budget for any citation, number, or proof step that AI produced is non-negotiable on our reading: when the verification inequality flips, do not use AI for it at all.

2) **Maintain an AI-free baseline, and put AI-free training on the schedule.** The endoscopists' drop in detection rate and the GPT students' exam reversal both mean that outsourced capability atrophies — and the atrophy likely shows only on the day the AI is unavailable. Train the key skills periodically — reading original papers, writing proofs, core code — without AI; when we train taste, we commit to a prediction of our own before looking at what the model produced.

3) **Use AI to compress the mechanical parts of the loop, and spend every saved hour staring at outputs.** AI best takes over first-pass literature screening, formatting, and initial failure-case clustering. What should never be outsourced is problem selection, transcript close-reading, baseline tuning, and the ablation analysis that reveals which component actually carries the result. That is precisely where, per the craft essay, most experimental information goes to die unread.

4) **Stay alert to shared models, shared ideas.** The contraction of research topics is the macro evidence, and the craft essay's information-diet claim is the micro mechanism. Deliberately read what AI does not recommend to you — old literature, neighboring disciplines, appendices no model has summarized. Use AI on your problems, and do not move to problems AI might be good at.

5) **Build disclosure and auditing in from the first day.** ICMJE, APA, and the major publishers have disclosure policies in place, and low compliance rates mean retroactive scrutiny is accumulating. Keep a log of AI use — which stage, which model, what human verification was applied — because this is compliance, and it is also how future-you reproduces present-you.

6) **Treat writing and public output as assets that appreciate, not assets that depreciate.** When everyone can produce fluent text, the unfakeable sample of thought — experiment logs, failure analyses, dated predictions — becomes the scarcest credential. AI can help you write faster, but the power of writing to expose gaps in our thinking fires only when we write the first draft ourselves. Write first; then let AI edit.

Six strategies answer the third question we set. What remains is to say what they add up to: what compounds, what does not, and what the record does not answer.

## Closing: what still compounds

Hamming asked his Bell Labs colleagues why they were not working on the important problems. Four decades later, a long-form essay brought the same question to a new generation of researchers, and thirty thousand of them bookmarked it. The question has not changed; the answer has.

What still compounds when generation becomes free? The new evidence is a footnote to Hamming's question: what problems you choose, how you judge outputs, and whether your work survives verification are the few research assets still compounding. That is the one-sentence answer; three conclusions follow, each with its boundary.

1) The craft essay holds because its emphasis was judgment-side all through: in the record we read, generation-side skills depreciate while judgment-side skills appreciate, and most of its pages were already on the latter.

2) The era's biggest danger is the false-productivity trap: the best controlled study puts the gap between perception and measurement at approximately forty points, and the verification inequality shows what the gains are worth.

3) Trainability has not changed, but the training environment has. Judgment is still a muscle, yet every exercise now comes with an assistant offering to lift the weight, so the discipline has to include refusing the lift on a schedule.

We leave three questions open, rather than smoothing them into the conclusion, because the record we read does not answer them.

- Deskilling has been measured in one medical specialty and one classroom setting; whether it generalizes across research disciplines is unknown.

- The contraction of the collective frontier rests on a single study; whether it is a durable trend or an adoption-phase artifact remains to be seen.

- The detection estimates of AI use in writing and review come with wide error bars, so the real scale remains unclear.

We hold our own claims to the same standard: each carries its source, and each conclusion carries its boundary.

The craft essay is right that these abilities are muscles, not gifts. What it does not say is that in the age of AI, training these muscles has become harder — because next to every exercise stands an assistant offering to lift the weight for you.

Accept its help. Do not let it do your reps.

---

## Sources

Most links below are also in the body above.

- The craft essay itself (community): [vivek: how to be good at research (X long-form, June 2026)](https://x.com/itsreallyvivek/article/2064686372737454155).
- Survey (industry): [Wiley ExplanAItions 2025](https://newsroom.wiley.com/press-releases/press-release-details/2025/AI-Adoption-Jumps-to-84-Among-Researchers-as-Expectations-Undergo-Significant-Reality-Check/default.aspx).
- Randomized controlled trial (preprint): [METR, July 2025](https://arxiv.org/pdf/2507.09089).
- Peer-reviewed field study: [Budzyń and colleagues (The Lancet Gastroenterology & Hepatology 2025)](https://www.thelancet.com/journals/langas/article/PIIS2468-12532500133-5/abstract).
- Peer-reviewed corpus forensics: [Kobak and colleagues (Science Advances 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219543/).
- Corpus analysis (preprint): [Hallucinated citations in NeurIPS 2025 accepted papers](https://arxiv.org/abs/2602.05930).
- Peer-reviewed (study summary): [Hao, Xu, Li and Evans (Nature 2026)](https://datascience.uchicago.edu/insights/new-research-shows-how-ai-tools-are-expanding-individual-capabilities-while-contracting-scientific-attention/).
- Journalism: [CJR/Tow Center](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php).
- Technical report (preprint): [Google AI co-scientist](https://arxiv.org/abs/2502.18864).
- Corporate research announcement: [FutureHouse's Robin](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system).
- Journalism (correction): [The A-Lab correction (C&EN, 2026)](https://cen.acs.org/research-integrity/Nature-robot-chemist-paper-corrected/104/web/2026/01).
- Journalism: [The Toner-Rodgers paper, disavowed by MIT (TechCrunch, May 2025)](https://techcrunch.com/2025/05/17/mit-disavows-doctoral-students-paper-on-ai-productivity-benefits/).
- Reference report: [Stanford HAI: 2026 AI Index Report](https://hai.stanford.edu/ai-index/2026-ai-index-report).

---

*Kezhongke (壳中客) is a nonprofit research community. If you are training judgment-side skills in your own research practice, or read the evidence cited here differently, we would like to hear from you.*

<!--
self-check（2026-09-14，写作方超时后由主流程独立复跑补记；python3 profiler.py 实测）：
- 篇幅 3,520 ✓ [2,100–3,750]；句长 20.4 ✓ [20–24]；P90 32 ✓ ≤35；段长 43.4 ✓ [33–53]
- 数密 18.5 ✓ [8–21]；hedge 9.94 ✓ [8–13.5]；克制比 4.99:1 ✓ 贴上沿；人称 47 ✓ [21–69]
- 客观自指 2 ✓；设问 3 ✓；MATTR 0.700 ✓ [0.66–0.70]；感叹号 0 ✓
- 超 35 词句子：0（原始切句下 5 处超长均为格式伪影：frontmatter/斜体署名行尾点号/加粗引导句合并）
- 自我检讨语气扫描（should have / embarrassingly / we failed / regret）：0 命中
- 体裁路由：博客体/行业分析取向（规则层 genre_guess 对英文稿返回 blog_or_exploration 系中文关键词口径空档，以人工路由为准）
-->
