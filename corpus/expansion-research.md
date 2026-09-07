# 语料扩展调研 · AI 研究机构博客候选库（2026-09）

> 调研日期：2026-09-07 ｜ 方法：Exa 搜索 + 博客索引页抽取（各站当前头条与栏目结构）
> 目的：把 style-profiler 的英文语料从 OpenAI/Anthropic 两家扩展为多机构对照库，回答"哪些机构的文体与现有五体裁/四子体裁系统适配、如何分期入库"。

## 一、结论速览

| 梯队 | 机构 | 频道 | 体裁适配（对照 OpenAI 四子体裁） | 适配度 |
|---|---|---|---|---|
| **一期** | Cerebras | cerebras.ai/blog | research-narrative × evaluation-report（论文复述 + TL;DR） | ★★★★ |
| **一期** | EleutherAI | blog.eleuther.ai + papers-blog | research-narrative + **research-update（探索体英文版，新信号）** | ★★★★ |
| **一期** | Databricks AI Research | databricks.com/blog AI Research 栏目 | engineering-deep-dive（reasoning/内核/系统） | ★★★☆ |
| **二期** | Google Research | research.google/blog（非 deepmind 产品流） | research-narrative + **机构合作科学体（新信号）** | ★★★☆ |
| **二期** | Microsoft Research | microsoft.com/research/blog | research-narrative（署名作者 + 工具研究） | ★★★☆ |
| **三期** | Meta AI Research | research.meta.ai/blog | research-narrative（Muse 系列） | ★★★ |
| **三期** | Mistral | mistral.ai/news | 产品公告为主，少数研究深潜（Magistral） | ★★☆ |
| **三期** | xAI | x.ai/news | 产品发布为主，偶有深潜（Grok Bot 设计） | ★★ |
| 不采 | NVIDIA Technical Blog | developer.nvidia.com/blog | 平台集成/性能基准文，论证结构弱 | ★ |
| 不采 | Apple ML Research | machinelearning.apple.com | **纯论文索引，无 prose 博客** | ✖ |

## 二、候选机构证据（各站 2026-08/09 当前内容）

### Cerebras ★★★★
研究论文式博客，最新文章即划入本库的体裁：
- [Thinking Inside the Box: The Implicit Chain Transformer for Efficient State Tracking](https://www.cerebras.ai/blog/thinking-inside-the-box-the-implicit-chain-transformer-for-efficient-state-tracking)（2025-12，研究叙述）
- [REAP: One-Shot Pruning for Trillion-Parameter Mixture-of-Experts Models](https://www.cerebras.ai/blog/reap)（2025-10，**TL;DR 开头** + 方法 + 结果——evaluation-report 骨架）
- [Compressing KV cache memory by half with sparse attention](https://www.cerebras.ai/blog/compressing-kv-cache-memory-by-half-with-sparse-attention)（2025-03）

特征：自产证据、性能数字、无外部引用依赖——与 OpenAI research-narrative/evaluation-report 同构。

### EleutherAI ★★★★
非营利开源研究社区（与壳中客的"社区研究"家世同构）：
- [Alignment Research @ EleutherAI](https://blog.eleuther.ai/alignment-eleuther/) —— 社区定位自述
- [Automatically Interpreting Millions of Features in Large Language Models](https://www.eleuther.ai/papers-blog/automatically-interpreting-millions-of-features-in-large-language-models)（论文博客）
- [A Dynamical Model of AI Governability](https://blog.eleuther.ai/dynamical-models-of-ai-governability/)（理论建构——探索体）
- [Mechanistic Anomaly Detection Research Update 2](https://blog.eleuther.ai/mad_research_update_2/)（**"Interim report on ongoing work"——研究进行时更新，英语里罕见的探索体原生产物**）

### Databricks AI Research ★★★☆
- [AI Research 栏目页](https://www.databricks.com/blog/category/databricks-ai/ai-research)：reasoning in practice、并行 test-time search
- [Achieving Extreme Efficiency through Specialized GPU Kernel Generation](https://www.databricks.com/blog/achieving-extreme-efficiency-through-specialized-gpu-kernel-generation)

定位：工程系统 + 评测混合；偏 engineering-deep-dive，说教性弱于 OpenAI，数字密度高。

### Google Research ★★★☆（二期）
机构合作 + 应用科学发现是独有信号：
- [TimesFM-3: A zero-shot foundation model for multivariate forecasting](https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/)
- [A connectomics milestone: Mapping the complete male fruit fly brain](https://research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/)（与 HHMI Janelia 合作，作者署名双人制）
- [Mapping global methane emissions from space with deep learning](https://research.google/blog/mapping-global-methane-emissions-from-space-with-deep-learning/)

注意分流：blog.google 的 Google DeepMind 流（WeatherNext 3 等）混入大量产品新闻，采 research.google/blog 栏目即可。署名 byline（"Vishal Batchu, Research Engineer"）是期刊体元素的英语残留——潜在新体裁信号。

### Microsoft Research ★★★☆（二期）
- [Data Formulator 0.7: AI-powered data analytics for enterprise data](https://www.microsoft.com/en-us/research/blog/)（署名 Chenglong Wang 等 4 人——论文作者制博客）

### Meta AI Research ★★★（三期）
- [Introducing Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe)（research.meta.ai/blog；ai.meta.com/blog 更产品化，Brain2Qwerty 等为 brain-computer 叙事）

### Mistral ★★☆（三期）
mistral.ai/news 以主权 AI 基础设施/产品公告为主流；Magistral 推理模型文（[arXiv 2506.10910](https://arxiv.org/pdf/2506.10910)）为研究向——采样需严格筛选。

### xAI ★★（三期）
x.ai/news 以 Grok 产品发布为主（Grok Bot、Grok 4.6）；[Designing Grok Bot for a world of persistent agents](https://x.ai/news) 类属于可采的 engineering-deep-dive 少数派。

### 不采理由
- **NVIDIA Technical Blog**：平台集成/性能调优导向，读者契约是开发者而非研究同行，论证组件稀疏（基准数字即结论），会稀释跨库档案的"研究文体"纯度。
- **Apple ML Research**：`machinelearning.apple.com/research` 是纯论文索引（按 venue/领域筛选），无 prose 长文——与 profiler 的文体单元不匹配，除非未来做"论文 → 博客文体"对照实验。

## 三、对现有体裁系统的新信号（rubric 00 扩展候选）

1. **community-research-update（社区研究更新）**：EleutherAI 的 MAD Research Update 2 是"进行中研究的阶段报告"——对应中文"探索体"的英文原生形态。OpenAI 四子体裁没有此档，建议升为英文第五子体裁。
2. **institutional-collaboration-science（机构合作科学）**：Google Research 的 connectomics/methane、MSR 的署名四作者——署名制度 + 跨机构合作 + 方法/发现双线，介于 research-narrative 与学术期刊体之间，可作英文"报告体"参照系。
3. **体裁纯度分层**：Google DeepMind 的 blog.google 流 ≈ 产品新闻混杂（对应壳中客"投稿"位），提示多机构语料应**按栏目分层采样**（research.google/blog 而非 blog.google），否则混体裁洗信号——与 rubric 00 纪律 2 一致。

## 四、分期入库建议

```
一期（3 机构 × 10 篇，高适配、快产出）
  食料：Cerebras 10 + EleutherAI 10 + Databricks 10
  产出：corpus/{cerebras,eleuther,databricks}/ + profiler.py 统计
       + 每库 1 份档案；跨库基线表扩为 5 栏（+OpenAI/Anthropic）
二期（2 机构 × 10 篇）
  Google Research（research.google/blog 栏目内采样，含 1 篇合作科学体）
  Microsoft Research
  产出：新增 2 档案 + rubric 00 增加英文第五子体裁（community-research-update）
三期（可选，各 10 篇）
  Meta AI Research / Mistral / xAI（严格筛选）——对照"产品化研究文体"光谱
```

入库纪律沿用现有约定：
- **版权**：全文不入库。每机构在 `corpus/README.md` 记 slug 清单 + 采集方式（与 openai/anthropic 同款），分析产出保留在 `output/`。
- **抓取**：Cloudflare 验证壳的站点（Cerebras/Databricks 需实测）优先浏览器工具；失败记录跳过。
- **分体裁**：一期三家若混入纯产品公告，按 rubric 00 confidence=low 单独分组。

## 五、预期增量价值（对照现有档案的缺口）

- OpenAI 档案"零引用、自产证据、侦探叙事"与 Anthropic"诚实边界声明、情景剧论证"已形成两极；**Cerebras/Eleuther 补"论文复述派"与"社区研究派"两个新极**，跨库光谱从 2 个风格点扩为 5 个。
- EleutherAI 的 research-update 直接为模式二（发布自检）提供"探索体英文档"基线——目前探索体只有中文基线。
- Google Research 的合作科学体为"标题冒号双段式"等现有维度提供机构级对照（期刊体元素在英语博客中的残留程度可测）。

## 来源

- 搜索产出（Exa）：
  - /tmp/exa-emerging.json（Cerebras/Databricks/Mistral）
  - /tmp/exa-safety.json（EleutherAI/CAIS）
  - /tmp/exa-toplabs.json（Google/Meta）
- 博客索引页抽取（Exa extract）：
  - deepmind.google/discover/blog、ai.meta.com/blog、mistral.ai/news、research.google/blog
  - microsoft.com/en-us/research/blog、developer.nvidia.com/blog、machinelearning.apple.com/research、x.ai/news

Sources:

- [Cerebras Blog](https://www.cerebras.ai/blog)（2025-03 ~ 2025-12 样本）
- [EleutherAI Blog](https://blog.eleuther.ai/) 与 [Papers-blog](https://www.eleuther.ai/papers-blog)
- [Databricks AI Research 栏目](https://www.databricks.com/blog/category/databricks-ai/ai-research)
- [Google Research Blog](https://research.google/blog/) 与 [Google DeepMind News](https://deepmind.google/discover/blog/)
- [Meta AI Research Blog](https://research.meta.ai/blog)
- [Microsoft Research Blog](https://www.microsoft.com/en-us/research/blog/)（Data Formulator 0.7）
- [Mistral News](https://mistral.ai/news/) 与 [Magistral 论文](https://arxiv.org/pdf/2506.10910)
- [xAI News](https://x.ai/news)（Grok Bot / Grok 4.6）
- [NVIDIA Technical Blog](https://developer.nvidia.com/blog)
- [Apple Machine Learning Research](https://machinelearning.apple.com/research)