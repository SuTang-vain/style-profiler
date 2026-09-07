---
name: style-profiler
description: 研究性文章风格分析与提取工具，双模式。模式一「拆解建档」：当用户要求分析/拆解某媒体、公众号、博客的文章风格，提取写作结构、语言风格、用词特征，生成《风格档案》时使用。模式二「发布自检」：当用户要求在发布前检查稿件是否符合某风格档案/栏目规范（句长、限定语、术语一致性、段落重复等）时使用。适用中文与英文研究性文章（深度报告、行业分析、研究综述、工程复盘）。
---

# Style Profiler · 研究性文章风格分析与自检

针对**研究性文章**（非营销号）的风格拆解工具。架构：Python 统计层（确定性指标，完全可信）+ LLM 标注层（按 rubric，必须带原文证据）+ 人工裁决位（⚑ 条目）。

**项目根目录（所有路径以此为基准）**：本文件向上两级的目录（即包含 `profiler.py` 的仓库根目录）。

| 资产 | 路径（相对项目根） |
|---|---|
| 统计层脚本 | `profiler.py` |
| 体裁路由 rubric | `rubric/00-genre-routing.md` |
| 语步标注 rubric | `rubric/01-move-annotation.md` |
| 论证标注 rubric | `rubric/02-argument-annotation.md` |
| 风格档案模板 | `templates/style-profile-template.md` |
| OpenAI 四子体裁模板（参照系） | `templates/genre-playbooks-openai.md` |
| 已有档案：壳中客 v0.1 | `output/kezhongke/STYLE-PROFILE-kezhongke-v0.md` |
| 已有档案：OpenAI v1 | `output/openai/STYLE-PROFILE-openai-v0.md` |

## 模式一：拆解建档（对标媒体 → 《风格档案》）

用户说"分析 X 媒体的风格 / 给 X 建风格档案 / 拆解 X 的写法"时执行：

### Step 1 语料采集（目标 10-15 篇，按栏目分层而非按爆款）
- 有 URL 清单：用浏览器逐篇打开（OpenAI 类站点会遇到 Cloudflare 验证壳，等待 3-6 秒自动通过后确认 `tab.title()` 不含 "Just a moment" 再提取），正文提取用 `document.querySelector('article')` 遍历 `h1-h3/p/li/blockquote` 转 Markdown。
- 有本地文件（md/PDF 转 md）：直接复制进 `corpus/<媒体名>/`。
- 清理：去掉页面 sticky 目录重复、导航残留；排除非文章文件（英文 SKILL 原文等）——记录在档案语料说明里。

### Step 2 统计层（全量必跑，结果只信这里）
```bash
cd <项目根目录>
python3 profiler.py corpus/<媒体名>/ -o output/<媒体名>/ --exclude '<排除glob>'
# 已知官方分类时加 --genre-map corpus/<媒体名>/genre-map.json
```
输出：每篇 JSON + `_aggregate.json`（中位数 + P25/P75，**不用均值**）。

### Step 3 LLM 标注（按 rubric 顺序执行）
1. **体裁路由**（rubric/00）：每篇判定五体裁之一（中文）/子体裁（英文站），输出 JSON 含 confidence + evidence；规则层已判的直接复核，low confidence 的篇目单独分组。
2. **语步标注**（rubric/01）：逐段标注七类语步（HOOK/FRAME/CONTEXT/ARGUE/COUNTER/APPLY/CLOSE），每条必带 ≤20 字 evidence_excerpt + narrative_ratio。
3. **论证标注**（rubric/02）：claims/evidence/qualifiers/rebuttals 组件图 + 信源四档分层 + 反驳处理结果（rebutted/left-open）。

### Step 4 生成《风格档案》
按 `templates/style-profile-template.md` 聚合：画像 → 量化基线表 → 结构模板 → 论证规范 → 用词 → 正反例库（每条带原文 ⚑）。与已有档案（壳中客/OpenAI）做差异对照是增值步骤。

### Step 5 人工裁决项（必须明确告知用户）
画像定性综合、禁忌清单、正反例取舍——机器出初稿，人定稿。

## 模式二：发布自检（稿件 × 档案基线 → 自检报告）

用户说"发布前检查 / 自检这篇稿 / 是否符合 X 的风格"时执行：

1. **跑统计层**：`python3 profiler.py <稿件.md>` 得单篇指标。
2. **对照基线**：与目标档案第 2 节的 median/P25–P75 逐项比对，越界指标预警（示例红线：感叹号、emoji、限定语下限、句长区间）。
3. **LLM 检查项**（统计层测不了）：
   - 术语一致性：同一概念是否一文多译（壳中客 FDE 篇教训：FDE 出现 5 种译法 + "全磁盘加密"误译）
   - 段落重复：CLOSE 区是否有重复段（FDE 篇 para 36 教训）
   - 反驳模块：行业分析/报告体裁必须含 COUNTER 节，且未解决的反驳如实标注 left-open
   - 比喻纪律：中心比喻是否贯穿且服务概念
4. **输出自检报告**：✅ 达标项 / ⚠️ 越界项（指标值 vs 基线区间）/ ❌ 红线项（感叹号、无来源判断、术语漂移），附修改建议。

## 纪律（不可违反）

1. **统计归脚本，判断归 LLM，裁决归人**：数字密度/句长/词频只信 profiler.py；LLM 标注必须带原文证据，无证据的标注作废。
2. **每个画像结论必须附原文例证**（⚑）——防风格去语境化（标签是压缩表示，输出会滑向统计平均）。
3. **聚合用中位数与四分位区间**，不用均值。
4. **体裁先路由再统计**：混体裁聚合会洗掉风格信号。
5. **重跑抽检**：关键篇目语步标注重跑两次，不一致率 >15% 标 unstable。
6. **语料保鲜**：媒体文风会漂移，档案每季度用新样本重跑更新（写入校准日志）。
7. **边界**：拆解产物是风格结论 + 短例证（≤40 字），不复制原文段落；仿写风格与结构模式，不搬运内容与素材。
