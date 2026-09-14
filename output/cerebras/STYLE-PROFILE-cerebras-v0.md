# 《Cerebras Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：20 篇（2026-09-14 体裁平衡扩容 10→20；原 10 篇：2026-03 至 2026-08，研究/工程深潜分层采样，排除纯产品新闻）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/cerebras/ ｜ 统计：output/cerebras/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**性能极限主义者的"快"叙事**：以推理速度作为一切论证的支点——无论是系统深潜、引擎对比还是经济学分析，最终都通向"更快"的世界观。作者单人署名（常见两个名字轮换），声音个人化但克制；卖点论据（自产基准、客户端案例）天然内嵌于研究叙述，营销与工程说理的边界模糊。
⚑ 例证："That is fast enough for the agent to treat iteration as cheap instead of precious."（never-loop-without-verifiers——速度即世界观）

## 2. 量化基线（20 篇，median；2026-09-15 扩容重聚合）· 六库对照表

| 指标 | **Cerebras** | EleutherAI | Databricks | OpenAI | Anthropic | 壳中客(中) |
|---|---|---|---|---|---|---|
| 篇幅（词/字） | 1,199.5 | 2,106 | 2,476.5 | 1,601.5 | 2,195 | 4,830 字 |
| 平均句长（词/字） | **17.95** | 25.1 | 23.75 | 22.4 | 23.8 | 34.5 字 |
| 数字密度 /千词(字) | **33.68** | 41.42 | 24.38 | 17.77 | 8.84 | 17.1 |
| 精确数字 /千词(字) | 3.09 | **9.86** | 4.0 | 0.9 | 0.6 | 5.6 |
| 限定语 /千词(字) | 5.54 | **8.8** | 5.28 | 10.16 | 10.52 | 2.7† |
| 断言绝对化 /千词(字) | **1.82** | 1.27 | 1.57 | 1.77 | 2.3 | 1.1 |
| 第一人称 | **9.0** | 27.5 | 30.5 | 40 | 30 | 6.0 |
| 客观自指 | 0.0 | 0.5 | 0.5 | 1.0 | 1.0 | 2.0 |
| 外链 /千词(字) | 0 | 0 | 0 | 0 | 0 | 0 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 |
| TTR | 0.43 | **0.35** | **0.40** | 0.35 | 0.35 | 0.35 |
| MATTR（w=150） | 0.71 | 0.66 | **0.71** | 0.68 | 0.69 | 0.74 |
| **指纹**（discriminate.py，vs 余六库 pooled，对照组=当前 7 库+重采语料） | **平均段长最低**（p<0.001，q=0.001，过 FDR）——短段快节奏；对照组敏感史：第一人称低→P90句长低→全称量词高→平均段长低（见校准日志）。**2026-09-14 两层口径复核：体裁构成校正后未过 FDR，原信号含构成成分**（N 格内段长仍最低 33.2 vs 同格 pooled 46.2，p=0.021，q=0.351，探索性；新口径最显著信号=数字密度高 @N格 42.45 vs 28.2，p=0.009，q=0.311）。**2026-09-15 扩容复核（n=20，FDR 族分列口径不变）**：最显著信号换位平均段长低 @A格（29.4 vs pooled 50.8，p=0.002，q=0.143）——旧口径指纹"段长最低"在新口径 A 格（n=5）重新居首，仍未过 FDR；旧口径对照（5b）保持段长最低（q<0.001 过 FDR，仅对照） | — | — | — | — | — | — |

> 指纹解读：五库中唯一低第一人称的研究博客——"没有 we 的极限性能叙事"，补足第 1 节画像的"个人化但克制"。
> † 壳中客限定语为 2026-09-07 词表修复后 v10 口径（原 4.8 含"约→约束"子串污染）。
> OpenAI/Anthropic 两列系 2026-09-08 v2 重采口径实测（MATTR 已补齐 0.68/0.69）；TTR 为长度敏感指标，跨库比较以 MATTR 为准。

## 3. 结构信号（rubric 01 全量标注：never-loop-without-verifiers，39 段 → 31 标注）

- **语步骨架**：HOOK → CONTEXT×2 → FRAME → ARGUE×15（穿插）→ APPLY×3 → CLOSE×2
- 特征：**COUNTER 缺失**（0 处）——反例全部内化为 ARGUE 的"对抗推演"（sub：模型会 cheat 的推演），与 OpenAI engineering-deep-dive 的"自我反驳内化"同构；
- APPLY×3 是教学转身（"build up your intuition" "Off-limits" 处方）——Cerebras 特有的"教程落点"，OpenAI deep-dive 没有这么强的读者指令；
- 叙事配比：23% 段落含叙事（案例+时间线），集中在开篇与案例段——低于壳中客 FDE 篇（0.25）；
- 完整标注：`output/cerebras/annotations/never-loop-without-verifiers.moves.jsonl`

> **3 篇聚合（2026-09-08）**：knowledge-base + economics 补齐后 COUNTER=0/118 保持（"对抗内化为推演"稳固）；叙事段 14%（工程复盘的迭代叙事点：initially...kept encountering...stopped working）。详见 `output/_moves-aggregate.md`。

## 4. 待人工裁决项

- ⚑ 画像"营销-研究混合"需人确认边界（哪些篇算研究、哪些算宣传）；
- 语步标注已完成 1 篇（never-loop-without-verifiers），其余 9 篇待标注；
- 篇幅为何显著短于 EleutherAI/Databricks？可能是采样偏近期短文的系统偏差，需复查列表。

## 5. 语料清单

how-cerebras-serves-gpt-5-6-sol / ultrafast-frontier-inference-hot-chips-2026 / how-we-built-our-knowledge-base / the-economics-of-ai-reasoning / lessons-learned-from-building-multi-agent-workflows / how-to-stop-your-autoresearch-loop-from-cheating / exomebench / latency-debt / never-loop-without-verifiers / thinking-inside-the-box-implicit-chain-transformer

## 6. 校准日志

- 2026-09-08：v0.1 数值同步。① 篇幅行全表改按当前单篇 JSON 重算的 word_count/cjk_chars median：Cerebras 2,036→1,313、EleutherAI 4,673→2,772、Databricks 4,199→2,076、OpenAI 2,819→3,164、Anthropic 2,622→2,640、壳中客（v10）3,905→4,830 字；② OpenAI/Anthropic 两列系 v2 重采口径——OpenAI：平均句长 22.2→22.3、数字密度 16.1→20.7、精确数字 1.1→0.92、限定语 8.8→9.57、断言绝对化 1.6→1.76、第一人称 59→53、客观自指 0.5→1.0、TTR 0.31→0.33、MATTR 待重算‡→0.68；Anthropic：数字密度 7.4→8.25、精确数字 1.6→1.46、限定语 9.6→10.52、断言绝对化 2.1→2.32、第一人称 42.5→30、客观自指 2.0→1.5、TTR 0.35→0.34、MATTR 待重算‡→0.69（‡ 注记随之删除，TTR 长度敏感提示保留）；③ Cerebras/EleutherAI/Databricks/壳中客（v10）四列其余数值逐格与 _aggregate.json 复核一致，无漂移；指纹行 p/q 与 output/_group-discrimination.txt 一致（平均段长最低，q=0.001 过 FDR）。
- 2026-09-14：两层口径复核（discriminate.py 体裁对体裁改造，报告见 output/_group-discrimination.txt 末节新旧对照）。旧指纹"平均段长最低"体裁构成校正后未过 FDR（N 格内 p=0.021，q=0.351），按纪律保留原行并加构成成分注记；新口径最显著信号为数字密度高 @N格（42.45 vs 同格 pooled 28.2，p=0.009，q=0.311，探索性，待扩容复验）。
- 2026-09-15：扩容重聚合（Phase B1）。语料 10→20 篇（2026-09-14 体裁平衡扩容，新篇 router=llm-routing-v2-expansion；旧 JSON 未重跑，genre.unified 不受影响）。顶层重算（profiler.aggregate()，等价性双验证通过），§2 表刷新：篇幅 1,313→1,199.5、句长 18.8→17.95、数字密度 40.1→33.68、精确数字 3.1→3.09、限定语 7.9→5.54、第一人称 10.5→9.0、客观自指 0.5→0.0、TTR 0.42→0.43、MATTR 0.70→0.71；断言 1.82 不变；其余五列同步扩容后口径（壳中客列保持 v10）。two_level：A3/N3 → A5/E3/G4/N4/R4（新增 E/G/R 格）。discriminate（FDR 族分列口径不变）：最显著信号由数字密度高 @N格（q=0.311）换位平均段长低 @A格（29.4 vs pooled 50.8，p=0.002，q=0.143）——旧口径指纹"段长最低"在新口径 A 格（n=5）重新居首，仍未过 FDR；旧口径对照保持段长最低（q<0.001，仅对照）。