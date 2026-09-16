# 自己改参数跑 SOXL 逐笔网格

**先读 [`../使用注意事项.md`](../使用注意事项.md)。** 本机 `cache/` 是 Binance UM 真实 aggTrades，默认 **cache_only**，不会乱下。逐笔 CSV **不进 git**（大约 3 GB）。

## 0. 先看本机有没有数据

```bash
cd /path/to/gate-grid-martingale
python3 soxl-lab/scripts/run_grid.py --list-cache
python3 soxl-lab/scripts/run_grid.py --check
```

`--check` 打印这次会用的参数，并核对窗口每一天的逐笔 CSV。缺天默认拒绝开跑。

## 1. 改 YAML

打开 [`../params/run.yaml`](../params/run.yaml)，改杠杆、格数、±U / ±%、本金、对冲方式、起止日。

```bash
python3 soxl-lab/scripts/run_grid.py
```

`params/01_yours_moving_grid.yaml` 那份底稿也可以直接 `--config` 喂进去。

## 2. 或者命令行盖一层（不用改文件）

```bash
# 3 倍、80 格、±15U、多空对冲
python3 soxl-lab/scripts/run_grid.py --leverage 3 --n-grids 80 --range-usdt 15

# ±10%、独立两本账、只要 8 月
python3 soxl-lab/scripts/run_grid.py --mode pct --range-pct 0.10 --hedge independent \
  --start 2026-08-01 --end 2026-08-31 --tag aug

# 只做多
python3 soxl-lab/scripts/run_grid.py --sides long --start 2026-07-16 --end 2026-07-20 --fills bar

# 先用 K 线快速试（结论仍以 tick 为准）
python3 soxl-lab/scripts/run_grid.py --fills bar --start 2026-07-16 --end 2026-07-20
```

## 3. 结果写哪

`soxl-lab/results/runs/<对冲_带宽_杠杆_格数_本金_成交_起止日>/`

- `README.md` 中文一页：收益 / 回撤 / 是否停机
- `spec.json` 这次实际用的参数
- `summary.json` 机器可读
- `daily.csv` 每天一行

窗口写进目录名，换日期不会覆盖上一次。

仓库根目录也可以：`python3 scripts/run_soxl_grid.py`（同一个入口）。

## 4. 常见拒绝

| 情况 | 怎么办 |
|------|--------|
| 窗口缺逐笔 | `--list-cache` 看缺哪天；或 `--allow-empty-ticks`（不建议） |
| 没有 1h K 线缓存 | 自动从逐笔重采样；也可 `--bars-from-ticks` 强制 |
| tick 模式没喂成交 | 引擎直接报错，不会偷偷改用影线 |
