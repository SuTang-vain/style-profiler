# 盲测大纲 · cerebras 库 · build-log 工程构建记

> 依据：templates/genre-playbook-cerebras.md（§一 路由表、§二 语步骨架、§三 预算表、§四 收尾形态、§五 操作化模式）+ output/cerebras/_aggregate.json。
> 子体裁：build-log 工程构建记。路由依据：题材为"How we built X"式多子系统工程复盘，含迭代失败叙事点（子串污染 / TTR 漂移 / 校验器静默跳过——即路由表所列 initially tested…kept encountering 结构），收尾用设计哲学收束（§四.2），不用号召。
> 篇幅目标：1,300–1,800 词；段长 ~30 词（1–2 句/段，库指纹）；句长 16–22 词、P90 ≤32；数字密度往 40/千词靠；hedge ≈8/千词；问句 ≤4（仅 FRAME 转折）；感叹号 0；外链/参考文献 0；we ≈6–21 次/篇。

| # | 小节 | MOVE | 功能（内容要点 → 对应 playbook 招式） |
|---|---|---|---|
| 1 | （引子，无标题） | HOOK | 数字+反直觉开场：单字"约"占限定语计数 43%（§五 反直觉/数字 HOOK，禁场景描写） |
| 2 | | CONTEXT | 工具定义：研究性文章风格分析 profiler；统计画像 |
| 3 | | CONTEXT | 7 机构 → 26 维数字向量（同期背景+数字锚定） |
| 4 | | CONTEXT | 统计层 ~26 个确定性指标；同输入同输出（术语定义） |
| 5 | | CONTEXT | 历史锚定：2026 年对照"丢给大模型打分"路线（年份密度预算） |
| 6 | | ARGUE | 机制论断：模型裁判无法回归测试（"cannot diff a mood"） |
| 7 | | FRAME | 设问转折+结构预告：two failure modes / one blind validator / 20 tests（问句预算 1/4） |
| 8 | The statistical layer | ARGUE | 主体：4 指标族总览（句长/数字密度/限定语/词表） |
| 9 | | ARGUE（数据锚定） | 每个指标可手工复核；4.75 hits/千词可逐条重数（§五 数据锚定句） |
| 10 | | ARGUE | 逐族定义展开（roughly/about 内嵌，抬 hedge 密度） |
| 11 | | ARGUE | 单个指标不聪明、组合稳定可测（机制→落点） |
| 12 | | ARGUE | 世界观落点：determinism 使验证 cheap not precious（§五 速度即世界观变体） |
| 13 | | ARGUE | 转折：计数器也失败，2 种特征方式，命名 |
| 14 | | ARGUE（概念对立命名） | Inflation 单句定义（§五，"Spiralling." 式独立短段） |
| 15 | | ARGUE（概念对立命名） | Drift 单句定义 |
| 16 | Inflation: the counter that saw ghosts | ARGUE（过程证据） | 词表含"约"；初版匹配器按子串匹配 |
| 17 | | ARGUE（过程证据） | "约束"含"约"为第二字；每次出现被计为限定语 |
| 18 | | ARGUE（过程证据） | 子串匹配当初为何合理：中文无空格，分词是另一个工程 |
| 19 | | ARGUE（过程证据） | 英文下 mostly 正常；语料转双语后污染显形 |
| 20 | | ARGUE（过程证据） | 发现路径：读命中清单而非代码 |
| 21 | | ARGUE（反例演示） | 谈 constrained optimization 的段落像"犹豫森林"；指标没崩、在撒谎 |
| 22 | | ARGUE（数据锚定） | 修复为词边界匹配；中位数 4.75→2.69/千词，roughly 43%（限定语+精确数字同句） |
| 23 | | ARGUE | 论文没变；约 43% 的"限定语"从来不是限定语 |
| 24 | | ARGUE | 新中位数 2.69 是现在敢辩护的数 |
| 25 | | ARGUE | 教训：危险 bug 不报错，返回可信数字 |
| 26 | Drift: the ruler that stretched | ARGUE | TTR 定义与来历（distinct/total）；长度依赖是机械性 |
| 27 | | ARGUE（过程证据） | 篇幅越长词越重复；同作者长文 vs 短札 |
| 28 | | ARGUE | 长度依赖有文献常识但易忘；悄悄倾斜所有比较 |
| 29 | | ARGUE | 7 机构原始 TTR 比较≈比长度；尺在量自己 |
| 30 | | ARGUE | 修复：MATTR 滑窗 w=150；等长帧消除篇幅泄漏 |
| 31 | | ARGUE（数据锚定） | 跨机构差距 0.204→0.070，roughly 三倍缩小；排序不动 |
| 32 | | ARGUE | 残差解读：约 2/3 表观差异是尺子不是文本 |
| 33 | | ARGUE（对抗推演，内化 COUNTER） | 反对意见"0.204 是真信号"→推演→排序未动→封堵（§五 对抗推演代替反驳节；不设独立 COUNTER 节） |
| 34 | | ARGUE | 教训：每个指标声明 invariance（必须不响应什么） |
| 35 | | ARGUE | 可声明即可测试；invariance 进回归套件 |
| 36 | Does the judge discriminate? | ARGUE | 目的：区分机构；LOO 设定（问句预算 2/4，小节标题） |
| 37 | | ARGUE | LOO 机制：每篇被没见过它的分类器评判 |
| 38 | | ARGUE | 不偷看、无第二次机会（过程证据短段） |
| 39 | | ARGUE（数据锚定） | 7 库 LOO 71%；约每 7 篇中 5 篇 |
| 40 | | ARGUE（克制） | 仍有约 2/7 误判；主张刻意 modest（限定语内嵌边界，不设 Limitations 节） |
| 41 | | ARGUE（对抗推演+克制） | 7 库是小世界；只主张"信号存在、特征可分" |
| 42 | | ARGUE | 近随机=装饰；71% 是地板不是奖杯 |
| 43 | The validator that only said PASS | ARGUE（过程证据） | 回归 harness 重算并 diff markdown 表期望值 |
| 44 | | ARGUE（过程证据） | 解析器跳过加粗单元格 → 从不比较、从不失配 |
| 45 | | ARGUE（反例演示） | 全绿 PASS；表的一部分对校验器不可见 |
| 46 | | ARGUE | 静默跳过比 loud failure 更糟 |
| 47 | | ARGUE（数据锚定） | 修复后立刻抓到 6 处数值漂移 |
| 48 | | ARGUE | 6 处多为过期期望值（修指标后未同步）；逐一钉进测试 |
| 49 | | ARGUE | 教训：不能失败的校验器比没有更糟（absolutist 预算内 1 处） |
| 50 | | ARGUE | 新规：每个 check 先演示失败；20 项回归测试都见过红 |
| 51 | What we now require | APPLY | 教学转向：build up your skepticism（§五 处方清单起手） |
| 52 | | APPLY | 祈使句短清单 6 条（150 tokens 等数字复用） |
| 53 | | APPLY | Off-limits 禁令封顶（§五 固定招式） |
| 54 | （收尾，无标题） | CLOSE | 设计哲学：难点不是 26 个指标，是赢得信任；cross-examination（§四.2 build-log 收束，无号召） |
| 55 | | CLOSE | determinism → answerable → 团队敢快速迭代（呼应速度即世界观） |
| 56 | | CLOSE | 一句设计原则终：always right vs always check（无 CTA、无参考文献、无感叹号） |

不写清单（§四反例）：参考文献/外链附录；编号结论+关注问题；Limitations 独立节；感叹号收束。
