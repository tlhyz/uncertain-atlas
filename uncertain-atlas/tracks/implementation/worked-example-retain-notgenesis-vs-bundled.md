# 例：看见全网都删会永久丢 / 看见开了 state sync / 看见能丢 is not already already genesis-replay interchangeable / already light-check interchangeable / already settled interchangeable

**层次**：实现 / 全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事（366 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事（366 余量）/ not 847 retain-notgenesis interchangeable / not 366 retain bundled interchangeable」，不是 retain bundled（366），也不是 retain_height 默认 0 不是已经在剪（845 item 1 余量）或低于这个高度的块可以被删不是已经没有历史（846 item 2 余量）。不要另写怎样写 Commit 保留高度。

## 官方三件事

规范把 Methods 里若网上所有节点都删了历史块则永久丢、除非开了 state sync 否则新节点加不进来 和「已经是全网都删就已经能从创世再装 interchangeable / 已经是开了 state sync 就已经能给轻客户端验 interchangeable / 已经是能丢就已经交差 interchangeable / 已经是 retain bundled interchangeable」分开写成三件独立的实现事，不是「看见全网都删会永久丢就已经能从创世再装 interchangeable / 就已经能给轻客户端验 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见全网都删会永久丢 / 看见若网上所有节点都删了历史块、这些数据就永久丢了 / 看见能剪会丢 is not already 已经能从创世再装 interchangeable / 已经 genesis-replay interchangeable / 已经从创世再装交差 interchangeable / 366 retain bundled interchangeable / 38 genesis-replay interchangeable / retain-sold-as-kept interchangeable，也不是已经 retain bundled（366） interchangeable / 847 retain-notgenesis interchangeable / 366 retain item 3 interchangeable，也不是已经全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事 bundled（366 item 3 余量） interchangeable / 366 retain item 3 interchangeable，也不是已经默认 0 全留就已经在剪（845） interchangeable / 846 retain-notdeleted interchangeable / 323 full-history interchangeable，也不是已经应用快照就已经从创世重放（38） interchangeable。**  
   官方写：若网上所有节点都删了历史块，这些数据就永久丢了。看见全网都删会永久丢，不是已经能从创世再装。看见全网都删会永久丢，不是已经 genesis-replay interchangeable——366 钉 bundled 三事，本页从 item 3 侧钉 not already genesis-replay 单句。看见若网上所有节点都删了历史块、这些数据就永久丢了，不是已经 retain bundled（366） interchangeable——366 钉 bundled，本页钉 item 3 第一件事。看见全网都删会永久丢，不是已经默认 0 全留就已经在剪（845） interchangeable——845 另钉 item 1。看见全网都删会永久丢，不是已经能删就没有历史（846） interchangeable——846 另钉 item 2。366 retain-vs-kept bundled unbundling 在本页 item 3 完成。

2. **看见开了 state sync / 看见除非链上开了 state sync、否则新节点加不进来 / 看见能引导 is not already 已经能给轻客户端验 interchangeable / 已经 light-check interchangeable / 已经轻客户端验交差 interchangeable / 366 retain bundled interchangeable / 323 full-history interchangeable，也不是已经 retain bundled（366） interchangeable / 847 retain-notgenesis interchangeable / 366 retain item 1 默认 0 interchangeable / 366 retain item 2 可删 interchangeable，也不是已经全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事 bundled（366 item 3 余量） interchangeable / 366 retain item 3 interchangeable，也不是已经能从创世再装（本页第一件事） interchangeable。**  
   官方写：看见开了 state sync，不是已经能给轻客户端验。看见除非链上开了 state sync、否则新节点加不进来，不是已经 light-check interchangeable——本页钉 not already light-check 单句。看见能引导，不是已经能从创世再装（本页第一件事） interchangeable——三件事分开钉。366 retain-vs-kept bundled unbundling 在本页 item 3 完成。

3. **看见能丢 / 看见能剪会永久丢 / 看见审计回放轻客户端还可能要用 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 366 retain bundled interchangeable / 33 fourgates interchangeable，也不是已经 retain bundled（366） interchangeable / 847 retain-notgenesis interchangeable / 366 retain item 1 / 366 retain item 2，也不是已经全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事 bundled（366 item 3 余量） interchangeable / 366 retain item 3 interchangeable，也不是已经能从创世再装（本页第一件事） interchangeable / 已经能给轻客户端验（本页第二件事） interchangeable。**  
   官方写：看见能丢，不是已经交差。看见能剪会永久丢，不是已经 settled interchangeable——本页钉 not already settled 单句。看见审计回放轻客户端还可能要用，不是已经能给轻客户端验（本页第二件事） interchangeable——三件事分开钉。366 retain-vs-kept bundled unbundling 在本页 item 3 完成。

怎样填 `retain_height`、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。retain bundled（366）、retain_height 默认 0 不是已经在剪（366 item 1 余量 / 845）、低于这个高度的块可以被删不是已经没有历史（366 item 2 余量 / 846）、崩溃三步就已经 Commit（320）、切进共识就已经有完整历史（323）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **全网都删会永久丢 not already genesis-replay ≠ 366 / 38 interchangeable：** 官方把能剪永久丢和已经能从创世再装分开。
- **开了 state sync not already light-check ≠ 已经能给轻客户端验 interchangeable：** 官方把能引导和已经能给轻客户端验分开。
- **能丢 not already settled ≠ 已经交差 interchangeable：** 官方把能丢和已经交差分开；366 retain-vs-kept bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 全网都删会永久丢 | 不是 already genesis-replay | 不是应用快照就已经从创世重放 alone（38） |
| 开了 state sync | 不是 already light-check | 不是默认 0 全留 already pruning alone（845） |
| 能丢 | 不是 already settled | 不是能删 already no-history alone（846） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事（366 余量），必须分开全网都删会永久丢 是不是 already genesis-replay interchangeable / 366 retain bundled interchangeable / retain-sold-as-kept interchangeable、开了 state sync 是不是 already light-check interchangeable、能丢 是不是 already settled interchangeable。可以跳过「看见全网都删会永久丢就已经能从创世再装 interchangeable / 就已经能给轻客户端验 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Commit 保留高度。366 retain-vs-kept bundled unbundling 在本页 item 3 完成（845 + 846 + 847）。

## 本页不抄

- 怎样填 `retain_height`、怎样删块、怎样开 state sync。
- retain bundled。那是不变量 366。
- retain_height 默认 0 不是已经在剪。那是不变量 366 item 1 余量 / 845。
- 低于这个高度的块可以被删不是已经没有历史。那是不变量 366 item 2 余量 / 846。
- 崩溃三步就已经 Commit。那是不变量 320。
- 切进共识就已经有完整历史。那是不变量 323。
- 应用快照就已经从创世重放。那是不变量 38。
