# 事实审计：article-meta-v1.md（项目自述生产稿）

- 审计员：独立事实审计环节（judge-fact）
- 审计日期：2026-09-15
- 审计模式：**仓库对账**（非外部检索）——每条数值/事件断言对账到本仓库工件或 git 历史。
- 事实基准：`output/_production-meta/source-pack.md`（批准事实清单）+ 仓库工件本身。
- 纪律遵守：未读取 `generation-selfcheck.md` / `article-meta-v1.profile.json`；未做任何 git 写操作（`git show` 只读）。
- 两个时代口径已区分：**A 时代** = commit 02917ae（2026-09-14，10 篇/库，消融事件发生点）；**B 时代** = 当前 HEAD（20 篇/库，扩容后）。

## 一、审计方法与工件清单

| 工件 | 用途 | 状态 |
|---|---|---|
| output/_group-discrimination.txt（当前） | §4b 指纹族（420 检验）、§5b 旧口径对照、§三 LOO | ✅ 全读 |
| `git show 02917ae:output/_group-discrimination.txt` | A 时代 §4b（180 检验）/§5b/LOO | ✅ |
| `git show 2ee4d23:output/_group-discrimination.txt` | 两层聚合引入时的旧口径 LOO 63% | ✅ |
| `git show 02917ae:output/openai/_aggregate.json`、`git show 2ee4d23:output/kezhongke/_aggregate.json` | A 时代 two_level（0.92/2.29、2.39/1.42、格集合） | ✅ |
| output/openai|kezhongke/_aggregate.json（当前） | B 时代 two_level（0.9/0.42、2.41/1.87、5 格） | ✅ |
| output/openai|eleuther|kezhongke/STYLE-PROFILE-*-v0.md | 指纹行双口径留痕、词表/TTR 修复日志 | ✅ |
| docs/genre-taxonomy-v0.md §四/§五/§六 | 路由 passe、28 条裁决、亚型软标签 | ✅ |
| output/_p2-revalidation.md、output/_p1-validation-samples/judge-kezhongke-en-v3.md | 盲测链 v2/v3/v4 | ✅ |
| output/_production-eval-power/judge-fact.md | 生产首跑事实审计两处红色项 | ✅ |
| tests/（`python3 -m unittest discover tests`）、check_profiles.py、profiler.py AGGREGATE_KEYS | 工程地基实测 | ✅ 实跑 |
| corpus/README.md | slug 可复现自采政策 | ✅ |

## 二、逐条断言判定

判定图例：✅ 对账一致 ｜ 🟡 一致但建议修订（时代标注/精度）｜ 🔴 与当前工件不符

| 行 | 成稿断言 | 对账结果 | 判定 |
|----|----------|----------|------|
| L3 | "first week of September 2026"；openai 第一人称指纹 median 53，p=0.002，q=0.003 过 FDR | 53.0/0.002/0.003 与 `02917ae §5b` 及 openai 档案指纹行逐字一致；旧指纹落地于 09-07（021b2d1/530adf3）~09-08 校准——"first week" 踩边界（见 Y2） | ✅（附 Y2） |
| L5 | "One week later"；R 格 55.5 vs pooled 22.0，p=0.347，q=0.687；"raw gap larger than the one we had pooled into significance" | 09-07/08 → 02917ae（09-14 17:06）恰一周 ✓；55.5/22.0/0.347/0.687 与 A 时代 openai 档案指纹行逐字一致 ✓；raw gap 复算：33.5 > 旧全库 gap 32.0（53−其余六库 60 篇 pooled median 21.0，逐篇复算）✓ | ✅ |
| L9 | 旧口径 7/7 过 FDR；新口径 0/7 | 两个时代 §5b 均 7/7 过、§4b 均 0/7 过 ✓ | ✅ |
| L15 | eight libraries, 164 articles, twenty-two metrics, six genre cells | 实点：7 英文库各 20 + kezhongke 24 = 164 ✓；AGGREGATE_KEYS=22 ✓；A/E/R/N/P/G ✓ | ✅ |
| L27 | 十篇时代 openai 10 篇中 7 篇在 E/R 格；eleuther 8 篇 R、"almost nothing else" | `02917ae` 报告头：openai E(n=3)+R(n=4)=7 ✓；eleuther 唯一出值格 R(n=8)/10 ✓；时代标注 "ten-article era" 明确 ✓ | ✅ |
| L33 | 旧指纹节 7 库全过 FDR，q ≤ 千分之一级；cerebras 段长、microsoft-research 第一人称 | 当前 §5b：六库 q=0.000 + openai q=0.001 ✓；cerebras 最显著=平均段长 ✓、msr=第一人称 ✓ | ✅ |
| L35 | 指纹族 = 库×共享格×指标，"420 tests at the current sample size" | 当前 §4b 头"共 420 检验" ✓，时代限定语在 ✓ | ✅ |
| L37 | eleuther 最近过线：MATTR 0.62 vs 0.70 @ R 格；"p-value rounds to zero"；q=0.088 | 当前 §4b 逐字一致（p=0.000 为显示精度，成稿 "rounds to zero" 措辞诚实）✓；q=0.088 确为七库最小 q ✓ | ✅ |
| L37 | **openai 最显著信号 = 限定语 @ R 格，"15.1 against a same-cell pooled 7.98 … q of 0.351"** | **时代混淆**：7.98/0.023/0.351 是 A 时代（10 篇）数字（`02917ae §4b`）；当前 §4b 与 openai 档案 2026-09-15 扩容复核行均为 **pooled 7.38、p=0.014、q=0.234**。同段 eleuther 数字用的是 B 时代口径，本句未标时代即以旧值充当前值（median 15.1 与"未过 FDR"结论两时代均成立） | 🔴 R1 |
| L39 | "not that institutional fingerprints do not exist, but that none survives correction at this sample size"，方向性信号留档 | 符合信源包 §7 纪律（0/7 不得写成"不存在"）✓ | ✅ |
| L41 | 英文库 10→20 翻倍；指纹族 "more than doubled"；结论不动，最近信号仍为 eleuther | 扩容 passe 每英文库 +10 ✓；指纹族 180→420 = 2.33× ✓；当前 §4b 0/7、eleuther 最近 ✓ | ✅ |
| L45 | 格内 n≥3 出中位、更薄格缺席不计 0；机构值 = 格中位的中位；每格一票 | aggregate_two_level.py 口径与报告头逐字一致 ✓ | ✅ |
| L47 | openai 精确数字：朴素 0.92/千词 → 两层 2.29，+149%，E 格构成压低 | `02917ae:output/openai/_aggregate.json`：朴素 median 0.92、institution 2.29 ✓；复算 +148.9%≈149% ✓；"engineering-heavy" 与信源包 §3"E 格构成压低"一致 ✓ | ✅ |
| L47 | kezhongke 限定语：朴素 2.39 → 两层 1.42，−41%，5 篇公告类上拉 | `2ee4d23:output/kezhongke/_aggregate.json`：2.39/1.42、N 格 n=5 ✓；复算 −40.6%≈41% ✓ | ✅ |
| L49 | LOO 最近质心：全库 63% → R 格 75% | `2ee4d23` 报告 63%（44/70）✓、`02917ae` 报告 R 格（6 库）75%（24/32）✓——均为 A 时代数字；**当前报告 §三为 N 格（7 库）65%（22/34）**，成稿未标时代（见 Y1） | ✅（附 Y1） |
| L51 | 扩容后 openai 精确数字反转：朴素 0.9、机构值 0.42；格集合 2→5；两口径均留痕 | 当前 JSON：朴素 0.9、institution 0.42 ✓；格 E/R → A/E/N/P/R = 5 ✓；格集合变化解释在稿 ✓（符合信源包 §7 同引纪律） | ✅ |
| L57 | hedge 词"约"子串污染；kezhongke 限定语 4.75→2.69/千字，约 43% 污染；哨兵测试 | kezhongke 档案 v0.2 日志逐字一致（单位=千字 ✓）；复算 43.4%≈43% ✓；tests/test_profiler.py:181 `test_hedge_substring_no_contamination` 在 ✓ | ✅ |
| L59 | TTR 差距 0.204 → 等长窗口 0.070，"roughly two-thirds smaller"；改 MATTR w=150 用于跨库比较 | eleuther 档案指纹解读逐字一致（"缩水约 2/3（0.204→0.070）"）✓；复算 −65.7%≈2/3 ✓；w=150 ✓ | ✅ |
| L61 | 规则路由关键词全中文、英文全部兜底；LLM passe 93 篇 + 扩容 71 篇；28 条低置信人工裁决全部维持 | 分类法 §现状/§五 逐字一致 ✓；93=8 库 93 篇（commit 44188ba）✓；71=7×10+1（§五扩容 passe）✓；28=v1 12+v2 16 全部 maintain（§五裁决收口 + genre-labels.json `_meta.adjudicated` 抽核 decision=maintain+注记）✓ | ✅ |
| L67 | 盲测三轮；决定性一轮主编判"像"；后一轮两层模型 A 格稿 12/13 定量走廊、六类病灶全部消除 | v2/v3/v4 三轮 ✓；v3 独立评审总评"像"（评审人未参与写作，信源包记"主编验收"，见 Y3）✓；v4=_p2-revalidation：13 项硬约束 12 达标、六类病灶全消除 ✓ | ✅（附 Y3） |
| L71 | 生产首跑事实审计摘下信源包 2 处错误（对战数、监管时间线），定点修订并留勘误 | eval-power judge-fact.md 红色项恰 2 处：2.8M/238→论文原文 2M/243/42；EU AI Act 高风险经 Digital Omnibus 推迟 2027-12-02 ✓ | ✅ |
| L73 | **"thirty-four regression tests"** | **已过期**：c322d40（2026-09-15 16:11）新增 test_gen_budgets.py 10 项——实测 `python3 -m unittest discover tests` = **Ran 44 tests, OK**。现在时句子，读者跑一遍即证伪（信源包 §6 同样滞留 34，需同步上游修订） | 🔴 R2 |
| L73 | 一致性校验 eight libraries and eight passes；全文本地、slug 公开可复采 | 实跑 check_profiles.py = 8 PASS / 0 FAIL ✓；corpus/README.md 版权与 slug 政策 ✓ | ✅ |
| L77 | 20 篇/库下无信号过线；eleuther q=0.088 登记为 tripwire | 当前 §4b ✓；eleuther 档案"最接近过线…扩容后优先复验" ✓ | ✅ |
| L79 | "Failing false-discovery correction is not evidence of absence" | 与 §4b 标注口径及信源包 §7 一致 ✓ | ✅ |
| L81 | 4 个双峰格、14 篇、亚型软标签、书面转正触发器；体裁边界是判断性裁决 | 分类法 §六逐字一致（4 格 14 篇、转正触发器 n≥6 且中位差>IQR）✓；§四/§五 裁决记录 ✓ | ✅ |
| L99–107 | 总结四条 + 两个未覆盖问题（≈40 篇/库、亚型重划） | 均为前文已核准断言的复用，推测部分已明确标注未被证据覆盖 ✓ | ✅ |
| L109 | 本文用被测 playbook 写成、发表将入自家语料 | 信源包 §7 批准的自指声明 ✓ | ✅ |
| Sources | 9 项文件 + 5 个代码工件 + 仓库地址 | 全部存在 ✓（profiler.py / discriminate.py / aggregate_two_level.py / check_profiles.py / tests/ 核实） | ✅ |

## 三、专项核查结论

1. **0/7 与 7/7 表述**：7/7（旧口径全过 FDR）与 0/7（新口径全未过）均按"未过 FDR 校正、方向性信号留档"纪律表述，未写成"指纹不存在"——合规。
2. **openai 消融链时代归属**：L3/L5 消融叙事用 A 时代数字且时代框架清晰（"one week later"）；**L37 openai 限定语句混入 A 时代数字而未标注（R1）**；数字密度两口径同引（L47+L51）已按 §7 纪律说明格集合变化——合规。
3. **派生百分比复算**：+149%（实 148.9）✓、−41%（实 40.6）✓、43%（实 43.4）✓、two-thirds（实 65.7%）✓、75% vs 63%（24/32=75.0、44/70=62.9）✓、指纹族 "more than doubled"（180→420=2.33×）✓、L5 raw gap 比较（33.5>32.0）✓。
4. **p=0.000 措辞**：成稿用 "Its p-value rounds to zero" 显式处理显示精度；§5b 的 q=0.000 以 "at or below the one-per-mille level" 转述——两处均规避了"等于零"误读，合规。
5. **工具可及性**：profiler.py / discriminate.py / aggregate_two_level.py / check_profiles.py / tests/ 全部在库且实跑通过（44 项测试 OK、8 PASS）。

## 四、红色项清单

1. 🔴 **R1 · L37**：openai 限定语信号 "15.1 against a same-cell pooled 7.98 … q of 0.351" 为 A 时代（10 篇/库）数字，出现在以当前口径叙述的 §1 段落中（同句群 eleuther 数字为当前口径）。当前工件（§4b 与 openai 档案 2026-09-15 扩容复核行）为 **pooled 7.38、p=0.014、q=0.234**。
   - 修订建议：直接更新为当前值（"...against a same-cell pooled 7.38 ... at q of 0.234"，可顺带补 p=0.014）；或保留旧值并加时代锚（"in the ten-article run"）。前文 L5 的消融数字（55.5/22.0/0.347/0.687）属 A 时代叙事框架，无需动。
2. 🔴 **R2 · L73**："thirty-four regression tests" 已过期——当前 44 项（c322d40 于 2026-09-15 增 10 项 gen_budgets 测试），实测全绿。
   - 修订建议：改 "forty-four regression tests"。上游 source-pack.md §6 同需修订（34→44）。

## 五、黄色项（建议，不阻断）

1. 🟡 **Y1 · L49**：LOO 63%→75% 为 A 时代数字，历史叙事框架内成立，但当前报告 §三为 N 格 65%（22/34）；读者打开 Sources 所引当前报告将找不到 "75% R 格"。建议加时代短语（"at the time" / "in the ten-article corpus"）或括注当前值。
2. 🟡 **Y2 · L3**："first week of September 2026"——旧口径指纹落地于 09-07~09-08，踩"第一周"边界（09-08 在 9/1–9/7 之外）。建议 "early September"。
3. 🟡 **Y3 · L67**："judged a match by the editor"——工件为独立评审报告（评审人未参与写作、总评"像"），"主编验收"系信源包定性。与批准事实一致，仅精度注记。

## 六、总判定

**需修订后发布（Revise, then publish）。**

理由：全文 30 组数值/事件断言中 28 组与仓库工件或 git 历史逐字/复算一致，论证链（7/7→0/7、两层纠正、量具纠错史、盲测+生产验证链）全部对账通过，两处专项纪律（0/7 措辞、p=0.000 精度）执行到位。两处红色项均为**句子级、局部、可当场核对的硬数字**：L37 系旧时代数字混入当前语境（时代归属未标清——恰为本文自身论点"口径须留痕"的适用范围），L73 系同日上游提交造成的测试计数过期。修订范围小（两句数字替换 + 一句计数更新），改完无需重走全流程；黄色三项建议一并处理以消除读者核验时的表面矛盾。
