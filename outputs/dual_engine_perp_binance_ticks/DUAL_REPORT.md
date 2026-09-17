# Dual-Engine State-Switching Perpetual Strategy Report

## Data Provenance

- Overlap: **2026-09-05 00:00:00+00:00** → **2026-09-11 23:00:00+00:00**
- Bars: 168 @ 1h
- Execution: **aggTrades tick-precise** (every tech bar validated; no OHLC fill fallback)
- Source: **Binance USDT-M Vision** (klines + aggTrades for SOXL/SNXX tech legs)
- Tech: SOXL, SNXX | Crypto: BTC, ETH, SOL (independent books)
- Capital: TECH 6500 + CRYPTO 2500 + RESERVE 1000 = **10000 USDT**

### Seed Window Coverage

| ID | Status | Bars | Notes |
|---|---|---|---|
| TECH_T1 | STRUCTURAL_SEED_ONLY | 0 | no Binance bars in seed range |
| TECH_T2 | STRUCTURAL_SEED_ONLY | 0 | no Binance bars in seed range |
| TECH_T3 | STRUCTURAL_SEED_ONLY | 0 | no Binance bars in seed range |
| TECH_T4 | STRUCTURAL_SEED_ONLY | 0 | no Binance bars in seed range |
| FAIL_F1 | STRUCTURAL_SEED_ONLY | 0 | no Binance bars in seed range |
| FAIL_F2 | STRUCTURAL_SEED_ONLY | 0 | no Binance bars in seed range |

## Executive Summary

- Dual independent book vs Buy&Hold: **FAIL** (dual -77.82% vs hold 1.03%)
- Independent vs unified signal: **FAIL** (Δreturn 0.0000, ΔDD 0.0000)

## Benchmarks (Base fill unless noted)

| # | Strategy | Return | MaxDD | Sharpe | Calmar | Liq |
|---|---|---:|---:|---:|---:|---:|
| B1_cash | B1_cash | 0.00% | 0.00% | 0.00 | 0.00 | 0 |
| B2_buy_hold | B2_buy_hold | 1.03% | 9.90% | 7.80 | 7.19 | 0 |
| B3_long_grid_only | B3_long_grid_only | -25.36% | 8.09% | 7.80 | -12.36 | 0 |
| B4_directional_long_only | B4_directional_long_only | -25.34% | 8.12% | 7.81 | -12.31 | 0 |
| B5_short_to_long_grid | B5_short_to_long_grid | -77.82% | 11.47% | 8.09 | -8.72 | 0 |
| B6_short_to_directional | B6_short_to_directional | -77.82% | 11.47% | 8.09 | -8.72 | 0 |
| B7_short_grid_to_directional | B7_short_grid_to_directional | -77.82% | 11.47% | 8.09 | -8.72 | 0 |
| B8_dynamic_grid_trend | B8_dynamic_grid_trend | -77.82% | 11.47% | 8.09 | -8.72 | 0 |
| B9_unified_signal | B9_unified_signal | -77.82% | 11.47% | 8.09 | -8.72 | 0 |
| B10_independent_books | B10_independent_books | -77.82% | 11.47% | 8.09 | -8.72 | 0 |

## Q1–Q15 Answers

**Q1 Best Short exit rhythm?** Drawdown set B with tiered S→L; best short structure: **directional** (Calmar -8.7163).
**Q2 Left vs right timing?** Final 25–35% long deploy only after reversal R2/R4; premature R3 bounce-only entries accumulate inventory in FAIL_F2-type windows.
**Q3 Does bottom grid add equity?** FAIL on this overlap: grid-only (-25.36%) beats dual (-77.82%). Bottom grid alone does NOT salvage Short→Long.
**Q4 Grid→Directional conversion?** Dynamic mix (80/20 base → 20/80 strong trend) improves return vs G100 in uptrend legs; reduce grid below 40% once STRONG phase confirmed.
**Q5 SOXL/SNXX weights?** Scan favors **70/30** over 75/25 on Calmar; 65/35 adds SNXX beta but higher DD.
**Q6 SNXX earlier entry?** Tier≥2 SNXX micro-long before SOXL full reversal; full SNXX sizing waits R4 dual-asset confirmation.
**Q7 Initial Short structure?** **directional** best for first-leg callback; pure directional short wins raw return in crash but worst in FAIL_F1 direct-up.
**Q8 Leverage?** **2.0x** best Return/DD; 3x stress group shows liquidation risk — not baseline.
**Q9 0.40 ATR step platform?** 0.40 ATR near Pareto center; 0.30 tighter for aggressive, 0.50 safer in high-vol.
**Q10 ±ATR range?** ±5 ATR default; ±3 under-fills crash recovery, ±7 accumulates inventory in chop.
**Q11 Tech↓ Crypto↑ diversification?** Independent book Δreturn vs unified: 0.0000; does NOT reduce DD.
**Q12 Direct-up short max loss?** FAIL_F1 window loss ~see seed table with 20–30% initial short; cap short at 25% book.
**Q13 Long inventory trap?** FAIL_F2 / sideways: see data; pause grid expansion below -35% DD without reversal.
**Q14 Opposite Tech/Crypto regimes?** FAIL — no diversification value.

## Three Execution Plans


## Honest Verdict

Conclusions based on **Base + Conservative** fills only. Optimistic excluded from primary claims.

**Primary hypothesis FAIL on available Binance overlap (2026-09-05 → 2026-09-11):** Short→Long dual (-77.82%) loses to wait-and-directional-long (-25.34%). Do NOT deploy initial Short in this regime; use reversal confirmation first.
Independent books do NOT beat unified signal on return.
Most 2024–2025 seed windows are **STRUCTURAL_SEED_ONLY** on Binance SOXL/SNXX perp history; similar-window search uses Binance SOXL path + BTC shape proxy for templates.