# 盲测成稿评审报告 · cerebras 库

> 评审对象：/tmp/sp-validation/draft-cerebras.md（大纲 outline-cerebras.md）
> 评审依据：rubric/01-move-annotation.md 七类语步；corpus/cerebras/ 10 篇原文；output/cerebras/annotations/ 3 篇已标注篇目；templates/genre-playbook-cerebras.md。
> 逐段标注产物：/tmp/sp-validation/judge-cerebras-moves.jsonl（52 段）。
> 评审人未参与写作；统计层已由他人核验，本报告只做语步/质感/招式三层对照。

## ① 总评

**基本像（偏像）。** 语步骨架、ARGUE 占比、六个固定招式全部落进该库观察范围，无一处越界结构；失分集中在文体质感——警句与华丽隐喻的密度系统性高于该库工程散文的平实基线，个别段落读起来像杂志专栏而非 Cerebras 工程师博客。

## ② 语步骨架对照

成稿骨架（52 段）：

```
HOOK → CONTEXT×4 → ARGUE → FRAME → ARGUE×6 → CONTEXT×2(概念命名)
→ ARGUE×24(三小节主体) → APPLY×3 → CLOSE×3
```

分布：ARGUE 38/52 = 73%；HOOK 1、FRAME 1、CONTEXT 6、APPLY 3、CLOSE 3、COUNTER 0。

与库内三篇已标注骨架逐项对照：

| 维度 | 库内观察 | 成稿 | 判定 |
|---|---|---|---|
| 开场 | 数字开场（15,000 questions）或反直觉断言（Loops are the least surprising…） | 数字+反直觉（"43 percent of our hedging counts"） | 在范围内 |
| CONTEXT 块 | 2–5 段（playbook 区间）；economics 篇 5 段 | 4 段 | 在范围内 |
| FRAME 位置 | never-loop 在 HOOK+CONTEXT 后；**economics 有 ARGUE→FRAME 先例**（para 9→10） | 1 个 ARGUE（机制论断）后再 FRAME | 在范围内，有先例 |
| 主体 ARGUE 占比 | 76%（118 段聚合） | 73% | 在范围内 |
| COUNTER | 3 篇 118 段 COUNTER=0，反驳一律内化为 ARGUE 推演段 | 0；para 32 "You could argue… play it forward" 内化处理 | 在范围内，无独立 COUNTER 节 |
| APPLY | 3 处，祈使清单+Off-limits | 3 处（教学转向/6 条清单/Off-limits） | 在范围内 |
| 收尾 | build-log 设计哲学收束 1 段（knowledge-base） | 设计哲学收束 3 段 | 形态对，**段数超样**（库内 CLOSE 均 1–2 段） |

越界结构检查：未发现该库从未出现的语步结构；无 COUNTER 独立成节、无 Limitations 节、无编号结论、无参考文献。小节组织（按子系统/失败模式分节：Inflation / Drift / validator）符合 build-log 代表篇 knowledge-base 的 Anatomy/Slack/Threads 式分节。两处概念命名单句段（para 14–15）按 never-loop 对 "Spiralling./Cheating." 的标注先例记为 CONTEXT 而非大纲所标的 ARGUE——这是 rubric 归属歧义，非成稿结构错误（见 ⑥）。

## ③ 最像 / 最露馅段落对照

抽对照的成稿段落：para 1（HOOK）、14–15（概念命名）、22（数据锚定）、32（对抗推演）、20–21（bug 发现叙事）、50–52（收尾）。

**最像**：概念对立命名段（draft L36–38）
> "Inflation. The counter sees things that are not there."

对照 never-loop-without-verifiers.md L57–58：
> "Spiralling. The loop never learns when it is done"

形式逐项同构：可传播的单词命名 + 句号 + 单句定义，独立成段。这是 playbook"概念对立命名"招式的精确复刻，也是全稿与原文库形式重合度最高的一处。次像的是数据锚定句（draft L54 "from 4.75 to 2.69 per 1,000 words, a fall of roughly 43 percent"），与原文 "about 1.2 seconds, running at roughly 1,500 tokens per second"（never-loop L39）同属"限定语+精确数字同句"句型。

**最露馅**：bug 发现叙事段（draft L50–52）
> "row after row of matches was 约束, the word for limits, wearing the badge of the word for vagueness"
> "A dry section on constrained optimization looked like a forest of hesitation."

对照 knowledge-base 同功能段落（初步实验失败，L90）：
> "We initially tested whether simple embeddings over raw text performed well enough. We quickly realized that vector search alone was insufficient"

库内工程失败叙事是平铺直述的机理说明，几乎不带修饰性隐喻；"wearing the badge""forest of hesitation"是双嵌套隐喻 + 同位语解释的文学化写法，register 偏散文专栏。同段 "The metric did not crash; it lied." 这种拟人化警句在库内也无对应物（库内最近的犀利句 "set your OpenAI bill on fire" 是具体场景，不是抽象拟人）。

## ④ 招式核验表（playbook §五 六条固定招式）

| 招式 | 落位证据（draft 行号） | 判定 |
|---|---|---|
| 速度即世界观 | L32 "makes verification cheap instead of precious"（直接用范式签名短语）；L125 "lets a team move fast without breaking its own measurements" | 落位（变体：换算成验证成本而非速度值） |
| 数据锚定句（hedge+精确数字同句） | L54 "4.75 to 2.69… roughly 43 percent"；L86 "71 percent… about 5 out of 7"；L14 "about 26 deterministic metrics" | 落位，多处 |
| 对抗推演代替反驳节 | L76 "You could argue the 0.204 gap was real signal… but play it forward… All 7 institutions kept their places." | 落位，推演+封堵完整 |
| 概念对立命名 | L36 "Inflation. The counter sees things that are not there." / L38 "Drift. The ruler changes length…" | 落位，形式精确 |
| 处方清单 + Off-limits 禁令 | L114–119 六条祈使句清单；L121 "Off-limits: you may not ship a metric whose failure mode you have never seen." | 落位，句式与原文 "Off-limits: you may not train on…" 同构 |
| 反直觉/数字 HOOK | L8 "One Chinese character was quietly responsible for 43 percent of our hedging counts."；无场景描写 | 落位 |

附加合规项：问句 2 个（L20 设问、L80 小节标题）≤4；感叹号 0；外链/参考文献 0；每 4–5 个 ARGUE 段有一个"锚"（数字或推演），符合 §二写作指令。唯一可议处：L32 直接搬用范式签名短语 "cheap instead of precious"，招式落位但与原文措辞过近，处于"致敬/套话"边界。

## ⑤ 若由我来改，3 条具体修改建议

1. **拆掉 Inflation 节的双嵌套隐喻，改平铺机理。** L50–52 改为直白工程叙事："We found the bug in the hit list, not the code: most hits were 约束 (constraint), booked as hedges." 对照 knowledge-base L90 的句式。同理删除 "forest of hesitation"，保留事实判断 "The metric did not crash; it returned plausible numbers."
2. **降低小节末尾警句密度：每个小节最多保留一枚。** 现状几乎每个 ARGUE 小节都以对仗警句收束（"you cannot diff a mood" / "plausible numbers get quoted" / "the ruler was measuring itself" / "a floor to stand on, not a trophy" / "it manufactures confidence"）。库内警句是偶发而非节拍器（knowledge-base 主体几乎零警句）。保留 L18 和 L106，其余改写为普通机理陈述句。
3. **CLOSE 三段并为一段半。** 库内 CLOSE 均为 1–2 个短段（"meets people where they…" 一段；"All that's left is for you to go build one." 两段）。删去 L123 的 cross-examination 隐喻句，合并 L125–127，让 "always right vs always check" 单独作终句；同时把 HOOK 的落点从抽象命题（"taught us what kind of judge we were actually building"）改为规模/机制实词，对齐库内 hook 落点（"more than 15,000 questions every day"）。

## ⑥ 本次盲测暴露的 playbook 缺陷清单

1. **"参考文献=反例"与 build-log 唯一样本冲突。** §四依 median=0 把参考文献列表列为反例，但唯一已标注的 build-log 篇 knowledge-base 正文带 9 条 REFERENCES 和 9 处脚注标号——median 口径把子体裁内合法形态判成了违规。写作方照 playbook 写 build-log 反而偏离该子体裁唯一样本。规则需按子体裁分层，不能只给全库中位数。
2. **"概念对立命名"定义段的语步归属在 rubric/playbook 间不一致。** 标注先例（never-loop）把 "Spiralling./Cheating." 单句定义标为 CONTEXT；写作方大纲标 ARGUE；playbook §五只描述招式形式、未说明语步归属。同一修辞单元两种标法，骨架聚合时 ARGUE 占比会产生 ±4% 的人为摆动。
3. **修辞密度无预算项。** §三定量预算管句长、数字、hedge、问句，但没有"警句/隐喻密度"维度，而该库工程散文基线平实（knowledge-base 主体几乎无隐喻）。本次盲测最大的质感偏差（警句节拍器化）恰好落在 playbook 无约束的维度——写作方逐条合规仍整体过度抛光。
4. **骨架图把 APPLY 线性化，掩盖了库内的交织分布。** §二骨架写作 ARGUE×n → APPLY×1–3，但 never-loop 的 3 处 APPLY（para 18/29/36）实际穿插在主体 ARGUE 中间。写作方按图把教学转向+清单+禁令全部堆到尾部单节，虽合规却不如原文的"中段教学转向"分布典型。
5. **HOOK 规则只禁开场形式、未规定落点。** §五禁"场景描写式开场"，但未要求 hook 落点为规模数字或机制（库内两个 hook 分别落在 "15,000 questions/day" 和 "Loops are the least surprising thing" 这类实词断言上）。成稿 hook 落在抽象命题上仍判合规，说明规则颗粒度不足。

---

附：逐段标注见 /tmp/sp-validation/judge-cerebras-moves.jsonl；标注纪律第 4 条（同篇重跑一致性）未执行，本评审为单次标注，语步结论未经 unstable 抽检。
