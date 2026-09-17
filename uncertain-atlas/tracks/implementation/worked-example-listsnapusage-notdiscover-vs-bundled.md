# 例：看见 discover on peers during state sync is not already ListSnapshots 空请求 bundled（395） interchangeable / ListSnapshots 本地清单 bundled（395） interchangeable / Snapshot Discovery 问了邻居就齐（322） interchangeable

**层次**：实现 / ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事（500 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事（500 余量）/ not 661 listsnapusage-notdiscover interchangeable / not 500 listsnapusage discover bundled interchangeable」，不是 ListSnapshots Usage discover / Snapshot type 正式二事 bundled（500），也不是 ListSnapshots 空请求 bundled（395）。不要另写怎样写 ListSnapshots、怎样列 Snapshot 类型。

## 官方三件事

规范把 ListSnapshots Usage 里 Used during state sync to discover available snapshots on peers 和「已经是 ListSnapshots 请求是空请求、向应用要一份快照清单 bundled（395） interchangeable / 已经是 ListSnapshots 回包 snapshots 是本地状态快照清单 bundled（395） interchangeable / 已经是 Snapshot Discovery 问了邻居就已经齐（322） interchangeable / 已经是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 discover on peers during state sync 就已经 ListSnapshots 空请求 bundled interchangeable / 就已经本地清单 interchangeable / 就已经问了邻居就齐 interchangeable / 就已经齐 interchangeable」一件事：

1. **看见 Used during state sync to discover available snapshots on peers / 看见在 state sync 时用来发现邻居上有哪些快照 is not already 已经 ListSnapshots 请求是空请求、向应用要一份快照清单 bundled（395） interchangeable / 395 listsnap bundled interchangeable / listsnapempty-sold-as-discovery interchangeable / 已经 ListSnapshots 空请求 bundled interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap accept/reject interchangeable / 322 listsnap discover interchangeable，也不是已经 ListSnapshots Usage discover / Snapshot type 正式二事 bundled（500） interchangeable / 661 listsnapusage-notdiscover interchangeable / 500 listsnapusage discover interchangeable / 659 loadsnapusage-notdiscover interchangeable / 501 loadsnapusage retrieve item 2 retrieve from peers interchangeable，也不是已经 discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事 bundled（500 item 1 余量） interchangeable / 500 listsnapusage discover item 1 interchangeable，也不是已经 See Snapshot data type for details not Snapshot 类型 bundled（500 item 2 余量） interchangeable / 662 listsnapusage-notsnaptype interchangeable / 368 snapshot-sold-as-identical interchangeable。**  
   官方 Usage 写：Used during state sync to discover available snapshots on peers。看见 discover on peers during state sync，不是已经 ListSnapshots 空请求 bundled（395） interchangeable——395 钉 Request/Response 栏和 Usage 发现句 bundled 三事，本页从 500 item 1 侧钉 not ListSnapshots 空请求 bundled 单句。看见 discover available snapshots on peers，不是已经 ListSnapshots Usage discover 单句 interchangeable——500 钉 bundled 二事，本页钉 Methods Usage discover on peers 单句。看见 during state sync，不是已经 LoadSnapshotChunk retrieve from peers interchangeable——659 另钉 LoadSnapshotChunk Usage retrieve item 2，本页钉 item 1 第一件事。500 listsnapusage discover unbundling 在本页 item 1 启动。

2. **看见 discover available snapshots on peers / discover on peers during state sync is not already 已经 ListSnapshots 回包 snapshots 是本地状态快照清单 bundled（395） interchangeable / 395 listsnap bundled interchangeable / listsnap-sold-as-listed interchangeable / 已经 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 bundled（395 第三件事） interchangeable / 368 snapshot-sold-as-identical interchangeable / 已经 ListSnapshots 本地清单 interchangeable，也不是已经 ListSnapshots Usage discover / Snapshot type 正式二事 bundled（500） interchangeable / 661 listsnapusage-notdiscover interchangeable / 500 listsnapusage discover item 1 discover on peers interchangeable / 659 loadsnapusage-notdiscover interchangeable / 647 offersnapusage-notlisted interchangeable，也不是已经 discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事 bundled（500 item 1 余量） interchangeable / 396 offersnap interchangeable / 483 offersnaptrust interchangeable / 396 OfferSnapshot 请求 bundled interchangeable，也不是已经 ListSnapshots 空请求 bundled（395） interchangeable / listsnapempty-sold-as-discovery interchangeable / 322 Snapshot Discovery interchangeable。**  
   官方把 Usage discover on peers 单句和 ListSnapshots Response 栏本地清单 bundled 分开——500 bundled 第一件事常与 395 混成「看见 discover on peers 就已经 ListSnapshots 回包 snapshots 是本地清单 interchangeable / 就已经本地清单 interchangeable」，本页钉 not ListSnapshots 本地清单 bundled 单句。看见 discover available snapshots on peers，不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable——395 钉本地清单栏，本页钉 Usage 侧发现邻居快照语义。看见 during state sync，不是已经 OfferSnapshot 请求 bundled（396） interchangeable——396 钉 Offer 请求栏，本页钉 item 1 第二件事。

3. **看见 during state sync / discover on peers during state sync is not already 已经 Snapshot Discovery 问了邻居就已经齐（322） interchangeable / 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap accept/reject interchangeable / 648 offersnapusage-notrestored interchangeable / 已经 Snapshot Connection 问了邻居 interchangeable，也不是已经 ListSnapshots Usage discover / Snapshot type 正式二事 bundled（500） interchangeable / 661 listsnapusage-notdiscover interchangeable / 500 listsnapusage discover item 1 discover on peers interchangeable / 659 loadsnapusage-notdiscover interchangeable / 501 loadsnapusage retrieve item 2 retrieve from peers interchangeable，也不是已经 discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事 bundled（500 item 1 余量） interchangeable / 500 listsnapusage discover item 2 See Snapshot data type interchangeable / 662 listsnapusage-notsnaptype interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable，也不是已经 ListSnapshots Used during state sync to discover on peers（500 bundled） interchangeable / listsnapusage-sold-as-bundled interchangeable / 395 listsnap bundled interchangeable。**  
   官方把 Usage discover on peers 单句和 app requirements Snapshot Discovery 路径分开——500 bundled 第一件事常与 322 混成「看见 discover on peers 就已经 Snapshot Discovery 问了邻居就齐 interchangeable / 就已经 ListSnapshots discover interchangeable」，本页钉 not Snapshot Discovery 单句。看见 during state sync，不是已经 Snapshot Discovery 问了邻居就已经齐 interchangeable——322 钉 app requirements Snapshot Discovery，本页钉 Methods ListSnapshots Usage 单句。看见 discover available snapshots on peers，不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 interchangeable——375 另钉 LoadSnapshotChunk bundled，本页钉 item 1 第三件事。500 listsnapusage discover unbundling 在本页 item 1 启动。

怎样做 ListSnapshots、怎样列 Snapshot 类型、怎样切块是规范里的做法，本页不抄。ListSnapshots Usage discover / Snapshot type 正式二事 bundled（500）、See Snapshot data type for details not Snapshot 类型 bundled（500 item 2 余量）、ListSnapshots 空请求 bundled（395）、Snapshot Discovery（322）、LoadSnapshotChunk 已经齐（375）、LoadSnapshotChunk Usage retrieve from peers（501 item 2 余量 / 659）是另外那套，本页不抄。

## 官方为什么这样拆

- **discover on peers not ListSnapshots 空请求 bundled ≠ 395 listsnap bundled interchangeable：** 官方把 Methods Usage discover 单句和 Request/Response bundled 分开。
- **discover on peers not ListSnapshots 本地清单 bundled ≠ 395 listsnap bundled 本地清单 interchangeable：** 官方把 Usage discover on peers 单句和 Response 栏本地清单 bundled 分开。
- **discover on peers not Snapshot Discovery ≠ 322 listsnap discover interchangeable：** 官方把 Usage discover on peers 单句和 app requirements Snapshot Discovery 路径分开；500 listsnapusage discover unbundling 启动（661 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| discover on peers during state sync | 不是 ListSnapshots 空请求 bundled（395） | 不是 LoadSnapshotChunk retrieve from peers（659/501） |
| discover available snapshots on peers | 不是 ListSnapshots 本地清单 bundled（395） | 不是 OfferSnapshot 请求 bundled（396） |
| during state sync | 不是 Snapshot Discovery（322） | 不是 See Snapshot data type（662/368） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事（500 余量），必须分开 discover on peers during state sync 是不是 ListSnapshots 空请求 bundled interchangeable / 395 listsnap bundled interchangeable / listsnapempty-sold-as-discovery interchangeable / 647 offersnapusage-notlisted interchangeable、discover available snapshots on peers 是不是 ListSnapshots 本地清单 bundled interchangeable / listsnap-sold-as-listed interchangeable / 396 offersnap interchangeable / 368 snapshot-sold-as-identical interchangeable、during state sync 是不是 Snapshot Discovery interchangeable / 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 499 offersnapusage item 1 bootstrap interchangeable。可以跳过「看见 discover on peers 就已经 ListSnapshots 空请求 bundled interchangeable / 就已经本地清单 interchangeable / 就已经问了邻居就齐 interchangeable」。不要另写怎样写 ListSnapshots、怎样列 Snapshot 类型。500 listsnapusage discover unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样做 ListSnapshots、怎样列 Snapshot 类型、怎样切块、怎样问邻居。
- ListSnapshots Usage discover / Snapshot type 正式二事 bundled。那是不变量 500。
- See Snapshot data type for details not Snapshot 类型 bundled。那是不变量 500 item 2 余量。
- ListSnapshots 空请求 bundled。那是不变量 395。
- Snapshot Discovery。那是不变量 322。
- LoadSnapshotChunk 已经齐。那是不变量 375。
- LoadSnapshotChunk Usage retrieve from peers。那是不变量 501 item 2 余量 / 659。
