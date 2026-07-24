#!/usr/bin/env python3
"""Enforce the HYPOTHESES/ three-surface invariant.

Only cards/**, HYPOTHESES.jsonl, and CLAUDE.md may be git-tracked under HYPOTHESES/.
Also verifies that the derived index is in sync with the cards on disk.
Exit 1 on any violation so this can gate a commit or CI run.
"""
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED = re.compile(r"^HYPOTHESES/(cards/|HYPOTHESES\.jsonl$|CLAUDE\.md$)")


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files", "HYPOTHESES/"],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout
    return [line for line in out.splitlines() if line.strip()]


def main():
    failures = []

    strays = [f for f in tracked_files() if not ALLOWED.match(f)]
    for stray in strays:
        failures.append(f"stray tracked file under HYPOTHESES/: {stray}")

    index = os.path.join(REPO, "HYPOTHESES", "HYPOTHESES.jsonl")
    before = open(index, encoding="utf-8").read() if os.path.isfile(index) else None
    subprocess.run(
        [sys.executable, os.path.join(REPO, "tool", "build_hypotheses_index.py")],
        cwd=REPO, capture_output=True, text=True, check=True,
    )
    after = open(index, encoding="utf-8").read() if os.path.isfile(index) else None
    if before != after:
        failures.append("HYPOTHESES.jsonl was stale — rebuilt from the cards; commit the result")

    if failures:
        for f in failures:
            print(f"FAIL: {f}", file=sys.stderr)
        return 1
    print("hypotheses surface: OK (cards/ + HYPOTHESES.jsonl + CLAUDE.md only, index in sync)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
