# 例：看见 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 is not already loading chunks interchangeable / not already complete interchangeable / not already Usage discover interchangeable

**层次**：实现 / ListSnapshots 用来发现 not already loading chunks / not already complete / not Usage discover 正式三事（395 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ListSnapshots 用来发现 not already loading chunks / not already complete / not Usage discover 正式三事（395 余量）/ not 736 listsnapempty-notchunks interchangeable / not 395 listsnapempty-vs-discovery bundled interchangeable」，不是 ListSnapshots 空请求 bundled（395），也不是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375）或 ListSnapshots Usage discover（500 / 661）。不要另写怎样写 ListSnapshots 空请求。

## 官方三件事

1. **看见 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 / 看见用来发现 / 用来发现 is not already 已经在从邻居拉快照块 interchangeable / 375 loadsnap interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / 736 listsnapempty-notchunks interchangeable / 734 listsnapempty-notcomplete interchangeable / 395 listsnapempty item 1 空请求 interchangeable，也不是已经用来发现 not already loading chunks / not already complete / not Usage discover 正式三事 bundled（395 item 3 余量） interchangeable / 395 listsnapempty item 3 interchangeable。**  
   官方写：用来在 state sync 时发现邻居上有哪些快照。看见用来发现，不是已经在从邻居拉快照块 interchangeable——本页从 395 item 3 侧钉 not already loading chunks 单句。395 listsnapempty vs discovery bundled unbundling 在本页 item 3 完成。

2. **看见用来发现 / 看见能发现 / 用来发现 is not already 已经齐 interchangeable / 322 snapdiscover interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / 736 listsnapempty-notchunks interchangeable / 395 listsnapempty item 2 本地清单 interchangeable / 735 listsnapempty-notidentical interchangeable。**  
   官方把能发现和已经齐分开——395 bundled 第三件事常与 322 混成「看见用来发现就已经齐 interchangeable」，本页钉 not already complete 单句。

3. **看见用来发现 / 看见能填 / 用来发现 is not already 已经 ListSnapshots Usage discover on peers interchangeable / 500 / 661 listsnapusage-notdiscover interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / 736 listsnapempty-notchunks interchangeable / 734 listsnapempty-notcomplete interchangeable。**  
   官方把 395 侧用来发现和 500 Usage discover 分开。看见能填，不是已经 661 interchangeable。395 listsnapempty vs discovery bundled unbundling 在本页 item 3 完成。

怎样写 ListSnapshots 空请求、怎样填空请求、怎样填本地清单是规范里的做法，本页不抄。

## 官方为什么这样拆

- **用来发现 not already loading chunks ≠ 375 interchangeable：** 官方把发现清单和拉块分开。
- **用来发现 not already complete ≠ 322 interchangeable：** 官方把能发现和已经齐分开。
- **用来发现 not Usage discover ≠ 500 / 661 interchangeable：** 官方把 395 侧用来发现和 500 Usage discover 分开；395 listsnapempty vs discovery bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 | 不是已经在拉块（375） | 不是空请求要清单（734/395 item 1） |
| 看见用来发现 | 不是已经齐（322） | 不是 ListSnapshots 空请求 bundled（395） |
| 看见能填 | 不是已经 Usage discover（500 / 661） | 不是本地清单（735/395 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 用来发现 not already loading chunks / not already complete / not Usage discover 正式三事（395 余量），必须分开用来发现是不是已经在拉块 interchangeable / 375、是不是已经齐 interchangeable / 322、是不是已经 Usage discover interchangeable / 500 / 661。可以跳过「看见用来发现就已经在拉块」。不要另写怎样写 ListSnapshots 空请求。395 listsnapempty vs discovery bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ListSnapshots 空请求、怎样填空请求、怎样填本地清单。
- ListSnapshots 空请求 bundled。那是不变量 395。
- ListSnapshots 空请求要清单。那是不变量 395 item 1 余量 / 734。
- ListSnapshots 回包 snapshots 是本地状态快照清单。那是不变量 395 item 2 余量 / 735。
- LoadSnapshotChunk 用来从邻居拉快照块就已经齐。那是不变量 375。
- 问了邻居就已经齐。那是不变量 322。
- ListSnapshots Usage discover。那是不变量 500 / 661。
