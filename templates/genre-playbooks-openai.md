# OpenAI 博客 · 四子体裁语步模板（基于 10 篇全量标注定稿）

> 2026-09-06 定稿。来源：style-profiler rubric 01/02 全量标注（见 output/openai/annotations/）。
> 用途：写作时的体裁层模板；与《OpenAI 博客风格档案 v1》配套。

## 体裁路由特征（rubric 00 的 OpenAI 扩展）

| 子体裁 | 识别特征 | 代表篇目 |
|---|---|---|
| **research-narrative 研究叙述** | 结论先行摘要段；"We show that: ①②③" 要点预告；模型输出原文作证据；论文外链兜底 | emergent-misalignment |
| **evaluation-report 评测报告** | 自建工具命名（CoT-Control/GDPval）；精确数字区间结论；Limitations 独立成节；制度化承诺收束 | reasoning-models-cot, gdpval, gpt-5-safe-completions |
| **engineering-deep-dive 工程深潜** | 第一人称调查叙事；单句段节拍器；自我反驳内化；格言化教训收束。三个变体：调查叙事型（core-dump）/ 教学型（unrolling-codex）/ 宣言型（harness-engineering） | core-dump 等 3 篇 |
| **approach-position 立场方法** | we believe 高频；行动宣告+信念陈述；局限主动声明；治理词汇（legibility/accountability） | model-spec, understanding-source |

## 四体裁通用骨架

```
无场景 HOOK（直接切入技术语境或极简事实开场）
→ CONTEXT（概念/系统铺垫）
→ FRAME（方法框架或问题清单，"We show that:" 式要点预告可选）
→ ARGUE×n（自产证据推进；COUNTER 全部内化为自我反驳）
→ APPLY（缓解/工具/制度承诺）
→ CLOSE（教训格言化：X is not just about A—it's about B）
```

## 各体裁特有语步

**research-narrative**：结论前置摘要段 → 三问题清单 → 要点式成果预告 → 实验方法+量化指标定义（misalignment score）→ 模型输出原文引用 → 免责声明内嵌（internal-only, not deployed）

**evaluation-report**：工具命名 → 数字区间结论（0.1%–15.4%）→ 失败案例原文（可带幽默）→ **Limitations 必备节**（gdpval 变体：前置到正文第 4 段）→ 对抗条件自查 → 制度化承诺（写入 system cards）

**engineering-deep-dive**：
- 调查叙事型：initial approach → 失败 → 单句段转折（This was the turning point.）→ 高潮确认（The answer was yes.）→ 费米估算 → 教训+承诺
- 教学型：定义逐层拆解 → 状态机/终止条件 → 实操配置（每个论断挂仓库源文件链接）
- 宣言型：极简事实开场（empty git repository）→ 规模数据锚定 → 哲学宣言统治全文 → 失败方案"四宗罪"清单（每条升格为普适原则）

**approach-position**：宏观问题 → 双轨/框架明示 → 行动宣告（joining X / adding Y to all Z）→ 生态投资 → 信念陈述（we believe）→ **局限主动声明**（不能伪造≠不能欺骗）

## 频率标签操作化（壳中客可借鉴的家族风格）

把模糊概念定量化的固定模式：GDPval 的"60% 知识工作阈值"、监控文的"Common = less than 1% of overall traffic"、CoT-Control 的"0.1%–15.4%"——每个定性判断都配一个数字定义与出处。
