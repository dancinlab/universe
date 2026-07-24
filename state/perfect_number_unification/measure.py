#!/usr/bin/env python3
"""H_003 — quantify the look-elsewhere power of the H-PH-9 formula family.

H-PH-9 predicts fermion masses and constants with unconstrained arithmetic expressions over the
small alphabet {phi=2, tau=4, P1=6, sigma=12, R=48}, then quotes the per-particle relative error
as evidence. This enumerates every value the family can build up to the complexity the document
itself uses and counts, for each target, how many distinct reachable values fall inside a 3% band.
If a target has dozens of rivals, one expression hitting it carries no information.

Exact rational arithmetic (fractions), bounded leaf count, operations + - * /. Exponentiation is
excluded so the count is a conservative LOWER bound on the family's true reach. Fully
deterministic — no sampling — so the output reproduces byte-identically.
"""
import bisect
import sys
from fractions import Fraction

ATOMS = {"phi": 2, "tau": 4, "P1": 6, "sigma": 12, "R": 48}
MAX_LEAVES = 5          # the document's own formulas reach ~5-7 leaves; 5 is conservative
BOUND = Fraction(10 ** 7)
DEN_CAP = 10 ** 6       # drop values with absurd denominators (keeps the set finite/meaningful)

# (name, measured value, the document's formula, its value, its quoted error %)
TARGETS = [
    ("m_electron", 0.511, "phi/tau", 0.5, 2.2),
    ("m_up", 2.16, "phi", 2.0, 7.4),
    ("m_down", 4.67, "tau*(1+phi/sigma)", 14 / 3, 0.07),
    ("m_strange", 93.4, "sigma*(sigma-tau)", 96.0, 2.8),
    ("m_muon", 105.66, "sigma(28)*phi-tau(28)", 106.0, 0.3),
    ("m_charm", 1270.0, "sigma^2*(sigma-tau+R)", 1296.0, 2.0),
    ("m_tau", 1776.86, "sigma^3+R", 1776.0, 0.048),
    ("m_bottom", 4180.0, "phi^sigma", 4096.0, 2.0),
    ("m_top", 172500.0, "sigma^3*(sigma^2-sigma*tau+tau)", 172800.0, 0.17),
    ("1/alpha", 137.036, "sigma^2-P1-R(6)", 137.0, 0.026),
]


def combine(a, b):
    out = [a + b, a - b, a * b]
    if b != 0:
        out.append(a / b)
    if a != 0:
        out.append(b / a)
    return out


def enumerate_values(max_leaves):
    """by_size[k] = set of Fractions reachable with exactly k atom leaves."""
    by_size = {1: set(Fraction(v) for v in ATOMS.values())}
    for size in range(2, max_leaves + 1):
        acc = set()
        for left in range(1, size):
            right = size - left
            for a in by_size[left]:
                for b in by_size[right]:
                    for v in combine(a, b):
                        if abs(v) <= BOUND and v.denominator <= DEN_CAP:
                            acc.add(v)
        by_size[size] = acc
    return by_size


def main():
    print(f"alphabet: {ATOMS}")
    print("operations: + - * /   (exponentiation EXCLUDED -> conservative lower bound)")
    print(f"complexity cap: {MAX_LEAVES} atom leaves")
    print()

    by_size = enumerate_values(MAX_LEAVES)
    reachable = set()
    for size in sorted(by_size):
        reachable |= by_size[size]
        print(f"  distinct values with <= {size} leaves: {len(reachable):,}")
    positives = sorted(float(v) for v in reachable if v > 0)
    print(f"  distinct POSITIVE values (the mass/constant candidates): {len(positives):,}")
    print()

    print(f"{'target':12} {'measured':>11} {'doc value':>11} {'doc err%':>9} "
          f"{'rivals in 3% band':>18} {'nearest err%':>13}")
    print("-" * 78)
    for name, measured, formula, docval, docerr in TARGETS:
        lo = bisect.bisect_left(positives, measured * 0.97)
        hi = bisect.bisect_right(positives, measured * 1.03)
        rivals = hi - lo
        j = bisect.bisect_left(positives, measured)
        cands = positives[max(0, j - 1): j + 1]
        nearest = min(cands, key=lambda v: abs(v - measured))
        nearest_err = abs(nearest - measured) / measured * 100.0
        print(f"{name:12} {measured:11.3f} {docval:11.3f} {docerr:9.3f} "
              f"{rivals:18,} {nearest_err:13.5f}")
    print()

    # density on a decade-spanning deterministic probe grid, via bisect
    print("density — deterministic probe grid, fraction covered within x% by SOME reachable value:")
    for pct in (0.05, 0.5, 3.0):
        hits = probes = 0
        for exp in range(0, 6):
            for m in range(10, 100):
                probe = (m / 10.0) * (10 ** exp)
                probes += 1
                lo = bisect.bisect_left(positives, probe * (1 - pct / 100))
                hi = bisect.bisect_right(positives, probe * (1 + pct / 100))
                if hi > lo:
                    hits += 1
        print(f"  within {pct:>4}% : {hits}/{probes} = {hits / probes * 100:5.1f}%")
    print()
    print("interpretation: a quoted per-particle error is evidence only if this family could not")
    print("easily have hit the target. Where the 3% band already holds many rivals, the individual")
    print("error figure carries no information about the hypothesis.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
