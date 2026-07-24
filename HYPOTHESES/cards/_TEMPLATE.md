---
ssot: ARCHITECTURE.json
id: H_000
slug: template
title: 반증 가능한 한 줄 주장
domain: <도메인>
tier: 🔵 PROPOSED
status: proposed
wired: none
pre_register_frozen: true
frozen_at: YYYY-MM-DD
since: YYYY-MM-DD
related: []
---

# H_000 — <제목>

> 📍 설계 SSOT → [ARCHITECTURE.json](../../ARCHITECTURE.json) · 등록 규칙 → [HYPOTHESES/CLAUDE.md](../CLAUDE.md)

## 가설

틀릴 수 있는 형태로 진술한 주장. "좋아진다" 가 아니라 "무엇이 어떤 기준선을 넘는다".

## 근거

이 가설을 세우게 만든 관찰이나 선행 결과.

## 예측

- **P1**: ...
- **P2**: ...

## 변수

- **axis1_...**: [...]

## 실행 규약

어떻게 측정하는가 — 명령 · 시드 · 출처 · 비용. 가능하면 결정론적으로.

## 판정 기준

- **C1**: ...
- **verdict_rule**: VERIFIED = ...; PARTIAL = ...; FALSIFIED = ...

## 반증 조건

- **F1**: ... 이면 가설 FALSIFIED

## 정직한 한계

- **L1**: ...

## 교차 링크

- **evidence_paths**: `state/verdicts/<slug>/<id>.txt`
- **related**: H_...

## 판정

```
verdict_class: <PROPOSED | VERIFIED | PARTIAL | WALL | FALSIFIED | INSTRUMENT-DEAD>
evidence_summary:
  - ...
falsifiers_triggered: none
criteria_met:
  - C1: ...
next:
  - ...
artifact_paths:
  - ...
```
