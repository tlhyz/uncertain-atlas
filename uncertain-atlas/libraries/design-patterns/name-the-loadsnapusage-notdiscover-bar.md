# 模式：把 LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事（501 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover ≠ bundled（501）](../../tracks/implementation/worked-example-loadsnapusage-notdiscover-vs-bundled.md)。

## 三个名字

1. **retrieve from peers 不是 ListSnapshots discover：** 看见 retrieve snapshot chunks from peers，不是已经 ListSnapshots Used during state sync to discover on peers interchangeable，不是 500 listsnapusage-discover interchangeable / listsnapusage-sold-as-bundled interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap interchangeable。
2. **retrieve from peers 不是 ListSnapshots 空请求 bundled：** 看见 retrieve from peers，不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable，不是 395 listsnap bundled interchangeable / listsnap-sold-as-listed interchangeable / 396 offersnap interchangeable / 368 snapshot-sold-as-identical interchangeable。
3. **retrieve from peers 不是 Snapshot Discovery：** 看见 from peers，不是已经 Snapshot Discovery 问了邻居就已经齐 interchangeable，不是 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage item 1 bootstrap interchangeable。

## 为什么要分开叫

官方把 LoadSnapshotChunk Usage retrieve from peers 单句、ListSnapshots Usage discover（500）、ListSnapshots 空请求 bundled（395）、Snapshot Discovery（322）写成三个名字。把它们叫成一个「看见 retrieve from peers 就已经 ListSnapshots discover interchangeable / 就已经本地清单 interchangeable / 就已经问了邻居就齐 interchangeable」，会把 not ListSnapshots discover、not ListSnapshots 空请求 bundled、not Snapshot Discovery 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事（501 余量），先数清问的是 retrieve from peers 是不是 ListSnapshots discover / 500 / 647，是不是 ListSnapshots 空请求 bundled / 395 / 396，还是 from peers 是不是 Snapshot Discovery / 322 / 334 / 499，再决定要不要同一次发布。501 loadsnapusage retrieve unbundling 在本页 item 2 续。
