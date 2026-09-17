# P7-16 — flatten hedge 2x / 3x TICK full listing

Verdict: **3x STOPPED** (same as 5x). **2x survived this 120d path** — CONDITIONAL,
**not live**.

Question: user may change leverage. Does 2x/3x avoid the 05-26 short liq?

## Results (tick, ±20U, 200, 5k+5k, flatten_survivor, 2026-05-15→09-11)

| Lev | Fee | Return | Pair DD | Stop | Notes |
|-----|-----|--------|---------|------|-------|
| 5x | base | +39.3% | −11.3% | **05-26** short | P7-15; 10 win / 110 idle |
| 3x | base | +28.8% | −6.9% | **05-27** short | 11 win days then cash |
| **2x** | base | **+70.7%** | −15.3% | **no** | 69 / 51 / 0 |
| 2x | conservative 4bps | +64.7% | −14.0% | **no** | fee does not flip |

SOXL buy-and-hold (daily last close): **−24.4%** (165.69 → 122.3). Asset DD **−69%**
(high 297.9 → low 92.4).

JSON: `outputs/experiments/p7_16_leverage_tick/compare.json`.

## Why +70% is not a deploy (red team)

1. **Not the user’s 5x.** 3x still dies. The “works” knob is a different product.
2. End state is not hedged: `inventory_frac` **1.81**, net **−43** SOXL. Short
   notional 11.7k on 5k = 2.33× inventory. Short leg DD **−71%**; long **−62%**.
   Pair DD −15% hides one-sided ruin.
3. One listing path. No second window, no funding, no Gate fill.
4. July 24 −1097 U / July 30 +1915 U — still a violent book. 5x died here as long.
5. Conservative still +65% — fee is not the story; inventory is.
6. A further rally from 122 with a −71% short DD can liquidate 2x next.
7. How this could be fake: MMR 0.5% kinder than venue; no funding on ~10k
   notional × 120d; remap lots after 55 reanchors may understate gap risk.

**Do not quote +70% as the 5x grid.** Do not promote 2x to MEDIUM.

## What is actually new

On this tape, flatten_survivor **first-liq death is leverage-sensitive**:
5x and 3x die in May; 2x stays on through the July event that killed 5x in P7-07.
That is a parameter fact, not an edge certificate.
