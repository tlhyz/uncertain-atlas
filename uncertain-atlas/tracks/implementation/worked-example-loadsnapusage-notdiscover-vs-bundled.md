# 例：看见 retrieve from peers is not already ListSnapshots discover on peers（500） interchangeable / ListSnapshots 空请求 bundled（395） interchangeable / Snapshot Discovery 问了邻居就齐（322） interchangeable

**层次**：实现 / LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事（501 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事（501 余量）/ not 659 loadsnapusage-notdiscover interchangeable / not 658 loadsnapusage-notretrieve interchangeable / not 501 loadsnapusage retrieve bundled interchangeable」，不是 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501），也不是 ListSnapshots Usage discover on peers（500）。不要另写怎样写 LoadSnapshotChunk、怎样切块、怎样写 ListSnapshots。

## 官方三件事

规范把 LoadSnapshotChunk Usage 里 retrieve snapshot chunks from peers 和「已经是 ListSnapshots Used during state sync to discover on peers（500） interchangeable / 已经是 ListSnapshots 空请求 bundled（395） interchangeable / 已经本地清单 interchangeable / 已经是 Snapshot Discovery 问了邻居就已经齐（322） interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 retrieve from peers 就已经 ListSnapshots discover interchangeable / 就已经本地清单 interchangeable / 就已经问了邻居就齐 interchangeable / 就已经齐 interchangeable」一件事：

1. **看见 retrieve snapshot chunks from peers / 看见从邻居拉块 is not already 已经 ListSnapshots Used during state sync to discover on peers（500） interchangeable / 500 listsnapusage-discover interchangeable / listsnapusage-sold-as-bundled interchangeable / 已经 ListSnapshots Usage discover 单句 interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap accept/reject interchangeable / 322 listsnap discover interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 659 loadsnapusage-notdiscover interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve interchangeable / 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable，也不是已经 retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事 bundled（501 item 2 余量） interchangeable / 501 loadsnapusage retrieve item 2 interchangeable，也不是已经 Used during state sync to retrieve not LoadSnapshotChunk bundled（501 item 1 余量 / 658） interchangeable / 658 loadsnapusage-notretrieve interchangeable / 375 LoadSnapshotChunk bundled interchangeable。**  
   官方 Usage 写：retrieve snapshot chunks from peers。看见 retrieve from peers，不是已经 ListSnapshots Usage discover on peers（500） interchangeable——500 钉 ListSnapshots Usage discover 单句，本页从 501 item 2 侧钉 not ListSnapshots discover 单句。看见从邻居拉块，不是已经 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 interchangeable——395 另钉本地清单栏，本页钉 Methods LoadSnapshotChunk Usage retrieve 单句。看见 snapshot chunks from peers，不是已经 LoadSnapshotChunk bundled（375） interchangeable——658 另钉 Used during state sync to retrieve not LoadSnapshotChunk bundled，本页钉 item 2 第一件事。501 loadsnapusage retrieve unbundling 在本页 item 2 续。

2. **看见 retrieve from peers / retrieve snapshot chunks from peers is not already 已经 ListSnapshots 空请求 bundled（395） interchangeable / 395 listsnap bundled interchangeable / listsnap-sold-as-listed interchangeable / 已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable / 已经 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 bundled（395 第三件事） interchangeable / 368 snapshot-sold-as-identical interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 659 loadsnapusage-notdiscover interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve item 2 retrieve from peers interchangeable / 500 listsnapusage-discover interchangeable / 647 offersnapusage-notlisted interchangeable，也不是已经 retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事 bundled（501 item 2 余量） interchangeable / 396 offersnap interchangeable / 483 offersnaptrust interchangeable / 396 OfferSnapshot 请求 bundled interchangeable，也不是已经 ListSnapshots Used during state sync to discover on peers（500） interchangeable / 500 listsnapusage-discover interchangeable / 322 Snapshot Discovery interchangeable。**  
   官方把 Usage retrieve from peers 单句和 ListSnapshots Response 栏本地清单 bundled 分开——501 bundled 第二件事常与 395 混成「看见 retrieve from peers 就已经 ListSnapshots 回包 snapshots 是本地清单 interchangeable / 就已经本地清单 interchangeable」，本页钉 not ListSnapshots 空请求 bundled 单句。看见 retrieve from peers，不是已经 ListSnapshots 空请求 bundled（395） interchangeable——395 钉 Request/Response 栏和 Usage 发现 bundled 三事，本页钉 Methods Usage retrieve 单句。看见从邻居拉块，不是已经 OfferSnapshot 请求 bundled（396） interchangeable——396 钉 Offer 请求栏，本页钉 item 2 第二件事。

3. **看见 from peers / retrieve snapshot chunks from peers is not already 已经 Snapshot Discovery 问了邻居就已经齐（322） interchangeable / 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap accept/reject interchangeable / 648 offersnapusage-notrestored interchangeable / 已经 Snapshot Connection 问了邻居 interchangeable，也不是已经 LoadSnapshotChunk Usage retrieve 正式三事 bundled（501） interchangeable / 659 loadsnapusage-notdiscover interchangeable / 658 loadsnapusage-notretrieve interchangeable / 501 loadsnapusage retrieve item 2 retrieve from peers interchangeable / 500 listsnapusage-discover interchangeable / 395 listsnap bundled interchangeable，也不是已经 retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事 bundled（501 item 2 余量） interchangeable / 501 loadsnapusage retrieve item 3 retrieve chunks interchangeable / 660 loadsnapusage-notchunks interchangeable / 397 applysnap-chunk interchangeable，也不是已经 ListSnapshots discover on peers（500） interchangeable / 500 listsnapusage-discover interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable。**  
   官方把 Usage retrieve from peers 单句和 app requirements Snapshot Discovery 路径分开——501 bundled 第二件事常与 322 混成「看见 retrieve from peers 就已经 Snapshot Discovery 问了邻居就齐 interchangeable / 就已经 ListSnapshots discover interchangeable」，本页钉 not Snapshot Discovery 单句。看见 from peers，不是已经 Snapshot Discovery 问了邻居就已经齐 interchangeable——322 钉 app requirements Snapshot Discovery，本页钉 Methods LoadSnapshotChunk Usage retrieve 单句。看见 retrieve snapshot chunks from peers，不是已经 retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 interchangeable——660 另钉 item 3，本页钉 item 2 第三件事。501 loadsnapusage retrieve unbundling 在本页 item 2 续。

怎样做 LoadSnapshotChunk、怎样切块、怎样写 ListSnapshots 是规范里的做法，本页不抄。LoadSnapshotChunk Usage retrieve 正式三事 bundled（501）、Used during state sync to retrieve not LoadSnapshotChunk bundled（501 item 1 余量 / 658）、retrieve snapshot chunks not ApplySnapshotChunk chunk 栏（501 item 3 余量）、ListSnapshots Usage discover on peers（500）、ListSnapshots 空请求 bundled（395）、Snapshot Discovery（322）、LoadSnapshotChunk bundled（375）是另外那套，本页不抄。

## 官方为什么这样拆

- **retrieve from peers not ListSnapshots discover ≠ 500 listsnapusage-discover interchangeable：** 官方把 LoadSnapshotChunk Usage retrieve 单句和 ListSnapshots Usage discover 单句分开。
- **retrieve from peers not ListSnapshots 空请求 bundled ≠ 395 listsnap bundled interchangeable：** 官方把 Usage retrieve from peers 单句和 ListSnapshots Response 栏本地清单 bundled 分开。
- **retrieve from peers not Snapshot Discovery ≠ 322 listsnap discover interchangeable：** 官方把 Usage retrieve from peers 单句和 app requirements Snapshot Discovery 路径分开；501 loadsnapusage retrieve unbundling 续（659 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| retrieve from peers | 不是 ListSnapshots discover（500） | 不是 Used during state sync to retrieve（658） |
| retrieve from peers | 不是 ListSnapshots 空请求 bundled（395） | 不是 OfferSnapshot 请求 bundled（396） |
| from peers | 不是 Snapshot Discovery（322） | 不是 retrieve chunks / ApplySnapshotChunk chunk 栏（660/397） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事（501 余量），必须分开 retrieve from peers 是不是 ListSnapshots discover interchangeable / 500 listsnapusage-discover interchangeable / listsnapusage-sold-as-bundled interchangeable / 647 offersnapusage-notlisted interchangeable、retrieve from peers 是不是 ListSnapshots 空请求 bundled interchangeable / 395 listsnap bundled interchangeable / listsnap-sold-as-listed interchangeable / 396 offersnap interchangeable、from peers 是不是 Snapshot Discovery interchangeable / 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 499 offersnapusage item 1 bootstrap interchangeable。可以跳过「看见 retrieve from peers 就已经 ListSnapshots discover interchangeable / 就已经本地清单 interchangeable / 就已经问了邻居就齐 interchangeable」。不要另写怎样写 LoadSnapshotChunk、怎样写 ListSnapshots。501 loadsnapusage retrieve unbundling 在本页 item 2 续。

## 本页不抄

- 怎样做 LoadSnapshotChunk、怎样切块、怎样写 ListSnapshots、怎样问邻居。
- LoadSnapshotChunk Usage retrieve 正式三事 bundled。那是不变量 501。
- Used during state sync to retrieve not LoadSnapshotChunk bundled。那是不变量 501 item 1 余量 / 658。
- retrieve snapshot chunks not ApplySnapshotChunk chunk 栏。那是不变量 501 item 3 余量。
- ListSnapshots Usage discover on peers。那是不变量 500。
- ListSnapshots 空请求 bundled。那是不变量 395。
- Snapshot Discovery。那是不变量 322。
- LoadSnapshotChunk bundled。那是不变量 375。
