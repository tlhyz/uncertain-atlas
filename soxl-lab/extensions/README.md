# 扩展点（以后改规则走这里，不要改调度）

改杠杆 / 格数 / ±U / 本金 / 窗口：直接改 `../params/run.yaml`，或 `--sweep`。

改「对冲怎么停、格子怎么排、带宽怎么算」：注册，不要改 `soxl_grid_cli.main`。

## 怎么加

1. 在本目录复制 [`_template_hedge.py`](_template_hedge.py) 成 `我的规则.py`（不要 `_` 开头）。
2. 里面调用 `register_hedge` / `register_grid_kind` / `register_range` / `register_reanchor` / `register_sizer`。
3. `python3 soxl-lab/scripts/run_grid.py --list-extensions` 能看到名字。
4. YAML 里写 `hedge: 那个名字`，或 `--hedge 那个名字`。

也认环境变量 `SOXLLAB_EXTENSIONS`（多个目录用 `:` 分隔）和 `--ext-dir`。

`_*.py` 不会自动加载，模板可以安心留着。

## 函数约定

```python
def my_book(bars, **engine_kwargs) -> dict:
    # engine_kwargs 至少有：
    #   range_mode leverage range_usdt range_pct n_grids
    #   fee_preset fill_engine get_trades on_bar
    #   grid_kind fee_bps reanchor mmr_frac sizer
    #   capital_long capital_short extras
    ...
```

返回值对齐 `run_user_hedge_pair`：必须带 `daily`（含 `daily_pnl`）、`return`、`max_dd`、`end_equity`、`fills`、`turnover`、`reanchors`、`inventory_frac`、`net_qty_units`。

未知 YAML 键、以及 `--set 键=值`，都进 `extras`，插件自己读。`register_yaml_keys("我的键")` 只让 `--check` 不再标「未登记」，**不会把键从 extras 拿掉**。

每格名义：

```python
def my_lots(*, capital, leverage, n_grids, level_idx, extras, direction, **_):
    return max(capital * leverage / n_grids, 1.0)

register_sizer("my_lots", my_lots)
```

内置 `equal`（均仓）、`martingale`（`extras.martingale_ratio`，默认 1.2）、`fixed`（`extras.lot_usdt`）。

## 不要动的

- 不要在插件里 `git add cache/`。
- 不要静默把 tick 改成 bar。
- 内置 `flatten_survivor` / `independent` 的行为是研究结论的对照，不要覆盖同名。
