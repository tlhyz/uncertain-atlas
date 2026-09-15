# soxl-lab — 只做 SOXL 的个人隐私库

这是从 `gate-grid-martingale` 拆出来的 **SOXL 专用目录**：逐笔库存、网格参数、回测结果三类分开存放，并经过三遍独立复核。

不是公开产品。不含 API key、账户、身份信息。原始逐笔 CSV（约 1.65 GB）留在本机 `cache/`，**永不入库**。

## 三类入口

| 类 | 目录 | 先看 |
|----|------|------|
| 数据 | `data/` | `INVENTORY.md` → `SCHEMA.md` → `manifests/` |
| 参数 | `params/` | `user_moving_grid.yaml`（你的 5x / ±20U / ±20% / 200 格 / 5k+5k） |
| 结果 | `results/` | `INDEX.md` → `p7_05_usdt20.json` / `p7_tick_hedge.base.soxl.json` |

全表：[`CATALOG.md`](CATALOG.md)。三遍复核：[`AUDIT_3PASS.md`](AUDIT_3PASS.md)。

## 本窗结论（已复核）

- 逐笔齐：2026-07-15→09-11，59 天无缺口，31,190,286 笔，覆盖 1392/1392 根 1h。
- 研究模板 ATR 0.40/±5 同标多空 **+12.3% / −17.7%** 的空腿当时是 BAR，不能当双边 TICK。
- 你的实盘参数（5x、±20U **和** ±20%、200 格、5k 多 + 5k 空、TICK 双边）全窗都 **FAIL**：±20U **−12.8% / DD −80%**，±20% **−18.7% / DD −77%**，两边都是多头爆仓。
- SOXL+SOXS 网格对冲 **FAIL**（价格是反向，网格不是对冲）。诚实对冲是日频 50/50，不加网格。

## 抽成独立私有 GitHub 库

本环境的 `gh` 是只读的，不能替你 `gh repo create --private`。步骤见 [`EXTRACT_PRIVATE_REPO.md`](EXTRACT_PRIVATE_REPO.md)。

```bash
python3 scripts/verify_three_passes.py --times 3
```
