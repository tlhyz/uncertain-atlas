# SOXL personal lab — classified catalog

Three classes only. Anything not SOXL stays out.

## 1. Data

| ID | Kind | Window | Fact (independently recounted) |
|----|------|--------|--------------------------------|
| D-TICK-LOCAL | UM aggTrades daily CSV | 2026-07-15 → 2026-09-11 | 59 days, 0 gaps, 31,190,286 prints, 1,646,097,593 bytes |
| D-TICK-PRICE | same | same | min **85.94** max **191.10**; daily medians 101.96–165.41 |
| D-TICK-MANIFEST | sha256+bytes | same | `data/manifests/binance_SOXLUSDT_aggTrades_2026-07-15_2026-09-11.json`; first/mid/last checksums match disk |
| D-TICK-HIST | manifest only | 2026-07-09 → 09-11 | lists 07-09→07-14 **not present** on this VM |
| D-BAR-1H | Vision 1h klines | 2026-07-16 00:00Z → 2026-09-11 23:00Z | **1392** bars |
| D-COV | TICK vs 1h | overlap | **1392/1392**, missing trades 0, p99 close rel err 6.93e-5 |
| D-BLOCKED | older ticks | 2024-09→11, 2025-09→10 | P3-09 / P3-10 still blocked |

Tick CSVs are **local-only**. Schema: `ts_ms,price,qty,quote_qty,is_buyer_maker,agg_id`.

## 2. Params

| ID | Spec | Values | Source of truth |
|----|------|--------|-----------------|
| P-USER | Personal moving grid | 5x isolated; 200 arithmetic rungs; **±20 USDT** and **±20%**; 5000U long + 5000U short; Base 2 bps; TICK fills; reanchor when price exits band | `params/user_moving_grid.yaml` **and** `../src/analysis/user_moving_grid.py` (`USER_*` constants) |
| P-ATR | Research template | ATR step 0.40 / range ±5; 1x; 10k; used in P7-03/04 | `params/research_atr.yaml` |
| P-WIN | Windows | local ticks 59d; user-grid PnL 2026-07-16→09-11 | `params/windows.yaml` |

Step size check: ±20U over 200 rungs → span 40 / 199 ≈ **0.201005** USDT. Unit test `test_usdt_levels_span_40` locks this.

## 3. Results

Rounded figures below match the JSON to 1 decimal pp. Exact floats live in `results/`.

| ID | What | Exact / rounded | Live? |
|----|------|-----------------|-------|
| R-P7-01 | Coverage | 1392/1392 PASS | n/a |
| R-P7-04-SOXL | SOXL-only long ATR grid TICK | +9.2949% / DD −45.2386% | **NO** |
| R-P7-04-LS | Same-symbol L+S (long TICK, short BAR) | +12.2657% / DD −17.6822% / inv 78.03% | **NO** — mixed engine |
| R-P7-04-PAIR | SOXL+SOXS long grids TICK | −5.9711% / DD −20.0660% | **NO** FAIL |
| R-P7-04-BH | Daily 50/50 B&H | +2.9391% / DD −2.2644% | honest hedge on this window |
| R-P7-03 | BAR pair +18.8% / −4.4% | **overturned** | do not cite |
| R-P7-05-U | User ±20U 5x 5k+5k TICK | −12.7777% / DD −80.1570%; long **liquidated**; short +74.44%; 28/58 up days; end equity 8722.23 | **NO** |
| R-P7-05-P | User ±20% 5x 5k+5k TICK | −18.6506% / DD −77.1628%; long **liquidated**; short +62.70%; 29/58 up days; end equity 8134.94 | **NO** |
