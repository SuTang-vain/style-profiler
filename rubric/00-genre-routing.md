# Rubric 00 · 体裁路由（Genre Routing）

> 用途：标注前第一步。体裁决定后续用哪套语步模板与基线，混体裁统计会洗掉风格信号。
> 方法：规则层（profiler.py 已给 genre_guess 初判）+ LLM 复核。本文件是 LLM 复核规范。

## 五个体裁（对齐壳中客 section 体系）

| 体裁 | 识别特征（满足 ≥3 条即可判） | 对应写作传统 |
|---|---|---|
| **报告体 report** | 元信息头（报告日期/数据截止/版本/分析对象/信息来源）；摘要节；编号章节；对比数据表；附录数据核验 | 行业研究机构报告 |
| **期刊体 journal** | "引言"节；"结论与讨论"节；三级编号（2.1/2.3）；文内 [n] 引用 + GB/T 文献表（[J]/[C]/[M]）；零第一人称 | 学术论文 IMRaD |
| **行业分析 industry** | 事件/场景化开场；数据锚定（岗位数、融资额）；明示"本文解答 N 个问题"；反面观点检验；编辑说明/信源征集 | WSJ 体研究化变体 |
| **博客体 blog** | 工程复盘叙事（失败→机制→处方）；第一人称出现在叙事段；代码块/表格为证据；"参考来源"非 GB/T 格式 | 工程博客深度文 |
| **探索体 exploration** | 理论建构带版本号（vX.X）与变更日志；概念自造并自证；明确标注未完成/免责 | 思想随笔/工作论文 |

## 输出契约

```json
{
  "genre": "report | journal | industry | blog | exploration",
  "confidence": "high | medium | low",
  "evidence": ["特征1（引原文≤15字）", "特征2", "特征3"],
  "mixed_with": "若含其他体裁成分，注明如 'report + blog 叙事段'"
}
```

## 规则

1. 优先信规则层命中（profiler 的 genre_guess）；规则层与 LLM 判断冲突时，**以特征证据多者胜**，并在输出中注明冲突。
2. 一篇文章只给一个主体裁，但 `mixed_with` 必须如实标注混合成分（如 FDE 系列是 industry 主体 + blog 的叙事段）。
3. confidence=low 时，该篇进入聚合统计时应单独分组，不并入任何体裁基线。

## Few-shot

**输入特征**：元信息头 + 摘要 + 目录 + "附录：数据核验与来源说明" →
**输出**：`{"genre":"report","confidence":"high","evidence":["元信息头四件套","摘要节","数据核验附录"],"mixed_with":""}`

**输入特征**：场景开场（"2026年5月的同一天…"）+ "本文将解答三个问题" + 反方观点节 + 文末编辑说明 →
**输出**：`{"genre":"industry","confidence":"high","evidence":["场景化开场","明示问题框架","编辑说明与信源征集"],"mixed_with":"blog 叙事段约 15%"}`

## 英文机构博客子体裁（2026-09-08 回填定稿）

> 依据：7 库 ≥3 篇语步标注（output/_moves-aggregate.md）+ 各库 genre-playbook + 判别实证。
> 适用对象：英文 AI 研究机构博客（openai/anthropic/cerebras/eleuther/databricks/google-research/microsoft-research）。
> 与中文五体裁的关系：英文侧主体裁 = 下列五类；中文五体裁的英文对应见映射表（探索体例外，见 5）。

| 子体裁 | 识别特征（满足 ≥3） | 代表篇目 | 语步签名（3 篇聚合实证） |
|---|---|---|---|
| **research-narrative** 研究叙述 | 结论前置摘要段（"We show that:"式要点）；自产证据推进；概念命名句（"We refer to this as X"）；论文外链兜底 | emergent-misalignment、alignment-faking、autointerp | ARGUE 51-83%；叙事段 0-9%；变体见下 |
| **evaluation-report** 评测报告 | 自建工具/基准命名；数字区间结论（"0.1%–15.4%"）；Limitations 独立成节；制度承诺收束 | gdpval、officeqa-pro-v2、Z.ai Code Bench 类 | FRAME 成果前置→评测设置→结果→边界 |
| **engineering-deep-dive** 工程深潜 | 第一人称调查/教学叙事；系统自建；"失败→转折→教训"或模式目录结构 | core-dump、knowledge-base、orchard | ARGUE 块×n 同构嵌套；COUNTER 内化或独立节 |
| **approach-position** 立场方法 | we believe 高频；行动宣告；局限主动声明；治理词汇 | model-spec、responsible-scaling-policy、common-pile | 立场声明节 + 质疑-回应单元（COUNTER） |
| **exploration（英文）** 探索体 | 理论建构带版本号；概念自造自证；明确标注未完成 | 候选：dynamical-models（**未标注，待验证**） | 待 ≥3 篇后定 |

### research-narrative 的三个库内变体（证据分级：标注-N 篇）

1. **论文复述型**（EleutherAI 主形态）：Key Findings 前置 + 图注段占 1/3 + 零叙事零 COUNTER——ARGUE 83%（六库最高）
2. **进度报告型 research-report**（MAD Research Update 实证）：结果前置 + "Interim report" 定位 + 负面收束（"deprioritising"）——**非探索体**（无概念自造/版本号，2026-09-08 修正原假设）
3. **合作科学型**（Google Research）：机构署名双人制 + APPLY 跨域扩展轴（"已推广到 X"）+ 图注驱动

### 修正史（防单篇外推复发）

- databricks "零 COUNTER" 被 3 篇聚合推翻（memory-scaling 有完整反驳节）——COUNTER 是**子体裁特征**（研究展望文有、系统文无），不是库特征
- google "无 HOOK" 被推翻（empty-shelves 设问开场）——同理按子体裁分论
- **教训**：库级结构结论必须 ≥3 篇聚合（② 纪律），识别特征表按子体裁而非机构声明

### 中英体裁映射

| 中文 | 英文对应 | 备注 |
|---|---|---|
| 报告体 | evaluation-report | 元信息头为中文报告体独有信号 |
| 期刊体 | research-narrative（论文复述型） | GB/T 文献表为中文期刊体独有 |
| 行业分析 | approach-position / 事件驱动型 research-narrative | 场景 HOOK+编辑说明为中文独有 |
| 博客体 | engineering-deep-dive | 教学型变体两语皆有 |
| 探索体 | 待定 | dynamical-models 标注后回填 |
