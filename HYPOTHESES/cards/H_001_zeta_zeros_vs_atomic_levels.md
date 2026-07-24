---
ssot: ARCHITECTURE.json
id: H_001
slug: zeta_zeros_vs_atomic_levels
title: 스즈키 2026 논문이 제타 영점과 원자 에너지 준위의 직접 관련을 발견했다
domain: 수론-양자역학 대응
tier: 🔴 FALSIFIED
status: closed
wired: source-checked
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

- **L1**: 대조 대상은 arXiv 의 LaTeXML HTML 렌더링을 평문화한 것이지 PDF 원본이 아니다. 수식은
  MathML 이 평문으로 풀린 형태로 들어온다. 다만 판정에 쓰인 어휘는 전부 산문이고, 변환이 산문을
  보존했다는 대조군으로 수학 용어 빈도(theorem 68 · self-adjoint 54 · screw function 25) 를
  같은 스캔에서 함께 센다 — 변환 유실이면 이쪽도 0 이 나와야 한다.
- **L2**: 영상 텍스트는 자동자막이라 음차 오류가 있다("리반 가설" 등). 다만 주장 사슬의 골자는
  반복 등장해 오인 여지가 낮다.
- **L3**: 정확도 점수(아래)는 정량 측정이 아니라 두 모델의 판단이며, 각각 18점·20점으로 갈렸다.
  판정 자체(FALSIFIED) 는 이 점수와 무관하게 기계 검사만으로 선다.
- **L4**: C1 은 어휘 부재로 판정한다. 논문이 물리 개념을 완전히 다른 용어로만 부르는 경우는
  이 검사가 놓칠 수 있다. 다만 분류(C2)·추측 여부(C3)·산술(C4) 이 독립적으로 같은 방향이라
  단일 검사에 판정이 걸려 있지는 않다.

## 교차 링크

- **paper**: `arXiv:2606.09096` — Masatoshi Suzuki, "Weil's quadratic form via the screw
  function", 2026-06-08, 30쪽, math.NT · math.FA
- **prior**: `arXiv:2308.11860` — Suzuki (2023), screw function 도입
- **evidence_paths**: `state/verdicts/zeta_zeros_vs_atomic_levels/H_001_source_check.txt` (원문 기계
  검사 · 1차 증거) · `state/verdicts/zeta_zeros_vs_atomic_levels/H_001.txt` (2모델 독립 판독 · 보조)
- **source_paths**: `state/zeta_zeros_vs_atomic_levels/` (자막 전문 · 서지 · 본문 전문 · 검사 스크립트)
- **related**: H_002 (영상이 왜곡한 실제 대응 — GUE 보편성의 직접 재현)

## 판정

```
verdict_class: FALSIFIED
measured (원문 기계 검사 · 본문 30쪽 평문 150,952자 전수 스캔):
  물리 어휘 빈도    atom 0 · atomic 0 · hydrogen 0 · energy level 0 · electron 0 · eV 0
                    Schrodinger 0 · Schrödinger 0 · Hamiltonian 0 · quantum jump 0  (합계 0)
  수학 어휘 빈도    theorem 68 · self-adjoint 54 · screw function 25 · Weil quadratic form 7
                    Riemann zeta 5 · nontrivial zeros 3 · conjecture 2 · nonlocal 1
                    (변환 유실 대조군 — 산문이 보존됐음을 같은 스캔이 스스로 보인다)
  분류              Number Theory (math.NT); Functional Analysis (math.FA) — 물리 분류 0건
  수소 보어 준위    n=4 -0.8500 · n=5 -0.5440 · n=6 -0.3778 · n=7 -0.2776 eV
                    → 영상이 '간격'이라 부른 네 숫자와 전부 일치 = 그것들은 준위값이다
  실제 인접 간격    0.3060 · 0.1662 · 0.1002 eV — 영상이 든 숫자와 일치하는 것이 하나도 없다
evidence_summary:
  - C1 FAIL — 본문 전체에 원자·수소·eV 없음(빈도 0). 대상은 "비자명 영점의 허수부를 고유값으로 갖는 자기수반
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
verification_path: >
  1차 판정은 두 프런티어 모델의 독립 판독이었고, 저장소 규칙이 모델 자가판정을 증거로 인정하지
  않으므로 본문 전문을 내려받아 어휘 빈도·분류·산술만으로 재판정했다. 판단 단계가 없는 검사이며
  재실행 시 같은 수치가 나온다. 두 경로의 결론이 일치했다.
next:
  - H_002 — 영상이 왜곡한 대응(GUE 보편성) 을 우리가 직접 수치로 재현 (완료 · 🟢 VERIFIED)
artifact_paths:
  - state/zeta_zeros_vs_atomic_levels/verify.py
  - state/zeta_zeros_vs_atomic_levels/data/arxiv-2606.09096v1-fulltext.txt
  - state/zeta_zeros_vs_atomic_levels/transcript.txt
  - state/zeta_zeros_vs_atomic_levels/arxiv-2606.09096-abstract.txt
  - state/verdicts/zeta_zeros_vs_atomic_levels/H_001_source_check.txt
  - state/verdicts/zeta_zeros_vs_atomic_levels/H_001.txt
```
