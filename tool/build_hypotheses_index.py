#!/usr/bin/env python3
"""Rebuild HYPOTHESES/HYPOTHESES.jsonl from the cards on disk.

The cards under HYPOTHESES/cards/H_*.md are the SSOT; this index is derived and must never be
hand-edited. One JSON object per card, ordered by numeric id then filename. Idempotent.

Emitted keys: id, slug, title, domain, tier, status, wired, frozen_at, since, related, card.
Values come from the card's YAML frontmatter; `title` falls back to the first H1 heading.
Files starting with an underscore (e.g. _TEMPLATE.md) are ignored.
"""
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_DIR = os.path.join(REPO, "HYPOTHESES", "cards")
OUT = os.path.join(REPO, "HYPOTHESES", "HYPOTHESES.jsonl")

KEYS = ["id", "slug", "title", "domain", "tier", "status", "wired", "frozen_at", "since", "related"]


def parse_frontmatter(text):
    """Return the leading YAML frontmatter as a flat dict (scalars + inline lists only)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not km:
            continue
        key, raw = km.group(1), km.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            fm[key] = [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
        else:
            fm[key] = raw.strip("'\"")
    return fm


def first_heading(text):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def id_sort_key(path):
    name = os.path.basename(path)
    m = re.match(r"^H_(\d+)", name)
    return (int(m.group(1)) if m else 1 << 30, name)


def main():
    cards = sorted(glob.glob(os.path.join(CARDS_DIR, "H_*.md")), key=id_sort_key)
    rows = []
    for path in cards:
        text = open(path, encoding="utf-8").read()
        fm = parse_frontmatter(text)
        rel = os.path.relpath(path, REPO)
        if not fm.get("id"):
            print(f"error: {rel} has no `id:` in its frontmatter", file=sys.stderr)
            return 1
        row = {k: fm.get(k, "") for k in KEYS}
        if not row["title"]:
            row["title"] = first_heading(text)
        if not isinstance(row["related"], list):
            row["related"] = [row["related"]] if row["related"] else []
        row["card"] = rel
        rows.append(row)

    with open(OUT, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"HYPOTHESES.jsonl: {len(rows)} card(s) indexed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
