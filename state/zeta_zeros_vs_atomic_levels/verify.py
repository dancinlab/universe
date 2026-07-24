#!/usr/bin/env python3
"""H_001 — mechanically re-verify the verdict against the primary source.

The first pass judged the claim from two independent language-model readings. The registry
forbids treating a model's opinion as evidence, so this script re-derives every criterion from
the paper's own full text and from arithmetic, with no judgement step.

Inputs (mirrored under data/):
  arxiv-2606.09096v1-fulltext.txt — plain text of the arXiv HTML rendering of the paper
  ../arxiv-2606.09096-abstract.txt — bibliographic record incl. subject classification

Criteria (frozen in the card before any of this ran):
  C1 the paper contains atoms / hydrogen / energy levels
  C2 the paper carries a physics subject classification
  C3 the paper's headline result is a proved theorem, not a conjecture
  C4 "hydrogen level spacings match zeta zero spacings" holds arithmetically as stated
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FULLTEXT = os.path.join(HERE, "data", "arxiv-2606.09096v1-fulltext.txt")
BIBLIO = os.path.join(HERE, "arxiv-2606.09096-abstract.txt")

# Physical vocabulary that must appear if the paper were about atomic energy levels.
PHYSICS_TERMS = [
    "atom", "atomic", "hydrogen", "energy level", "electron", "electronvolt", "eV",
    "quantum jump", "Schrodinger", "Schrödinger", "Hamiltonian", "spectrum of an atom",
]
# Mathematical vocabulary the paper is actually built from.
MATH_TERMS = [
    "screw function", "Weil quadratic form", "self-adjoint", "nontrivial zeros",
    "Riemann zeta", "nonlocal", "conjecture", "theorem",
]


def word_count(text, term):
    """Case-insensitive count. 'eV' is matched case-sensitively as a standalone token."""
    if term == "eV":
        return len(re.findall(r"\beV\b", text))
    return len(re.findall(re.escape(term), text, re.IGNORECASE))


def main():
    text = open(FULLTEXT, encoding="utf-8").read()
    biblio = open(BIBLIO, encoding="utf-8").read()
    print(f"source: {os.path.relpath(FULLTEXT, HERE)}  ({len(text)} chars)")
    print(f"source: {os.path.relpath(BIBLIO, HERE)}")
    print()

    # --- C1 -- does the paper talk about atoms at all? -------------------------------
    print("C1 — physical vocabulary in the full text")
    physics_hits = {t: word_count(text, t) for t in PHYSICS_TERMS}
    for term, n in physics_hits.items():
        print(f"   {term:22} {n}")
    print()
    print("     mathematical vocabulary, for contrast")
    math_hits = {t: word_count(text, t) for t in MATH_TERMS}
    for term, n in math_hits.items():
        print(f"   {term:22} {n}")
    total_physics = sum(physics_hits.values())
    c1 = total_physics > 0
    print(f"   -> physical terms total = {total_physics}; C1 (paper is about atoms) = {'PASS' if c1 else 'FAIL'}")
    print()

    # --- C2 -- subject classification ------------------------------------------------
    print("C2 — subject classification")
    subj = re.search(r"Subjects:\s*(.+)", biblio)
    subj_line = subj.group(1).strip() if subj else "(not found)"
    print(f"   {subj_line}")
    physics_classes = re.findall(r"\b(physics|quant-ph|hep-th|math-ph|cond-mat|astro-ph)\b", subj_line, re.IGNORECASE)
    c2 = bool(physics_classes)
    print(f"   -> physics classes found: {physics_classes or 'none'}; C2 = {'PASS' if c2 else 'FAIL'}")
    print()

    # --- C3 -- theorem or conjecture? -------------------------------------------------
    print("C3 — is the headline result proved?")
    formulate = re.findall(r"[^.]*\bformulate a conjecture\b[^.]*\.", text, re.IGNORECASE)
    for s in formulate[:3]:
        print(f"   quote: {' '.join(s.split())[:220]}")
    n_conj = word_count(text, "conjecture")
    print(f"   occurrences: 'conjecture' = {n_conj}, 'theorem' = {word_count(text, 'theorem')}")
    c3 = not formulate
    print(f"   -> headline stated as a conjecture: {bool(formulate)}; C3 (proved theorem) = {'PASS' if c3 else 'FAIL'}")
    print()

    # --- C4 -- the hydrogen arithmetic ------------------------------------------------
    print("C4 — the numbers the video presented as 'spacings'")
    quoted = [-0.28, -0.38, -0.54, -0.85]
    print("   Bohr levels E_n = -13.6 / n^2 :")
    levels = {}
    for n in range(4, 8):
        e = -13.6 / (n * n)
        levels[n] = e
        match = min(quoted, key=lambda q: abs(q - e))
        near = abs(match - e) < 0.02
        print(f"     n={n}  E_n = {e:8.4f} eV   quoted {match:6.2f} -> {'MATCHES a quoted value' if near else 'no match'}")
    print("   actual adjacent spacings between those levels:")
    for n in range(4, 7):
        gap = levels[n + 1] - levels[n]
        print(f"     E_{n+1} - E_{n} = {gap:7.4f} eV")
    quoted_are_levels = all(
        any(abs(q - levels[n]) < 0.02 for n in levels) for q in quoted
    )
    print(f"   -> every quoted number is a LEVEL, not a spacing: {quoted_are_levels}")
    c4 = not quoted_are_levels
    print(f"   C4 (the stated hydrogen-spacing correspondence holds) = {'PASS' if c4 else 'FAIL'}")
    print()

    # --- verdict ----------------------------------------------------------------------
    passed = sum([c1, c2, c3, c4])
    print(f"criteria passed: {passed}/4  (C1={c1} C2={c2} C3={c3} C4={c4})")
    print("falsifiers:")
    print(f"  F1 subject classification is pure mathematics only : {'FIRED' if not c2 else 'not fired'}")
    print(f"  F2 headline result is stated as a conjecture       : {'FIRED' if not c3 else 'not fired'}")
    print(f"  F3 no physical objects in the paper                : {'FIRED' if not c1 else 'not fired'}")
    print(f"  F4 hydrogen-spacing correspondence absent          : {'FIRED' if not c4 else 'not fired'}")
    print()
    verdict = "VERIFIED" if passed == 4 else ("PARTIAL" if passed >= 2 else "FALSIFIED")
    print(f"verdict_class: {verdict}  (rule: VERIFIED=4/4, PARTIAL=2-3, FALSIFIED<=1)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
