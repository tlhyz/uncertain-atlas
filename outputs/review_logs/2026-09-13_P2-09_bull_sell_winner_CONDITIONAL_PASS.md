# Review Log — P2-09 Bull trend sell-the-winner check

**Date (UTC):** 2026-09-13T06:00Z  
**Task:** P2-09  
**Verdict:** **CONDITIONAL PASS** (structural OK; C1 backtest blocked)

---

## Structural check (PASS)

Added `test_bull_dynamic_sell_the_winner_mix` in `tests/test_dual_engine.py`:

- `CryptoParams(grid_mix="dynamic")` in **BULL** regime uses `grid_mix_fractions("dynamic", "strong")` → **20% grid / 80% directional**
- Verified `long_dir_frac > long_grid_frac` (ratio 4.0 at lev 1.5, util 0.65)

This implements STRATEGY_CRYPTO §Grid→Trend sell-the-winner wiring.

---

## C1 execution backtest (BLOCKED)

P2-08 regime sample on C1 (2024-09→11):

| Symbol | BULL bars |
|--------|-----------|
| BTC | **0** |
| ETH | **0** |
| SOL | **0** |

Cannot measure tick-PnL impact of bull sell-the-winner on current C1 window — no BULL classifications.

---

## Recommendation

- Defer PnL test to window with BULL bars (extend klines download beyond C1, or P2-14)
- P2-07 grid_mix scan (running) will compare static mixes including `dynamic` on C1

---

## Tests

128 passed (+1).

---

## Next

P2-10 Q-crypto-1 partial answer when P2-02/P2-03 complete.
