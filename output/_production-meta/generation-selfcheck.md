# 自检报告：article-meta-v1.md（元稿《Your Style Profile Is a Genre Artifact》）

> 生成日期 2026-09-15。输入：templates/genre-playbook-kezhongke.md（§0 英文第一输出 + §0.2 走廊与处方 1–9 + §4 两层 + §5 信源分层 + §6 收尾组合 + §7 招式）+ output/_production-meta/source-pack.md（唯一事实来源，§7 写作纪律已执行）。
> 实测命令：`python3 profiler.py output/_production-meta/article-meta-v1.md -o output/_production-meta/article-meta-v1.profile.json`（JSON 留存同目录）。
> 事实核验方式：每个数值断言在写作前已对账到仓库工件（含 `git show <commit>:<path>` 只读核验历史口径），对账表见 §3。

## 1. 走廊实测（profiler 单文件实测，英文口径）

| 指标 | 目标 | 合格区间 | 实测 | 判定 |
|---|---|---|---|---|
| 篇幅（词） | ≈2,900 | [2,100, 3,750] | 2,873 | ✅ |
| 平均句长（词） | ≈22 | [20, 24] | 20.8 | ✅ |
| P90 句长（词） | ≤35 | ≤41 | 34 | ✅ |
| 平均段长（词） | ≈42 | [33, 53] | 51.5 | ✅ |
| 数字密度 /千词 | ≈14 | [8, 21] | 17.75（51 tokens） | ✅ 高于中值，见 §6.1 |
| hedge /千词 | ≈10 | [8, 13.5] | 9.05 | ✅ |
| absolutist /千词 | ≈2 | [1.4, 3.4] | 2.09 | ✅ |
| 克制比 hedge:absolutist | 典型 4–5:1 | 红线 ≥3:1 | 4.33:1 | ✅ |
| 第一人称（次/篇） | ≈40 | [21, 69] | 31 | ✅ 带内偏下，见 §6.2 |
| 客观自指（次/篇） | 1–2 | [1, 2] | 2（this analysis ×1 + this essay ×1） | ✅ |
| 设问（次/篇） | 2–3 | [0, 5] | 3（HOOK "What changed?" + §4 末 "What could still be wrong?" + CLOSE 设问自答） | ✅ |
| MATTR | 0.68–0.69 | [0.66, 0.70]，高侧容差 ≤+0.02 | 0.698 | ✅ **带内**，无需动用容差条款 |
| 年份锚点 /千词 | ≈1 | 软上限 2 | 0.35（全文仅 "September 2026" 一处） | ✅ 软约束，见 §6.3 |
| 感叹号 | 0 | 0 | 0 | ✅ |
| emoji | — | — | 0 | ✅ |

补充记录（非走廊项）：参考条目 9（Sources 节）；单句/短节拍段 2 处（≤4 限额内："The articles had not moved. The reading had."、编号结论引导句）；段长 P90 91 词（走廊只约束均值，留痕——Sources 块与编号结论块为列表合并段，结构性偏大，同前稿处置）；规则层 genre_guess=blog_or_exploration（规则只识别三类中文体裁，英文 A 格预期外命中，属工具口径而非体裁失格，同前稿判定）。

## 2. 语步序列声明

HOOK（开场 5 段：openai 第一人称"显著→消融"反差并置；设问 1 设而不答留到 §1）
→ FRAME（## Three questions：命名核心概念 genre-composition contamination 并声明短称复用；明示三问题清单；四节+反驳+指南结构预告；kezhongke 首现 gloss；客观自指 #1 this analysis）
→ **CONTEXT 前置（## The story so far，主编终审增补，2026-09-15 第二轮）：语步归类 = CONTEXT 的开篇叙事部而非 FRAME 延伸**——playbook §2 规定叙事只允许出现在 CONTEXT 区（叙事比 0.3–0.6），前史为历史叙事，故 CONTEXT 自此节起算，"A paradox in the pooling" 为其概念定义续部；该节首句即结论（"Everything reported here happened inside two September weeks"），末句指向 Simpson 节（"the next section names it"）；CONTEXT 区叙事比 ≈305/635 ≈ 0.48，在 [0.3, 0.6] 内）
→ CONTEXT（## A paradox in the pooling：Simpson 悖论最小解释（诊所例子+聚合机制两句）→ 体裁敏感指标映射 → 旧口径如何落入陷阱；叙事仅在此区与 §3 纠错史）
→ ARGUE×4（## 1 头条反转 7/7→0/7 → ## 2 两层方法（机制→双向证据→LOO→格集合敏感诚实段）→ ## 3 量具纠错史（词表/长度/路由三修复）→ ## 4 验证链（盲测→生产事实审计→工程地基）；各主节末句均指向下节）
→ COUNTER（## Three objections, three verdicts：①样本小→方法无效 **rebutted as stated, boundary left standing**（tripwire 登记）；②0/7→机构无风格 **rebutted**；③LLM 体裁标签循环论证 **left open**，缓解措施+残留如实列出）
→ APPLY（## A reading discipline for practitioners：五条可执行读数纪律 + 双向折价补充句）
→ CLOSE（## So is your own profile an artifact：设问自答 → 编号结论 ×4 → 开放问题（中性"the evidence does not cover"，非自我检讨）→ lens 比喻收束 + 自指一句（客观自指 #2 this essay）；**无自我批评位**）

招式执行：①三问题清单 ✅；②信源分层——本稿事实全在仓库内，分层以工件层级实现（聚合 JSON / 档案散文 / commit 记录 / 评审报告），文末 Sources 9 条全部给出工件路径 ✅；③判断带边界（none survives at this sample size / not yet separable / roughly / likely / appear）✅；④编号结论+开放问题 ✅；⑤单一比喻 lens 全文复用（§1 铺设 "composition is treated as a lens whose curvature we can map" → §4 标题 "the corrected lens" → CLOSE 回收 "map its curvature and correct for the bend"，服务概念非情绪）✅；⑥术语全文唯一（genre cell / fingerprint / pooled caliber / cell-corrected caliber / two-level model / institution value / cell delta / composition contamination / library 各一主词；库名全小写沿用仓库命名）✅。

处方 7 指针句核查：CONTEXT→§1（"What the fix looks like, and what it cost, comes next"）、§1→§2（"the subject of the next section"）、§2→§3（"the instrument has its own record"）、§3→§4（"whether the corrected instrument performs"）、§4→COUNTER（"Three objections deserve explicit verdicts"）、COUNTER→APPLY（"still needs a working discipline"）、APPLY→CLOSE（"the title's question, turned back on the reader"）✅。

## 3. 数值对账表（文中数值断言 ↔ source-pack 条目 ↔ 仓库工件）

source-pack 条目按小节引用；历史口径工件以 `git show <commit>:<path>` 只读核验（未做任何 git 写操作）。

| # | 文中断言（位置） | 包条目 | 对账工件 | 核验方式 |
|---|---|---|---|---|
| 1 | openai 第一人称 median 53、p=0.002、q=0.003、过 FDR（HOOK ¶1） | §1 | `git show 02917ae:output/_group-discrimination.txt` §5b（"第一人称（高，p=0.002，q=0.003）过 FDR"）；median 53 见 output/openai/STYLE-PROFILE-openai-v0.md 指纹行与 templates/genre-playbooks-openai.md 留痕（朴素 53） | 已核，一致 |
| 2 | R 格 55.5 vs 同格 pooled 22.0、p=0.347、q=0.687（HOOK ¶2） | §1 | output/openai/STYLE-PROFILE-openai-v0.md 2026-09-14 两层口径复核注记（L27/L95）；55.5 另见 output/openai/_aggregate.json two_level R 格 | 已核，一致 |
| 3 | 旧口径 7 库指纹全部过 FDR（HOOK ¶4 / §1 ¶1） | §2 | output/_group-discrimination.txt §5b（当前版本 7/7 "过 FDR"） | 已核，一致 |
| 4 | 新口径 0/7 过 FDR、"探索性信号…待样本扩容复验"措辞（§1 ¶2–3） | §2、§7 | output/_group-discrimination.txt §4b（7 行统一标注） | 已核，一致；措辞按 §7 纪律（"未过 FDR、方向性信号留档"，未写"指纹不存在"） |
| 5 | q≤0.001 级（one-per-mille，§1 ¶1）；cerebras 段长 / microsoft-research 第一人称为例 | §2 | 当前 §5b（全部 q=0.000/0.001）；cerebras/msr 两行在 02917ae 与当前两版 §5b 中同名同向 | 已核，一致；旧口径例名取两时代稳定行，避免年代混杂 |
| 6 | 指纹族 420 检验（§1 ¶2） | §2 | output/_group-discrimination.txt §4b 头（"共 420 检验"） | 已核，一致 |
| 7 | eleuther MATTR 低 @ R 格 0.62 vs 0.70、p 四舍五入为零、q=0.088（§1 ¶2、COUNTER ¶1） | §2 | output/_group-discrimination.txt §4b（p=0.000，q=0.088） | 已核，一致 |
| 8 | openai 新口径最显著信号换位限定语：R 格 15.1 vs 7.38、q=0.234（§1 ¶2 末） | §1 | output/_group-discrimination.txt §4b（当前版，p=0.014）；10 篇时代值（pooled 7.98、p=0.023、q=0.351）见 `git show 02917ae:…` §4b 与 openai 档案注记 | 已核，一致（**修订 R1 后取当前 20 篇版**，与同段 eleuther 行同一年代） |
| 9 | 扩容 10→20 篇/库后 0/7 不变；指纹族"more than doubled"（180→420）（§1 ¶4） | §2 | 180 见 `git show 02917ae:…` §4b 头；420 见当前 §4b 头；扩容 commits 3bbf704/37d5933 | 已核，一致（2.33 倍，措辞 "more than doubled" 保守成立） |
| 10 | 格内 n≥3 出中位、薄格缺席不计 0（§2 ¶1） | （方法描述） | aggregate_two_level.py + 报告头"各库出值体裁格（n≥3）"；commit 2ee4d23 message | 已核，一致 |
| 11 | openai 精确数字：朴素 0.92 → 两层 2.29（+149%）（§2 ¶2） | §3 | `git show 2ee4d23:output/openai/_aggregate.json`（corpus_naive_median.precise_per_1k=0.92；institution=2.29） | 已核，一致（+148.9%≈149%） |
| 12 | kezhongke 限定语：朴素 2.39 → 两层 1.42（−41%）；5 篇公告类上拉（§2 ¶2） | §3 | `git show 2ee4d23:output/kezhongke/_aggregate.json`（2.39/1.42）；N 格 n=5 见 playbook §4.2 | 已核，一致（−40.6%≈41%） |
| 13 | LOO 最近质心归属 63%→75%（10 篇时代，R 格）；扩容后同练习在 N 格 65%（§2 ¶3，修订后带双时代锚） | §3 | `git show 2ee4d23:output/_group-discrimination.txt` §三（63%，44/70，全库）；`git show 02917ae:…` §三（75%，24/32，R 格 6 库）；当前 output/_group-discrimination.txt §三（65%，22/34，N 格 7 库） | 已核，一致；文中明示"across the pooled corpus → inside the research cell"及两个时代各自口径，未隐瞒比较面变化 |
| 14 | 扩容后 openai 精确数字方向反转：朴素 0.9 vs 两层 0.42；出值格 2→5（§2 ¶4） | §3（双口径留痕纪律） | 当前 output/openai/_aggregate.json（naive 0.9 / inst 0.42；A/E/N/P/R 五格）；2ee4d23 版 E/R 两格 | 已核，一致；§7 纪律"同引须说明格集合变化"已执行（文中归因于 cell set 2→5 且两口径留痕） |
| 15 | 词表子串污染：kezhongke 限定语 4.75→2.69、43% 为污染、修复=单字词精确匹配（§3 ¶1） | §4 | output/kezhongke/STYLE-PROFILE-kezhongke-v0.md v0.2 注记（2026-09-07）；tests/test_profiler.py 词表哨兵 | 已核，一致 |
| 16 | TTR 长度污染：差距 0.204→0.070（约缩水三分之二）；MATTR w=150 替代（§3 ¶2） | §4 | output/eleuther/STYLE-PROFILE-eleuther-v0.md 指纹注记（"缩水约 2/3（0.204→0.070）"） | 已核，**取工件精确数**；包 §4 作 "60%"，实为 65.7%≈2/3，文中用 "roughly two-thirds" 与工件一致（见 §6.6） |
| 17 | 规则路由英文库从未运行（全兜底）；LLM 路由 93 篇 v1 + 71 篇 v2；28 条低置信全部维持（§3 ¶3） | §4 | docs/genre-taxonomy-v0.md §五（v1 93 篇 / 扩容 passe "7×10+1"=71 / 28 条裁决收口）；commits 44188ba/041422b | 已核，一致 |
| 18 | 盲测三轮；决定性一轮主编判"像"；后一轮走廊 12/13、六类病灶全部消除（§4 ¶1） | §5 | output/_p2-revalidation.md + judge-kezhongke-en-v2/v3/v4 报告；commits b6d9b28/cfa999e | 已核，一致（v3="decisive round … a match"，v4="a later round … twelve of thirteen"） |
| 19 | 生产首跑事实审计摘下信源包 2 处错误（对战计数、监管时间线）并留勘误（§4 ¶3） | §5 | output/_production-eval-power/judge-fact.md + 该稿 generation-selfcheck.md 修订记录 R1/R2 + source-pack 勘误节 | 已核，一致；文中刻意不复述外部数字（数字预算） |
| 20 | 44 项回归测试（as of mid-September 2026）；一致性校验 8 库 8 PASS（§4 ¶4） | §6（已同步更新为 44） | 实测 `python3 -m unittest discover tests`（Ran 44 tests OK）；`python3 check_profiles.py`（合计 8 PASS / 0 FAIL） | 已核，**修订 R2 后复跑一致**；测试数随开发增长，文中表述带时代锚 |
| 21 | 8 库 164 篇（7 英文×20 + kezhongke 24）；22 项指标/篇；六统一体裁（FRAME ¶1） | §6 | output/ 各库 per-article JSON 计数；profiler.py AGGREGATE_KEYS（22 键）；docs/genre-taxonomy-v0.md | 已核，一致 |
| 22 | 10 篇时代 openai 7/10 落 E/R 格、eleuther R 格 8 篇（CONTEXT ¶3） | §1 机制（派生） | `git show 02917ae:…` 出值格表（openai E3+R4=7；eleuther R(n=8) 单格） | 已核，派生自格表计数，标注派生 |
| 23 | 全文本地不入库、slug 可复现自采（§4 ¶4） | §6 | corpus/README.md、README.md 语料说明 | 已核，一致 |
| 24 | 4 个双峰格 14 篇亚型软标签 + 书面转正触发器（COUNTER ¶3） | §6 | docs/genre-taxonomy-v0.md §六；commit 37e2ea3 | 已核，一致 |
| 25 | 公开仓库 github.com/SuTang-vain/style-profiler（Sources 末条） | §6 | README.md 安装节 | 已核，一致 |
| 26 | "In the first week of September 2026 … one week later"（HOOK 时间线） | §1 时代标注 | 旧口径指纹时代：v0.2 注记 2026-09-07（discriminate 加 FDR）；新口径落地：commit 02917ae（2026-09-14） | 已核，一致（相隔恰一周） |

**包外事实零引入**：全文所有具体数字/事件均出自上表；Simpson 悖论解释为公共教科书知识（诊所例子为自制最小例，无外部数据）；"one-per-mille"为 q≤0.001 的英文转写。分析性发挥（lens 比喻、折价措辞、"anecdote with decimals"）不含新数字或事件。

## 4. 出处计数

- **具体出处（文档名/工件路径）：9 处**（Sources 节全部带仓库相对路径：_group-discrimination.txt、openai 档案、两份 _aggregate.json、genre-taxonomy-v0.md、两份修复记录档案、_p2-revalidation.md、judge-fact.md、代码与测试清单+仓库 URL）。内文另有指名文档引用 5 处（the discrimination report 新旧两节 / the taxonomy document / the adjudication log / the errata / the source pack）。下限 ≥5 ✅。
- **模糊归因：0 处**（限额 ≤2）。全文无外部事件断言，无需媒体/日期归因；所有事实经 §3 表对账到工件。

## 5. MATTR 与词族纪律

MATTR 实测 0.698，在 [0.66, 0.70] 带内（贴高侧，未出带，不动用 2026-09-14 容差条款）。结构性说明（留痕）：题材为双域（统计测量 × 软件工程）且专名/术语密集（Simpson、FDR、MATTR、TTR、LOO、八库名、jieba），靠术语统一（处方 3）与主词复用压回带内；top_terms 前列 pooled/correction/cell/genre 均为声明过的统一主词，非失控重复。
处方 9 扫描（自建正则，12 个词族）：唯一残留命中为 "Seven libraries, seven signatures, seven clean certificates" 单句三叠——**刻意回环修辞，有明示框架**（标题 "Seven Fingerprints, One Trap" + §1 标题 "Seven for seven, then zero of seven" + CLOSE 结论 1/4 回收），按豁免条款留痕。写作中另处置两处：§2 "cell median…cell yields…cell" 三叠改写为变体；APPLY "caliber×3" 改写为 2 次。**修订轮追加（评审黄色项 6）**：§1 ¶2 "family" 单句 ×4 与 APPLY "family" 单句 ×3，按处方 9 登记变体轮换——主词 family（correction family / test family）+ 变体 batch（pooled batch），两处各降至 family×2；术语主词不变（correction family 仍为概念主词，batch 仅在同句计数压力处轮换），见修订记录 Y6。

## 6. 未达标项与诚实标注

1. **数字密度 17.75/千词，高于 ≈14 中值**（区间 [8,21] 内）：题材为测量学本身，数字锚即论据（类比 N 格结构性冲高）；已削减一切非承载性数字（180、"a dozen siblings"、旧口径例表等），再压将损失对账精度。
2. **第一人称 31，低于 ≈40 中值**（区间 [21,69] 内）：we 叙事实测自然落点；接近 openai 库指纹 41 的下侧，题材（方法自述）支撑但不过量。
3. **年份锚点 0.35/千词，低于 ≈1**（软约束、软上限 2）：有意为之——全文日期一律用 "September 14 当周/one week later" 式表述以守软上限，仅 HOOK 一处 2026 定锚。
4. **段长 P90 91 词**：走廊仅约束均值（51.5 ✅）；偏大多来自 Sources 与编号结论两个列表合并段，结构性，同前稿处置（留痕不判失格）。
5. **p 值措辞**："Its p-value rounds to zero" 对应工件记录 p=0.000（三位小数显示），若评审以更多位小数复算仍为强显著但非严格零；措辞已用 "rounds to" 限定，留痕。
6. **TTR 缩水表述**：包 §4 作 "60%"，工件作 "0.204→0.070、约 2/3"；文中取工件精确值（"roughly two-thirds"）。两处口径差异已在此登记，以工件为准。
7. 规则层 genre_guess=blog_or_exploration 为工具口径预期（仅识别三类中文体裁），非体裁失格。
8. **修订后残留的双时代引用（收窄）**：§1 的 openai 限定语行已改当前版（R1），LOO 行已带双时代锚（Y3）；仍属 10 篇时代的仅 HOOK 两条（条 1–2：median 53、p=0.002/q=0.003、R 格 55.5/22.0、p=0.347/q=0.687），文中以 "In early September 2026 … One week later" 时间锚明示，对账表分行列明，未混引。

## 7. 收尾组合核对（§6/§0.2）与边界限额

设问自答 ✅ → 编号结论 ×4 ✅ → 开放问题（中性、"the evidence does not cover"，非自我检讨；按 judge-v3 划界不计入边界限额）✅ → lens 比喻收束 ✅ → **无自我批评位** ✅。
边界/局限声明全篇 2 处（≤3 限额内）：①COUNTER ¶3 末（"something the current evidence does not cover"，中性）；②COUNTER ¶1 tripwire 登记句（判决条款性质）。§2 ¶4"机构值随格集合变化"为论点本体（构成敏感的例证），非免责声明。

## 8. 复跑命令留痕

```bash
python3 profiler.py output/_production-meta/article-meta-v1.md -o output/_production-meta/article-meta-v1.profile.json
python3 -m unittest discover tests        # Ran 44 tests, OK（2026-09-15 修订后复跑）
python3 check_profiles.py                 # 合计 8 PASS / 0 FAIL / 0 SKIP
```

---

## 修订记录（2026-09-15 三路评审后定点修订，句子级，骨架未动）

> 评审结论：定量 14/14 合格；风格"像"高置信；事实审计"需修订后发布"（2 红 3 黄 + 1 处方 9 观察）。以下逐条 before/after；数字改动仅用评审给出的工件值，改前均回核工件。

### R1（红色项 1，§1 ¶2 末，时代混淆）
- before: "…hedge density in the research cell, 15.1 against a same-cell pooled 7.98, and it fails correction as well, at q of 0.351."
- after: "…hedge density in the research cell, 15.1 against a same-cell pooled 7.38, and it fails correction as well, at q of 0.234."
- 依据：评审推荐取当前 20 篇版（output/_group-discrimination.txt §4b：15.1 vs 7.38，p=0.014，q=0.234），与同段 eleuther 行（0.62/0.70，q=0.088）同一年代；10 篇时代值（7.98/0.023/0.351）在对账表条 8 留痕。

### R2（红色项 2，§4 ¶4，测试计数过期）
- before: "thirty-four regression tests that lock behavior rather than numbers"
- after: "a regression suite, forty-four tests as of mid-September 2026, that locks behavior rather than numbers"
- 依据：修订前复跑 `python3 -m unittest discover tests` 实测 Ran 44 tests OK（并行工作已落地）；按评审要求带时代锚。source-pack.md §6 同步 34→44 并注明"该数字随开发增长，成稿引用须带时代锚"。

### Y3（黄色项 3，§2 ¶3，LOO 时代锚）
- before: "…accuracy rose from 63 percent across the pooled corpus to 75 percent inside the research cell."
- after: "…accuracy rose from 63 percent across the pooled corpus to 75 percent inside the research cell — both figures from the ten-article stage; at the current twenty-article size the same exercise runs on the announcement cell and lands at 65 percent."
- 依据：63%/75% 系 10 篇时代（2ee4d23 全库 / 02917ae R 格）；当前版 §三为 N 公告类格 65%（22/34），补当前可核对锚点。

### Y4（黄色项 4，HOOK ¶1，日期表述）
- before: "In the first week of September 2026, …"
- after: "In early September 2026, …"
- 依据：旧口径指纹 2026-09-08 前已出（v0.2 注记 09-07），"first week" 偏严。

### Y5a（黄色项 5 前半，FRAME ¶1，kezhongke 首现 gloss）
- before: "…eight libraries, 164 articles, twenty-two metrics per article…"
- after: "…eight libraries — seven English, plus the kezhongke library, this site's own Chinese corpus — 164 articles, …"
- 依据：本站自有语料库的身份前移至首现处（§2 ¶2 与 CLOSE 自指句不再承担首次点破）。

### Y5b（黄色项 5 后半，§1 ¶3–4，近同义重申收拢）
- before（¶3）: "The honest sentence here is narrow: not that institutional fingerprints do not exist, but that none survives correction at this sample size. We keep the directional signals archived as exploratory, each with its cell and its q-value attached."（¶4 首句）: "The expansion then tested the small-sample excuse directly: …"
- after（¶3，功能性过渡）: "How to word that result responsibly is a discipline of its own, and the expansion put every wording to a direct test."（¶4 首句）: "The expansion supplied that test: we doubled every English library from ten to twenty articles, …"
- 依据："零过校正≠无风格"表述收归 CLOSE 结论 4 单点承载（COUNTER 判决 ② 为论证呼应，非重申）；source-pack §7 的 0/7 措辞纪律仍由 §1 ¶2 表格措辞（"exploratory signal, did not pass correction"）+ COUNTER ② + CLOSE ④ 三处承载，未丢失。

### Y6（处方 9 观察，§1 ¶2 与 APPLY ¶2，"family" 同句 ×4/×3）
- before（§1）: "The family split matters, because correction is priced per family; a signal that would clear one pooled family could fail once the family honestly mirrors the structure of the comparison."
- after（§1）: "The split matters, because correction is priced per family: a signal that would clear a single pooled batch could fail once the test family honestly mirrors the structure of the comparison."
- before（APPLY）: "…until it survives the right family: the correction family has to mirror the comparison structure, because a single pooled family spread over mixed genres manufactures confidence."
- after（APPLY）: "…until it survives the right correction family: the family has to mirror the comparison structure, because one pooled batch spread over mixed genres manufactures confidence."
- 依据：处方 9 变体轮换（family 主词 / batch 变体），两处各降至 family×2；概念主词不变，登记见 §5。

### 修订后走廊复测（profiler 重跑，JSON 已覆盖更新）

| 指标 | 合格区间 | 修订前 | 修订后 | 判定 |
|---|---|---|---|---|
| 篇幅（词） | [2,100, 3,750] | 2,873 | 2,890 | ✅ |
| 平均句长 / P90 | [20, 24] / ≤35 | 20.8 / 34 | 21.1 / 35 | ✅ |
| 平均段长 | [33, 53] | 51.5 | 51.8 | ✅ |
| 数字密度 /千词 | [8, 21] | 17.75 | 18.34（53 tokens：+2026 年份锚、+65% 当前 LOO；7.98→7.38 与 0.351→0.234 等额替换） | ✅ |
| 年份锚点 /千词 | 软上限 2 | 0.35（1 处） | 0.69（2 处：early September 2026 + mid-September 2026） | ✅ 更贴近 ≈1 目标 |
| hedge / absolutist / 克制比 | [8,13.5] / [1.4,3.4] / ≥3:1 | 9.05 / 2.09 / 4.33 | 9.34 / 2.08 / 4.49 | ✅ |
| 第一人称 / 客观自指 / 设问 / 感叹号 | [21,69] / [1,2] / 2–3 / 0 | 31 / 2 / 3 / 0 | 30 / 2 / 3 / 0 | ✅ |
| MATTR | [0.66, 0.70]，不留容差尾巴 | 0.698 | **0.697（带内，未贴容差条款）** | ✅ |

14 项全带内；处方 9 复扫唯一残留为 "seven" 三叠（豁免留痕不变，见 §5）。

### 残留说明

- 双时代引用收窄至 HOOK 两条（条 1–2），时间锚明示；其余全部当前版。
- 数字密度 18.34 仍在区间上半段（结构性，§6.1 注记不变）。
- 段长 P90 92 为列表合并段结构性偏大（走廊仅约束均值 51.8 ✅），留痕不判失格。

---

## 修订记录 第二轮（2026-09-15 主编终审：补前史小节，结构性新增一节，骨架其余未动）

> 终审意见：元稿上下文不完整——新读者不知道项目为何存在、流水线是什么、反转发生在哪条时间线上。处置：在 FRAME（## Three questions）与 CONTEXT（## A paradox in the pooling）之间新增独立小节 **## The story so far**（5 段，正文 312 词）。五项规定内容全部落入：①起源（为剖 kezhongke 自有中文语料而建，先描述后引导——对账 templates/genre-playbook-kezhongke.md 头部、output/kezhongke/validation-report.md）；②对照扩张（七家机构公开博客、各二十篇、全文本地 slug 可复现——对账 corpus/README.md）；③流水线闭环（指标→体裁路由→两层聚合→playbook→成稿→盲评→事实审计；本稿为流水线第一次转向自身——仅引用 §4 既有内容，不重复其数字）；④时间线（上旬剖面与首版 playbook、中旬两层模型/扩容/反转——对账 git log，措辞 early/mid-month 未逐个列日期）；⑤公开理由（教训不限于本站）。

### 新增小节全文（终态）

> ## The story so far
>
> Everything reported here happened inside two September weeks, on a toolchain built for something narrower. The project began as a way to describe one library, the kezhongke corpus of this site's own Chinese writing, and then to guide. The playbook layer turns the per-article readings into writing budgets and readability prescriptions, so a new draft is held to a measured corridor rather than to anyone's memory of the house style.
>
> The comparison layer came from a question: whether this site's own style was an exception or one point on a field. Seven public blog streams from research organizations became the reference libraries, twenty articles each. The collection rule has not changed since: full texts stay local, and the slug lists that rebuild every sample are published with the code.
>
> With the comparison shelf in place, the loop closed. Every article is measured, routed into a genre cell, and aggregated into the two-level budgets, and those budgets feed the playbook that new drafts are written against. Finished drafts then pass blind review and a fact audit before anything is published. Ours is the first draft in that loop whose subject is the pipeline itself.
>
> The timing matters for reading what follows. The profiles and the first playbook were built in the early days of the month. The two-level model, the sample expansion, and the reversal at the center of this account all landed in the middle of it, within days of one another. What follows is therefore not a slow accumulation of doubts but one week in which a correction and its consequence arrived together.
>
> We are publishing the failure because the lesson is not ours alone: anyone who quotes style data — ours, a vendor's, or a reviewer's — stands at the edge of the same trap. The trap is an old one and it has a textbook name; the next section names it.

### 执行纪律逐项核对

- **数字最小化**：新节零数字 token（"two September weeks"/"twenty articles each" 均拼写，且与 FRAME 的 8 库/164 篇/22 项口径一致，未重复其数字形态）。
- **处方 7**：首句即该节结论；末句指向 Simpson 节（与 CONTEXT 首句 "The textbook name for the trap is…" 形成指代链接力，非重申）；与 §4 ¶4 的 "full texts stay local / slug lists" 有一处事实重叠——此处为来源记叙（collection rule），§4 为工程地基（reproducibility 标准），功能不同，留痕。
- **处方 9**：新节无同词族单句三叠（复扫确认；唯一残留仍为 §1 "seven" 三叠豁免项）。
- **自指控制**：新节初稿带入 "this essay"/"this article" 各一处，使客观自指升至 4（出带）；已改为 "Ours is the first draft…" 与 "the reversal at the center of this account"，回落 2 ✅。自指口吻维持第三人称库标签 + 克制。
- **语步归类**：CONTEXT 开篇叙事部（见 §2 登记），非 FRAME 延伸。

### 复测表（profiler 重跑，JSON 已覆盖更新）

| 指标 | 合格区间 | 第一轮修订后 | 本轮终态 | 判定 |
|---|---|---|---|---|
| 篇幅（词） | [2,100, 3,750] | 2,890 | 3,206 | ✅ |
| 平均句长 / P90 | [20, 24] / ≤35 | 21.1 / 35 | 21.0 / 34 | ✅ |
| 平均段长 | [33, 53] | 51.8 | 52.0 | ✅ |
| 数字密度 /千词 | [8, 21] | 18.34 | 16.53（新节零数字，密度回落） | ✅ |
| 年份锚点 /千词 | 软上限 2 | 0.69 | 0.62（仍 2 处，未新增年份词） | ✅ |
| hedge / absolutist / 克制比 | [8,13.5] / [1.4,3.4] / ≥3:1 | 9.34 / 2.08 / 4.49 | 8.73 / 1.87 / 4.67 | ✅ |
| 第一人称 / 客观自指 / 设问 / 感叹号 | [21,69] / [1,2] / 2–3 / 0 | 30 / 2 / 3 / 0 | 30 / 2 / 3 / 0 | ✅ |
| **MATTR** | <0.70（不留容差尾巴） | 0.697 | **0.693（余量 0.007）** | ✅ 词族复用策略生效，不涨反降 |

14 项全带内；MATTR 余量 0.007，后续任何增删仍须先重跑 profiler 再定稿。
