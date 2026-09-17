# Review Log — P6-02 Promote BTC Row to MEDIUM Confidence

## Meta

- **date_utc:** 2026-09-14T10:12Z
- **task:** P6-02
- **method:** Formal promotion gate checklist (ROADMAP L11 criteria)
- **output:** outputs/experiments/p6_promotion_gates/btc_promotion_gate.json

## Implementation

- **`src/analysis/live_promotion.py`:** gate definitions + `evaluate_promotion()`
- **`scripts/run_p6_promotion_gate.py`:** `--asset BTC` runner
- **`tests/test_p6_promotion_gate.py`:** BTC/ETH FAIL smoke (167 tests green full suite pending)
- **`outputs/LIVE_CANDIDATES.md`:** BTC confidence **MEDIUM → LOW**

## Promotion gates (BTC, 1.5x lev 0.40 ATR ±5)

| Gate | Status | Blocks | Evidence |
|------|--------|:------:|----------|
| Temporal OOS holdout | **fail** | yes | P5-04 holdout 2024: −86.44% |
| Calendar walk-forward | **fail** | yes | P5-03 mean test −86.58% |
| MC DD tail | **fail** | yes | P5-05 P(DD>20%)=89% |
| C1 tick edge | **fail** | yes | P2-02 all lev −87% (C-06) |
| Param plateau | **fail** | yes | P5-02 0.40 worst Calmar |
| Portfolio C-07 | **fail** | yes | OOS+MC gates FAIL |
| Gate fill cal | conditional | no | P6-01 BAR fill_ratio 0.986 |
| A/B PERP>ETF | conditional | no | C-02 BAR only; different engine |

**Blocking failures: 6/6 required gates**

## Question

Can the BTC crypto grid row be promoted to (or retain) MEDIUM live confidence?

## Findings

1. **Promotion:** **FAIL** — 6 blocking gates; OOS catastrophic (−86.44% holdout 2024).
2. **Stale label:** LIVE_CANDIDATES had **MEDIUM** from pre-P2 A/B bar evidence — contradicted by C-06 (C1 tick NO EDGE) and C-07 (robustness FAIL).
3. **A/B PERP win (C-02)** remains MEDIUM-HIGH for *structure choice* (PERP vs ETF) but does **not** validate the crypto grid FSM at listed params.
4. **Demotion applied:** BTC row → **LOW** with evidence `C-06/C-07 FAIL; A/B bar only`.
5. **Gate fill calibration (P6-01)** does not rescue — execution drift modest; strategy has no edge.

## Verdict

- **task_verdict:** **done**
- **promotion_verdict:** **FAIL**
- **confidence_action:** **MEDIUM → LOW** (honest downgrade)

## Red team (≥5)

1. A/B bar window (Gate 9k bars) ≠ C1 tick window — different conclusions both valid
2. BTC holdout only tested on BAR klines — tick holdout likely similar (~−87%)
3. MC DD gate uses dual-book 65d — crypto-only DD may differ but still FAIL at C1
4. Demotion does not remove row — remains research reference config
5. ETH/SOL still MEDIUM in table — P6-03 next (same expected FAIL)

## Next

- P6-03 ETH promotion gate (expected FAIL + demote)
- P6-05 final LIVE_CANDIDATES synthesis
