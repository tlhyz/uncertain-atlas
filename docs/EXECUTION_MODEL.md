# Execution Model

## Live intent: LIMIT / MAKER-FIRST

All research conclusions for deployment must use **Base** and **Conservative** fill modes.

| Mode | Rule |
|------|------|
| Optimistic | Touch = fill — **excluded from primary verdict** |
| Base | Trade must **through** limit; participation capped by real volume |
| Conservative | +1–2 tick penetration, volume cap, adverse queue |

## Tick path (Binance aggTrades)

Walk: `bar_open → each aggTrade → bar_close` (`qtb/dual/tick_fills.py`).

Grid: crossing rules match bar engine — no multi-level phantom fills.

Directional rebalance: `adjust_notional_via_ticks` with participation budget.

## Bar path (when ticks unavailable)

Must label report **BAR BACKTEST**. Gate ETF/perp bar engine: `qtb/ab/fills.py`.

## Binance vs Gate

Structure research on Binance; **Gate OOS** calibrates funding, tick, spread, rebate, fill ratio.

If Gate calibration diverges → lower confidence in live candidate.

## Outputs required per run

`report.md` · `summary.json` · `metrics.csv` · `parameters.csv` · `data_manifest.json`

Sections: DATA COVERAGE · LIMITATIONS · ASSUMPTIONS · RESULTS · FAILURES · OOS · ROBUSTNESS · VERDICT
