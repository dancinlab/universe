---
ssot: ARCHITECTURE.json
id: H_001
slug: zeta_zeros_vs_atomic_levels
title: 스즈키 2026 논문이 제타 영점과 원자 에너지 준위의 직접 관련을 발견했다
domain: 수론-양자역학 대응
tier: 🔴 FALSIFIED
status: closed
wired: none
pre_register_frozen: true
frozen_at: 2026-07-25
since: 2026-07-25
related: [H_002]
---

# H_001 — 제타 영점 = 원자 에너지 준위 주장의 검증

> 📍 설계 SSOT → [ARCHITECTURE.json](../../ARCHITECTURE.json) · 등록 규칙 → [HYPOTHESES/CLAUDE.md](../CLAUDE.md)

## 가설

대중과학 영상 "신이 원자를 설계할 때 사용한 함수가 리만가설의 제타함수인 이유"
(지식보관소 · 2026-07-11 · `JdtWRVaNi9c`) 가 전한 주장, 즉 **마사토시 스즈키가 2026년 6월
논문에서 리만 제타함수의 비자명 영점이 원자의 에너지 준위와 직접 관련됨을 발견했다**는 서술은
해당 논문(`arXiv:2606.09096`) 의 실제 내용과 일치한다.

## 근거

영상은 arXiv 게재일(2026-06-08) · 저자 · 리만가설이라는 소재를 정확히 특정한다. 따라서 논문
자체를 오독한 것인지, 아니면 정말 그런 결과가 있는지는 원문 대조로만 갈린다.

## 예측

- **P1**: 논문 초록·본문에 원자(atom) · 수소(hydrogen) · 에너지 준위(energy level) 에 해당하는
  물리적 대상이 등장한다.
- **P2**: 논문의 분류(subject) 에 물리 분야가 포함된다.
- **P3**: 논문이 제시한 것은 추측(conjecture) 이 아니라 증명된 정리(theorem) 다.
- **P4**: "수소 원자 전자의 에너지 준위 간격이 제타 영점 간격과 일치한다" 는 선행 연구 결과가
  실제로 존재한다.

## 변수

- **axis1_source**: [영상 자막 전문, arXiv 초록 원문, arXiv 본문 HTML]
- **axis2_checker**: [Claude Fable 5, OpenAI Codex 5.6] — 독립 2경로 대조

## 실행 규약

1. 영상 자동자막을 받아 시간축 포함 전문으로 정규화 (`yt-dlp` → VTT → 중복 제거).
2. `arXiv:2606.09096` 의 서지·분류·초록을 원문 그대로 확보.
3. 영상의 주장 사슬을 6개 항목으로 분해해, 두 프런티어 모델에 **동일한 지시문**으로 독립 판정
   위임 (`sidecar lab full`). 판정이 갈리면 원문으로 직접 재확인.
4. 캡처된 출력 전체를 `state/` 에 보존.

## 판정 기준

- **C1**: P1 성립 — 논문에 원자/수소/에너지 준위가 실재
- **C2**: P2 성립 — 물리 분류 존재
- **C3**: P3 성립 — 정리로 증명됨
- **C4**: P4 성립 — 수소 준위 ↔ 제타 영점 선행 결과 실재
- **verdict_rule**: VERIFIED = C1–C4 전부 통과; PARTIAL = 2–3개; FALSIFIED = 1개 이하

## 반증 조건

- **F1**: 논문 분류가 순수수학(math) 뿐이면 P2 반증
- **F2**: 초록의 핵심 결과가 "conjecture" 로 명시되면 P3 반증
- **F3**: 논문에 물리적 대상이 부재하면 P1 반증
- **F4**: 수소 준위 대응 결과가 문헌에 부재하면 P4 반증

## 정직한 한계

- **L1**: 1차 대조 근거는 초록·서지 원문이고, 본문 30쪽 전문은 한 경로(Codex 5.6 의 HTML 판독)
  에서만 확인됐다. 본문 인용(§1.1 · §1.2 · Corollary 1.6) 은 단일 경로 근거다.
- **L2**: 영상 텍스트는 자동자막이라 음차 오류가 있다("리반 가설" 등). 다만 주장 사슬의 골자는
  반복 등장해 오인 여지가 낮다.
- **L3**: 정확도 점수(아래)는 정량 측정이 아니라 두 모델의 판단이며, 각각 18점·20점으로 갈렸다.

## 교차 링크

- **paper**: `arXiv:2606.09096` — Masatoshi Suzuki, "Weil's quadratic form via the screw
  function", 2026-06-08, 30쪽, math.NT · math.FA
- **prior**: `arXiv:2308.11860` — Suzuki (2023), screw function 도입
- **evidence_paths**: `state/verdicts/zeta_zeros_vs_atomic_levels/H_001.txt`
- **source_paths**: `state/zeta_zeros_vs_atomic_levels/`
- **related**: H_002 (영상이 왜곡한 실제 대응 — GUE 보편성의 직접 재현)

## 판정

```
verdict_class: FALSIFIED
evidence_summary:
  - C1 FAIL — 초록에 원자·수소·eV 없음. 대상은 "비자명 영점의 허수부를 고유값으로 갖는 자기수반
    연산자"이며, 유한구간 [-a,a] 위 1계 미분연산자의 비국소 실현의 a→∞ 극한으로 얻는 구성.
  - C2 FAIL — 분류 math.NT + math.FA 뿐. 물리 분류 없음 (MSC 11M26·42A82·46E22·47B25).
  - C3 FAIL — 초록이 "we formulate a conjecture" 로 명시. 정리가 아니라 추측이며, 논문은
    리만가설을 증명하지 않는다. 증명된 유한-a 결과들은 리만가설을 가정하지 않는 무조건적 결과.
  - C4 FAIL — 영상이 든 -0.28·-0.38·-0.54·-0.85 eV 는 '간격'이 아니라 수소의 n=7,6,5,4 준위값
    (E_n≈-13.6/n²). 실제 인접 간격은 약 0.10·0.17·0.31 eV. 자유 수소 스펙트럼은 규칙적·가적분계라
    영점의 무작위행렬 통계와 성격이 정반대이고, "수소 준위 ↔ 제타 영점 간격 일치" 결과는 문헌에 없다.
  - 실재하는 대응은 (a) 힐베르트-폴리아 추측 (영점이 어떤 자기수반 연산자의 고유값이라는 프로그램),
    (b) 몽고메리 쌍상관(1973) + 오들리즈코 수치(1987) — 영점 간격 통계가 GUE 무작위행렬 통계와
    일치. 물리 쪽 짝은 무거운 원자핵의 중성자 공명 준위 통계이고, 시간반전 대칭 때문에 핵은 주로
    GOE · 제타 영점은 GUE 다. 같은 숫자가 아니라 같은 보편성 부류라는 뜻.
  - 논문의 실제 기여: Yoshida(1992)·Bombieri(2001,2003)·Connes-Consani(2023)·
    Connes-Consani-Moscovici(2025+) 의 베유 이차형식 결과를 screw function 관점으로 통합해,
    분포로 정의되던 대상을 연속함수로 다룰 수 있게 하고, 위 스펙트럼 실현 추측을 정식화한 것.
falsifiers_triggered: F1, F2, F3, F4 (전부 발동)
criteria_met:
  - C1: FAIL
  - C2: FAIL
  - C3: FAIL
  - C4: FAIL
biggest_misrepresentation: >
  보조함수의 실수 영점(정리) → 제타 영점으로 수렴한다는 극한(미증명 추측) → 실제 원자의 에너지
  준위(물리) — 서로 다른 세 대상을 하나로 합친 것. 과장이 아니라 수학적 대상의 바꿔치기.
accuracy_score: 18-20 / 100 (2경로 독립 채점 · 소수-오일러곱-리만 배경만 정확)
next:
  - H_002 — 영상이 왜곡한 대응(GUE 보편성) 을 우리가 직접 수치로 재현
artifact_paths:
  - state/zeta_zeros_vs_atomic_levels/transcript.txt
  - state/zeta_zeros_vs_atomic_levels/arxiv-2606.09096-abstract.txt
  - state/verdicts/zeta_zeros_vs_atomic_levels/H_001.txt
```
