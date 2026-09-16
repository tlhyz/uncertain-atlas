# 自己改参数跑 SOXL 逐笔网格

本机 `cache/` 里是 Binance UM 真实 aggTrades，默认 **cache_only**，不会乱下。

## 1. 改 YAML

打开 [`../params/run.yaml`](../params/run.yaml)，改杠杆、格数、±U / ±%、本金、对冲方式、起止日。

```bash
cd /path/to/gate-grid-martingale
python3 soxl-lab/scripts/run_grid.py
```

## 2. 或者命令行盖一层（不用改文件）

```bash
# 3 倍、80 格、±15U、多空对冲
python3 soxl-lab/scripts/run_grid.py --leverage 3 --n-grids 80 --range-usdt 15

# ±10%、独立两本账、只要 8 月
python3 soxl-lab/scripts/run_grid.py --mode pct --range-pct 0.10 --hedge independent \
  --start 2026-08-01 --end 2026-08-31 --tag aug

# 先用 K 线快速试（结论仍以 tick 为准）
python3 soxl-lab/scripts/run_grid.py --fills bar --start 2026-07-16 --end 2026-07-20
```

## 3. 结果写哪

`soxl-lab/results/runs/<对冲_带宽_杠杆_格数_本金_tick>/`

- `spec.json` 这次实际用的参数
- `summary.json` 收益 / 回撤 / 是否爆仓 / 是否停机
- `daily.csv` 每天一行

仓库根目录也可以：`python3 scripts/run_soxl_grid.py`（同一个入口）。
