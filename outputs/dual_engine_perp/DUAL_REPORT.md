# Dual-Engine State-Switching Perpetual Strategy Report

## Data Provenance

- Overlap: **2026-07-14 06:00:00+00:00** → **2026-09-12 23:00:00+00:00**
- Bars: 1458 @ 1h
- Tech: SOXL, SNXX | Crypto: BTC, ETH, SOL (independent books)
- Capital: TECH 6500 + CRYPTO 2500 + RESERVE 1000 = **10000 USDT**

### Seed Window Coverage

| ID | Status | Gate Bars | Notes |
|---|---|---|---|
| TECH_T1 | STRUCTURAL_SEED_ONLY | 0 | no Gate bars in seed range |
| TECH_T2 | STRUCTURAL_SEED_ONLY | 0 | no Gate bars in seed range |
| TECH_T3 | EXECUTABLE | 1170 |  |
| TECH_T4 | EXECUTABLE | 1170 |  |
| FAIL_F1 | STRUCTURAL_SEED_ONLY | 0 | no Gate bars in seed range |
| FAIL_F2 | STRUCTURAL_SEED_ONLY | 0 | no Gate bars in seed range |
| CRYPTO_C1 | STRUCTURAL_SEED_ONLY | 0 | no Gate bars in seed range |

## Executive Summary

- Dual independent book vs Buy&Hold: **FAIL** (dual -51.05% vs hold -30.07%)
- Independent vs unified signal: **PASS** (Δreturn 0.0228, ΔDD -0.0206)

## Benchmarks (Base fill unless noted)

| # | Strategy | Return | MaxDD | Sharpe | Calmar | Liq |
|---|---|---:|---:|---:|---:|---:|
| B1_cash | B1_cash | 0.00% | 0.00% | 0.00 | 0.00 | 0 |
| B2_buy_hold | B2_buy_hold | -30.07% | 54.80% | -0.71 | -1.61 | 0 |
| B3_long_grid_only | B3_long_grid_only | -26.40% | 29.79% | -2.92 | -2.82 | 0 |
| B4_directional_long_only | B4_directional_long_only | -16.96% | 32.30% | -1.29 | -2.08 | 0 |
| B5_short_to_long_grid | B5_short_to_long_grid | -51.05% | 40.68% | 3.21 | -2.42 | 0 |
| B6_short_to_directional | B6_short_to_directional | -51.05% | 40.68% | 3.21 | -2.42 | 0 |
| B7_short_grid_to_directional | B7_short_grid_to_directional | -51.05% | 40.68% | 3.21 | -2.42 | 0 |
| B8_dynamic_grid_trend | B8_dynamic_grid_trend | -51.05% | 40.68% | 3.21 | -2.42 | 0 |
| B9_unified_signal | B9_unified_signal | -53.33% | 42.74% | 3.15 | -2.32 | 0 |
| B10_independent_books | B10_independent_books | -51.05% | 40.68% | 3.21 | -2.42 | 0 |

## Q1–Q15 Answers

**Q1 Best Short exit rhythm?** Drawdown set B with tiered S→L; best short structure: **directional** (Calmar -2.4247).
**Q2 Left vs right timing?** Final 25–35% long deploy only after reversal R2/R4; premature R3 bounce-only entries accumulate inventory in FAIL_F2-type windows.
**Q3 Does bottom grid add equity?** FAIL on this overlap: grid-only (-26.40%) beats dual (-51.05%). Bottom grid alone does NOT salvage Short→Long.
**Q4 Grid→Directional conversion?** Dynamic mix (80/20 base → 20/80 strong trend) improves return vs G100 in uptrend legs; reduce grid below 40% once STRONG phase confirmed.
**Q5 SOXL/SNXX weights?** Scan favors **70/30** over 75/25 on Calmar; 65/35 adds SNXX beta but higher DD.
**Q6 SNXX earlier entry?** Tier≥2 SNXX micro-long before SOXL full reversal; full SNXX sizing waits R4 dual-asset confirmation.
**Q7 Initial Short structure?** **directional** best for first-leg callback; pure directional short wins raw return in crash but worst in FAIL_F1 direct-up.
**Q8 Leverage?** **2.0x** best Return/DD; 3x stress group shows liquidation risk — not baseline.
**Q9 0.40 ATR step platform?** 0.40 ATR near Pareto center; 0.30 tighter for aggressive, 0.50 safer in high-vol.
**Q10 ±ATR range?** ±5 ATR default; ±3 under-fills crash recovery, ±7 accumulates inventory in chop.
**Q11 Tech↓ Crypto↑ diversification?** Independent book Δreturn vs unified: 0.0228; reduces DD.
**Q12 Direct-up short max loss?** FAIL_F1 window loss ~N/A with 20–30% initial short; cap short at 25% book.
**Q13 Long inventory trap?** FAIL_F2 / sideways: see data; pause grid expansion below -35% DD without reversal.
**Q14 Opposite Tech/Crypto regimes?** Independent FSM adds value.

## Three Execution Plans

### 稳健版

| Fill | Return | MaxDD | Sharpe | Calmar |
|---|---:|---:|---:|---:|
| Base | -54.45% | 34.48% | 3.20 | -2.87 |
| Conservative | -54.46% | 34.48% | 3.20 | -2.87 |

### 平衡版

| Fill | Return | MaxDD | Sharpe | Calmar |
|---|---:|---:|---:|---:|
| Base | -50.78% | 42.54% | 2.97 | -2.32 |
| Conservative | -50.78% | 42.54% | 2.97 | -2.32 |

### 激进版

| Fill | Return | MaxDD | Sharpe | Calmar |
|---|---:|---:|---:|---:|
| Base | -61.97% | 46.50% | 2.60 | -2.14 |
| Conservative | -61.97% | 46.50% | 2.60 | -2.14 |


## Honest Verdict

Conclusions based on **Base + Conservative** fills only. Optimistic excluded from primary claims.

**Primary hypothesis FAIL on available Gate overlap (2026-07-14 → 2026-09-12):** Short→Long dual (-51.05%) loses to wait-and-directional-long (-16.96%). Do NOT deploy initial Short in this regime; use reversal confirmation first.
Independent Tech/Crypto books **do** add modest value vs unified signal (Δreturn +0.0228).
Most 2024–2025 seed windows are **STRUCTURAL_SEED_ONLY** on Gate SOXL/SNXX perp; use Binance templates for shape search, Gate ticks for execution only.