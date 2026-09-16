# ① 数据 — SOXL 逐笔

CSV **不入库**。清单和格式在这里。

| 问题 | 答案 |
|------|------|
| 哪一天开始有？ | Binance UM Vision **2026-05-15**（05-14 及更早 404） |
| 本机有几天？ | **120** 天，2026-05-15 → 09-11，**0 缺口** |
| 多大？ | 全量 **3.27 GB**；已复核窗 07-15→09-11 为 1.65 GB / 3119 万笔 |
| 价格大概？ | 已复核窗 min **85.94** / max **191.10** |
| 1h 对得上吗？ | 回测窗 **1392/1392**，缺 0 |
| 文件长什么样？ | `ts_ms, price, qty, quote_qty, is_buyer_maker, agg_id` — [`SCHEMA.md`](SCHEMA.md) |
| 校验和？ | [`manifests/binance_SOXLUSDT_aggTrades_2026-07-15_2026-09-11.json`](manifests/binance_SOXLUSDT_aggTrades_2026-07-15_2026-09-11.json) |
| 机器可读？ | [`inventory.json`](inventory.json) |

本机路径：`../../cache/binance_futures_SOXLUSDT_aggTrades_YYYY-MM-DD.csv`
