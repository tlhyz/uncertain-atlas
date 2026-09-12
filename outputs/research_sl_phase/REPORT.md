# Gate 3L/3S 现货网格 + S→L 对抗回测报告

判定标准：NET ETF GRID EDGE 必须在 Base/Conservative、0% 返佣、失败窗口、Walk-forward、Monte Carlo 下仍稳健。否则判失败。

**总判定：FAIL**

## 1. ETF 真实数据完整性

主数据：`download.gatedata.org/spot/deals` 官方逐笔。禁止 Yahoo/Stooq 日线做网格或策略 PnL。

- maker=0.0008 taker=0.00085 来源：qtb.costs.fees VIP7 spot table
- 返佣情景：0% / 50% / 70% 分开记账，不并进隐藏费率。

### PUMP 污染

- 规则：PUMP3L before 2025-07-18 is old PumpBTC-era; do not merge with pump.fun PUMP3L
- 旧带月份：['202504', '202505', '202506']
- 现行月份：['202507', '202508', '202509', '202510', '202511', '202512', '202601', '202602', '202603', '202604', '202605', '202606', '202607', '202608']
- 是否合并：False

### 各产品

- `SOXL3L_USDT` listed=2026-06-25 months=['202606', '202607', '202608'] strategy_prints=71701 status=ok
- `SOXL3S_USDT` listed=2026-06-25 months=['202606', '202607', '202608'] strategy_prints=62331 status=ok
- `SOXLG_USDT` listed=2026-07-01 months=['202607', '202608'] strategy_prints=238588 status=ok
- `SNXX3L_USDT` listed=2026-07-29 months=['202607', '202608'] strategy_prints=37108 status=ok
- `SNXX3S_USDT` listed=2026-07-29 months=['202607', '202608'] strategy_prints=27829 status=ok
- `SNXXG_USDT` listed=2026-07-01 months=['202607', '202608'] strategy_prints=199618 status=ok
- `AAOI3L_USDT` listed=2026-09-09 months=[] strategy_prints=0 status=DATA_MISSING
- `BTC3L_USDT` listed=None months=['202407', '202408', '202409', '202410', '202411', '202412', '202501', '202502', '202503', '202504', '202505', '202506', '202507', '202508', '202509', '202510', '202511', '202512', '202601', '202602', '202603', '202604', '202605', '202606', '202607', '202608'] strategy_prints=879036 status=ok
- `ETH3L_USDT` listed=None months=['202407', '202408', '202409', '202410', '202411', '202412', '202501', '202502', '202503', '202504', '202505', '202506', '202507', '202508', '202509', '202510', '202511', '202512', '202601', '202602', '202603', '202604', '202605', '202606', '202607', '202608'] strategy_prints=836117 status=ok
- `SOL3L_USDT` listed=None months=['202407', '202408', '202409', '202410', '202411', '202412', '202501', '202502', '202503', '202504', '202505', '202506', '202507', '202508', '202509', '202510', '202511', '202512', '202601', '202602', '202603', '202604', '202605', '202606', '202607', '202608'] strategy_prints=1448457 status=ok
- `PENGU3L_USDT` listed=2025-07-18 months=['202507', '202508', '202509', '202510', '202511', '202512', '202601', '202602', '202603', '202604', '202605', '202606', '202607', '202608'] strategy_prints=480452 status=ok
- `PUMP3L_USDT` listed=2025-07-18 months=['202504', '202505', '202506', '202507', '202508', '202509', '202510', '202511', '202512', '202601', '202602', '202603', '202604', '202605', '202606', '202607', '202608'] strategy_prints=693394 status=ok
- `PUMPBTC_USDT` listed=2025-06-01 months=[] strategy_prints=0 status=DATA_MISSING

## 2. 哪些区间是真实 Gate ETF

自动扫描得到 REAL 窗口 154 个（按 ETF 自身小时序列，不用底层日期）。

## 3. 哪些区间是 Synthetic

SYNTHETIC 窗口 0 个。上市前无 Gate 3L 逐笔且无合格高频底层时，**不会**伪造窗口。

AAOI3L：官方 deals 不存在（上市 2026-09-09，9 月文件未发布）。不得用 AAOI 日线代替 AAOI3L 进统计。

SOXL3L/3S 上市前：无 Gate 逐笔，无 SOXLG。S1/S2 保持 UNDERLYING_ONLY_CANDIDATE，**不进最终统计**。

## 4. Synthetic vs Real 校准

- SOXL3L_USDT_3L: status=ok n_days=55 C=-94.04% A=-92.13% B=-93.33% A-C=1.91% B-C=0.71% A_MAE=0.0551 B_MAE=0.0754
- SOXL3S_USDT_3S: status=ok n_days=55 C=-7.31% A=-50.35% B=-38.70% A-C=-43.04% B-C=-31.38% A_MAE=0.3110 B_MAE=0.4165
  - **LOW CONFIDENCE**：A vs C MAE > 15% 归一化路径。更早 synthetic 不得当高置信。
- SNXX3L_USDT_3L: status=ok n_days=35 C=54.78% A=181.78% B=10.27% A-C=127.01% B-C=-44.50% A_MAE=1.2567 B_MAE=0.6438
  - **LOW CONFIDENCE**：A vs C MAE > 15% 归一化路径。更早 synthetic 不得当高置信。
- SNXX3S_USDT_3S: status=ok n_days=35 C=-99.15% A=-100.00% B=-100.00% A-C=-0.85% B-C=-0.85% A_MAE=0.0508 B_MAE=0.0806

## 5. 每只 ETF 最相似 / 自动窗口（ETF 自身）

### SOXL3L_USDT
- drop_then_rise 2026-06-26 09:00:00+00:00 → 2026-08-10 08:00:00+00:00 ret=-93.29% dd=-98.66% rebound=255.98% x1%=896 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2026-08-13 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=-40.98% dd=-71.53% rebound=65.34% x1%=244 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-07-03 09:00:00+00:00 → 2026-08-17 08:00:00+00:00 ret=-84.06% dd=-96.57% rebound=277.61% x1%=876 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-08-20 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=6.24% dd=-42.88% rebound=65.34% x1%=122 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-07-16 09:00:00+00:00 → 2026-07-23 08:00:00+00:00 ret=-0.41% dd=-51.04% rebound=103.40% x1%=140 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-07-07 21:00:00+00:00 → 2026-07-14 20:00:00+00:00 ret=7.51% dd=-53.03% rebound=36.88% x1%=141 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-08-24 21:00:00+00:00 → 2026-08-31 20:00:00+00:00 ret=0.91% dd=-38.63% rebound=12.18% x1%=121 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-07-27 09:00:00+00:00 → 2026-08-17 08:00:00+00:00 ret=-39.29% dd=-83.92% rebound=277.61% x1%=400 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-07-08 09:00:00+00:00 → 2026-07-15 08:00:00+00:00 ret=54.65% dd=-53.03% rebound=54.65% x1%=141 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-07-19 21:00:00+00:00 → 2026-07-26 20:00:00+00:00 ret=20.82% dd=-47.58% rebound=20.82% x1%=140 `REAL_GATE_ETF_WINDOW`
- rise_then_fall 2026-07-03 21:00:00+00:00 → 2026-08-02 20:00:00+00:00 ret=-89.59% dd=-96.57% rebound=150.72% x1%=600 `REAL_GATE_ETF_WINDOW`
- rise_then_fall 2026-08-06 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=-24.11% dd=-71.53% rebound=65.34% x1%=373 `REAL_GATE_ETF_WINDOW`

### SOXL3S_USDT
- drop_then_rise 2026-06-29 21:00:00+00:00 → 2026-08-28 20:00:00+00:00 ret=-29.19% dd=-88.43% rebound=99.02% x1%=1160 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-07-29 21:00:00+00:00 → 2026-08-28 20:00:00+00:00 ret=-76.81% dd=-88.35% rebound=99.02% x1%=559 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-07-15 21:00:00+00:00 → 2026-07-29 20:00:00+00:00 ret=170.56% dd=-62.80% rebound=260.44% x1%=273 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-06-25 09:00:00+00:00 → 2026-07-09 08:00:00+00:00 ret=26.15% dd=-59.04% rebound=70.25% x1%=290 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-07-13 09:00:00+00:00 → 2026-07-27 08:00:00+00:00 ret=7.55% dd=-62.80% rebound=43.39% x1%=268 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-08-20 21:00:00+00:00 → 2026-08-27 20:00:00+00:00 ret=-6.19% dd=-44.10% rebound=21.68% x1%=125 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-06-27 21:00:00+00:00 → 2026-07-27 20:00:00+00:00 ret=5.28% dd=-66.66% rebound=146.99% x1%=592 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-08-06 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=-37.49% dd=-53.38% rebound=29.70% x1%=373 `REAL_GATE_ETF_WINDOW`
- rise_then_fall 2026-06-25 21:00:00+00:00 → 2026-08-24 20:00:00+00:00 ret=-16.83% dd=-88.43% rebound=114.92% x1%=1154 `REAL_GATE_ETF_WINDOW`
- trend_up 2026-06-29 21:00:00+00:00 → 2026-07-29 20:00:00+00:00 ret=190.23% dd=-66.66% rebound=392.47% x1%=600 `REAL_GATE_ETF_WINDOW`
- trend_up 2026-08-15 21:00:00+00:00 → 2026-08-29 20:00:00+00:00 ret=47.38% dd=-44.10% rebound=95.06% x1%=246 `REAL_GATE_ETF_WINDOW`
- trend_down 2026-07-01 09:00:00+00:00 → 2026-08-15 08:00:00+00:00 ret=-31.10% dd=-86.57% rebound=14.88% x1%=883 `REAL_GATE_ETF_WINDOW`

### SNXX3L_USDT
- drop_then_rise 2026-08-01 07:00:00+00:00 → 2026-08-15 06:00:00+00:00 ret=147.26% dd=-79.30% rebound=423.87% x1%=284 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2026-08-16 07:00:00+00:00 → 2026-08-30 06:00:00+00:00 ret=-67.05% dd=-82.95% rebound=30.67% x1%=276 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-08-03 19:00:00+00:00 → 2026-08-17 18:00:00+00:00 ret=199.22% dd=-79.30% rebound=645.64% x1%=273 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-08-20 07:00:00+00:00 → 2026-08-27 06:00:00+00:00 ret=-35.74% dd=-60.73% rebound=59.17% x1%=138 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-08-09 07:00:00+00:00 → 2026-08-30 06:00:00+00:00 ret=61.78% dd=-82.95% rebound=83.03% x1%=403 `REAL_GATE_ETF_WINDOW`
- rise_then_fall 2026-07-29 07:00:00+00:00 → 2026-08-12 06:00:00+00:00 ret=-21.23% dd=-81.33% rebound=60.65% x1%=294 `REAL_GATE_ETF_WINDOW`
- rise_then_fall 2026-08-16 19:00:00+00:00 → 2026-08-30 18:00:00+00:00 ret=-67.15% dd=-82.95% rebound=28.67% x1%=275 `REAL_GATE_ETF_WINDOW`
- trend_up 2026-08-09 19:00:00+00:00 → 2026-08-23 18:00:00+00:00 ret=194.38% dd=-66.95% rebound=244.24% x1%=267 `REAL_GATE_ETF_WINDOW`
- trend_up 2026-07-29 07:00:00+00:00 → 2026-08-05 06:00:00+00:00 ret=124.33% dd=-72.33% rebound=341.12% x1%=153 `REAL_GATE_ETF_WINDOW`
- trend_down 2026-08-17 19:00:00+00:00 → 2026-08-31 18:00:00+00:00 ret=-78.87% dd=-82.94% rebound=14.92% x1%=276 `REAL_GATE_ETF_WINDOW`
- trend_down 2026-07-31 19:00:00+00:00 → 2026-08-07 18:00:00+00:00 ret=-44.59% dd=-78.79% rebound=12.52% x1%=152 `REAL_GATE_ETF_WINDOW`

### SNXX3S_USDT
- drop_then_rise 2026-08-03 07:00:00+00:00 → 2026-08-24 06:00:00+00:00 ret=-93.79% dd=-98.04% rebound=136.03% x1%=421 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-07-29 07:00:00+00:00 → 2026-08-28 06:00:00+00:00 ret=-98.42% dd=-99.54% rebound=182.62% x1%=616 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-08-19 19:00:00+00:00 → 2026-08-26 18:00:00+00:00 ret=7.79% dd=-44.30% rebound=33.55% x1%=140 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-08-16 19:00:00+00:00 → 2026-08-23 18:00:00+00:00 ret=-4.88% dd=-47.27% rebound=76.36% x1%=143 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-08-04 07:00:00+00:00 → 2026-08-11 06:00:00+00:00 ret=-33.00% dd=-54.90% rebound=48.56% x1%=142 `REAL_GATE_ETF_WINDOW`
- rise_then_fall 2026-07-29 07:00:00+00:00 → 2026-08-19 06:00:00+00:00 ret=-98.98% dd=-99.54% rebound=82.97% x1%=433 `REAL_GATE_ETF_WINDOW`
- trend_up 2026-08-17 19:00:00+00:00 → 2026-08-31 18:00:00+00:00 ret=122.64% dd=-51.43% rebound=140.74% x1%=284 `REAL_GATE_ETF_WINDOW`
- trend_down 2026-07-29 19:00:00+00:00 → 2026-08-19 18:00:00+00:00 ret=-98.89% dd=-99.51% rebound=116.78% x1%=433 `REAL_GATE_ETF_WINDOW`

### BTC3L_USDT
- drop_then_rise 2024-07-15 23:00:00+00:00 → 2024-11-18 09:00:00+00:00 ret=65.29% dd=-56.76% rebound=229.07% x1%=1432 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2025-01-18 20:00:00+00:00 → 2025-05-10 11:00:00+00:00 ret=-4.59% dd=-67.11% rebound=156.12% x1%=1473 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2025-12-16 23:00:00+00:00 → 2026-03-16 22:00:00+00:00 ret=-52.38% dd=-76.75% rebound=56.18% x1%=1374 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-02-02 11:00:00+00:00 → 2025-05-22 22:00:00+00:00 ret=33.24% dd=-60.78% rebound=213.11% x1%=1463 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-01-17 23:00:00+00:00 → 2026-04-17 22:00:00+00:00 ret=-59.87% dd=-75.03% rebound=59.08% x1%=1450 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-05-23 23:00:00+00:00 → 2026-08-21 22:00:00+00:00 ret=-14.21% dd=-62.33% rebound=119.48% x1%=1178 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-03-03 23:00:00+00:00 → 2026-06-01 22:00:00+00:00 ret=-7.26% dd=-39.20% rebound=12.41% x1%=1262 `REAL_GATE_ETF_WINDOW`
- double_bottom 2025-07-03 11:00:00+00:00 → 2025-10-01 10:00:00+00:00 ret=6.67% dd=-36.36% rebound=22.13% x1%=1171 `REAL_GATE_ETF_WINDOW`
- double_bottom 2024-11-16 09:00:00+00:00 → 2025-02-04 10:00:00+00:00 ret=7.89% dd=-35.61% rebound=19.46% x1%=979 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2024-11-07 23:00:00+00:00 → 2025-03-06 08:00:00+00:00 ret=27.25% dd=-55.89% rebound=36.81% x1%=1474 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2024-07-28 21:00:00+00:00 → 2024-10-24 00:00:00+00:00 ret=-21.39% dd=-56.76% rebound=71.99% x1%=950 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-02-22 11:00:00+00:00 → 2026-05-23 10:00:00+00:00 ret=4.97% dd=-36.25% rebound=35.19% x1%=1325 `REAL_GATE_ETF_WINDOW`

### ETH3L_USDT
- drop_then_rise 2025-02-28 08:00:00+00:00 → 2025-06-11 14:00:00+00:00 ret=75.51% dd=-81.83% rebound=544.52% x1%=1677 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2025-06-11 15:00:00+00:00 → 2025-08-10 14:00:00+00:00 ret=149.17% dd=-60.00% rebound=522.85% x1%=1063 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2026-05-26 15:00:00+00:00 → 2026-08-24 14:00:00+00:00 ret=23.82% dd=-67.47% rebound=280.67% x1%=1391 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-01-26 20:00:00+00:00 → 2025-05-13 23:00:00+00:00 ret=-55.44% dd=-92.76% rebound=487.80% x1%=1683 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-05-16 00:00:00+00:00 → 2025-08-14 02:00:00+00:00 ret=353.30% dd=-60.00% rebound=781.35% x1%=1610 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-05-24 03:00:00+00:00 → 2026-08-22 02:00:00+00:00 ret=18.15% dd=-69.63% rebound=280.41% x1%=1393 `REAL_GATE_ETF_WINDOW`
- double_bottom 2025-07-18 03:00:00+00:00 → 2025-10-16 02:00:00+00:00 ret=1.12% dd=-65.63% rebound=29.56% x1%=1550 `REAL_GATE_ETF_WINDOW`
- double_bottom 2024-08-24 11:00:00+00:00 → 2024-11-20 20:00:00+00:00 ret=5.61% dd=-46.67% rebound=89.09% x1%=1019 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-02-23 03:00:00+00:00 → 2026-05-24 02:00:00+00:00 ret=6.97% dd=-48.04% rebound=15.17% x1%=1422 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-05-07 08:00:00+00:00 → 2025-07-06 14:00:00+00:00 ret=101.27% dd=-60.00% rebound=120.24% x1%=1089 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-08-03 15:00:00+00:00 → 2025-11-01 14:00:00+00:00 ret=-2.55% dd=-67.77% rebound=16.06% x1%=1552 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-02-13 15:00:00+00:00 → 2026-05-14 14:00:00+00:00 ret=2.21% dd=-44.06% rebound=47.67% x1%=1440 `REAL_GATE_ETF_WINDOW`

### SOL3L_USDT
- drop_then_rise 2025-01-25 03:00:00+00:00 → 2025-04-25 11:00:00+00:00 ret=-78.83% dd=-94.63% rebound=271.70% x1%=1740 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2025-05-26 19:00:00+00:00 → 2025-08-24 18:00:00+00:00 ret=20.97% dd=-68.00% rebound=249.69% x1%=1719 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2024-08-21 09:00:00+00:00 → 2024-11-22 12:00:00+00:00 ret=209.41% dd=-50.29% rebound=367.66% x1%=1621 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-02-12 15:00:00+00:00 → 2025-05-14 03:00:00+00:00 ret=-32.49% dd=-89.39% rebound=452.58% x1%=1732 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-05-16 04:00:00+00:00 → 2025-08-14 06:00:00+00:00 ret=19.16% dd=-72.01% rebound=247.08% x1%=1719 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-04-08 19:00:00+00:00 → 2026-07-07 18:00:00+00:00 ret=-33.05% dd=-78.81% rebound=105.40% x1%=1506 `REAL_GATE_ETF_WINDOW`
- double_bottom 2024-11-20 13:00:00+00:00 → 2025-01-19 14:00:00+00:00 ret=6.54% dd=-66.91% rebound=157.69% x1%=1097 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-02-24 07:00:00+00:00 → 2026-05-25 06:00:00+00:00 ret=0.09% dd=-51.07% rebound=19.47% x1%=1474 `REAL_GATE_ETF_WINDOW`
- double_bottom 2024-08-05 00:00:00+00:00 → 2024-09-20 08:00:00+00:00 ret=6.69% dd=-53.67% rebound=63.81% x1%=811 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-03-31 22:00:00+00:00 → 2025-06-30 06:00:00+00:00 ret=6.19% dd=-72.01% rebound=166.03% x1%=1725 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-05-26 19:00:00+00:00 → 2026-08-24 18:00:00+00:00 ret=7.25% dd=-65.03% rebound=200.50% x1%=1479 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2024-10-26 06:00:00+00:00 → 2025-01-24 14:00:00+00:00 ret=110.67% dd=-66.91% rebound=158.30% x1%=1677 `REAL_GATE_ETF_WINDOW`

### PENGU3L_USDT
- drop_then_rise 2025-10-08 23:00:00+00:00 → 2026-01-06 23:00:00+00:00 ret=469.07% dd=-99.83% rebound=326709.64% x1%=1870 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2026-01-28 00:00:00+00:00 → 2026-04-27 23:00:00+00:00 ret=-57.59% dd=-90.87% rebound=314.75% x1%=1820 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2026-05-26 00:00:00+00:00 → 2026-08-23 23:00:00+00:00 ret=-16.37% dd=-83.24% rebound=361.35% x1%=1690 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-11-14 23:00:00+00:00 → 2026-01-13 23:00:00+00:00 ret=56698.39% dd=-84.13% rebound=314362.30% x1%=1225 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-02-08 12:00:00+00:00 → 2026-05-09 11:00:00+00:00 ret=109.42% dd=-69.97% rebound=312.19% x1%=1812 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-06-01 12:00:00+00:00 → 2026-08-30 11:00:00+00:00 ret=-5.53% dd=-71.60% rebound=226.50% x1%=1703 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-04-15 12:00:00+00:00 → 2026-05-30 11:00:00+00:00 ret=1.39% dd=-76.77% rebound=17.65% x1%=921 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-02-08 12:00:00+00:00 → 2026-03-25 11:00:00+00:00 ret=1.15% dd=-58.12% rebound=45.76% x1%=912 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-06-26 00:00:00+00:00 → 2026-07-25 23:00:00+00:00 ret=3.12% dd=-44.83% rebound=21.45% x1%=564 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-09-30 11:00:00+00:00 → 2025-12-29 11:00:00+00:00 ret=228.22% dd=-99.85% rebound=127536.59% x1%=1866 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2026-04-02 00:00:00+00:00 → 2026-05-31 23:00:00+00:00 ret=5.97% dd=-76.77% rebound=41.80% x1%=1216 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-12-29 12:00:00+00:00 → 2026-01-28 11:00:00+00:00 ret=8.46% dd=-75.25% rebound=54.91% x1%=599 `REAL_GATE_ETF_WINDOW`

### PUMP3L_USDT
- drop_then_rise 2025-10-17 12:00:00+00:00 → 2026-01-15 13:00:00+00:00 ret=17042.14% dd=-98.80% rebound=423436.74% x1%=1894 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2026-05-25 14:00:00+00:00 → 2026-08-23 13:00:00+00:00 ret=612.66% dd=-83.53% rebound=3929.08% x1%=1855 `REAL_GATE_ETF_WINDOW`
- drop_then_rise 2025-08-17 00:00:00+00:00 → 2025-09-15 23:00:00+00:00 ret=794.47% dd=-70.40% rebound=2388.04% x1%=652 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-10-30 00:00:00+00:00 → 2026-01-28 01:00:00+00:00 ret=5798.73% dd=-98.74% rebound=451083.06% x1%=1899 `REAL_GATE_ETF_WINDOW`
- v_reversal 2026-05-25 02:00:00+00:00 → 2026-08-23 01:00:00+00:00 ret=828.87% dd=-83.53% rebound=4505.62% x1%=1854 `REAL_GATE_ETF_WINDOW`
- v_reversal 2025-07-20 00:00:00+00:00 → 2025-09-17 23:00:00+00:00 ret=67.83% dd=-94.16% rebound=1982.19% x1%=1330 `REAL_GATE_ETF_WINDOW`
- double_bottom 2025-10-12 00:00:00+00:00 → 2025-11-10 23:00:00+00:00 ret=7.75% dd=-75.41% rebound=74.59% x1%=635 `REAL_GATE_ETF_WINDOW`
- double_bottom 2025-07-29 12:00:00+00:00 → 2025-08-19 11:00:00+00:00 ret=-2.59% dd=-70.18% rebound=21.66% x1%=472 `REAL_GATE_ETF_WINDOW`
- double_bottom 2026-02-24 02:00:00+00:00 → 2026-03-26 01:00:00+00:00 ret=-4.56% dd=-51.28% rebound=29.56% x1%=616 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-10-08 12:00:00+00:00 → 2026-01-06 13:00:00+00:00 ret=639.24% dd=-99.80% rebound=301652.18% x1%=1886 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-09-04 12:00:00+00:00 → 2025-10-04 11:00:00+00:00 ret=114.63% dd=-84.98% rebound=176.54% x1%=658 `REAL_GATE_ETF_WINDOW`
- high_vol_chop 2025-07-31 00:00:00+00:00 → 2025-08-29 23:00:00+00:00 ret=10.54% dd=-78.65% rebound=131.12% x1%=660 `REAL_GATE_ETF_WINDOW`

## 6–9. 先跌后涨 / 先涨后跌 / 横盘 / 单边（ETF 自身）

### 先跌后涨 (21)
- SOXL3L_USDT 2026-06-26 09:00:00+00:00 → 2026-08-10 08:00:00+00:00 ret=-93.29% dd=-98.66%
- SOXL3L_USDT 2026-08-13 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=-40.98% dd=-71.53%
- SOXL3S_USDT 2026-06-29 21:00:00+00:00 → 2026-08-28 20:00:00+00:00 ret=-29.19% dd=-88.43%
- SNXX3L_USDT 2026-08-01 07:00:00+00:00 → 2026-08-15 06:00:00+00:00 ret=147.26% dd=-79.30%
- SNXX3L_USDT 2026-08-16 07:00:00+00:00 → 2026-08-30 06:00:00+00:00 ret=-67.05% dd=-82.95%
- SNXX3S_USDT 2026-08-03 07:00:00+00:00 → 2026-08-24 06:00:00+00:00 ret=-93.79% dd=-98.04%
- BTC3L_USDT 2024-07-15 23:00:00+00:00 → 2024-11-18 09:00:00+00:00 ret=65.29% dd=-56.76%
- BTC3L_USDT 2025-01-18 20:00:00+00:00 → 2025-05-10 11:00:00+00:00 ret=-4.59% dd=-67.11%

### V 反 (23)
- SOXL3L_USDT 2026-07-03 09:00:00+00:00 → 2026-08-17 08:00:00+00:00 ret=-84.06% dd=-96.57%
- SOXL3L_USDT 2026-08-20 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=6.24% dd=-42.88%
- SOXL3S_USDT 2026-07-29 21:00:00+00:00 → 2026-08-28 20:00:00+00:00 ret=-76.81% dd=-88.35%
- SOXL3S_USDT 2026-07-15 21:00:00+00:00 → 2026-07-29 20:00:00+00:00 ret=170.56% dd=-62.80%
- SOXL3S_USDT 2026-06-25 09:00:00+00:00 → 2026-07-09 08:00:00+00:00 ret=26.15% dd=-59.04%
- SNXX3L_USDT 2026-08-03 19:00:00+00:00 → 2026-08-17 18:00:00+00:00 ret=199.22% dd=-79.30%
- SNXX3L_USDT 2026-08-20 07:00:00+00:00 → 2026-08-27 06:00:00+00:00 ret=-35.74% dd=-60.73%
- SNXX3S_USDT 2026-07-29 07:00:00+00:00 → 2026-08-28 06:00:00+00:00 ret=-98.42% dd=-99.54%

### 先涨后跌 (22)
- SOXL3L_USDT 2026-07-03 21:00:00+00:00 → 2026-08-02 20:00:00+00:00 ret=-89.59% dd=-96.57%
- SOXL3L_USDT 2026-08-06 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=-24.11% dd=-71.53%
- SOXL3L_USDT 2026-06-26 09:00:00+00:00 → 2026-07-03 08:00:00+00:00 ret=-55.29% dd=-78.07%
- SOXL3S_USDT 2026-06-25 21:00:00+00:00 → 2026-08-24 20:00:00+00:00 ret=-16.83% dd=-88.43%
- SNXX3L_USDT 2026-07-29 07:00:00+00:00 → 2026-08-12 06:00:00+00:00 ret=-21.23% dd=-81.33%
- SNXX3L_USDT 2026-08-16 19:00:00+00:00 → 2026-08-30 18:00:00+00:00 ret=-67.15% dd=-82.95%
- SNXX3S_USDT 2026-07-29 07:00:00+00:00 → 2026-08-19 06:00:00+00:00 ret=-98.98% dd=-99.54%
- BTC3L_USDT 2025-12-13 11:00:00+00:00 → 2026-03-13 10:00:00+00:00 ret=-60.05% dd=-76.75%

### 高波动横盘 (23)
- SOXL3L_USDT 2026-07-27 09:00:00+00:00 → 2026-08-17 08:00:00+00:00 ret=-39.29% dd=-83.92%
- SOXL3L_USDT 2026-07-08 09:00:00+00:00 → 2026-07-15 08:00:00+00:00 ret=54.65% dd=-53.03%
- SOXL3L_USDT 2026-07-19 21:00:00+00:00 → 2026-07-26 20:00:00+00:00 ret=20.82% dd=-47.58%
- SOXL3S_USDT 2026-06-27 21:00:00+00:00 → 2026-07-27 20:00:00+00:00 ret=5.28% dd=-66.66%
- SOXL3S_USDT 2026-08-06 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=-37.49% dd=-53.38%
- SNXX3L_USDT 2026-08-09 07:00:00+00:00 → 2026-08-30 06:00:00+00:00 ret=61.78% dd=-82.95%
- SNXX3S_USDT 2026-08-16 19:00:00+00:00 → 2026-08-23 18:00:00+00:00 ret=-4.88% dd=-47.27%
- SNXX3S_USDT 2026-08-04 07:00:00+00:00 → 2026-08-11 06:00:00+00:00 ret=-33.00% dd=-54.90%

### 单边下跌 (22)
- SOXL3L_USDT 2026-07-01 09:00:00+00:00 → 2026-07-31 08:00:00+00:00 ret=-95.68% dd=-98.50%
- SOXL3L_USDT 2026-08-01 21:00:00+00:00 → 2026-08-31 20:00:00+00:00 ret=-34.45% dd=-71.53%
- SOXL3S_USDT 2026-07-01 09:00:00+00:00 → 2026-08-15 08:00:00+00:00 ret=-31.10% dd=-86.57%
- SOXL3S_USDT 2026-08-20 09:00:00+00:00 → 2026-08-27 08:00:00+00:00 ret=-22.27% dd=-44.10%
- SNXX3L_USDT 2026-08-17 19:00:00+00:00 → 2026-08-31 18:00:00+00:00 ret=-78.87% dd=-82.94%
- SNXX3L_USDT 2026-07-31 19:00:00+00:00 → 2026-08-07 18:00:00+00:00 ret=-44.59% dd=-78.79%
- SNXX3S_USDT 2026-07-29 19:00:00+00:00 → 2026-08-19 18:00:00+00:00 ret=-98.89% dd=-99.51%
- BTC3L_USDT 2025-11-08 23:00:00+00:00 → 2026-02-06 22:00:00+00:00 ret=-74.29% dd=-84.53%

### 单边上涨 (22)
- SOXL3L_USDT 2026-07-29 09:00:00+00:00 → 2026-08-19 08:00:00+00:00 ret=9.33% dd=-54.44%
- SOXL3L_USDT 2026-07-16 21:00:00+00:00 → 2026-07-23 20:00:00+00:00 ret=24.84% dd=-38.19%
- SOXL3S_USDT 2026-06-29 21:00:00+00:00 → 2026-07-29 20:00:00+00:00 ret=190.23% dd=-66.66%
- SOXL3S_USDT 2026-08-15 21:00:00+00:00 → 2026-08-29 20:00:00+00:00 ret=47.38% dd=-44.10%
- SNXX3L_USDT 2026-08-09 19:00:00+00:00 → 2026-08-23 18:00:00+00:00 ret=194.38% dd=-66.95%
- SNXX3L_USDT 2026-07-29 07:00:00+00:00 → 2026-08-05 06:00:00+00:00 ret=124.33% dd=-72.33%
- SNXX3S_USDT 2026-08-17 19:00:00+00:00 → 2026-08-31 18:00:00+00:00 ret=122.64% dd=-51.43%
- BTC3L_USDT 2024-07-21 22:00:00+00:00 → 2024-11-22 16:00:00+00:00 ret=75.20% dd=-56.76%

### 二次探底 (21)
- SOXL3L_USDT 2026-07-16 09:00:00+00:00 → 2026-07-23 08:00:00+00:00 ret=-0.41% dd=-51.04%
- SOXL3L_USDT 2026-07-07 21:00:00+00:00 → 2026-07-14 20:00:00+00:00 ret=7.51% dd=-53.03%
- SOXL3L_USDT 2026-08-24 21:00:00+00:00 → 2026-08-31 20:00:00+00:00 ret=0.91% dd=-38.63%
- SOXL3S_USDT 2026-07-13 09:00:00+00:00 → 2026-07-27 08:00:00+00:00 ret=7.55% dd=-62.80%
- SOXL3S_USDT 2026-08-20 21:00:00+00:00 → 2026-08-27 20:00:00+00:00 ret=-6.19% dd=-44.10%
- SNXX3S_USDT 2026-08-19 19:00:00+00:00 → 2026-08-26 18:00:00+00:00 ret=7.79% dd=-44.30%
- BTC3L_USDT 2026-03-03 23:00:00+00:00 → 2026-06-01 22:00:00+00:00 ret=-7.26% dd=-39.20%
- BTC3L_USDT 2025-07-03 11:00:00+00:00 → 2025-10-01 10:00:00+00:00 ret=6.67% dd=-36.36%

## Candidate remap（底层日期 ±15/30 天，禁止沿用 underlying_bottom）

- candidate `S1` → SOXL UNDERLYING_ONLY_CANDIDATE regime=unknown start=None bottom=None reversal=None end=None allowed=False
- candidate `S2` → SOXL UNDERLYING_ONLY_CANDIDATE regime=unknown start=None bottom=None reversal=None end=None allowed=False
- candidate `S3` → SOXL3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2026-06-25 09:00:00+00:00 bottom=2026-07-29 21:00:00+00:00 reversal=2026-07-29 23:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `S3` → SOXL3S_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2026-06-25 09:00:00+00:00 bottom=2026-08-17 15:00:00+00:00 reversal=2026-08-18 01:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `S3` → ETH3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2026-05-26 00:00:00+00:00 bottom=2026-06-26 02:00:00+00:00 reversal=2026-06-26 15:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `S3` → SOL3L_USDT REAL_GATE_ETF_WINDOW regime=trend_up start=2026-05-26 00:00:00+00:00 bottom=2026-06-06 04:00:00+00:00 reversal=2026-06-06 08:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `S3` → SNXX3L_USDT SYNTHETIC_GATE_ETF_WINDOW regime=v_reversal start=2026-07-29 07:00:00+00:00 bottom=2026-08-10 12:00:00+00:00 reversal=2026-08-10 13:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `S3` → SNXX3S_USDT SYNTHETIC_GATE_ETF_WINDOW regime=v_reversal start=2026-07-29 07:00:00+00:00 bottom=2026-08-17 14:00:00+00:00 reversal=2026-08-17 18:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `N1` → SNXX3L_USDT SYNTHETIC_GATE_ETF_WINDOW regime=v_reversal start=2026-07-29 07:00:00+00:00 bottom=2026-08-10 12:00:00+00:00 reversal=2026-08-10 13:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `N1` → SNXX3S_USDT SYNTHETIC_GATE_ETF_WINDOW regime=v_reversal start=2026-07-29 07:00:00+00:00 bottom=2026-08-17 14:00:00+00:00 reversal=2026-08-17 18:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `A1` → AAOI UNDERLYING_ONLY_CANDIDATE regime=unknown start=None bottom=None reversal=None end=None allowed=False
- candidate `A2` → AAOI UNDERLYING_ONLY_CANDIDATE regime=unknown start=None bottom=None reversal=None end=None allowed=False
- candidate `B1` → BTC3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2024-07-01 00:00:00+00:00 bottom=2024-08-05 12:00:00+00:00 reversal=2024-08-05 14:00:00+00:00 end=2024-10-29 23:00:00+00:00 allowed=True
- candidate `B2` → BTC3L_USDT REAL_GATE_ETF_WINDOW regime=v_reversal start=2024-12-21 00:00:00+00:00 bottom=2025-04-07 06:00:00+00:00 reversal=2025-04-07 12:00:00+00:00 end=2025-06-29 23:00:00+00:00 allowed=True
- candidate `E1` → ETH3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2025-02-22 00:00:00+00:00 bottom=2025-04-09 03:00:00+00:00 reversal=2025-04-09 06:00:00+00:00 end=2025-06-11 23:00:00+00:00 allowed=True
- candidate `L1` → SOL3L_USDT REAL_GATE_ETF_WINDOW regime=v_reversal start=2024-07-01 00:00:00+00:00 bottom=2024-08-05 12:00:00+00:00 reversal=2024-08-05 13:00:00+00:00 end=2024-09-22 23:00:00+00:00 allowed=True
- candidate `L2` → SOL3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2025-02-22 00:00:00+00:00 bottom=2025-04-07 06:00:00+00:00 reversal=2025-04-07 08:00:00+00:00 end=2025-06-29 23:00:00+00:00 allowed=True
- candidate `PG1` → PENGU3L_USDT SYNTHETIC_GATE_ETF_WINDOW regime=trend_down start=2025-07-18 11:00:00+00:00 bottom=2025-08-29 18:00:00+00:00 reversal=None end=2025-08-29 23:00:00+00:00 allowed=True
- candidate `PG2` → PENGU3L_USDT REAL_GATE_ETF_WINDOW regime=high_vol_chop start=2025-12-17 00:00:00+00:00 bottom=2025-12-19 01:00:00+00:00 reversal=2025-12-19 03:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `PP1` → PUMP3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2026-01-02 00:00:00+00:00 bottom=2026-06-25 16:00:00+00:00 reversal=2026-06-26 03:00:00+00:00 end=2026-08-31 23:00:00+00:00 allowed=True
- candidate `SX_FAIL` → SOXL3L_USDT SYNTHETIC_GATE_ETF_WINDOW regime=drop_then_rise start=2026-06-25 09:00:00+00:00 bottom=2026-07-29 21:00:00+00:00 reversal=2026-07-29 23:00:00+00:00 end=2026-08-14 23:00:00+00:00 allowed=True
- candidate `SX_FAIL` → SOXL3S_USDT SYNTHETIC_GATE_ETF_WINDOW regime=drop_then_rise start=2026-06-25 09:00:00+00:00 bottom=2026-08-17 15:00:00+00:00 reversal=2026-08-18 01:00:00+00:00 end=2026-08-29 23:00:00+00:00 allowed=True
- candidate `NX_FAIL` → SNXX3L_USDT SYNTHETIC_GATE_ETF_WINDOW regime=drop_then_rise start=2026-07-29 07:00:00+00:00 bottom=2026-08-10 12:00:00+00:00 reversal=2026-08-10 13:00:00+00:00 end=2026-08-12 23:00:00+00:00 allowed=True
- candidate `NX_FAIL` → SNXX3S_USDT SYNTHETIC_GATE_ETF_WINDOW regime=drop_then_rise start=2026-07-29 07:00:00+00:00 bottom=2026-08-17 14:00:00+00:00 reversal=2026-08-17 18:00:00+00:00 end=2026-08-27 23:00:00+00:00 allowed=True
- candidate `AX_FAIL` → AAOI UNDERLYING_ONLY_CANDIDATE regime=unknown start=None bottom=None reversal=None end=None allowed=False
- candidate `BX_FAIL` → BTC3L_USDT REAL_GATE_ETF_WINDOW regime=trend_up start=2024-08-07 00:00:00+00:00 bottom=2024-09-06 20:00:00+00:00 reversal=2024-09-09 13:00:00+00:00 end=2025-05-06 23:00:00+00:00 allowed=True
- candidate `EX_FAIL` → ETH3L_USDT REAL_GATE_ETF_WINDOW regime=rise_then_fall start=2024-08-02 01:00:00+00:00 bottom=2025-04-09 03:00:00+00:00 reversal=2025-04-09 06:00:00+00:00 end=2025-05-08 23:00:00+00:00 allowed=True
- candidate `LX_FAIL` → SOL3L_USDT REAL_GATE_ETF_WINDOW regime=rise_then_fall start=2024-07-06 00:00:00+00:00 bottom=2025-04-07 06:00:00+00:00 reversal=2025-04-07 08:00:00+00:00 end=2025-05-08 23:00:00+00:00 allowed=True
- candidate `PGX_FAIL` → PENGU3L_USDT SYNTHETIC_GATE_ETF_WINDOW regime=high_vol_chop start=2025-07-18 11:00:00+00:00 bottom=2025-12-19 01:00:00+00:00 reversal=2025-12-19 03:00:00+00:00 end=2026-01-14 23:00:00+00:00 allowed=True
- candidate `PPX_FAIL` → PUMP3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2025-08-30 00:00:00+00:00 bottom=2025-12-24 05:00:00+00:00 reversal=2025-12-24 15:00:00+00:00 end=2026-01-14 23:00:00+00:00 allowed=True
- candidate `E_V2024` → ETH3L_USDT REAL_GATE_ETF_WINDOW regime=drop_then_rise start=2024-07-14 00:00:00+00:00 bottom=2024-09-06 20:00:00+00:00 reversal=2024-09-07 07:00:00+00:00 end=2024-10-14 23:00:00+00:00 allowed=True

## 10. 各策略收益（仅 REAL + SYNTHETIC）

网格结果条数：全部 240，进统计 240，剔除 UNDERLYING_ONLY 0。

| window | symbol | fill | rebate | init | final | ret | MDD | grid_pnl | inv_pnl | gross_fee | rebate | mgmt | n_prints | conf |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| S3_SOXL3L_USDT_pad15 | SOXL3L_USDT | base | 0.00% | 1500.00 | 1228.34 | -18.11% | nan% | 261.02 | -8823.07 | 19.04 | 0.00 | 14.62 | 29895 | REAL_GATE_ETF_WINDOW |
| S3_SOXL3L_USDT_pad15 | SOXL3L_USDT | base | 70.00% | 1500.00 | 1228.34 | -18.11% | nan% | 261.02 | -8823.07 | 19.04 | 13.33 | 14.62 | 29895 | REAL_GATE_ETF_WINDOW |
| S3_SOXL3L_USDT_pad15 | SOXL3L_USDT | conservative | 0.00% | 1500.00 | 1414.71 | -5.69% | nan% | 194.85 | -5205.67 | 11.28 | 0.00 | 7.62 | 29895 | REAL_GATE_ETF_WINDOW |
| S3_SOXL3L_USDT_pad15 | SOXL3L_USDT | conservative | 70.00% | 1500.00 | 1414.71 | -5.69% | nan% | 194.85 | -5205.67 | 11.28 | 7.89 | 7.62 | 29895 | REAL_GATE_ETF_WINDOW |
| S3_SOXL3S_USDT_pad15 | SOXL3S_USDT | base | 0.00% | 500.00 | 618.63 | 23.73% | nan% | 132.71 | -8833.45 | 15.50 | 0.00 | 4.37 | 21516 | REAL_GATE_ETF_WINDOW |
| S3_SOXL3S_USDT_pad15 | SOXL3S_USDT | base | 70.00% | 500.00 | 618.63 | 23.73% | nan% | 132.71 | -8833.45 | 15.50 | 10.85 | 4.37 | 21516 | REAL_GATE_ETF_WINDOW |
| S3_SOXL3S_USDT_pad15 | SOXL3S_USDT | conservative | 0.00% | 500.00 | 608.55 | 21.71% | nan% | 120.81 | -7693.24 | 13.80 | 0.00 | 4.19 | 21516 | REAL_GATE_ETF_WINDOW |
| S3_SOXL3S_USDT_pad15 | SOXL3S_USDT | conservative | 70.00% | 500.00 | 608.55 | 21.71% | nan% | 120.81 | -7693.24 | 13.80 | 9.66 | 4.19 | 21516 | REAL_GATE_ETF_WINDOW |
| S3_ETH3L_USDT_pad30 | ETH3L_USDT | base | 0.00% | 750.00 | 799.64 | 6.62% | nan% | 59.43 | -3400.42 | 6.18 | 0.00 | 9.45 | 48800 | REAL_GATE_ETF_WINDOW |
| S3_ETH3L_USDT_pad30 | ETH3L_USDT | base | 70.00% | 750.00 | 799.64 | 6.62% | nan% | 59.43 | -3400.42 | 6.18 | 4.33 | 9.45 | 48800 | REAL_GATE_ETF_WINDOW |
| S3_ETH3L_USDT_pad30 | ETH3L_USDT | conservative | 0.00% | 750.00 | 792.55 | 5.67% | nan% | 51.02 | -2493.25 | 5.24 | 0.00 | 8.89 | 48800 | REAL_GATE_ETF_WINDOW |
| S3_ETH3L_USDT_pad30 | ETH3L_USDT | conservative | 70.00% | 750.00 | 792.55 | 5.67% | nan% | 51.02 | -2493.25 | 5.24 | 3.66 | 8.89 | 48800 | REAL_GATE_ETF_WINDOW |
| S3_SOL3L_USDT_pad30 | SOL3L_USDT | base | 0.00% | 1050.00 | 776.07 | -26.09% | nan% | 33.10 | -2386.26 | 4.30 | 0.00 | 13.96 | 34105 | REAL_GATE_ETF_WINDOW |
| S3_SOL3L_USDT_pad30 | SOL3L_USDT | base | 70.00% | 1050.00 | 776.07 | -26.09% | nan% | 33.10 | -2386.26 | 4.30 | 3.01 | 13.96 | 34105 | REAL_GATE_ETF_WINDOW |
| S3_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 788.04 | -24.95% | nan% | 27.92 | -1934.80 | 3.69 | 0.00 | 12.87 | 34105 | REAL_GATE_ETF_WINDOW |
| S3_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 788.04 | -24.95% | nan% | 27.92 | -1934.80 | 3.69 | 2.59 | 12.87 | 34105 | REAL_GATE_ETF_WINDOW |
| S3_SNXX3L_USDT_pad15 | SNXX3L_USDT | base | 0.00% | 600.00 | 450.98 | -24.84% | nan% | 170.69 | -6266.09 | 11.62 | 0.00 | 5.98 | 34436 | SYNTHETIC_GATE_ETF_WINDOW |
| S3_SNXX3L_USDT_pad15 | SNXX3L_USDT | base | 70.00% | 600.00 | 450.98 | -24.84% | nan% | 170.69 | -6266.09 | 11.62 | 8.14 | 5.98 | 34436 | SYNTHETIC_GATE_ETF_WINDOW |
| S3_SNXX3L_USDT_pad15 | SNXX3L_USDT | conservative | 0.00% | 600.00 | 491.22 | -18.13% | nan% | 131.99 | -3745.06 | 7.94 | 0.00 | 4.30 | 34436 | SYNTHETIC_GATE_ETF_WINDOW |
| S3_SNXX3L_USDT_pad15 | SNXX3L_USDT | conservative | 70.00% | 600.00 | 491.22 | -18.13% | nan% | 131.99 | -3745.06 | 7.94 | 5.56 | 4.30 | 34436 | SYNTHETIC_GATE_ETF_WINDOW |
| S3_SNXX3S_USDT_pad15 | SNXX3S_USDT | base | 0.00% | 500.00 | 239.62 | -52.08% | nan% | 51.77 | -2406.47 | 4.22 | 0.00 | 1.68 | 19866 | SYNTHETIC_GATE_ETF_WINDOW |
| S3_SNXX3S_USDT_pad15 | SNXX3S_USDT | base | 70.00% | 500.00 | 239.62 | -52.08% | nan% | 51.77 | -2406.47 | 4.22 | 2.95 | 1.68 | 19866 | SYNTHETIC_GATE_ETF_WINDOW |
| S3_SNXX3S_USDT_pad15 | SNXX3S_USDT | conservative | 0.00% | 500.00 | 345.20 | -30.96% | nan% | 42.79 | -1323.15 | 2.85 | 0.00 | 1.09 | 19866 | SYNTHETIC_GATE_ETF_WINDOW |
| S3_SNXX3S_USDT_pad15 | SNXX3S_USDT | conservative | 70.00% | 500.00 | 345.20 | -30.96% | nan% | 42.79 | -1323.15 | 2.85 | 2.00 | 1.09 | 19866 | SYNTHETIC_GATE_ETF_WINDOW |
| B1_BTC3L_USDT_pad30 | BTC3L_USDT | base | 0.00% | 300.00 | 282.35 | -5.88% | nan% | 12.40 | -509.64 | 1.21 | 0.00 | 4.96 | 27096 | REAL_GATE_ETF_WINDOW |
| B1_BTC3L_USDT_pad30 | BTC3L_USDT | base | 70.00% | 300.00 | 282.35 | -5.88% | nan% | 12.40 | -509.64 | 1.21 | 0.84 | 4.96 | 27096 | REAL_GATE_ETF_WINDOW |
| B1_BTC3L_USDT_pad30 | BTC3L_USDT | conservative | 0.00% | 300.00 | 285.15 | -4.95% | nan% | 7.34 | -183.54 | 0.62 | 0.00 | 3.32 | 27096 | REAL_GATE_ETF_WINDOW |
| B1_BTC3L_USDT_pad30 | BTC3L_USDT | conservative | 70.00% | 300.00 | 285.15 | -4.95% | nan% | 7.34 | -183.54 | 0.62 | 0.43 | 3.32 | 27096 | REAL_GATE_ETF_WINDOW |
| B2_BTC3L_USDT_pad30 | BTC3L_USDT | base | 0.00% | 300.00 | 324.04 | 8.01% | nan% | 22.76 | -549.66 | 1.34 | 0.00 | 2.93 | 10770 | REAL_GATE_ETF_WINDOW |
| B2_BTC3L_USDT_pad30 | BTC3L_USDT | base | 70.00% | 300.00 | 324.04 | 8.01% | nan% | 22.76 | -549.66 | 1.34 | 0.94 | 2.93 | 10770 | REAL_GATE_ETF_WINDOW |
| B2_BTC3L_USDT_pad30 | BTC3L_USDT | conservative | 0.00% | 300.00 | 318.62 | 6.21% | nan% | 16.80 | -300.63 | 0.69 | 0.00 | 2.59 | 10770 | REAL_GATE_ETF_WINDOW |
| B2_BTC3L_USDT_pad30 | BTC3L_USDT | conservative | 70.00% | 300.00 | 318.62 | 6.21% | nan% | 16.80 | -300.63 | 0.69 | 0.48 | 2.59 | 10770 | REAL_GATE_ETF_WINDOW |
| E1_ETH3L_USDT_pad30 | ETH3L_USDT | base | 0.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 0.00 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| E1_ETH3L_USDT_pad30 | ETH3L_USDT | base | 70.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 2.49 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| E1_ETH3L_USDT_pad30 | ETH3L_USDT | conservative | 0.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 0.00 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| E1_ETH3L_USDT_pad30 | ETH3L_USDT | conservative | 70.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 1.42 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| L1_SOL3L_USDT_pad30 | SOL3L_USDT | base | 0.00% | 1050.00 | 985.18 | -6.17% | nan% | 74.17 | -2474.51 | 5.70 | 0.00 | 9.12 | 51569 | REAL_GATE_ETF_WINDOW |
| L1_SOL3L_USDT_pad30 | SOL3L_USDT | base | 70.00% | 1050.00 | 985.18 | -6.17% | nan% | 74.17 | -2474.51 | 5.70 | 3.99 | 9.12 | 51569 | REAL_GATE_ETF_WINDOW |
| L1_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 1012.73 | -3.55% | nan% | 55.11 | -1165.95 | 3.48 | 0.00 | 6.26 | 51569 | REAL_GATE_ETF_WINDOW |
| L1_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 1012.73 | -3.55% | nan% | 55.11 | -1165.95 | 3.48 | 2.44 | 6.26 | 51569 | REAL_GATE_ETF_WINDOW |
| L2_SOL3L_USDT_pad30 | SOL3L_USDT | base | 0.00% | 1050.00 | 1133.01 | 7.91% | nan% | 85.21 | -3227.82 | 7.44 | 0.00 | 12.34 | 23149 | REAL_GATE_ETF_WINDOW |
| L2_SOL3L_USDT_pad30 | SOL3L_USDT | base | 70.00% | 1050.00 | 1133.01 | 7.91% | nan% | 85.21 | -3227.82 | 7.44 | 5.21 | 12.34 | 23149 | REAL_GATE_ETF_WINDOW |
| L2_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 1107.01 | 5.43% | nan% | 56.04 | -1483.65 | 4.34 | 0.00 | 10.51 | 23149 | REAL_GATE_ETF_WINDOW |
| L2_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 1107.01 | 5.43% | nan% | 56.04 | -1483.65 | 4.34 | 3.04 | 10.51 | 23149 | REAL_GATE_ETF_WINDOW |
| PG1_PENGU3L_USDT_pad30 | PENGU3L_USDT | base | 0.00% | 600.00 | 591.37 | -1.44% | nan% | 73.43 | -2175.06 | 3.90 | 0.00 | 1.84 | 10175 | SYNTHETIC_GATE_ETF_WINDOW |
| PG1_PENGU3L_USDT_pad30 | PENGU3L_USDT | base | 70.00% | 600.00 | 591.37 | -1.44% | nan% | 73.43 | -2175.06 | 3.90 | 2.73 | 1.84 | 10175 | SYNTHETIC_GATE_ETF_WINDOW |
| PG1_PENGU3L_USDT_pad30 | PENGU3L_USDT | conservative | 0.00% | 600.00 | 595.99 | -0.67% | nan% | 67.39 | -1548.65 | 3.31 | 0.00 | 1.66 | 10175 | SYNTHETIC_GATE_ETF_WINDOW |
| PG1_PENGU3L_USDT_pad30 | PENGU3L_USDT | conservative | 70.00% | 600.00 | 595.99 | -0.67% | nan% | 67.39 | -1548.65 | 3.31 | 2.32 | 1.66 | 10175 | SYNTHETIC_GATE_ETF_WINDOW |
| PG2_PENGU3L_USDT_pad15 | PENGU3L_USDT | base | 0.00% | 600.00 | 10334.12 | 1622.35% | nan% | 83.06 | 8738.33 | 2.63 | 0.00 | 152.62 | 46893 | REAL_GATE_ETF_WINDOW |
| PG2_PENGU3L_USDT_pad15 | PENGU3L_USDT | base | 70.00% | 600.00 | 10334.12 | 1622.35% | nan% | 83.06 | 8738.33 | 2.63 | 1.84 | 152.62 | 46893 | REAL_GATE_ETF_WINDOW |
| PG2_PENGU3L_USDT_pad15 | PENGU3L_USDT | conservative | 0.00% | 600.00 | 10315.04 | 1619.17% | nan% | 66.66 | 9160.66 | 1.64 | 0.00 | 155.31 | 46893 | REAL_GATE_ETF_WINDOW |
| PG2_PENGU3L_USDT_pad15 | PENGU3L_USDT | conservative | 70.00% | 600.00 | 10315.04 | 1619.17% | nan% | 66.66 | 9160.66 | 1.64 | 1.15 | 155.31 | 46893 | REAL_GATE_ETF_WINDOW |
| PP1_PUMP3L_USDT_pad30 | PUMP3L_USDT | base | 0.00% | 300.00 | 328.22 | 9.41% | nan% | 39.66 | -1422.49 | 3.25 | 0.00 | 3.07 | 17946 | REAL_GATE_ETF_WINDOW |
| PP1_PUMP3L_USDT_pad30 | PUMP3L_USDT | base | 70.00% | 300.00 | 328.22 | 9.41% | nan% | 39.66 | -1422.49 | 3.25 | 2.28 | 3.07 | 17946 | REAL_GATE_ETF_WINDOW |
| PP1_PUMP3L_USDT_pad30 | PUMP3L_USDT | conservative | 0.00% | 300.00 | 311.99 | 4.00% | nan% | 21.62 | -588.61 | 1.79 | 0.00 | 2.43 | 17946 | REAL_GATE_ETF_WINDOW |
| PP1_PUMP3L_USDT_pad30 | PUMP3L_USDT | conservative | 70.00% | 300.00 | 311.99 | 4.00% | nan% | 21.62 | -588.61 | 1.79 | 1.25 | 2.43 | 17946 | REAL_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3L_USDT_pad15 | SOXL3L_USDT | base | 0.00% | 1500.00 | 1469.54 | -2.03% | nan% | 251.80 | -8046.44 | 17.95 | 0.00 | 12.57 | 26206 | SYNTHETIC_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3L_USDT_pad15 | SOXL3L_USDT | base | 70.00% | 1500.00 | 1469.54 | -2.03% | nan% | 251.80 | -8046.44 | 17.95 | 12.56 | 12.57 | 26206 | SYNTHETIC_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3L_USDT_pad15 | SOXL3L_USDT | conservative | 0.00% | 1500.00 | 1559.70 | 3.98% | nan% | 187.32 | -4622.13 | 10.37 | 0.00 | 6.51 | 26206 | SYNTHETIC_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3L_USDT_pad15 | SOXL3L_USDT | conservative | 70.00% | 1500.00 | 1559.70 | 3.98% | nan% | 187.32 | -4622.13 | 10.37 | 7.26 | 6.51 | 26206 | SYNTHETIC_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3S_USDT_pad30 | SOXL3S_USDT | base | 0.00% | 500.00 | 616.42 | 23.28% | nan% | 128.13 | -8437.70 | 14.84 | 0.00 | 4.17 | 20366 | SYNTHETIC_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3S_USDT_pad30 | SOXL3S_USDT | base | 70.00% | 500.00 | 616.42 | 23.28% | nan% | 128.13 | -8437.70 | 14.84 | 10.38 | 4.17 | 20366 | SYNTHETIC_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3S_USDT_pad30 | SOXL3S_USDT | conservative | 0.00% | 500.00 | 605.80 | 21.16% | nan% | 116.41 | -7339.23 | 13.17 | 0.00 | 4.01 | 20366 | SYNTHETIC_GATE_ETF_WINDOW |
| SX_FAIL_SOXL3S_USDT_pad30 | SOXL3S_USDT | conservative | 70.00% | 500.00 | 605.80 | 21.16% | nan% | 116.41 | -7339.23 | 13.17 | 9.22 | 4.01 | 20366 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3L_USDT_pad15 | SNXX3L_USDT | base | 0.00% | 600.00 | 703.37 | 17.23% | nan% | 147.47 | -4165.42 | 9.24 | 0.00 | 1.85 | 15309 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3L_USDT_pad15 | SNXX3L_USDT | base | 70.00% | 600.00 | 703.37 | 17.23% | nan% | 147.47 | -4165.42 | 9.24 | 6.47 | 1.85 | 15309 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3L_USDT_pad15 | SNXX3L_USDT | conservative | 0.00% | 600.00 | 690.32 | 15.05% | nan% | 106.11 | -2032.08 | 5.29 | 0.00 | 0.91 | 15309 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3L_USDT_pad15 | SNXX3L_USDT | conservative | 70.00% | 600.00 | 690.32 | 15.05% | nan% | 106.11 | -2032.08 | 5.29 | 3.71 | 0.91 | 15309 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3S_USDT_pad30 | SNXX3S_USDT | base | 0.00% | 500.00 | 239.45 | -52.11% | nan% | 42.67 | -1586.29 | 2.88 | 0.00 | 0.76 | 26145 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3S_USDT_pad30 | SNXX3S_USDT | base | 70.00% | 500.00 | 239.45 | -52.11% | nan% | 42.67 | -1586.29 | 2.88 | 2.01 | 0.76 | 26145 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3S_USDT_pad30 | SNXX3S_USDT | conservative | 0.00% | 500.00 | 371.10 | -25.78% | nan% | 34.72 | -798.27 | 1.65 | 0.00 | 0.43 | 26145 | SYNTHETIC_GATE_ETF_WINDOW |
| NX_FAIL_SNXX3S_USDT_pad30 | SNXX3S_USDT | conservative | 70.00% | 500.00 | 371.10 | -25.78% | nan% | 34.72 | -798.27 | 1.65 | 1.15 | 0.43 | 26145 | SYNTHETIC_GATE_ETF_WINDOW |
| BX_FAIL_BTC3L_USDT_pad30 | BTC3L_USDT | base | 0.00% | 300.00 | 305.54 | 1.85% | nan% | 9.04 | -425.03 | 1.08 | 0.00 | 4.72 | 7650 | REAL_GATE_ETF_WINDOW |
| BX_FAIL_BTC3L_USDT_pad30 | BTC3L_USDT | base | 70.00% | 300.00 | 305.54 | 1.85% | nan% | 9.04 | -425.03 | 1.08 | 0.75 | 4.72 | 7650 | REAL_GATE_ETF_WINDOW |
| BX_FAIL_BTC3L_USDT_pad30 | BTC3L_USDT | conservative | 0.00% | 300.00 | 300.56 | 0.19% | nan% | 3.11 | -108.56 | 0.43 | 0.00 | 3.79 | 7650 | REAL_GATE_ETF_WINDOW |
| BX_FAIL_BTC3L_USDT_pad30 | BTC3L_USDT | conservative | 70.00% | 300.00 | 300.56 | 0.19% | nan% | 3.11 | -108.56 | 0.43 | 0.30 | 3.79 | 7650 | REAL_GATE_ETF_WINDOW |
| EX_FAIL_ETH3L_USDT_pad30 | ETH3L_USDT | base | 0.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 0.00 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| EX_FAIL_ETH3L_USDT_pad30 | ETH3L_USDT | base | 70.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 2.49 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| EX_FAIL_ETH3L_USDT_pad30 | ETH3L_USDT | conservative | 0.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 0.00 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| EX_FAIL_ETH3L_USDT_pad30 | ETH3L_USDT | conservative | 70.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 1.42 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| LX_FAIL_SOL3L_USDT_pad30 | SOL3L_USDT | base | 0.00% | 1050.00 | 1133.01 | 7.91% | nan% | 85.21 | -3227.82 | 7.44 | 0.00 | 12.34 | 23149 | REAL_GATE_ETF_WINDOW |
| LX_FAIL_SOL3L_USDT_pad30 | SOL3L_USDT | base | 70.00% | 1050.00 | 1133.01 | 7.91% | nan% | 85.21 | -3227.82 | 7.44 | 5.21 | 12.34 | 23149 | REAL_GATE_ETF_WINDOW |
| LX_FAIL_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 1107.01 | 5.43% | nan% | 56.04 | -1483.65 | 4.34 | 0.00 | 10.51 | 23149 | REAL_GATE_ETF_WINDOW |
| LX_FAIL_SOL3L_USDT_pad30 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 1107.01 | 5.43% | nan% | 56.04 | -1483.65 | 4.34 | 3.04 | 10.51 | 23149 | REAL_GATE_ETF_WINDOW |
| PGX_FAIL_PENGU3L_USDT_pad15 | PENGU3L_USDT | base | 0.00% | 600.00 | 1293.52 | 115.59% | nan% | 105.30 | -1203.32 | 4.76 | 0.00 | 79.51 | 65626 | SYNTHETIC_GATE_ETF_WINDOW |
| PGX_FAIL_PENGU3L_USDT_pad15 | PENGU3L_USDT | base | 70.00% | 600.00 | 1293.52 | 115.59% | nan% | 105.30 | -1203.32 | 4.76 | 3.33 | 79.51 | 65626 | SYNTHETIC_GATE_ETF_WINDOW |
| PGX_FAIL_PENGU3L_USDT_pad15 | PENGU3L_USDT | conservative | 0.00% | 600.00 | 662.79 | 10.47% | nan% | 79.76 | -1069.91 | 2.91 | 0.00 | 45.54 | 65626 | SYNTHETIC_GATE_ETF_WINDOW |
| PGX_FAIL_PENGU3L_USDT_pad15 | PENGU3L_USDT | conservative | 70.00% | 600.00 | 662.79 | 10.47% | nan% | 79.76 | -1069.91 | 2.91 | 2.03 | 45.54 | 65626 | SYNTHETIC_GATE_ETF_WINDOW |
| PPX_FAIL_PUMP3L_USDT_pad15 | PUMP3L_USDT | base | 0.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.00 | 1.44 | 75501 | REAL_GATE_ETF_WINDOW |
| PPX_FAIL_PUMP3L_USDT_pad15 | PUMP3L_USDT | base | 70.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.71 | 1.44 | 75501 | REAL_GATE_ETF_WINDOW |
| PPX_FAIL_PUMP3L_USDT_pad15 | PUMP3L_USDT | conservative | 0.00% | 300.00 | 355.38 | 18.46% | nan% | 30.99 | -194.42 | 0.63 | 0.00 | 1.29 | 75501 | REAL_GATE_ETF_WINDOW |
| PPX_FAIL_PUMP3L_USDT_pad15 | PUMP3L_USDT | conservative | 70.00% | 300.00 | 355.38 | 18.46% | nan% | 30.99 | -194.42 | 0.63 | 0.44 | 1.29 | 75501 | REAL_GATE_ETF_WINDOW |
| E_V2024_ETH3L_USDT_pad15 | ETH3L_USDT | base | 0.00% | 750.00 | 724.03 | -3.46% | nan% | 18.53 | -901.23 | 2.37 | 0.00 | 10.37 | 7747 | REAL_GATE_ETF_WINDOW |
| E_V2024_ETH3L_USDT_pad15 | ETH3L_USDT | base | 70.00% | 750.00 | 724.03 | -3.46% | nan% | 18.53 | -901.23 | 2.37 | 1.66 | 10.37 | 7747 | REAL_GATE_ETF_WINDOW |
| E_V2024_ETH3L_USDT_pad15 | ETH3L_USDT | conservative | 0.00% | 750.00 | 718.20 | -4.24% | nan% | 7.24 | -292.49 | 1.07 | 0.00 | 7.71 | 7747 | REAL_GATE_ETF_WINDOW |
| E_V2024_ETH3L_USDT_pad15 | ETH3L_USDT | conservative | 70.00% | 750.00 | 718.20 | -4.24% | nan% | 7.24 | -292.49 | 1.07 | 0.75 | 7.71 | 7747 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_v_reversal_45d_192 | SOXL3L_USDT | base | 0.00% | 1500.00 | 1548.73 | 3.25% | nan% | 258.93 | -8400.05 | 18.70 | 0.00 | 14.23 | 28024 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_v_reversal_45d_192 | SOXL3L_USDT | base | 70.00% | 1500.00 | 1548.73 | 3.25% | nan% | 258.93 | -8400.05 | 18.70 | 13.09 | 14.23 | 28024 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_v_reversal_45d_192 | SOXL3L_USDT | conservative | 0.00% | 1500.00 | 1601.77 | 6.78% | nan% | 193.26 | -4923.91 | 11.01 | 0.00 | 7.39 | 28024 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_v_reversal_45d_192 | SOXL3L_USDT | conservative | 70.00% | 1500.00 | 1601.77 | 6.78% | nan% | 193.26 | -4923.91 | 11.01 | 7.71 | 7.39 | 28024 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_drop_then_rise_45d_24 | SOXL3L_USDT | base | 0.00% | 1500.00 | 1275.72 | -14.95% | nan% | 226.45 | -6611.01 | 15.19 | 0.00 | 10.18 | 22740 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_drop_then_rise_45d_24 | SOXL3L_USDT | base | 70.00% | 1500.00 | 1275.72 | -14.95% | nan% | 226.45 | -6611.01 | 15.19 | 10.63 | 10.18 | 22740 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_drop_then_rise_45d_24 | SOXL3L_USDT | conservative | 0.00% | 1500.00 | 1454.60 | -3.03% | nan% | 166.38 | -3450.51 | 8.04 | 0.00 | 5.18 | 22740 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_drop_then_rise_45d_24 | SOXL3L_USDT | conservative | 70.00% | 1500.00 | 1454.60 | -3.03% | nan% | 166.38 | -3450.51 | 8.04 | 5.63 | 5.18 | 22740 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_high_vol_chop_21d_768 | SOXL3L_USDT | base | 0.00% | 1500.00 | 1215.51 | -18.97% | nan% | 17.14 | -1164.53 | 2.66 | 0.00 | 12.02 | 21715 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_high_vol_chop_21d_768 | SOXL3L_USDT | base | 70.00% | 1500.00 | 1215.51 | -18.97% | nan% | 17.14 | -1164.53 | 2.66 | 1.86 | 12.02 | 21715 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_high_vol_chop_21d_768 | SOXL3L_USDT | conservative | 0.00% | 1500.00 | 1278.77 | -14.75% | nan% | 10.80 | -767.39 | 1.74 | 0.00 | 7.91 | 21715 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_high_vol_chop_21d_768 | SOXL3L_USDT | conservative | 70.00% | 1500.00 | 1278.77 | -14.75% | nan% | 10.80 | -767.39 | 1.74 | 1.22 | 7.91 | 21715 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_trend_down_30d_144 | SOXL3L_USDT | base | 0.00% | 1500.00 | 538.28 | -64.11% | nan% | 9.35 | -1475.06 | 1.90 | 0.00 | 6.04 | 40246 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_trend_down_30d_144 | SOXL3L_USDT | base | 70.00% | 1500.00 | 538.28 | -64.11% | nan% | 9.35 | -1475.06 | 1.90 | 1.33 | 6.04 | 40246 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_trend_down_30d_144 | SOXL3L_USDT | conservative | 0.00% | 1500.00 | 697.81 | -53.48% | nan% | 4.27 | -968.13 | 1.18 | 0.00 | 4.81 | 40246 | REAL_GATE_ETF_WINDOW |
| SOXL3L_USDT_trend_down_30d_144 | SOXL3L_USDT | conservative | 70.00% | 1500.00 | 697.81 | -53.48% | nan% | 4.27 | -968.13 | 1.18 | 0.83 | 4.81 | 40246 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_14d_492 | SOXL3S_USDT | base | 0.00% | 500.00 | 560.60 | 12.12% | nan% | 60.90 | -2578.57 | 5.23 | 0.00 | 0.30 | 12938 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_14d_492 | SOXL3S_USDT | base | 70.00% | 500.00 | 560.60 | 12.12% | nan% | 60.90 | -2578.57 | 5.23 | 3.66 | 0.30 | 12938 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_14d_492 | SOXL3S_USDT | conservative | 0.00% | 500.00 | 558.56 | 11.71% | nan% | 41.94 | -1233.67 | 2.92 | 0.00 | 0.37 | 12938 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_14d_492 | SOXL3S_USDT | conservative | 70.00% | 500.00 | 558.56 | 11.71% | nan% | 41.94 | -1233.67 | 2.92 | 2.04 | 0.37 | 12938 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_rise_then_fall_60d_12 | SOXL3S_USDT | base | 0.00% | 500.00 | 594.33 | 18.87% | nan% | 97.78 | -5807.58 | 10.47 | 0.00 | 3.47 | 15862 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_rise_then_fall_60d_12 | SOXL3S_USDT | base | 70.00% | 500.00 | 594.33 | 18.87% | nan% | 97.78 | -5807.58 | 10.47 | 7.33 | 3.47 | 15862 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_rise_then_fall_60d_12 | SOXL3S_USDT | conservative | 0.00% | 500.00 | 584.90 | 16.98% | nan% | 88.26 | -4995.45 | 9.12 | 0.00 | 3.37 | 15862 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_rise_then_fall_60d_12 | SOXL3S_USDT | conservative | 70.00% | 500.00 | 584.90 | 16.98% | nan% | 88.26 | -4995.45 | 9.12 | 6.38 | 3.37 | 15862 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_drop_then_rise_60d_108 | SOXL3S_USDT | base | 0.00% | 500.00 | 619.17 | 23.83% | nan% | 128.01 | -8424.51 | 14.81 | 0.00 | 4.07 | 19781 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_drop_then_rise_60d_108 | SOXL3S_USDT | base | 70.00% | 500.00 | 619.17 | 23.83% | nan% | 128.01 | -8424.51 | 14.81 | 10.37 | 4.07 | 19781 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_drop_then_rise_60d_108 | SOXL3S_USDT | conservative | 0.00% | 500.00 | 608.35 | 21.67% | nan% | 116.37 | -7332.88 | 13.16 | 0.00 | 3.92 | 19781 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_drop_then_rise_60d_108 | SOXL3S_USDT | conservative | 70.00% | 500.00 | 608.35 | 21.67% | nan% | 116.37 | -7332.88 | 13.16 | 9.21 | 3.92 | 19781 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_30d_828 | SOXL3S_USDT | base | 0.00% | 500.00 | 272.46 | -45.51% | nan% | 51.93 | -2570.22 | 4.29 | 0.00 | 4.55 | 31818 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_30d_828 | SOXL3S_USDT | base | 70.00% | 500.00 | 272.46 | -45.51% | nan% | 51.93 | -2570.22 | 4.29 | 3.00 | 4.55 | 31818 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_30d_828 | SOXL3S_USDT | conservative | 0.00% | 500.00 | 320.53 | -35.89% | nan% | 46.79 | -1913.45 | 3.51 | 0.00 | 3.67 | 31818 | REAL_GATE_ETF_WINDOW |
| SOXL3S_USDT_v_reversal_30d_828 | SOXL3S_USDT | conservative | 70.00% | 500.00 | 320.53 | -35.89% | nan% | 46.79 | -1913.45 | 3.51 | 2.46 | 3.67 | 31818 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_v_reversal_14d_132 | SNXX3L_USDT | base | 0.00% | 600.00 | 735.11 | 22.52% | nan% | 114.59 | -2718.67 | 5.95 | 0.00 | 1.61 | 16400 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_v_reversal_14d_132 | SNXX3L_USDT | base | 70.00% | 600.00 | 735.11 | 22.52% | nan% | 114.59 | -2718.67 | 5.95 | 4.16 | 1.61 | 16400 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_v_reversal_14d_132 | SNXX3L_USDT | conservative | 0.00% | 600.00 | 709.03 | 18.17% | nan% | 87.75 | -1489.18 | 3.44 | 0.00 | 0.85 | 16400 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_v_reversal_14d_132 | SNXX3L_USDT | conservative | 70.00% | 600.00 | 709.03 | 18.17% | nan% | 87.75 | -1489.18 | 3.44 | 2.41 | 0.85 | 16400 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_drop_then_rise_14d_72 | SNXX3L_USDT | base | 0.00% | 600.00 | 730.97 | 21.83% | nan% | 118.24 | -2899.72 | 6.29 | 0.00 | 1.89 | 15491 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_drop_then_rise_14d_72 | SNXX3L_USDT | base | 70.00% | 600.00 | 730.97 | 21.83% | nan% | 118.24 | -2899.72 | 6.29 | 4.40 | 1.89 | 15491 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_drop_then_rise_14d_72 | SNXX3L_USDT | conservative | 0.00% | 600.00 | 703.66 | 17.28% | nan% | 90.21 | -1522.15 | 3.67 | 0.00 | 1.17 | 15491 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_drop_then_rise_14d_72 | SNXX3L_USDT | conservative | 70.00% | 600.00 | 703.66 | 17.28% | nan% | 90.21 | -1522.15 | 3.67 | 2.57 | 1.17 | 15491 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_high_vol_chop_21d_264 | SNXX3L_USDT | base | 0.00% | 600.00 | 694.34 | 15.72% | nan% | 98.33 | -2559.36 | 4.50 | 0.00 | 1.12 | 23372 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_high_vol_chop_21d_264 | SNXX3L_USDT | base | 70.00% | 600.00 | 694.34 | 15.72% | nan% | 98.33 | -2559.36 | 4.50 | 3.15 | 1.12 | 23372 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_high_vol_chop_21d_264 | SNXX3L_USDT | conservative | 0.00% | 600.00 | 685.58 | 14.26% | nan% | 88.29 | -1737.84 | 3.55 | 0.00 | 1.10 | 23372 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_high_vol_chop_21d_264 | SNXX3L_USDT | conservative | 70.00% | 600.00 | 685.58 | 14.26% | nan% | 88.29 | -1737.84 | 3.55 | 2.48 | 1.10 | 23372 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_rise_then_fall_14d_0 | SNXX3L_USDT | base | 0.00% | 600.00 | 703.37 | 17.23% | nan% | 147.47 | -4165.42 | 9.24 | 0.00 | 1.85 | 15309 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_rise_then_fall_14d_0 | SNXX3L_USDT | base | 70.00% | 600.00 | 703.37 | 17.23% | nan% | 147.47 | -4165.42 | 9.24 | 6.47 | 1.85 | 15309 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_rise_then_fall_14d_0 | SNXX3L_USDT | conservative | 0.00% | 600.00 | 690.32 | 15.05% | nan% | 106.11 | -2032.08 | 5.29 | 0.00 | 0.91 | 15309 | REAL_GATE_ETF_WINDOW |
| SNXX3L_USDT_rise_then_fall_14d_0 | SNXX3L_USDT | conservative | 70.00% | 600.00 | 690.32 | 15.05% | nan% | 106.11 | -2032.08 | 5.29 | 3.71 | 0.91 | 15309 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_v_reversal_30d_0 | SNXX3S_USDT | base | 0.00% | 500.00 | 239.08 | -52.18% | nan% | 42.67 | -1586.66 | 2.88 | 0.00 | 0.77 | 26516 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_v_reversal_30d_0 | SNXX3S_USDT | base | 70.00% | 500.00 | 239.08 | -52.18% | nan% | 42.67 | -1586.66 | 2.88 | 2.01 | 0.77 | 26516 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_v_reversal_30d_0 | SNXX3S_USDT | conservative | 0.00% | 500.00 | 370.89 | -25.82% | nan% | 34.72 | -798.47 | 1.65 | 0.00 | 0.44 | 26516 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_v_reversal_30d_0 | SNXX3S_USDT | conservative | 70.00% | 500.00 | 370.89 | -25.82% | nan% | 34.72 | -798.47 | 1.65 | 1.15 | 0.44 | 26516 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_drop_then_rise_21d_120 | SNXX3S_USDT | base | 0.00% | 500.00 | 280.32 | -43.94% | nan% | 35.78 | -1077.40 | 1.88 | 0.00 | 1.30 | 17783 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_drop_then_rise_21d_120 | SNXX3S_USDT | base | 70.00% | 500.00 | 280.32 | -43.94% | nan% | 35.78 | -1077.40 | 1.88 | 1.32 | 1.30 | 17783 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_drop_then_rise_21d_120 | SNXX3S_USDT | conservative | 0.00% | 500.00 | 362.21 | -27.56% | nan% | 31.50 | -668.45 | 1.20 | 0.00 | 0.86 | 17783 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_drop_then_rise_21d_120 | SNXX3S_USDT | conservative | 70.00% | 500.00 | 362.21 | -27.56% | nan% | 31.50 | -668.45 | 1.20 | 0.84 | 0.86 | 17783 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_trend_down_21d_12 | SNXX3S_USDT | base | 0.00% | 500.00 | 238.07 | -52.39% | nan% | 42.67 | -1587.71 | 2.88 | 0.00 | 0.73 | 18782 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_trend_down_21d_12 | SNXX3S_USDT | base | 70.00% | 500.00 | 238.07 | -52.39% | nan% | 42.67 | -1587.71 | 2.88 | 2.01 | 0.73 | 18782 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_trend_down_21d_12 | SNXX3S_USDT | conservative | 0.00% | 500.00 | 370.33 | -25.93% | nan% | 34.72 | -799.06 | 1.65 | 0.00 | 0.42 | 18782 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_trend_down_21d_12 | SNXX3S_USDT | conservative | 70.00% | 500.00 | 370.33 | -25.93% | nan% | 34.72 | -799.06 | 1.65 | 1.15 | 0.42 | 18782 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_rise_then_fall_21d_0 | SNXX3S_USDT | base | 0.00% | 500.00 | 238.07 | -52.39% | nan% | 42.67 | -1587.71 | 2.88 | 0.00 | 0.73 | 18782 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_rise_then_fall_21d_0 | SNXX3S_USDT | base | 70.00% | 500.00 | 238.07 | -52.39% | nan% | 42.67 | -1587.71 | 2.88 | 2.01 | 0.73 | 18782 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_rise_then_fall_21d_0 | SNXX3S_USDT | conservative | 0.00% | 500.00 | 370.33 | -25.93% | nan% | 34.72 | -799.06 | 1.65 | 0.00 | 0.42 | 18782 | REAL_GATE_ETF_WINDOW |
| SNXX3S_USDT_rise_then_fall_21d_0 | SNXX3S_USDT | conservative | 70.00% | 500.00 | 370.33 | -25.93% | nan% | 34.72 | -799.06 | 1.65 | 1.15 | 0.42 | 18782 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_3792 | BTC3L_USDT | base | 0.00% | 300.00 | 324.04 | 8.01% | nan% | 22.76 | -549.66 | 1.34 | 0.00 | 2.93 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_3792 | BTC3L_USDT | base | 70.00% | 300.00 | 324.04 | 8.01% | nan% | 22.76 | -549.66 | 1.34 | 0.94 | 2.93 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_3792 | BTC3L_USDT | conservative | 0.00% | 300.00 | 318.62 | 6.21% | nan% | 16.80 | -300.63 | 0.69 | 0.00 | 2.59 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_3792 | BTC3L_USDT | conservative | 70.00% | 300.00 | 318.62 | 6.21% | nan% | 16.80 | -300.63 | 0.69 | 0.48 | 2.59 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_288 | BTC3L_USDT | base | 0.00% | 300.00 | 282.35 | -5.88% | nan% | 12.40 | -509.64 | 1.21 | 0.00 | 4.96 | 27096 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_288 | BTC3L_USDT | base | 70.00% | 300.00 | 282.35 | -5.88% | nan% | 12.40 | -509.64 | 1.21 | 0.84 | 4.96 | 27096 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_288 | BTC3L_USDT | conservative | 0.00% | 300.00 | 285.15 | -4.95% | nan% | 7.34 | -183.54 | 0.62 | 0.00 | 3.32 | 27096 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_288 | BTC3L_USDT | conservative | 70.00% | 300.00 | 285.15 | -4.95% | nan% | 7.34 | -183.54 | 0.62 | 0.43 | 3.32 | 27096 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_3504 | BTC3L_USDT | base | 0.00% | 300.00 | 324.04 | 8.01% | nan% | 22.76 | -549.66 | 1.34 | 0.00 | 2.93 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_3504 | BTC3L_USDT | base | 70.00% | 300.00 | 324.04 | 8.01% | nan% | 22.76 | -549.66 | 1.34 | 0.94 | 2.93 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_3504 | BTC3L_USDT | conservative | 0.00% | 300.00 | 318.62 | 6.21% | nan% | 16.80 | -300.63 | 0.69 | 0.00 | 2.59 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_drop_then_rise_90d_3504 | BTC3L_USDT | conservative | 70.00% | 300.00 | 318.62 | 6.21% | nan% | 16.80 | -300.63 | 0.69 | 0.48 | 2.59 | 10770 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_14736 | BTC3L_USDT | base | 0.00% | 300.00 | 293.82 | -2.06% | nan% | 10.24 | -548.31 | 1.17 | 0.00 | 3.92 | 52949 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_14736 | BTC3L_USDT | base | 70.00% | 300.00 | 293.82 | -2.06% | nan% | 10.24 | -548.31 | 1.17 | 0.82 | 3.92 | 52949 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_14736 | BTC3L_USDT | conservative | 0.00% | 300.00 | 291.75 | -2.75% | nan% | 8.40 | -466.05 | 0.98 | 0.00 | 3.73 | 52949 | REAL_GATE_ETF_WINDOW |
| BTC3L_USDT_v_reversal_90d_14736 | BTC3L_USDT | conservative | 70.00% | 300.00 | 291.75 | -2.75% | nan% | 8.40 | -466.05 | 0.98 | 0.69 | 3.73 | 52949 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_3756 | ETH3L_USDT | base | 0.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 0.00 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_3756 | ETH3L_USDT | base | 70.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 2.49 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_3756 | ETH3L_USDT | conservative | 0.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 0.00 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_3756 | ETH3L_USDT | conservative | 70.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 1.42 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_5964 | ETH3L_USDT | base | 0.00% | 750.00 | 805.54 | 7.41% | nan% | 60.16 | -3588.33 | 6.56 | 0.00 | 11.69 | 24683 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_5964 | ETH3L_USDT | base | 70.00% | 750.00 | 805.54 | 7.41% | nan% | 60.16 | -3588.33 | 6.56 | 4.59 | 11.69 | 24683 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_5964 | ETH3L_USDT | conservative | 0.00% | 750.00 | 792.15 | 5.62% | nan% | 44.64 | -1844.69 | 4.82 | 0.00 | 10.19 | 24683 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_v_reversal_90d_5964 | ETH3L_USDT | conservative | 70.00% | 750.00 | 792.15 | 5.62% | nan% | 44.64 | -1844.69 | 4.82 | 3.37 | 10.19 | 24683 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_90d_4440 | ETH3L_USDT | base | 0.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 0.00 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_90d_4440 | ETH3L_USDT | base | 70.00% | 750.00 | 724.60 | -3.39% | nan% | 37.39 | -1578.08 | 3.56 | 2.49 | 9.36 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_90d_4440 | ETH3L_USDT | conservative | 0.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 0.00 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_90d_4440 | ETH3L_USDT | conservative | 70.00% | 750.00 | 729.04 | -2.79% | nan% | 24.40 | -802.01 | 2.03 | 1.42 | 6.59 | 15287 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_60d_6600 | ETH3L_USDT | base | 0.00% | 750.00 | 805.54 | 7.41% | nan% | 60.16 | -3588.33 | 6.56 | 0.00 | 11.69 | 24683 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_60d_6600 | ETH3L_USDT | base | 70.00% | 750.00 | 805.54 | 7.41% | nan% | 60.16 | -3588.33 | 6.56 | 4.59 | 11.69 | 24683 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_60d_6600 | ETH3L_USDT | conservative | 0.00% | 750.00 | 792.15 | 5.62% | nan% | 44.64 | -1844.69 | 4.82 | 0.00 | 10.19 | 24683 | REAL_GATE_ETF_WINDOW |
| ETH3L_USDT_drop_then_rise_60d_6600 | ETH3L_USDT | conservative | 70.00% | 750.00 | 792.15 | 5.62% | nan% | 44.64 | -1844.69 | 4.82 | 3.37 | 10.19 | 24683 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_v_reversal_90d_5328 | SOL3L_USDT | base | 0.00% | 1050.00 | 1133.01 | 7.91% | nan% | 85.21 | -3227.82 | 7.44 | 0.00 | 12.34 | 23149 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_v_reversal_90d_5328 | SOL3L_USDT | base | 70.00% | 1050.00 | 1133.01 | 7.91% | nan% | 85.21 | -3227.82 | 7.44 | 5.21 | 12.34 | 23149 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_v_reversal_90d_5328 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 1107.01 | 5.43% | nan% | 56.04 | -1483.65 | 4.34 | 0.00 | 10.51 | 23149 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_v_reversal_90d_5328 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 1107.01 | 5.43% | nan% | 56.04 | -1483.65 | 4.34 | 3.04 | 10.51 | 23149 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_drop_then_rise_90d_4884 | SOL3L_USDT | base | 0.00% | 1050.00 | 1139.91 | 8.56% | nan% | 83.83 | -3138.64 | 7.26 | 0.00 | 11.88 | 22591 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_drop_then_rise_90d_4884 | SOL3L_USDT | base | 70.00% | 1050.00 | 1139.91 | 8.56% | nan% | 83.83 | -3138.64 | 7.26 | 5.09 | 11.88 | 22591 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_drop_then_rise_90d_4884 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 1114.05 | 6.10% | nan% | 55.15 | -1433.06 | 4.23 | 0.00 | 10.07 | 22591 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_drop_then_rise_90d_4884 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 1114.05 | 6.10% | nan% | 55.15 | -1433.06 | 4.23 | 2.96 | 10.07 | 22591 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_trend_down_90d_4752 | SOL3L_USDT | base | 0.00% | 1050.00 | 1056.72 | 0.64% | nan% | 51.86 | -2505.92 | 6.09 | 0.00 | 10.06 | 18497 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_trend_down_90d_4752 | SOL3L_USDT | base | 70.00% | 1050.00 | 1056.72 | 0.64% | nan% | 51.86 | -2505.92 | 6.09 | 4.26 | 10.06 | 18497 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_trend_down_90d_4752 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 1036.56 | -1.28% | nan% | 28.47 | -1100.81 | 3.50 | 0.00 | 8.36 | 18497 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_trend_down_90d_4752 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 1036.56 | -1.28% | nan% | 28.47 | -1100.81 | 3.50 | 2.45 | 8.36 | 18497 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_rise_then_fall_90d_4740 | SOL3L_USDT | base | 0.00% | 1050.00 | 1056.72 | 0.64% | nan% | 51.86 | -2505.92 | 6.09 | 0.00 | 10.06 | 18497 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_rise_then_fall_90d_4740 | SOL3L_USDT | base | 70.00% | 1050.00 | 1056.72 | 0.64% | nan% | 51.86 | -2505.92 | 6.09 | 4.26 | 10.06 | 18497 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_rise_then_fall_90d_4740 | SOL3L_USDT | conservative | 0.00% | 1050.00 | 1036.56 | -1.28% | nan% | 28.47 | -1100.81 | 3.50 | 0.00 | 8.36 | 18497 | REAL_GATE_ETF_WINDOW |
| SOL3L_USDT_rise_then_fall_90d_4740 | SOL3L_USDT | conservative | 70.00% | 1050.00 | 1036.56 | -1.28% | nan% | 28.47 | -1100.81 | 3.50 | 2.45 | 8.36 | 18497 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_1980 | PENGU3L_USDT | base | 0.00% | 600.00 | 1565.97 | 161.00% | nan% | 105.30 | -932.32 | 4.76 | 0.00 | 78.05 | 62636 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_1980 | PENGU3L_USDT | base | 70.00% | 600.00 | 1565.97 | 161.00% | nan% | 105.30 | -932.32 | 4.76 | 3.33 | 78.05 | 62636 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_1980 | PENGU3L_USDT | conservative | 0.00% | 600.00 | 674.46 | 12.41% | nan% | 79.76 | -1058.31 | 2.91 | 0.00 | 45.48 | 62636 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_1980 | PENGU3L_USDT | conservative | 70.00% | 600.00 | 674.46 | 12.41% | nan% | 79.76 | -1058.31 | 2.91 | 2.03 | 45.48 | 62636 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_v_reversal_60d_2868 | PENGU3L_USDT | base | 0.00% | 600.00 | 1293.52 | 115.59% | nan% | 105.30 | -1203.32 | 4.76 | 0.00 | 79.51 | 65626 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_v_reversal_60d_2868 | PENGU3L_USDT | base | 70.00% | 600.00 | 1293.52 | 115.59% | nan% | 105.30 | -1203.32 | 4.76 | 3.33 | 79.51 | 65626 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_v_reversal_60d_2868 | PENGU3L_USDT | conservative | 0.00% | 600.00 | 662.79 | 10.47% | nan% | 79.76 | -1069.91 | 2.91 | 0.00 | 45.54 | 65626 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_v_reversal_60d_2868 | PENGU3L_USDT | conservative | 70.00% | 600.00 | 662.79 | 10.47% | nan% | 79.76 | -1069.91 | 2.91 | 2.03 | 45.54 | 65626 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_high_vol_chop_90d_1776 | PENGU3L_USDT | base | 0.00% | 600.00 | 41925.73 | 6887.62% | nan% | 80.35 | 39486.36 | 4.64 | 0.00 | 73.52 | 39676 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_high_vol_chop_90d_1776 | PENGU3L_USDT | base | 70.00% | 600.00 | 41925.73 | 6887.62% | nan% | 80.35 | 39486.36 | 4.64 | 3.25 | 73.52 | 39676 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_high_vol_chop_90d_1776 | PENGU3L_USDT | conservative | 0.00% | 600.00 | 21001.32 | 3400.22% | nan% | 66.85 | 19300.41 | 2.85 | 0.00 | 45.29 | 39676 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_high_vol_chop_90d_1776 | PENGU3L_USDT | conservative | 70.00% | 600.00 | 21001.32 | 3400.22% | nan% | 66.85 | 19300.41 | 2.85 | 2.00 | 45.29 | 39676 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_7476 | PENGU3L_USDT | base | 0.00% | 600.00 | 601.10 | 0.18% | nan% | 37.93 | -1316.65 | 2.74 | 0.00 | 5.45 | 10828 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_7476 | PENGU3L_USDT | base | 70.00% | 600.00 | 601.10 | 0.18% | nan% | 37.93 | -1316.65 | 2.74 | 1.92 | 5.45 | 10828 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_7476 | PENGU3L_USDT | conservative | 0.00% | 600.00 | 597.67 | -0.39% | nan% | 28.58 | -714.29 | 1.84 | 0.00 | 5.03 | 10828 | REAL_GATE_ETF_WINDOW |
| PENGU3L_USDT_drop_then_rise_90d_7476 | PENGU3L_USDT | conservative | 70.00% | 600.00 | 597.67 | -0.39% | nan% | 28.58 | -714.29 | 1.84 | 1.29 | 5.03 | 10828 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_2484 | PUMP3L_USDT | base | 0.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.00 | 1.44 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_2484 | PUMP3L_USDT | base | 70.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.71 | 1.44 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_2484 | PUMP3L_USDT | conservative | 0.00% | 300.00 | 355.38 | 18.46% | nan% | 30.99 | -194.42 | 0.63 | 0.00 | 1.29 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_2484 | PUMP3L_USDT | conservative | 70.00% | 300.00 | 355.38 | 18.46% | nan% | 30.99 | -194.42 | 0.63 | 0.44 | 1.29 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_drop_then_rise_90d_2184 | PUMP3L_USDT | base | 0.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.00 | 1.44 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_drop_then_rise_90d_2184 | PUMP3L_USDT | base | 70.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.71 | 1.44 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_drop_then_rise_90d_2184 | PUMP3L_USDT | conservative | 0.00% | 300.00 | 355.38 | 18.46% | nan% | 30.99 | -194.42 | 0.63 | 0.00 | 1.29 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_drop_then_rise_90d_2184 | PUMP3L_USDT | conservative | 70.00% | 300.00 | 355.38 | 18.46% | nan% | 30.99 | -194.42 | 0.63 | 0.44 | 1.29 | 75501 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_high_vol_chop_90d_1968 | PUMP3L_USDT | base | 0.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.00 | 1.44 | 51803 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_high_vol_chop_90d_1968 | PUMP3L_USDT | base | 70.00% | 300.00 | 339.47 | 13.16% | nan% | 40.91 | -379.44 | 1.01 | 0.71 | 1.44 | 51803 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_high_vol_chop_90d_1968 | PUMP3L_USDT | conservative | 0.00% | 300.00 | 358.25 | 19.42% | nan% | 30.99 | -191.68 | 0.63 | 0.00 | 1.16 | 51803 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_high_vol_chop_90d_1968 | PUMP3L_USDT | conservative | 70.00% | 300.00 | 358.25 | 19.42% | nan% | 30.99 | -191.68 | 0.63 | 0.44 | 1.16 | 51803 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_7452 | PUMP3L_USDT | base | 0.00% | 300.00 | 328.22 | 9.41% | nan% | 39.66 | -1422.49 | 3.25 | 0.00 | 3.07 | 17946 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_7452 | PUMP3L_USDT | base | 70.00% | 300.00 | 328.22 | 9.41% | nan% | 39.66 | -1422.49 | 3.25 | 2.28 | 3.07 | 17946 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_7452 | PUMP3L_USDT | conservative | 0.00% | 300.00 | 311.99 | 4.00% | nan% | 21.62 | -588.61 | 1.79 | 0.00 | 2.43 | 17946 | REAL_GATE_ETF_WINDOW |
| PUMP3L_USDT_v_reversal_90d_7452 | PUMP3L_USDT | conservative | 70.00% | 300.00 | 311.99 | 4.00% | nan% | 21.62 | -588.61 | 1.79 | 1.25 | 2.43 | 17946 | REAL_GATE_ETF_WINDOW |

S→L 方向仓（S3 / REAL SOXLG+3L/3S，无网格）：

- planA_remaining_ov1: equity=11083.05 ret=10.83% S=667.09 L=609.45 stage=4 rev=True
- planA_remaining_ov0: equity=11083.05 ret=10.83% S=667.09 L=609.45 stage=4 rev=True
- planA_initial_ov1: equity=10873.62 ret=8.74% S=455.08 L=609.45 stage=4 rev=True
- planB_remaining_ov1: equity=11337.47 ret=13.37% S=909.32 L=626.14 stage=4 rev=True
- planC_remaining_ov1: equity=11521.15 ret=15.21% S=1563.24 L=0.00 stage=0 rev=True
- L_only_SOXL3L_2000: equity=12.68 ret=-99.37% S=n/a L=n/a stage=None rev=None

## 11–12. ETF 网格 vs 底层现货网格 vs 3 倍合约网格

底层现货网格只在 SOXLG/SNXXG 有逐笔时作为 **Benchmark**，不替代 3L PnL。
3 倍永续网格需要 funding / 强平 / 保证金；本次未下载合约资金费 tape，**Benchmark 5 标 INCOMPLETE**，不编造优势。

## 13. ETF 路径损耗

SOXL3L 是 3×SOXL，不是 9×SOX。SNXX3L 是 3×SNXX，不是 6×SNDK。
校准见 §4。Crypto 3L 未下载 BTC/ETH/SOL 现货逐笔（单月 40–150MB），衰减只在有 SOXLG/SNXXG 重叠处量化。

## 14. 返佣贡献

- SOXL3L_USDT: eq0=700.80 eq50=700.80 eq70=700.80 70-0=0.00 alive0=False mgmt×2=False slip×2=False miss20=False
- BTC3L_USDT: eq0=334.40 eq50=334.40 eq70=334.40 70-0=0.00 alive0=True mgmt×2=True slip×2=True miss20=True
- ETH3L_USDT: eq0=845.32 eq50=845.32 eq70=845.32 70-0=0.00 alive0=True mgmt×2=True slip×2=True miss20=True
- SOL3L_USDT: eq0=1179.32 eq50=1179.32 eq70=1179.32 70-0=0.00 alive0=True mgmt×2=True slip×2=True miss20=True
- PENGU3L_USDT: eq0=710.22 eq50=710.22 eq70=710.22 70-0=0.00 alive0=True mgmt×2=True slip×2=True miss20=True
- PUMP3L_USDT: eq0=398.93 eq50=398.93 eq70=398.93 70-0=0.00 alive0=True mgmt×2=True slip×2=True miss20=True

## 15. 最大回撤

统计样本最差 MDD：SOXL3L_USDT S3_SOXL3L_USDT_pad15 nan% equity=1228.34

## 16. 失败案例

进统计样本中亏损 100 / 240。
- SOXL3L_USDT SOXL3L_USDT_trend_down_30d_144 fill=base eq 1500.00→538.28 grid=9.35 inv=-1475.06
- SOXL3L_USDT SOXL3L_USDT_trend_down_30d_144 fill=base eq 1500.00→538.28 grid=9.35 inv=-1475.06
- SOXL3L_USDT SOXL3L_USDT_trend_down_30d_144 fill=conservative eq 1500.00→697.81 grid=4.27 inv=-968.13
- SOXL3L_USDT SOXL3L_USDT_trend_down_30d_144 fill=conservative eq 1500.00→697.81 grid=4.27 inv=-968.13
- SOXL3L_USDT SOXL3L_USDT_high_vol_chop_21d_768 fill=base eq 1500.00→1215.51 grid=17.14 inv=-1164.53
- SOXL3L_USDT SOXL3L_USDT_high_vol_chop_21d_768 fill=base eq 1500.00→1215.51 grid=17.14 inv=-1164.53
- SOL3L_USDT S3_SOL3L_USDT_pad30 fill=base eq 1050.00→776.07 grid=33.10 inv=-2386.26
- SOL3L_USDT S3_SOL3L_USDT_pad30 fill=base eq 1050.00→776.07 grid=33.10 inv=-2386.26
- SOXL3L_USDT S3_SOXL3L_USDT_pad15 fill=base eq 1500.00→1228.34 grid=261.02 inv=-8823.07
- SOXL3L_USDT S3_SOXL3L_USDT_pad15 fill=base eq 1500.00→1228.34 grid=261.02 inv=-8823.07
- SOL3L_USDT S3_SOL3L_USDT_pad30 fill=conservative eq 1050.00→788.04 grid=27.92 inv=-1934.80
- SOL3L_USDT S3_SOL3L_USDT_pad30 fill=conservative eq 1050.00→788.04 grid=27.92 inv=-1934.80

## 17. 参数平台

{
  "top": [
    {
      "symbol": "PENGU3L_USDT",
      "grid_n": 80,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "base",
      "median": 1.1558586844277579,
      "min": -0.014378263102817423,
      "max": 68.87621879690519,
      "count": 14
    },
    {
      "symbol": "SOXL3S_USDT",
      "grid_n": 48,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "base",
      "median": 0.21075155410322866,
      "min": -0.45508942153303766,
      "max": 0.23834523461919477,
      "count": 12
    },
    {
      "symbol": "SOXL3S_USDT",
      "grid_n": 48,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": 0.19070740358440452,
      "min": -0.3589310347697934,
      "max": 0.2171003046274187,
      "count": 12
    },
    {
      "symbol": "PUMP3L_USDT",
      "grid_n": 80,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": 0.1846131285917436,
      "min": 0.03996157859741145,
      "max": 0.19417470495925748,
      "count": 12
    },
    {
      "symbol": "SNXX3L_USDT",
      "grid_n": 64,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "base",
      "median": 0.1722887193118796,
      "min": -0.24837043569760064,
      "max": 0.22518728143409406,
      "count": 12
    },
    {
      "symbol": "SNXX3L_USDT",
      "grid_n": 64,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": 0.15053512800973867,
      "min": -0.1812984717142605,
      "max": 0.18171245762235877,
      "count": 12
    },
    {
      "symbol": "PUMP3L_USDT",
      "grid_n": 80,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "base",
      "median": 0.13156542687488204,
      "min": 0.09405166149919153,
      "max": 0.1315654268752231,
      "count": 12
    },
    {
      "symbol": "PENGU3L_USDT",
      "grid_n": 80,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": 0.10465484690614812,
      "min": -0.006688399741508588,
      "max": 34.002207818741226,
      "count": 14
    },
    {
      "symbol": "SOL3L_USDT",
      "grid_n": 64,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "base",
      "median": 0.04272709488543569,
      "min": -0.26088262109961535,
      "max": 0.08563025897384646,
      "count": 16
    },
    {
      "symbol": "SOL3L_USDT",
      "grid_n": 64,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": 0.02074760800456965,
      "min": -0.24948323679938222,
      "max": 0.06099552448108403,
      "count": 16
    },
    {
      "symbol": "BTC3L_USDT",
      "grid_n": 40,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "base",
      "median": 0.01845482563380263,
      "min": -0.058844440074590776,
      "max": 0.08011969320856838,
      "count": 14
    },
    {
      "symbol": "BTC3L_USDT",
      "grid_n": 40,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": 0.0018708737961499189,
      "min": -0.04951106385477144,
      "max": 0.06205510220093813,
      "count": 14
    },
    {
      "symbol": "ETH3L_USDT",
      "grid_n": 56,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": -0.027941540135910548,
      "min": -0.042397666540127776,
      "max": 0.056728744531483466,
      "count": 16
    },
    {
      "symbol": "ETH3L_USDT",
      "grid_n": 56,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "base",
      "median": -0.03386286325601773,
      "min": -0.03462102903796227,
      "max": 0.07405776147036836,
      "count": 16
    },
    {
      "symbol": "SOXL3L_USDT",
      "grid_n": 56,
      "range_mult": 1.0,
      "reanchor": "off",
      "fill_model": "conservative",
      "median": -0.04356565889835057,
      "min": -0.5347944228496374

## 18. Walk-forward

Train = 2024 REAL crypto ETF 窗口；Test = 2025 REAL；2026 **不参与选参**。

```
{
  "status": "ok",
  "selected_on_2024_only": {
    "grid_n": 64,
    "range_mult": 1.0,
    "reanchor": "off",
    "fill_model": "conservative",
    "median": 0.009402638604382507,
    "min": -0.03549107205144386
  },
  "2025_median": 0.07905781556113567,
  "2025_min": -0.03386286325601773,
  "n_2024": 32,
  "n_2025": 88,
  "n_2026_held_out": 120,
  "note": "2026 rows reported but not used for selection."
}
```

## 19. Monte Carlo

```
{
  "BTC3L_USDT": {
    "1": {
      "n_paths": 1000,
      "block_days": 1,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "3": {
      "n_paths": 1000,
      "block_days": 3,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "5": {
      "n_paths": 1000,
      "block_days": 5,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "point_last90": {
      "final_equity": 336.1247782816208,
      "ret": 0.12041592760540265
    }
  },
  "SOXL3L_USDT": {
    "1": {
      "n_paths": 1000,
      "block_days": 1,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "3": {
      "n_paths": 1000,
      "block_days": 3,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "5": {
      "n_paths": 1000,
      "block_days": 5,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "point_last90": {
      "final_equity": 490.5363430267833,
      "ret": -0.6729757713154778
    }
  },
  "SOL3L_USDT": {
    "1": {
      "n_paths": 1000,
      "block_days": 1,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "3": {
      "n_paths": 1000,
      "block_days": 3,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "5": {
      "n_paths": 1000,
      "block_days": 5,
      "p05": NaN,
      "p25": NaN,
      "p50": NaN,
      "p75": NaN,
      "p95": NaN,
      "p_loss": 0.0,
      "p_loss_10": 0.0,
      "p_loss_20": 0.0,
      "mdd_p50": NaN,
      "mdd_p05": NaN,
      "mdd_p95": NaN
    },
    "point_last90": {
      "final_equity": 1283.3894740608116,
      "ret": 0.22227568958172528
    }
  }
}
```

## 20. 最终建议 / 三套方案 / Q1–Q13

### NET ETF GRID EDGE

{
  "n_allowed": 240,
  "median_edge_base_rebate0": -1553.6154145570274,
  "median_edge_conservative_rebate0": -1038.6049677119743,
  "all_base_rebate0_green": false,
  "rows": [
    {
      "symbol": "SOXL3L_USDT",
      "window_id": "S3_SOXL3L_USDT_pad15",
      "fill": "base",
      "rebate": 0.0,
      "edge": -8595.700796257133,
      "grid": 261.02492614247166,
      "rebate_income": 0.0,
      "inventory": -8823.070246799207,
      "decay_floor": -8823.070246799207,
      "mgmt": 14.616659029064346,
      "net_fee": 19.038816571333463,
      "total_equity_ret": -0.18110740558695615
    },
    {
      "symbol": "SOXL3L_USDT",
      "window_id": "S3_SOXL3L_USDT_pad15",
      "fill": "base",
      "rebate": 0.7,
      "edge": -8569.046453057266,
      "grid": 261.02492614247166,
      "rebate_income": 13.327171599933349,
      "inventory": -8823.070246799207,
      "decay_floor": -8823.070246799207,
      "mgmt": 14.616659029064346,
      "net_fee": 5.711644971400114,
      "total_equity_ret": -0.18110740558695615
    },
    {
      "symbol": "SOXL3L_USDT",
      "window_id": "S3_SOXL3L_USDT_pad15",
      "fill": "conservative",
      "rebate": 0.0,
      "edge": -5029.7159207305185,
      "grid": 194.85049701113306,
      "rebate_income": 0.0,
      "inventory": -5205.666193013595,
      "decay_floor": -5205.666193013595,
      "mgmt": 7.623391168115611,
      "net_fee": 11.276833559941476,
      "total_equity_ret": -0.05686324692266864
    },
    {
      "symbol": "SOXL3L_USDT",
      "window_id": "S3_SOXL3L_USDT_pad15",
      "fill": "conservative",
      "rebate": 0.7,
      "edge": -5013.928353746601,
      "grid": 194.85049701113306,
      "rebate_income": 7.89378349195905,
      "inventory": -5205.666193013595,
      "decay_floor": -5205.666193013595,
      "mgmt": 7.623391168115611,
      "net_fee": 3.383050067982426,
      "total_equity_ret": -0.05686324692266864
    },
    {
      "symbol": "SOXL3S_USDT",
      "window_id": "S3_SOXL3S_USDT_pad15",
      "fill": "base",
      "rebate": 0.0,
      "edge": -8720.60588945734,
      "grid": 132.7057039080359,
      "rebate_income": 0.0,
      "inventory": -8833.447285917282,
      "decay_floor": -8833.447285917282,
      "mgmt": 4.368647674810793,
      "net_fee": 15.495659773281002,
      "total_equity_ret": 0.23725908259090844
    },
    {
      "symbol": "SOXL3S_USDT",
      "window_id": "S3_SOXL3S_USDT_pad15",
      "fill": "base",
      "rebate": 0.7,
      "edge": -8698.911965774745,
      "grid": 132.7057039080359,
      "rebate_income": 10.846961841296835,
      "inventory": -8833.447285917282,
      "decay_floor": -8833.447285917282,
      "mgmt": 4.368647674810793,
      "net_fee": 4.648697931984167,
      "total_equity_ret": 0.23725908259090844
    },
    {
      "symbol": "SOXL3S_USDT",
      "window_id": "S3_SOXL3S_USDT_pad15",
      "fill": "conservative",
      "rebate": 0.0,
      "edge": -7590.425248746231,
      "grid": 120.81045247149135,
      "rebate_income": 0.0,
      "inventory": -7693.23983853997,
      "decay_floor": -7693.23983853997,
      "mgmt": 4.192463472481358,
      "net_fee": 13.803399205271457,
      "total_equity_ret": 0.2171003046274187
    },
    {
      "symbol": "SOXL3S_USDT",
      "window_id": "S3_SOXL3S_USDT_pad15",
      "fill": "conservative",
      "rebate": 0.7,
      "edge": -7571.100489858851,
      "grid": 120.81045247149135,
      "rebate_income": 9.662379443690023,
      "inventory": -7693.23983853997,
      "decay_floor": -7693.23983853997,
      "mgmt": 4.192463472481358,
      "net_fee": 4.141019761581434,
      "total_equity_ret": 0.2171003046274187
    },
    {
      "symbol": "ETH3L_USDT",
      "window_id": "S3_ETH3L_USDT_pad30",
      "fill": "base",
      "rebate": 0.0,
      "edge": -3356.6158150978986,
      "grid": 59.4335172169345,
      "rebate_income": 0.0,
      "inventory": -3400.4197206514286,
      "decay_floor": -3400.4197206514286,
      "mgmt": 9.448600714675317,
      "net_fee": 6.1810109487291856,
      "total_equity_ret": 0.06618129311629284
    },
    {
      "symbol": "ETH3L_USDT",
      "window_id": "S3_ETH3L_USDT_pad30",
      "fill": "base",
      "rebate": 0.7,
      "edge": -3347.9623997696776,
      "grid": 59.4335172169345,
      "rebate_income": 4.3267076641103825,
      "inventory": -3400.4197206514286,
      "decay_floor": -3400.4197206514286,
      "mgmt": 9.448600714675317,
      "net_fee": 1.854303284618803,
      "total_equity_ret": 0.06618129311629284
    },
    {
      "symbol": "ETH3L_USDT",
      "window_id": "S3_ETH3L_USDT_pad30",
      "fill": "conservative",
      "rebate": 0.0,
      "edge": -2456.3574362317204,
      "grid": 51.020966147955285,
      "rebate_income": 0.0,
      "inventory": -2493.2526962198167,
      "decay_floor": -2493.2526962198167,
      "mgmt": 8.890439442908004,
      "net_fee": 5.235266716950988,
      "total_equity_ret": 0.056728744531483466
    },
    {
      "symbol": "ETH3L_USDT",
      "window_id": "S3_ETH3L_USDT_pad30

### Plan A / B / C

{
  "A_low_dd": {
    "reanchor": "off",
    "fill": "conservative",
    "rebate_assumption": 0.0,
    "s_cap": 1500,
    "grids": {
      "SOXL3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.6C",
        "upper": "1.45C",
        "grid_n": 56,
        "capital": 1500,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "AAOI3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.5C",
        "upper": "1.6C",
        "grid_n": 64,
        "capital": 600,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "SNXX3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.5C",
        "upper": "1.65C",
        "grid_n": 64,
        "capital": 600,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "BTC3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.7C",
        "upper": "1.35C",
        "grid_n": 40,
        "capital": 300,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "ETH3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.6C",
        "upper": "1.45C",
        "grid_n": 56,
        "capital": 750,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "SOL3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.55C",
        "upper": "1.55C",
        "grid_n": 64,
        "capital": 1050,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "PENGU3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.4C",
        "upper": "1.8C",
        "grid_n": 80,
        "capital": 600,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "PUMP3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.35C",
        "upper": "1.9C",
        "grid_n": 80,
        "capital": 300,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      }
    }
  },
  "B_balance": {
    "reanchor": "14_day_up_only",
    "fill": "base",
    "rebate_assumption": 0.0,
    "s_cap": 2000,
    "grids": {
      "SOXL3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.6C",
        "upper": "1.45C",
        "grid_n": 56,
        "capital": 1500,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "AAOI3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.5C",
        "upper": "1.6C",
        "grid_n": 64,
        "capital": 600,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "SNXX3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.5C",
        "upper": "1.65C",
        "grid_n": 64,
        "capital": 600,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "BTC3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.7C",
        "upper": "1.35C",
        "grid_n": 40,
        "capital": 300,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬回撤触发后停新 3L；禁止下扩；库存按市价计 TOTAL EQUITY",
        "trend_filter": "SYSTEM E 3L 回撤 + 反转确认",
        "exit": "趋势破坏或硬 DD"
      },
      "ETH3L": {
        "entry": "ETF-native T1 或反转 R1/R2/R3，禁止未来低点",
        "lower": "0.6C",
        "upper": "1.45C",
        "grid_n": 56,
        "capital": 750,
        "deploy": "30/30/40",
        "reanchor": "off 或仅向上",
        "stop": "硬

### Q1
在真实 Gate 3L 逐笔上，Base/Conservative 样本中位 EDGE=-1553.6154145570274。总判定 FAIL。不是‘仍然优秀’。

### Q2
此前若用底层日线/价格当 3L，会系统性高估：漏掉第二层路径损耗、管理费、限价不成交。本次禁止该做法。

### Q3
额外波动提高理论穿越次数，但不自动变成 TOTAL EQUITY。必须看 inventory。SOXL3L 真实带上网格利润可为负。

### Q4
SOXL3L 上市后真实带接近归零路径；校准 A/B vs C 见 synth。库存亏损是主要损耗项。

### Q5
extra_grid − decay 用 inventory+grid 观察：中位 EDGE=-1553.6154145570274。未稳定为正。

### Q6
不能。SOXL 上再套 Gate 3L 是第二层每日杠杆。真实 SOXL3L 2026-06-25 起大幅路径损耗，窄网格+下移会爆。宽网格仍吃库存。

### Q7
相对不那么糟的是成交较密且未归零的 crypto 3L 短窗；没有任何产品在 0% 返佣 + Conservative + 失败窗上形成平台。

### Q8
SOXL3L/SNXX3S/高 Beta 山寨 3L（PENGU/PUMP）只可能短周期，且必须禁止向下扩格。AAOI3L 无真实带，不能下结论。

### Q9
3 倍合约网格 Benchmark 5 本次 INCOMPLETE（无 funding tape）。不得声称 ETF 网格优于或劣于合约网格。

### Q10
70% 返佣贡献见 robustness 的 eq70−eq0。它降低摩擦，不能把负库存翻正。

### Q11
最后 60 日全样本稳健性里，BTC/ETH/SOL/PENGU/PUMP 3L 结束权益略高于网格本金，SOXL3L 不能。这主要是库存盯市，不是返佣（样本均返佣收入约 1.6 USDT）。没有返佣也能“活”的只有：本来库存没被路径打穿的短窗。策略级 EDGE 中位数为负，不能说没返佣也能作为系统赚钱。

### Q12
判断错误（先涨后跌/单边下跌）样本亏损数=24。SOXL3L 真实带账户可接近归零（见该产品 final_equity）。

### Q13
存活率相对最高的是：不重锚向下、宽区间、少库存、禁止 3S 网格、S 硬顶 2500、硬回撤熔断。这是少亏，不是 alpha。
