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

## 五、LLM 路由 passe 结果（2026-09-14，router=llm-routing-v1，已全量回填 per-article JSON 的 genre.unified；扩容 passe 为 llm-routing-v2-expansion）

**分布总表**（2026-09-14 体裁平衡扩容后：英文库各 20 篇、kezhongke 全量 24 篇；括号内 v10 子集 10 篇构成不变；扩容前 v1 分布见 git 历史）：

| 库 | A | E | R | N | P | G |
|---|---|---|---|---|---|---|
| anthropic | 4 | 3 | 3 | 4 | 3 | 3 |
| cerebras | 5 | 3 | 4 | 4 | 0 | 4 |
| databricks | 0 | 4 | 7 | 6 | 0 | 3 |
| eleuther | 4 | 0 | 8 | 5 | 1 | 2 |
| google-research | 0 | 2 | 13 | 5 | 0 | 0 |
| kezhongke | 11 (5) | 2 (0) | 2 (2) | 5 (3) | 0 | 4 (0) |
| microsoft-research | 2 | 4 | 9 | 5 | 0 | 0 |
| openai | 3 | 4 | 4 | 5 | 3 | 1 |

**对 §二/§三 先验的两处结构性修正**：
1. **cerebras 不是 E 主导**——重判后 A3/N3 主导、E 仅 1 篇。先前"engineering 系"的印象来自标题风格而非交际目的。机构层聚合须按真实构成。
2. **kezhongke v10"五体裁各 2 篇"均衡已破**——glm-5-3-flash-analysis 由博客体改判 N（全文为发布核验报告，与报告体四篇同目的），v10 实际为 A5/N3/R2。旧五体裁标签来自线上 section 侧写，与全文内容在 6 篇上不符（详见 output/kezhongke/genre-labels.json 与本文 §二映射表的差异）。

**低置信边界条目（10 篇）处置**：逐条复核后**全部采纳路由判定**——它们均落在已裁决的边界规则上（R/N 看可用性声明、E/R 看实验发现是否为主体、A/G 看教学是否为主体），规则适用正确，不确定性来自体裁本身混合而非规则误用。清单：cerebras×3（autoresearch-loop-cheating→R、multi-agent-workflows→G、never-loop-without-verifiers→A）、databricks×2（memalign→N、scaling-small-llms-mps→R）、eleuther×3（deep-ignorance→R、aletheia-retrospective→R、dynamical-models→A）、google-research×1（connectomics-milestone→N）、microsoft-research×1（echoverse→R）、openai×1（monitor-coding-agents→R）、kezhongke×1（eval-harness-landscape→A）。若未来统计结论对某篇敏感，优先复查此清单。

**扩容 passe（2026-09-14，router=llm-routing-v2-expansion）**：7 个英文库各 +10 篇、kezhongke +1 篇（投稿 sub-6e00d207fee4 重新入库 → G）。新篇目按 §一裁决规则逐篇打标（genre + confidence），低置信条目并入各库 genre-labels.json 的 _meta.low_confidence 留档（处置惯例同 v1 清单）；旧篇目标签一律未动。扩容后空格大幅减少：anthropic/openai 六格全满，cerebras 新增 E/G/R 格，databricks 新增 E/G，eleuther 新增 A/N，msr 新增 E/A，google-research 新增 E。**仍空的格**（计数 0）：cerebras P；databricks A/P；eleuther E；google-research A/P/G；kezhongke P；microsoft-research P/G。**近空格**（n<3 不出格值）：eleuther P1/G2、google-research E2、msr A2、openai G1、kezhongke E2/R2。空格在跨机构比较中缺席处理（§三第 3 条），不计 0。

## 六、亚层分析：是否继续细分/分层（2026-09-15 裁决）

**结论：六类主轴不加分、第三统计层不建；对 4 个证据确凿的双峰格引入亚型软标签（非统计层），并立转正触发器。**

### 体检方法与证据

方法：对 8 库 31 个出值格（n≥3）× 8 个核心指标计算格内 IQR/中位比，初筛高内散格，再逐格看分布形态区分**噪音**与**结构**。

- **噪音类**（大多数初筛命中）：低计数指标（absolutist 中位 1–2 时 IQR 1–2 自然爆比率）与零中位指标——小样本计数噪声，非结构；databricks/R 篇幅（901→3426 渐变）、kezhongke/A 句长（26.9→44.2 渐变）等**连续分布无断点**也不是亚型。
- **结构类**（4 格真双峰，数据为逐篇实测值）：

| 格 | 双峰数据 | 亚型划分 |
|---|---|---|
| anthropic/N（篇幅） | 340/564 vs 2563/11950 词 | `milestone_brief` 里程碑简报 ×2 / `release_feature` 发布长文 ×2 |
| openai/A（数字密度） | 2.2/3.2 vs 35.1 /千词 | `position_essay` 立场随笔 ×2 / `data_trend_reading` 数据趋势解读 ×1 |
| eleuther/A（人称） | 10/24/27 vs 192 次 | `critique` 评论批评 ×3 / `concept_modeling` 概念建模 ×1（=探索体的英文原生型） |
| anthropic/E（人称） | 9/16 vs 69 次 | `engineering_deep_dive` 工程深潜 ×2 / `narrative_postmortem` 叙事复盘 ×1 |

### 不继续细分/分层的理由

1. **统计功效是瓶颈而非粒度**：扩容后 discriminate 指纹仍全未过 FDR（格内 n=3–8），再切一刀全部归零；细分方向与统计可行性直接冲突。
2. **两层模型已隔离最大混淆源**（体裁构成）；残余问题（指纹功效、量具漂移）非粒度能解。
3. 四个双峰格的亚型篇数均 1–2 篇，达不到 n≥3 出值线，建统计格无意义。

### 落地机制

1. **亚型软标签**：上表 14 篇的 per-article JSON 在 `genre.unified` 内加 `subtype` + `subtype_source` 字段（2026-09-15 已落）。聚合脚本（aggregate_two_level / discriminate）不读该字段，**零统计影响**；playbook 写作含义可引用亚型名作定性引导。
2. **转正触发器**：某亚型篇数 ≥6 **且**两亚型在 ≥1 个核心指标的中位差 > 合并格该指标 IQR 时，亚型升格为独立统计格（走与六类相同的 n≥3 出值、缺席不计 0 纪律）。
3. **定向扩容**：下轮采集优先补亚型（anthropic milestone_brief、openai data_trend_reading、eleuther concept_modeling、anthropic narrative_postmortem），把软标签喂到转正线。
4. **时间/量具轴**（databricks 网站改版先例）与**语言轴**（中英分列，discriminate 已执行）维持"校准注记"待遇，不建层。
