# P1 横向对照评审 · 四库同题材成稿（2026-09-08）

> 题材固定：四篇均写 "style-profiler 自身构建与加固"（同一故事）。
> 目标库：cerebras / openai / anthropic / kezhongke-en（§0 跨语种口径）。
> 评审方法：结构对照（节标题/开场/收尾/语步骨架）+ profiler 定量对照各库基线。
> 产物：output/_p1-validation-samples/draft-{cerebras,openai,anthropic,kezhongke-en}.md

## 一、总评

**"同一题材 × 四库"的对照实验成功暴露了 playbook 引导的边界**：
三库（cerebras/openai/anthropic）成稿共享同一个"三失败叙事"骨架，库差异退化为表皮（命名/开场/收尾措辞）；
仅 kezhongke-en 在结构层真正分岔（五层功能命名）。**题材的通用叙事结构（构建→失败→加固）压过了库的语步特征**——这是"撰写引导"当前的真实能力边界，不是缺陷，但必须写进 playbook 的适用声明。

## 二、结构对照（同题材如何被四库重写）

| 维度 | cerebras | openai | anthropic | kezhongke-en |
|---|---|---|---|---|
| 开场 | frontmatter + 裸标题直入 | frontmatter + 裸标题直入 | **经验开场**（"Over the past year, we have been building..."）| **比喻立起**（"We built a ruler."）+ 三问题 FRAME |
| 失败叙事组织 | 戏剧命名节（Inflation / Drift / validator）| **Bug #1/#2/#3** 编号 + 每 bug=初态→失败→转折→修复→教训 | **Failure mode 1/2/3** + Why-detection 自我批评节 | 五层（phenomenon→mechanism→prescription→diagnosis→decision）|
| 概念命名 | 隐性（主题句）| 侦探式（"the judge"拟人）| **显式命名句**（"We refer to this as measurement contamination"）| ruler 隐喻全程 |
| 收尾 | 三连排比格言（"the one we can always check"）| 格言 + 5 条加粗 bullet + 制度化承诺 | 成功重定义（"isn't about..."）+ 三原则清单 + 边界声明 | 编号结论 + 开放问题 |
| 语步签名 | ARGUE 主导 + 短段 | ARGUE + COUNTER 内化（Bug#2 自反驳）| CONTEXT 开场 + 双层 COUNTER（澄清+自我批评）| FRAME 三问 + 五层 ARGUE |

**库特征 → 成稿的映射**：
- anthropic 的 postmortem 元素（Why detection was difficult、aren't prescriptive 边界）**成功转移**进工程方法论文——库特征最强的一次体现
- openai 的侦探叙事（Bug 编号 + 教训格言）**可见**但被题材同质化稀释（与 cerebras 的"validator 节"撞车）
- cerebras 的短段+警句排比收尾**可见**
- kezhongke-en 的五层命名 + 比喻 + 证据分级标注**完全独有**——唯一结构级分岔

## 三、定量对照（成稿 vs 各库基线）

| 篇 | 句长/基 | 段长/基 | 数密/基 | hedge/基 | 人称/基 | mattr/基 |
|---|---|---|---|---|---|---|
| cerebras | 19.7/18.8 ✓ | 23.7/30.6 短 | 32.1/40.1 ✓ | 8.97/7.89 ✓ | 16/10.5 ✓ | 0.683/0.70 下缘 |
| openai | 22.5/22.3 ✓ | 43.7/40.2 ✓ | 17.1/20.7 ✓ | 12.3/**9.6** 偏多 | 58/53 ✓ | 0.686/0.68 ✓ |
| anthropic | 22.2/22.5 ✓ | 45.3/44.8 ✓ | 4.76/**8.25** 偏少 | 13.3/**10.5** 偏多 | 57/**30** 近 2 倍 | 0.708/0.69 ✓ |
| kezhongke-en | 18.8/**22.9** 偏短 | 66.6/**40.7** 偏长 | 11.4/**19.7** 偏少 | 12.9/**4.44** 高 3 倍 | 12/19.5 ✓ | 0.681/0.73 下缘 |

### 关键信号

1. **人称密度未分化**：openai 58 / anthropic 57 几乎同值——anthropic 成稿人称超基线近 2 倍。最显眼的两库指纹（第一人称高低）在四篇里没拉开。**题材的 we 叙事本能压过了库预算**（或 playbook 人称预算未作硬约束）。
2. **kezhongke-en 英文 hedge 天然高**（12.9 vs 中文基线 4.44）：§0 要求克制比 ≥3:1 成立，但**绝对值跨语种不可比**——英文写作的 hedge 密度基线本就 8-13（英文库全如此）。跨语种迁移的固有张力，§0 的"不迁移"原则是对的，但成稿 hedge 12.9 已高于所有英文库中位——需自检器口径。
3. **kezhongke-en 段长反向偏离**（66.6 vs 40.7 偏长）：五层论证的段长特征没向"中文短段快节奏"靠拢——跨语种后段长直觉失效。
4. cerebras 段长偏短（23.7 vs 30.6）是其"短招式段"固有倾向，两库共识缺陷（排版/叙事配比）again。

## 四、盲测新暴露的工具缺陷（追加 P2）

1. **英文问句指标 bug**（kezhongke-en 自审发现）：`sentence_stats.question_sentences` 英文恒为 0——按 `[.!?]+` 切句后分隔符被剥除，再以 `？/?` 后缀判定必然为 0，与 `stance.questions=3` 矛盾。英文问句指标当前不可用。
2. **OBJ_SELFREF_EN 缺变体**（§0 执行时已自曝）：无 this essay/this analysis——kezhongke §0 弱迁移项无法用工具自验。
3. **三库骨架同质化**（本次横评）：engineering 系 playbook（cerebras/openai/anthropic）对"构建+失败+加固"题材都引导出三失败→教训→改进——playbook 需加"题材抗同质化"提示（给定题材时，库差异应体现在语步密度与招式而非骨架）。

## 五、结论与建议

- **横向对照法成立**：题材固定是比"随机题材"更严的盲测——它把库差异从"题材巧合"中剥离出来，是测量 playbook 引导力的正确实验。
- **三库（cerebras/openai/anthropic）playbook 的区分度不足**：骨架同质化说明它们共享的 engineering-deep-dive/playbook 变体对同一题材的约束收敛。建议：playbook 补"库差异显性化"列（本库相对他库的**结构级**独有项——如 anthropic 的自我批评节、openai 的 Bug 编号、cerebras 的警句收尾）。
- **kezhongke-en 是唯一结构级分岔**：五层命名+比喻+证据分级=跨语种口径的最佳验证样本——建议优先补独立评审（judge-kezhongke-en），把 §0 从"设计"变"实证"。
- **P2 追加 3 项**（英文问句 bug / OBJ_SELFREF / 题材抗同质化提示）。

## 六、样本

四篇 draft 均在 output/_p1-validation-samples/（正文+自审注释格式），未入库前为工作区文件。
