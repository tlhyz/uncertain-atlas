# Review Log — P6-01 Gate Fill Ratio Calibration vs Binance

## Meta

- **date_utc:** 2026-09-14T10:05Z
- **task:** P6-01
- **config:** configs/experiments/gate_calibration.yaml
- **method:** BAR BACKTEST grid limit fills on overlapping BTC 1h (Gate cache vs Binance 65d klines)
- **output:** outputs/experiments/gate_calibration_v1/

## Implementation

- **`src/analysis/gate_fill_calibration.py`:** align Gate/Binance bars; synthetic crypto grid pending orders; `resolve_bar_fills` base + conservative
- **`scripts/run_p6_gate_fill_calibration.py`:** runner → JSON + report.md
- **`scripts/run_gate_oos.py`:** delegates to P6-01 runner (fill_ratio step only)
- **`tests/test_p6_gate_fill_calibration.py`:** alignment + volume sensitivity smoke (165 tests green)

## Data overlap

| Source | Bars | Range |
|--------|-----:|-------|
| Gate `futures_BTC_USDT_1h_ab_candles.csv` | 10,003 | 2025-07-23 → 2026-09-12 |
| Binance `binance_futures_BTCUSDT_1h_2026-07-09_2026-09-12_klines.csv` | 1,560 | 2026-07-09 → 2026-09-11 |
| **Aligned overlap** | **1,560** | 2026-07-09 → 2026-09-11 |

## Base fill mode (20% participation)

| Metric | Value |
|--------|------:|
| Pending grid orders | 19,765 |
| Binance filled | 1,466 (7.4%) |
| Gate filled | 1,445 (7.3%) |
| **Fill ratio Gate/Binance (count)** | **0.986** |
| **Fill ratio Gate/Binance (notional)** | **0.986** |
| Volume ratio Gate/Binance (mean quote vol) | **0.345** |
| Mean \|close\| diff | 0.71 bps |
| Mean \|range\| diff | **320 bps** |
| Volume-swap only (Binance OHLC + Gate vol) | **1.000** (no change) |

## Conservative fill mode

| Metric | Value |
|--------|------:|
| Fill ratio Gate/Binance (count) | **1.034** |
| Fill ratio Gate/Binance (notional) | **1.035** |

Conservative extra-tick penetration interacts with Gate's wider/different wicks → slightly **more** fills on Gate.

## Question

Can we quantify Binance-structure grid fill drift when executed on Gate?

## Findings

1. **Implementation:** PASS — measurable fill_ratio on 1560-bar overlap; artifacts written.
2. **Volume is not binding** at 500 USDT grid target — participation budget never constrains fills (swap=1.0 despite Gate vol 34% of Binance).
3. **OHLC path divergence drives drift** — mean range diff 320 bps explains ±1–3% fill count shift base/conservative.
4. **BAR BACKTEST only** — no Gate aggTrades; tick-path calibration still blocked.
5. **Does not rescue strategy** — C-07 OOS/MC gates still block live promotion; calibration is execution metadata only.
6. **SOXL/SNXX Gate calibration** — not attempted (INSUFFICIENT_GATE_HISTORY for tech tick windows).

## Verdict

- **task_verdict:** **done**
- **implementation_verdict:** **CONDITIONAL PASS**
- **calibration_verdict:** fill_ratio ≈ **0.99 base / 1.03 conservative** on BTC 1h — modest drift, dominated by wick shape not volume at tested grid sizes
- **live_confidence:** unchanged LOW — no MEDIUM candidate exists (P3-16)

## Red team (≥5)

1. Synthetic grid per bar ignores inventory state / reanchor — structural not path-exact
2. 500 USDT target may understate live book fill pressure at 10k portfolio scale
3. Gate quote_volume units may not be directly comparable to Binance Vision klines
4. Conservative mode Gate>Binance fills counterintuitive for "worse venue" narrative — wick asymmetry artifact
5. 1h bar calibration irrelevant to SOXL tick FSM where execution risk concentrates

## Next

- P6-02/03: document FAIL to promote BTC/ETH to MEDIUM (C-07)
- P6-05: synthesize LIVE_CANDIDATES.md with fill calibration footnote
- Future: Gate aggTrades for tick-path fill_ratio if Gate API quota allows
