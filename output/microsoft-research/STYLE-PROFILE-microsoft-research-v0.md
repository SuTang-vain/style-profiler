# 《Microsoft Research Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2026-06 至 2026-08，research blog 分层采样）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/microsoft-research/ ｜ 统计：output/microsoft-research/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**企业研究院的"集体署名工具文"**：多人署名（4-6 位，含 title：Principal Research Manager / Technical Fellow）比 Google 更重；内容以**工具/系统**为核心（Orchard 框架、Echoverse、CARE-X、Flint 语言），每题 = 动机 → 系统设计 → 评测 → 开放生态落点。七库对比下最鲜明特征：**第一人称最低（9.0）**——几乎没有 "we did" 的叙事主体，转为机构化陈述；篇幅短小（median 1,634 词，七库第 5/7）——正文是摘要式短文，深度内容靠论文/开源外链承载。
⚑ 例证："Orchard: An open framework for scalable agentic AI"——系统名即标题，工具即内容。

## 2. 量化基线（10 篇，median）· 七库对照表

| 指标 | Cerebras | Eleuther | Databricks | OpenAI | Anthropic | GoogleRes | **MSR** |
|---|---|---|---|---|---|---|---|
| 篇幅（词） | 1,313 | 2,772 | 2,076 | 3,164 | 2,640 | 1,462 | **1,634** |
| 平均句长 | 18.8 | 25.7 | 26.1 | 22.3 | 22.4 | 22.9 | 22.6 |
| 数字密度 /千词 | 40.1 | 44.1 | 24.4 | 20.7 | 8.25 | 19.7 | 26.9 |
| 精确数字 /千词 | 3.1 | 14.1 | 4.0 | 0.92 | 1.46 | 5.6 | 7.5 |
| 限定语 /千词 | 7.9 | 10.6 | 5.5 | 9.6 | 10.52 | 4.4 | 7.5 |
| MATTR(150) | 0.70 | **0.65** | 0.71 | 0.68 | 0.69 | 0.73 | 0.70 |
| 第一人称 | 10.5 | 61.5 | 21.5 | 53.0 | 30.0 | 19.5 | **9.0** |
| 年份锚点 /千词 | 2.0 | 1.2 | 0.5 | 1.2 | 0.6 | 1.0 | 0.9 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

> 指纹（discriminate.py，vs 余六库 pooled）：**第一人称最低**（9.0 vs 库群 ~26，p=0.001，q=0.002，过 FDR）——七库中最"无我"的研究文体；Cerebras（10.5）同处低段，但机制不同（Cerebras 是营销型第三人称，MSR 是机构化陈述）。

## 3. 结构信号（rubric 01 全量标注：orchard 篇，33 段 → 24 标注）

- **语步骨架**：FRAME（摘要前置）→ CONTEXT×2 → ARGUE×7（方案/设计/架构）→ CONTEXT → ARGUE×3 → CONTEXT → ARGUE×6（三个子题各：需求→方法→结果）→ APPLY×3（含义+两条展望）
- 特征：**零叙事、零 COUNTER**——纯正向"动机→方案→评测→落点"；三个产品子题（SWE/GUI/Claw）严格同构嵌套，是系统文的标准模板；
- 每个子题 = CONTEXT（领域需求）+ ARGUE（训练方法→数字结果）**内聚成块**——与 Databricks 的固定骨架同族，但更系统化；
- **APPLY×3 是收尾三连**（环境层含义 + 经验复用 + 数据效率）——与 connectomics 的 APPLY（跨物种扩展）不同，此处是"框架级意义"陈述；
- 完整标注：`output/microsoft-research/annotations/orchard-an-open-framework-for-scalable-agentic-ai.moves.jsonl`

> **3 篇聚合（2026-09-08）**：echoverse + verifying-rust 补齐后 APPLY=8 处（六库最高）——资源链接落点（HF/技术报告/开源分支）是 MSR 指纹级结构特征；echoverse 含 4 处 COUNTER（预设质疑+回应）。详见 `output/_moves-aggregate.md`。

## 4. 待人工裁决项

- ⚑ 与 Databricks"工程化评测派"的亲缘：MSR 更偏系统、Databricks 更偏基准——orchard 语步实证：两者同属"系统文模板"（CONTEXT→ARGUE 块×n→APPLY），差异在落点（MSR 框架级意义 vs Databricks 基准宣称）；
- orchard 篇已全量语步标注（其余 9 篇待标）；
- "集体署名"是否应记入 rubric 02 的 source_tier（机构信用 vs 个人信用层）。

## 5. 语料清单

gigapath-flash / skala / mindtopo / care-x / orchard / echoverse / evolib / symcrypt-rust / aurora-1-5 / flint

## 6. 校准日志

- 2026-09-08：对照表全量同步当前统计层（output/<库>/ 单篇 JSON 与 _aggregate.json 实测 median）。① openai/anthropic 两列系 v2 重采口径：篇幅 2,819→3,164 / 2,622→2,640，第一人称 59.0→53.0 / 42.5→30.0，限定语 8.8→9.6 / 9.6→10.52，数字密度 16.1→20.7 / 7.4→8.25，精确数字 1.1→0.92 / 1.6→1.46，年份锚点 2.0→1.2 / 0.3→0.6，平均句长 22.1→22.3（openai），MATTR 待重算†→0.68 / 0.69 并删"正文不入库、待重采"注记；② 本库（MSR）篇幅 1,673→1,634（单篇 JSON word_count 重算中位数）；③ cerebras/databricks MATTR 0.71→0.70 / 0.72→0.71（旧值与现行 _aggregate.json 不符）；④ 指纹行 p/q 0.002/0.003→0.001/0.002——旧值与 output/_group-discrimination.txt（MSR：p=0.001，q=0.002）冲突，以统计层为准。
