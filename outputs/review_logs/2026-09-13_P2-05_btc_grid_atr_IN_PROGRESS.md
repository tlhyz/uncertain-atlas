# Review Log — P2-05 BTC grid ATR step sweep started

**Date (UTC):** 2026-09-13T05:10Z  
**Task:** P2-05 (in_progress)  
**Verdict:** IN_PROGRESS — grid scan running

---

## Config

`configs/experiments/crypto_btc_grid_atr_step.yaml`

| Param | Value |
|-------|-------|
| Symbol | BTC |
| Window | 2024-09-01 → 2024-11-30 (2184 bars) |
| Leverage | 1.5 (default, LEDGER-002) |
| Grid step sweep | 0.30, 0.40, 0.50, 0.60 |
| Grid range | ±5 ATR (fixed) |
| Fill | base, tick-precise |

---

## Job

tmux `p2-05-btc-grid-atr` — started 05:10Z; 4 step variants × 1 range.

Log: `[run] crypto grid scan steps=[0.3, 0.4, 0.5, 0.6] ranges=[5.0]...`

---

## Parallel load (6 jobs)

| tmux | Task | Note |
|------|------|------|
| p1-11-backtest | P1-11 | ~208 min |
| p2-02-btc-leverage | P2-02 | ~147 min, no per-level logs |
| p2-03-eth-leverage | P2-03 | ETH 1.25x ~19 min |
| p2-04-sol-leverage | P2-04 | SOL 1.25x done (-88.01%), 1.5x running |
| p2-05-btc-grid-atr | P2-05 | grid scan started |

---

## Interim SOL 1.25x (not final verdict)

Per-level log: **return=-88.01%, calmar=-2.52** — suspiciously bad; await full CRYPTO_REPORT + conservative fill before ledger update. Red-team: liquidation cascade, fill optimism, C1 bear window.

---

## Tests

`python3 -m pytest -q` → **126 passed**.

---

## Next

Await `outputs/experiments/crypto_btc_grid_atr_step/CRYPTO_REPORT.md` → PASS review → mark P2-05 done → partial Q-crypto-2.
