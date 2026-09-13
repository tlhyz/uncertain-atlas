# Review Log — P2-07 grid mix runner + scan started

**Date (UTC):** 2026-09-13T05:40Z  
**Task:** P2-07 (in_progress)  
**Verdict:** IN_PROGRESS — runner extended; scan restarted after YAML fix

---

## Code changes

Added to `qtb/dual/crypto_run.py`:

- `_rank_crypto_grid_mix()` with per-mix progress logging
- `run_grid_mix_scan` + `grid_mix_scan` config keys
- Report section **Grid→Trend mix rank**
- Test `test_run_crypto_grid_mix_scan` — **127 tests pass**

---

## YAML pitfall (fixed)

Unquoted `80_20` in YAML parses as integer **8020**. Config uses quoted strings: `"80_20"`, etc.

First P2-07 start used wrong mix keys; killed and restarted 05:41Z.

---

## Config

`configs/experiments/crypto_btc_grid_mix_scan.yaml` — BTC C1, mixes 80_20→20_80 + dynamic.

tmux `p2-07-btc-grid-mix` — 6 variants.

---

## Checkpoint (05:40Z)

| Task | Progress |
|------|----------|
| P2-02 BTC lev | ~177 min, still running |
| P2-03 ETH lev | 1.25x done **-87.86%**; 1.5x running (~49 min total) |
| P2-04 SOL lev | 1.25x–1.75x all **-88.01%**; 2.0x running |
| P2-05 grid step | ~29 min |
| P2-06 grid range | ~10 min |

SOL/ETH catastrophic returns — await full reports + liquidation counts before ledger updates.

---

## Interim results (0920Z)

| Mix | Return | Calmar | Status |
|-----|--------|--------|--------|
| 80_20 | -87.35% | -17.18 | done |
| 60_40 | -87.97% | -18.56 | done |
| 50_50 | **-88.43%** | -15.70 | done |
| 40_60 | **-88.12%** | -60.50 | done |
| 20_80 | — | — | running |
| dynamic | — | — | pending |

**Pattern:** All completed mixes ~-87 to -88% — FAIL expected at scan end.
| 40_60 | — | — | pending |
| 20_80 | — | — | pending |
| dynamic | — | — | pending |

**Pattern:** All completed mixes in ~-87% band — no mix rescues C1 crypto FSM. Expect FAIL verdict when scan completes.

## Next

P2-07 report when 6 mixes complete → mark **done** (likely FAIL).
