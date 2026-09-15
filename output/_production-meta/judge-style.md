# judge-style — article-meta-v1.md 独立风格评审

> 口径：judge-kezhongke-en 系列（参照 templates/genre-playbook-kezhongke.md，2026-09-15 扩容刷新版）。
> 对象：output/_production-meta/article-meta-v1.md（目标：anthropic × openai 中间带 + kezhongke 签名；A 分析评论类）。
> 独立性声明：未读 generation-selfcheck.md 与 article-meta-v1.profile.json（铁律已守）。本文全部定量数据为评审以 `python3 profiler.py output/_production-meta/article-meta-v1.md` 独立重跑产出（/tmp 临时文件，未写回库）。
> 参照系抽读：corpus/anthropic/building-effective-agents.md、effective-context-engineering.md；corpus/openai/harness-engineering.md、unrolling-the-codex-agent-loop.md（各开头 ~500 词）。
> 评审日期：2026-09-15。

## 总判定

**像（置信度：高）。** §0.2 走廊 13/13 项带内（独立重跑）；A 类语步骨架七语步全命中且顺序合规；英文收尾组合四件全套、无自我批评位；处方 1–9 逐项有执行痕迹；红线（感叹号 0）守住。唯一严格读起来越限的是处方 7(c) 边界重申次数，且各次重申分布在不同语步、功能有别，属"擦边"而非 v2 式排比重申病灶。

## 一、§0.2 定量走廊复核（评审独立重跑 profiler.py）

| 指标 | 走廊（目标 / 合格区间） | 实测 | 判定 |
|---|---|---|---|
| 篇幅（词） | ≈2,900 / [2,100, 3,750] | 2,873 | ✅ 贴目标 |
| 平均句长（词） | ≈22 / [20, 24] | 20.8 | ✅ 带内偏低 |
| P90 句长（词） | ≤35 / ≤41 | 34 | ✅ |
| 平均段长（词） | ≈42 / [33, 53] | 51.5 | ✅ 带内偏高（与 A 格长段 delta 同向） |
| 数字密度 /千词 | ≈14 / [8, 21] | 17.75 | ✅ 偏高侧（题材为测量报告，处方 4 允许题材调节） |
| hedge /千词 | ≈10 / [8, 13.5] | 9.05 | ✅ |
| absolutist /千词 | ≈2 / [1.4, 3.4] | 2.09 | ✅ |
| 克制比 | 典型 4–5:1 / 红线 <3:1 | ≈4.3:1 | ✅ |
| 第一人称（次/篇） | ≈40 / [21, 69] | 31 | ✅ we 叙事题材下克制 |
| 客观自指（次/篇） | 1–2 / [1, 2] | 2 | ✅ 贴上沿（this analysis / this essay 各一） |
| 设问（次/篇） | 2–3 / [0, 5] | 3 | ✅ |
| MATTR | 0.68–0.69 / [0.66, 0.70] | 0.698 | ✅ 带内贴上沿，未出带，无需启动处方 8 |
| 年份锚点 /千词 | ≈1 / 软上限 2 | 0.35 | ✅ 与 A 格 −0.4 delta 同向 |
| 感叹号 | 0 / 0 | 0 | ✅ 红线 |

单句段：正文级单句段 ≈1 处（"With the objections priced in…"过渡段；编号结论条目不计），节拍器用量远低于 ≤4 上限——偏克制方向，不违处方 2。

## 二、A 类语步骨架核验（逐语步）

| 语步 | 位置 | 内容 | 判定 |
|---|---|---|---|
| HOOK | L3–11（≈269 词） | 一周反转叙事："The articles had not moved." | ✅ A 类/行业分析许可 HOOK；叙事集中于钩段位 |
| FRAME | L13–17（≈141 词） | "This analysis answers three questions"＋First/Second/Third＋概念命名＋四节路线图 | ✅ 招式 1 明示 N 问题清单；与编号节对应 |
| CONTEXT | L19–29（≈317 词） | Simpson's paradox 命名→机制→风格测量同构→六格分类法→旧口径 | ✅ 概念定义/背景归位，叙事只在此区 |
| ARGUE×4 | §1–4，L31–73（≈1,379 词） | 反转→两层模型→仪器纠错史→验证链 | ✅ 主体位，论断均挂数字锚（evidence 配比目测达标） |
| COUNTER | L75–83（≈250 词） | 三质疑逐条，verdict 显式标注：rebutted（带边界）/ rebutted / left open | ✅ 处理结果如实，未解决的未装已解决 |
| APPLY | L85–91（≈245 词） | 五条可执行判据（First…Fifth 序数链） | ✅ "判断标准清单"位 |
| CLOSE | L93–109（≈265 词） | 设问自答→编号结论×4→开放问题×2→比喻收束 | ✅ 英文收尾组合全套，无自我批评位，无重复段 |

ARGUE 篇幅占比 ≈48%（1,379/2,866），低于 [标注-3篇] ≈2/3 经验值——本节 CONTEXT 承载了机制论证（Simpson 几何向风格测量的映射实质是论证），且元稿需给验证链留位，记为次要观察而非失格。

次要观察：FRAME 落在全文第 6–7 段（HOOK 占 5 个短段），严读"开场三段内完成框架预告"略超；但 HOOK 紧凑且末段以 "What changed?" 设问预位，行业分析实证骨架（HOOK→CONTEXT→FRAME）本身框架位也在第三语步，判合规从宽。

## 三、处方 1–9 逐项

1. **长句拆分** ✅ 均值 20.8 / P90 34；>35 词长句偶见但均可一口气读完（如 L45 两层模型定义句）。
2. **段长回落** ✅ 均值 51.5 在 [33,53] 偏高侧；A 格长段铺陈方向一致；单句段 ≈1，节拍器克制。
3. **概念显式命名** ✅ "genre-composition contamination, composition contamination for short"（L17）一次命名全程复用（L49 回收）；pooled caliber / cell-corrected caliber / institution value / tripwire 全程唯一。比喻（lens/curvature）服务概念理解，合并招式 5 执行。
4. **数字纪律取中** ✅ 17.75/千词在带内偏 openai 侧；每个定性判断配数字锚（p/q 值、百分比、计数），未堆密度——测量报告题材下合理。
5. **边界声明中性化、限额化** ✅ 非收尾边界声明 3 处，恰在上限：L39 "none survives correction"（窄表述）、L77 "a boundary left standing"、L81 "the current evidence does not cover"；全部事实陈述语域，无 "we should have" 式自我检讨；不设自我批评小节。§3 仪器纠错史为题材本体（信任论证的一部分），措辞为修复记录而非道歉，不算越界。
6. **人称预算** ✅ 31 次在 [21,69]；we 本能题材压在 anthropic 侧（30），未放任漂向 openai 的 53。
7. **语言逻辑显性化** —— 见第六节专项：主题句=结论、承接装置、末句指针三项全优；**(c) 边界重申次数擦边越限**。
8. **MATTR 高侧处置** ✅ 0.698 未出带，无需启动；专名（pooled×28、correction×26）为处方 3 要求的统一复用，非失控。
9. **主题词对偶负面清单** ✅ 未见自造名词化复现（无 "the graded" 类）；"Seven libraries, seven signatures, seven clean certificates"（L33）同句 seven×3，但有节题 "Seven for seven, then zero of seven" 与标题构成明示回环框架，命中豁免条款。"the mix" 为 genre mix 的短称复用，属专名短称机制。

## 四、签名装置与收尾组合

- **招式 1 明示 N 问题清单** ✅ L15 三问题 + First/Second/Third，后文 §1–4 与 COUNTER/APPLY 逐题对应。
- **招式 2 信源分层标注** ⚠️ 弱合规（详见"最弱维度"）。外部三层（官方/第三方/社区）对本题材（自研究）天然不适用，装置以"论断挂内部工件锚"变体存活：in-text 具体锚点 ≥5（discrimination report L33、adjudication log L61、errata L71、taxonomy document L81、regression tests L73），Sources 区 9 条按工件类型分层。模糊归因 ≤1（"Reviewers who did not see the drafting instructions" L67 为无出处行为者指称）。
- **招式 3 判断带边界** ✅ 结论句普遍带数量/范围限定："roughly two-thirds smaller"、"an unknown share"、"Some of it usually is"。
- **招式 4 编号结论＋开放问题** ✅ 结论 1)–4)＋"Two questions the evidence does not cover"（中性、写证据未覆盖什么，按划界不计入处方 5 限额）。
- **招式 5 单一比喻复用** ✅ lens/curvature  optical 比喻：L35 命名→§4 节题 "the corrected lens"→L109 收尾回收 "you map its curvature and correct for the bend"；服务概念，不服务情绪。tripwire 为第二名词但作命名概念使用（×3），不构成第二比喻系统。
- **招式 6 术语纪律（英文反向）** ✅ 全文术语唯一；无中文原生概念需括注（kezhongke 作库标签沿用，与 openai library 同寄存器）。
- **收尾组合** ✅ 设问自答→编号结论→开放问题→比喻收束，四件齐、序合规、无自我批评位。

## 五、红线

感叹号 0 ✅；无 "业内普遍认为"式无出处断言（事实断言均有工件锚或属公共知识，如 Simpson's paradox）✅；术语无一文多译 ✅；CLOSE 区无重复段 ✅；emoji 0 ✅。

## 六、处方 7 专项检查

(a) **主题句＝结论** ✅ 抽核约 20 个正文段，论证段全部首句即该段结论（"The mechanism is plain aggregation"、"The correction moves real numbers, in both directions"、"Attribution sharpened as well" 等）；仅 HOOK 段为首句叙事（钩段位许可）。一段一义成立。

(b) **段间承接** ✅ 装置多样：连接词/短语（"Nor was openai a special case"、"With the objections priced in"）、指代链（"Under this caliber"、"The expansion then tested"）、序数链（"The second repair…The third repair"、"First objection…Second…Third…"、五条规则 First…Fifth）。未见无承接排比重申段。

(c) **边界重申 ≤1 次** ⚠️ **擦边越限**。"零过校正 ≠ 机构无风格（只是样本量不支撑）"这一边界表述出现 ≥3 个位置：L39（ARGUE，"none survives correction"）、L77–79（COUNTER，"not evidence of absence"＋"we do not claim otherwise"）、L95/L105（CLOSE，"not fingerprints found but signals"）。减缓因素：L79 系质疑二题中应有之义（反驳必须重述边界），L105 属编号结论回收，各次功能有别，非 v2 §23–25 同区三段排比重申。但 L39 的 not-X-but-Y 句式与 L105 结论 4 近乎同义，fluency pass 可再分化一次（建议：让边界表述只由 CLOSE 结论 4 承载，L39 退化为纯事实窄句）。

(d) **主节末句指针** ✅ 全链：L29→§1、L41→§2、L53→§3（隐含）、L63→§4、L73→COUNTER、L83→APPLY、L91→CLOSE。无子节，不存在指针句与下节首句同义重申问题。

## 七、自指处理专项（元稿：用签名装置写自身研究）

判定：**得当——克制、不炫耀、一笔带过。**

- 对自有语料用第三人称库标签处理："the kezhongke library shows the mirror image"（L47）——把自身数据当八个库中的普通一员接受同一仪器检验，论证上诚实，语气上去特殊化。
- 元披露仅收尾一句："drafted under the playbook it describes…will join the corpus it analyzes"（L109），一笔带过，"that is as it should be" 带轻微自嘲式从容而非邀功。
- §4 验证链（盲测三轮、事实审计抓出两处自家 source-pack 错误）是论点证据而非装饰性自省，数字具体、语域中性。
- 标题与框架不预告"我们的方法多巧"，论点落在普遍陷阱（Simpson/体裁构成）上，自身案例作举证。
- 小注（非违规）：kezhongke＝作者自有库的身份关系迟至收尾句才点破，中段读者理论上可能误读为第三方库；这是刻意的克制选择，且 L3 已示范了库标签的平白 gloss 手法（"this repository's plain label"），可在 FRAME 段同法加半句以绝歧义。当前处理可接受。

## 八、偏离方向判断

相对中间带的位置：**居中，语态/警句微偏 anthropic，数字密度微偏 openai，无出库寄存器漂移。**

- 偏 anthropic 侧证据：概念先命名后展开的定义纪律（对照 building-effective-agents 的 workflows/agents 划界句式）；格言式短拍 "The articles had not moved. The reading had."；第一人称 31 贴 anthropic 的 30；段内心智模型铺陈（two clinics 例）。
- 偏 openai 侧证据：数字密度 17.75 向 openai 的 20.69 靠拢（对照 harness-engineering 开篇即 "1,500 pull requests…3.5 PRs per engineer per day"）；we 建造/修复日志叙事骨架（"we ran…we doubled…we switched"）。
- 句长 20.8 略低于两库（22.45/22.3），由 HOOK 短句拉低，属节奏选择而非失控。
- kezhongke 签名件（三问题清单、verdict 标注、编号结论＋开放问题、工件分层 Sources）整合进论证流，无拼贴感。

## 九、最弱 2 维

1. **处方 7(c) 边界重申次数**——同一边界（零过校正≠无风格）在 ARGUE/COUNTER/CLOSE 三位 ≥3 次表述，严读超 "≤1 次重申"；功能分化使其不构成 v2 式病灶，但 L39 与 L105 结论 4 近同义，是全文唯一与处方条文直接摩擦之处。
2. **招式 2 信源分层（变体存活、执行最薄）**——外部三层对自研究题材天然缺位，装置以内部工件锚变体存活且 in-text 锚点 ≥5，但：锚点多无时间标签（哪一版 report、哪一轮 log 靠 Sources 兜底）；存在无出处行为者指称（L67 "Reviewers who…"）。与 playbook 2026-09-14 修订轮记录的"签名装置中执行最薄"一脉相承，本稿未见增量恶化也未见改善突破。

次要观察（不入最弱）：ARGUE 占比 ≈48% 低于 2/3 经验值；FRAME 预告落在第 6–7 段；数字密度贴带上沿——三项均有题材/骨架依据，记档即可。

## 十、结论

总判定 **像（高置信）**。成稿在定量走廊、语步骨架、收尾组合、签名装置四个层面均落在"anthropic × openai 中间带 + kezhongke 签名"目标内；自指处理克制得体，元稿身份一笔带过。建议（非发布阻断项）：一次 fluency pass 收拢边界重申至 CLOSE 单点承载；FRAME 段为 kezhongke 库标签加半句平白 gloss；in-text 工件锚补时间标签。
