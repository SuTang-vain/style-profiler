# style-profiler · 研究性文章风格分析提取工具

> 针对**研究性文章**（深度报告、行业分析、研究综述、工程复盘）的风格拆解工具。
> 形态：Skill 主控（LLM 判断层）+ Python 确定性脚本（统计层）的混合架构。
> 设计哲学与《把 LLM 的不可控关进可验证的笼子》一致：**为每一维质量找一个确定性裁判**。

## 为什么不用现成工具

| 现有生态 | 缺口 |
|---|---|
| 营销号拆解 Skill（vicky-writer / wechat-article-writer / Goink） | 维度表为流量逻辑设计（钩子/情绪曲线/emoji），不适用论证逻辑 |
| 学术语步自动化（Mover / RWT / Kim 2024 LLM 标注） | 绑定英文研究论文文体，无中文媒体文体 |
| Deep Research 类工具 | 只做"资料→初稿"，不做风格对标与画像 |
| Stylometry 工具链（stylo 等） | 只回答"像不像"，回答不了"怎么写" |

本工具 = 学术方法（move analysis + argument mining + stylometry）的**中文研究性媒体适配** + 双模式闭环（拆解建档 → 稿件自检）。

## 目录结构

```
profiler.py                    # 统计层：~25 个确定性指标（中英双语，独立运行）
rubric/
  00-genre-routing.md          # 体裁路由：五体裁识别 + few-shot
  01-move-annotation.md        # 语步标注：七类语步 + 段落级叙事配比
  02-argument-annotation.md    # 论证标注：C/E/Q/R 组件 + 信源分层
templates/
  style-profile-template.md    # 《风格档案》输出模板
  genre-playbooks-openai.md    # OpenAI 四子体裁语步模板（10 篇全量标注定稿）
skills/style-profiler/SKILL.md # 生产流技能（Agent Skills 标准格式，跨平台，双模式）
corpus/                        # 语料（kezhongke 10 篇中文·五体裁各2 / openai 10 篇英文 / anthropic 10 篇英文）
output/                        # 每篇 JSON + _aggregate.json + 档案 + annotations/（output/kezhongke 为 24 篇全量存档，v10 子集结果在 output/kezhongke-v10）
```

## 安装（任意 Agent，三选一）

1. **skills.sh（推荐，跨平台）**：`npx skills add SuTang-vain/style-profiler` —— 自动适配 Claude Code、Codex CLI、Cursor 等兼容 Agent Skills 标准的平台。
2. **手动安装**：克隆本仓库，把 `skills/style-profiler/` 复制或软链到你的 Agent 技能目录（如 Claude Code 为 `~/.claude/skills/`，其他 Agent 参照各自技能目录约定）。skill 内所有资产路径均相对仓库根解析。
3. **零安装**：直接让 Agent 阅读本仓库的 `skills/style-profiler/SKILL.md` 作为指令执行——SKILL.md 本身即是完整操作手册。

依赖：`python3`；中文词汇指标需 `jieba`（`pip3 install jieba`，缺失时自动降级跳过）。

## 生产流接入

安装后对 Agent 说：
- **"分析 X 媒体的风格"** / **"给 X 建风格档案"** → 模式一（拆解建档）；
- **"发布前检查这篇稿"** / **"自检是否符合 X 的风格"** → 模式二（发布自检，对照已有档案基线 + 术语一致性/段落重复检查）。

档案现库：壳中客 v0.1（24 篇中文语料）、OpenAI v1（10 篇英文语料，全量标注）。

## 用法

### 模式一：拆解建档（对标媒体 → 风格档案）

```bash
# 1. 语料入库：把目标媒体的 md 文件放入 corpus/<媒体名>/
# 2. 跑统计层（确定性，全量必跑）
python3 profiler.py corpus/kezhongke/ -o output/kezhongke/
# 3. LLM 按 rubric 标注（判断层）：体裁路由 → 语步 → 论证
#    把 rubric/00→01→02 依次作为指令喂给 Agent，逐篇标注
# 4. 按 templates/style-profile-template.md 聚合成《风格档案》
# 5. 人工裁决 ⚑ 证据链条目，定稿
```

### 模式二：稿件自检（发布前对照）

```bash
# 单篇稿件对照已有《风格档案》：
python3 profiler.py draft.md
# 对照档案第 2 节的量化基线：越界指标即预警
# 术语一致性 / 段落重复：LLM 按 rubric 02 的 source_tier 与证据链核对
```

## 核心纪律

1. **统计归脚本，判断归 LLM，裁决归人**：数字密度、句长等只信 profiler.py；语步/论证 LLM 标注必须带 evidence_excerpt；⚑ 条目人工复核。
2. **聚合用中位数与四分位**，不用均值（防单篇长文拉偏）。
3. **每个画像结论必须带原文例证**（防风格去语境化——标签是压缩表示）。
4. **重跑抽检**：同篇语步标注重跑两次，不一致率 >15% 标 unstable。
5. **体裁先路由再统计**：混体裁聚合会洗掉风格信号。

## 方法出处

- 语步标注：Swales 体裁分析；Kim 2024 (JEAP) ChatGPT 语步标注；RAAMove 语料
- 论证组件：Stab & Gurevych (ACL C14-1142) claim-premise 模型
- 统计特征：stylometry（stylo / StyloMetrix 特征集），中文适配 jieba
- 维度框架：《研究性文章风格拆解 补充深度分析 2026-09》（论证层五维度 + 叙事-分析配比）

## 语料说明

`corpus/kezhongke/` 为项目方自有语料（壳中客研究社区，10 篇，五体裁各 2）。OpenAI / Anthropic 博客全文语料因版权不入库，采集方式与 slug 清单见 [corpus/README.md](corpus/README.md)；其分析产出（统计 JSON、标注、风格档案）保留在 `output/` 供参照。

## License

[MIT](LICENSE)（代码与文档）；`corpus/kezhongke/` 文章内容的著作权归壳中客社区所有。
