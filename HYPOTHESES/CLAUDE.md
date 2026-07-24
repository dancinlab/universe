# HYPOTHESES/ — hypothesis + verdict registry (folder guide)

The hypothesis registry of this repo, adopted verbatim in shape from `dancinlab/anima`.
Every research claim is registered, falsified or verified, and cemented here — walls and
negative results included. Card bodies are written in Korean (repo doc language); this guide
stays English because it re-injects every turn.

## Surface invariant (3 surfaces, nothing else)

Git-tracked files under `HYPOTHESES/` are **only** `cards/**`, `HYPOTHESES.jsonl`, and this
`CLAUDE.md`. No `.py`, no run output, no per-domain logs, no theme buckets, no prose overview.
Code and results live in `state/<slug>/`; long-form prose lives in `state/`.

Self-check (must print nothing):

```sh
git ls-files 'HYPOTHESES/*' | grep -vE '^HYPOTHESES/(cards/|HYPOTHESES\.jsonl$|CLAUDE\.md$)'
```

Enforced by `python3 tool/check_hypotheses_surface.py` (exit 1 on any stray file).

## The two data surfaces

- `cards/H_<id>_<slug>.md` — the card, and the SSOT for one hypothesis. YAML frontmatter plus
  fixed sections; the verdict, the numbers, and the `wired:` state axis live here.
- `HYPOTHESES.jsonl` — one line per card, id-ordered, derived from the cards. Never hand-edit;
  regenerate with `python3 tool/build_hypotheses_index.py`.

Start a new card from `cards/_TEMPLATE.md` (the underscore keeps it out of the index).

## Registration flow

```
research -> pre-register (freeze the bar) -> run -> capture verbatim output
         -> state/verdicts/<slug>/<id>.txt -> cards/H_<id>_<slug>.md -> rebuild index
```

Every tier gets a card — verified, wall, falsified, proposed. Walls are results too.
Recurring lessons go to `ARCHITECTURE.json` `convergence.records[]`, not into a card body.

## Tiers

| tier | meaning |
| --- | --- |
| PROPOSED | registered, bar frozen, not yet run |
| RUNNING | measurement in flight |
| VERIFIED | bar met on captured output, and wired |
| WALL | measured and blocked — a real negative, reopenable |
| FALSIFIED | a pre-registered falsifier fired |
| INSTRUMENT-DEAD | the measurement path itself was invalid; no scientific claim |
| BLOCKED-INFRA | infrastructure failure — **not** a verdict; the bar does not move |

## Discipline — the 5-second check before cementing a verdict

1. **Frozen-first, no tune-to-green.** The bar is registered before measuring and never moves
   afterwards. Falsified, negative, and disputed results are published, never buried.
2. **Suspect the measurement path first.** When two paths disagree, suspect the harness, the
   environment, or an unfinished run before believing a real effect.
3. **An infra wall is not a scientific ceiling.** OOM, reboot, refused SSH → BLOCKED-INFRA.
4. **A single run can be an illusion.** Re-run under independent seeds or independent sources
   and take the majority before calling anything genuine.
5. **No self-judging.** Captured output is the evidence; a model's impression is not.
6. **VERIFIED means wired.** Verified but not wired into the live system is not green — record
   `wired:` and the follow-on id.
7. **Cite the exact artifact.** Which commit, which checkpoint, which version of the paper — an
   unattributed number is a rumour.
