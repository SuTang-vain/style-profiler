# 修订留痕 r2：article-meta-v1.md 阅读体验修订（2026-09-15）

> 触发：五路阅读体验评审（结构/语言×两稿+横向）后用户批准的定点修订轮。范围 P1（术语首用即释）+ P3（导航对齐）；P2（表格化）暂缓，理由见末节。
> 复验方式：`python3 profiler.py output/_production-meta/article-meta-v1.md -o …profile.json`，对 §0.2 冻结走廊。

## P1 术语首用即释（13 处）

- `caliber` 全部 11 处 → `standard`，首用（原 L9）带定义同位语；`standard` 已核实不中 profiler 任何词表（grep profiler.py 无命中）
- MATTR 释义前移首用处（原 L49）：moving-average type-token ratio + "length-stable diversity metric"；原 L71 定义保留作修复史
- FDR 首段加内联释义；hedge density 加 "about/roughly" 例释（hedge +2 token，带内）
- kezhongke 身份首句给全（"this site's own Chinese corpus and the project's reference case"），原 L21 重复 gloss 删
- correction family 段拆段 + 白话机制句（"judged alongside hundreds of siblings"）；openai 信号独立成段
- 原 L51/L53 合并，"wording" 悬念闭合于 "archived, not claimed"
- 原 L61 按样本时代拆三句；cell 更换原因落实为已核实事实（"the exercise always runs on the cell the most libraries populate"，依据 output/_group-discrimination.txt 三节"取覆盖库最多的体裁格"）
- 原 L63 方向反转显式化（0.90 vs 0.92 小数位错开）；subtype soft labels 加同位语；"forty articles" 无出处数字删除；"one-per-mille" → 0.001

## P3 导航对齐（9 处）

- 编号节 1–4 标题加内容子句，与路线图逐字对应（the headline reversal / the correction / the correction's own error history / the validation chain）
- 三问、五条规则改编号列表（间接问句+句号，未引入新 `?`，设问保持 3）
- 结尾节标题对齐首句完整问句；roadmap "field guide" → "reading discipline"
- L29 双命名悬念改点明关系；"Two questions" 段前移至四点结论之前

## 复验结果：14 项全带内

篇幅 3,320｜句长 21.5｜P90 35｜段长 47.9（52.8→47.9，列表化改善）｜数密 18.67（列表编号计入，带内）｜hedge 8.43｜absolutist 2.11｜克制比 4.0｜人称 30｜自指 2｜设问 3｜MATTR 0.692（0.698→0.692，持续下行）｜年份 2 处｜感叹号 0。

注记：段长余量曾仅 0.2（P1 后 52.8/上限 53），P3 列表化后回到带中。数字密度上行主因列表编号 `1)` 计入 token，带内无需处置。

## P2 暂缓理由

`clean_markdown`（profiler.py:97-127）对 markdown 表格只检测不剥离，表格行并入段落块统计——走廊冻结口径下插表会使段长/数密测量失真（与"数密计入标题"同族工具缺陷）。两稿密度最高段已用 prose 方案（拆段+白话机制句+例释）化解。表格化待工具剥离表格行后再评估。

## 配图（2026-09-20）

封面（玻璃棱镜分光，CC0，Jan Helebrant）+ Simpson's paradox 示意图（公共领域，Schutz，置 "A paradox in the pooling" 节）+ McLeod 真空规（CC BY 2.5，Ytrottier/Amada44，置 §3）——全部 Wikimedia Commons，署名行入 Sources。复验：14 项全带内（MATTR raw 0.69116，数密 19.35 上行因署名行版本号，带内）。
