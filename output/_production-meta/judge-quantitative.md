# judge-quantitative — article-meta-v1.md 独立定量评审

- 评审对象：output/_production-meta/article-meta-v1.md（按 kezhongke 两层 playbook 生成的生产稿，A 分析类）
- 评审日期：2026-09-15
- 独立性声明：本评审未读取同目录 generation-selfcheck.md 与 article-meta-v1.profile.json（生成方材料）；全部数值由评审方独立执行 `python3 profiler.py output/_production-meta/article-meta-v1.md` 实测，MATTR 原始值按 profiler.py `mattr()`（w=150, step=25）复算，处方 9 体检由评审方独立脚本逐句扫描。
- 判定依据：templates/genre-playbook-kezhongke.md §0.2 处方走廊（冻结口径，硬约束）+ 处方 8/9；两库包络对照用 output/anthropic/_aggregate.json 与 output/openai/_aggregate.json 的 `two_level.institution`（2026-09-15 扩容后，各 n=20）。

## 1. 总判定：合格（PASS）

14 项走廊指标**全部带内**（含 MATTR 0.698，本次在带内，无需动用高侧容差条款）。处方 9 体检通过：无 v4 式裸名词化病灶，2 处同词族单句技术性触发判观察项，不判失格。感叹号红线 0 命中。

## 2. 逐指标判定表（vs §0.2 冻结走廊）

| 指标 | 实测 | 走廊目标 / 合格区间 | 判定 |
|---|---|---|---|
| 篇幅（词） | 2,873 | ≈2,900 / [2,100, 3,750] | ✅ 带内，贴目标（−27） |
| 平均句长（词） | 20.8 | ≈22 / [20, 24] | ✅ 带内 |
| P90 句长（词） | 34 | ≤35 / 上限 41 | ✅ 带内 |
| 平均段长（词） | 51.5 | ≈42 / [33, 53] | ✅ 带内（偏高侧，距上沿 1.5） |
| 数字密度 /千词 | 17.75 | ≈14 / [8, 21] | ✅ 带内 |
| hedge /千词 | 9.05 | ≈10 / [8, 13.5] | ✅ 带内 |
| absolutist /千词 | 2.09 | ≈2 / [1.4, 3.4] | ✅ 带内，贴目标 |
| 克制比 hedge:absolutist | 4.33:1 | 典型 4–5:1 / 红线 <3:1 | ✅ 典型区 |
| 第一人称（次/篇） | 31 | ≈40 / [21, 69] | ✅ 带内 |
| 客观自指（次/篇） | 2 | 1–2 / [1, 2] | ✅ 贴上沿，未越界 |
| 设问（次/篇） | 3 | 2–3 / [0, 5] | ✅ 贴目标上沿 |
| MATTR | 0.698（raw 0.69755） | 0.68–0.69 / [0.66, 0.70] | ✅ 带内（见 §3） |
| 年份锚点 /千词（软约束） | 0.35（1 处） | ≈1 / 软上限 2 | ✅ 软约束内，无需豁免注记 |
| 感叹号 | 0 | 0 | ✅ 红线 |

附加观察（走廊表外、与处方相关）：单句段 0 处（处方 2 上限 ≤4，✅）；参考条目 9 条（Sources 节，档案路径+文档名齐全）；§0.2 英文收尾组合四件齐全——设问自答（L95 "So is your style profile a genre artifact? Some of it usually is…"）→ 编号结论 ×4（L99–105）→ 开放问题中性表述（L107 "Two questions the evidence does not cover"）→ 比喻收束（L109 lens/curvature 隐喻，复用全文单一比喻）；处方 5 语气扫描：计入限额的边界声明 2 处（L77 "we do not claim otherwise"、L81 "the current evidence does not cover"，均 COUNTER 位），L107 开放问题按 judge-v3 划界豁免，全部中性事实语气，自我检讨表述（should have / embarrass / we failed 式）0 命中，**未设自我批评小节**，✅。

## 3. MATTR 专项

实测：MATTR raw = 0.69755（109 个滑动窗口，w=150/step=25），**带内** [0.66, 0.70]，距上沿 0.00245。

- 高侧容差条款与处方 8 修正白名单**本次均不触发**——两者仅适用于出带情形（对照：_production-eval-power 稿 0.71971 出带 +0.0197 动用容差；本稿无需）。
- 方向性注记：走廊注记"术语统一会拉低 MATTR……贴带下沿即可，不求带内高位"，本稿 0.698 位于带内高位区，方向性偏好未满足但**不构成出带**，仅记录。本稿为双域题材（统计方法 × 风格测量）且专名密度中等（Simpson's paradox、leave-one-out、false-discovery、MATTR 等），属结构性高 MATTR 题材。
- 预警：距上沿仅 0.00245，后续编辑轮引入新词族即可能出带；出带后 ≤+0.02 走容差、超 +0.02 按处方 8 白名单强制修正。建议任何修订后重跑 profiler 复核。

## 4. 处方 9 体检（主题词对偶负面清单）

独立逐句扫描（137 句，轻量词干归并，剔除 the/and/that 等功能词后判内容词族）：

- **自造名词化支（裸 "the + 分词" 全篇 >5 次）：未触发。** "the pooled" ×8 全部后接名词（caliber/corpus/figure×2/line/rest/table/test），为形容词性修饰而非裸名词化；"the corrected" ×2（instrument/lens）、"the populated" ×1（cell）同。无 v4 式 "the graded"×12 病灶。✅
- **同词族单句 ≥3 次支：内容词命中 4 处——**
  - L35 "family"×4："The family split matters, because correction is priced per family; a signal that would clear one pooled family could fail once the family honestly mirrors the structure of the comparison."。技术术语（统计检验族），四次指涉各异，无变体轮换登记，无明示修辞框架声明 → **技术性触发**。处置：观察项，fluency pass 登记 2–3 个变体（test family / correction family / batch），不判失格（对照 v4 反例为同句词族三叠+全篇裸名词化×12 的双重病灶，本稿仅单支、单词族、指涉可辨）。
  - L89 "family"×3："…until it survives the right family: the correction family has to mirror the comparison structure, because a single pooled family spread over mixed genres…"。同上，**技术性触发**，观察项。
  - L33 "seven"×3："Seven libraries, seven signatures, seven clean certificates of distinctiveness"。刻意对仗/回环，节标题 "1. Seven for seven, then zero of seven" + 文章标题 "Seven Fingerprints" 构成明示框架 → **豁免成立**，仅记录。
  - L61 "label"×3（labeled/labels/label，93/71/28 枚举句）与 L89 "need"×3（word lists need / diversity metrics need / routers need，三并列）：枚举修辞，非病灶，仅记录。
- **结论：处方 9 通过**，2 处技术性触发（同词族 family，L35/L89）判观察项，建议下一轮 fluency pass 登记变体。

## 5. 两库 two_level.institution 包络对照（2026-09-15 扩容后，各 n=20）

口径说明：§0.2 走廊冻结于 2026-09-08 旧聚合（"走廊值冻结至下次盲测校准，不随源聚合漂移"），故 §2 硬约束判定以冻结走廊为准；下表为任务要求的当前 institution 包络 [min(a,o), max(a,o)] 对照，作校准参考。

| 指标 | 本稿 | anthropic | openai | 包络位置 |
|---|---|---|---|---|
| 篇幅（词） | 2,873 | 1,960 | 2,135 | ❌ 高出 +738 |
| 平均句长 | 20.8 | 22.88 | 22.2 | 低 −1.4 |
| P90 句长 | 34 | 39 | 35 | 低 −1 |
| 平均段长 | 51.5 | 39.58 | 37.5 | ❌ 高 +11.9 |
| 数字密度 | 17.75 | 9.55 | 17.77 | ✅ 内（贴 openai 侧上沿 −0.02） |
| hedge | 9.05 | 11.18 | 10.57 | 低 −1.52 |
| absolutist | 2.09 | 2.32 | 2.24 | 低 −0.15 |
| 克制比 | 4.33:1 | 4.82:1 | 4.72:1 | 略低于两库比值，远高于 3:1 红线 |
| 第一人称 | 31 | 29 | 41 | ✅ 内 |
| 客观自指 | 2 | 0.75 | 1 | 高 +1 |
| 设问 | 3 | 1.5 | 1.5 | 高 +1.5 |
| MATTR | 0.698 | 0.69 | 0.68 | 高 +0.008 |
| 年份 /千词 | 0.35 | 0.94 | 1.44 | 低 −0.59 |
| TTR | 0.306 | 0.35 | 0.35 | 低 −0.044 |
| 感叹号 | 0 | 0 | 0 | ✅ 内 |

解读：15 项中 3 项落在两 institution 包络内（数字密度、第一人称、感叹号）；带外 12 项**全部仍在冻结走廊合格区间内**。与 _production-eval-power 评审 §5 相同的口径背离再度出现：**篇幅**（冻结走廊依据旧 median 2,640/3,164，扩容后 institution 下移至 1,960/2,135；本稿 2,873 贴冻结目标）与**平均段长**（冻结带 [33,53] vs 当前 institution 39.58/37.5）。参照系下移两例同向，已呈稳定方向。按 playbook 冻结条款不构成本稿失格依据；记录为下次盲测校准输入项（篇幅带与段长带或需随扩容后参照系重估）。

## 6. 偏离项清单与处置建议

| # | 项 | 性质 | 处置 |
|---|---|---|---|
| 1 | L35 "family"×4、L89 "family"×3 同词族单句 | 处方 9 技术性触发（单支、单词族、指涉可辨） | 观察项；fluency pass 登记 2–3 变体（test family / correction family / batch），不判失格 |
| 2 | MATTR 0.698 带内高位（距上沿 0.00245） | 方向性偏好（贴下沿）未满足，非出带 | 仅记录；任何修订后重跑 profiler 复核 |
| 3 | 客观自指 2、设问 3（均贴走廊上沿） | 贴线未越界 | 仅记录 |
| 4 | 平均段长 51.5 带内偏高、当前包络外（+11.9） | 冻结走廊内 | 仅记录 |
| 5 | 走廊篇幅/段长带 vs 扩容后 institution（第二例同向证据） | 参照系口径漂移，非本稿问题 | 移交下次盲测校准 |

**总判定：合格（PASS）。** 14/14 走廊指标带内（MATTR 本次带内，无需动用容差条款与处方 8）；处方 9 通过（2 处技术性触发判观察项）；当前两库 institution 包络对照不构成追加失格依据（冻结走廊优先）。
