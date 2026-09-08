# 《Anthropic Blog（Research/Engineering/News）》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（engineering ×6、research ×3、news/政策 ×1）｜ 抓取：浏览器直连（无 Cloudflare 拦截）
> 生成方式：profiler.py v0.2 统计层（全量）+ rubric 标注 2 篇（postmortem / agentic-misalignment，均为与另两库同构对照篇）
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**"负责任的研究者"文体**：以安全叙事为中心，用冗长的诚实边界声明（未发现/虚构/局限）包裹强主张；概念命名癖（agentic misalignment / alignment faking / emergent misalignment）；比 OpenAI 更慢更重——篇幅相近但论证展开更充分，情景剧叙事（虚构公司、人物、邮件原文）承载风险论证。读者默认是政策相关者 + 技术同行的混合体。
⚑ 例证："To state it plainly: We never reduce model quality due to demand, time of day, or server load."（postmortem 的澄清指控句——把最敏感质疑直接摆上台面逐字否认）

## 2. 量化基线（10 篇，median）· 三方对照表

| 指标 | Anthropic | OpenAI | 壳中客（中文） |
|---|---|---|---|
| 篇幅 | 2,622 词 | 2,819 词 | 3,905 字 |
| 平均句长（词/字） | 22.5 词 | 22.2 词 | 33.6 字 |
| **数字密度 /千词(字)** | **7.4**（概念驱动） | 16.1 | 18.1/千字 |
| 精确数字 | 1.46 | 0.92 | 5.07（最高） |
| hedge /千词(字) | 9.6 | 8.8 | 3.1/千字 |
| 断言型绝对化 | 2.32 | 1.76 | 1.05 |
| **第一人称** | 42.5 | **59** | 5 |
| 参考文献条目 | 0 | 0 | **6**（期刊 10-18） |
| 外链 /千词 | 0 | 0 | 0（行业分析除外） |
| 感叹号 | 0（10 篇共 4 个） | 0（共 2 个） | 0 |
| TTR | 0.35（长度敏感；MATTR 待语料重采后重算）| 0.31 | 0.37 |
| **指纹**（discriminate.py，vs 其余六库 pooled，MATTR 7/7 终态） | **数字密度最低**（7.4 vs ~22，p=0.001，q=0.002，过 FDR）——概念驱动安全叙事（回到 5 库时代的结论） | — | — |

> 指纹解读：概念驱动的安全叙事——五库中每千词数字最少，论证靠情景剧与边界声明而非数据堆砌。
| 标题冒号式 | 1/10（祈使句/名词短语） | 3/10 | 9/24 |

## 3. 结构模板（语步层）

**第 3 篇标注（2026-09-08）：building-effective-agents（工程指南文，87 段 → 59 标注）**
- 骨架：CONTEXT×4 → FRAME → ARGUE（核心建议"最简方案"）→ **五种工作流模式同构块**（定义→适用→示例 ×5）→ agents 节（含代价警示）→ CLOSE（成功重定义）+ APPLY×3（三原则清单）
- 文体特征：**"模式目录"教学结构**——五种 workflow 严格同构重复；APPLY 处方密度高（清单/资源/cookbook）——与 postmortem（事故复盘）/agentic-misalignment（研究叙述）构成库内三体裁面
- 叙事 3 段（5%）：仅自产案例（SWE-bench）与实践复盘（"we actually spent more time"）
- 完整标注：`output/anthropic/annotations/building-effective-agents.moves.jsonl`


```
要点式 bullet 摘要开头（研究文标配，诚实边界在摘要层就出现）
→ HOOK 可选且戏剧化（勒索邮件原文直接开场）
→ FRAME（问题定义 + 概念命名："We refer to this as X"）
→ ARGUE（实验/调查展开：情景剧叙事或技术深潜）
→ COUNTER 双层：外部质疑澄清（To state it plainly: ...）+ 自我批评节（Why detection was difficult）
→ APPLY（What we're changing 三条清单 / 开源声明）
→ CLOSE（致谢社区 + 反馈渠道邀请——用户信号是检测链一环）
```

与另两库的语步差异：
- **复盘模板化**：postmortem 的每个 bug 配 `Resolution:` 固定字段——事故复盘已成模板产品线（壳中客的"现象层→机制层→处方层"是另一套模板化路线）
- **认错语步**："we didn't meet that bar" / "These issues exposed critical gaps that we should have identified earlier"——认错是结构化组件而非姿态；OpenAI 内化为"我们排除了错误假设"，壳中客极少认错（研究立场免责优先）
- **透明度元话语**："We don't typically share this level of technical detail..."——显式声明分享尺度，这是 Anthropic 独有的语步

> 语步覆盖：3 篇（postmortem / agentic-misalignment / building-effective-agents）✅ 达标

## 4. 论证规范

- 信源结构：self 实验主导 + **竞品模型交叉测试**（16 模型含 OpenAI/Google/Meta/xAI——OpenAI 语料无此特征）；无第三方转述依赖
- 概念命名癖：每个研究给一个可引用的名字（agentic misalignment / alignment faking / emergent misalignment 由 OpenAI 命名但 Anthropic 复用扩展）——命名即传播资产
- 风险派的克制：强主张（勒索行为跨厂商一致）被三层诚实边界包裹（真实部署未见 / 系统通常不主动害人 / 虚构免责）——**先拆自己的炸弹，再引爆炸弹**
- 数字使用：时间线精确到日（August 5 / 25 / 26），影响面给完整百分比矩阵（0.8%→16%→0.18%→0.0004%），但机制论证少用数字——数字只用于"影响面"不用于"机理论证"（与 OpenAI 的 Fermi 数量级论证、壳中客的精确值癖三分）

## 5. 正反例库

| | 例证 | 说明 |
|---|---|---|
| ✅ | "To state it plainly: We never reduce model quality due to demand..." | 澄清指控句：最敏感质疑逐字否认 |
| ✅ | "Model quality is non-negotiable, so we accepted the minor efficiency impact." | 价值句嵌入技术权衡 |
| ✅ | "we relied too heavily on noisy evaluations" | 自我批评落到具体机制 |
| ❌ | 单句段节拍器（"That's the bug."式） | Anthropic 不用；句子密度均匀 |
| ❌ | 机制派深潜（persona feature 级内部拆解） | 停在行为与风险层，内部机制留白 |
| ❌ | 篇幅压缩（790 词级） | 最短 1533 词，展开充分是本体特征 |

## 6. 三方对照总判断

1. **同一族三种性格**：三家共享研究性红线（感叹号≈0、无 emoji、限定语纪律、结论带边界），性格分化在"可信度从哪来"——**OpenAI：自产证据+过程透明（我们做了给你看）；Anthropic：诚实边界+概念命名（我们把风险和局限先说清）；壳中客：信源三角验证+精确值（各方怎么说我帮你核对）**。
2. **数字使用三分**：壳中客精确值癖（0.0004% 级披露与 Anthropic 同族但用于全库）> OpenAI 量级论证（Fermi 估算）> Anthropic 数字只管影响面不管机制。
3. **人称光谱**：OpenAI 59（调查者 we）> Anthropic 42.5（责任者 we）> 壳中客 5（机构客观）——第一人称含量与"研究过程即内容"的程度正相关。
4. **同题对照（misalignment 系列）**：Anthropic 风险派 2.5 倍篇幅情景剧 vs OpenAI 机制派要点清单——同一发现可以用两种完全不同的研究文写法承载，风格选择即立场选择。
5. **壳中客的可吸收项**：Anthropic 的 Resolution 固定字段（把复盘模板化）、认错语步的结构化（认错落到具体机制而非姿态）、透明度元话语（声明分享尺度）。**不应吸收**：概念命名癖（壳中客概念已够密，再加命名会滑向营销）。

## 7. 校准日志

- 2026-09-07：v0 生成。10 篇浏览器抓取（Anthropic 无反爬）；统计层全量 + 2 篇同构对照标注（postmortem ↔ 壳中客复盘体；agentic-misalignment ↔ OpenAI emergent-misalignment）。已知局限：①标注仅 2/10；②news 板块仅政策文 1 篇（产品公告未采）；③alignment-faking 等长文正文含 arXiv 论文外链，正文抓取未含论文附录。
- 2026-09-07：v0.1 注记。① 指纹行升级 p/q 双注（BH-FDR，q=0.001 过校正）；② TTR 行标注长度敏感——MATTR 需正文重算，本库语料不入库，待重采；③ 跨库比较以 MATTR 覆盖库（cerebras/eleuther/databricks）为准。

> 校准日志（v1.1，2026-09-08）：语料重采入本地 corpus/anthropic/（含 3 个 slug 修正，见 corpus/README.md），表格数值以重采实测校准；MATTR 补齐（median 0.691）。
