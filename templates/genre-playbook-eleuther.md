# EleutherAI Blog · 撰写引导 playbook v0（初稿）

> 2026-09-08 初稿。来源：output/eleuther/_aggregate.json（统计层）+ rubric 01 标注 3 篇（mad_research_update_2 / autointerp / common-pile，共 159 段）+ STYLE-PROFILE-eleuther-v0.md（散文，仅作推断依据）。
> 用途：回答"要写一篇符合该库风格的文章，具体怎么写"。与《EleutherAI Blog 风格档案 v0》配套；凡本文件与 output/ 下 JSON 冲突，以 JSON 为准。
> 证据分级约定：[统计层]=全库 10 篇定量，可信；[标注-3篇]=3 篇语步标注聚合（output/eleuther/annotations/ 与 output/_moves-aggregate.md）；[推断]=仅档案散文支持，待标注验证。

## 1. 体裁路由特征（候选子体裁，全部待裁决）

[推断]（规则层 10 篇全部判为 blog_or_exploration，未分子体裁；下表从档案与 3 篇标注归纳，**路由规则未裁决，写作前须先由人确认目标子体裁**）

| 候选子体裁 | 识别特征 | 代表篇目 | 状态 |
|---|---|---|---|
| **research-report 进度报告体** | 自报进度开场（"This is a short update on progress"）；结果前置含负面结果；图注段为论证主体；边界声明+"去优先级"收束 | mad_research_update_2, tyche-poser-comparison | [标注-1篇] 支撑，候选命名待裁决（档案 §4） |
| **paper-companion 论文伴随体** | "Announcing X" 宣告；多作者署名；摘要式要点预告；多级小节复述论文方法/实验；文末 bibtex 引用块 | autointerp, deep-ignorance | [标注-1篇] 支撑（98 段），待裁决 |
| **release-announcement 发布宣告体** | "Today we are excited to announce" 开场；版本号（v0.1）；合作机构清单；质疑-回应单元（COUNTER）；版本声明收束 | common-pile | [标注-1篇] 支撑（22 段），待裁决 |
| **theory-construction 理论建构体** | 概念自造并数学化（dynamical model）；参数扫描+模拟抽数；图注重现性声明（"figures exactly reproducible"） | dynamical-models-of-ai-governability | 未标注，档案散文提示，待裁决 |

> 注意：档案已实证 mad_research_update_2 **不是**探索体（无概念自造、无版本号）；探索体信号应到 dynamical-models 验证（档案 §4 待裁决项）。不要拿 rubric 00 的中文探索体模板直接套英文理论文。

## 2. 通用语步骨架

[标注-3篇]（3 篇聚合：ARGUE 83%、COUNTER 1 处、HOOK 0、APPLY 4 处、叙事段 0%——六库中最纯论证文体）

```
无 HOOK：直入成果、问题或进度声明（"This is a short update on progress"）
→ FRAME（成果/发现前置预告，可含负面结果："results are discouraging for our MAD"）
→ CONTEXT（领域背景/实验设计/引用背景，少量：3 篇合计仅 ~10 段）
→ ARGUE×n（绝对主体：方法→结果→图注循环；图注段可占全篇 1/3）
   · COUNTER 可选且至多一处：仅发布宣告体出现质疑-回应单元
   （"A common concern raised" → "matches the performance"）
→ APPLY（可选：代码/工具/数据落点，如 GitHub 仓库链接；APPLY 密度低于 MSR）
→ CLOSE（两种收束形态见 §5）
```

执行要点：
- **零叙事**：不要写"我们发现……这让我们想起……"式调查叙事；narrative_ratio 全 0。叙事腔是本库最大禁忌。
- **负面结果不藏**：进度报告体以"未获得有希望的结果+去优先级"收束是合法且典型的写法。
- **图是论证主体**：写正文时把图注段当一等公民规划，文本是图的注释，不是反过来。

## 3. 定量预算表

[统计层]（全部抄自 output/eleuther/_aggregate.json；⚠️ 篇幅一项 _aggregate.json 缺 word_count 字段，取自 output/eleuther/ 单篇 JSON 汇总，口径同为统计层）

| 指标 | median | P25–P75 | 写作预算 |
|---|---|---|---|
| 篇幅（词） | 2,771.5 | 1,799–5,328 | 目标 2,000–5,000 词；低于 1,000 或高于 10,000 需有明确体裁理由 |
| 阅读时长（分钟） | 9.0 | 7–17 | 与篇幅联动 |
| 平均句长（词） | 25.7 | 19.1–26.7 | 长句为主，允许 25+ 词的复合句；P90 句长 median 44.5，不必切碎技术长句 |
| 平均段长（词） | 52.5 | 46.2–62.2 | 短段节拍：一段一个论点/一张图 |
| 数字密度 /千词 | 44.1 | 37.5–52.7 | 每千词约 44 个数字 token——每段至少出现可量化内容 |
| 精确数字 /千词 | 14.1 | 9.3–28.3 | **六库最高**：定性判断必须配具体测量值（精确到小数/具体规模数） |
| 年份锚点 /千词 | 1.18 | 0.82–5.05 | 少量时间锚定即可 |
| 外链 /千词 | 0 | 0–0 | 零外链（正文不贴外部链接；代码落点走 APPLY 段的仓库地址） |
| 引用标记 / 文献条目 | 0 | 0–0（max 2） | 不做学术式文内引用；论文伴随体用文末 bibtex 块代替 |
| 限定语 /千词 | 10.61 | 7.9–11.9 | 限定语密度高：seems/appears/unclear/may 常备 |
| 断言绝对化 /千词 | 1.2 | 1.0–2.1 | 压低绝对化断言（never/always/clearly 少用） |
| 全称量词 /千词 | 6.17 | 5.0–7.4 | all/every 类允许中等密度 |
| 第一人称（次/篇） | 61.5 | 39–100 | 高频 "we"——研究共同体口吻，不是侦探叙事主体 |
| 客观自指（this paper 等） | 1.5 | 0–3 | 极少自我指涉 |
| 感叹号 | 0 | 0–1 | 禁用或至多 1 个（发布宣告体开场可用） |
| 问句 | 1.0 | 0–5 | 极少设问；不要设问式 HOOK |
| TTR / MATTR | 0.26 / 0.65 | — / 0.61–0.67 | 术语循环复用是文体成分：核心术语全文重复，不刻意换同义词 |

## 4. 操作化模式（该库特有固定招式）

[统计层]+[标注-3篇]

1. **精确数字癖** [统计层]：每个定性判断配一个具体测量。精确数字 14.1/千词，是 OpenAI 的 13 倍（档案 §1，与 JSON 一致）。写法：不说"performance dropped significantly"，写"AUC dropped to X at layer Y"。
2. **图注即论证** [标注-3篇]：mad_research_update_2 图注段 13 处占标注段 1/3；autointerp 图注/表格段遍布全文。写法：图注段写满"图里看什么、轴是什么、结论是什么"，如 "clear s-shaped relationship"（mad_research_update_2 P34）。
3. **结果前置含负面** [标注-3篇]：开篇摘要段直接给结果，包括坏消息："results are discouraging for our MAD"（P5）。
4. **边界声明内置** [标注-3篇]：论证中段主动声明稳健性边界："unclear if this is a robust relationship"（P38）。限定语 10.6/千词的统计预算是它的支撑。
5. **版本号宣告** [标注-1篇·common-pile]：发布体用版本号表达意图："a very clear statement of intent"（Common Pile v0.1）。
6. **代码落点** [标注-3篇]：APPLY 段给仓库/工具地址："github.com/EleutherAI/sae-auto-interp"（autointerp P8）。
7. **bibtex 收尾块** [推断]：论文伴随体文末附 Citation Information + bibtex（common-pile、deep-ignorance 均有），替代文内引用。

## 5. 收尾形态与正反例

[标注-3篇]（CLOSE 仅 2 篇有显式标注；autointerp 以附录注收尾，无 CLOSE 段——"可弱收尾"本身是该库特征）

**形态 A · 负面收束+去优先级**（进度报告体）
> 正例："We are deprioritising work on MAD"（mad_research_update_2）
> 结构：承认结果不佳 → 归因但声明未完全解释 → 宣布去优先级 → 留重启条件（"may revisit"）

**形态 B · 版本声明收束**（发布宣告体）
> 正例："the first step not the last step"（common-pile）
> 结构：版本号意图声明 → 下一步清单（bigger versions / unlock data）

**形态 C · 附录+bibtex 收尾**（论文伴随体）
> 正例：autointerp 以附录方法注结束，无总结段；deep-ignorance 以 bibtex 块结束。

**反例（不要这样收尾）**：
- 格言化教训收束（"X is not just about A—it's about B"）——那是 OpenAI 招式，本库 CLOSE 不含格言。
- 制度化承诺/营销呼吁——零感叹号统计预算下，兴奋语气只能出现在发布体开场一句。
- 故事回扣式收尾——零叙事纪律贯穿到结尾。

## 6. 就绪度评估

**结论：部分能。** 统计层完备且可信（10 篇全量），通用骨架与定量预算可直接指导写作；但子体裁路由未裁决，按子体裁写作前必须先人工确认 §1 的目标体裁。

**缺口清单**：
1. 标注覆盖 3/10 篇；theory-construction 候选子体裁（dynamical-models 等）完全未标注，其骨架目前只有档案散文支持。
2. 子体裁路由规则未裁决（档案 §4 悬置项），rubric 00 尚无英文子体裁扩展，"research-report" 命名仅为档案建议。
3. _aggregate.json 缺 word_count 字段，篇幅预算只能从单篇 JSON 汇总；聚合脚本应补此项。
4. rubric 02（论证标注）对 eleuther 零覆盖，论证层模式（如质疑-回应单元的内部结构）无依据。
5. 档案第 2 节"篇幅 4,673 词"与统计层（median 2,771.5）冲突——档案散文数值不可直接引用（详见冲突记录，本文件预算表已全部改用 JSON 口径）。

**最小补全动作**：
1. 补标 dynamical-models-of-ai-governability（rubric 01），裁决 theory-construction 子体裁并更新 §1；
2. profiler 聚合脚本补 word_count 进 _aggregate.json；
3. 人工修正档案 §2 篇幅数值（2,771.5）并重跑 check_profiles.py。
