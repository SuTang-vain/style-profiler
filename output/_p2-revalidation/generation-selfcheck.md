# 生成自检报告 · draft-v4-a-genre（A 分析评论类）

> 成稿：`output/_p2-revalidation/draft-v4-a-genre.md`（英文，3,102 词）
> 实测：`python3 profiler.py output/_p2-revalidation/draft-v4-a-genre.md`，原始输出存 `output/_p2-revalidation/draft-v4-a-genre.json`
> 日期：2026-09-14。执行依据：templates/genre-playbook-kezhongke.md（§0.2 处方走廊 + §4.1/§4.2 两层预算 + §1–§3 行业分析骨架 + §5–§7）。

## 1. 走廊指标逐条自评（全部 profiler 实测）

| 指标 | 目标 / 合格区间（§0.2） | 实测 | 判定 |
|---|---|---|---|
| 篇幅（词） | ≈2,900 / [2,100, 3,750] | 3,102 | ✅ 带内 |
| 平均句长（词） | ≈22 / [20, 24] | 22.1（median 22.0，144 句） | ✅ 贴目标 |
| P90 句长（词） | ≤35 / 硬上限 41 | 34 | ✅ |
| 平均段长（词） | ≈42 / [33, 53] | 49.7（median 55.0，64 段） | ✅ 带内偏上沿——按 A 格段长 delta +11.3 的方向性指示取上沿（§4.2） |
| 单句段（节拍器） | ≤4 处（处方 2） | 0 | ✅ |
| 数字密度 /千词 | ≈14 / [8, 21] | 12.57（39 tokens） | ✅ 带内，略低于中值 |
| hedge /千词 | ≈10 / [8, 13.5] | 11.93 | ✅ |
| absolutist /千词 | ≈2 / [1.4, 3.4] | 2.26（7 次：must×2, never×2, essentially, impossible, critical） | ✅ |
| 克制比 hedge:absolutist | 典型 4–5:1 / 红线 <3:1 | 5.3:1 | ✅ |
| 第一人称（次/篇） | ≈40 / [21, 69]（处方 6 硬约束） | 39（we/our/us，指从业者与采购共同体） | ✅ 贴目标 |
| 客观自指（次/篇） | 1–2 | 2（this essay ×2） | ✅ |
| 设问（次/篇） | 2–3 / [0, 5]（A 格 +1 已计入） | 3（正文 1 + CLOSE 设问自答 1 + 开放问题 1） | ✅ |
| 感叹号 | 0（红线） | 0 | ✅ |
| MATTR | 0.68–0.69 / [0.66, 0.70] | **0.713** | ❌ **未达标（高出上沿 0.013）**——见 §4 |
| 年份锚点 /千词 | 英文走廊未设；A 格 delta −1.0 方向性适用 | 4.19（13 处） | ⚠️ 方向偏离，见 §3 |

补充口径说明：profiler 规则层 genre 路由判定为 blog_or_exploration——其规则只识别中文标记（"本文将解答"等），对英文成稿不适用，不代表体裁偏离；语步序列按声明见 §2。

## 2. 语步序列声明（§2 骨架 + §3 行业分析实证序列 + §0.2 英文收尾组合）

```
HOOK（场景并置：2007 S&P "cows" 邮件场景 ∥ 2025  leaderboard 27 私有变体场景；叙事比 ≈0.9）
→ FRAME ×2（"It answers three questions" 三问题清单，开场第 3 段内完成；
            + 概念显式命名段：benchmark issuer / rating shopping / evaluation industry 固定句式定义、全程复用——处方 3）
→ CONTEXT（The License to Grade：1975 NRSRO 指定 → issuer-pays 转向 → 危机与和解史；唯一允许叙事的语步）
→ ARGUE ×4（Who Pays the Grader / The Inflation Machine / Shopping for the Grade / The Regulator Arrives Late；
            主体占比 ≈55%，略低于 2/3 实证配比——HOOK+CONTEXT 因题材为历史叙事而偏厚）
→ COUNTER（独立节 Four Objections, Two Verdicts：4 条质疑，2 rebutted + 2 left-open 显式标注——§5 默认处理配比）
→ APPLY（A Buyer's Discipline：四项测试清单 + "fails two or more should not enter a procurement decision" 可执行判据——§6 ✅例式）
→ CLOSE（§0.2 英文收尾组合：设问自答 → 编号结论 ×3 → 开放问题（中性，"证据未覆盖什么"）→ 比喻收束（license/ink/printing/cows 回收）；
        不含自我批评位）
```

承接装置（处方 7）：每个主节末句为指向下节的指针句（"The money comes first." → "the next mechanism is why the grades themselves keep rising." → "— and buyers can." → "where is the regulator in all of this?" → "the standard objections deserve a hearing of their own." → "A working discipline is needed now." → "it brings the argument back to the question we opened with."）；段首主题句＝该段结论，段间用 therefore / but / in practice / by contrast 类连接与指代链承接。

## 3. 两层预算 / delta 应用说明

- **格属**：A 分析评论类（n=11）。多数 delta≈0，机构层由 A 格居中，故英文硬约束直接采用 §0.2 处方走廊（§4 中文绝对值按 §0 不迁移条款不作硬约束）。
- **段长 delta +11.3（字，中文口径）**：方向性适用——英文段长取走廊上沿方向，实测 49.7/55.0（mean/median），贴 [33,53] 上沿。
- **年份锚点 delta −1.0**：方向未达标。本题是"历史重演"论证，日期是结构性证据（1975 指定、2007 降级潮、2015 和解、2020/2023 benchmark、2025 监管落地），实测 4.19/千词（13 处）。已压缩两轮：初稿 16 处 → 13 处（"mid-seventies""two years before the crisis""a decade later"等改相对表述）；再压缩将损伤论证的时间锚定功能。判定：题材性偏离，理由留存。
- **设问 delta +1**：已应用——3 次 = 机构层 2 + A 格 1。
- **人称**：处方 6 英文硬约束 [21,69]、目标 ≈40——预分配为 HOOK/FRAME 4、CONTEXT 5、ARGUE 各 4–6、COUNTER 3、APPLY 7、CLOSE 8；实测 39。
- **克制比**：英文相对比例口径（§0 可迁移项），实测 5.3:1，在典型 4–5:1 附近、远离 <3:1 红线。
- **参考条目/外链**：A 格参考条目 8、外链少量为中文语料口径；英文成稿未设参考文献节（信源分层改为行文内属性标注，见 §5 招式 2 迁移）。评审若要求英文稿也落参考条目，此为已知分歧点。

## 4. 未达标项及原因

**MATTR 0.713（走廊 [0.66, 0.70]，目标 0.68–0.69）——未达标，高出上沿 0.013。**

过程与原因：
1. 初稿 0.721；三轮术语归并（约 55 处稀有词→核心词替换，全部以"150 词窗口内已有该核心词"为生效条件验证）压至 0.713。
2. 继续下压的两个手段均与更高优先级约束冲突：(a) 语义失真替换（如 villains→pattern、university→rating）损害成稿质量；(b) 追加高重复度排比重述段违反处方 7"禁止无承接的排比式重申"。
3. 结构性原因：本题为历史对照叙事，专名密度高（Enron / Dodd-Frank / NRSRO / MMLU / SWE-bench / Scale AI / EU AI Act…），专名不可归并；且 §0.2 已记录"术语统一会拉低 MATTR"的方向性冲突（judge-v3），处方只承诺"贴带下沿"即低侧容差，未给高侧超标处方。
4. 参照系事实：anthropic 库 MATTR max=0.743、openai 库 max=0.724（_aggregate.json）——0.713 在两库实测文件范围内，仅出 IQR 包络。

**处置建议留给评审**：接受（题材性 + 库内实测范围内）或要求再压（需接受术语多样化下降的代价）。

## 5. 其他纪律清点

- **数字纪律**：39 tokens/12.57‰，全部趋势性/约数表述（roughly/about/some + 出处属性），无编造小数点假数据；关键定性判断均挂数字锚（1975、95%、40%、$1.4B/$864M、44%→90%、2%→70%、27 变体、49%/$14B、$500k、3% 罚则、600 页听证记录）。
- **信源分层（招式 2）**：官方（SEC's own reports / congressional findings / Senate investigators / EU AI Act）→ 第三方（reporting last year / a 2025 paper, outside researchers）→ 社区（community-run leaderboard）；转述全部带属性（according to / reportedly / by the paper's account）。
- **判断带边界（招式 3）**：结论句带数量/范围限定（most of / a small set of / two of them / fails two or more / mostly are too）。
- **边界声明 ≤3 处（处方 5）**：全文无自我检讨语气；局限表述仅 COUNTER 的 2 处 left-open（标注装置，非免责）与 CLOSE 的开放问题（judge-v3 划界：不计入限额）。未设自我批评小节。
- **单一比喻复用（招式 5）**：信用评级系统为唯一比喻体系（license / grade / safest grade / shopping / printing / ink / downgrade / cows 回收）；已清除初稿混入的第二比喻（gravity、wet cement、checkbox、arena、porous 等）。"teaching to the test"为领域固定术语，保留。
- **术语唯一**：benchmark issuer / rating shopping / evaluation industry / the grader / the graded 全文唯一形态。
- **CLOSE 区无重复段**；感叹号 0；emoji 0。
- **遗留**（诚实声明）：profiler 英文 genre 路由不适用（见 §1 注）；论据层 evidence_per_claim 未做 rubric 02 级标注自评（§5 本身为 [标注-1篇] 单篇外推口径）。
