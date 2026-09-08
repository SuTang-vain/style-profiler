# Google Research 博客 · 撰写引导 playbook 初稿

> 2026-09-08 初稿。语料：10 篇（corpus/google-research/）；统计：output/google-research/_aggregate.json 及逐篇 JSON；标注：annotations/ 3 篇 rubric 01 语步标注（connectomics 15 段 / empty-shelves 28 段 / timesfm-3 18 段，共 61 段）。
> 证据分级约定：[统计层] = _aggregate.json 全库数值；[标注-3篇] = 基于 3/10 篇语步标注聚合；[推断] = 仅档案散文或单篇观察支持。数值冲突时以 output/ JSON 为准。

## 一、体裁路由特征表（候选子体裁，⚑ 全部待裁决）

[标注-3篇] + [推断]：规则层 genre 路由将 10 篇全部判为 blog_or_exploration（即"未路由"），子体裁尚未经 rubric 00 裁决。以下候选从 3 篇标注骨架与档案散文归纳，写作前建议先按此分流，但分类边界待人工裁决。

| 候选子体裁 | 识别特征 | 代表篇目（已标注） | 待覆盖篇目 |
|---|---|---|---|
| **成果发布文**（模型/工具发布） | 首段 "We introduce X" 摘要前置；无 HOOK；方法→评测→可用性落点（GitHub/HF） | timesfm-3（18 段） | glucofm / biomarkers / agenthands / methane / planetary-engine |
| **诊断发现文**（框架+反直觉发现） | 设问 HOOK 开场；自造框架命名（knowledge profiling）；Takeaway 式思维转变收束 | empty-shelves（28 段） | mobility-place（待核） |
| **里程碑合作文**（机构联合成果） | 合作署名前置（"We partnered with HHMI Janelia"）；APPLY 为跨物种/领域推广轴；愿景 CLOSE | connectomics（15 段） | — |

⚑ 路由规则仅是归纳候选：3 篇标注恰好各占一个候选类，其余 7 篇归位全靠档案散文推断，须补标后裁决。

## 二、通用语步骨架

[标注-3篇]：3 篇聚合 61 段，ARGUE 占 72%，COUNTER 0 处，HOOK 1 处，APPLY 2 处，叙事段 4%。骨架：

```
[可选 HOOK：设问式动机开场——仅诊断发现文子类使用（1/3 篇）]
→ FRAME（成果声明/摘要前置："We introduce X"，第 1 段即给成果+一句话定义）
→ CONTEXT（领域背景 或 前代局限："Up until TimesFM-2.5..."）
→ ARGUE×n（主干 ≥70% 篇幅：方法拆解 → 量化评测 → 图注段充当证据；
            前人工作以 CONTEXT 小段穿插，不设独立综述节）
→ [可选 APPLY×1-2：推广轴（跨物种/跨领域"已经推广到 XX"）]
→ CLOSE（见第四节三种形态）
```

硬性排除项 [标注-3篇]：
- **零 COUNTER**：3/3 篇无任何反方观点、失败叙事或自我反驳节——不写 "However, critics argue..." 式段落；
- **零场景叙事**：叙事段仅 4%，无人物故事、无调查弧；
- **无 HOOK 是默认态**：3 篇中 2 篇直入成果，设问 HOOK 只在"发现反直觉"时使用。

## 三、定量预算表

[统计层]：全部抄自 output/google-research/_aggregate.json（篇幅一项 _aggregate.json 未收录，按同目录 10 篇逐篇 JSON 的 word_count 计算 median/P25/P75，口径与档案一致）。

| 指标 | median | P25–P75 | 写作指令 |
|---|---|---|---|
| 篇幅（词） | 1,462 | 1,301–1,643 | 目标 1,300–1,650 词；<1,167 或 >1,775 即出库域 |
| 阅读时间（分钟） | 5.0 | 4–6 | 与篇幅互为校验 |
| 平均句长（词） | 22.85 | 21.2–23.8 | 长句为主的学术博客腔，勿写成短句新闻体 |
| P90 句长（词） | 35.0 | 33–38 | 允许至多约 1/10 句子到 33–38 词（方法定义句） |
| 平均段长（词） | 40.65 | 36.6–44.0 | 段落短而密；单句段 median 0 次（max 1），不要用单句段做节拍器 |
| 数字密度 /千词 | 19.7 | 11.9–23.5 | 每千字约 12–24 个数字；低于 12 会显得"无证据" |
| 精确数字 /千词 | 5.59 | 2.0–8.5 | 成果声明必带规模数字锚定（"166,000 neurons"） |
| 年份锚点 /千词 | 0.96 | 0.62–1.68 | 约 1 个/千词（"Since the debut of TimesFM in 2024"） |
| 限定语 /千词 | 4.44 | 2.8–6.2 | **本库指纹：七库最低**。克制使用 may/might/suggest，直接陈述 |
| 绝对化语 /千词 | 1.41 | 0–2.4 | 低限定 ≠ 绝对化；"state-of-the-art" 级措辞可用但须挂基准 |
| 量化词 /千词 | 6.41 | 3.4–7.7 | multiple/several/across 类 |
| 第一人称（次/篇） | 19.5 | 11–22 | we/our 每篇 11–22 次，用于成果声明与推广，不用于感想 |
| 客观自称（次/篇） | 1.0 | 0–2 | "this work/the model" 少量 |
| 感叹号 | 0 | 0 | 禁用 |
| 疑问句 | 0 | 0–2 | 默认 0；仅诊断发现文可用设问（单篇 max 9，非常态） |
| 外链 / 参考文献 / 引用标记 | 0 | 0 | 正文零引用格式；论文只在散文中提名（"in 'Empty Shelves or Lost Keys?'..."） |
| MATTR(150) | 0.73 | 0.67–0.74 | 术语复用度高：固定术语反复出现，不要刻意换同义词 |

## 四、收尾形态与正反例

[标注-3篇]：三种已观测 CLOSE 形态，按子体裁选用：

1. **总结+资源落点**（成果发布文）：复述成果一句话 → 挂可用性。正例："now available on GitHub and Hugging Face"（timesfm-3）。
2. **Takeaway 思维转变**（诊断发现文）："Takeaway" 小节，把发现升格为方法论建议。正例（35 字）："precisely diagnose factual behavior"（empty-shelves）。
3. **愿景收束**（里程碑合作文）：成果定位为领域基础设施。正例："a foundational resource"（connectomics）。

[推断]（档案散文+未标注篇正文观察，待补标确认）：
4. **局限+下一步** 可能为第四种形态："pre-training population remains modest"（glucofm）——⚑ 仅 1 篇未标注语料支持，待裁决。

反例（本库不收的收尾）：
- 教训格言化（"X is not just about A—it's about B"）——OpenAI 指纹，本库 3 篇 0 例；
- 行动号召/营销语、感叹号——统计层感叹号 median 0；
- 独立"参考文献"节——reference_entries median 0。

## 五、操作化模式（本库固定招式）

[标注-3篇]（除注明外）：

1. **"We introduce X" 摘要前置**：第 1 段 = 成果 + 一句话定义 + 量化锚点，三段式压缩进一段。例证（22 字）："We introduce TimesFM-3"。10 篇中 9 篇首段即成果+定义式（"We introduce / X is a / We partnered / We evaluate and find"，[推断]：逐篇首段观察；[统计层] 旁证：第一人称 median 19.5 集中于成果声明）。
2. **命名+缩写制**：产物必命名并缩写——TimesFM-3 / ME-POIs / PPE / GlucoFM / WikiProfile；命名后全文用缩写复现（MATTR 0.73 的成因之一）。
3. **规模数字锚定**：成果声明句必挂量级数字。例证（31 字）："166,000 neurons and 125 million"。[统计层] 旁证：精确数字 median 5.59/千词。
4. **图注即论证**：图注段不是装饰，是 ARGUE 证据单元（connectomics 15 标注段中 4 段为图注）。写作时每张图配一段"读图结论"，让图注独立成立。
5. **前代局限对照**（成果发布文）：CONTEXT 用 "Up until X, our models were..." 给出前代边界，再以 "Today we introduce" 翻转——不承担失败叙事，只做能力边界对照。
6. **设问式动机**（仅诊断发现文）：HOOK 用二选一设问抛出反直觉问题。例证（40 字）："is it because they never learned them or"。⚑ 3 篇中仅 1 篇使用，非默认开场。
7. **推广轴 APPLY**：APPLY 不写成"教训"或"教程"，写成"已推广到 XX"（connectomics：鱼类→斑马鱼→脊椎动物）。
8. **署名元信息头**：正文前固定三行——日期；"Name and Name, Research Scientists, Google Research" 双作者署名制。

## 六、就绪度评估

**结论：部分能。** 定量预算完备可直接执行（[统计层] 全指标就位，MATTR 不缺失）；语步骨架已达 3 篇标注门槛（61 段），但距 10 篇全覆盖差 7 篇，且子体裁路由未经裁决。

**缺口清单：**
1. 标注覆盖 3/10——候选子体裁中"成果发布文"外的归位全靠推断，其余 7 篇（glucofm / biomarkers / agenthands / methane / planetary-engine / mobility-place / transfer-learning）未标注；
2. rubric 02 论证标注 0 篇——证据类型、反驳处理只有 rubric 01 的 COUNTER=0 间接信号；
3. 子体裁路由未走 rubric 00 裁决流程，本文件第一节全部标"待裁决"；
4. "局限+下一步"收尾形态仅 1 篇未标注语料支持，未列入骨架；
5. _aggregate.json 未收 word_count 字段——篇幅预算靠逐篇 JSON 现算，aggregate 管线可补。

**最小补全动作（按性价比排序）：**
1. 补标 2 篇"成果发布文"（glucofm + methane，该候选类疑似占全库一半），把最大子体裁从单篇外推中解救出来；
2. 补标 1 篇疑似"局限+下一步"收尾篇（glucofm 可兼任），裁决第四收尾形态；
3. 跑 rubric 00 路由裁决，把第一节候选表转正；
4.（管线向）profiler.py 的 aggregate 增加 word_count 汇总。
