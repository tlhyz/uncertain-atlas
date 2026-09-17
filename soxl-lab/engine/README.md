# Engine pointers (not forked)

This lab stores **inventory, params, and results**. Execution code stays in the
parent research repo so the two copies cannot drift.

| What | Parent path |
|------|-------------|
| 改参入口 | `../soxl-lab/scripts/run_grid.py` + `../src/analysis/soxl_grid_cli.py` |
| 扩展注册表 | `../src/analysis/grid_ext.py` |
| User 5x moving grid | `../src/analysis/user_moving_grid.py` |
| 重锚后挂单 | `apply_reanchor`：remap / drop_lots / flatten + `register_reanchor` |
| 新对冲规则 | `register_hedge(name, fn)`；或 `../extensions/*.py` |
| 格子种类 | `grid_kind`: arithmetic / geometric + `register_grid_kind` |
| 每格名义 | `sizer`: equal / martingale / fixed + `register_sizer` |
| 带宽 | `usdt` / `pct` + `register_range` |
| 扫参 | `../params/sweep.yaml` + `--sweep` |
| DayTradeCache / ATR pair | `../src/analysis/soxl_soxs_hedge.py` |
| P7-05 runner | `../scripts/run_p7_user_soxl_ls_grid.py` |
| Tick download | `../scripts/download_soxl_overlap_ticks.py` |
| Unit tests | `../tests/test_p7_user_moving_grid.py` · `../tests/test_soxl_grid_cli.py` |

When this folder is extracted to a private repo, copy those files in the same
relative layout, or set `SOXLLAB_PARENT` to the research checkout.
