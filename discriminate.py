#!/usr/bin/env python3
"""跨机构风格判别分析（profiler.py 输出的第二层分析）

在 profiler.py 的单篇指标之上量化"机构间的风格差异是否可识别"：
  1. Mann-Whitney U 逐指标两两机构显著检验（探索性，未校正多重比较）
  2. 秩化 F 比率排序指标判别力（组间方差/组内方差）
  3. LOO 最近质心归属 + 混淆矩阵（单篇能否靠统计指标归属机构）
  4. 每机构 vs 余者 pooled 的最显著偏离指标（机构指纹）

用法: python3 discriminate.py [--json out]    # --json 输出归属明细
前置: 先跑 python3 profiler.py <corpus>/ -o output/<org>/
"""
"""跨机构风格判别分析：显著检验 + 判别力排序 + 质心归属（LOO）"""
import json, statistics, math
from pathlib import Path
from itertools import combinations

LIBS = {
    "cerebras": "output/cerebras", "eleuther": "output/eleuther",
    "databricks": "output/databricks", "openai": "output/openai",
    "anthropic": "output/anthropic",
}
METRICS = [  # (key, 组, 标签)
    ("word_count", "", "篇幅(词)"),
    ("avg_sentence_len", "sentences", "平均句长(词)"),
    ("p90_sentence_len", "sentences", "P90句长(词)"),
    ("avg_paragraph_len", "paragraphs", "平均段长(词)"),
    ("number_per_1k", "evidence", "数字密度/千词"),
    ("precise_per_1k", "evidence", "精确数字/千词"),
    ("year_per_1k", "evidence", "年份锚点/千词"),
    ("hedge_hits", "stance", "限定语/千词"),
    ("absolutist_hits", "stance", "断言绝对化/千词"),
    ("quantifier_hits", "stance", "全称量词/千词"),
    ("first_person_count", "stance", "第一人称"),
    ("objective_selfref_count", "stance", "客观自指"),
    ("questions", "stance", "问句数"),
    ("ttr", "diction", "TTR"),
]

def val(r, k, g):
    try:
        v = r[g][k] if g else r[k]
        return v if isinstance(v, (int, float)) else None
    except KeyError:
        return None

def mann_whitney_u(x, y):
    """两样本 Mann-Whitney U（双侧近似 p）"""
    n1, n2 = len(x), len(y)
    merged = sorted([(v, 0) for v in x] + [(v, 1) for v in y])
    ranks, i = {0: [], 1: []}, 0
    while i < len(merged):
        j = i
        while j < len(merged) and merged[j][0] == merged[i][0]:
            j += 1
        r = (i + 1 + j) / 2
        for k in range(i, j):
            ranks[merged[k][1]].append(r)
        i = j
    R1 = sum(ranks[0])
    U1 = R1 - n1 * (n1 + 1) / 2
    U2 = n1 * n2 - U1
    U = min(U1, U2)
    mu = n1 * n2 / 2
    sd = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)
    z = (U - mu) / sd
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return min(p, 1.0)

data = {}   # lib -> {metric -> [values]}
for lib, path in LIBS.items():
    data[lib] = {m[0]: [] for m in METRICS}
    for f in Path(path).glob("*.json"):
        if f.name == "_aggregate.json":
            continue
        r = json.load(open(f))
        for k, g, _ in METRICS:
            v = val(r, k, g)
            if v is not None:
                data[lib][k].append(v)

names = {k: v for k, _, v in METRICS}
libs = list(LIBS)

# 1) 显著性热力摘要：每指标「显著区分了几对机构」
print("=" * 76)
print("一、指标判别力（Mann-Whitney U，n=10/机构，探索性未校正）")
print("=" * 76)
sig_count = {}
for k, g, label in METRICS:
    n_sig = 0
    pairs = []
    for a, b in combinations(libs, 2):
        xa, xb = data[a][k], data[b][k]
        if len(xa) >= 4 and len(xb) >= 4:
            p = mann_whitney_u(xa, xb)
            if p < 0.05:
                n_sig += 1
                pairs.append(f"{a}×{b}")
    sig_count[k] = n_sig
    print(f"{label:12s} 显著区分 {n_sig}/10 对机构  {' '.join(pairs[:6])}")

# 2) 判别力排序：组间方差 / 组内方差（F 比率，去量纲：用 rank 归一）
def f_ratio(values_by_group):
    merged = sorted(v for vs in values_by_group for v in vs)
    n = len(merged)
    ranks = {v: i + 1 for i, v in enumerate(merged)}
    groups = [[ranks[v] for v in vs] for vs in values_by_group]
    allr = [r for g in groups for r in g]
    grand = statistics.mean(allr)
    ssb = sum(len(g) * (statistics.mean(g) - grand) ** 2 for g in groups)
    ssw = sum(sum((r - statistics.mean(g)) ** 2 for r in g) for g in groups)
    return ssb / max(ssw, 1e-9)

print("\n" + "=" * 76)
print("二、判别力排序（秩化 F 比率：组间差异/组内差异）")
print("=" * 76)
fr = []
for m in METRICS:
    k, g, label = m
    fr.append((f_ratio([data[l][k] for l in libs]), k, label))
for i, (f, k, label) in enumerate(sorted(fr, reverse=True), 1):
    print(f"  {i:2d}. {label:12s} F={f:.2f}  显著对={sig_count[k]}/10")

# 3) LOO 最近质心归属
print("\n" + "=" * 76)
print("三、LOO 最近质心归属（z-score 标准化指标向量）")
print("=" * 76)
use = [k for k, _, _ in METRICS]
# 全库合并求 mean/sd（按指标）
allv = {k: [] for k in use}
for l in libs:
    for k in use:
        allv[k] += data[l][k]
zs = {}
for l in libs:
    zs[l] = {}
    for k in use:
        vs = data[l][k]
        mu, sd = statistics.mean(allv[k]), statistics.pstdev(allv[k]) or 1
        zs[l][k] = [(v - mu) / sd for v in vs]

correct = {l: 0 for l in libs}
total = {l: 0 for l in libs}
conf = {a: {b: 0 for b in libs} for a in libs}
for true_l in libs:
    for i in range(len(zs[true_l][use[0]])):
        vec = [zs[true_l][k][i] for k in use]
        best, best_d = None, 1e18
        for cand in libs:
            c = [statistics.mean(zs[cand][k]) for k in use]
            d = math.sqrt(sum((vec[j] - c[j]) ** 2 for j in range(len(vec))))
            if d < best_d:
                best, best_d = cand, d
        total[true_l] += 1
        conf[true_l][best] += 1
        if best == true_l:
            correct[true_l] += 1

acc = sum(correct.values()) / max(sum(total.values()), 1)
print(f"总准确率：{acc:.0%}（{sum(correct.values())}/{sum(total.values())}）")
print(f"{'真实\\预测':12s}" + "".join(f"{l:>12s}" for l in libs))
for a in libs:
    print(f"{a:12s}" + "".join(f"{conf[a][b]:>12d}" for b in libs))
print(f"逐机构准确率：" + ", ".join(f"{l}={correct[l]}/{total[l]}" for l in libs))

# 4) 每机构 vs 全体其他：最大判别指标
print("\n" + "=" * 76)
print("四、每机构最显著偏离指标（vs 其余四库 pooled，Mann-Whitney）")
print("=" * 76)
for l in libs:
    best_k, best_p, best_dir = None, 1.0, ""
    for k, g, label in METRICS:
        x = data[l][k]
        rest = [v for ll in libs if ll != l for v in data[ll][k]]
        if len(x) >= 4 and len(rest) >= 4:
            p = mann_whitney_u(x, rest)
            if p < best_p:
                best_p = p
                best_k, best_dir = label, "高" if statistics.median(x) > statistics.median(rest) else "低"
    print(f"  {l:10s} 最显著: {best_k}（{best_dir}，p={best_p:.3f}）")
