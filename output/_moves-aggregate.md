# 跨库语步聚合对照（≥3 篇/库，2026-09-08 ②补齐后）

> 数据：每库 3 篇（openai 10 篇既有）rubric 01 全量标注聚合。
> 用途：修正"单篇外推"——库级画像现在建立在多篇聚合上，与"聚合用中位数"纪律对齐。

| 库 | 篇数 | 标注段 | ARGUE% | COUNTER | HOOK | APPLY | 叙事段% | 备注 |
|---|---|---|---|---|---|---|---|---|
| kezhongke | 3 | 131 | 64% | 7 | 1 | 2 | 12% | fde（行业分析）贡献全部 COUNTER；报告体/期刊体 0 |
| cerebras | 3 | 118 | 76% | **0** | 2 | 3 | 14% | 六库唯一零 COUNTER 保持；工程复盘有迭代叙事点 |
| eleuther | 3 | 159 | **83%** | 1 | 0 | 4 | **0%** | 最纯论证文体；common-pile 有质疑-回应单元 |
| databricks | 3 | 130 | 76% | **7** | 0 | 6 | 0% | ⚠️ 修正：memory-scaling 有完整反驳节（"What Gets in the Way"+回应） |
| google-research | 3 | 61 | 72% | 0 | **1** | 2 | 4% | ⚠️ 修正：empty-shelves 设问 HOOK（"never learned them or..."） |
| microsoft-research | 3 | 127 | 77% | 4 | 0 | **8** | 1% | APPLY 密度六库最高——资源链接（HF/报告/开源）是落点指纹 |
| openai | 10 | 41+ | 51% | 5 | 0 | 2 | 9% | 语步最多元（叙事/转折多），ARGUE 占比最低 |

## 修正记录（相对单篇外推的推翻项）

1. **databricks"零 COUNTER"→ 推翻**：3 篇聚合 7 处（memory-scaling 的"What Gets in the Way"节 = 完整的质疑呈现 + 议程化回应；officeqa 有内化让步）。原 orchard 单篇结论只在"系统文"子类成立。
2. **google-research"无 HOOK"→ 推翻**：empty-shelves 以设问开场（"is it because they never learned them or..."）。原 connectomics 单篇结论只在"成果发布文"子类成立。
3. **kezhongke 报告体/期刊体骨架确认**：glm-5-3（元信息头+摘要 FRAME×5 → 编号章节 ARGUE → 编号结论+关注问题 CLOSE → 核验附录）；multi-agent-sociology（摘要+关键词 → 引言事件背景 → 分层论证 → 结论+**局限声明**+后续方向）。
4. **cerebras 零 COUNTER 在 3 篇下保持**（0/118）——"对抗内化为 ARGUE 推演"的画像稳固。
5. **叙事谱系分层确认**：cerebras 14% ≈ kezhongke 12% > openai 9% > google 4% > msr 1% > databricks/eleuther 0%。

## 跨库结构签名（3 篇聚合）

- **开场**：eleuther/msr/databricks 直入成果或问题（无 HOOK）；cerebras 数字/反直觉 HOOK；google 设问或成果声明；kezhongke 报告体元信息头+摘要
- **收尾**：kezhongke 编号结论+关注问题（报告体）/结论+局限+未来（期刊体）；msr APPLY 资源落点；eleuther 边界声明；其余主张收束
- **COUNTER 谱系**：kezhongke 行业分析（7）≈ databricks 研究展望文（7）> msr 系统论证文（4）> openai deep-dive（5/10 篇）> eleuther 立场文（1）> cerebras/google 发布文（0）

## 标注清单（本轮新增 13 篇）

- databricks：memalign(40) / memory-scaling(54) / officeqa-pro-v2(36)
- cerebras：how-we-built-our-knowledge-base(62) / the-economics-of-ai-reasoning(25)
- eleuther：autointerp(98) / common-pile(22)
- google-research：timesfm-3(18) / empty-shelves(28)
- microsoft-research：echoverse(59) / verifying-rust(44)
- kezhongke：glm-5-3-analysis(48) / multi-agent-sociology(45)

anthropic 维持 2 篇（正文不入库，无法补标——受限记录）。
