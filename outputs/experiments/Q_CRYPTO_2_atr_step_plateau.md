# Q-crypto-2 — Is 0.40 ATR step on a parameter plateau?

**Status:** PARTIAL (2026-09-13T06:20Z)  
**Window:** C1 2024-09-01 → 2024-11-30, BTC-only grid step sweep (P2-05)  
**Sweep:** steps [0.30, 0.40, 0.50, 0.60], range fixed ±5 ATR, lev 1.5

---

## Question

Is **0.40 ATR** grid spacing near a stable optimum (plateau), or a sharp peak?

Prior claim W-02 in `docs/CURRENT_CONCLUSIONS.md` — **LOW confidence**, not verified by executed sweep.

---

## Status

**P2-05 running** (~69 min at 06:20Z). No `CRYPTO_REPORT.md` yet.

Default `CryptoParams.grid_atr_step = 0.40` — center of sweep band.

---

## Interim (no measurements yet)

Cannot confirm or deny plateau until P2-05 `grid_rank` payload arrives.

**Pre-registration criteria for plateau (P5-style):**

- Top-3 steps by Calmar within **≤10%** return of best
- 0.40 in top-3 by Calmar on Base fill
- Conservative fill does not invert ranking

---

## Remaining work

- [ ] P2-05 complete → read `crypto_results.json` grid_rank
- [ ] Run plateau check (manual or `qtb/optimize` if available)
- [ ] Mark P2-11 **done** with PASS/FAIL verdict

---

## Related

- Config: `configs/experiments/crypto_btc_grid_atr_step.yaml`
- P2-06 range sweep (±3/5/7) also running — separate question (Q-crypto-3)
