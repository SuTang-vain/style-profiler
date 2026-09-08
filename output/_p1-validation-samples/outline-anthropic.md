# 盲测大纲 · anthropic 库 · engineering-playbook 工程方法指南

> 依据：templates/genre-playbook-anthropic.md（§一 路由表、§二 通用语步骨架、§三 定量预算表、§四 收尾形态、§五 操作化模式）+ output/anthropic/_aggregate.json（10 篇 median/P25–P75）。
> 校准锚点（仅校准，不挪用）：building-effective-agents（经验开场、"aren't prescriptive"边界声明、Summary 原则清单）；a-postmortem-of-three-recent-issues（认错落机制、"Why detection was difficult"自我批评节）；effective-context-engineering（定义辨析先行、有限资源概念命名）。
>
> **子体裁路由：engineering-playbook。** 理由：题材是"我们如何构建并加固一个统计工具"的方法论复盘——路由表中 engineering-playbook 的识别特征（经验背景开场、定义辨析先行、模式清单结构、处方落到最简方案）与素材最贴合；postmortem 子体裁虽含"bug 修复"元素，但其识别特征是面向用户的事故（澄清指控句前置 + `Resolution:` 固定字段 + 时间线到日），且仅 1 篇标注支撑（单篇外推，playbook §六标注为高风险外推），本题材无外部用户受影响，故不取。证据等级声明：骨架 [标注-3篇]，engineering-playbook 条目本身仅 building-effective-agents 单篇标注支撑，属小样本外推。
>
> **篇幅/预算目标**（全部抄自 §三 [统计层] 行）：
> - 词数 ~2,600（median 2,639.5；P25–P75 2,098–3,145；阅读时长对应 7–10 分钟）
> - 平均句长 19.6–23.8 词（median 22.45）；P90 句长 30–41、硬上限 45
> - 平均段长 36.6–53.1 词（median 44.75；2–3 句/段，**禁单句段节拍器**）
> - hedge ≈10.5/千词（8.3–13.56）→ 全稿 ~27 处；绝对化 ≈2.3/千词（≤3.37）→ ~6 处，hedge:绝对化 ≈4.5:1
> - 数字密度 ≈8.25/千词（3.27–17.0）→ ~21 处；精确数字 ≈1.46/千词 → ~4–8 处，集中投向影响面披露（§五.8）；年份 ≤2 处（0.61/千词）
> - 疑问句 2–3 个（median 2.5，0–5）；感叹号 0（硬约束）；外链 0、参考文献 0（median 均 0）
> - 第一人称 we ≈30 次（21–69，"责任者 we"）；客观自称（this post 等）1–2 处
> - MATTR 0.67–0.70（命名概念全程复用，不压 MATTR）

## 语步骨架（engineering-playbook 偏差版）

骨架 = CONTEXT 开场（HOOK 缺席，§二"工程指南类以 CONTEXT 开场"）→ FRAME（问题定义 + 概念命名句）→ ARGUE×3（模式清单三段式：定义 → 出现条件 → 示例，§五.7）→ COUNTER 双层（外部质疑澄清 + 自我批评节，§二）→ APPLY（改进清单三条 + 资源指向）→ CLOSE（成功重定义 + 原则清单，§四.3）。

| # | 小节 | MOVE | 功能（内容要点 → playbook 招式） |
|---|---|---|---|
| 1 | （开场，无标题） | CONTEXT | 经验背景开场：过去一年我们在构建测量机构写作风格的工具；一句话成果 + 一句话主张（§一 engineering-playbook 识别特征："dozens of teams / Over the past year"式） |
| 2 | | CONTEXT | 工具一句话定义 + 本文承诺（分享构建中学到的、给做测量工具者的实践建议）；客观自称 1/2 |
| 3 | What the profiler measures | FRAME | 定义辨析先行：statistical layer vs judgment layer 切分（§五 定义辨析；"At X, we categorize..."式）；26 个确定性指标、同输入同输出 |
| 4 | | FRAME | 为何选确定性：LLM 打分无法回归测试；确定性是验证前提（hedge 层包裹的强主张） |
| 5 | | FRAME（概念命名句） | 核心现象命名：指标回答了一个与你所问略有不同的问题——"We refer to this as measurement contamination"，后文全程复用（§五.1，命名即传播资产） |
| 6 | Three failure modes | ARGUE（清单引子） | 结构预告：三种 contamination 失效模式，各按 定义 → 何时出现 → 实例 展开（§五.7 排比预告）；问句预算 1/3 可用于小节标题 |
| 7 | Failure mode 1: the counter that matched substrings | ARGUE（定义） | 定义：字符串匹配计数器把子串当证据；何时出现：无空格文字/词边界缺失时 |
| 8 | | ARGUE（示例） | 实例：中文限定语词表含单字"约"；substring matcher 把"约束"计为限定语；数字留到段尾集中披露（4.75→2.69 hits/千词，roughly 43% 假命中——§五.8 影响面集中投放） |
| 9 | | ARGUE（发现路径+修复） | 发现靠读命中清单而非代码；修复为词边界匹配；教训：危险 bug 不报错，返回可信数字（认错结构化 §五.6：落到 substring 机制） |
| 10 | Failure mode 2: the ruler that stretched | ARGUE（定义） | 定义：长度混淆——指标随篇幅机械变化；何时出现：跨不同长度样本比较词表丰富度 |
| 11 | | ARGUE（示例） | 实例：原始 TTR 随篇幅下降；跨机构比较实际在比长度；修复为滑动窗口 MATTR |
| 12 | | ARGUE（影响面披露） | 修复后跨机构差距 0.204→0.070（roughly 三倍缩小），排序不变（精确数字集中于此，"影响面百分比矩阵"变体） |
| 13 | | ARGUE（对抗推演） | 内化处理"0.204 是真信号"质疑：推演→排序未动→残差解读（约 2/3 表观差异是尺子不是文本）；hedge 内嵌 |
| 14 | | ARGUE（教训） | 每个指标须声明 invariance（它不响应什么）；可声明即可测试 |
| 15 | Failure mode 3: the validator that only said PASS | ARGUE（定义） | 定义：静默跳过——校验器看不见部分输入却报告全绿；何时出现：解析器白名单过窄 |
| 16 | | ARGUE（示例） | 实例：markdown 表解析器跳过加粗单元格，从不比较、从不失配；全绿 PASS |
| 17 | | ARGUE（影响面+修复） | 修复后立刻抓到 6 处期望值漂移（多为过期期望值）；教训：不能失败的校验器比没有更糟 |
| 18 | Why detection was difficult | COUNTER（自我批评节） | 三类失效共同根因：我们信任了绿灯输出；隐私式盲区类比不适用，直接认：测试套件没有一条先演示过失败（认错落机制 §五.6；节名呼应 postmortem 自我批评节） |
| 19 | | COUNTER（外部质疑澄清+边界声明） | "To state it plainly"式澄清：这些 bug 未改变任何已发布结论（排序不动）；但这些模式 aren't prescriptive——是我们的经验不是普遍法律（§二 COUNTER 双层；hedge 密集段） |
| 20 | What we changed | APPLY（改进清单三条） | 三条改进：①计数一律词边界+双语分词 ②每个指标声明并测试 invariance ③每个 check 先演示失败——20 项回归测试全部见过红（§二 APPLY 改进清单三条式） |
| 21 | | APPLY（资源指向） | 工具与词表已开源/可复核指向（不附外链，正文零外链硬约束——用"available in the repository"式叙述） |
| 22 | Summary | CLOSE（成功重定义） | "Success in measuring style isn't about the cleverest metric..."句式重定义成功（§四.3） |
| 23 | | CLOSE（原则清单） | 三条核心原则 bullet：Prefer deterministic checks over judgments / Name what your metric ignores / Require every test to fail once（§四.3 原则清单变体） |
| 24 | | CLOSE（克制展望） | 一句无感叹号展望句收尾；无 CTA、无招聘、无参考文献、无外链 |

**禁令清单（§四反例）**：单句段节拍器；正文外链/参考文献列表；数字驱动机理论证（数字只投影响面）；感叹号；feature 级内部机制拆解停在行为层（本题材为工具行为层，天然适配）。

**hedge 配额分布**（~27 处）：§3–5 FRAME 6 处 / 三种失效模式各 4–5 处 / COUNTER 5 处 / APPLY+CLOSE 3 处。
**精确数字配额**（~5 处）：4.75、2.69、43%、0.204、0.070 集中于 #8/#12；6 处漂移、20 项测试、26 维、7 家为整数级数字。
**问句配额**（2–3）：#6 小节标题设问 1 处、#18 自我批评节内 1 处、机动 1 处。
