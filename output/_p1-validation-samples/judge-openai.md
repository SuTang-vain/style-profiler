# 独立评审报告 · 盲测成稿《Cross-examining the judge》（openai 库 · 英文成稿）

> 评审对象：output/_p1-validation-samples/draft-openai.md（大纲 outline-openai.md）
> 评审依据：templates/genre-playbooks-openai.md（engineering-deep-dive 调查叙事型 + 通用骨架）；corpus/openai/ 10 篇原文；output/_moves-aggregate.md
> 逐段标注产物：output/_p1-validation-samples/judge-openai-moves.jsonl（70 段 → 61 标注）
> 评审人未参与写作；文末 `<!-- self-check -->` 注释未采信（统计层以本横评独立复跑为准，见 _p1-cross-review.md）

## ① 总评

**基本像，且是四篇中库特征完成度最高的一篇。** engineering-deep-dive 调查叙事型的全部识别特征命中：无场景数字反转 HOOK（"43 percent of..."）、**Bug #1/#2/#3 编号**、每 Bug = 初态→失败→单句段转折→修复确认→教训的完整链、COUNTER 内化（Bug#2 自我问答）、APPLY 加粗 bullet + 制度化承诺、格言式收束（"A metric is not just a measurement—it is a claim about..."——正是 playbook 的 X is not just A—it is B 模板）。

**单句段节拍器 6 处**（P9/25/31/42/52/57），含三句教科书级："We wanted the opposite property." / "The articles had not changed. The counter had." / "That was the week we stopped trusting green."——这是 openai 库特征最强的一次外部体现。

**定量**：句长 22.5/22.3 ✓、段长 43.7/40.2 ✓、MATTR 0.686/0.68 ✓、人称 58/53 ✓、数密 17.1/20.7 略低 ✓、hedge 12.3/9.6 偏多（超 P75，见 ③）。

**证据等级声明**：本评审按 [标注-10篇]（openai 全量）核结构，置信度高于其他库。

## ② 语步骨架对照

```
HOOK（数字反转 43%）→ CONTEXT×2（工具/动机）→ ARGUE×2（主张）→ CONTEXT（选型背景）
→ ARGUE 单句段转折 → FRAME（三问题：What does it take to trust）
→ ARGUE×7（系统描述：族系/聚合/确定性/验证/输出/惯例/哲学）
→ Bug#1：ARGUE×12（机制→COUNTER 自问→失败时间线→发现→归因→教训→修复→复测→重数→对照→声明）
→ Bug#2：ARGUE×14（机制→缺陷→例证→影响→背景→修复→理由→复测→单句判定→稳健→COUNTER 质疑→谦逊→残差→要求）
→ Bug#3：ARGUE×13（漏抓→形式→归因→单句对照→时长→发现→stale→格言→教训→规则→ritual→数据→格言）
→ APPLY×2（处方 bullet + 制度）→ ARGUE（同型回看）→ CLOSE×2（格言+收束）
```

分布：ARGUE 49/61 = 80%；COUNTER 2（均为内化自问，全在 Bug 叙事内部）；APPLY 2；单句段教训句 6。

逐项对照 engineering-deep-dive（调查叙事型）：
- "无场景数字反转 HOOK" ✓（43%）
- "Bug 编号化 + 单句段节拍器" ✓✓（6 处，密度超原库单篇）
- "COUNTER 内化为自我反驳问答" ✓（P21 "Why did that seem reasonable at the time?" + P44 "Could the original gap..."）
- "教训格言化收束（X is not just A—it is B）" ✓（P68 逐字套用模板）
- "制度化承诺收束" ✓（P65 "20 tests now run on each change"）

**唯一结构性发现**：三个 Bug 节是同构嵌套（与 kezhongke-en 五层、anthropic 三 Failure mode 同题不同构——openai 用的是**编号侦探链**而非模块清单）。

## ③ 定量与露馅

- hedge 12.31 vs 基线 median 9.57 [P75 约 11]：**偏多、超 P75**——侦探叙事的回顾语气（"could have been""seemed"）天然推高 hedge。方向符合 openai 高 hedge 特征，但过 P75。
- 单句段密度超原库：6 处 vs 原库单篇通常 3-4 处——节拍器是 playbook 显性特征，写作方执行偏"超额"，未破坏质感（评审判定为风格强化而非失真）。
- 数密 17.1 vs 20.7：略低（Bug 叙事的机制描述天然少数字；原库评测类拉高基线——子体裁混合基线的已知问题）。
- 无外链/参考文献 ✓（playbook：零引用、自产证据）；感叹号 0 ✓。

## ④ 结论

盲测通过。openai playbook（调查叙事型）在四库横评中**引导完成度最高**：骨架、节拍器、COUNTER 内化、格言模板全部落地且被独立评审确认为库内已观察模式。P2 遗留：hedge 超 P75 的侦探语气效应，建议 playbook 补"回顾语气 hedge 预算"条目。
