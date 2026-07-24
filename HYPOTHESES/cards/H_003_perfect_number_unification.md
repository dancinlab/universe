---
ssot: ARCHITECTURE.json
id: H_003
slug: perfect_number_unification
title: 완전수 τ(P_k)=2p 가 끈이론 차원 위계를 재현하고 표준모형+중력을 통일한다 (외부 문서 H-PH-9)
domain: 수론-물리 대응
tier: 🔴 FALSIFIED
status: closed
wired: source-checked
pre_register_frozen: true
frozen_at: 2026-07-25
since: 2026-07-25
related: [H_001]
---

# H_003 — 완전수 통일 패턴(H-PH-9) 검증

> 📍 설계 SSOT → [ARCHITECTURE.json](../../ARCHITECTURE.json) · 등록 규칙 → [HYPOTHESES/CLAUDE.md](../CLAUDE.md)

## 가설

외부 저장소 문서 `H-PH-9`(dancinlab/archive-TECS-L · `math/docs/hypotheses/`) 의 핵심 주장 —
짝수 완전수 P_k = 2^(p-1)(2^p−1) 의 약수 개수 τ(P_k)=2p 가 끈이론 차원 위계(4·6·10·14·26) 를
재현하고, σ·φ·τ 함수가 게이지·중력·시공간 구조를 동시에 부호화해 "표준모형+중력" 을 통일하며,
그 통계적 유의성이 p<0.0002 · CERN 종합 6.4σ 라는 주장 — 이 성립한다.

## 근거

문서가 정직하게 산술(EXACT) 과 물리 대응(STRUCTURAL) 을 나누고 사후성 태그([MODEL]·FITTED) 를
붙였으므로, 쟁점은 "산술이 참인가" 가 아니라 **물리 대응이 정보를 담는가 아니면 사후 짜맞추기인가**
하나로 좁혀진다. 이는 우리 저장소에서 결정론적으로 측정 가능하다.

## 예측

- **P1**: 문서가 든 차원 매칭 5개(4·6·10·14·26) 가 각각 표준적·독립적 물리 식별이다.
- **P2**: τ(P_k)=2p 수열이 현대 통일 그림의 중심인 M이론 11차원 · G₂ 다양체 7차원을 담는다.
- **P3**: 몬테카를로 p<0.0002 가 이 주장에 대한 유의미한 유의확률이다.
- **P4**: 질량 공식의 표적 적중(예: m_τ 오차 0.048%) 이 표현식 계열의 기본 명중률로는 설명되지
  않는다 — 즉 사후 탐색으로 쉽게 나올 수 없다.

## 변수

- **axis1_source**: [H-PH-9 원문 2789줄, arXiv/표준 물리 정의]
- **axis2_checker**: [Claude Fable 5, OpenAI Codex 5.6] — 독립 2경로 적대적 리뷰
- **axis3_enumeration**: 알파벳 {2,4,6,12,48} · 연산 {+,−,×,÷} · 잎 ≤5 전수 열거 (자체 스크립트)

## 실행 규약

1. 원문을 내려받아 `state/` 에 보존.
2. 두 프런티어 모델에 동일 지시문으로 적대적 리뷰 독립 위임 — 5/5 매칭 항목별 감사 · 널모형 ·
   look-elsewhere 정량화 · "진짜 유도" 항목 검증.
3. look-elsewhere 는 우리가 직접 결정론적으로 측정: 문서와 같은 재료·복잡도로 만들 수 있는 서로
   다른 값을 전수 열거하고, 표적별 3% 밴드 안 경쟁 표현식 수를 센다(`measure.py`).
4. 모든 출력을 `state/verdicts/` 에 캡처.

## 판정 기준

- **C1**: P1 성립 — 5개 매칭 전부 표준·독립
- **C2**: P2 성립 — 11 또는 7 이 수열에 등장
- **C3**: P3 성립 — 널모형이 실제 선택 자유도를 반영
- **C4**: P4 성립 — 3% 밴드 경쟁 표현식이 소수(예: 표적당 ≤2)
- **verdict_rule**: VERIFIED = C1–C4 전부; PARTIAL = 2–3개; FALSIFIED = 1개 이하

## 반증 조건

- **F1**: 차원 매칭에 범주 오류(군 차원↔다양체 차원) 가 있으면 P1 반증
- **F2**: τ(P_k)=2p 가 항상 짝수라 11·7 이 원리상 불가능하면 P2 반증
- **F3**: 널모형이 사후 선택된 표적/함수/식문법 자유도를 누락하면 P3 반증
- **F4**: 3% 밴드에 표적당 수십 개 경쟁 표현식이 존재하면 P4 반증

## 정직한 한계

- **L1**: 원문은 arXiv 논문이 아니라 사설 저장소의 연구 노트다. 판정 대상은 "이 문서의 주장" 이며
  Koide 관계(1981) 같은 그 안의 실제 경험적 사실을 부정하는 것이 아니다.
- **L2**: look-elsewhere 열거는 지수연산을 제외한 보수적 하한이다. 문서는 φ^σ 같은 지수식도
  쓰므로 실제 탐색력은 측정치보다 크다. 즉 이 한계는 판정을 약화하는 방향이 아니다.
- **L3**: C1·C3 의 "표준 물리 식별인가" 판단은 문헌 대조에 기댄다. 다만 결정적 항목(G₂ 14 대 7)
  은 정의 문제라 두 경로가 독립적으로 같은 결론에 도달했다.

## 교차 링크

- **source**: `dancinlab/archive-TECS-L` · `math/docs/hypotheses/H-PH-9-perfect-number-string-unification.md`
- **evidence_paths**: `state/verdicts/perfect_number_unification/H_003.txt` (열거 · 1차 증거) ·
  `state/verdicts/perfect_number_unification/H_003_two_model_review.txt` (2모델 적대 리뷰 · 보조)
- **source_paths**: `state/perfect_number_unification/` (원문 · 열거 스크립트)
- **related**: H_001 (같은 실패 유형 — 산술 참·물리 대응 사후짜맞추기)

## 판정

```
verdict_class: FALSIFIED
measured (look-elsewhere 전수 열거 · 재실행 바이트 동일):
  재료 {2,4,6,12,48} · 연산 +−×÷ · 잎 ≤5 → 서로 다른 양수값 27,789개
  표적                doc오차%   3% 밴드 경쟁 표현식 수
  m_electron 0.511     2.200        169
  m_up       2.16      7.400        102   (정확히 일치하는 표현식 존재)
  m_down     4.67      0.070         83
  m_strange  93.4      2.800        197
  m_muon     105.66    0.300         56
  m_charm    1270      2.000         35
  m_tau      1776.86   0.048         72   ← "기적적 0.048%" 의 실체
  m_bottom   4180      2.000         27
  m_top      172500    0.170          6
  1/alpha    137.036   0.026         63
  밀도: 임의의 십진 격자점의 98.1% 가 3% 이내, 67.8% 가 0.05% 이내로 이 집합에 적중된다.
evidence_summary:
  - C1 FAIL — 5/5 매칭 중 "14 = G₂ 홀로노미 다양체" 는 범주 오류. G₂ 다양체는 7차원이고 14는
    리 군 G₂ 자체의 차원. 시공간 차원(4·10·26)·콤팩트 다양체 차원(6)·군 차원(14) 을 섞어
    5/5 를 만들었다. 게다가 6=10−4 라 독립 적중도 아니다. 실제 최대 3/5.
  - C2 FAIL — τ(P_k)=2p 는 항상 짝수라 M이론 11차원·G₂ 다양체 7차원이 원리상 영원히 등장 불가.
    현대 통일 그림의 중심축이 구조적으로 배제된다.
  - C3 FAIL — 널모형 '4~62 짝수 5개 무작위 추출' 이 틀렸다. (a) 수열은 결정론이라 추첨 자체가
    없고, (b) 표적 {4,6,10,14,26}=2×{소수 5개} 를 수를 본 뒤 골랐으며, (c) 함수(σ·τ·φ·…)·물리
    정수풀·식문법 선택 자유도를 전부 시행횟수 1로 놓았다. p<0.0002 는 누락된 시행횟수를 1로 둔
    수. p=0.0002 도 단측 환산 3.54σ 이지 6.4σ 가 아니다.
  - C4 FAIL — 3% 밴드에 표적당 6~197개(중앙값 ~68) 의 경쟁 표현식. m_τ 의 "0.048%" 는 이 계열의
    기본 명중률이며 up·charm 등은 정확 일치 표현식까지 존재. 밀도 98.1% 는 "아무 표적이나 준다"
    해도 3% 안에 뭔가 걸린다는 뜻.
  - 두 모델 독립 수렴: 27,789개 서로 다른 값, 표적별 경쟁 수(169·102·83·197·56·35·72·27·6) 가
    우리 자체 재현과 정확히 일치.
  - 정밀 측정 대조: m_μ=105.6583745(24) MeV 에 '106' 은 ~10^5σ 배제, m_τ=1776.86(12) 에 '1776'
    은 ~7σ 배제. 물리학 기준으론 이미 반증된 값들이다.
  - 살아남는 것: 496=dim(E₈×E₈)=dim(SO(32)) 중첩 하나뿐인데, 이는 Green-Schwarz(1984) 이래 알려진
    기존 사실이고(모든 짝수완전수는 삼각수, dim SO(n)=T(n−1)) 문서의 기여가 아니다.
falsifiers_triggered: F1, F2, F3, F4 (전부 발동)
criteria_met:
  - C1: FAIL
  - C2: FAIL
  - C3: FAIL
  - C4: FAIL
verdict: 🔴 수비학(numerology). 산술은 자명 참, 물리 대응은 사후 짜맞추기.
next:
  - 문서에 반증 기회를 준다면: 수열 다음 항 τ=34·38·62 (p=17·19·31) 의 물리적 의미를 결과를 보기
    전에 사전등록하고, 미사용 무차원 관측량 하나를 오차까지 예측해 블라인드 검정. 사후 적중 추가는
    아무것도 해결하지 못한다.
artifact_paths:
  - state/perfect_number_unification/measure.py
  - state/perfect_number_unification/H-PH-9-source.md
  - state/verdicts/perfect_number_unification/H_003.txt
  - state/verdicts/perfect_number_unification/H_003_two_model_review.txt
```
