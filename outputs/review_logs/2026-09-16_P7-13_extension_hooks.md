# P7-13 — plugin registry + sweep (user: 可能会改)

Verdict: **PASS** (structure). Not a trading verdict.

## What changed

The runner was already YAML-driven (P7-08/11). This pass makes *rules* pluggable
the same way numbers already are.

| Layer | How to change it later |
|-------|------------------------|
| leverage / grids / ±U / capital / window | `params/run.yaml` or CLI |
| many combinations at once | `--sweep params/sweep.yaml` |
| hedge stop rule | `register_hedge` or `soxl-lab/extensions/*.py` |
| rung spacing | `register_grid_kind` |
| band (±U / ±% / custom) | `register_range` |
| exit-band policy | `register_reanchor` |
| extra YAML keys | land in `extras`; `register_yaml_keys` silences `--check` |

Scheduler (`soxl_grid_cli.main`) does not need edits for the above.

## Checks

- `pytest tests/test_grid_ext.py tests/test_soxl_grid_cli.py tests/test_p7_user_moving_grid.py` → **40 passed**
- `--list-extensions` lists flatten_survivor / independent / usdt / pct / arithmetic / geometric / remap|drop_lots|flatten
- `--sweep soxl-lab/params/sweep.yaml --check` overlays yours / lev3 / g80 / pct10
- 1-day **bar** smoke (not a verdict): yours +0.55% / lev3 +0.33% / g80 +1.51% / pct10 +0.64% — knobs bite

## Not plugged (still engine work)

New fill model other than tick/bar. Time-varying ATR band per bar.

## Do not

Commit `cache/` ticks. Treat sweep bar/1d as a knob check, not a 58-day hedge result.
