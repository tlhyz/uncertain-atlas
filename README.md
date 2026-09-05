# Gate.io 现货网格 + 马丁格尔 回测工具包

面向 **Gate VIP7 + 现货返佣 70%** 的现金流式（cash-flow）网格 / 马丁研究工具。  
**不是套利**，不含实盘下单，不需要 API Key。

## 功能

- `fees.py`：手续费 / 返佣公式 `effective_fee = base_fee * (1 - rebate_rate)`
- `strategies/grid.py`：现货网格模拟
- `strategies/martingale.py`：现货马丁（加仓回本止盈，无杠杆）
- `data.py`：拉取公开 K 线（默认 **Binance 公开 klines** 作为流动性代理；失败时尝试 Gate 公开接口；再失败用内置 CSV）
- `backtest.py`：净盈亏、最大回撤、循环次数、费用拖累、胜率；无返佣 vs 有返佣对比
- `optimize.py`：对间距 / 止盈 / 乘数 / 最大加仓做简单网格搜索
- `cli.py`：命令行入口

## 环境

- Python 3.11+
- 建议使用虚拟环境：

```bash
cd /workspace/gate-grid-martingale
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 一键 Demo

```bash
cd /workspace/gate-grid-martingale
source .venv/bin/activate   # 若已创建
python cli.py demo --symbol BTCUSDT --interval 1h --days 90
```

将完整 stdout 保存示例：

```bash
python cli.py demo --symbol BTCUSDT --interval 1h --days 90 2>&1 | tee demo_output.txt
```

离线 / 网络失败时：

```bash
python cli.py gen-sample
python cli.py demo --prefer sample
```

## 其他命令

```bash
python cli.py fee-example --notional 10000 --rebate 0.70
python cli.py recommend
python cli.py backtest --rebate 0.70 --grid-spacing 0.008 --mart-tp 0.012
python cli.py optimize --days 60
pytest -q
```

## VIP7 + 70% 现货返佣费用示例

| 项目 | 数值 |
|------|------|
| VIP7 现货 Maker 基础费率 | 0.08% = 0.0008 |
| VIP7 现货 Taker 基础费率 | 0.085% = 0.00085 |
| 现货返佣 | 70% |
| 有效 Maker | `0.0008 * (1 - 0.70) = 0.00024`（0.024%） |
| 有效 Taker | `0.00085 * 0.30 = 0.000255`（0.0255%） |

举例：10,000 USDT Maker 成交  

- 无返佣手续费：`10000 * 0.0008 = 8 USDT`  
- 有返佣手续费：`10000 * 0.00024 = 2.4 USDT`  
- **节省 5.6 USDT（约 70%）**

期货返佣（75%）仅作对照说明；本工具默认做 **现货**，更符合「少用高杠杆马丁」的偏好。

## 数据来源说明

1. **默认**：Gate `GET /api/v4/spot/candlesticks`（公开、免 Key，自动分页，每页最多 1000 根）。  
2. **备选**：Binance `GET /api/v3/klines` / `data-api.binance.vision`（部分地区可能 HTTP 451）。  
3. **兜底**：`data_sample/BTCUSDT_1h_sample.csv` 或 `cli.py gen-sample` 合成数据。

价格序列用于相对回测与费用敏感性分析，不保证与 Gate 成交价逐笔一致。

## 风险提示（必读）

1. **网格 / 马丁会占用资金并可能在单边行情中深度套牢**；回测盈利 ≠ 未来盈利。  
2. 本工具 **仅研究用**，无实盘、无密钥、无下单接口。  
3. 返佣降低费用拖累，**不能消除趋势风险**；马丁加仓会放大回撤。  
4. 请只用闲置资金做小仓位实验；不要用高杠杆期货马丁硬刚行情。  
5. 作者不对任何资金损失负责。

## 推荐起步参数（VIP7 + 70% 返佣费用优势下）

运行 `python cli.py recommend` 或 demo 结尾会打印，大致为：

- **现货网格**：间距约 0.8%，约 24 格，单格 50 USDT（Maker）  
- **现货马丁**：基数 80 USDT，乘数 1.4，跌 1.8% 加仓，均价上 1.2% 止盈，最多加 4 次  

有返佣后费用拖累下降，可略微收紧间距 / 止盈；仍需严格限制最大加仓。
