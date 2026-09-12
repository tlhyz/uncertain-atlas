# Gate 3L ETF Spot Grid vs Underlying Perpetual Grid — A/B

This report is computed from **real Gate public data** on overlapping timestamps only.
Optimistic fills are not used in conclusions. Synthetic ETF ticks were not generated.

## Data limits (do not hide)

- Gate REST candlesticks cap: **10000 bars**.
- Primary interval: `1h` (covers 60–180d windows).
- Execution-sensitivity interval: `5m` (last ~35d).
- Historical **ticks / 1s** exist for hours, not for 3–180d. Conclusions use Base + Conservative bar fills.
- Historical ETF **NAV series is not published**. Snapshot NAV/premium is recorded; path-drag uses price vs theoretical 3x underlying.
- Perpetual mark/liquidation uses last-price OHLC plus contract `maintenance_rate`. Research-grade, not an exchange replica.
- Gate public funding history pages back ~180 days / ~1000 prints. Earlier overlap bars have funding=0 (not a synthetic average).

## Verdict by asset (no 'it depends' cop-out)

- **BTC**: PERP WIN — 首选 `PERP_1.5x` / 次选 `HYBRID` / 不推荐 `ETF`
- **ETH**: PERP WIN — 首选 `PERP_1.5x` / 次选 `PERP_3x` / 不推荐 `ETF`
- **SOL**: PERP WIN — 首选 `PERP_1.5x` / 次选 `ETF` / 不推荐 `PERP_3x`
- **PENGU**: ETF WIN — 首选 `ETF` / 次选 `HYBRID` / 不推荐 `PERP_3x`
- **PUMP**: ETF WIN — 首选 `ETF` / 次选 `HYBRID` / 不推荐 `PERP_1.5x`
- **SOXL**: PERP WIN — 首选 `PERP_1.5x` / 次选 `HYBRID` / 不推荐 `ETF`
- **SNXX**: PERP WIN — 首选 `PERP_3x` / 次选 `PERP_1.5x` / 不推荐 `ETF`
- **AAOI**: PERP WIN — 首选 `PERP_1.5x` / 次选 `PERP_3x` / 不推荐 `ETF`

## Answers to the required questions

**Q1 same 1000U, 3L ETF grid vs 3x perp grid — who has higher final equity?**  PERP. BTC: ETF 136.6 vs PERP3x 162.3 → PERP; ETH: ETF 48.4 vs PERP3x 86.0 → PERP; SOL: ETF 21.9 vs PERP3x 43.4 → PERP; PENGU: ETF 269.3 vs PERP3x 0.5 → ETF; PUMP: ETF 10.1 vs PERP3x 1.5 → ETF; SOXL: ETF 119.0 vs PERP3x 100.4 → ETF; SNXX: ETF 799.6 vs PERP3x 1971.1 → PERP; AAOI: ETF 948.7 vs PERP3x 1008.5 → PERP

**Q2 who has lower max DD?**  PERP (3-5). BTC ETF=0.923657 PERP=0.898025; ETH ETF=0.979677 PERP=0.943659; SOL ETF=0.987555 PERP=0.959161; PENGU ETF=0.988569 PERP=0.999667; PUMP ETF=0.995075 PERP=0.998975; SOXL ETF=0.947553 PERP=0.962761; SNXX ETF=0.719744 PERP=0.405624; AAOI ETF=0.15348 PERP=0.073487

**Q3 who keeps more net profit per 1M turnover?**  PERP (1-7). BTC ETF=-6140.2941 PERP=-996.1738; ETH ETF=-12055.2783 PERP=-1313.3606; SOL ETF=-14084.635 PERP=-7453.5081; PENGU ETF=-910.9587 PERP=-7343.5003; PUMP ETF=-12324.8185 PERP=-5953.457; SOXL ETF=-39361.3451 PERP=-9022.352; SNXX ETF=-7024.6353 PERP=7003.4322; AAOI ETF=-29039.3002 PERP=659.3

**Q4 how much edge did ETF path drag eat?**
- BTC: ETF -0.8733283176465167 vs theo3x -0.8190321968330275 drag=-0.054296120813489224 und=-0.3057054162932019
- ETH: ETF -0.9576360330116099 vs theo3x -0.9448982374069396 drag=-0.012737795604670366 und=-0.4167835918014491
- SOL: ETF -0.9821851606178338 vs theo3x -0.974101166063556 drag=-0.008083994554277774 und=-0.515504245778075
- PENGU: ETF -0.9184975640421182 vs theo3x -0.999614831977545 drag=0.08111726793542673 und=-0.7654779994180594
- PUMP: ETF 1.952844350121639 vs theo3x -0.9963716533809596 drag=2.9492160035025985 und=-0.02637249871728853
- SOXL: ETF -0.9776647857630062 vs theo3x -0.9869061301319256 drag=0.009241344368919435 und=-0.5147734996601498
- SNXX: ETF 1.0061148108450033 vs theo3x -0.24166103320573118 drag=1.2477758440507345 und=1.2394889318080518
- AAOI: ETF -0.08630381056382574 vs theo3x -0.08968917496800011 drag=0.0033853644041743625 und=-0.027356471573462215

**Q5 how much edge did perp funding eat?**
- BTC: net_funding=-17.516858 paid=20.327907 recv=2.81105 vs net_profit=-837.6577
- ETH: net_funding=-6.681471 paid=12.899319 recv=6.217848 vs net_profit=-914.0352
- SOL: net_funding=-3.877561 paid=4.35051 recv=0.472949 vs net_profit=-956.6215
- PENGU: net_funding=-8.765815 paid=9.904613 recv=1.138798 vs net_profit=-999.503
- PUMP: net_funding=-8.07666 paid=10.742768 recv=2.666108 vs net_profit=-998.4923
- SOXL: net_funding=0.0 paid=0.0 recv=0.0 vs net_profit=-899.5915
- SNXX: net_funding=-12.212745 paid=12.212745 recv=0.0 vs net_profit=971.1137
- AAOI: net_funding=0.0 paid=0.0 recv=0.0 vs net_profit=8.4839

**Q6 is perp liquidation risk worth lower path drag?**  NO — liquidation occurred on the 3x isolated book.

**Q7 rebate value-add (baseline vs 0%)**
- BTC: {'A2_etf_native_atr_d0.0_reb_base': 27.6378553967252, 'B_perp_3.0x_iso_P1_d0.0_reb_base': 34.05159705370082}
- ETH: {'A2_etf_native_atr_d0.0_reb_base': 7.382720300998869, 'B_perp_3.0x_iso_P1_d0.0_reb_base': 11.644258449668996}
- SOL: {'A2_etf_native_atr_d0.0_reb_base': 1.7086742422566843, 'B_perp_3.0x_iso_P1_d0.0_reb_base': 7.700707997975314}
- PENGU: {'A2_etf_native_atr_d0.0_reb_base': 28.605109470007847, 'B_perp_3.0x_iso_P1_d0.0_reb_base': -0.25656984232076496}
- PUMP: {'A2_etf_native_atr_d0.0_reb_base': 0.7139787753561819, 'B_perp_3.0x_iso_P1_d0.0_reb_base': 1.3746870938946323}
- SOXL: {'A2_etf_native_atr_d0.0_reb_base': 3.098962679942531, 'B_perp_3.0x_iso_P1_d0.0_reb_base': 3.87446639800244}
- SNXX: {'A2_etf_native_atr_d0.0_reb_base': 10.832080913279015, 'B_perp_3.0x_iso_P1_d0.0_reb_base': 8.319752653383148}
- AAOI: {'A2_etf_native_atr_d0.0_reb_base': 0.9763966558911079, 'B_perp_3.0x_iso_P1_d0.0_reb_base': 0.7720845514356824}

**Q8 if rebate is zero, does the winner flip?**  BTC: with-rebate PERP / zero-rebate PERP; ETH: with-rebate PERP / zero-rebate PERP; SOL: with-rebate PERP / zero-rebate PERP; PENGU: with-rebate ETF / zero-rebate ETF; PUMP: with-rebate ETF / zero-rebate ETF; SOXL: with-rebate ETF / zero-rebate ETF; SNXX: with-rebate PERP / zero-rebate PERP; AAOI: with-rebate PERP / zero-rebate PERP

**Q9 high-vol range (−5%..+5% und, high RV):**  ETF 2 vs PERP 5 over 7 windows → PERP

**Q10 one-way up (≥20%):**  ETF 8 vs PERP 20 over 28 windows → PERP

**Q11 crash (≤−15%):**  ETF 33 vs PERP 49 over 82 windows → PERP

**Q12 V-reversal:**  ETF 0 vs PERP 4 over 4 windows → PERP

**Q13 long-run unattended:**  PERP at 1.5x–2x (do not unattended-run 3x where it liquidated). Per-asset primaries ETF=2 PERP=6 HYBRID=0. Liquidated 3x books: ['SOL', 'PENGU', 'PUMP'].

**Q14 max turnover/rebate with controlled DD:**
- BTC: B_perp_3.0x_iso_P1_d0.0_reb_base turnover=840875.024714 DD=0.898025
- ETH: B_perp_2.0x_iso_P1_d0.0_reb_base turnover=685474.913449 DD=0.788104
- SOL: B_perp_1.5x_iso_P1_d0.0_reb_base turnover=349876.853201 DD=0.516137
- PENGU: A2_etf_native_atr_d0.0_reb_base turnover=802129.371534 DD=0.988569
- PUMP: A2_etf_native_atr_d0.0_reb_base turnover=80313.914858 DD=0.995075
- SOXL: B_perp_2.0x_iso_P1_d0.0_reb_base turnover=113586.320492 DD=0.830895
- SNXX: B_perp_3.0x_iso_P1_d0.0_reb_base turnover=138662.544223 DD=0.405624
- AAOI: B_perp_3.0x_iso_P1_d0.0_reb_base turnover=12868.075857 DD=0.073487

**Q15 portfolio risk-adjusted: Pure ETF vs Pure Perp vs Hybrid**
- pure_etf: final=11379.9573 ret=0.137996 DD=0.316014 sharpe=1.0987 score=0.346241 LIQ=False
- pure_perp: final=11878.2951 ret=0.18783 DD=0.192628 sharpe=1.7187 score=0.423534 LIQ=False
- hybrid_60_20_20: final=10883.6334 ret=0.088363 DD=0.234776 sharpe=1.1173 score=0.337988 LIQ=False
- hybrid_70_15_15: final=10907.7144 ret=0.090771 DD=0.258485 sharpe=1.1072 score=0.33163 LIQ=False
- **Portfolio winner: pure_perp**

## Three fairness lenses (must not be collapsed)

### same_wallet 3x
- BTC: ETF eq=136.6 score=-0.507 | PERP eq=162.3 score=-0.416 LIQ=False → **PERP**
- ETH: ETF eq=48.4 score=-0.532 | PERP eq=86.0 score=-0.454 LIQ=False → **PERP**
- SOL: ETF eq=21.9 score=-0.536 | PERP eq=43.4 score=-1.262 LIQ=True → **ETF**
- PENGU: ETF eq=269.3 score=-0.400 | PERP eq=0.5 score=-1.278 LIQ=True → **ETF**
- PUMP: ETF eq=10.1 score=-0.539 | PERP eq=1.5 score=-1.277 LIQ=True → **ETF**
- SOXL: ETF eq=119.0 score=-0.517 | PERP eq=100.4 score=-0.524 LIQ=False → **ETF**
- SNXX: ETF eq=799.6 score=-0.242 | PERP eq=1971.1 score=0.747 LIQ=False → **PERP**
- AAOI: ETF eq=948.7 score=0.097 | PERP eq=1008.5 score=0.383 LIQ=False → **PERP**
- Lens tally: ETF 4 / PERP 4 → **TIE**

### same_exposure
- BTC: ETF eq=136.6 score=-0.507 | PERP eq=114.9 score=-0.431 LIQ=False → **PERP**
- ETH: ETF eq=48.4 score=-0.532 | PERP eq=59.0 score=-0.465 LIQ=False → **PERP**
- SOL: ETF eq=21.9 score=-0.536 | PERP eq=57.7 score=-1.257 LIQ=True → **ETF**
- PENGU: ETF eq=269.3 score=-0.400 | PERP eq=0.1 score=-1.278 LIQ=True → **ETF**
- PUMP: ETF eq=10.1 score=-0.539 | PERP eq=0.1 score=-1.278 LIQ=True → **ETF**
- SOXL: ETF eq=119.0 score=-0.517 | PERP eq=139.1 score=-0.513 LIQ=False → **PERP**
- SNXX: ETF eq=799.6 score=-0.242 | PERP eq=1852.2 score=0.748 LIQ=False → **PERP**
- AAOI: ETF eq=948.7 score=0.097 | PERP eq=1007.3 score=0.385 LIQ=False → **PERP**
- Lens tally: ETF 3 / PERP 5 → **PERP**

### same_risk
- BTC: ETF eq=136.6 score=-0.507 | PERP eq=117.2 score=-0.430 LIQ=False → **PERP**
- ETH: ETF eq=48.4 score=-0.532 | PERP eq=56.0 score=-0.465 LIQ=False → **PERP**
- SOL: ETF eq=21.9 score=-0.536 | PERP eq=50.9 score=-1.260 LIQ=True → **ETF**
- PENGU: ETF eq=269.3 score=-0.400 | PERP eq=0.6 score=-1.278 LIQ=True → **ETF**
- PUMP: ETF eq=10.1 score=-0.539 | PERP eq=1.5 score=-1.278 LIQ=True → **ETF**
- SOXL: ETF eq=119.0 score=-0.517 | PERP eq=148.7 score=-0.510 LIQ=False → **PERP**
- SNXX: ETF eq=799.6 score=-0.242 | PERP eq=1841.3 score=0.748 LIQ=False → **PERP**
- AAOI: ETF eq=948.7 score=0.097 | PERP eq=1007.5 score=0.384 LIQ=False → **PERP**
- Lens tally: ETF 3 / PERP 5 → **PERP**

## PLAN A — ETF dominant

- Assets (primaries): ['PENGU', 'PUMP']
- Allocation (if A is chosen): majors 28/28, SOXL ≤24%, meme ≤8% each, rest cash.
- Grid: geometric native 0.40 ATR (use 0.30–0.50 plateau only if not flagged OVERFIT), range ±5 ATR, reanchor on range exit.
- Expected turnover / DD: see per-asset A2 native ATR base rows — do not invent a constant.

## PLAN B — PERP dominant

- Assets (primaries): ['BTC', 'ETH', 'SOL', 'SOXL', 'SNXX', 'AAOI']
- Leverage: start 1.5–2.0x wallet notional; 3x only if that pair's 3x score beat 1.5x and no liquidation.
- Margin: isolated P2 (70/30) unless P1 clearly won without approaching liq.
- Liquidation buffer trigger 15% (test 10/20 shown in rows). Funding: halt if rolling 7d net funding < −1.5% of equity.

## PLAN C — HYBRID

- Default book: ETF grid 60% / perp grid 20% / cash 20% (alt 70/15/15).
- ETF sleeve: SOL3L + ETH3L core; SOXL3L only inside its real overlap; meme ≤8%.
- Perp sleeve: same underlyings, **2x** wallet cap, isolated, 30% reserve.
- Use hybrid when single-mechanism scores split across regimes (see Q9–Q12).

Portfolio scores rank: [('pure_perp', 0.423534, 11878.2951), ('pure_etf', 0.346241, 11379.9573), ('hybrid_60_20_20', 0.337988, 10883.6334), ('hybrid_70_15_15', 0.33163, 10907.7144)]

## Per-asset detail

## BTC

- ETF `BTC3L_USDT` vs perp `BTC_USDT`
- Overlap **2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00** (9000 bars, `1h`)
- Funding source: `cache+funding` rows=1079
- Decision: **PERP WIN**  primary=PERP_1.5x  secondary=HYBRID  do-not-use=ETF

- ETF snapshot leverage=3.0045780254096215 NAV=1.65501786 premium=-0.0012192375978348213 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold -0.8733283176465167 vs theo 3x und -0.8190321968330275 → drag=-0.054296120813489224

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 123.4068 | -0.8766 | 0.9551 | -876816.75 | -2.6409 | -0.8288 | -1.1906 | -0.9105 | 999.7450 | 0.0000 | no | -0.5197 |
| B1_spot_hold | benchmark | 689.4466 | -0.3106 | 0.5374 | -310632.66 | -0.4226 | -0.5934 | -0.8318 | -0.5652 | 999.7450 | 0.0000 | no | -0.2293 |
| B2_spot_grid | benchmark | 648.3243 | -0.3517 | 0.5179 | -1079.99 | -0.9599 | -1.5217 | -1.6706 | -0.6646 | 325628.34 | 0.0000 | no | -0.2005 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 136.6109 | -0.8634 | 0.9237 | -6140.29 | -4.8460 | -1.9403 | -2.0076 | -0.9267 | 140610.38 | 0.0000 | no | -0.5073 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 108.9730 | -0.8910 | 0.9352 | -6735.96 | -5.3490 | -2.2016 | -2.2606 | -0.9457 | 132279.16 | 0.0000 | no | -0.5132 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 130.0089 | -0.8700 | 0.9409 | -12287.13 | -3.4111 | -1.3741 | -1.7131 | -0.9169 | 70805.06 | 0.0000 | no | -0.5144 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 449.8340 | -0.5502 | 0.6871 | -959.9134 | -1.8240 | -1.6700 | -1.5025 | -0.7866 | 573141.32 | -9.9534 | no | -0.3074 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 325.3614 | -0.6746 | 0.7832 | -974.3933 | -2.5341 | -1.7060 | -1.5757 | -0.8488 | 692367.84 | -12.8416 | no | -0.3604 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 235.3099 | -0.7647 | 0.8477 | -976.7206 | -3.2520 | -1.6104 | -1.5181 | -0.8912 | 782915.89 | -15.1998 | no | -0.3922 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 162.3423 | -0.8377 | 0.8980 | -996.1738 | -3.9752 | -1.5755 | -1.5237 | -0.9238 | 840875.02 | -17.5169 | no | -0.4165 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 128.2907 | -0.8717 | 0.9119 | -1090.89 | -4.3498 | -1.8381 | -1.7841 | -0.9481 | 799084.23 | -17.1489 | no | -0.4289 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 416.6471 | -0.5834 | 0.6496 | -989.9074 | -3.9361 | -1.9573 | -1.7825 | -0.8830 | 589300.41 | -12.2689 | no | -0.3019 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 162.3423 | -0.8377 | 0.8980 | -996.1738 | -3.9752 | -1.5755 | -1.5237 | -0.9238 | 840875.02 | -17.5169 | no | -0.4165 |
| B6_hold_3x_dir | same_wallet | 0.0000 | -1.0000 | 1.0000 | -333400.34 | -3.6859 | -1.6148 | -1.6557 | -1.0000 | 2999.40 | -35.7852 | **YES** | -1.2785 |
| A2_same_expo_base | same_exposure | 136.6109 | -0.8634 | 0.9237 | -6140.29 | -4.8460 | -1.9403 | -2.0076 | -0.9267 | 140610.38 | 0.0000 | no | -0.5073 |
| B_same_expo_base | same_exposure | 114.9223 | -0.8851 | 0.9239 | -1037.26 | -4.5213 | -1.6860 | -1.6653 | -0.9506 | 853280.91 | -18.5726 | no | -0.4308 |
| A2_same_risk_base | same_risk | 136.6109 | -0.8634 | 0.9237 | -6140.29 | -4.8460 | -1.9403 | -2.0076 | -0.9267 | 140610.38 | 0.0000 | no | -0.5073 |
| B_same_risk_base | same_risk | 117.2497 | -0.8828 | 0.9223 | -1030.14 | -4.4487 | -1.6895 | -1.6504 | -0.9497 | 856921.40 | -18.6683 | no | -0.4297 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 112.5331 | -0.8875 | 0.9316 | -6600.74 | -5.1945 | -2.1790 | -2.2282 | -0.9454 | 134449.70 | 0.0000 | no | -0.5117 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 81.0301 | -0.9190 | 0.9429 | -1273.00 | -5.1488 | -2.3134 | -2.3114 | -0.9687 | 721894.41 | -16.2826 | no | -0.4520 |

- Parameter plateau: ETF `{'flag': 'plateau', 'values': [-0.874022, -0.863389, -0.812734], 'spread': 0.06128800000000001}`  PERP `{'flag': 'sensitive', 'values': [-0.927052, -0.837658, -0.652496], 'spread': 0.274556}`

### Short sleeve (3S vs perp short)
- Window 2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=9000
- 3S final=1008.1367 DD=0.023077 | perp short final=1115.9293 DD=0.426674 LIQ=False

## ETH

- ETF `ETH3L_USDT` vs perp `ETH_USDT`
- Overlap **2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00** (9000 bars, `1h`)
- Funding source: `cache+funding` rows=1080
- Decision: **PERP WIN**  primary=PERP_1.5x  secondary=PERP_3x  do-not-use=ETF

- ETF snapshot leverage=3.0920750740581586 NAV=0.15184977 premium=-0.0021716858708445974 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold -0.9576360330116099 vs theo 3x und -0.9448982374069396 → drag=-0.012737795604670366

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 38.5917 | -0.9614 | 0.9911 | -961653.52 | -4.9313 | -0.6144 | -0.9141 | -0.9666 | 999.7450 | 0.0000 | no | -0.5364 |
| B1_spot_hold | benchmark | 565.4587 | -0.4345 | 0.6799 | -434652.10 | -0.7310 | -0.5101 | -0.7375 | -0.6264 | 999.7450 | 0.0000 | no | -0.3479 |
| B2_spot_grid | benchmark | 459.5112 | -0.5405 | 0.6646 | -1890.14 | -1.7391 | -1.7958 | -1.8058 | -0.7988 | 285951.04 | 0.0000 | no | -0.3413 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 48.3558 | -0.9516 | 0.9797 | -12055.28 | -6.9730 | -1.7500 | -1.9318 | -0.9673 | 78940.05 | 0.0000 | no | -0.5320 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 40.9731 | -0.9590 | 0.9820 | -12635.78 | -7.2447 | -1.8701 | -2.0688 | -0.9729 | 75897.71 | 0.0000 | no | -0.5331 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 43.0912 | -0.9569 | 0.9846 | -23993.01 | -5.7782 | -1.2514 | -1.5848 | -0.9681 | 39882.82 | 0.0000 | no | -0.5340 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 448.5179 | -0.5515 | 0.6667 | -1002.50 | -1.6077 | -0.8898 | -0.9219 | -0.8127 | 550105.02 | -4.2314 | no | -0.3027 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 314.9009 | -0.6851 | 0.7881 | -999.4517 | -2.3899 | -0.8101 | -0.8378 | -0.8568 | 685474.91 | -5.1087 | no | -0.3648 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 151.2911 | -0.8487 | 0.8928 | -1223.03 | -3.8169 | -0.9290 | -0.9875 | -0.9419 | 693937.62 | -5.8222 | no | -0.4280 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 85.9648 | -0.9140 | 0.9437 | -1313.36 | -4.9719 | -0.6635 | -0.7610 | -0.9625 | 695951.40 | -6.6815 | no | -0.4541 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 74.3206 | -0.9257 | 0.9485 | -1373.56 | -5.1372 | -0.7772 | -0.8837 | -0.9703 | 673925.63 | -6.6459 | no | -0.4593 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 366.0202 | -0.6340 | 0.6873 | -1298.41 | -4.7553 | -1.3576 | -1.3015 | -0.9080 | 488274.51 | -4.9170 | no | -0.3395 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 85.9648 | -0.9140 | 0.9437 | -1313.36 | -4.9719 | -0.6635 | -0.7610 | -0.9625 | 695951.40 | -6.6815 | no | -0.4541 |
| B6_hold_3x_dir | same_wallet | 0.2458 | -0.9998 | 0.9998 | -334736.24 | -6.8854 | -1.0394 | -0.5333 | -0.9999 | 2986.69 | -10.4583 | **YES** | -1.2784 |
| A2_same_expo_base | same_exposure | 48.3558 | -0.9516 | 0.9797 | -12055.28 | -6.9730 | -1.7500 | -1.9318 | -0.9673 | 78940.05 | 0.0000 | no | -0.5320 |
| B_same_expo_base | same_exposure | 59.0338 | -0.9410 | 0.9616 | -1383.21 | -5.5118 | -0.5397 | -0.6580 | -0.9737 | 680274.85 | -7.1068 | no | -0.4651 |
| A2_same_risk_base | same_risk | 48.3558 | -0.9516 | 0.9797 | -12055.28 | -6.9730 | -1.7500 | -1.9318 | -0.9673 | 78940.05 | 0.0000 | no | -0.5320 |
| B_same_risk_base | same_risk | 55.9825 | -0.9440 | 0.9625 | -1377.44 | -5.5815 | -0.5141 | -0.6358 | -0.9762 | 685339.75 | -7.1053 | no | -0.4652 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 36.8736 | -0.9631 | 0.9828 | -12478.44 | -7.2104 | -1.9135 | -2.1043 | -0.9765 | 77183.24 | 0.0000 | no | -0.5336 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 48.9996 | -0.9510 | 0.9677 | -1635.77 | -5.8957 | -1.1209 | -1.3229 | -0.9785 | 581379.13 | -6.6736 | no | -0.4789 |

- Parameter plateau: ETF `{'flag': 'plateau', 'values': [-0.957206, -0.951644, -0.950868], 'spread': 0.006337999999999955}`  PERP `{'flag': 'plateau', 'values': [-0.932348, -0.914035, -0.948876], 'spread': 0.03484100000000001}`

### Short sleeve (3S vs perp short)
- Window 2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=9000
- 3S final=1015.9015 DD=0.061934 | perp short final=370.1438 DD=0.740767 LIQ=False

## SOL

- ETF `SOL3L_USDT` vs perp `SOL_USDT`
- Overlap **2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00** (9000 bars, `1h`)
- Funding source: `cache:futures_SOL_USDT_8h_funding.csv|gate_futures_usdt_funding_rate` rows=1079
- Decision: **PERP WIN**  primary=PERP_1.5x  secondary=ETF  do-not-use=PERP_3x

- ETF snapshot leverage=3.0071495699269635 NAV=0.18819389 premium=-0.0016679074968906082 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold -0.9821851606178338 vs theo 3x und -0.974101166063556 → drag=-0.008083994554277774

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 18.0031 | -0.9820 | 0.9967 | -982247.40 | -5.0546 | -0.8792 | -1.3194 | -0.9832 | 999.7450 | 0.0000 | no | -0.5392 |
| B1_spot_hold | benchmark | 486.0649 | -0.5139 | 0.7578 | -514066.16 | -0.9210 | -0.7120 | -1.0608 | -0.6658 | 999.7450 | 0.0000 | no | -0.4011 |
| B2_spot_grid | benchmark | 386.4250 | -0.6136 | 0.7042 | -2421.18 | -2.3210 | -2.0553 | -2.3283 | -0.8573 | 253419.74 | 0.0000 | no | -0.3824 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 21.9062 | -0.9781 | 0.9876 | -14084.64 | -7.1377 | -1.7497 | -2.0309 | -0.9880 | 69444.03 | 0.0000 | no | -0.5358 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 20.1975 | -0.9798 | 0.9884 | -14402.46 | -7.3461 | -1.7991 | -2.0869 | -0.9890 | 68030.20 | 0.0000 | no | -0.5362 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 19.9088 | -0.9801 | 0.9924 | -27804.33 | -5.9159 | -1.4422 | -1.8567 | -0.9854 | 35249.59 | 0.0000 | no | -0.5376 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 724.2695 | -0.2757 | 0.5161 | -788.0787 | -1.2470 | -0.4684 | -0.4383 | -0.5221 | 349876.85 | 5.3999 | no | -0.1602 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 389.0612 | -0.6109 | 0.8091 | -1190.61 | -3.2328 | -0.9091 | -0.9614 | -0.7429 | 513132.01 | 4.7210 | no | -0.3733 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 207.2710 | -0.7927 | 0.9039 | -1749.80 | -5.3227 | -1.0466 | -1.1803 | -0.8672 | 453040.07 | 4.5939 | no | -0.4518 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 43.3785 | -0.9566 | 0.9592 | -7453.51 | -40.6946 | -1.0566 | -0.2030 | -0.9934 | 128345.13 | -3.8776 | **YES** | -1.2624 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 35.6778 | -0.9643 | 0.9664 | -7513.51 | -41.0222 | -1.0638 | -0.2043 | -0.9945 | 128345.13 | -3.8776 | **YES** | -1.2652 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 431.0458 | -0.5690 | 0.6489 | -1466.94 | -5.9054 | -1.5563 | -1.4742 | -0.8618 | 387850.24 | 2.9246 | no | -0.3243 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 52.2857 | -0.9477 | 0.9702 | -3215.72 | -10.9218 | -1.6105 | -1.8003 | -0.9725 | 294712.58 | 5.0502 | no | -0.5169 |
| B6_hold_3x_dir | same_wallet | 33.7078 | -0.9663 | 0.9789 | -330543.88 | -5.6660 | -0.9321 | -0.4976 | -0.9839 | 2923.34 | 8.3007 | **YES** | -1.2698 |
| A2_same_expo_base | same_exposure | 21.9062 | -0.9781 | 0.9876 | -14084.64 | -7.1377 | -1.7497 | -2.0309 | -0.9880 | 69444.03 | 0.0000 | no | -0.5358 |
| B_same_expo_base | same_exposure | 57.6653 | -0.9423 | 0.9457 | -7535.28 | -40.8435 | -1.0387 | -0.1914 | -0.9916 | 125056.34 | -3.7093 | **YES** | -1.2571 |
| A2_same_risk_base | same_risk | 21.9062 | -0.9781 | 0.9876 | -14084.64 | -7.1377 | -1.7497 | -2.0309 | -0.9880 | 69444.03 | 0.0000 | no | -0.5358 |
| B_same_risk_base | same_risk | 50.9055 | -0.9491 | 0.9521 | -7587.84 | -41.1956 | -1.0457 | -0.1929 | -0.9925 | 125081.06 | -3.6924 | **YES** | -1.2596 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 22.7530 | -0.9772 | 0.9868 | -14244.48 | -7.3140 | -1.8254 | -2.0808 | -0.9879 | 68605.29 | 0.0000 | no | -0.5355 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 9.3123 | -0.9907 | 0.9911 | -7900.36 | -41.9453 | -1.0860 | -0.2088 | -0.9983 | 125397.86 | -3.8327 | **YES** | -1.2750 |

- Parameter plateau: ETF `{'flag': 'plateau', 'values': [-0.982341, -0.978094, -0.969336], 'spread': 0.013005000000000044}`  PERP `{'flag': 'plateau', 'values': [-0.950304, -0.956621, -0.967944], 'spread': 0.01763999999999999}`

### Short sleeve (3S vs perp short)
- Window 2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=9000
- 3S final=1017.823 DD=0.037651 | perp short final=908.9606 DD=0.594608 LIQ=False

## PENGU

- ETF `PENGU3L_USDT` vs perp `PENGU_USDT`
- Overlap **2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00** (9000 bars, `1h`)
- Funding source: `cache:futures_PENGU_USDT_8h_funding.csv|gate_futures_usdt_funding_rate` rows=2159
- Decision: **ETF WIN**  primary=ETF  secondary=HYBRID  do-not-use=PERP_3x

- ETF snapshot leverage=3.136892105682555 NAV=0.05234456 premium=-0.00696462058330416 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold -0.9184975640421182 vs theo 3x und -0.999614831977545 → drag=0.08111726793542673

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 81.6099 | -0.9184 | 0.9992 | -918624.34 | -2.1389 | 0.9832 | 447.0659 | -0.9135 | 999.7450 | 0.0000 | no | -0.5373 |
| B1_spot_hold | benchmark | 234.5532 | -0.7654 | 0.8577 | -765642.04 | -2.0370 | -0.8169 | -1.4707 | -0.8817 | 999.7450 | 0.0000 | no | -0.4778 |
| B2_spot_grid | benchmark | 259.2843 | -0.7407 | 0.7934 | -3674.48 | -2.7433 | -1.5489 | -2.1002 | -0.9217 | 201583.72 | 0.0000 | no | -0.4457 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 269.2932 | -0.7307 | 0.9886 | -910.9587 | -0.5110 | 0.9756 | 246.1098 | -0.7295 | 802129.37 | 0.0000 | no | -0.4000 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 240.6881 | -0.7593 | 0.9890 | -997.1829 | -0.5753 | 0.9754 | 247.0398 | -0.7584 | 761456.99 | 0.0000 | no | -0.4151 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 165.2218 | -0.8348 | 0.9920 | -1895.79 | -0.8811 | 0.9761 | 238.6376 | -0.8334 | 440332.51 | 0.0000 | no | -0.4823 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 1.4490 | -0.9986 | 0.9988 | -14049.84 | -16.0085 | -0.9644 | -0.2351 | -0.9994 | 71072.05 | -4.4289 | **YES** | -1.2780 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 0.4915 | -0.9995 | 0.9996 | -10530.89 | -16.0820 | -0.9190 | -0.2333 | -0.9998 | 94912.04 | -5.8479 | **YES** | -1.2784 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 0.0525 | -0.9999 | 1.0000 | -8569.04 | -16.2250 | -0.8656 | -0.2295 | -1.0000 | 116693.03 | -7.2336 | **YES** | -1.2784 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 0.4970 | -0.9995 | 0.9997 | -7343.50 | -16.1882 | -0.7836 | -0.2199 | -0.9997 | 136107.16 | -8.7658 | **YES** | -1.2782 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 0.7536 | -0.9992 | 0.9995 | -7186.13 | -16.5220 | -0.8181 | -0.2277 | -0.9996 | 139052.08 | -8.3574 | **YES** | -1.2781 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 0.6476 | -0.9994 | 0.9995 | -10251.05 | -23.4581 | -0.9281 | -0.2366 | -0.9997 | 97487.81 | -5.8951 | **YES** | -1.2783 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 0.0000 | -1.0000 | 1.0000 | -7347.15 | -16.1963 | -2.4510 | -2.1704 | -1.0000 | 136107.16 | -8.7658 | **YES** | -1.2783 |
| B6_hold_3x_dir | same_wallet | 0.0000 | -1.0000 | 1.0000 | -333709.20 | -9.2167 | -1.2043 | -1.3206 | -1.0000 | 2996.62 | -15.4395 | **YES** | -1.2785 |
| A2_same_expo_base | same_exposure | 269.2932 | -0.7307 | 0.9886 | -910.9587 | -0.5110 | 0.9756 | 246.1098 | -0.7295 | 802129.37 | 0.0000 | no | -0.4000 |
| B_same_expo_base | same_exposure | 0.0565 | -0.9999 | 1.0000 | -7259.41 | -16.2224 | -0.7790 | -0.2193 | -1.0000 | 137744.49 | -8.8404 | **YES** | -1.2783 |
| A2_same_risk_base | same_risk | 269.2932 | -0.7307 | 0.9886 | -910.9587 | -0.5110 | 0.9756 | 246.1098 | -0.7295 | 802129.37 | 0.0000 | no | -0.4000 |
| B_same_risk_base | same_risk | 0.6074 | -0.9994 | 0.9996 | -7040.35 | -16.3329 | -0.7712 | -0.2192 | -0.9997 | 141952.08 | -9.0587 | **YES** | -1.2781 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 12.2954 | -0.9877 | 0.9920 | -21521.07 | -14.4430 | -1.7593 | -1.1786 | -0.9942 | 45894.77 | 0.0000 | no | -0.5377 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 0.3666 | -0.9996 | 0.9998 | -7404.81 | -16.4320 | -0.8245 | -0.2321 | -0.9998 | 134997.82 | -8.5531 | **YES** | -1.2782 |

- Parameter plateau: ETF `{'flag': 'sensitive', 'values': [-0.179547, -0.730707, -0.992795], 'spread': 0.813248}`  PERP `{'flag': 'sensitive', 'values': [-0.815779, -0.999503, -0.990551], 'spread': 0.183724}`

### Short sleeve (3S vs perp short)
- Window 2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=9000
- 3S final=1055.0539 DD=0.066497 | perp short final=339.5386 DD=0.986753 LIQ=False

## PUMP

- ETF `PUMP3L_USDT` vs perp `PUMP_USDT`
- Overlap **2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00** (9000 bars, `1h`)
- Funding source: `cache:futures_PUMP_USDT_8h_funding.csv|gate_futures_usdt_funding_rate` rows=2157
- Decision: **ETF WIN**  primary=ETF  secondary=HYBRID  do-not-use=PERP_1.5x

- ETF snapshot leverage=2.8043838507806926 NAV=0.5699011 premium=-0.007231254686120292 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold 1.952844350121639 vs theo 3x und -0.9963716533809596 → drag=2.9492160035025985

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 2532.26 | 1.5323 | 0.9995 | 1532646.10 | 0.6648 | 0.9896 | 403.5799 | 1.4713 | 999.7450 | 0.0000 | no | 0.5295 |
| B1_spot_hold | benchmark | 920.9302 | -0.0791 | 0.8663 | -79090.02 | -0.1158 | 0.6181 | 1.1128 | -0.0889 | 999.7450 | 0.0000 | no | -0.1765 |
| B2_spot_grid | benchmark | 463.5720 | -0.5364 | 0.8049 | -2681.46 | -2.2972 | -0.5331 | -0.6831 | -0.6545 | 200050.83 | 0.0000 | no | -0.4101 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 10.1456 | -0.9899 | 0.9951 | -12324.82 | -18.2997 | -1.4461 | -0.9712 | -0.9934 | 80313.91 | 0.0000 | no | -0.5389 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 9.4316 | -0.9906 | 0.9953 | -12550.72 | -18.7417 | -1.4862 | -1.0016 | -0.9940 | 78925.21 | 0.0000 | no | -0.5390 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 1276.97 | 0.2770 | 0.9972 | 6800.06 | 0.2349 | 1.0000 | 79.3327 | 0.2695 | 40730.26 | 0.0000 | no | 0.3422 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 0.1735 | -0.9998 | 0.9999 | -11886.88 | -21.7377 | -0.9167 | -0.2213 | -0.9999 | 84111.77 | -4.1055 | **YES** | -1.2785 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 1.4220 | -0.9986 | 0.9989 | -8863.22 | -21.7415 | -0.8468 | -0.2091 | -0.9994 | 112665.43 | -5.4307 | **YES** | -1.2780 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 1.6700 | -0.9983 | 0.9988 | -7088.63 | -21.7440 | -0.7609 | -0.1980 | -0.9992 | 140835.44 | -6.7657 | **YES** | -1.2778 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 1.5077 | -0.9985 | 0.9990 | -5953.46 | -21.8424 | -0.6735 | -0.1852 | -0.9992 | 167716.38 | -8.0767 | **YES** | -1.2773 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 0.1330 | -0.9999 | 0.9999 | -5966.93 | -21.9360 | -0.6822 | -0.1876 | -0.9999 | 167568.03 | -8.0564 | **YES** | -1.2777 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 1.1617 | -0.9988 | 0.9991 | -8547.93 | -31.2574 | -0.8465 | -0.2155 | -0.9995 | 116851.46 | -5.6491 | **YES** | -1.2781 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 0.0000 | -1.0000 | 1.0000 | -5962.45 | -21.8754 | -2.1043 | -1.8281 | -1.0000 | 167716.38 | -8.0767 | **YES** | -1.2777 |
| B6_hold_3x_dir | same_wallet | 0.0000 | -1.0000 | 1.0000 | -333647.41 | -4.0956 | 0.6750 | 0.7222 | -1.0000 | 2997.18 | -17.8281 | **YES** | -1.2785 |
| A2_same_expo_base | same_exposure | 10.1456 | -0.9899 | 0.9951 | -12324.82 | -18.2997 | -1.4461 | -0.9712 | -0.9934 | 80313.91 | 0.0000 | no | -0.5389 |
| B_same_expo_base | same_exposure | 0.0846 | -0.9999 | 0.9999 | -7241.58 | -21.8389 | -0.7730 | -0.1998 | -1.0000 | 138079.70 | -6.6118 | **YES** | -1.2783 |
| A2_same_risk_base | same_risk | 10.1456 | -0.9899 | 0.9951 | -12324.82 | -18.2997 | -1.4461 | -0.9712 | -0.9934 | 80313.91 | 0.0000 | no | -0.5389 |
| B_same_risk_base | same_risk | 1.5109 | -0.9985 | 0.9989 | -6838.92 | -21.7768 | -0.7458 | -0.1961 | -0.9993 | 146000.97 | -7.0190 | **YES** | -1.2778 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 11.6223 | -0.9884 | 0.9943 | -12480.68 | -18.4830 | -1.3692 | -0.9104 | -0.9926 | 79192.62 | 0.0000 | no | -0.5386 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 0.1567 | -0.9998 | 0.9999 | -6103.11 | -22.4780 | -0.7357 | -0.2088 | -0.9999 | 163825.14 | -7.9118 | **YES** | -1.2778 |

- Parameter plateau: ETF `{'flag': 'sensitive', 'values': [-0.629696, -0.989854, -0.130489], 'spread': 0.859365}`  PERP `{'flag': 'plateau', 'values': [-0.998876, -0.998492, -0.999896], 'spread': 0.0014039999999999608}`

### Short sleeve (3S vs perp short)
- Window 2025-09-02 22:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=9000
- 3S final=940.8156 DD=0.220282 | perp short final=0.7072 DD=0.999361 LIQ=True

## SOXL

- ETF `SOXL3L_USDT` vs perp `SOXL_USDT`
- Overlap **2026-06-25 09:00:00+00:00 → 2026-09-12 21:00:00+00:00** (1909 bars, `1h`)
- Funding source: `cache:futures_SOXL_USDT_8h_funding.csv|gate_futures_usdt_funding_rate` rows=364
- Decision: **PERP WIN**  primary=PERP_1.5x  secondary=HYBRID  do-not-use=ETF

- ETF snapshot leverage=3.11710940722494 NAV=0.01797296 premium=-0.0018338659853468497 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold -0.9776647857630062 vs theo 3x und -0.9869061301319256 → drag=0.009241344368919435

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 29.1756 | -0.9708 | 0.9898 | -971072.06 | -5.1678 | -0.8638 | -1.3701 | -1.0103 | 999.7450 | 0.0000 | no | -0.5364 |
| B1_spot_hold | benchmark | 526.5789 | -0.4734 | 0.6730 | -473541.81 | -0.7423 | -1.1436 | -1.6375 | -1.4076 | 999.7450 | 0.0000 | no | -0.3555 |
| B2_spot_grid | benchmark | 705.7514 | -0.2942 | 0.5012 | -5009.71 | -0.6610 | -0.9681 | -1.3820 | -1.5924 | 58735.71 | 0.0000 | no | -0.2357 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 119.0265 | -0.8810 | 0.9476 | -39361.35 | -3.7249 | -1.0752 | -1.3995 | -1.0553 | 22381.69 | 0.0000 | no | -0.5173 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 115.9276 | -0.8841 | 0.9485 | -39834.42 | -3.7735 | -1.1053 | -1.4383 | -1.0542 | 22193.68 | 0.0000 | no | -0.5178 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 72.8605 | -0.9271 | 0.9666 | -79622.27 | -4.3758 | -1.3191 | -1.8148 | -1.0346 | 11644.22 | 0.0000 | no | -0.5263 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 513.3481 | -0.4867 | 0.7108 | -5014.13 | -1.2669 | -0.7472 | -1.0874 | -1.3410 | 97056.07 | 0.0000 | no | -0.3825 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 326.7256 | -0.6733 | 0.8309 | -5927.42 | -2.0302 | -0.7394 | -1.1185 | -1.1964 | 113586.32 | 0.0000 | no | -0.4582 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 174.2065 | -0.8258 | 0.9161 | -7601.66 | -2.9513 | -0.6923 | -1.0729 | -1.0912 | 108633.34 | 0.0000 | no | -0.5028 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 100.4085 | -0.8996 | 0.9628 | -9022.35 | -3.7945 | -0.3278 | -0.5219 | -1.0387 | 99706.98 | 0.0000 | no | -0.5236 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 96.5340 | -0.9035 | 0.9635 | -9219.82 | -3.8384 | -0.3560 | -0.5649 | -1.0379 | 97991.67 | 0.0000 | no | -0.5241 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 369.8439 | -0.6302 | 0.7324 | -9074.94 | -3.8029 | -1.7106 | -1.8810 | -1.3512 | 69439.14 | 0.0000 | no | -0.4191 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 100.4085 | -0.8996 | 0.9628 | -9022.35 | -3.7945 | -0.3278 | -0.5219 | -1.0387 | 99706.98 | 0.0000 | no | -0.5236 |
| B6_hold_3x_dir | same_wallet | 0.6388 | -0.9994 | 0.9996 | -333383.33 | -8.1768 | -1.9961 | -1.0636 | -1.0004 | 2997.63 | 0.0000 | **YES** | -1.2783 |
| A2_same_expo_base | same_exposure | 119.0265 | -0.8810 | 0.9476 | -39361.35 | -3.7249 | -1.0752 | -1.3995 | -1.0553 | 22381.69 | 0.0000 | no | -0.5173 |
| B_same_expo_base | same_exposure | 139.1118 | -0.8609 | 0.9384 | -8124.47 | -3.2964 | -0.5610 | -0.8747 | -1.0656 | 105962.35 | 0.0000 | no | -0.5129 |
| A2_same_risk_base | same_risk | 119.0265 | -0.8810 | 0.9476 | -39361.35 | -3.7249 | -1.0752 | -1.3995 | -1.0553 | 22381.69 | 0.0000 | no | -0.5173 |
| B_same_risk_base | same_risk | 148.7233 | -0.8513 | 0.9311 | -8002.05 | -3.1820 | -0.6225 | -0.9670 | -1.0739 | 106382.38 | 0.0000 | no | -0.5097 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 106.8181 | -0.8932 | 0.9481 | -42567.68 | -4.0503 | -1.4103 | -1.7816 | -1.0547 | 20982.63 | 0.0000 | no | -0.5182 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 94.5067 | -0.9055 | 0.9653 | -9509.69 | -3.9101 | -0.3507 | -0.5539 | -1.0359 | 95217.92 | 0.0000 | no | -0.5248 |

- Parameter plateau: ETF `{'flag': 'plateau', 'values': [-0.89729, -0.880973, -0.851835], 'spread': 0.04545500000000002}`  PERP `{'flag': 'plateau', 'values': [-0.980853, -0.899592, -0.868434], 'spread': 0.11241899999999994}`

### Short sleeve (3S vs perp short)
- Window 2026-06-25 09:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=1909
- 3S final=1039.7638 DD=0.138793 | perp short final=523.3767 DD=0.715767 LIQ=False

## SNXX

- ETF `SNXX3L_USDT` vs perp `SNXX_USDT`
- Overlap **2026-07-29 07:00:00+00:00 → 2026-09-12 21:00:00+00:00** (1095 bars, `1h`)
- Funding source: `gate_futures_usdt_funding_rate` rows=182
- Decision: **PERP WIN**  primary=PERP_3x  secondary=PERP_1.5x  do-not-use=ETF

- ETF snapshot leverage=3.066287108580723 NAV=1.14223885 premium=-0.0004717489691408172 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold 1.0061148108450033 vs theo 3x und -0.24166103320573118 → drag=1.2477758440507345

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 2029.21 | 1.0292 | 0.8295 | 1029469.91 | 0.4093 | 3.6272 | 9.1355 | 347.1807 | 999.7450 | 0.0000 | no | 0.5528 |
| B1_spot_hold | benchmark | 2243.92 | 1.2439 | 0.3946 | 1244235.70 | 0.6204 | 3.4955 | 6.0966 | 1635.92 | 999.7450 | 0.0000 | no | 0.7353 |
| B2_spot_grid | benchmark | 1310.83 | 0.3108 | 0.2833 | 5348.02 | 0.4446 | 2.4623 | 2.7976 | 27.3032 | 58120.47 | 0.0000 | no | 0.6442 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 799.5642 | -0.2004 | 0.7197 | -7024.64 | -0.3772 | 1.6412 | 1.9110 | -1.1577 | 28533.27 | 0.0000 | no | -0.2425 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 788.7321 | -0.2113 | 0.7213 | -7402.82 | -0.3999 | 1.6163 | 1.8809 | -1.1790 | 28538.84 | 0.0000 | no | -0.2516 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 1432.95 | 0.4330 | 0.8097 | 27076.47 | 0.2808 | 3.4050 | 6.0108 | 20.7775 | 15989.94 | 0.0000 | no | 0.4678 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 1485.11 | 0.4851 | 0.2892 | 7002.33 | 0.8189 | 3.0864 | 3.7258 | 78.6065 | 69278.78 | -6.1005 | no | 0.7248 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 1647.71 | 0.6477 | 0.3377 | 7010.76 | 1.0629 | 3.3066 | 4.0847 | 158.4920 | 92387.90 | -8.1392 | no | 0.7424 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 1809.26 | 0.8093 | 0.3754 | 7006.61 | 1.2930 | 3.4940 | 4.4025 | 304.5345 | 115499.13 | -10.1748 | no | 0.7478 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 1971.11 | 0.9711 | 0.4056 | 7003.43 | 1.5122 | 3.6584 | 4.6940 | 562.1141 | 138662.54 | -12.2127 | no | 0.7470 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 1962.79 | 0.9628 | 0.4072 | 6943.43 | 1.4992 | 3.6393 | 4.6680 | 541.2722 | 138662.54 | -12.2127 | no | 0.7461 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 1679.33 | 0.6793 | 0.3460 | 7004.52 | 1.5111 | 3.3445 | 4.1488 | 180.6297 | 96984.46 | -8.5422 | no | 0.7469 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 1971.11 | 0.9711 | 0.4056 | 7003.43 | 1.5122 | 3.6584 | 4.6940 | 562.1141 | 138662.54 | -12.2127 | no | 0.7470 |
| B6_hold_3x_dir | same_wallet | 4689.13 | 3.6891 | 0.5155 | 1229970.43 | 0.9256 | 3.7735 | 10.4469 | 458595.18 | 2999.37 | -43.4019 | no | 0.7124 |
| A2_same_expo_base | same_exposure | 799.5642 | -0.2004 | 0.7197 | -7024.64 | -0.3772 | 1.6412 | 1.9110 | -1.1577 | 28533.27 | 0.0000 | no | -0.2425 |
| B_same_expo_base | same_exposure | 1852.25 | 0.8522 | 0.3840 | 7004.17 | 1.3523 | 3.5399 | 4.4830 | 359.8174 | 121677.35 | -10.7180 | no | 0.7480 |
| A2_same_risk_base | same_risk | 799.5642 | -0.2004 | 0.7197 | -7024.64 | -0.3772 | 1.6412 | 1.9110 | -1.1577 | 28533.27 | 0.0000 | no | -0.2425 |
| B_same_risk_base | same_risk | 1841.30 | 0.8413 | 0.3816 | 7011.49 | 1.3375 | 3.5293 | 4.4639 | 345.1404 | 119989.18 | -10.5710 | no | 0.7480 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 753.3126 | -0.2467 | 0.7197 | -11190.38 | -0.5826 | 0.9636 | 1.0375 | -1.2457 | 22044.60 | 0.0000 | no | -0.2895 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 1929.81 | 0.9298 | 0.4133 | 6705.52 | 1.4486 | 3.5636 | 4.5652 | 465.2738 | 138663.96 | -12.2131 | no | 0.7422 |

- Parameter plateau: ETF `{'flag': 'sensitive', 'values': [-0.351518, -0.200436, -0.307855], 'spread': 0.151082}`  PERP `{'flag': 'sensitive', 'values': [0.807728, 0.971114, 0.300855], 'spread': 0.670259}`

### Short sleeve (3S vs perp short)
- Window 2026-07-29 07:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=1095
- 3S final=595.9477 DD=0.466763 | perp short final=470.3443 DD=0.529656 LIQ=True

## AAOI

- ETF `AAOI3L_USDT` vs perp `AAOI_USDT`
- Overlap **2026-09-09 08:00:00+00:00 → 2026-09-12 21:00:00+00:00** (86 bars, `1h`)
- Funding source: `gate_futures_usdt_funding_rate` rows=321
- Decision: **PERP WIN**  primary=PERP_1.5x  secondary=PERP_3x  do-not-use=ETF

- ETF snapshot leverage=3.041335144575975 NAV=0.79371092 premium=0.0015233253940867275 (NAV history: False)

- Path-drag attribution (not a PnL debit): ETF hold -0.08630381056382574 vs theo 3x und -0.08968917496800011 → drag=0.0033853644041743625

| name | lens | final | ret | maxDD | pnl/1M | capEff | sharpe | sortino | calmar | turnover | funding | LIQ | score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_cash | benchmark | 1000.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |  | no | 0.3500 |
| A1_etf_hold | benchmark | 848.7134 | -0.1513 | 0.2585 | -151325.21 | -0.1699 | -3.8469 | -5.7955 | -3.8679 | 999.7450 | 0.0000 | no | -0.0130 |
| B1_spot_hold | benchmark | 947.0172 | -0.0530 | 0.0959 | -52996.34 | -0.0552 | -4.2150 | -6.0138 | -10.3922 | 999.7450 | 0.0000 | no | 0.1236 |
| B2_spot_grid | benchmark | 1001.69 | 0.0017 | 0.0250 | 398.2249 | 0.0041 | 1.3377 | 3.2551 | 7.6294 | 4250.49 | 0.0000 | no | 0.3728 |
| A2_etf_native_atr_d0.0_reb_base | same_wallet | 948.7418 | -0.0513 | 0.1535 | -29039.30 | -0.0802 | -2.3008 | -4.3355 | -6.4867 | 1765.13 | 0.0000 | no | 0.0969 |
| A2_etf_native_atr_d0.0_noreb_base | same_wallet | 947.7654 | -0.0522 | 0.1538 | -29613.19 | -0.0818 | -2.3485 | -4.3927 | -6.4742 | 1763.90 | 0.0000 | no | 0.0958 |
| A2_etf_native_atr_d0.5_reb_base | same_wallet | 897.6198 | -0.1024 | 0.1864 | -74047.85 | -0.1326 | -3.1436 | -5.2077 | -5.3644 | 1382.62 | 0.0000 | no | 0.0454 |
| B_perp_1.5x_iso_P1_d0.0_reb_base | same_wallet | 1004.28 | 0.0043 | 0.0369 | 665.4503 | 0.0105 | 1.7006 | 4.3352 | 14.9664 | 6429.14 | 0.0000 | no | 0.3905 |
| B_perp_2.0x_iso_P1_d0.0_reb_base | same_wallet | 1005.64 | 0.0056 | 0.0492 | 658.0795 | 0.0138 | 1.7571 | 4.4903 | 15.9662 | 8571.28 | 0.0000 | no | 0.3874 |
| B_perp_2.5x_iso_P1_d0.0_reb_base | same_wallet | 1007.10 | 0.0071 | 0.0613 | 662.0226 | 0.0174 | 1.8257 | 4.6891 | 17.4932 | 10723.86 | 0.0000 | no | 0.3852 |
| B_perp_3.0x_iso_P1_d0.0_reb_base | same_wallet | 1008.48 | 0.0085 | 0.0735 | 659.3000 | 0.0209 | 1.8883 | 4.8682 | 18.8942 | 12868.08 | 0.0000 | no | 0.3825 |
| B_perp_3.0x_iso_P1_d0.0_noreb_base | same_wallet | 1007.71 | 0.0077 | 0.0737 | 599.3000 | 0.0190 | 1.8241 | 4.6555 | 16.3879 | 12868.08 | 0.0000 | no | 0.3774 |
| B_perp_3x_iso_P2_reb_base | same_wallet | 1005.93 | 0.0059 | 0.0517 | 659.0881 | 0.0209 | 1.7697 | 4.5236 | 16.2471 | 9001.48 | 0.0000 | no | 0.3889 |
| B_perp_3x_cross_P1_reb_base | same_wallet | 1008.48 | 0.0085 | 0.0735 | 659.3000 | 0.0209 | 1.8883 | 4.8682 | 18.8942 | 12868.08 | 0.0000 | no | 0.3825 |
| B6_hold_3x_dir | same_wallet | 841.6624 | -0.1583 | 0.2739 | -52791.28 | -0.1795 | -3.4961 | -5.2825 | -3.6503 | 2999.31 | 0.0000 | no | -0.0242 |
| A2_same_expo_base | same_exposure | 948.7418 | -0.0513 | 0.1535 | -29039.30 | -0.0802 | -2.3008 | -4.3355 | -6.4867 | 1765.13 | 0.0000 | no | 0.0969 |
| B_same_expo_base | same_exposure | 1007.35 | 0.0073 | 0.0635 | 661.1304 | 0.0181 | 1.8370 | 4.7211 | 17.7246 | 11110.61 | 0.0000 | no | 0.3847 |
| A2_same_risk_base | same_risk | 948.7418 | -0.0513 | 0.1535 | -29039.30 | -0.0802 | -2.3008 | -4.3355 | -6.4867 | 1765.13 | 0.0000 | no | 0.0969 |
| B_same_risk_base | same_risk | 1007.49 | 0.0075 | 0.0653 | 656.5060 | 0.0184 | 1.8405 | 4.7298 | 17.7345 | 11408.61 | 0.0000 | no | 0.3840 |
| A2_etf_native_atr_d0.0_reb_conservative | same_wallet | 946.0928 | -0.0539 | 0.1538 | -37924.76 | -0.0871 | -2.5984 | -4.6691 | -6.4820 | 1421.42 | 0.0000 | no | 0.0935 |
| B_perp_3.0x_iso_P1_d0.0_reb_conservative | same_wallet | 993.4016 | -0.0066 | 0.0875 | -500.9246 | -0.0142 | 1.0598 | 2.4324 | -5.6492 | 13172.43 | 0.0000 | no | 0.2750 |

- Parameter plateau: ETF `{'flag': 'plateau', 'values': [-0.058435, -0.051258, -0.047342], 'spread': 0.011092999999999999}`  PERP `{'flag': 'plateau', 'values': [0.011643, 0.008484, 0.015648], 'spread': 0.0071639999999999985}`

### Short sleeve (3S vs perp short)
- Window 2026-09-09 08:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=86
- 3S final=1043.4814 DD=0.031527 | perp short final=1000.0 DD=0.0 LIQ=False

## Portfolio (10_000 USDT, overlapping history only)

- Overlap 2026-06-25 09:00:00+00:00 → 2026-09-12 21:00:00+00:00 bars=1909
- Weights {'SOL': 0.28, 'ETH': 0.28, 'SOXL': 0.23999999999999996, 'PENGU': 0.07999999999999999, 'PUMP': 0.07999999999999999} cash=0.040000000000000036

