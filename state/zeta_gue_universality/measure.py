#!/usr/bin/env python3
"""H_002 — measure nearest-neighbour spacing statistics of Riemann zeta zeros.

Protocol frozen in HYPOTHESES/cards/H_002_zeta_gue_universality.md before this ran.

Sources (Odlyzko's tables, mirrored under data/):
  odlyzko_zeros1.txt — imaginary parts of the first 100,000 nontrivial zeros
  odlyzko_zeros3.txt — zeros numbered 10^12+1 .. 10^12+10^4, stored as gamma - OFFSET3

Unfolding uses the Riemann-von Mangoldt counting function
    N(t) = (t / 2pi) * (log(t / 2pi) - 1) + 7/8
so that the unfolded spacings s_n = N(g_{n+1}) - N(g_n) have mean ~1 by construction.

Reference nearest-neighbour distributions (Wigner surmises):
    Poisson  p(s) = exp(-s)
    GOE      p(s) = (pi/2)  s   exp(-pi s^2 / 4)
    GUE      p(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)

Deterministic: no randomness anywhere. Re-running reproduces the numbers exactly.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OFFSET3 = 267653395647.0  # zeros3 stores gamma - OFFSET3 (see that file's header)

TWO_PI = 2.0 * math.pi


def load_zeros1():
    path = os.path.join(DATA, "odlyzko_zeros1.txt")
    return [float(line) for line in open(path, encoding="utf-8") if line.strip()]


def load_zeros3():
    """zeros3 has a prose header; every numeric line is an offset from OFFSET3."""
    path = os.path.join(DATA, "odlyzko_zeros3.txt")
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            out.append(OFFSET3 + float(line))
        except ValueError:
            continue  # header prose
    return out


def counting_function(t):
    """Smooth part of the Riemann-von Mangoldt formula: the mean number of zeros below t."""
    return (t / TWO_PI) * (math.log(t / TWO_PI) - 1.0) + 0.875


def unfolded_spacings(gammas):
    n = [counting_function(g) for g in gammas]
    return [n[i + 1] - n[i] for i in range(len(n) - 1)]


def cdf_poisson(s):
    return 1.0 - math.exp(-s)


def cdf_goe(s):
    return 1.0 - math.exp(-math.pi * s * s / 4.0)


def cdf_gue(s):
    a = 4.0 / math.pi
    term_erf = math.sqrt(math.pi) / (4.0 * a ** 1.5) * math.erf(s * math.sqrt(a))
    term_exp = s / (2.0 * a) * math.exp(-a * s * s)
    return (32.0 / math.pi ** 2) * (term_erf - term_exp)


def ks_statistic(sample_sorted, cdf):
    """Two-sided Kolmogorov-Smirnov distance between the sample and a reference CDF."""
    n = len(sample_sorted)
    d = 0.0
    for i, x in enumerate(sample_sorted):
        f = cdf(x)
        d = max(d, (i + 1) / n - f, f - i / n)
    return d


def analyse(label, gammas):
    spacings = unfolded_spacings(gammas)
    spacings.sort()
    n = len(spacings)
    mean = sum(spacings) / n
    ks = {
        "GUE": ks_statistic(spacings, cdf_gue),
        "GOE": ks_statistic(spacings, cdf_goe),
        "Poisson": ks_statistic(spacings, cdf_poisson),
    }
    # C2 — level repulsion: observed mass below s = 0.2 against the Poisson expectation.
    small = sum(1 for s in spacings if s <= 0.2) / n
    poisson_small = cdf_poisson(0.2)
    return {
        "label": label,
        "n_zeros": len(gammas),
        "n_spacings": n,
        "height_lo": gammas[0],
        "height_hi": gammas[-1],
        "mean_spacing": mean,
        "ks": ks,
        "mass_le_0.2": small,
        "poisson_mass_le_0.2": poisson_small,
    }


def main():
    z1 = load_zeros1()
    z3 = load_zeros3()
    print(f"loaded: zeros1 n={len(z1)} (gamma {z1[0]:.6f} .. {z1[-1]:.6f})")
    print(f"loaded: zeros3 n={len(z3)} (gamma {z3[0]:.6f} .. {z3[-1]:.6f})")
    print()

    windows = [
        ("W1  first 10^4 zeros", z1[:10000]),
        ("W2  zeros 9*10^4..10^5", z1[90000:100000]),
        ("W3  zeros 10^12+1..10^12+10^4", z3),
    ]

    results = [analyse(label, g) for label, g in windows]

    hdr = f"{'window':32} {'n_s':>6} {'mean s':>8} {'KS_GUE':>8} {'KS_GOE':>8} {'KS_Pois':>8} {'P(s<=.2)':>9}"
    print(hdr)
    print("-" * len(hdr))
    for r in results:
        print(
            f"{r['label']:32} {r['n_spacings']:6d} {r['mean_spacing']:8.5f} "
            f"{r['ks']['GUE']:8.5f} {r['ks']['GOE']:8.5f} {r['ks']['Poisson']:8.5f} "
            f"{r['mass_le_0.2']:9.5f}"
        )
    print()
    print(f"Poisson reference mass below s=0.2: {results[0]['poisson_mass_le_0.2']:.5f}")
    print()

    # Diagnostic only (NOT part of the frozen bar): the 5% KS critical value 1.36/sqrt(n)
    # says whether the sample is formally consistent with the reference law in absolute
    # terms. The Wigner surmise is an approximation to the exact GUE (Gaudin) spacing law,
    # so a low-height window can beat Poisson decisively yet still exceed this threshold.
    print("diagnostic (not a criterion) — absolute goodness of fit vs the GUE Wigner surmise:")
    for r in results:
        crit = 1.36 / math.sqrt(r["n_spacings"])
        verdict = "within" if r["ks"]["GUE"] <= crit else "exceeds"
        print(
            f"  {r['label']:32} KS_GUE={r['ks']['GUE']:.5f}  5% crit={crit:.5f}  -> {verdict}"
        )
    print()

    # --- pre-registered criteria -------------------------------------------------
    c1 = all(r["ks"]["GUE"] < r["ks"]["Poisson"] * 0.5 for r in results)
    c2 = all(r["mass_le_0.2"] <= r["poisson_mass_le_0.2"] * 0.5 for r in results)
    gue = [r["ks"]["GUE"] for r in results]
    c3 = all(gue[i + 1] < gue[i] for i in range(len(gue) - 1))
    # F3 — does GOE beat GUE consistently? (symmetry-class misassignment)
    f3 = all(r["ks"]["GOE"] < r["ks"]["GUE"] for r in results)

    print("criteria (frozen before measurement):")
    print(f"  C1  KS_GUE < 0.5 * KS_Poisson in every window          : {'PASS' if c1 else 'FAIL'}")
    for r in results:
        print(
            f"        {r['label']:32} {r['ks']['GUE']:.5f} vs {0.5 * r['ks']['Poisson']:.5f}"
        )
    print(f"  C2  mass(s<=0.2) <= 0.5 * Poisson in every window      : {'PASS' if c2 else 'FAIL'}")
    for r in results:
        print(
            f"        {r['label']:32} {r['mass_le_0.2']:.5f} vs {0.5 * r['poisson_mass_le_0.2']:.5f}"
        )
    print(f"  C3  KS_GUE decreases monotonically with height         : {'PASS' if c3 else 'FAIL'}")
    print(f"        {' -> '.join(f'{g:.5f}' for g in gue)}")
    print()
    print("falsifiers:")
    print(f"  F1  KS_Poisson <= KS_GUE anywhere : {'FIRED' if any(r['ks']['Poisson'] <= r['ks']['GUE'] for r in results) else 'not fired'}")
    print(f"  F2  no suppression at small s     : {'FIRED' if not c2 else 'not fired'}")
    print(f"  F3  GOE beats GUE in every window : {'FIRED' if f3 else 'not fired'}")
    print()

    if c1 and c2 and c3:
        verdict = "VERIFIED"
    elif c1 and c2:
        verdict = "PARTIAL"
    else:
        verdict = "FALSIFIED"
    print(f"verdict_class: {verdict}  (rule: VERIFIED=C1+C2+C3, PARTIAL=C1+C2, FALSIFIED=C1 fails)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
