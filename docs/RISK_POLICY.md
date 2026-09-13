# Risk Policy

All limits in `configs/risk.yaml` and `configs/portfolio.yaml` — **not hardcoded in strategies**.

## Drawdown

- Soft (−10/−12/−15%): reduce new risk, satellite, raise cash
- Hard (−18/−20/−25%): stop adding risk; close high-beta experiments
- **Never** increase leverage to recover losses

## Funding stress

Rolling 7d net funding cost vs book equity — de-leverage thresholds 1.0 / 1.5 / 2.0%.

## Liquidation

Simulate maintenance margin; report **minimum liquidation buffer**, not just binary liq flag.

## Portfolio leverage caps

- Baseline account contract leverage ≤ **1.5x**
- Hard cap ≤ **2.0x**
- Tech: remember **leveraged-on-leveraged** (SOXL/SNXX ETP × perp)

## Meme satellite

PENGU + PUMP combined ≤ **5%** account.

## Reserve

70/30 margin/reserve baseline scan. Reserve exhaustion = **system failure state**.
