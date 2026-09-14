#!/usr/bin/env python3
"""跨机构风格判别分析（两层模型口径：体裁对体裁，2026-09-14 改造）

改造依据 docs/methodology-two-level-style-model.md §三：
  1. 体裁对体裁：只在同体裁格之间比较（per-article JSON 的 genre.unified.code 分格，
     格内 n≥3 才出库，与 aggregate_two_level.py 同口径）；机构无该格则退出该组比较
     ——分离"写法差异"与"体裁构成差异"（旧全库口径混入构成差异，仅留作对照）
  2. FDR 族分列：族 = 体裁格（格内 指标×库对 全部检验为一个 BH 族），各族内分别校正；
     机构指纹独立一族（库×体裁格×指标，pooled = 同体裁格内其余各库篇目合并）
  3. 机构层指纹值表用 inst(L,m)（体裁中位的中位，取自各库 _aggregate.json two_level）
  4. 报告同附各库体裁构成表（构成差异是事实，只是不再污染指纹）

声明：探索性分析，n=10/机构、格内 n≥3，未预注册；显著性以 BH-FDR q<0.05 为准。
kezhongke 不参与：跨语种分母（字/词）与词表不同，秩检验可比性存疑（见该库档案注记）。
MATTR 依赖正文长度 ≥150 词窗口，格内短篇自动缺数（覆盖注记随表给出）。

用法: python3 discriminate.py > output/_group-discrimination.txt
前置: python3 aggregate_two_level.py（机构层指纹值表读 two_level.institution）
"""
import json, math, statistics, sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from aggregate_two_level import load_articles  # noqa: E402  同口径文章识别

LIBS = {
    "cerebras": "output/cerebras", "eleuther": "output/eleuther",
    "databricks": "output/databricks", "openai": "output/openai",
    "anthropic": "output/anthropic",
    "googleResearch": "output/google-research", "microsoftResearch": "output/microsoft-research",
}
# _aggregate.json 目录名映射（机构层指纹值表用）
AGG_DIR = {"googleResearch": "google-research", "microsoftResearch": "microsoft-research"}
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
    ("ttr", "diction", "TTR(长度敏感)"),
    ("mattr", "diction", "MATTR(w=150)"),
]
GENRE_NAMES = {"A": "分析评论类", "E": "工程类", "R": "研究类",
               "N": "公告类", "P": "政策类", "G": "指南类"}
MIN_CELL_N = 3  # 格内 n≥3 才出库（与 aggregate_two_level 同纪律）
# 内参指标：保留计算供参照，但不参与判别力排序——其"显著"来自已知混淆
# （TTR 的组间差异主要是篇幅效应，等长窗口 MATTR 才是文体成分）
REFERENCE_ONLY = {"ttr"}


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


def bh_fdr(pvals):
    """Benjamini-Hochberg FDR：{检验id: p} -> {检验id: q}（单调调整）"""
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m = len(items)
    q = {}
    prev = 1.0
    for rank, (kid, p) in reversed(list(enumerate(items, 1))):
        prev = min(prev, p * m / rank)
        q[kid] = min(prev, 1.0)
    return q


def f_ratio(values_by_group):
    """秩化 F 比率：组间方差/组内方差（去量纲）。"""
    merged = sorted(v for vs in values_by_group for v in vs)
    ranks = {}
    i = 0
    while i < len(merged):  # 并列取平均秩
        j = i
        while j < len(merged) and merged[j] == merged[i]:
            j += 1
        r = (i + 1 + j) / 2
        for v in merged[i:j]:
            ranks.setdefault(v, r)
        i = j
    groups = [[ranks[v] for v in vs] for vs in values_by_group]
    allr = [r for g in groups for r in g]
    grand = statistics.mean(allr)
    ssb = sum(len(g) * (statistics.mean(g) - grand) ** 2 for g in groups)
    ssw = sum(sum((r - statistics.mean(g)) ** 2 for r in g) for g in groups)
    return ssb / max(ssw, 1e-9)


# ---------- 数据装载 ----------

def load_flat():
    """旧口径（对照用）：lib -> {metric: [全库 values]}，coverage 门槛 ≥4。"""
    data = {}
    for lib, path in LIBS.items():
        data[lib] = {m[0]: [] for m in METRICS}
        for r in load_articles(ROOT / path):
            for k, g, _ in METRICS:
                v = val(r, k, g)
                if v is not None:
                    data[lib][k].append(v)
    coverage = {k: [l for l in LIBS if len(data[l][k]) >= 4] for k, _, _ in METRICS}
    return data, coverage


def load_cells():
    """新口径：lib -> {体裁代码: {metric: [格内 values]}}；只保留 n≥3 的格。
    格内指标缺数（如短文的 mattr）按实际非空值计，检验时再按 ≥n 门槛过滤。"""
    cells = {}
    for lib, path in LIBS.items():
        by_genre = {}
        for r in load_articles(ROOT / path):
            unified = r.get("genre", {}).get("unified")
            code = unified.get("code") if isinstance(unified, dict) else None
            if code:
                by_genre.setdefault(code, []).append(r)
        cells[lib] = {}
        for code, arts in by_genre.items():
            if len(arts) >= MIN_CELL_N:
                cells[lib][code] = {
                    k: [v for a in arts if (v := val(a, k, g)) is not None]
                    for k, g, _ in METRICS
                }
    return cells


# ---------- 新口径检验 ----------

def libs_in_cell(cells, genre, metric, min_n=MIN_CELL_N):
    """该体裁格内、该指标有 ≥min_n 个值的库。"""
    return [l for l in cells
            if genre in cells[l] and len(cells[l][genre].get(metric, [])) >= min_n]


def cell_pairwise(cells):
    """体裁格两两比较：{genre: {(metric, libA, libB): p}}——只含双方都出值的库对。"""
    families = {}
    genres = sorted({g for lib in cells.values() for g in lib})
    for g in genres:
        pv = {}
        for k, _, _ in METRICS:
            for a, b in combinations(libs_in_cell(cells, g, k), 2):
                pv[(k, a, b)] = mann_whitney_u(cells[a][g][k], cells[b][g][k])
        if pv:
            families[g] = pv
    return families


def cell_fingerprint(cells):
    """机构指纹（新口径）：{(lib, genre, metric): {p, n_x, n_rest, med_x, med_rest}}
    x = 本库该格篇目；rest = 同体裁格内其余各库篇目合并（无该格的库不进入 rest）。"""
    out = {}
    for l in cells:
        for g in cells[l]:
            for k, _, _ in METRICS:
                x = cells[l][g].get(k, [])
                rest = [v for ll in cells if ll != l
                        for v in cells[ll].get(g, {}).get(k, [])]
                if len(x) >= MIN_CELL_N and len(rest) >= MIN_CELL_N:
                    out[(l, g, k)] = {
                        "p": mann_whitney_u(x, rest),
                        "n_x": len(x), "n_rest": len(rest),
                        "med_x": statistics.median(x), "med_rest": statistics.median(rest),
                    }
    return out


def institution_table():
    """机构层指纹值表：{metric: {lib: inst(L,m)}}（读 two_level.institution）。"""
    table = {}
    for lib in LIBS:
        d = AGG_DIR.get(lib, lib)
        agg = json.loads((ROOT / "output" / d / "_aggregate.json").read_text(encoding="utf-8"))
        inst = agg.get("two_level", {}).get("institution", {})
        for k, _, _ in METRICS:
            if k in inst:
                table.setdefault(k, {})[lib] = inst[k]
    return table


# ---------- 报告 ----------

def report(cells, flat, flat_cov):
    names = {k: v for k, _, v in METRICS}
    libs = list(LIBS)

    print("=" * 76)
    print("跨机构风格判别报告（两层模型口径 · 体裁对体裁）")
    print("FDR 族划分：① 格内两两族——按体裁分列，族 = 该格内 指标×库对 全部检验；")
    print("           ② 机构指纹族——库×共享体裁格×指标（pooled=同格其余各库合并），一族；")
    print("           各族内分别 BH-FDR 校正，q<0.05 为显著。旧全库口径见末节对照。")
    print("=" * 76)

    # 零、体裁构成表
    print("\n各库出值体裁格（n≥3）：")
    for l in libs:
        comp = " ".join(f"{g}(n={len(cells[l][g]['word_count'])})"
                        for g in sorted(cells[l]))
        print(f"  {l:18s} {comp or '（无出值格）'}")

    # 一、体裁格两两比较（族 = 体裁格）
    families = cell_pairwise(cells)
    fam_q = {g: bh_fdr(pv) for g, pv in families.items()}
    print("\n" + "=" * 76)
    print("一、体裁格两两比较（Mann-Whitney U；FDR 族 = 体裁格，格内 指标×库对）")
    print("=" * 76)
    for g in sorted(families):
        pv = families[g]
        q = fam_q[g]
        g_libs = sorted({l for (_, a, b) in pv for l in (a, b)})
        n_pairs = len(list(combinations(g_libs, 2)))
        print(f"\n── {g} {GENRE_NAMES[g]}（{len(g_libs)} 库：{'、'.join(g_libs)}；"
              f"族内 {len(pv)} 检验 = {n_pairs} 库对 × 指标）──")
        for k, _, label in METRICS:
            pairs = [(a, b) for (kk, a, b) in pv if kk == k]
            if not pairs:
                continue
            sig_p = [f"{a}×{b}" for (kk, a, b), p in pv.items() if kk == k and p < 0.05]
            sig_q = [f"{a}×{b}" for (kk, a, b) in pv if kk == k and q[(kk, a, b)] < 0.05]
            ref = " [内参]" if k in REFERENCE_ONLY else ""
            print(f"  {label:14s} p显著 {len(sig_p)}/{len(pairs)}  q显著 {len(sig_q)}/{len(pairs)}"
                  f"  {' '.join(sig_q[:6])}{ref}")

    # 二、格内判别力排序（F 比率，按体裁格分列）
    print("\n" + "=" * 76)
    print("二、格内判别力排序（秩化 F 比率；格与格之间 F 值不可直接比较）")
    print("=" * 76)
    for g in sorted(families):
        g_libs = sorted({l for (_, a, b) in families[g] for l in (a, b)})
        if len(g_libs) < 3:
            print(f"\n── {g} {GENRE_NAMES[g]}：仅 {len(g_libs)} 库，跳过排序 ──")
            continue
        print(f"\n── {g} {GENRE_NAMES[g]}（{len(g_libs)} 库）──")
        fr = []
        for k, _, label in METRICS:
            if k in REFERENCE_ONLY:
                continue
            cov = libs_in_cell(cells, g, k)
            if len(cov) >= 3:
                fr.append((f_ratio([cells[l][g][k] for l in cov]), k, label, len(cov)))
        for i, (f, k, label, cov_n) in enumerate(sorted(fr, reverse=True)[:8], 1):
            cov_note = "" if cov_n == len(g_libs) else f" ({cov_n}库)"
            print(f"  {i:2d}. {label:14s} F={f:.2f}{cov_note}")

    # 三、格内 LOO 最近质心归属（取库数最多的格）
    print("\n" + "=" * 76)
    print("三、格内 LOO 最近质心归属（z-score 标准化；取覆盖库最多的体裁格）")
    print("=" * 76)
    best_g = max(families, key=lambda g: len({l for (_, a, b) in families[g] for l in (a, b)}))
    g_libs = sorted({l for (_, a, b) in families[best_g] for l in (a, b)})
    use = [k for k, _, _ in METRICS
           if all(len(cells[l][best_g][k]) >= MIN_CELL_N for l in g_libs)]
    print(f"格 = {best_g} {GENRE_NAMES[best_g]}（{len(g_libs)} 库），全覆盖指标 {len(use)}/{len(METRICS)}")
    allv = {k: [v for l in g_libs for v in cells[l][best_g][k]] for k in use}
    zs = {l: {k: [(v - statistics.mean(allv[k])) / (statistics.pstdev(allv[k]) or 1)
                  for v in cells[l][best_g][k]] for k in use} for l in g_libs}
    correct = {l: 0 for l in g_libs}
    conf = {a: {b: 0 for b in g_libs} for a in g_libs}
    for true_l in g_libs:
        for i in range(len(zs[true_l][use[0]])):
            vec = [zs[true_l][k][i] for k in use]
            best, best_d = None, 1e18
            for cand in g_libs:
                c = [statistics.mean(zs[cand][k]) for k in use]
                d = math.sqrt(sum((vec[j] - c[j]) ** 2 for j in range(len(vec))))
                if d < best_d:
                    best, best_d = cand, d
            conf[true_l][best] += 1
            if best == true_l:
                correct[true_l] += 1
    n_tot = sum(len(cells[l][best_g][use[0]]) for l in g_libs)
    acc = sum(correct.values()) / max(n_tot, 1)
    print(f"总准确率：{acc:.0%}（{sum(correct.values())}/{n_tot}）")
    print(f"{'actual\\pred':12s}" + "".join(f"{l:>18s}" for l in g_libs))
    for a in g_libs:
        print(f"{a:12s}" + "".join(f"{conf[a][b]:>18d}" for b in g_libs))
    print("逐机构准确率：" + ", ".join(f"{l}={correct[l]}/{len(cells[l][best_g][use[0]])}"
                                    for l in g_libs))

    # 四、机构层指纹值表 + 新口径指纹检验
    print("\n" + "=" * 76)
    print("四、机构指纹（两层口径）")
    print("=" * 76)
    inst = institution_table()
    print("\n4a. 机构层指纹值表 inst(L,m)（体裁中位的中位；—=本库无出值格覆盖该指标）：")
    print(f"  {'指标':14s}" + "".join(f"{l[:12]:>14s}" for l in libs))
    for k, _, label in METRICS:
        row = f"  {label:14s}"
        for l in libs:
            v = inst.get(k, {}).get(l)
            row += f"{v:>14}" if v is not None else f"{'—':>14}"
        print(row)

    fp = cell_fingerprint(cells)
    fp_q = bh_fdr({k: v["p"] for k, v in fp.items()})
    print(f"\n4b. 指纹检验（族 = 库×共享格×指标，共 {len(fp)} 检验；pooled=同格其余各库合并）：")
    for l in libs:
        mine = [((ll, g, k), v) for (ll, g, k), v in fp.items() if ll == l]
        if not mine:
            print(f"  {l:18s} 无共享出值格，无指纹检验")
            continue
        (ll, g, k), v = min(mine, key=lambda kv: kv[1]["p"])
        q = fp_q[(ll, g, k)]
        direction = "高" if v["med_x"] > v["med_rest"] else "低"
        verdict = "过 FDR" if q < 0.05 else "探索性信号，未过 FDR，待样本扩容复验"
        if k in REFERENCE_ONLY:
            verdict += "；内参指标（长度敏感），仅供参照"
        print(f"  {l:18s} 最显著: {names[k]} @ {g}格（{direction}，"
              f"median {round(v['med_x'], 2)} vs 同格 pooled {round(v['med_rest'], 2)}，"
              f"p={v['p']:.3f}，q={q:.3f}）{verdict}")

    # 五、旧口径对照
    print("\n" + "=" * 76)
    print("五、旧口径对照（全库聚合，构成污染口径，仅对照——不作结论依据）")
    print("=" * 76)
    pvals = {}
    for k, g, label in METRICS:
        for a, b in combinations(flat_cov[k], 2):
            pvals[(k, a, b)] = mann_whitney_u(flat[a][k], flat[b][k])
    qvals = bh_fdr(pvals)
    print("\n5a. 两两显著计数（一族 BH，混入体裁构成差异）：")
    for k, g, label in METRICS:
        pairs = [(a, b) for (kk, a, b) in pvals if kk == k]
        sig_p = sum(1 for (kk, a, b), p in pvals.items() if kk == k and p < 0.05)
        sig_q = sum(1 for (kk, a, b) in pvals if kk == k and qvals[(kk, a, b)] < 0.05)
        print(f"  {label:14s} p显著 {sig_p}/{len(pairs)}  q显著 {sig_q}/{len(pairs)}")
    print("\n5b. 旧口径机构指纹（vs 其余六库 pooled，全库聚合）：")
    fp_p, fp_info = {}, {}
    for l in libs:
        best_k, best_p = None, 1.0
        for k, g, label in METRICS:
            x = flat[l][k]
            rest = [v for ll in libs if ll != l for v in flat[ll][k]]
            if len(x) >= 4 and len(rest) >= 4:
                p = mann_whitney_u(x, rest)
                if p < best_p:
                    best_p, best_k = p, k
        fp_p[l], fp_info[l] = best_p, best_k
    fp_q_old = bh_fdr(fp_p)
    for l in libs:
        k = fp_info[l]
        x = flat[l][k]
        rest = [v for ll in libs if ll != l for v in flat[ll][k]]
        direction = "高" if statistics.median(x) > statistics.median(rest) else "低"
        print(f"  {l:18s} 最显著: {names[k]}（{direction}，p={fp_p[l]:.3f}，"
              f"q={fp_q_old[l]:.3f}）{'过 FDR' if fp_q_old[l] < 0.05 else '未过 FDR'}")


def main():
    cells = load_cells()
    flat, flat_cov = load_flat()
    report(cells, flat, flat_cov)


if __name__ == "__main__":
    main()
