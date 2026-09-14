# _p2 复验：两层模型盲测（A 分析评论类，2026-09-14）

> 路线图第 6 项。生成侧：draft-v4-a-genre.md（题目"The Evaluation Industry Is Replaying the History of Credit Rating Agencies"，语料外题材，英文成稿，kezhongke 两层 playbook）。
> 评审侧三路独立盲评（均未见生成方自检材料）：judge-quantitative.md（定量走廊）、judge-lesions.md（_p2 病灶对照）、judge-style.md（风格相似度，v2/v3 评审同口径）。

## 总判定：通过

| 评审路 | 判定 | 关键事实 |
|---|---|---|
| 定量走廊 | 通过 | §0.2 十三项硬约束 12 项达标、0 结构性偏离；两库包络 9/12 项带内、3 项出包络但仍在走廊内；多项贴目标值命中（absolutist 2.26 与 anthropic 机构值逐位相同、人称 39 vs ≈40、句长 22.1 vs ≈22） |
| _p2 病灶 | 通过 | 六类病灶（hedge 雾/膨胀稀释/言语痉挛/机械脚手架/语法失守/警句稀释）全部消除；无预算当靶心症状；COUNTER 判决明确（2 rebutted / 2 left-open 与 §5 实证比例精确一致） |
| 风格 | 像（高置信） | 可读性处方 7/7 兑现；收尾四环节齐备无自我批评位；语步序列与 A 类骨架逐位吻合；带内偏 anthropic 侧未出带 |

## 残留项（非退稿级）

1. **MATTR 0.713 出带上沿（+0.013）**——三路评审一致判轻微：题材跨双域专名密集（NRSRO/Dodd-Frank/SWE-bench）是结构性原因；实测仍在 anthropic/openai 库内文件范围内（两库 max 0.743/0.724）。暴露一个 **playbook 真空：§0.2 只写了"贴下沿"，高侧超标无处方**——继续压只能撞处方 3（术语统一）或处方 7（禁排比重述）。**处置状态：已修订**（playbook §0.2 走廊表 MATTR 行高侧容差条款 + 处方 8 修正白名单/禁用手段）。
2. **主题词对偶过载**（新病灶类，_p2 未记录）："the graded" 名词化 ×12，一处同句三 "grade" 词族叠加——建议 fluency pass 变体 2–3 处；已记入待办。**处置状态：已修订**（playbook §0.2 处方 9 主题词对偶负面清单，含阈值、轮换要求与回环修辞豁免）。
3. **信源分层执行最薄**：一处事实断言未挂来源（"According to reporting last year"）；EU AI Act 罚款比例一处建议信源复核。**处置状态：已修订**（playbook §5 信源分层强化：事实断言归因标签强制、模糊归因全篇 ≤2 处、每篇 ≥5 处具体出处）。
4. **年份锚点 4.19/千词 vs A 格 delta −1.0 方向未达成**：历史对照题材的结构性证据需求；走廊未设此项，不越界，但若走廊未来补收年份项本篇将出带（judge-quantitative §5 存档）。**处置状态：已修订**（playbook §0.2 走廊表新增年份锚点软约束行：目标 ≈1/千词、软上限 2/千词，历史对照/编年类题材豁免须自检注记——本稿情形即豁免条款的引例）。

## 对两层模型的验证含义

- **A 格 delta 定向有效**：段长 49.7 贴上沿（delta +11.3 方向）且被定量评审独立识别为"更像 kezhongke A 格"——两层 delta 的方向性引导真实生效且可观测。
- **_p2 四层病灶的对症疗法确认**：本次生成以"走廊=护栏非靶心 + delta 定向 + 处方负面清单"执行，病灶清零——_p2 根因分析的四层错配在本体裁上得到修复验证。
- **遗留处方真空两个**（MATTR 高侧处置、年份锚点是否入走廊）转入 playbook 下一轮修订候选。

## 文件清单

- draft-v4-a-genre.md（成稿）/ generation-selfcheck.md（生成方自检，含 MATTR 未达标的诚实标注与三轮修正史）/ draft-v4-a-genre.json（生成方 profiler 留档）
- judge-quantitative.md / judge-lesions.md / judge-style.md（三路盲评）
