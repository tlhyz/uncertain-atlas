# Review Log — P2-02 BTC leverage scan (in progress)

**Date (UTC):** 2026-09-13T02:27Z  
**Task:** P2-02 (in_progress)  
**Verdict:** IN_PROGRESS — runner fixes applied; scan running

---

## Blockers fixed

| Issue | Fix |
|-------|-----|
| Missing BTC klines cache for C1 window | Fetched `binance_futures_BTCUSDT_1h_2024-09-01_2024-11-30_klines.csv` (2184 bars) |
| `KeyError: ETH` on BTC-only run | `portfolio.py` — dynamic `crypto_symbols` from dataset |
| SOXL tick error with `tech_disabled` | Skip tech leg fill loop when `tech_disabled=True` |
| `trades_lazy=False` despite aggTrades cache | `load_binance_market` — detect cache files under `cache_only` |

## Config

`configs/experiments/crypto_btc_leverage_scan.yaml` — BTC-only, leverage [1.25, 1.5, 1.75, 2.0], tick-precise, C1 window.

## Job

tmux `p2-02-btc-leverage` — started after fixes; 4 leverage levels on 2184 bars BTC aggTrades.

## P1-11

65d Tech tick backtest still running separately (~45 min at checkpoint).

## Tests

126 passed after portfolio/data fixes.

## Next

Wait for `outputs/experiments/crypto_btc_leverage_scan/CRYPTO_REPORT.md` → rank leverage → mark P2-02 done.
