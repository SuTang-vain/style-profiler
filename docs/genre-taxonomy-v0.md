# 统一体裁分类法 v0（草案，2026-09-14）

> 目的：为"两层风格模型"（机构主导风格 + 体裁层 delta，见 docs/methodology-two-level-style-model.md）提供跨机构通约的体裁标签。
> 现状问题：中文库（kezhongke）有五体裁标签；6 个英文库的 per-article JSON 全部停留在兜底标签 `blog_or_exploration`（规则层关键词为中文，英文路由从未真正运行）。
> 本文是草案：**分类轴与映射规则需主编裁决**，逐篇归属由后续 LLM 路由 passe 确认（低置信进人工）。

## 一、分类轴

先按**交际目的**分（不是按形式分——形式是结果）：

| 代码 | 体裁 | 交际目的 | 典型形态 |
|---|---|---|---|
| **A** | 分析评论类 | 对现象/趋势/文本做论证性解读 | 行业分析、深度解读、观点评论、概念探索 |
| **E** | 工程类 | 记录"我们如何构建/修复/运维" | build-log、postmortem、工具链复盘 |
| **R** | 研究类 | 报告实验/评测/研究发现 | 对齐研究、基准结果、论文式报告 |
| **N** | 公告类 | 宣布新产品/模型/里程碑 | 发布文、性能发布、数据集发布 |
| **P** | 政策类 | 陈述规范/政策/立场 | 安全政策、模型行为规范 |
| **G** | 指南类 | 教读者怎么做 | 最佳实践、教程、方法清单 |

判定规则（优先级自上而下）：
1. 含政策/规范主体（model spec、RSP）→ **P**
2. 以发布为目的（新模型/产品/数据集/里程碑，含性能表与可用性声明）→ **N**
3. 以实验发现为主体（有方法+结果+解读）→ **R**
4. 以构建过程为主体（How we built X、故障复盘）→ **E**
5. 以教会读者操作为主体（best practices、how-to 清单）→ **G**
6. 以上皆非，以论证性解读为主体 → **A**

混合体裁取**主导目的**；主导目的不明标 low-confidence 进人工。

## 二、现有标签 → 统一标签映射

**kezhongke（中文五体裁）**：

| 原标签 | 映射 | 理由 | 状态 |
|---|---|---|---|
| 期刊体 | R | 论文式研究发现 | 直接 |
| 报告体 | **N** | 模型发布核验报告（元信息头+性能+附录），交际目的是发布告知 | **待主编裁决**（备选 R：其评测内容有研究属性） |
| 行业分析 | A | 论证性行业解读 | 直接 |
| 博客体 | A | 评论/分析随笔 | 直接 |
| 探索体 | A | 概念建模探索，分析的子型 | **待主编裁决**（备选：单列"探索体"） |
| blog_or_exploration（投稿 4 篇） | 待裁决 | 官方 section 未覆盖 | LLM 路由复核 |

**英文六库**：无既有标签，逐篇初判如下（依据标题+playbook 标注史，全部待 LLM 路由确认）：

| 库 | A | E | R | N | P | G |
|---|---|---|---|---|---|---|
| cerebras | economics-of-ai-reasoning | autoresearch-loop-cheating、knowledge-base、multi-agent-workflows、never-loop-without-verifiers、latency-debt | thinking-inside-the-box | gpt-5-6-sol、hot-chips-2026、exomebench | — | — |
| openai | understanding-source（？） | core-dump、harness-engineering、unrolling-codex-agent-loop | emergent-misalignment、gdpval、gpt-5-safe-completions、monitor-coding-agents、reasoning-models-cot | — | our-approach-to-model-spec | — |
| anthropic | — | postmortem-three-issues、building-c-compiler、effective-harnesses | agentic-misalignment、alignment-faking、auditing-hidden-objectives | — | responsible-scaling-policy | building-effective-agents、demystifying-evals、effective-context-engineering |
| eleuther | deep-ignorance、dynamical-models-governability（？） | — | attention-probes、autointerp、reward-hacking-indicators、tyche-poser、generating-text-nl-simulate | common-pile（数据集发布）、mad_research_update_2（进展通报）、aletheia-retrospective（？） | — | — |
| databricks | — | scaling-small-llms-mps | 3x-faster-search、agentic-reasoning-practice、enhancing-agent-retrieval、memalign、memex、memory-scaling | officeqa-pro-v2、meet-karl、genie | — | — |
| google-research | — | — | 全部 10 篇倾向 R | （多数带发布性质，N/R 边界见下） | — | — |
| microsoft-research | — | orchard（框架）、verifying-rust-cryptography | aurora-1.5、echoverse、evolib、flint、gigapath-flash、mindtopo | broadening-access-skala、care-x | — | — |

（？）= 低置信，必须过 LLM 路由。

## 三、已暴露的结构性事实（先于任何统计）

1. **体裁构成各库悬殊**：eleuther ≈ 全 R、google-research ≈ 全 R/N、cerebras E 主导、anthropic 有 P 和 G 而 cerebras 没有——**全库聚合必然混入体裁构成差异**，两层模型不是可选项是必需品。
2. **R/N 边界是最大模糊带**：google/msr 的"研究里程碑发布"兼有研究发现与公告目的（按判定规则 2 vs 3 都可落）。倾向裁决：有明确产品可用性声明 → N，否则 → R。
3. **空格预警**：多库的 A/G/P 格为空或近空——空体裁格不参与跨机构比较，机构层聚合时该体裁中位缺席（而非计 0）。

## 四、裁决记录（2026-09-14，主编口头裁决"推进执行后续"→ 按文档倾向项定案）

1. **报告体 → N**。模型发布核验报告的交际目的是发布告知；其评测内容的研究属性由 R 格在跨库比较时吸收（R/N 边界规则同下）。
2. **探索体并入 A**。概念建模探索是论证性解读的子型，不单列。
3. **R/N 边界规则认可**：有明确产品/模型/数据集**可用性声明**（available、开放、下载、API 上线）→ N；仅为研究里程碑通报而无可用性声明 → R。
4. **六类定案，不加第七类**。当前 84 篇语料无访谈/对话类样本；将来出现再扩类并回填。

裁决后即进入 LLM 路由 passe：每库一个子代理按本分类法逐篇打标（genre + confidence + evidence），低置信进人工；kezhongke 已有五体裁标签走映射复核而非重判。
