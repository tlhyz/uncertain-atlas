# Review Log — P7-02 SOXL↔SOXS beta / hedge ratio

## Meta

- **date_utc:** 2026-09-15T21:55Z
- **task:** P7-02
- **data_class:** BAR (Binance Vision 1h klines)
- **window:** 2026-07-16 09:00Z → 2026-09-11 23:00Z
- **n_bars:** 1383 aligned
- **script:** `scripts/run_p7_soxl_soxs_hedge.py`
- **output:** `outputs/experiments/soxl_soxs_hedge/hedge_report.json`

## Probe (P7-01 partial)

Binance UM `SOXSUSDT` Vision aggTrades:

| Field | Value |
|-------|-------|
| earliest | **2026-07-16** (2026-07-15 = 404) |
| latest probed | 2026-09-14 |
| days with ZIP | **61 / 61** (no gaps) |
| vs SOXL overlap | 2026-07-16 → 2026-09-11 |

Tick download running in tmux `p7-soxs-ticks` (not required for this BAR verdict).

## Diagnostics (1h log returns)

| Metric | SOXL↔SOXS | SOXL↔SNXX (P3-17, 20d) |
|--------|-----------|-------------------------|
| corr | **−0.988** | +0.45 (same direction) |
| β(SOXS on SOXL) | **−0.991** | n/a |
| 1:1 residual vol | 0.00255 | — |
| SOXL vol | 0.01617 | — |
| residual / SOXL vol | **15.8%** | — |
| OLS hedge ratio h* | 0.986 | — |

**Inverse gate:** PASS (`corr < −0.70` and `β < −0.50`).

**Implication:** SNXX was never an inverse hedge. SOXS on this Binance UM window **is**.

## Red team (≥5)

1. BAR returns, not tick VWAP — microstructure lead/lag unmeasured
2. 57-day listing window only; no pre-2026-07-16 history
3. Perp mark ≠ Direxion SOXS NAV (funding, index, hours)
4. Residual 16% of SOXL vol is not zero — gap / weekend risk remains
5. Some SOXS days have thin prints (Vision ZIP <1MB) — slippage unmodeled
6. Correlation can break in halt / corporate-action / delist events

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** N/A (diagnostic)
