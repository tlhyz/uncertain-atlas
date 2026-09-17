# 例：看见全网都删了会永久丢 is not already genesis reload interchangeable / not already light-client verify interchangeable / not already settled interchangeable

**层次**：实现 / 全网都删会永久丢 not already genesis reload / not already light-client verify / not already settled 正式三事（366 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「全网都删会永久丢 not already genesis reload / not already light-client verify / not already settled 正式三事（366 余量）/ not 829 retain-notgenesis interchangeable / not 366 retain-vs-kept bundled interchangeable」，不是 Commit 保留高度 bundled（366），也不是应用快照就已经从创世重放（38），也不是 Commit Usage retain_height caution 从创世（491/693），也不是切进共识就已经有完整历史（323）。不要另写怎样写 Commit 保留高度。

## 官方三件事

1. **看见全网都删了会永久丢、除非开了 state sync / 看见能剪 / 这份永久丢 is not already 已经能从创世再装 interchangeable / 38 snapshotreplay interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 829 retain-notgenesis interchangeable / 827 retain-notpruning interchangeable / 366 retain item 1 默认 0 interchangeable，也不是已经全网都删会永久丢 not already genesis reload / not already light-client verify / not already settled 正式三事 bundled（366 item 3 余量） interchangeable / 366 retain item 3 interchangeable。**  
   官方写：若网上所有节点都删了历史块，这些数据就永久丢了；除非链上开了 state sync，否则新节点加不进来。看见能剪，不是已经能从创世再装 interchangeable——本页从 366 item 3 侧钉 not already genesis reload 单句。366 retain vs kept bundled unbundling 在本页 item 3 完成。

2. **看见能剪 / 看见开了 state sync / 这份永久丢 is not already 已经能给轻客户端验 interchangeable / 38 snapshotreplay interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 829 retain-notgenesis interchangeable / 366 retain item 2 可删 interchangeable / 828 retain-nothistory interchangeable，也不是已经应用快照就已经从创世重放 interchangeable / 38 snapshotreplay interchangeable，也不是已经 Commit Usage retain_height caution 从创世 interchangeable / 491 retaincaution / 693 commitretaincaution-notgenesis interchangeable。**  
   官方把开了 state sync 和已经能给轻客户端验分开——366 bundled 第三件事常与 38 / 491 混成「看见能剪就已经能从创世再装或已经能给轻客户端验 interchangeable」，本页钉 not already light-client verify 单句。

3. **看见能剪 / 看见能丢 / 这份永久丢 is not already 已经交差 interchangeable，也不是已经 Commit 保留高度 bundled（366） interchangeable / 829 retain-notgenesis interchangeable / 827 retain-notpruning interchangeable，也不是已经切进共识就已经有完整历史 interchangeable / 323 history interchangeable。**  
   官方把能丢和已经交差分开。看见能丢，不是已经交差 interchangeable。366 retain vs kept bundled unbundling 在本页 item 3 完成。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **全网都删会永久丢 not already genesis reload ≠ 38 interchangeable：** 官方把能剪和还能从创世核验分开。
- **看见开了 state sync not already light-client verify ≠ 已经能给轻客户端验 interchangeable：** 官方把开了 state sync 和已经能给轻客户端验分开。
- **看见能丢 not already settled ≠ 已经交差 interchangeable：** 官方把能丢和已经交差分开；366 retain vs kept bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 全网都删了会永久丢 | 不是已经能从创世再装（38） | 不是默认 0（827/366 item 1） |
| 看见开了 state sync | 不是已经能给轻客户端验 | 不是 retain_height caution 从创世（491/693） |
| 看见能丢 | 不是已经交差 | 不是切进共识就已经有完整历史（323） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看全网都删会永久丢 not already genesis reload / not already light-client verify / not already settled 正式三事（366 余量），必须分开是不是已经能从创世再装 interchangeable / 38、是不是已经能给轻客户端验、是不是已经交差。可以跳过「看见能剪就已经能从创世再装」。不要另写怎样写 Commit 保留高度。366 retain vs kept bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit 保留高度 bundled。那是不变量 366。
- retain_height 默认 0。那是不变量 366 item 1 余量 / 827。
- 应用快照就已经从创世重放。那是不变量 38。
- Commit Usage retain_height caution 从创世。那是不变量 491 / 693。
