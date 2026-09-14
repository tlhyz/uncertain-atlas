# Review Log — P4-02 Regime A Tech↓ Crypto↑

## Meta

- **date_utc:** 2026-09-14T05:50Z
- **task:** P4-02
- **method:** Regime classification on 65d overlap; P4-01 portfolio equity + SOXL/BTC price proxy

## Question

Does the dual portfolio capture **Regime A** (Tech down, Crypto up) with independent books?

## Findings

### Portfolio equity (P4-01 dual run)

`regime_cross_stats(tech_equity, crypto_equity)` on measured dual:

| Regime | Bars | Frac |
|--------|------|------|
| tech_down_crypto_up | **0** | 0.0 |
| tech_up_crypto_down | 0 | 0.0 |
| both_up / both_down | 0 | 0.0 |

**Cause:** `crypto_max_dd=0` — crypto book equity **flat/inert** on dual engine 65d runs (no crypto FSM P&L). Regime classification on portfolio equity is **degenerate**.

### Price proxy (SOXL close vs BTC close)

Market structure **does** exhibit Regime A on same 1546 bars:

| Regime | Bars | Frac |
|--------|------|------|
| **tech_down_crypto_up** | **324** | **21.0%** |
| tech_up_crypto_down | 322 | 20.8% |
| both_up | 453 | 29.3% |
| both_down | 435 | 28.1% |

Regime A **exists in the market** but is **not testable** on dual portfolio P&L until crypto book trades.

## Verdict

- **task_verdict:** **BLOCKED**
- **reason:** Dual crypto book inactive on 65d overlap; portfolio-level regime stats all zero
- **unblock:** Enable crypto FSM trading in dual `run_dual_portfolio` OR run combined Tech+Crypto tick backtest with active crypto legs

## Red team (≥5)

1. Price proxy ≠ portfolio capture — only shows opportunity exists
2. SOXL/BTC may not match Tech book / Crypto book symbols exactly
3. 21% Regime A bars still need P&L attribution test
4. P2-14 C1 had active crypto — different config path
5. Gate dual may have active crypto — Binance dual path may be bug/config gap

## Next

- Audit why crypto legs flat in `run_dual_portfolio` (implementation)
- P4-03…F blocked same root cause until crypto active
- Consider P2 crypto-only regime analysis on overlapping dates as partial evidence
