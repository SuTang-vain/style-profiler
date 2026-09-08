# 盲测大纲 · openai 库 · engineering-deep-dive（调查叙事型）

> 依据：templates/genre-playbooks-openai.md（体裁路由特征、四体裁通用骨架、engineering-deep-dive 调查叙事型语步、频率标签操作化）+ output/openai/_aggregate.json（统计层预算）。
> 子体裁：**engineering-deep-dive · 调查叙事型**（core-dump 变体）。
> 路由依据：题材是"我们如何构建并加固 X"的第一人称工具复盘，素材天然是调查结构——初版方案（子串匹配/TTR/静默校验器）→ 失败显形 → 转折 → 修复+确认 → 教训；命中路由表"第一人称调查叙事、自我反驳内化、格言化教训收束"三条识别特征。未选宣言型（harness-engineering）：素材以 bug 调查为主线，无"哲学宣言统治全文+规模数据锚定"形态；未选 evaluation-report：无自建基准命名与 Limitations 独立节诉求（局限改为 ARGUE 内自我反驳内化）。
> 篇幅目标：~3,100 词（median 3,164；P25–P75 1,628–3,758）。

## 定量预算表（[统计层]，~3,100 词折算）

| 指标 | median | P25–P75 | 本篇目标 |
|---|---|---|---|
| 词数 | 3,164 | 1,628–3,758 | ~3,100 |
| 平均句长（词） | 22.3 | 19.9–24.9 | ~22 |
| P90 句长 | 35.5 | 34–38 | ≤38 |
| 平均段长（词） | 40.2 | 32.9–43.9 | ~40（多 2 句段） |
| 数字密度/千词 | 20.69 | 15.64–27.64 | ~60 个数字 |
| 精确小数/千词 | 0.92 | 0.31–2.66 | 4–6 处（4.75/2.69/0.204/0.070） |
| 年份/千词 | 1.23 | 0.8–1.82 | ~4 处（2025/2026） |
| hedge/千词 | 9.57 | 7.99–14.73 | ~29 处（roughly/about/seems/likely/initial/remains…） |
| absolutist/千词 | 1.76 | 1.38–2.93 | ~5 处（自然用法，不堆） |
| quantifier/千词 | 5.9 | 1.9–6.51 | ~18 处（all/every/most/first） |
| 第一人称（we/our/I，原文计数） | 53 | 33–90 | ~50 |
| this post 类自指 | 1 | 1–2 | 1–2 |
| 问句 | 3 | 1–11 | 3（2 进小节标题+1 正文） |
| 感叹号 | 0 | 0–1 | 0 |
| 外链/参考文献 | 0 | 0 | 0 |

## 语步骨架（通用骨架 + 调查叙事型特有语步）

通用：无场景 HOOK → CONTEXT → FRAME → ARGUE×n（COUNTER 内化）→ APPLY → CLOSE（格言化）。
调查叙事型：initial approach → 失败 → 单句段转折 → 高潮确认 → 费米估算 → 教训+承诺。

| # | 小节 | MOVE | 功能（内容要点 → playbook 招式） |
|---|---|---|---|
| 1 | （引子，无标题） | HOOK | 数字+反转直接切入：首版基线里 43% 的 hedge 命中来自同一个汉字（无场景开场，禁场景描写） |
| 2 | | CONTEXT | 工具定义：给研究性文章做统计画像的 profiler；26 个确定性指标 |
| 3 | | CONTEXT | 7 家机构博客、每家约 10 篇、每篇压成 26 维向量（规模数据锚定） |
| 4 | | CONTEXT | 为什么确定性：2026 年另一条路是把语料丢给大模型打分；我们选择计数器（历史锚定+年份预算） |
| 5 | | FRAME | 问题清单式预告：three failures——a matcher that saw ghosts / a ruler that stretched / a validator that only said PASS；声明 "This post is about…"（自指预算 1/2） |
| 6 | What the profiler measures | CONTEXT | 指标分族：句长/数字密度/hedge/词表重复；每个数都可手工重数（频率标签操作化：定性判断配数字定义） |
| 7 | | CONTEXT | 同输入同输出；可回归测试；与世界观：验证因此 cheap（一句落点，不展开宣言） |
| 8 | The matcher that saw ghosts | ARGUE（initial approach） | 初版：中文无空格，分词是另一个工程，子串匹配当时 seems reasonable（hedge 内嵌） |
| 9 | | ARGUE（失败显形） | 发现路径：读命中清单而非代码；"约束/简约/契约"全含"约" |
| 10 | | ARGUE（证据） | 一段谈 constrained optimization 的文字读起来充满犹豫；指标没崩、在撒谎 |
| 11 | | ARGUE（单句段转折） | 单句段：That was the first time we read the hit list instead of the code.（节拍器，自撰句） |
| 12 | | ARGUE（修复+量化） | 改词边界匹配；中位数 4.75→2.69/千词；roughly 43% 是假命中（精确数字+hedge 同句） |
| 13 | | ARGUE（费米估算） | 手工复核抽查：挑 1 篇逐条重数，手工数与管线差几个百分点内；语料没变，变的是计数器 |
| 14 | | ARGUE（教训） | 危险 bug 不报错，返回可信数字；lesson 落段 |
| 15 | The ruler that stretched | ARGUE | TTR 定义（distinct/total）与来历；长度依赖是机械性的：越长越重复 |
| 16 | | ARGUE | 7 家机构原始 TTR 比较 ≈ 比篇幅；尺在量自己 |
| 17 | | ARGUE（修复） | MATTR：滑动窗口 w=150，等长帧消除篇幅泄漏（数字定义） |
| 18 | | ARGUE（数据锚定） | 跨机构差距 0.204→0.070，roughly 三倍缩小；排序未动 |
| 19 | | ARGUE（COUNTER 内化） | 自我反驳："0.204 会不会是真信号？"→推演：若是真信号，等长窗口应保留差距→未保留→封堵（问句预算 1/3） |
| 20 | | ARGUE | 残差解读：约 2/3 表观差异来自尺子不来自文本；残余 0.070 才是敢辩护的信号（克制） |
| 21 | | ARGUE（教训+承诺） | 每个指标必须声明 invariance（不响应什么）；可声明即可测试→进回归套件 |
| 22 | Why didn't the tests catch any of this? | ARGUE | 问句标题（问句预算 2/3）；回归 harness 设定：重算并 diff markdown 表期望值 |
| 23 | | ARGUE（失败显形） | 解析器跳过加粗单元格→从不比较、从不失配 |
| 24 | | ARGUE（单句段节拍器） | 全绿 PASS；单句段：Everything passed. Nothing was checked.（自撰短句对） |
| 25 | | ARGUE（高潮确认） | 修复解析器后立刻抓到 6 处数值漂移——确认校验器此前是盲的 |
| 26 | | ARGUE | 6 处多为过期期望值（修指标后未同 commit 同步）；逐一钉进测试 |
| 27 | | ARGUE（转折+新规） | 单句段转折：That was the week we stopped trusting green. → 新规：每个 check 先演示失败 |
| 28 | | ARGUE（数据锚定） | 20 项回归测试，每项都见过红至少 1 次 |
| 29 | | ARGUE（教训） | 不能失败的校验器比没有更糟：它制造信心（absolutist 预算内使用） |
| 30 | What we now require | APPLY | 制度化收束：5 条 bullet（加粗引领句，harness 式清单）——boundaries are the contract / declare the invariance / recompute by hand / no unearned PASS / expectations move with the metric |
| 31 | | APPLY | 承诺句：这 20 项测试随每次改动运行；新指标入表前先交 invariance 声明 |
| 32 | （收尾，无标题） | CLOSE | 格言化：A metric is not just a measurement—it is a claim about what can be safely ignored.（X is not just A—it is B 公式） |
| 33 | | CLOSE | 升华+承诺：profiler 的价值不在 26 个指标，而在每个数都能被 cross-examine；呼应开头 43%（无 CTA、无参考文献、无感叹号） |

## 排版惯例（校准自 corpus/openai 样本）

- ## 小节标题，短语式、可带问句；引子与收尾无标题。
- 正文全 prose；仅 APPLY 一处 bullet 清单（加粗引领）。
- 单句段作节拍器 2–3 处；禁用场景描写、emoji、感叹号、外链、参考文献节。
- 年份用法：2025/2026 各 1–2 处，作历史锚定而非日期堆砌。

## 不写清单（反例对照）

- 不设 Limitations 独立节（evaluation-report 特征，局限一律内化进 ARGUE 自我反驳）。
- 不写"We show that: ①②③"成果预告（research-narrative 特征）。
- 不写"四宗罪"式升格清单、不做哲学宣言统治全文（宣言型特征）。
- 不用 we believe 高频信念陈述（approach-position 特征）。
- 禁场景化 HOOK（"某天下午警报响了"式）、禁 CTA、禁 References。
