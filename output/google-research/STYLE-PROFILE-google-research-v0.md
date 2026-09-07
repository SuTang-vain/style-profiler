# 《Google Research Blog》风格档案 v0（机器版）

> 生成日期：2026-09-07 ｜ 语料：10 篇（2026-08 至 2026-09，research.google/blog 栏目分层采样）｜ 抓取：Kimi WebBridge 真实浏览器
> 语料路径：corpus/google-research/ ｜ 统计：output/google-research/
> ⚠️ 机器初稿：定量结论可信；定性综合待人工裁决。

## 1. 风格画像

**机构科学家的"应用研究叙事"**：研究覆盖从基因组预测、果蝇脑连接组到甲烷监测——题材跨学科，但骨架统一：动机（科学问题）→ 方法（模型/管线）→ 量化评估 → 开放展望。命名制双作者署名（"Ayush Jain and Rajat Sen, Research Scientists"）。与 OpenAI 的侦探叙事不同，这里没有"失败→反转"的戏剧弧——是"问题→方案→验证"的正向推进。
⚑ 例证："What if pathology foundation models could do more with less?"（GigaPath——设问式动机开场）

## 2. 量化基线（10 篇，median）· 七库对照表

| 指标 | Cerebras | Eleuther | Databricks | OpenAI | Anthropic | **GoogleRes** | MSR |
|---|---|---|---|---|---|---|---|
| 篇幅（词） | 1,313 | 2,772 | 2,076 | 2,819 | 2,622 | **1,462** | 1,673 |
| 平均句长 | 18.8 | 25.7 | 26.1 | 22.1 | 22.4 | 22.9 | 22.8 |
| 数字密度 /千词 | 40.1 | 44.1 | 24.4 | 16.1 | 7.4 | 19.7 | 26.6 |
| 精确数字 /千词 | 3.1 | 14.1 | 4.0 | 1.1 | 1.6 | 5.6 | 7.3 |
| 限定语 /千词 | 7.9 | 10.6 | 5.5 | 8.8 | 9.6 | **4.4** | 7.4 |
| MATTR(150) | 0.71 | **0.65** | 0.72 | † | † | 0.73 | 0.70 |
| 第一人称 | 10.5 | 61.5 | 21.5 | 59.0 | 42.5 | 19.5 | 9.0 |
| 年份锚点 /千词 | 2.0 | 1.2 | 0.5 | 2.0 | 0.3 | 1.0 | 0.9 |
| 感叹号 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

† OpenAI/Anthropic 正文不入库，MATTR 待重采后补。
> 指纹（discriminate.py，vs 余六库 pooled）：**限定语最低**（4.4 vs 库群 ~7.9，p=0.005，q=0.005，过 FDR）——跨库最"少声明"的稳健叙述，与 Anthropic 的高限定语（9.6）形成两极。

## 3. 结构信号（抽样观察，待全量标注）

- 开场：设问或动机句直入（"What if..." / 科学问题），无场景 HOOK；
- 论证：模型/方法 → 基准对比 → 消融或案例；几乎无 COUNTER；
- 收尾：展望/局限声明（"unclear if this is a robust relationship" 式）；
- **应用科学混合体**：健康/气候/神经科学题材占 6/10——"研究机构输出科学发现"而非纯 AI 博客。

## 4. 待人工裁决项

- ⚑ 与壳中客"探索体"的对照：行星预测引擎/GlucoFM 等"模型+科学应用"文是否构成英文"应用报告体"；
- 语步全量标注未做（推荐 connectomics 篇——合作科学体代表）；
- "机构合作科学体"（institutional-collaboration-science）信号在本库最强，是否升为 rubric 00 英文子体裁待定。

## 5. 语料清单

transfer-learning-genomic-prediction / connectomics-fruit-fly / methane-emissions / timesfm-3 / planetary-prediction-engine / glucofm / agenthands / biomarkers-wearable / mobility-place / empty-shelves-recall