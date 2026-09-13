# Current Conclusions (Honest — 2026-09-13)

> Update after each major experiment. **Do not beautify FAIL results.**

## PROVEN / STRONG

| Claim | Evidence |
|-------|----------|
| 3L ETF long-run grid fails vs total equity | Exp 001, Gate real data |
| Majors prefer 1.5–2x PERP grid over 3L ETF grid | Exp 002, `outputs/ab_etf_vs_perp/` |
| 3x PERP not unattended-safe (SOL/PENGU/PUMP liq) | Exp 002 |
| Rebate alone does not fix wrong direction + inventory | Exp 002 |
| Tech Short→Long **FAIL** vs simpler baselines on Gate overlap | Exp 003, `outputs/dual_engine_perp/` |

## WEAK

| Claim | Evidence |
|-------|----------|
| Independent Crypto book may help vs unified Tech signal | +2.3% Δreturn one window |
| 0.40 ATR grid spacing near parameter plateau | Prior sweeps — **re-verify** on Binance ticks |

## UNTESTED

| Claim | Blocker |
|-------|---------|
| Binance tick-precise Tech FSM full matrix | Downloader + validation pipeline completing |
| Crypto multi-year decoupling C1 | Not re-run post-refactor |
| Gate OOS fill calibration vs Binance structure | STEP 6 |
| Monte Carlo survival at baseline params | STEP 9 |

## LIVE candidates

See `outputs/LIVE_CANDIDATES.md` — **no high-confidence deploy params yet.**

Baseline configs in `configs/portfolio.yaml` are **candidates only**, not approved live settings.
