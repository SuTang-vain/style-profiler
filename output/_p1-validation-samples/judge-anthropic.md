# 独立评审报告 · 盲测成稿《Measuring style without trusting the meter》（anthropic 库 · 英文成稿）

> 评审对象：output/_p1-validation-samples/draft-anthropic.md（大纲 outline-anthropic.md）
> 评审依据：templates/genre-playbook-anthropic.md（engineering-playbook 工程方法指南 + postmortem 变体）；corpus/anthropic/ 10 篇原文；output/_moves-aggregate.md
> 逐段标注产物：output/_p1-validation-samples/judge-anthropic-moves.jsonl（39 个正文段 → 39 标注，全覆盖）
> 评审人未参与写作；文末 `<!-- self-check -->` 注释未采信（统计层以本横评独立复跑为准，见 _p1-cross-review.md）

## ① 总评

**基本像——库特征命中率四篇最高，但人称密度显著超预算。** engineering-playbook 全部识别特征命中：经验开场（"Over the past year"）、定义辨析先行（statistical/annotation/archive 三层区分）、模式清单三段式（每 Failure mode = 定义→机理→制度化）、**澄清指控句**（"To state it plainly: these bugs did not change any published conclusions"）、**Why detection was difficult 自我批评节**、**aren't prescriptive 边界声明**、Summary 三原则清单、概念命名句（"We refer to this as measurement contamination"）。

上述六项是 anthropic 库的签名元素（postmortem + playbook 双谱系），全部落地且无一处越界。**唯一显著偏差：第一人称 57 vs 库基线 median 30**——约为 median 近 2 倍、接近 openai（58）；但仍在 IQR [21, 69] 内，属 median 偏离而非越界。理由与后果见 ③。

**定量**：句长 22.2/22.45 ✓、段长 45.3/44.75 ✓、MATTR 0.708/0.69 ✓（略超 P75 0.70，概念复用所致，与 playbook 注记一致）、数密 4.76/8.25（低于 median，但在 IQR [3.27, 17.0] 内——方向符合"数字密度低"指纹）、hedge 13.31/10.52 高于 median（方向符合高 hedge 指纹，贴 P75 13.56 内缘，未越界）。

**证据等级声明**：engineering-playbook 条目仅 building-effective-agents 单篇标注支撑（playbook 自标高风险外推）——本评审核的是"条目是否落地"，"条目本身是否忠实于库"置信受限。

## ② 语步骨架对照

```
CONTEXT×2（经验开场 → 动机）→ FRAME（文章定位）
→ ARGUE×5（指标/语料/聚合/三层区分/侵蚀警示）→ ARGUE（失败形状总起）
→ FM1：ARGUE×5（定义→例→机理→发现→泛化）+ ARGUE（制度化）
→ FM2：ARGUE×4（定义→TTR→修复）+ COUNTER（让步质疑）+ ARGUE×2（限定+invariance）
→ FM3：ARGUE×4（定义→漂移→重算→格言）+ ARGUE（历史回顾）
→ Why detection：ARGUE×4（根因→COUNTER 设问自答→澄清声明→边界声明→读者建议）
→ What we changed：ARGUE + APPLY×3（处方/开源/维护者建议）
→ Summary：CLOSE×4（成功重定义→三原则引入→清单→信任收束）
```

分布：ARGUE 25/39 ≈ 64%；COUNTER 2（让步质疑 + 设问自答，均内化）；APPLY 3；CLOSE 4。

逐项对照 playbook（engineering-playbook + postmortem 变体）：
- "经验背景开场（Over the past year）" ✓（逐字命中）
- "定义辨析先行" ✓（P9-10 三层架构区分置于失败叙事前）
- "模式清单结构（定义→出现条件→示例）" ✓（三个 Failure mode 同构）
- "处方落到最简方案" ✓（P40 word-boundary 处方 + P44 "isn't about the cleverest"）
- "澄清指控句"（postmortem 签名）✓（P35 "To state it plainly"——逐字命中 a-postmortem 的标志性句式）
- "自我批评节"（postmortem 签名）✓（P32 Why detection was difficult）
- "边界声明（aren't prescriptive）" ✓（P36 逐字命中 building-effective-agents 的标志性句式）
- "Summary 原则清单" ✓（P45-46 三原则）

**库特征转化机制评注**：本篇的成功不是"照抄某篇原文结构"，而是 playbook 把两个库内签名（postmortem 的澄清/自我批评 + playbook 的模式清单）**组合**进了工程方法论文——这是 playbook 作为"可迁移约束集"（而非模板复制）的直接证据。

## ③ 定量与露馅

- **第一人称 57 vs 基线 median 30**：**四篇最大 median 偏离**（近 2 倍；仍在 IQR [21, 69] 内，不构成越界——核验更正：初稿误称"超 P75"）。根因：题材是 we 叙事（多作者项目），且 playbook 人称预算未列硬约束。后果：成稿人称密度接近 openai（58）——anthropic"第一人称中低"的指纹在成稿中消失。这是横评"人称未分化"现象的本篇主例。
- 数密 4.76：低于 median 8.25 约四成——"数字密度低是指纹"方向正确，幅度在 IQR [3.27, 17.0] 内（Failure mode 概念叙事天然少数字；原库的评测类拉高基线）。
- hedge 13.31 高于 median 10.52、贴 P75 13.56 内缘：方向符合（anthropic 高 hedge 指纹），幅度未越界——诚实边界声明（plainly/should also be clear）推高。
- 澄清声明、边界声明、自我批评节的**位置与原库一致**（收尾前三分之二处），结构转译正确。

## ④ 结论

盲测通过，且是**playbook 组合转化能力的最佳证据**：两个库内签名谱系（postmortem + engineering-playbook）被组合进一篇非库原生题材，六个签名元素全部落位。P2 遗留：**人称预算硬约束**（当前 playbook 未列——题材为 we 叙事时向 median 上方漂移近 2 倍，库间指纹未分化；虽未越 IQR，指纹层面仍需预算约束）；hedge/数密的子体裁基线问题与 openai 同源（混体裁基线已知局限）。
