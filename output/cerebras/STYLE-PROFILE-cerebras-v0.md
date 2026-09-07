# 《Cerebras Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2026-03 至 2026-08，研究/工程深潜分层采样，排除纯产品新闻）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/cerebras/ ｜ 统计：output/cerebras/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**性能极限主义者的"快"叙事**：以推理速度作为一切论证的支点——无论是系统深潜、引擎对比还是经济学分析，最终都通向"更快"的世界观。作者单人署名（常见两个名字轮换），声音个人化但克制；卖点论据（自产基准、客户端案例）天然内嵌于研究叙述，营销与工程说理的边界模糊。
⚑ 例证："That is fast enough for the agent to treat iteration as cheap instead of precious."（never-loop-without-verifiers——速度即世界观）

## 2. 量化基线（10 篇，median）· 六库对照表

| 指标 | **Cerebras** | EleutherAI | Databricks | OpenAI | Anthropic | 壳中客(中) |
|---|---|---|---|---|---|---|
| 篇幅（词/字） | 2,036 | 4,673 | 4,199 | 2,819 | 2,622 | 3,905 字 |
| 平均句长（词/字） | **18.8** | 25.7 | 26.2 | 22.2 | 22.5 | 34.5 字 |
| 数字密度 /千词(字) | **40.1** | 44.1 | 24.4 | 16.1 | 7.4 | 17.1 |
| 精确数字 /千词(字) | 3.1 | **14.1** | 4.0 | 1.1 | 1.6 | 5.6 |
| 限定语 /千词(字) | 7.9 | **10.6** | 5.5 | 8.8 | 9.6 | 2.7† |
| 断言绝对化 /千词(字) | **1.82** | 1.2 | 1.1 | 1.6 | 2.1 | 1.1 |
| 第一人称 | **10.5** | 61.5 | 21.5 | 59.0 | 42.5 | 6.0 |
| 客观自指 | 0.5 | 1.5 | 0.0 | 0.5 | 2.0 | 2.0 |
| 外链 /千词(字) | 0 | 0 | 0 | 0 | 0 | 0 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 |
| TTR | 0.42 | **0.26** | **0.46** | 0.31 | 0.35 | 0.35 |
| MATTR（w=150） | 0.70 | 0.65 | **0.71** | 待重算‡ | 待重算‡ | 0.74 |
| **指纹**（discriminate.py，vs 余四库 pooled） | **第一人称最低**（10.5 vs ~46，p<0.001，q=0.001，过 FDR） | — | — | — | — | — |

> 指纹解读：五库中唯一低第一人称的研究博客——"没有 we 的极限性能叙事"，补足第 1 节画像的"个人化但克制"。
> † 壳中客限定语为 2026-09-07 词表修复后 v10 口径（原 4.8 含"约→约束"子串污染）。
> ‡ OpenAI/Anthropic 正文不入库，MATTR 待语料重采后重算；其 TTR 行为长度敏感指标，跨库比较以 MATTR 为准。

## 3. 结构信号（rubric 01 全量标注：never-loop-without-verifiers，39 段 → 31 标注）

- **语步骨架**：HOOK → CONTEXT×2 → FRAME → ARGUE×15（穿插）→ APPLY×3 → CLOSE×2
- 特征：**COUNTER 缺失**（0 处）——反例全部内化为 ARGUE 的"对抗推演"（sub：模型会 cheat 的推演），与 OpenAI engineering-deep-dive 的"自我反驳内化"同构；
- APPLY×3 是教学转身（"build up your intuition" "Off-limits" 处方）——Cerebras 特有的"教程落点"，OpenAI deep-dive 没有这么强的读者指令；
- 叙事配比：23% 段落含叙事（案例+时间线），集中在开篇与案例段——低于壳中客 FDE 篇（0.25）；
- 完整标注：`output/cerebras/annotations/never-loop-without-verifiers.moves.jsonl`

## 4. 待人工裁决项

- ⚑ 画像"营销-研究混合"需人确认边界（哪些篇算研究、哪些算宣传）；
- 语步标注已完成 1 篇（never-loop-without-verifiers），其余 9 篇待标注；
- 篇幅为何显著短于 EleutherAI/Databricks？可能是采样偏近期短文的系统偏差，需复查列表。

## 5. 语料清单

how-cerebras-serves-gpt-5-6-sol / ultrafast-frontier-inference-hot-chips-2026 / how-we-built-our-knowledge-base / the-economics-of-ai-reasoning / lessons-learned-from-building-multi-agent-workflows / how-to-stop-your-autoresearch-loop-from-cheating / exomebench / latency-debt / never-loop-without-verifiers / thinking-inside-the-box-implicit-chain-transformer