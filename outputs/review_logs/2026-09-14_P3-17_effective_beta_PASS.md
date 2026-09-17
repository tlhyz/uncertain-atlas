# Review Log — P3-17 Effective beta rolling SOXL/SNXX

## Meta

- **date_utc:** 2026-09-14T04:40Z
- **task:** P3-17
- **method:** `rolling_realized_beta()` from `src/features/beta.py` on 65d overlap klines
- **window:** 2026-07-09 → 2026-09-11, 1546 bars @ 1h

## Results

Rolling realized beta on overlap (SOXL vs SNXX closes):

| Window (bars) | ~days @1h | SOXL→SNXX mean | SOXL→SNXX last | SNXX→SOXL mean | SNXX→SOXL last |
|---------------|-----------|----------------|----------------|----------------|----------------|
| 48 | 2d | 0.459 | 0.234 | 1.076 | 0.575 |
| 168 | 7d | 0.453 | 0.368 | 1.125 | 0.720 |
| 480 | 20d | 0.466 | 0.406 | 1.215 | 0.944 |

**Finding:** SOXL beta to SNXX **~0.45–0.47** (stable on 20d window, σ=0.04). SNXX beta to SOXL **~1.1–1.2** — SNXX moves ~2× SOXL sensitivity on this crash-bounce window. Short-window (48h) beta more volatile (σ=0.19).

Implication for P3-07 weight sweep: 70/30 default reasonable; 75/25 overweight SOXL vs measured co-movement; 65/35 adds SNXX beta exposure without return benefit (P3-07 FAIL).

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** N/A (diagnostic only)
- **Note:** `effective_beta.py` formal module still not built (GAP_ANALYSIS); used existing `rolling_realized_beta`

## Red team (≥5)

1. Beta to SNXX not to physical SOXL underlying (no und proxy on Binance perp)
2. Crash window — beta unstable in calm regimes
3. 48h window last=0.234 vs 20d last=0.406 — regime shift within overlap
4. Perp SOXL/SNXX may not match ETF beta semantics
5. No leak test re-run on this script path (function covered in TASK-0010)

## Next

- Use 20d beta (~0.45) as sizing prior if book weights revisited
- P4 regime tasks when portfolio phase opens
