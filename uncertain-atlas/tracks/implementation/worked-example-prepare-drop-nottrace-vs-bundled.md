# 例：看见把 t1 改成 t2 is not already can look up t1 interchangeable / not already someone knows t2 from t1 interchangeable / not already settled interchangeable

**层次**：实现 / 把 t1 改成 t2 not already can look up t1 / not already someone knows t2 from t1 / not already settled 正式三事（355 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「把 t1 改成 t2 not already can look up t1 / not already someone knows t2 from t1 / not already settled 正式三事（355 余量）/ not 856 prepare-drop-nottrace interchangeable / not 355 prepare-drop-vs-mempool bundled interchangeable」，不是 Prepare 改列表 bundled（355），也不是四门已经结算（33），也不是没调 Prepare 就已经又装了一份 raw 提案（356/853）。不要另写怎样改 Prepare 列表。

## 官方三件事

1. **看见把 t1 改成 t2 / 看见 t1 没进块 这份改了 is not already 已经还能按 t1 查到 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 856 prepare-drop-nottrace interchangeable / 854 prepare-drop-notdeleted interchangeable / 355 prepare-drop item 1 拿掉 interchangeable，也不是已经把 t1 改成 t2 not already can look up t1 / not already someone knows t2 from t1 / not already settled 正式三事 bundled（355 item 3 余量） interchangeable / 355 prepare-drop item 3 interchangeable。**  
   官方写：拿掉再加可能丢掉可追踪性。客户端去查 t1，会发现 t1 没进已提交块。看见 t1 没进块，不是已经还能按 t1 查到 interchangeable——本页从 355 item 3 侧钉 not already can look up t1 单句。355 prepare-drop vs mempool bundled unbundling 在本页 item 3 完成。

2. **看见 t1 没进块 / 看见 t2 进了块 / 这份改了 is not already 已经有人知道 t2 来自 t1 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 856 prepare-drop-nottrace interchangeable / 355 prepare-drop item 2 加新的 interchangeable / 855 prepare-drop-notinpool interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把 t2 进了块和已经有人知道来源分开——355 bundled 第三件事常与 33 混成「看见 t1 没进块就已经还能按 t1 查到或已经有人知道 t2 来自 t1 interchangeable」，本页钉 not already someone knows t2 from t1 单句。

3. **看见 t1 没进块 / 看见改了 / 这份改了 is not already 已经交差 interchangeable，也不是已经 Prepare 改列表 bundled（355） interchangeable / 856 prepare-drop-nottrace interchangeable / 854 prepare-drop-notdeleted interchangeable，也不是已经没调 Prepare 就已经又装了一份 raw 提案 interchangeable / 356 validvalue / 853 validvalue-notraw interchangeable。**  
   官方把改了和已经交差分开。看见改了，不是已经交差 interchangeable。355 prepare-drop vs mempool bundled unbundling 在本页 item 3 完成。

怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池是规范里的做法，本页不抄。

## 官方为什么这样拆

- **把 t1 改成 t2 not already can look up t1 ≠ 已经还能按 t1 查到 interchangeable：** 官方把改列表和可追踪性分开。
- **看见 t2 进了块 not already someone knows t2 from t1 ≠ 已经有人知道来源 interchangeable：** 官方把 t2 进了块和已经有人知道来源分开。
- **看见改了 not already settled ≠ 已经交差 interchangeable：** 官方把改了和已经交差分开；355 prepare-drop vs mempool bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 把 t1 改成 t2 | 不是已经还能按 t1 查到 | 不是四门已经结算（33） |
| 看见 t2 进了块 | 不是已经有人知道 t2 来自 t1 | 不是没调 Prepare 就已经又装 raw（356/853） |
| 看见改了 | 不是已经交差 | 不是从提案拿掉就已经出池（854） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把 t1 改成 t2 not already can look up t1 / not already someone knows t2 from t1 / not already settled 正式三事（355 余量），必须分开是不是已经还能按 t1 查到、是不是已经有人知道 t2 来自 t1、是不是已经交差。可以跳过「看见 t1 没进块就已经还能按 t1 查到」。不要另写怎样改 Prepare 列表。355 prepare-drop vs mempool bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样改 Prepare 列表、怎样记派生哈希、怎样再检踢池。
- Prepare 改列表 bundled。那是不变量 355。
- 从提案拿掉 tx。那是不变量 355 item 1 余量 / 854。
- 四门已经结算。那是不变量 33。
- 没调 Prepare 就已经又装了一份 raw 提案。那是不变量 356 / 853。
