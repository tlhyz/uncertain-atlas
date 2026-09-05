# Gate.io 多币种网格 / 马丁研究工具（期货激进双开 + 现货）

面向 **Gate VIP7 + 返佣** 的现金流式回测工具包。  
支持任意 USDT 永续合约（`BTC_USDT` / `ETH_USDT` / `牛来_USDT` 等中文合约名）。  
**不是套利**，**不含实盘下单**，公开行情 **不需要 API Key**。

## 功能

- `data.py`：Gate 公开 K 线 + **磁盘缓存 / 增量补齐** + 429 退避；可选少量 REST trades；文档化 WebSocket `futures.trades`
- `strategies/futures_martingale.py`：USDT 永续多空马丁（杠杆、保证金、投资额止损）
- `strategies/grid.py` / `martingale.py`：现货网格 / 现货马丁
- `optimize_futures.py`：激进双开（LONG+SHORT）参数搜索，`--stop-loss 0.5|0.7`
- `fees.py`：`effective_fee = base_fee * (1 - rebate_rate)`（现货 VIP7+70% / 期货 VIP7+75%）
- `cli.py`：统一命令行

## 环境

```bash
cd /workspace/gate-grid-martingale
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 任意币种怎么跑

合约名与 Gate 永续一致。中文合约直接写（或 URL 编码后的名字）；CLI 会交给 httpx 自动编码。

```bash
# 拉 K 线并写入 cache/（第二次几乎 0 次 API）
python cli.py fetch --symbol BTC_USDT --interval 5m --days 30
python cli.py fetch --symbol ETH_USDT --interval 15m --days 30
python cli.py fetch --symbol 牛来_USDT --interval 5m --days 18

# 只用本地缓存（断网 / 省配额）
python cli.py fetch --symbol BTC_USDT --interval 5m --days 14 --cache-only

# 激进双开优化（默认 compact 网格，止损 50%）
python cli.py optimize --symbol BTC_USDT --stop-loss 0.5 --style aggressive-dual --days 14

# 止损 70% + 中等搜索
python cli.py optimize --symbol 牛来_USDT --stop-loss 0.7 --grid medium --days 18

# 快速 demo（固定参数双开，不搜参）
python cli.py demo --symbol BTC_USDT --stop-loss 0.7 --days 14

# 现货对比（旧入口仍可用）
python cli.py demo --style spot --symbol BTC_USDT --interval 1h --days 60 --prefer gate
```

### 搜索网格大小

| `--grid` | 约每侧组合数 | 适用 |
|----------|-------------|------|
| `compact`（默认） | ~数百 | 日常多币 / `--days 14` |
| `medium` | ~数千 | 更细搜索 |
| `full` | ≈1 万+ | 重搜索；耗时长，按需使用 |

`full` 太重时请改用 `compact` / `medium`，不要为了省事去拉 tick 历史。

## 配额策略（重要）

Gate 公开接口有速率限制。本工具默认按「省配额」设计：

1. **回测用 K 线，不用逐笔**  
   优先 `5m` / `15m` / `1h`。用 REST `/futures/usdt/candlesticks`（或 spot candlesticks）。
2. **磁盘缓存 + 增量**  
   文件在 `cache/futures_<合约>_<周期>_candles.csv`。第二次 `fetch` / `optimize` 若无缺口 → **api_calls=0**。只补左/右缺口，不整段重下。
3. **`--cache-only`**  
   强制不访问网络；缓存不足则报错退出。
4. **429 退避**  
   遇到 HTTP 429 会指数 sleep / 尊重 `Retry-After`，并打印 `[rate-limit]`。
5. **不要用 REST trades 拼 18 天历史**  
   `python cli.py fetch --symbol BTC_USDT --trades` 只会拉**一小段**最近成交作样例。多日 tick = 配额自杀。  
   **实盘/直播行情**请用 WebSocket：

```text
wss://fx-ws.gateio.ws/v4/ws/usdt
channel: futures.trades
payload: ["BTC_USDT"]   # 中文合约名同理
```

查看内置说明：

```bash
python cli.py fetch --symbol BTC_USDT --show-ws-doc
```

## 费用模型（保持 VIP7+返佣）

| 市场 | Maker 基础 | Taker 基础 | 返佣 | 有效 Maker / Taker |
|------|------------|------------|------|---------------------|
| 现货 VIP7 | 0.08% | 0.085% | 70% | ≈0.024% / 0.0255% |
| 期货 VIP7 | 0.008% | 0.02% | 75% | ≈0.002% / 0.005% |

```bash
python cli.py fee-example --notional 10000
python cli.py fee-example --futures --notional 10000
```

## 策略风格（激进双开）

默认 **不**改成保守单边：

- LONG + SHORT 同时跑（双开对冲风格）
- 小仓（默认 LONG 950 / SHORT 1380，可用 `--long-cap` / `--short-cap` 改）
- 杠杆默认 5x（`--leverage`）
- 深 `max_adds`（搜索含 40/90，展示时可 buf 到 90）
- `--stop-loss 0.5|0.7`：按 **投资额回撤**（`uPnL / initial_margin ≤ -SL`）止损平仓后开新周期

注意：Gate UI 若把「止损%」解释成相对均价的**价格%**，与本回测经济含义不同；填写前请对照帮助中心。

## 其他命令

```bash
python cli.py recommend
python cli.py backtest --rebate 0.70
python cli.py gen-sample
pytest -q
```

## 风险提示

1. 网格 / 马丁会占用资金，单边行情可能深度套牢或触发止损 / 强平；回测盈利 ≠ 未来盈利。  
2. 仅研究用：无实盘、无密钥、无下单。  
3. 返佣降低费用拖累，不能消除趋势与杠杆风险。  
4. 未计入资金费、滑点、挂单失败。  
5. 请只用闲置资金；作者不对任何资金损失负责。

## 目录提示

- `cache/`：K 线磁盘缓存（可删，下次会重新拉）
- `data_sample/`：示例 / 离线 CSV
- `opt_*_results.json` / `opt_*_report.md`：优化输出
