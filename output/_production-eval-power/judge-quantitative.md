# judge-quantitative — article-eval-power-v1.md 独立定量评审

- 评审对象：output/_production-eval-power/article-eval-power-v1.md（按 kezhongke 两层 playbook 生成的生产稿）
- 评审日期：2026-09-15
- 独立性声明：本评审未读取同目录 generation-selfcheck.md 与 article-eval-power-v1.profile.json（生成方材料）；全部数值由评审方独立执行 `python3 profiler.py output/_production-eval-power/article-eval-power-v1.md` 实测，MATTR 原始值按 profiler.py `mattr()`（w=150, step=25）复算。
- 判定依据：templates/genre-playbook-kezhongke.md §0.2 处方走廊（冻结口径，硬约束）；两库包络对照用 output/anthropic/_aggregate.json 与 output/openai/_aggregate.json 的 `two_level.institution`（2026-09-15 扩容后，各 n=20）。

## 1. 总判定：合格（PASS）

14 项走廊指标中 13 项带内；唯一出带项 MATTR 0.71971（出带上沿 +0.0197）落入 §0.2 高侧容差条款边界（≤+0.02）且适用条件成立，本评审意见为判可接受（附条件，见 §3）。处方 9 体检通过，1 处观察项不判失格。感叹号红线 0 命中。

## 2. 逐指标判定表（vs §0.2 冻结走廊）

| 指标 | 实测 | 走廊目标 / 合格区间 | 判定 |
|---|---|---|---|
| 篇幅（词） | 2,985 | ≈2,900 / [2,100, 3,750] | ✅ 带内，贴目标 |
| 平均句长（词） | 21.3 | ≈22 / [20, 24] | ✅ 带内 |
| P90 句长（词） | 32 | ≤35 / 上限 41 | ✅ 带内 |
| 平均段长（词） | 39.3 | ≈42 / [33, 53] | ✅ 带内 |
| 数字密度 /千词 | 12.4 | ≈14 / [8, 21] | ✅ 带内 |
| hedge /千词 | 10.05 | ≈10 / [8, 13.5] | ✅ 带内，贴目标 |
| absolutist /千词 | 2.35 | ≈2 / [1.4, 3.4] | ✅ 带内 |
| 克制比 hedge:absolutist | 4.28:1 | 典型 4–5:1 / 红线 <3:1 | ✅ 典型区 |
| 第一人称（次/篇） | 44 | ≈40 / [21, 69] | ✅ 带内 |
| 客观自指（次/篇） | 2 | 1–2 / [1, 2] | ✅ 贴上沿，未越界 |
| 设问（次/篇） | 3 | 2–3 / [0, 5] | ✅ 带内 |
| MATTR | 0.71971（profiler 报 0.72） | 0.68–0.69 / [0.66, 0.70] | ⚠ 出带上沿 +0.0197 → 容差条款评估（§3） |
| 年份锚点 /千词（软约束） | 1.01（3 处） | ≈1 / 软上限 2 | ✅ 软约束内，无需豁免注记 |
| 感叹号 | 0 | 0 | ✅ 红线 |

附加观察（走廊表外、与处方相关）：单句段 0 处（处方 2 上限 ≤4，✅）；参考条目 10 条（Sources 节，机构/文档名+月份齐全）；设问 3 处中收尾组合"设问自答"（L137）在位；处方 5 语气扫描无自我批评表述（"embarrass no one who pays" 为厂商激励描述，非自我检讨）。

## 3. MATTR 容差专项评估（本评审核心意见）

实测：MATTR raw = 0.71971（114 个滑动窗口，w=150/step=25），出带上沿 +0.0197，**压在容差边界（≤+0.02）内侧，余量仅 0.0003**。低于两库库内 max（anthropic 0.743 / openai 0.724）。

容差条款两项适用条件核查：

1. **是否双域/专名密集题材 → 成立（实际为三域）**。标题即跨商业×科学×法律三域（"The Business, the Science, and the Law"）；专名密度极高：基准名 6 个（MMLU-Pro、GPQA、SWE-bench、LiveCodeBench、ARC-AGI、Humanity's Last Exam）+ 平台/机构/法规名 20+ 处（Chatbot Arena/LMArena、Patronus AI、EU AI Act、Bradley-Terry、Cohere Labs、AI2、Princeton、Stanford、Meta、Llama 4、a16z、Greenfield、European Commission JRC、Kili Technology、CIVAC 等）。top_terms 全为主题专名族（leaderboard×20、evaluation×14、authority×14、measurement×13、arena×10、benchmark×9+benchmarks×8）。
2. **是否有其他更低成本修正空间 → 经处方 8 白名单逐项核查，结论：没有不拆签名的低成本空间**。
   - 白名单①（专名短称复用）：已执行（Arena、the Act、the paper、the company），无残量；
   - 白名单②（同义归并）：两大高频词族 evaluation×14 / measurement×13 正是处方 3 显式命名概念（evaluative authority / measurement layer），归并=撞处方 3 的语义失真禁区；scores×9 / numbers×8 部分归并收益估算远不及 0.02 所需（150 词窗口内需平均减 ~3 个独立词型，零星合并不足以移动均值）；
   - 白名单③（删非必要新专名）：单现专名（OddsShopper、aiglossary.news、opper.ai、CIVAC 等）全部承担 §5 信源分层归因（"≥5 处具体出处"硬指标），删除=拆信源分层签名装置，成本高于 MATTR 越线本身。

**独立意见：适用容差条款，判可接受。** 附带两条：
- 条件：生成方自检必须按条款标注结构性原因（三域题材 + 专名密集 + 处方 3 术语统一的方向性冲突）——此为容差成立的程序要件；
- 预警：余量仅 0.0003，任何后续编辑轮引入新词族即越 +0.02 硬线（届时按处方 8 强制修正）。建议本稿词汇面冻结，任何修订后重跑 profiler 复核 MATTR。

## 4. 处方 9 体检（主题词对偶负面清单）

- **自造名词化复现**："the graded" 全篇 ×4（L71、L73、L75、L127），未超 >5 触发线（对照 v4 反例 ×12）。且其与 "the grader"（L75）、"the evaluated / the evaluator"（L65、L67 节标题、L141）构成对偶系统，由节标题 "The evaluated pay the evaluator" 与 L71 "the graded, in other words, commission the grading" 明示框架——即便超线亦满足豁免条件，实际未超，无需动用豁免论证。
- **同词族单句 ≥3 次**：机械扫描命中 2 处——
  - L45 "score"×3："None of this makes the score useless — it makes the score interested, and an interested score deserves…"。判定：**技术性触发、实质为刻意对仗**（useless→interested 递进 + antimetabole 回环），但缺处方 9 豁免条款要求的明示框架声明（"The pattern is the point" 式）。处置：观察项，建议 fluency pass 登记 1 个备换变体（ranking/standing），不判失格。
  - L67 "evaluat"×3：为节标题 + 首句的跨句切分 artifact（标题 "The evaluated pay the evaluator" 自身仅 2 次），不计入。
- **结论：处方 9 通过**，1 处观察项（L45）。

## 5. 两库 two_level.institution 包络对照（2026-09-15 扩容后，各 n=20）

口径说明：§0.2 走廊冻结于 2026-09-08 旧聚合（"走廊值冻结至下次盲测校准，不随源聚合漂移"），故 §2 硬约束判定以冻结走廊为准；下表为任务要求的当前 institution（机构中位）包络 [min(a,o), max(a,o)] 对照，作校准参考。

| 指标 | 本稿 | anthropic | openai | 包络内？ |
|---|---|---|---|---|
| 篇幅（词） | 2,985 | 1,960 | 2,135 | ❌ 高出 +850 |
| 平均句长 | 21.3 | 22.88 | 22.2 | 低 −0.9 |
| P90 句长 | 32 | 39 | 35 | 低 −3 |
| 平均段长 | 39.3 | 39.58 | 37.5 | ✅ 内 |
| 数字密度 | 12.4 | 9.55 | 17.77 | ✅ 内 |
| hedge | 10.05 | 11.18 | 10.57 | 低 −0.52 |
| absolutist | 2.35 | 2.32 | 2.24 | 高 +0.03 |
| 克制比 | 4.28:1 | 4.8:1 | 4.7:1 | 略低于两库比值，远高于 3:1 红线 |
| 第一人称 | 44 | 29 | 41 | 高 +3 |
| 客观自指 | 2 | 0.75 | 1 | 高 +1 |
| 设问 | 3 | 1.5 | 1.5 | 高 +1.5 |
| MATTR | 0.71971 | 0.69 | 0.68 | 高 +0.03（容差条款处置，见 §3） |
| 年份 /千词 | 1.01 | 0.94 | 1.44 | ✅ 内 |
| TTR | 0.337 | 0.35 | 0.35 | 低 −0.013 |
| 感叹号 | 0 | 0 | 0 | ✅ 内 |

解读：15 项中 4 项落在两中位数包络内；带外 11 项全部仍在冻结走廊合格区间内。最显眼的口径背离是**篇幅**：冻结走廊依据的旧 median 为 2,640/3,164，扩容后 institution 下移至 1,960/2,135——本稿 2,985 在冻结走廊内贴目标，但对当前包络高出 40%。按 playbook 冻结条款，这不构成本稿失格依据；记录为下次盲测校准的输入项（走廊篇幅带可能需随扩容后参照系重估）。

## 6. 偏离项清单与处置建议

| # | 项 | 性质 | 处置 |
|---|---|---|---|
| 1 | MATTR 0.71971 出带上沿 +0.0197 | 容差边界内（余量 0.0003） | 判可接受；生成方自检须注结构性原因；词汇面冻结，修订后重跑 |
| 2 | L45 单句 "score"×3 | 处方 9 技术性触发，修辞性实质 | 观察项；fluency pass 备 1 变体，不判失格 |
| 3 | 客观自指 2（走廊上沿） | 贴线未越界 | 仅记录 |
| 4 | 走廊篇幅带 vs 扩容后 institution（2,640/3,164 → 1,960/2,135） | 参照系口径漂移，非本稿问题 | 移交下次盲测校准 |

**总判定：合格（PASS）。** 唯一实质偏离 MATTR 经容差条款判可接受；处方 9 通过；当前两库 institution 包络对照不构成追加失格依据（冻结走廊优先）。
