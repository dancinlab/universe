---
ssot: ARCHITECTURE.json
id: H_002
slug: zeta_gue_universality
title: 제타 영점의 정규화된 간격 분포는 포아송이 아니라 GUE 를 따른다
domain: 수론-양자역학 대응
tier: 🔵 PROPOSED
status: proposed
wired: none
pre_register_frozen: true
frozen_at: 2026-07-25
since: 2026-07-25
related: [H_001]
---

# H_002 — 제타 영점 간격의 GUE 보편성 직접 재현

> 📍 설계 SSOT → [ARCHITECTURE.json](../../ARCHITECTURE.json) · 등록 규칙 → [HYPOTHESES/CLAUDE.md](../CLAUDE.md)

## 가설

리만 제타함수 비자명 영점의 허수부 γ 를 평균 밀도로 정규화(unfolding=평균 간격이 1이 되도록
펴는 것) 했을 때, 이웃 간격 분포는 무상관 무작위 배열(포아송) 이 아니라 **GUE(가우스 유니터리
앙상블 = 시간반전 대칭이 깨진 양자계의 무작위행렬 모형)** 의 간격 분포를 따른다.

## 근거

H_001 에서 확인했듯, 대중 서사가 "원자 에너지 준위와 일치" 로 왜곡한 실제 결과는 몽고메리
쌍상관(1973) 과 오들리즈코 수치실험(1987) 의 **통계적 일치**다. 이것은 우리 저장소에서 외부
주장에 의존하지 않고 직접 재현할 수 있는 1차 사실이며, 수론과 양자적 스펙트럼을 잇는 모든 후속
가설의 바닥돌이다. 남의 결론을 인용하는 대신 우리 손으로 측정해 두는 것이 목적이다.

## 예측

- **P1**: 정규화된 이웃 간격 분포가 GUE 위그너 추측식에 포아송보다 유의하게 가깝다.
- **P2**: s→0 에서 간격이 억눌린다(level repulsion=준위 반발). 포아송이면 s=0 에서 최대여야 한다.
- **P3**: 이 일치는 영점을 높은 곳(예: 10^12 번째 부근) 에서 취할수록 더 좋아진다.

## 변수

- **axis1_window**: [최초 10^4 개, 10^5 번째 부근, 10^6 번째 부근]
- **axis2_statistic**: [이웃 간격 분포, 쌍상관 함수, 수 분산(number variance)]
- **axis3_reference**: [GUE 위그너 추측식, 포아송, GOE]

## 실행 규약

- 영점 허수부는 공개 데이터(오들리즈코 표) 또는 `mpmath.zetazero` 로 산출하고, 어느 쪽인지와
  개수·구간을 실행 로그에 남긴다.
- 평균 밀도 N(T) ≈ (T/2π)·log(T/2πe) 로 unfolding.
- 세 참조 분포와의 거리를 콜모고로프-스미르노프 통계량으로 계산.
- 결정론적: 난수 미사용. 재실행 시 동일 수치가 나와야 한다.
- 산출물은 `state/zeta_gue_universality/` 에, 캡처 출력은
  `state/verdicts/zeta_gue_universality/H_002.txt` 에 보존.

## 판정 기준

- **C1**: KS(관측, GUE) < KS(관측, 포아송) × 0.5 — 전 구간에서
- **C2**: 관측 분포의 s ≤ 0.2 구간 질량이 포아송 예측의 절반 이하 (준위 반발 확인)
- **C3**: 구간을 높일수록 KS(관측, GUE) 가 단조 감소
- **verdict_rule**: VERIFIED = C1+C2+C3; PARTIAL = C1+C2; FALSIFIED = C1 실패

## 반증 조건

- **F1**: KS(관측, 포아송) ≤ KS(관측, GUE) → 가설 FALSIFIED
- **F2**: s→0 에서 간격 분포가 억눌리지 않음 → P2 반증 (보편성 서사 붕괴)
- **F3**: GOE 가 GUE 보다 일관되게 더 잘 맞음 → 대칭 부류 귀속 오류

## 정직한 한계

- **L1**: 유한 표본 재현이다. 무한 극한에서의 보편성을 증명하는 것이 아니다.
- **L2**: unfolding 방식에 결과가 민감할 수 있다 — 밀도 공식과 구간 폭을 사전 고정해 둔다.
- **L3**: 이 가설이 통과해도 "리만가설이 참" 이나 "물리적 해밀토니안이 존재한다" 는 따라 나오지
  않는다. 통계적 일치는 힐베르트-폴리아 프로그램의 정황 증거이지 증명이 아니다.

## 교차 링크

- **prior**: 몽고메리(1973) 쌍상관 · 오들리즈코(1987) 수치 · 베리-키팅(1999) H=xp 반고전 모형
- **related**: H_001 (이 대응을 왜곡한 대중 서사의 판정)
- **evidence_paths**: `state/verdicts/zeta_gue_universality/H_002.txt` (미생성 — 실행 전)

## 판정

```
verdict_class: PROPOSED
evidence_summary:
  - 미실행. 기준선(C1·C2·C3) 만 사전 동결됨.
falsifiers_triggered: none
criteria_met:
  - C1: 미측정
  - C2: 미측정
  - C3: 미측정
next:
  - 영점 데이터 출처 확정 → unfolding → KS 3종 비교 실행
artifact_paths: []
```
