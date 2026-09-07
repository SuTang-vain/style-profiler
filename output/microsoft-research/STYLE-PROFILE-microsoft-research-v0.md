# 《Microsoft Research Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2026-06 至 2026-08，research blog 分层采样）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/microsoft-research/ ｜ 统计：output/microsoft-research/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**企业研究院的"集体署名工具文"**：多人署名（4-6 位，含 title：Principal Research Manager / Technical Fellow）比 Google 更重；内容以**工具/系统**为核心（Orchard 框架、Echoverse、CARE-X、Flint 语言），每题 = 动机 → 系统设计 → 评测 → 开放生态落点。七库对比下最鲜明特征：**第一人称最低（8.5）**——几乎没有 "we did" 的叙事主体，转为机构化陈述；篇幅最长（5,660 词）。
⚑ 例证："Orchard: An open framework for scalable agentic AI"——系统名即标题，工具即内容。

## 2. 量化基线（10 篇，median）· 七库对照表

| 指标 | Cerebras | Eleuther | Databricks | OpenAI | Anthropic | GoogleRes | **MSR** |
|---|---|---|---|---|---|---|---|
| 篇幅（词） | 1,313 | 2,772 | 2,076 | 2,819 | 2,622 | 1,462 | **1,673** |
| 平均句长 | 18.8 | 25.7 | 26.1 | 22.1 | 22.4 | 22.9 | 22.8 |
| 数字密度 /千词 | 40.1 | 44.1 | 24.4 | 16.1 | 7.4 | 19.7 | 26.6 |
| 精确数字 /千词 | 3.1 | 14.1 | 4.0 | 1.1 | 1.6 | 5.6 | 7.3 |
| 限定语 /千词 | 7.9 | 10.6 | 5.5 | 8.8 | 9.6 | 4.4 | 7.4 |
| MATTR(150) | 0.71 | **0.65** | 0.72 | † | † | 0.73 | 0.70 |
| 第一人称 | 10.5 | 61.5 | 21.5 | 59.0 | 42.5 | 19.5 | **9.0** |
| 年份锚点 /千词 | 2.0 | 1.2 | 0.5 | 2.0 | 0.3 | 1.0 | 0.9 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

† OpenAI/Anthropic 正文不入库，MATTR 待重采后补。
> 指纹（discriminate.py，vs 余六库 pooled）：**第一人称最低**（9.0 vs 库群 ~26，p=0.002，q=0.002，过 FDR）——七库中最"无我"的研究文体；Cerebras（10.5）同处低段，但机制不同（Cerebras 是营销型第三人称，MSR 是机构化陈述）。

## 3. 结构信号（抽样观察，待全量标注）

- 开场：直接进入系统动机，无叙事弧；
- 论证：自建工具 + 评测（含医学/安全领域评测）；COUNTER 罕见；
- 收尾：开放生态/未来方向（"Learn more" 连接论文与开源）；
- 特色：**每篇都配论文/开源链接**（tech report 外链在正文内），但 innerText 提取抹平链接——档案外链指标失真需注意。

## 4. 待人工裁决项

- ⚑ 与 Databricks"工程化评测派"的亲缘：MSR 更偏系统、Databricks 更偏基准——需 rubric 00 定夺是否同族分叉；
- 语步全量标注未做（推荐 Orchard 篇）；
- "集体署名"是否应记入 rubric 02 的 source_tier（机构信用 vs 个人信用层）。

## 5. 语料清单

gigapath-flash / skala / mindtopo / care-x / orchard / echoverse / evolib / symcrypt-rust / aurora-1-5 / flint