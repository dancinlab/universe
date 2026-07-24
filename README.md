# universe

우주·양자역학·리만가설을 잇는 주장을 **등록하고 반증하는** 저장소. 결론을 인용해 쌓는 곳이 아니라,
주장마다 기준선을 미리 얼려 두고 측정으로 판정해 남기는 곳이다. 가설 폴더 체계는
`dancinlab/anima` 의 것을 그대로 채택했다.

## 구조

```
universe/
├── HYPOTHESES/            — 가설·판정 레지스트리 (3-표면 불변식)
│   ├── CLAUDE.md          — 폴더 규칙
│   ├── HYPOTHESES.jsonl   — 카드 1장당 1줄 인덱스 (파생 · 손으로 고치지 않음)
│   └── cards/             — 카드 본문 = 한 가설의 SSOT
├── tool/                  — 인덱스 재생성 · 표면 불변식 게이트
├── state/                 — 모든 작업 산출물 (원자료 · 측정 · 판정 증거)
├── CLAUDE.md              — 저장소 규칙
└── CHANGELOG.jsonl        — 이력 (append 전용)
```

## 등록된 가설

| id | 등급 | 주장 |
| --- | --- | --- |
| H_001 | 🔴 FALSIFIED | 스즈키 2026 논문이 제타 영점과 원자 에너지 준위의 직접 관련을 발견했다 |
| H_002 | 🟢 VERIFIED | 제타 영점의 정규화된 간격 분포는 포아송이 아니라 GUE 를 따른다 |
| H_003 | 🔴 FALSIFIED | 완전수 τ(P_k)=2p 가 끈이론 차원을 재현하고 표준모형+중력을 통일한다 (외부 문서 H-PH-9) |

전체 목록은 `HYPOTHESES/HYPOTHESES.jsonl`, 규칙과 등급 정의는 `HYPOTHESES/CLAUDE.md` 를 본다.

## 쓰는 법

```sh
cp HYPOTHESES/cards/_TEMPLATE.md HYPOTHESES/cards/H_00N_<slug>.md   # 새 가설 등록
python3 tool/build_hypotheses_index.py                              # 인덱스 재생성
python3 tool/check_hypotheses_surface.py                            # 불변식 + 인덱스 신선도 게이트
```

## 규칙 요약

- 기준선(bar) 은 측정 **전에** 얼리고 이후 옮기지 않는다. 반증·부정 결과도 그대로 남긴다.
- `HYPOTHESES/` 에 git 으로 추적되는 것은 `cards/**` · `HYPOTHESES.jsonl` · `CLAUDE.md` 뿐이다.
  코드와 결과는 `state/<slug>/` 로 간다.
- "됐다" 는 캡처된 출력으로 증명한다. 모델의 자가판정은 증거가 아니다.

## 라이선스

MIT © dancinlab
