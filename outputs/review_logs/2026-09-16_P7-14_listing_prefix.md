# P7-14 — listing-prefix window 2026-05-15→07-15 (new days)

Verdict: **CONDITIONAL** — BAR probe + 3-day tick smoke. **Not a hedge verdict.**

P7-07 only used 2026-07-16→09-11. Listing prefix 05-15→07-15 is on disk (P1-12)
and had never been run through the user 5x / 200 / flatten_survivor book.

## Runs

Same knobs as the user book: 5x isolated, 200 arithmetic, 5k+5k, flatten_survivor.

| Tag | Fills | Window | Return | Max DD | Stop | Liq |
|-----|-------|--------|--------|--------|------|-----|
| p714u | **BAR** | 05-15→07-15 (62d) | +37.6% | −6.6% | no | no |
| p714p | **BAR** | 05-15→07-15 | +26.1% | −7.7% | no | no |
| p714t | TICK | 05-15 (1d) | +2.14% | −1.4% | no | no |
| p714t3 | TICK | 05-15→05-17 (3d) | +2.10% | −1.4% | no | no |

JSON: `outputs/experiments/p7_14_listing_prefix/compare.json`.

## How the BAR number is fake (red team, ≥5)

1. **Wick fill** — P7-03 BAR +18.8% was overturned by P7-04 TICK. Same engine family.
2. 57,584 BAR fills vs 160 tick fills in 3 days: BAR is crossing rungs the tape never did.
3. Prefix BAR did not stop; P7-07 TICK on the *next* window stopped 07-28. Different path.
4. 3-day tick already has `inventory_frac` 1.26 and net −22 SOXL — drift started.
5. 3 days cannot speak for 62. One listing-day +2% is not harvest.
6. No funding. Isolated MMR 0.5% may be kinder than venue.

**Do not quote +37% / +26%.** Next: P7-15 full-prefix **TICK**.

## What is actually new

The prefix days exist, `--check` is clean (0 missing tick days), and the runner
accepts 2026-05-15. That is a data/engine fact, not an edge.
