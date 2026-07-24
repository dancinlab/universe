# universe

Hypothesis registry for claims tying number theory to quantum mechanics and cosmology. Claims are
not accumulated by citation — each one freezes its bar first, then gets measured and cemented as a
card. The registry shape is adopted from `dancinlab/anima`.

> 📍 SSOT pointers (this file = entry point + work rules only):
> · **structure/design → [ARCHITECTURE.json](ARCHITECTURE.json)** — the deep tree lives there
> · registry rules → [HYPOTHESES/CLAUDE.md](HYPOTHESES/CLAUDE.md) (surface invariant · tiers)
> · history → [CHANGELOG.jsonl](CHANGELOG.jsonl) (append)

## Project

A registry, not a library. Every research claim about zeta zeros, spectral interpretations, and
random-matrix universality is registered as a card under `HYPOTHESES/`, with its falsifiers and
pass bar frozen before any measurement runs. Verdicts cite captured output stored in `state/`,
so a reader can re-derive the call instead of trusting a summary. Negative results, walls, and
retractions stay in the registry — they are the point, not an embarrassment.

## Tree

Top-level orientation map (deep SSOT = [ARCHITECTURE.json](ARCHITECTURE.json)):

```
universe/
├─ HYPOTHESES/   — hypothesis + verdict registry (3-surface invariant)
│  ├─ cards/     — H_<id>_<slug>.md, the SSOT body of one hypothesis
│  ├─ HYPOTHESES.jsonl — derived id-ordered index (never hand-edited)
│  └─ CLAUDE.md  — folder rules, tiers, pre-verdict checklist
├─ tool/         — index rebuild + surface invariant gate (stdlib only)
├─ state/        — every work output: raw sources and captured verdict evidence
└─ ARCHITECTURE.json — design SSOT (current-state snapshot)
```

## doc-language

- do: Author and maintain ALL docs in KOREAN — `README.md` · hypothesis cards · `ARCHITECTURE.json` human fields · `CHANGELOG.jsonl` `title`/`body` · `docs/` prose
- dont: New English prose docs · leaving a ported-in English doc untranslated

## inject-doc-language

- do: Keep `CLAUDE.md` + `.harness/commons.md` ENGLISH and compact — they re-inject every turn
- dont: Korean prose in a re-injected governance doc (guard `INJECT-NON-ENGLISH`)

## jargon-gloss

- do: Gloss jargon on first use in Korean prose as `term(=plain meaning)`
- dont: Bare acronyms or project slang in user-facing prose

## code-language

- do: Identifiers · code comments · docstrings · commit subjects in ENGLISH
- dont: Korean identifiers or Korean commit subjects

## single-doc

- do: Design = one `ARCHITECTURE.json` current-state snapshot, updated in place; history appended to `CHANGELOG.jsonl`; `README.md` = current state
- dont: Scattered `*-report`/`*-summary`/`*-notes` · versions/dates/change narration in the tree or README

## hypothesis-registry

- do: Register every research claim under `HYPOTHESES/` per `HYPOTHESES/CLAUDE.md`, keeping the 3-surface invariant
- dont: Code or results git-tracked inside `HYPOTHESES/` (they belong in `state/<slug>/`)

## frozen-bar

- do: Freeze the bar before measuring, and publish negative results
- dont: Moving the bar after measuring · burying a falsified or disputed result

## verify-done

- do: Prove "done" by running the command and citing the captured output as evidence
- dont: Model self-judging · hiding a failure · unverified "done"
