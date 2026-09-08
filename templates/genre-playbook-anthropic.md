# Anthropic 博客 · 撰写引导 playbook 初稿

> 2026-09-08 初稿。来源：output/anthropic/_aggregate.json（统计层，10 篇全量）+ annotations/ 3 篇标注（postmortem / agentic-misalignment / building-effective-agents）+ STYLE-PROFILE-anthropic-v0.md（档案散文，仅作推断依据）。
> 证据分级约定：**[统计层]** = 全库 10 篇实测，可直接采信；**[标注-3篇]** = 仅 3/10 篇有语步标注（其中 building-effective-agents 只有 moves 序列、无 argument 层），单类子体裁常仅靠 1 篇支撑——**属小样本外推，指导写作前建议补标至每类 ≥3 篇**；**[推断]** = 仅档案散文支持，未经标注/统计验证，待裁决。
> 数值与档案散文冲突时，一律以 _aggregate.json 与各篇 JSON 为准（冲突清单见文末）。

## 一、体裁 / 子体裁路由特征表

[统计层] 规则层路由：9 篇 blog_or_exploration + 1 篇期刊体（a-postmortem-of-three-recent-issues）——规则层对本库几乎无区分度，子体裁需 LLM 路由（rubric/00）。

[标注-3篇] + [推断] 候选子体裁（**全部待裁决**，除已标注 3 篇外归属均为档案推断）：

| 候选子体裁 | 识别特征 | 代表篇目（★=已标注） |
|---|---|---|
| **安全研究叙述 research-narrative** | 要点式 bullet 摘要开场（方法/发现/边界）；戏剧性证据 HOOK（模型输出原文）；概念命名句 "We refer to this as X"；情景剧叙事承载风险论证；三层诚实边界 | agentic-misalignment★；推断：alignment-faking、auditing-hidden-objectives |
| **事故复盘 postmortem** | 澄清指控句前置；认错句；透明度元话语；时间线精确到日；每个 bug 配 `Resolution:` 固定字段；自我批评节（Why detection was difficult） | a-postmortem-of-three-recent-issues★（全库仅 1 篇，单篇外推） |
| **工程方法指南 engineering-playbook** | 经验背景开场（dozens of teams / Over the past year）；定义辨析先行；模式清单结构（每个模式 = 定义 → 适用条件 "When to use" → 示例清单）；处方落到"最简方案"；附录承载补充论证 | building-effective-agents★；推断：effective-context-engineering、effective-harnesses-long-running-agents、demystifying-evals-for-ai-agents、building-c-compiler |
| **政策立场 position/policy** | 制度化承诺文档；致谢评估机构；脚注层 | 推断：responsible-scaling-policy（890 词，全库最短，无任何标注，特征最不确定） |

## 二、通用语步骨架

[标注-3篇] 三类已标注篇目可归纳出的公共骨架（七类语步序列）：

```
（研究文标配）要点式 bullet 摘要开头——诚实边界在摘要层就出现
→ HOOK 可选且戏剧化：模型输出/邮件原文直接开场（"Cancel the 5pm wipe"）
→ FRAME：问题定义 + 概念命名（"as agentic misalignment"）
→ CONTEXT：架构/经验/方法铺垫（工程指南类以此开场，HOOK 缺席）
→ ARGUE×n：情景剧演示（五步计划式逐步复现）或模式清单（定义→适用条件→示例）
→ COUNTER 双层：外部质疑澄清（"To state it plainly" 式）+ 自我批评节（检测为何难/边界声明 "aren't prescriptive"）
→ APPLY：改进清单（三条）/ 开源声明（"open-sourcing the code"）/ 资源指向（cookbook）
→ CLOSE：致谢社区 + 反馈渠道邀请 / 成功重定义 + 原则清单（"Maintain simplicity"）
```

子体裁偏差：
- **postmortem**：HOOK 缺席，FRAME（范围+调查启动）后立刻接澄清指控句与认错句——先把最敏感质疑摆上台面逐字否认，再展开事实。
- **engineering-playbook**：ARGUE 是排比式模式枚举而非单线论证；CLOSE 后允许附录（Appendix 1/2）继续承载 ARGUE。
- **research-narrative**：COUNTER 以"诚实边界三连"形式出现（真实部署未见 / 系统通常不主动害人 / 虚构免责）——**先拆自己的炸弹，再引爆炸弹**。

## 三、定量预算表

[统计层] 全部抄自 output/anthropic/_aggregate.json（10 篇，median 与 P25–P75）：

| 指标 | median | P25–P75 | 写作预算解读 |
|---|---|---|---|
| 阅读时长（分钟） | 8.5 | 7.0–10.0 | 对应约 2,100–3,700 词；全库实测 890–7,977 词 |
| 平均句长（词） | 22.45 | 19.6–23.8 | 长句为主，句子密度均匀，不用单句段节拍器 |
| P90 句长（词） | 34.5 | 30–41 | 允许 30+ 词的展开句，但不超过 45 |
| 平均段长（词） | 44.75 | 36.6–53.1 | 段落饱满（2–3 句），不写一句一段 |
| 数字密度 /千词 | 8.25 | 3.27–17.0 | 七库最低档：数字只用于影响面，不用于机理论证 |
| 精确数字 /千词 | 1.46 | 0.47–3.95 | 精确值保留给影响面披露（百分比矩阵、时间线到日） |
| 年份 /千词 | 0.61 | 0.34–1.91 | 少做编年铺陈 |
| 外链 /千词 | 0 | 0–0 | 正文零外链（论文链接放附录/更新注记） |
| 参考文献条目 | 0 | 0–0 | 不设文献列表 |
| 限定语 hedge /千词 | 10.52 | 8.3–13.56 | 高频诚实边界：hypothetical / fictional / potentially / it seems unlikely |
| 绝对化 /千词 | 2.32 | 1.37–3.37 | 允许少量强主张，但必须被 hedge 层包裹（hedge:绝对化 ≈ 4.5:1） |
| 数量词 /千词 | 5.06 | 4.29–7.51 | — |
| 第一人称（次/篇） | 30 | 21–69 | "责任者 we"：高频但低于 OpenAI 的"调查者 we" |
> **人称硬约束**（P1 横评实证升级，2026-09-08）：上表区间 [21, 69] 为**硬预算**（非参考行）——次数类有长度依赖，按实际篇幅折算（±20% 篇幅差异对应 ±20% 次数调整）；写作时**按节预分配**（开场/主体/收尾各多少处 we/our，大纲阶段声明）；完稿必须过 `profiler first_person_count` 自检。**题材豁免制**：题材本身要求团队构建叙事（build-log/复盘）时可上浮，但须在大纲声明"人称豁免：目标 ~X 次，上浮原因 Y"——未声明的超界=失格（实证：P1 同题材盲测 anthropic 成稿 57 vs 基线 30，题材 we 本能压过库预算；openai 58/53 贴上沿）。本库为 P1 最大偏差库（57 vs 30）——豁免声明对 build-log 类题材几乎必填。
| 客观自称（the post 等） | 1.5 | 1–2 | 少元话语，透明度声明除外 |
| 感叹号 | 0 | 0–1 | 硬约束：不用 |
| 疑问句 | 2.5 | 0–5 | 少量设问，不作主要推进手段 |
| TTR | 0.34 | 0.31–0.35 | 长度敏感，仅作参考 |
| MATTR | 0.69 | 0.67–0.70 | 词汇丰富度中上；术语复用（命名概念）不压 MATTR |
| CJK 字符 | 0 | 0 | 全英文写作 |

## 四、收尾形态与正反例

[标注-3篇] 三种已验证的 CLOSE 形态：
1. **致谢 + 反馈渠道邀请**（postmortem）：致谢社区，请用户继续用 /bug 反馈——用户信号被写成检测链的一环。
2. **预警定位 + 开源收束**（research-narrative）：早期预警自定位 + 方法公开促进复现。
3. **成功重定义 + 原则清单**（engineering-playbook）："isn't about building the most sophisticated..." 句式重定义成功，接三条核心原则（"Maintain simplicity"）。

[推断] 未标注篇目语料尾部（corpus/anthropic/，≤40 字例证）显示两种补充形态：**致谢 + 招聘邀请**（"Interested candidates...anthropic.com/careers" 类）与**领域宣言**（"alignment auditing is just beginning"）。

正反例：

| | 例证（原文，≤40 字） | 说明 |
|---|---|---|
| ✅ | "We never reduce model quality" | 澄清指控句：最敏感质疑逐字否认，加粗级声明前置 |
| ✅ | "we didn't meet that bar" | 认错句：结构化组件，落到标准而非姿态 |
| ✅ | "relied too heavily on noisy evaluations" | 自我批评落到具体机制 |
| ✅ | "context as a precious, finite resource" | 概念命名式收束：给读者一个可带走的词 |
| ✅ | "we're entering a new world" | 克制的展望句，不配感叹号 |
| ❌ | 单句段节拍器（"That's the bug." 式） | 段长 median 44.75 词，句子密度均匀 |
| ❌ | 机制派内部拆解（feature 级） | [推断] 停在行为与风险层，内部机制留白 |
| ❌ | 正文外链 / 参考文献列表 | [统计层] 两项 median 均为 0 |
| ❌ | 数字驱动机理论证 | [统计层] 数字密度 8.25/千词，全库最低档 |

## 五、操作化模式（本库特有固定招式）

1. **概念命名句** [标注-3篇]：每个研究给一个可引用的名字，固定句式 "We refer to this behavior as X"——命名即传播资产。写作时：核心现象必须在 FRAME 段完成命名，后文全程复用该名。
2. **诚实边界三连** [标注-3篇，仅 agentic-misalignment 单篇验证，外推需谨慎]：强风险主张必须配三层包裹——①真实部署未见实例（摘要层+正文各一次）②"系统通常不主动害人"防渲染句 ③虚构免责声明（fictional names / no real people harmed）。
3. **澄清指控句** [标注-3篇，postmortem 单篇]：把最敏感的外部质疑逐字摆上台面再否认，"To state it plainly: ..." 固定起手，置于 FRAME 之后、事实展开之前。
4. **Resolution 固定字段** [标注-3篇，postmortem 单篇]：事故复盘中每个 bug 一个 `Resolution:` 解决块——复盘模板化。
5. **透明度元话语** [标注-3篇，postmortem 单篇]：显式声明分享尺度（"We don't typically share this level of technical detail..."）。
6. **认错结构化** [标注-3篇]：认错必须落到具体机制（哪条 eval 太噪、哪项隐私实践妨碍调试），不接受姿态式道歉。
7. **模式清单三段式** [标注-3篇，building-effective-agents 单篇]：工程指南中每个模式固定为 定义 → "When to use this workflow" 适用条件 → 示例清单，排比展开。
8. **影响面百分比矩阵** [标注-3篇]：数字预算集中投向影响面披露，精确到 0.0004% 级；机理论证不用数字。

## 库差异显性化（同题材抗同质化）

> 2026-09-08 新增。依据：output/_p1-cross-review.md 第五节——四库同题材盲测中本库成稿与 cerebras/openai 共享"三失败→教训→改进"骨架，库差异退化为开场/收尾措辞。

**适用声明**：同一题材下，本库风格必须体现在下列结构级独有项与语步密度上。若成稿骨架与他库收敛（如"三失败→教训→改进"通稿结构），只换开场/收尾措辞者判不合格。

**本库结构级独有项**（同题材成稿时必须显性命中）：
1. **显式概念命名句** [标注-3篇]：核心现象在 FRAME 段以 "We refer to this as X" 固定句式命名，后文全程复用——区别于 cerebras 的隐性主题句与 openai 的拟人化命名。
2. **自我批评节** [标注-3篇，postmortem 单篇，外推需谨慎]：独立成节的 "Why detection was difficult" 式自省，把失败归因于自身检测/评估机制，不并入教训清单。
3. **边界声明** [标注-3篇]：处方/建议后附 "aren't prescriptive" 式免责；研究文另配诚实边界三连——强主张必被 hedge 层包裹。
4. **成功重定义收尾 + 原则清单** [标注-3篇，engineering-playbook 单篇]：以 "isn't about..." 句式重定义成功，接编号原则清单收束，不以格言排比收尾。
5. **语步密度签名** [统计层]：段长 median 44.75 词（饱满多句段，禁单句段节拍器）；hedge 10.52/千词；数字密度 8.25/千词（七库最低档，数字只投影响面）。

**写作自检**（成稿后逐项核对）：
- 独有项 1–4 命中 ≥3 条；其中**自我批评节**必须独立出现——本库签名语步，区别于 openai 把自反驳内化进 Bug 编号叙事。
- 对照第三节定量预算表：段长 / hedge / 数字密度须落在本库 P25–P75 内；若向 cerebras 短段或 openai 高人称靠拢，视为指纹丢失，退回重写。

## 六、就绪度评估

**结论：部分能。** 统计层（定量预算、零外链、感叹号禁令等硬约束）可直接指导写作；语步层仅 3/10 篇有标注，三类子体裁各只有 1 篇支撑，政策类（responsible-scaling-policy）完全无标注，骨架与子体裁路由均为小样本外推。

缺口清单：
1. **标注覆盖 3/10**：postmortem / research-narrative / engineering-playbook 各 1 篇；building-effective-agents 只有 moves 序列、缺 argument 层（claims/evidence/qualifiers 未标）。
2. **子体裁路由未经 LLM 全量裁决**：规则层 9/10 篇停留在 blog_or_exploration 未细分，路由表中 6 篇归属是推断。
3. **news/政策板块仅 1 篇**（890 词的政策更新，档案注明产品公告未采），代表产品/公告体裁缺失。
4. TTR 长度敏感已知；MATTR 已补齐（median 0.69）——档案 v0 早期注记中"MATTR 待重算"已被 v1.1 与 _aggregate.json 覆盖，不再构成缺口。
5. **同题材抗同质化为新增约束（2026-09-08）**：P1 横评（output/_p1-cross-review.md）发现本库 playbook 对"构建+失败+加固"题材与他库引导收敛；上文"库差异显性化"节的对抗效力未经二轮盲测验证。

最小补全动作（按性价比排序）：
1. 补标 2 篇工程指南类（建议 effective-context-engineering + demystifying-evals，含 argument 层）→ engineering-playbook 达 3 篇；
2. 补标 1 篇研究类（建议 alignment-faking 或 auditing-hidden-objectives）→ research-narrative 达 2 篇；
3. 对全库跑 rubric/00 LLM 体裁路由，裁决本文件第一节的候选子体裁表；
4. 若要用政策/公告体裁写作，先补采 2–3 篇产品公告入语料再标注。

## 附：档案 / 数据冲突清单（以 JSON 为准）

| 冲突项 | 档案散文（STYLE-PROFILE-anthropic-v0.md） | output/ JSON 实测 | 处置 |
|---|---|---|---|
| 第一人称 | §2 表记 42.5 | _aggregate.json median 30（P25–P75: 21–69） | 以 30 为准；42.5 疑为旧口径或未校准值 |
| hedge /千词 | §2 表记 9.6 | median 10.52 | 以 10.52 为准 |
| 数字密度 /千词 | §2 表记 7.4 | median 8.25 | 以 8.25 为准（"七库最低"的方向性结论不受影响） |
| 最短篇幅 | §5 称"最短 1533 词" | 各篇 JSON：responsible-scaling-policy 890 词 | 以 890 为准；§5 反例行需修正 |
| 篇幅 median | §2 表记 2,622 词 | 各篇 word_count 实测 median 2,639.5（890–7,977） | 口径略异，差异 0.7%，以各篇 JSON 为准 |
| TTR | §2 表记 0.35 | median 0.34 | 以 0.34 为准 |
| 标注篇数 | §1/§7 称"标注 2 篇" | annotations/ 实有 3 篇（含 building-effective-agents.moves.jsonl） | 以 3 篇为准；档案校准日志未追记该文件 |
