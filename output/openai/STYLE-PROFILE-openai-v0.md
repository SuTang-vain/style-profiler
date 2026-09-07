# 《OpenAI Blog（Engineering/Research 板块）》风格档案 v1（标注全量定稿）

> 生成日期：2026-09-06（v1 定稿：10/10 篇全量标注完成，四子体裁模板见 templates/genre-playbooks-openai.md）｜ 语料：10 篇英文文章（2024-05 至 2026-06-30）｜ 采样：研究叙述 ×2、评测报告 ×3、工程深潜 ×3、立场方法 ×2
> 生成方式：profiler.py 英文适配层（v0.2）+ rubric 全量标注（每篇语步骨架 + 论证组件）

## 1. 风格画像

**一线研究者的"侦探故事"文体**：以第一人称复数（we）叙述一次真实的调查过程——包括失败、错误假设与认知反转——最终把教训提炼为普适原则。读者被默认为技术同行；说服力不靠外部权威（几乎零引用、零外链），靠**自产证据 + 过程透明 + 数量级推理**。
⚑ 例证："This was the turning point."（三个词独立成段——研究叙事的节拍器）

## 2. 量化基线（10 篇，median）

| 指标 | OpenAI（/千词） | 壳中客（/千字）对照 |
|---|---|---|
| 篇幅 | 2,819 词 ≈ 中文学 5.6K 字 | 3,905 字 |
| 平均句长 | 22.2 词 | 33.6 字（≈中等偏长，两库相当）|
| 数字密度 | 16.1 | 18.1（相当）|
| 精确数字 | 1.06（低——用数量级不用精确值）| 5.07（高——精确值癖）|
| 限定语 hedge | **8.8** | 3.1（OpenAI 高 3 倍）|
| 断言型绝对化 | 1.64 | 1.05 |
| 第一人称 | **59** | 5（OpenAI 高 12 倍）|
| 客观自指 | 0.5 | 1 |
| 外链/千词 | **0** | 0（median；但壳中客行业分析有内文外链）|
| 参考文献条目 | **0** | 6（壳中客有规范参考节）|
| 感叹号 | 0（10 篇共 2 个，均在戏剧高潮）| 0 |
| TTR | 0.31 | 0.37 |
| **指纹**（discriminate.py，vs 其余四库） | **精确数字最低**（1.06 vs ~2.3，p=0.023） | — |

> 指纹解读：侦探叙事用数量级而非精确值——数字密度（16.1）不低但精确值极少，唯一精确值留给关键证据（0.1%–15.4%）。
| 标题冒号式 | 3/10（名词短语+冒号副题）| 9/24 |

## 3. 结构模板（语步层，core-dump 篇标注 + 全库观察）

```
无 HOOK（不设场景钩子，"First, let's go deeper on X" 直接切入）
→ CONTEXT（系统/原理铺垫，占 25-30%）
→ FRAME（方法框架声明："Our initial approach was to…"）
→ ARGUE×n（调查叙事：尝试→失败→转向→突破，占主体）
   ⊙ COUNTER 全部内化：自我假设的错误自白
     ——"we (incorrectly) ruled out" / "exactly backward" / "That surprised us"
   ⊙ 单句段 = 戏剧节拍器
     ——"That pushed us toward the kernel." / "This was the turning point."
     ——"The answer was yes." / "That's the bug."
→ APPLY（缓解措施 + 上游贡献 + 承诺 reinforcement of commitment）
→ CLOSE（教训提炼 → 普适原则 → 格言收束）
```

与壳中客的关键差异：
- **推进引擎不同**：OpenAI 靠"调查过程的故事弧"（悬念在'我们如何找到答案'），壳中客靠"论证义务的对峙"（悬念在'结论是否成立'）
- **反驳方向不同**：OpenAI 的质疑指向自己（研究诚实作为风格），壳中客指向外部（呈现反方观点再回应）
- **比喻功能不同**：OpenAI 的比喻是方法论命名（doctor vs epidemiologist 直接做章节标题），壳中客的概念比喻（修路）用于解释机制

## 4. 论证规范

- 证据配比：evidence_per_claim ≈ 1.5-2.0（与壳中客 1.8 相当）
- **信源结构相反**：OpenAI 以 self（自产管道/自产数据/自产估算）+ external-artifact（源码/PR）为主，几乎无 third-party 转述；壳中客 third-party 44% + community 44%
- 数量级论证：Fermi estimation 是标志性招式（10^-8 概率 × 10^4 次/秒 → 数小时一崩），宁要量级正确不要精确值——与壳中客的精确值癖（4.6→28.3、1e-7 量级）相反
- hedge 密度高：may/might/seems/roughly/Maybe——结论以概率化语气交付；壳中客 hedge 靠信源转述式（据报道/以官方为准）
- 限定与诚实：无法复现、错误排除、意外发现全部如实写入——**承认无知是可信度来源**

## 5. 用词与语言

- 高频实词：data, model, system, training, research, safety, scale（术语直接用、无括注翻译问题）
- 句式：主语几乎总是 we + 动作动词（we tried / we found / we decided）；被动语态极少
- 比喻纪律：每篇至多一个中心比喻，且承担结构性功能（命名章节/统摄教训）
- 章节标题：疑问句与名词短语（"Why did the libunwind bug appear now?" "Doctor or epidemiologist?"）——标题即叙事节点的钩子

## 6. 正反例库

| | 例证 | 说明 |
|---|---|---|
| ✅ | "We weren't able to find anything that seemed related." | 失败路径如实记录，构成研究诚实 |
| ✅ | "Reliability is not just about fixing bugs after they happen—it's about building the data, workflows, and skills…" | 教训格言化：X is not just about A—it's about B 句式 |
| ✅ | "This was the turning point." | 单句段节拍器 |
| ❌ | 文内罗列第三方观点再逐条回应（壳中客式）| OpenAI 不做外部对峙，质疑只来自自己 |
| ❌ | 文末参考文献表 | 全库 0 参考节；信源用内联链接（the fix (opens in a new window)）|
| ❌ | 精确值堆叠（"57 分""643→5330"式）| 用 one-instruction wide / a hundred picoseconds 等量级表达 |

## 7. 与壳中客基线的五点对照结论

1. **可信度来源相反**：OpenAI = 自产证据 + 过程透明；壳中客 = 外部信源三角验证 + 信源分层。两者都是"可核验"路线，但一个是"我做了给你看"，一个是"各方怎么说我帮你核对"。
2. **人称策略相反**：we 主导（59/篇）vs 客观自指主导。壳中客若吸收 OpenAI 式过程叙事，第一人称需在"编辑说明"之外解禁。
3. **叙事-分析配比**：OpenAI 全程是叙事化论证（故事弧承载论证），壳中客是论证主体+叙事佐料（FDE 篇 ≈0.25，core-dump ≈0.1 但叙事以"调查动作"形式存在）。
4. **共通红线**：感叹号≈0、无 emoji、结论带限定——两个体系的克制气质一致，验证了"研究性文风"的跨语言共性。
5. **可吸收项（若壳中客想借鉴）**：单句段节拍器、调查失败的自白式记录、教训格言化收束（"X is not just about A—it's about B"）、设问式章节标题。**不应吸收项**：零引用实践（与壳中客信源分层纪律冲突——那是它的差异化资产）。

## 8. 校准日志

- 2026-09-06：v0 生成。10 篇浏览器抓取（Cloudflare 验证自动通过）；profiler 英文适配层上线（语言检测/英文词表/词数分句）；core-dump 篇全篇标注示范。
- 已知局限：① 采样偏研究/工程板块，产品公告类未采样；② OpenAI 部分文章有系统卡外链 PDF，正文抓取未含附件；③ 单篇标注示范，体裁层模板待其余 9 篇标注后定稿。
