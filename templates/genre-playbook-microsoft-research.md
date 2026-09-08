# Microsoft Research Blog · 撰写引导 playbook（初稿 v0）

> 生成日期：2026-09-08 ｜ 配套档案：《Microsoft Research Blog 风格档案 v0》
> 数据来源：output/microsoft-research/_aggregate.json（10 篇全量统计）+ 同目录 10 篇单篇 JSON + annotations/ 3 篇语步标注（orchard 24 段 / echoverse 59 段 / verifying-rust 44 段，共 127 段）+ output/_moves-aggregate.md 跨库聚合。
> 证据分级（每节开头标注）：**[统计层]** = output/ 下 JSON 全库统计，可直接信；**[标注-3篇]** = rubric 01 语步标注，实际覆盖 3/10 篇；**[推断]** = 仅档案散文或语料通读支持，未经脚本核验。
> 纪律：数值一律以 output/ JSON 为准；本文数字均可回溯至 _aggregate.json 或单篇 JSON。档案散文与 JSON 冲突处以 JSON 为准（已知冲突见文末清单）。

## 0. 一句话定位

**[推断]** 写一篇 MSR 风 = 写一篇"机构署名的工具发布短文"：系统名当主语、"At a glance" 要点块前置、CONTEXT→ARGUE 同构块推进、资源链接落点收尾。不写故事，不写心路，不吆喝。

## 1. 体裁 / 子体裁路由

**[推断]**（规则层 10/10 均判 `blog_or_exploration`，即"无法细分"；rubric 00 的 LLM 复核未跑。以下候选子体裁从档案 + 3 篇标注 + 语料通读归纳，**全部待裁决**。）

| 候选子体裁 | 识别特征 | 候选篇目 | 标注覆盖 |
|---|---|---|---|
| **系统/框架发布文** | 标题 = 系统名 + 冒号副题（"Orchard: An open framework for…"）；工具/框架即内容；多子题同构嵌套（SWE/GUI/Claw）或管线阶段分节（Factory/Building/Growing）；开源发布承诺为落点 | orchard、echoverse、flint、evolib | 2/4（待裁决） |
| **模型/基准发布文** | 标题含版本号或 "Introducing X"/"X reveals"（Aurora 1.5、Skala 1.1、CARE-X、MindTopo）；"At a glance" 要点带规模/精度数字；医学类附监管免责声明；强调与产品/生态连接（Microsoft Weather、CP2K 集成） | aurora-1.5、skala、gigapath-flash、care-x、mindtopo | 0/5（待裁决，**最大缺口**） |
| **方法论/工程验证文** | 副题路径式 "from standards to code"；按工程管线阶段分节（Lean specifications → Connecting spec to code → Intrinsics → …）；CLOSE 为长期愿景陈述 | verifying-rust | 1/1（待裁决） |

> 写作实务：在裁决落地前，先按"要发布的东西是什么"路由——发布工具/框架走第一类骨架，发布模型/基准走第二类，讲方法论走第三类。三类的差异目前主要在标题句式与收尾形态，骨架主体（见 §2）共用。

## 2. 通用语步骨架

**[标注-3篇]**（127 标注段聚合：ARGUE 77%、APPLY 8 处（六库最高）、COUNTER 4 处、HOOK 0 处、叙事段 1%——来源 output/_moves-aggregate.md）

```
无 HOOK（0/127 段：禁止场景/悬念/提问开场）
→ FRAME：署名墙后紧跟 "At a glance" 摘要块（3-5 条要点，成果前置、含数字）
→ CONTEXT×1-2：领域背景 + 瓶颈/缺口（"a persistent bottleneck"式问题陈述）
→ ARGUE 方案引入（"we introduce Orchard"——全文少数允许的第一人称句式）
→ ARGUE×n：设计/架构/方法 → 数字结果（系统文按子题同构分块；方法论文按管线阶段分节；
   图注段 "Figure N." 计入 ARGUE 节拍）
→ COUNTER×0-4（可选，内化为自我限定/边界限定，不设独立"反驳节"）
→ APPLY×1-3：资源落点必备（HF/GitHub/aka.ms/技术报告）+ 含义/展望
→ CLOSE×1-2（可省）：愿景式或评价式收束；Acknowledgements / Related publications 附录可选
```

三篇实证序列对照：

- **orchard**（系统发布）：FRAME → CONTEXT×2 → ARGUE×7（方案/架构）→ 三个子题块各 CONTEXT+ARGUE（领域需求→训练方法→数字结果）→ APPLY×3（含义+两条展望）。零 COUNTER。
- **echoverse**（系统深潜，4,880 词长文变体）：FRAME×2（主题句+成果前置）→ ARGUE 必要性 → APPLY×2（资源前置！开篇即挂 HF/技术报告）→ ARGUE×n 管线长文 → COUNTER×4（预设质疑"Control is only the floor"式回应 + 两处自我限定）→ APPLY（"We are releasing a piece of the factory"）→ CLOSE×2。
- **verifying-rust**（方法论）：FRAME → CONTEXT×2 → ARGUE×2 → APPLY×2（开源分支前置）→ 按管线阶段 ARGUE×n → Conclusion 节 ARGUE（权衡背景）→ CLOSE×2（方法总结 + 长期愿景）。

> 注意：APPLY 可不压尾——echoverse 与 verifying-rust 都把资源链接前移到开篇前 1/3。"落点指纹"指**必有一处以上资源型 APPLY**，位置灵活。

## 3. 定量预算表

**[统计层]**（全部抄自 _aggregate.json；唯二例外：词数分位数 aggregate 未收，由 10 篇单篇 JSON 现算补齐，来源已注明）

| 维度 | median | P25–P75 | 写作执行口径 |
|---|---|---|---|
| 阅读时长 | 5.5 min | 4.0–8.0 | 目标 5-6 分钟读完 |
| 篇幅（词数）¹ | 1,634 | 1,160–2,230 | 目标 ~1,600 词；>2,200 需理由（echoverse 4,880 为深度管线文例外） |
| 平均句长 | 22.55 词 | 20.8–23.6 | 长句为常态，勿切碎 |
| P90 句长 | 36 词 | 32–39 | 允许一成句子达 35+ 词 |
| 平均段长 | 44.4 词 | 41.0–47.1 | 2-3 句短段为主；单句段罕见（单篇 JSON `one_line_paragraphs`：8/10 篇为 0，flint/care-x 各 1 处） |
| 数字密度 | 26.87 /千词 | 13.61–29.55 | 每千词 ≥14 个数字 token |
| 精确数字（含小数/百分比） | 7.47 /千词 | 0–13.52 | 结果句必带精确数字 |
| 年份锚点 | 0.91 /千词 | 0.59–1.57 | 全文 1-2 处年份即可 |
| 限定语（hedge） | 7.5 /千词 | 4.14–10.01 | 论断留余地（about/around/toward/may） |
| 绝对化断言 | 1.81 /千词 | 0.63–2.36 | 压低 must/never/always |
| 全称量词 | 4.53 /千词 | 3.76–6.5 | all/every/any 适度 |
| **第一人称** | **9 次/篇** | 6–15 | **指纹指标：七库最低**（vs 库群 ~26，p=0.001，q=0.002 过 FDR）。主语让位给系统名 |
| 客观自指（this paper 等） | 0.5 次/篇 | 0–2 | 基本不用 |
| 问句 | 0 个/篇 | 0–2 | 不设问、不反问 |
| 感叹号 | 0 | 0–0 | 禁用 |
| MATTR(150) | 0.70 | 0.68–0.72 | 词汇多样但术语复现集中 |
| TTR | 0.38 | 0.36–0.42 | （长度敏感内参，不作目标） |
| 链接 / 文内引用 / 文献条目 | 0 | 0 | ⚠️ 抓取归一化伪零，实际资源落点靠标注层确认（见文末冲突记录）；正文不写 [n] 引用、不附参考文献 |

¹ 词数：median 1,634 / P25 1,160 / P75 2,230 / min 952 / max 4,880，由 output/microsoft-research/ 10 篇单篇 JSON 的 `word_count` 现算（_aggregate.json 未聚合此维度）。

## 4. 收尾形态与正反例

**[标注-3篇]**（APPLY 8 处/3 篇，六库密度最高——资源链接落点是 MSR 结构指纹）

收尾三段式（可压缩为两段）：① 含义/愿景陈述 → ② 资源落点（开源/数据/报告）→ ③ 可选 Acknowledgements + Related publications。

正例（例证 ≤40 字，保留原文）：

- 资源落点压尾：orchard — "By releasing the complete Orchard stack"（接"帮助社区共建"句式收尾）
- 资源落点 + 链接直给：echoverse — "Code and tasks: https://aka.ms/echoverse"
- 愿景式 CLOSE：verifying-rust — "That is the long-term promise"（"code that remains fast, portable, maintainable"式三并列形容词收束）
- 评价式 CLOSE：echoverse — "worlds grow at the frontier"（evaluation becomes "the engine"式隐喻升格）
- 开源落点前置进摘要：aurora — "Released as open source on GitHub"（At a glance 第 2 条即落点）；evolib 压尾 "results are available on GitHub"
- 框架级含义陈述：orchard — "the environment layer matters"（把单点成果升格为层/级论断）

反例（这些写法在库内无实证，写了就不像 MSR）：

- 场景/悬念开场（"2026 年 5 月的某一天…"）——HOOK 0/127 段；
- 第一人称调查叙事主线（"We struggled… then we realized"）——第一人称 median 9 次/篇、叙事段 1%，Eleuther 式复盘叙事（61.5 次/篇）是本库反面；
- 感悟格言收束（"X is not just about A—it's about B"连用）——OpenAI 式 CLOSE，本库 CLOSE 出现率仅 2/3 篇且为愿景陈述而非格言；
- 无数字定性连段、感叹号、营销问句——感叹号全库 0、问句 median 0、数字密度 P25 仍达 13.61/千词；
- 文内 [n] 引用 + 参考文献表撑深度——citation/reference 全 0，深度一律靠外链论文与图注承载。

## 5. 操作化模式（MSR 固定招式）

1. **"At a glance" 摘要块** **[推断]**（语料全文核对 10/10 均有此块，尚未入 output/ 统计，待脚本化复核）：署名墙后立即 3-5 条要点，每条 = 可选加粗小标题 + 成果句（含数字）。范式：flint "Polished charts from simple specs." / evolib "Self-supervised. EvoLib enables…" / echoverse "a 9B model nearly doubles its base score"。写作动作：先写正文，最后凝练 3-5 条前置；每条必含一个可核验事实或数字。
2. **署名墙机构信用** **[推断]**：By 4-11 位作者、人人带头衔（Principal Researcher / Technical Fellow & CVP）。信用靠机构层级背书，不靠个人叙事——这解释了第一人称最低：作者已列在文头，正文无需 "we" 在场。
3. **系统名主语化** **[统计层]**（第一人称 9 次/篇 + 档案画像互证）：正文主语默认用系统名（"Orchard is…""Flint allows…""EvoLib transforms…"）；"we" 只保留三个槽位：we introduce / we release / we hope。
4. **同构子题块** **[标注-3篇]**（orchard 实证）：多子题文章按"领域需求 CONTEXT → 训练方法 → 数字结果 ARGUE"严格平行嵌套（Orchard-SWE/GUI/Claw 三块同构）。写多子题文时，每块段落功能对齐、量级对齐。
5. **双数字改进句式** **[标注-3篇]**：性能结论用"起点→终点"双数字锚定——orchard "rises from 18.6% for the untrained model"、echoverse "36.5% to 67.1%"。禁用单点吹嘘（"达到 SOTA"），必给对照基线。
6. **图注段入节拍** **[标注-3篇]**："Figure N." 说明段承担 ARGUE 功能（orchard 2 图、echoverse 13 图注均入标注流），图注写足机制解释，不是摆设。
7. **监管免责声明块** **[推断]**（医学候选子体裁 2 篇实证）：care-x 独立 "Research Note" 块前置（"not a Microsoft product offering"）、gigapath 内嵌（"not validated for clinical use"）。涉医/涉监管题材必备，位置在 At a glance 前后。
8. **主题句悬置副题** **[标注-3篇]**（echoverse）：标题下、At a glance 上可悬一句三并列口号（"Scaling fidelity over sheer count"），仅长文变体使用。

## 6. 就绪度评估

**结论：部分能。** 定量预算表（§3）与宏观骨架（§2 主干）已达可直接指导写作的成熟度；"At a glance" 块、系统名主语化、资源落点三招式可操作。但子体裁路由全挂待裁决、模型/基准发布文 0 篇标注，篇级细骨架（尤其第二大候选子体裁）不足以直接执行。

缺口清单：

1. **标注覆盖 3/10 且偏科**：已标 2 篇系统文 + 1 篇方法论文；5 篇模型/基准发布候选篇 0 标注 → §1 路由表与 §2 变体骨架依赖外推。
2. **子体裁未正式路由**：规则层 genre 全部 `blog_or_exploration`，rubric 00 LLM 复核未跑，三类划分仅为候选。
3. **链接/引用指标伪零**：`links_per_1k`/`citation_marks`/`reference_entries` 全 0 系抓取归一化所致，资源落点强度目前只能靠标注层（APPLY 8 处）旁证，定量表该行不可用于校验成稿。
4. **_aggregate.json 未收词数分位数**：篇幅预算由单篇 JSON 现算补齐（median 1,634 / P25 1,160 / P75 2,230），尚未入聚合管线。
5. **档案内部冲突未回改**：档案 §2 表格篇幅作 1,673，与 §1 及 JSON 中位数 1,634 冲突（以 JSON 为准）。
6. **rubric 02 论证标注 0 篇**：档案 §4 所列"集体署名是否记入 source_tier"等裁决项悬空。

最小补全动作（按性价比排序）：

1. 补标 mindtopo + care-x（或 aurora-1.5）两篇模型/基准发布文 → 标注覆盖 5/10 且三个候选子体裁各 ≥1 篇，§1 路由表即可提交裁决；
2. 跑 rubric 00 LLM 复核，正式确认/推翻三类子体裁划分；
3. profiler 小改：把 `word_count` 分位数收进 _aggregate.json，消除口径补丁；
4. 回改档案 §2 表格 1,673 → 1,634 并记冲突日志（本条与本 playbook 无关，但属同一份档案的遗留事实错误）。

---

### 附：档案 / 数据冲突记录（本次编写发现）

| # | 冲突 | 裁决 |
|---|---|---|
| 1 | 档案 §1 "median 1,634 词" vs §2 七库对照表 "1,673" | 10 篇单篇 JSON `word_count` 中位数 = **1,634**，以 JSON 为准；§2 表格待回改 |
| 2 | 统计层 `links_per_1k`=0 vs 标注层 APPLY 资源链接 8 处（HF/aka.ms/技术报告/开源分支） | 系抓取归一化伪零；写作指导以标注层为准，统计行标 ⚠️ |
| 3 | （背景已知错误：档案 §1 曾作"篇幅最长 5,660 词""第一人称 8.5"） | 现行 v0 已修复为 1,634 / 9.0（commit 249bf07），与 JSON 一致，无遗留冲突 |
