# Investment Thesis (Working Hypotheses — Not Facts)

## Two independent books

### Book A — Tech / Semiconductor (`SOXL`, `SNXX`, watch `AAOI`)

**Subjective view:** sector may **pull back → high-vol base → strong uptrend**.

**Strategy shape (hypothesis):**

```
SHORT (tactical) → REDUCE SHORT → LONG GRID → GRID + TREND → TREND LONG
```

- Short is **tactical**, not the main edge hypothesis.
- Main expected PnL: **post-drawdown long / trend**, not permanent short.
- SOXL/SNXX are **already leveraged ETPs** → perp leverage must stay **conservative** (see `configs/risk.yaml`).

### Book B — Crypto (`BTC`, `ETH`, `SOL`; satellite `PENGU`, `PUMP`)

**Subjective view:** crypto can move **independently** of semis.

**Hard rule:** Crypto **must not** read SOXL/SNXX state as direction input.

Tech drawdown + Crypto uptrend → Crypto may still go **long / grid / trend long**.

---

## Capital framework (config, not code)

Default **10,000 USDT** research account — see `configs/portfolio.yaml`:

| Pool | USDT |
|------|------|
| TECH_BOOK | 6500 |
| CRYPTO_BOOK | 2500 |
| GLOBAL_RESERVE | 1000 |

Reserve is **not** unlimited rescue capital.

---

## Success criteria (what “winning” means)

Rank strategies by:

1. **TOTAL EQUITY** (not grid realized alone)
2. **Max drawdown**
3. **Liquidation / min buffer**
4. **OOS + robustness** (walk-forward, plateau, Monte Carlo)

If Short→Long loses to **Cash→Long**, Short must be **removed** from baseline — even if narrative feels right.

---

## Venue roles

| Venue | Role |
|-------|------|
| **Binance** | Long-history **structure research** (official aggTrades) |
| **Gate** | **Execution calibration** + OOS (fees, funding, fills) |

Never claim Binance fills equal Gate fills. Limit/maker-first structure can transfer; calibration required.
