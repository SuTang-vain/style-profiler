# corpus 语料说明

## 已入库

- `kezhongke/`：壳中客（Kezhongke，kezhongke.cn）研究社区文章 10 篇（CC 内容，项目方自有语料），五体裁各 2 篇；`genre-map.json` 为官方 section 覆盖映射。
- `cerebras/`、`eleuther/`、`databricks/`：一期语料扩展（2026-09-07，Kimi WebBridge 真浏览器抓取，见 `expansion-research.md`）。版权约定同 openai/anthropic：全文供本地分析，不分发；如需复现，按文件名 slug 从官方博客自采。
  - Cerebras 10 篇：cerebras.ai/blog 研究/工程深潜分层采样（排除纯产品新闻）；统计见 `output/cerebras/`，档案 `STYLE-PROFILE-cerebras-v0.md`
  - EleutherAI 10 篇：blog.eleuther.ai 研究深潜 + research-update（探索体英文原生形态）；统计见 `output/eleuther/`，档案 `STYLE-PROFILE-eleuther-v0.md`
  - Databricks 10 篇：databricks.com/blog AI RESEARCH 栏目全量；统计见 `output/databricks/`，档案 `STYLE-PROFILE-databricks-v0.md`
- `google-research/`、`microsoft-research/`：二期语料（2026-09-07，WebBridge 真浏览器抓取）。**版权政策同上：全文不入库**（2026-09-07 授权核实：Google ToS 保留全部 IP、Microsoft TOU 明文禁止复制分发，均无 CC 授权；文件曾被误跟踪并已从全部历史中清除）。slug 清单见各自档案第 5 节，如需复现请自采；分析产出（统计 JSON、标注、档案）正常入库。
  - Google Research 10 篇：research.google/blog 栏目分层（含连接组学/甲烷监测等合作科学体）；统计见 `output/google-research/`，档案 `STYLE-PROFILE-google-research-v0.md`
  - Microsoft Research 10 篇：microsoft.com/en-us/research/blog（正文为摘要式短文，深度内容靠论文/开源外链）；统计见 `output/microsoft-research/`，档案 `STYLE-PROFILE-microsoft-research-v0.md`

## 本地在库、不随仓库分发（版权原因）

`openai/` 与 `anthropic/` 为对应公司博客全文（**2026-09-08 按 slug 重采入本地**，.gitignore 挡住；政策同其他第三方：本地分析可、git 分发不可）。如需复现 `output/openai/`、`output/anthropic/` 中的分析结果，请自行从官方博客采集对应文章（文件名按 slug 命名即可对齐输出文件）。**slug 修正记录（重采时实测，原清单 3 个不完整）**：
- `effective-harnesses-long-running-agents` → 实际 URL 为 `/engineering/effective-harnesses-for-long-running-agents`（多 "for"）
- `effective-context-engineering` → `/engineering/effective-context-engineering-for-ai-agents`（多 "for-ai-agents"）
- `responsible-scaling-policy` → `/news/anthropics-responsible-scaling-policy`（初版 2023-10；另一版 `announcing-our-updated-responsible-scaling-policy` 为 RSP 2.0——原外部 workspace 版本不可考，本地取初版）
- OpenAI 全部 slug 有效，但需加 `/en/` 前缀（`openai.com/en/index/<slug>/`）避免按浏览器语言重定向到中文版：

**OpenAI（10 篇）**：harness-engineering / gpt-5-safe-completions / core-dump-epidemiology-data-infrastructure-bug / how-we-monitor-internal-coding-agents-misalignment / emergent-misalignment / unrolling-the-codex-agent-loop / reasoning-models-chain-of-thought-controllability / understanding-the-source-of-what-we-see-and-hear-online / our-approach-to-the-model-spec / gdpval

**Anthropic（10 篇）**：a-postmortem-of-three-recent-issues / auditing-hidden-objectives / effective-harnesses-long-running-agents / agentic-misalignment / demystifying-evals-for-ai-agents / responsible-scaling-policy / building-c-compiler / effective-context-engineering / building-effective-agents / alignment-faking

采集后运行：

```bash
python3 profiler.py corpus/openai/ -o output/openai/
```
