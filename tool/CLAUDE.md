# tool/ — repo maintenance scripts (folder guide)

Small, dependency-free Python scripts that keep the repo's invariants true. Run from anywhere;
each resolves the repo root from its own path. Standard library only — no install step.

| script | job |
| --- | --- |
| `build_hypotheses_index.py` | Rebuild `HYPOTHESES/HYPOTHESES.jsonl` from the cards. Idempotent. |
| `check_hypotheses_surface.py` | Gate the `HYPOTHESES/` three-surface invariant and index freshness. Exit 1 on violation. |

Conventions: English identifiers and docstrings (repo `code-language` rule); no third-party
imports; every script is safe to re-run and prints a one-line result.
