# SOXL results index (classified)

Pair-grid numbers are kept only as a **negative control**. This lab is SOXL-only.

| ID | Class | Engine | Verdict | File |
|----|-------|--------|---------|------|
| P7-01 | TICK coverage | aggTrades vs 1h | **PASS** 1392/1392 | `p7_tick_coverage.soxl.json` |
| P7-03 | BAR ATR 0.40/±5 | wick-touch | **OVERTURNED** by P7-04 | `p7_bar_hedge_report.OVERTURNED.json` |
| P7-04 | TICK ATR 0.40/±5 | path-exact | **FAIL** pair −5.97%/DD −20.07%; same-LS +12.27%/DD −17.68% (short leg BAR); SOXL-only +9.29%/DD −45.24% | `p7_tick_hedge.base.soxl.json` |
| P7-05 usdt | User 5x ±20U 200-grid 5k+5k | TICK both legs | **FAIL / liquidated long** −12.78% / DD −80.16%; 28/58 up days | `p7_05_usdt20.json` + `p7_05_usdt20_daily.csv` |
| P7-05 pct | User 5x ±20% 200-grid 5k+5k | TICK both legs | **FAIL / liquidated long** −18.65% / DD −77.16%; 29/58 up days | `p7_05_pct20.json` + `p7_05_pct20_daily.csv` |

Full P7-04 dump (includes SOXS pair columns): `p7_tick_hedge_report.json`.
