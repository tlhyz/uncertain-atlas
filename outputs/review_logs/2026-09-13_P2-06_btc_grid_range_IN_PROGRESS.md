# Review Log — P2-06 BTC grid ATR range sweep started

**Date (UTC):** 2026-09-13T05:30Z  
**Task:** P2-06 (in_progress)  
**Verdict:** IN_PROGRESS — range scan running

---

## Config

`configs/experiments/crypto_btc_grid_atr_range.yaml`

| Param | Value |
|-------|-------|
| Symbol | BTC |
| Window | C1 2024-09-01 → 2024-11-30 |
| Leverage | 1.5 |
| Grid step | 0.40 ATR (fixed) |
| Range sweep | ±3, ±5, ±7 ATR |

tmux `p2-06-btc-grid-range` — log: `[run] crypto grid scan steps=[0.4] ranges=[3.0, 5.0, 7.0]...`

---

## Parallel checkpoint (05:30Z)

| Task | Elapsed | Progress |
|------|---------|----------|
| P2-02 BTC lev | ~167 min | still running (old process, no per-level logs) |
| P2-03 ETH lev | ~39 min | 1.25x still running (~2× SOL per-level time — larger tick cache) |
| P2-04 SOL lev | ~39 min | 1.25x/1.5x done -88.01% each; 1.75x running |
| P2-05 grid step | ~19 min | first grid variant in progress |

---

## SOL interim red-flag

Identical **-88.01%** return at 1.25x and 1.5x suggests wallet wipe / liquidation floor rather than leverage sensitivity. Hold final verdict until `CRYPTO_REPORT.md` + conservative fill + `liquidation_count` in payload.

---

## Tests

126 passed.

---

## Next

Await P2-02 CRYPTO_REPORT → mark done → Q-crypto-1 partial. P2-05/P2-06 reports when grid scans complete.
