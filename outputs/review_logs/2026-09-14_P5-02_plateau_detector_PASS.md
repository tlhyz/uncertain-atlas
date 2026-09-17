# Review Log — P5-02 Parameter Plateau Detector (ATR Step)

## Meta

- **date_utc:** 2026-09-14T08:20Z
- **task:** P5-02
- **method:** `detect_plateau` / `analyze_sweep` on P2-05 BTC ATR step sweep
- **input:** outputs/experiments/crypto_btc_grid_atr_step/crypto_results.json
- **output:** outputs/experiments/crypto_btc_grid_atr_step/plateau_report.json

## Implementation

- **`src/analysis/parameter_plateau.py`:** `overfit_flag`, `is_plateau`, `robust_pick`, `detect_plateau`, `analyze_sweep`
- Flags: `PLATEAU_ACTIONABLE`, `PLATEAU_INERT`, `SENSITIVE`, `OVERFIT`, `insufficient`
- **`scripts/run_p5_plateau_detector.py`** — replays existing sweep JSON
- **`tests/test_parameter_plateau.py`** — 7 tests (152 full suite green)

## Results — BTC C1 ATR step [0.30–0.60], reference 0.40

| Metric | Flag | Spread | Reference rank | Robust pick |
|--------|------|--------|----------------|-------------|
| **total_return** | **PLATEAU_INERT** | 0.20pp | — | — |
| **calmar** | **SENSITIVE** | 1.85 | **4/4 (worst)** | 0.30 |

Return spread 0.002 across ~−87% band → flat **inert** plateau (spacing tuning dead). Calmar spread 1.85 → sensitive; default 0.40 worst by Calmar.

## Question

Is the parameter plateau detector implemented and does it correctly classify the ATR step sweep?

## Findings

1. **Implementation:** PASS — god-param OVERFIT rule + spread threshold + inert failure-band detection.
2. **W-02 / Q-crypto-2:** CONFIRM FAIL — 0.40 ATR not on actionable plateau; prior LOW-confidence claim remains unsupported.
3. **Robust pick:** 0.30 (median Calmar rank), not 0.40 default.
4. **Dual metric:** Returns flat (inert); Calmar sensitive — report both to avoid scale confusion.

## Verdict

- **task_verdict:** **DONE**
- **implementation_verdict:** **PASS**
- **strategy_verdict:** **FAIL** — no deployable ATR step; spacing inert in failure band

## Red team (≥5)

1. Single C1 window — detector replays P2-05 only
2. Calmar vs return spread use different scales — must specify metric in reports
3. `tol=0.15` absolute on Calmar misfires; inert check uses return spread separately
4. Robust pick 0.30 still −87.39% — not actionable despite “best” rank
5. No conservative fill replay — base fill only

## Next

- P5-03 walk-forward split BTC 2019+
- Apply detector to dual-book tech sweeps when finalists exist
- Update GAP_ANALYSIS stub note when convenient
