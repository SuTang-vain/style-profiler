# Rubric 02 · 论证与证据标注（Argument Annotation）

> 方法依据：argument mining 的组件-关系模型（Stab & Gurevych 的 claim-premise-support/attack）映射到研究性媒体文章；自动预期据学术共识调低——媒体文体论证标记比学术议论文松散，本 rubric 定位为 **LLM 初稿 + 人工裁决**。
> 标注对象：全篇一次（结构图），不逐段。

## 组件类目

| 代码 | 组件 | 定义 |
|---|---|---|
| C | 主张 Claim | 作者要读者接受的判断（含分论点） |
| E | 证据 Evidence | 数据、引语、文献、案例、代码/实验结果 |
| Q | 限定 Qualifier | 主张的边界声明（"在…范围内""仅在闭源对比中"） |
| R | 让步/反驳 Rebuttal | 反方观点及其处理 |

## 关系类型

- `supports`：E → C（证据支撑主张）
- `specifies`：C → C（主张细分为主张）
- `qualifies`：Q → C（限定收窄主张）
- `rebuts`：R → C（反驳/让步指向被限定的主张）

## 输出契约

```json
{
  "claims": [
    {"id": "C1", "text": "≤30字主张转写", "level": 1},
    {"id": "C2", "text": "…", "level": 2, "parent": "C1"}
  ],
  "evidence": [
    {"id": "E1", "type": "data|quote|citation|case|artifact", "supports": "C2",
     "source_tier": "official|third-party|community|self", "excerpt": "≤20字"}
  ],
  "qualifiers_on": ["C1"],
  "rebuttals": [{"text": "≤25字", "targets": "C2", "resolution": "accepted|rebutted|left-open"}],
  "conclusion_form": "open-questions | action | outlook | restrained-close",
  "stats": {
    "claims_total": 0, "evidence_total": 0,
    "evidence_per_claim": 0.0,
    "source_tier_ratio": {"official": 0.0, "third-party": 0.0, "community": 0.0, "self": 0.0},
    "first_party_vs_second_party": "一手信源占比 vs 二手转引占比（0-1）",
    "qualifier_density": "qualifiers_on 数 / claims_total"
  }
}
```

字段纪律：
- `source_tier` 是信源分层维度：official=官方原文/一手数据；third-party=媒体/机构转述；community=论坛/从业者讨论；self=作者自产实验或推演。
- `resolution`：反驳的三种处理结果必须区分——"接受并收窄主张"（accepted）是研究性文章的高质量信号。
- `conclusion_form` 与修正版维度框架的"结论形态"对齐。

## 与统计层的分工（防重复劳动）

- 每千字数字密度、引用条数、外链数：**以 profiler.py 脚本结果为准**，本 rubric 的 stats 不重复计算，只做组件级比值（evidence_per_claim 等）。
- 人工裁决位：claims 的 level/parent 关系、rebuttals 的 resolution、结论形态，这三项抽检时优先人审。

## Few-shot

**输入**（FDE 一文节选）："有质疑认为这是岗位改名；但从业者复盘显示工作内容确实横跨交付与工程；本文给出四项判断标准。"
**标注**：
```json
{"claims":[{"id":"C1","text":"FDE 是真实的岗位形态而非改名","level":1}],
 "evidence":[{"id":"E1","type":"quote","supports":"C1","source_tier":"community","excerpt":"从业者复盘显示"}],
 "rebuttals":[{"text":"质疑：岗位改名论","targets":"C1","resolution":"rebutted"}],
 "conclusion_form":"action"}
```

**输入**（GLM 报告节选）："Artificial Analysis 智能指数 57 分，与 Opus 4.8 持平——据官方口径，尚待第三方复测。"
**标注**：
```json
{"claims":[{"id":"C1","text":"Flash 智能水平追平 Opus 4.8","level":1}],
 "evidence":[{"id":"E1","type":"data","supports":"C1","source_tier":"official","excerpt":"57 分"}],
 "qualifiers_on":["C1"],
 "stats":{"evidence_per_claim":1.0,"qualifier_density":1.0}}
```
