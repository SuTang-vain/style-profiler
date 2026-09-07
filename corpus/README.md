# corpus 语料说明

## 已入库

- `kezhongke/`：壳中客（Kezhongke，kezhongke.cn）研究社区文章 10 篇（CC 内容，项目方自有语料），五体裁各 2 篇；`genre-map.json` 为官方 section 覆盖映射。

## 未入库（版权原因）

`openai/` 与 `anthropic/` 两个语料库为对应公司博客的全文拷贝，不随本仓库分发。如需复现 `output/openai/`、`output/anthropic/` 中的分析结果，请自行从官方博客采集对应文章（Markdown 格式，文件名按下表 slug 命名即可直接对齐输出文件）：

**OpenAI（10 篇）**：harness-engineering / gpt-5-safe-completions / core-dump-epidemiology-data-infrastructure-bug / how-we-monitor-internal-coding-agents-misalignment / emergent-misalignment / unrolling-the-codex-agent-loop / reasoning-models-chain-of-thought-controllability / understanding-the-source-of-what-we-see-and-hear-online / our-approach-to-the-model-spec / gdpval

**Anthropic（10 篇）**：a-postmortem-of-three-recent-issues / auditing-hidden-objectives / effective-harnesses-long-running-agents / agentic-misalignment / demystifying-evals-for-ai-agents / responsible-scaling-policy / building-c-compiler / effective-context-engineering / building-effective-agents / alignment-faking

采集后运行：

```bash
python3 profiler.py corpus/openai/ -o output/openai/
```
