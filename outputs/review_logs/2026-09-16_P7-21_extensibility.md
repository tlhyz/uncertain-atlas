# Review Log — P7-21 extensibility (user may change rules)

**Date:** 2026-09-16  
**Question:** 网格脚本以后改参数/规则，能不能不动调度？  
**Verdict:** **PASS** (hooks only; no new live-grid claim)

## What changed

- `register_yaml_keys` used to drop those keys from `extras`. Plugins then never saw them. Fixed: engine keys vs plugin keys are separate; extras always keep non-engine keys.
- New `register_sizer` / `resolve_notional`. Built-ins: `equal` (default), `martingale` (`martingale_ratio`), `fixed` (`lot_usdt`).
- `resolve_rungs` forwards `extras` (3-arg plugins still work).
- CLI `--sizer` and `--set key=value` write extras without editing YAML.
- `--check` says unregistered keys still go to extras; it no longer claims they “will not take effect”.
- `register_validator` for plugin-required extras.

## How to change later (do not edit `soxl_grid_cli.main`)

| Change | Path |
|--------|------|
| Numbers (lev, grids, ±U, capital, window) | `params/run.yaml` / CLI |
| Temporary extra | `--set k=v` |
| Hedge / band / rungs / reanchor / lot formula | `soxl-lab/extensions/*.py` |
| New fill model (not tick/bar) | still engine |

## Tests

See `tests/test_grid_ext.py` + `tests/test_soxl_grid_cli.py`. No new full-window SOXL run. Q_SOXL_USER_GRID stays **NO**.
