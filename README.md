# qtb — Gate USDT-M 永续回测 / 寻参 / 报告框架

面向 **Gate VIP7 + 高返佣** 的现金流型量化研究工具。  
任意 USDT 永续合约（`BTC_USDT` / `ETH_USDT` / `牛来_USDT`）。  
默认 **只做回测**。实盘模块存在，但 **强制 DRY_RUN**，没有真实下单通道。

**不是套利。公开行情不需要 API Key。不要把回测当承诺收益。**

激进双开马丁（LONG + SHORT 对冲式加仓）是一等公民策略，不是「不建议」的边角功能。投资额止损默认提供 **50% / 70%** 两档（`risk.investment_sl_pct`）。

---

## 架构

```
qtb/
  data/        K 线磁盘缓存 + 增量拉取、资金费、合约 quanto
  costs/       VIP 费率 / 返佣 / 滑点 / 资金费 / 最小下单
  strategies/  classic_grid / trend_grid / dual_grid / martingale / dual_martingale
  risk/        止盈止损、回撤停机、接近强平强平前离场、破网格停机
  engine/      统一逐 K 回测引擎
  optimize/    复合打分 + 训练/测试、滚动、多行情、Monte Carlo、参数稳定
  report/      成交 CSV、热力图、权益/回撤/持仓图、中文摘要
  live/        实盘桩：默认 DRY_RUN；无私钥、无下单
  screen.py    USDT 永续选币（高波动 + 低路径效率）
configs/       YAML / TOML
outputs/       每次运行的产物
```

旧脚本（`optimize_futures.py`、`cli.py` / `gate-gm`）仍可用，核心实现已迁到 `qtb/`。

---

## 环境

Python 3.11+。

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# 或: pip install -e .
```

入口：

```bash
python -m qtb.cli --help
# 安装后也可: qtb --help
```

---

## 怎么跑

所有关键参数写在 `configs/*.yaml`，不要改代码里的魔法数。

```bash
# 回测（默认）。示例用本地 BTC 1h sample，不打 API
python -m qtb.cli backtest -c configs/backtest_dual_martingale.yaml

# 经典网格 / 趋势网格 / 对称双网格
python -m qtb.cli backtest -c configs/backtest_classic_grid.yaml
python -m qtb.cli backtest -c configs/backtest_trend_grid.yaml
python -m qtb.cli backtest -c configs/backtest_dual_grid.yaml

# 寻参 + 防过拟合（train/test、walk-forward、regime、Monte Carlo、邻域稳定）
python -m qtb.cli optimize -c configs/optimize.yaml

# 从已有 outputs/<run> 重看摘要
python -m qtb.cli report outputs/demo_btc_dual_martingale

# 多合约 / 多周期
python -m qtb.cli batch -c configs/batch.yaml

# 覆盖 CLI（不必改 YAML）
python -m qtb.cli backtest -c configs/backtest_dual_martingale.yaml \
  --symbol ETH_USDT --interval 15m --days 30 --stop-loss 0.7

# 选币（高波动 + 低路径效率，不是裸 24h 振幅）
python -m qtb.cli screen
python -m qtb.cli screen --min-volume 5000000 --min-range 0.12 --max-trend 0.28 --prefilter 40 --top 20
python -m qtb.cli screen --cache-only --out outputs/screen_offline

# 选币后对前 K 名跑激进双开 SL50（覆盖 YAML 里的 symbol）
python -m qtb.cli screen --batch-backtest --picks 3
python -m qtb.cli batch-screen --picks 3 --batch-mode backtest
python -m qtb.cli batch-screen --batch-mode optimize -c configs/optimize_niulai_aggressive_sl50.yaml
```

## 选币逻辑（给激进双开用）

不要按「24h 振幅最大」直接开马丁。回测里：

- **极端单边趋势**（如 BULLA / AKE）：路径效率高，一边吃尽加仓，另一边空转或止损。
- **纯横盘碎抖**（如 BTW / TUT）：振幅/波动太碎，手续费和加仓间距吃掉现金流。
- **更合适的是 牛来 / HYPE 一类**：中高波动、K 线来回走（**低路径效率**），双开马丁才有换手。

流程（省配额：ticker **只拉一次**，K 线走磁盘缓存 + 429 退避）：

1. `GET /futures/usdt/tickers`，24h quote volume ≥ `--min-volume`（默认 500 万 USDT）
2. 24h range `(high-low)/last` ≥ `--min-range`（默认 0.12）做预筛
3. 按 24h range 取前 `--prefilter`（默认 40），拉约 `--days` 天 `--interval` K 线（默认 7×1h，约 168 根）
4. 每个合约：
   - `vol` = 1h 收益率的 **pstdev**
   - `amp` = mean((high-low)/close)
   - `trend` / 路径效率 = `|净收益| / Σ|ret|`
   - `score` = `vol * amp / (trend + 0.05)`
5. 按 score 排序；默认再丢掉 `trend ≥ --max-trend`（0.28）
6. 打印表格，并写 `outputs/screen_*.json` / `.md`

`--max-trend` 设为负数可关闭趋势过滤。`--batch-backtest` / `batch-screen` 读取 `configs/optimize_niulai_aggressive_sl50.yaml`（或 `-c`），对前 `--picks`（默认 3）用入选合约覆盖 `symbol`（并关掉 sample），走 `qtb` 的 `backtest`（固定参数）或 `optimize`（compact 搜索）。对比摘要写到 `outputs/batch_screen_*.md`。

---

## 牛来_USDT 激进双开默认配置（用户风格，未改保守）

这是 **LONG + SHORT 同时开、小仓、深加仓缓冲** 的现金流打法，不是保守单边。

| 项 | 默认 |
|----|------|
| 合约 | `牛来_USDT`（任意合约可用 `--symbol` 覆盖） |
| 周期 / 天数 | `5m` / `18`（`--interval` / `--days`） |
| 投资额 | LONG **950** / SHORT **1380** USDT |
| 杠杆 | **5x** |
| 最大加仓 | **90**（缓冲；实际层数通常远低于 90） |
| 止损 | 投资额回撤 `uPnL / initial_margin`：**50%** 或 **70%** |
| 费率 | 期货 VIP7 + **75%** 返佣 |
| SL50 非对称 | LONG 倍数 1.4 / 跌 2.5% / 止盈 1.2%；SHORT 1.2 / 涨 4.0% / 1.2% |
| SL70 非对称 | LONG 倍数 1.8 / 跌 1.8% / 止盈 1.2%；SHORT 1.3 / 涨 4.0% / 1.2% |

默认 `prefer_sample: true`，读 `data_sample/niulai_USDT_5m_futures.csv`，**不打 Gate 配额**。  
`--symbol` 覆盖其他合约时会关掉 sample，改走缓存 / 行情。

```bash
# SL50 / SL70 固定参数回测（本地 sample）
python -m qtb.cli backtest -c configs/backtest_niulai_aggressive_sl50.yaml
python -m qtb.cli backtest -c configs/backtest_niulai_aggressive_sl70.yaml

# 紧凑网格寻参 + 防过拟合（train/test、walk-forward、regime、Monte Carlo）
python -m qtb.cli optimize -c configs/optimize_niulai_aggressive_sl50.yaml
python -m qtb.cli optimize -c configs/optimize_niulai_aggressive_sl70.yaml

# 同一套风格换任意合约（磁盘缓存，省配额）
python -m qtb.cli backtest -c configs/backtest_niulai_aggressive_sl50.yaml \
  --symbol ETH_USDT --interval 5m --days 18 --cache-only
python -m qtb.cli optimize -c configs/optimize_niulai_aggressive_sl70.yaml \
  --symbol BTC_USDT --days 14 --stop-loss 0.7 --cache-only
```

产物在 `outputs/<run_name>/`：

| 文件 | 内容 |
|------|------|
| `trades.csv` | 逐笔成交 |
| `equity_curve.png` | 权益曲线 |
| `drawdown_curve.png` | 回撤 |
| `position_chart.png` | 净持仓 |
| `parameter_heatmap.png` | 寻参热力图（optimize） |
| `summary.md` | 中文摘要 |
| `metrics.json` | 数值指标 |
| `config.used.yaml` | 实际用到的配置 |

---

## 策略与风控

| `strategy.name` | 含义 |
|-----------------|------|
| `classic_grid` | 经典网格 |
| `trend_grid` | EMA 定方向的趋势网格 |
| `dual_grid` | 多空对称网格（可加 `martingale_addon`） |
| `martingale` | 单边马丁 |
| `dual_martingale` | **激进双开**（默认） |

止盈：单笔、组合、分批/`scaled_tp`、移动止盈、持仓 bar 数。  
止损：单笔价格%、**投资额 50%/70%**、组合权益、最大回撤停机、浮亏达到阈值停止加仓、估计强平价前强平、价格跌破网格区间停机。

复合分同时看：收益、最大回撤、Sharpe、Calmar、胜率、盈亏比、最大浮亏、强平风险、费用比、参数稳定性。强平直接重罚。

---

## 配额（重要）

Gate 公开接口有速率限制。本框架按「省配额」设计：

1. **回测用 K 线，不用逐笔。** 优先 `5m` / `15m` / `1h`。接口：`/futures/usdt/candlesticks`。
2. **磁盘缓存 + 增量。** `cache/futures_<合约>_<周期>_candles.csv`。无缺口时 `api_calls=0`。
3. **`--cache-only` / `prefer_sample: true`。** 断网或演示用本地 CSV。
4. **HTTP 429** 指数退避，尊重 `Retry-After`。
5. **不要用 REST trades 拼多日历史。** 直播用 WebSocket：

```text
wss://fx-ws.gateio.ws/v4/ws/usdt
channel: futures.trades
payload: ["BTC_USDT"]
```

资金费：`/futures/usdt/funding_rate`，同样磁盘缓存；拉不到则用 8h 合成费率，保证成本模型仍在跑。

---

## 费用（VIP 可配）

`effective_fee = base_fee * (1 - rebate_rate)`

| 市场 | Maker 基础 | Taker 基础 | 默认返佣 | 有效 Maker / Taker |
|------|------------|------------|----------|---------------------|
| 现货 VIP7 | 0.08% | 0.085% | 70% | ≈0.024% / 0.0255% |
| 期货 VIP7 | 0.008% | 0.02% | 75% | ≈0.002% / 0.005% |

另计入：滑点 bps、资金费、quanto / 最小张数 / 最小名义。

---

## 实盘安全

- 配置默认 `mode: backtest`，`live.dry_run: true`。
- `LiveBroker.send_order` **不会**打私有下单 API。
- 想「关闭 DRY_RUN」必须同时：环境变量 `ALLOW_LIVE=1` **且** `live.dry_run: false`。即便如此，模块仍会拒绝：`LiveStubError`（没有下单实现）。
- 不要把 API Key 放进仓库。

```bash
python -m qtb.cli live -c configs/live.toml --ping
# 输出 status=dry_run, filled=false
```

---

## 测试

```bash
pytest -q
```

覆盖：费用/滑点/资金费/quanto、止盈止损触发、复合分、DRY_RUN 守卫、选币 score/trend（合成序列，不打网络）。

---

## 风险声明

1. 网格 / 马丁会占用资金；单边行情可能深套、反复止损或触发强平。回测盈利 ≠ 未来盈利。
2. 仅研究用。无密钥、无真实下单。`live` 是桩。
3. 返佣只降低费用拖累，不能消除趋势与杠杆风险。
4. 强平价、维持保证金、部分成交、挂单失败与交易所不完全一致；这是研究级近似。
5. 只用闲置资金。作者不对任何资金损失负责。

Gate UI 若把「止损%」解释成相对均价的**价格%**，与本框架默认的 **投资额回撤止损**（`uPnL / initial_margin`）含义不同，下单前请对照帮助中心。
