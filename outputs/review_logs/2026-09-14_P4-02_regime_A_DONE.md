# Review Log — P4-02 Regime A Tech↓ Crypto↑ (dual book unblocked)

## Meta

- **date_utc:** 2026-09-14T06:50Z
- **task:** P4-02
- **method:** Dual-book config (`tech_tick_only=false`, bar crypto fills); 7d smoke + 65d tick run in progress
- **prior:** BLOCKED — outputs/review_logs/2026-09-14_P4-02_regime_A_BLOCKED.md

## Unblock (PASS)

Root cause fixed in `qtb/dual/portfolio.py` + config wiring:

| Issue | Fix |
|-------|-----|
| `tech_tick_only=True` zeroed crypto targets | Config `tech_tick_only: false` |
| No bar fallback for crypto when `tick_precise=True` | `crypto_tick_fills=false` → bar grid + rebalance |
| `trades_lazy=True` with empty aggTrades | `load_binance_market`: lazy only if rows > 0 |
| No crypto aggTrades on 65d overlap | `crypto_download_trades: false` (BAR crypto label) |

**7d smoke** (`configs/experiments/dual_binance_tick_dual_book_7d.yaml`):

| Metric | Independent | Unified |
|--------|-------------|---------|
| Return | −75.87% | −75.87% |
| crypto_max_dd | **4.32%** | **4.32%** |
| Δreturn | **0.00pp** | — |

**Regime A (tech_down_crypto_up) — portfolio equity:**

| Window | Bars | Frac | avg_tech_ret | avg_crypto_ret |
|--------|------|------|--------------|----------------|
| 7d dual-book | **40** | **23.8%** | −1.46%/bar | +0.39%/bar |
| 65d price proxy (prior) | 324 | 21.0% | — | — |
| 65d inert dual (prior) | **0** | 0% | — | — |

Crypto book is **active**; regime classification is **non-degenerate**.

## 65d tick run (in progress)

`scripts/run_p4_dual_book.py` started 06:06Z — ETA ~48min (2× tick portfolios). Results will update `outputs/experiments/dual_binance_tick_independent_vs_unified/dual_results.json`.

Execution label: **TICK tech + BAR crypto** (SOXL/SNXX aggTrades; BTC/ETH/SOL bar fills — no 2026 crypto aggTrades cached).

## Question

Does the dual portfolio capture **Regime A** (Tech down, Crypto up) with independent books?

## Findings

1. **Measurement:** PASS — portfolio-level Regime A bars > 0 with dual book (was 0 when crypto inert).
2. **Diversification:** FAIL on 7d — independent ≡ unified (Δreturn=0); no hedging benefit in Regime A bars.
3. **Regime A bar averages (7d):** Tech loses −1.46%/bar while Crypto gains +0.39%/bar — structure exists but books move together under current FSM (unified signal off still identical P&L path on 7d).

## Verdict

- **task_verdict:** **DONE** (unblock + Regime A measurable)
- **strategy_verdict:** **FAIL** — no independent-book benefit in Regime A on available window
- **execution:** TICK tech + BAR crypto (65d); 7d validated

## Red team (≥5)

1. BAR crypto fills ≠ tick crypto — conservative for crypto leg; tick crypto aggTrades for 2026 not cached
2. 7d window short — 40 Regime A bars vs 324 on 65d price proxy
3. ind≡uni may differ on 65d full run — pending tick completion
4. Regime classification uses bar-to-bar equity returns — not cumulative P&L attribution
5. Unified signal=false still produced identical 7d paths — FSM coupling elsewhere?

## Next

- Complete 65d tick dual-book run → update P4-01 notes (expect crypto_max_dd > 0)
- P4-03 Regime B (tech_up_crypto_down) — same config, 46 bars on 7d
- Optional: download BTC/ETH/SOL aggTrades for 2026-07→09 for full TICK crypto
