# Review Log — P2-03 ETH leverage scan FAIL (data gap) + fix + restart

**Date (UTC):** 2026-09-13T04:50Z  
**Task:** P2-03  
**Verdict:** FAIL (first attempt) → fix applied → **restarted in_progress**

---

## Failure

```
RuntimeError: tick_precise: no aggTrades in bar 2024-09-04 17:00:00+00:00 for ETH — refuse bar approximation
```

First run (tmux `p2-03-eth-leverage`, started 04:40Z) crashed on leverage 1.25x.

---

## Root cause

`cache/binance_futures_ETHUSDT_aggTrades_2024-09-04.csv` was **truncated**:

| Check | Bad file | Fixed file |
|-------|----------|------------|
| Rows | 1,112,327 | 1,347,154 |
| Last trade | 2024-09-04 **16:28:21** | 2024-09-04 **23:59:59** |
| meta.json | missing | present |

Same class of gap as prior BTC Sep-01 / SOL Sep-04 fixes (P1-01).

---

## Fix

```python
fetch_agg_trades_day('ETHUSDT', date(2024,9,4), force_refresh=True)
```

Re-downloaded from Binance Vision (~7s). P2-03 restarted 04:51Z; leverage 1.25x running with per-level logging.

---

## Tests

`python3 -m pytest -q` → **126 passed**.

---

## Red team

1. Other ETH days may be truncated — spot-check before marking P2-03 done  
2. `--cache-only` download script cannot repair missing files (returns empty)  
3. Manifest row counts may not catch intra-day truncation  
4. C1 window single-regime risk unchanged  
5. P2-02 still on old code path without per-level prints — harder to monitor

---

## Next

Await `outputs/experiments/crypto_eth_leverage_scan/CRYPTO_REPORT.md` → PASS review → mark P2-03 done.
