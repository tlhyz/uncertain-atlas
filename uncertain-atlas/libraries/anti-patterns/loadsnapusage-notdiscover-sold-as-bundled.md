# 反模式：把 LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事（501 余量）说成已经 ListSnapshots discover / 已经本地清单 / 已经问了邻居就齐

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover ≠ bundled（501）](../../tracks/implementation/worked-example-loadsnapusage-notdiscover-vs-bundled.md)。

## 错在哪里

把 retrieve snapshot chunks from peers 写成已经 ListSnapshots Used during state sync to discover on peers interchangeable / 500 listsnapusage-discover interchangeable / listsnapusage-sold-as-bundled interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap interchangeable；把 retrieve from peers 写成已经 ListSnapshots 空请求 bundled interchangeable / 395 listsnap bundled interchangeable / listsnap-sold-as-listed interchangeable / 396 offersnap interchangeable / 368 snapshot-sold-as-identical interchangeable；把 from peers 写成已经 Snapshot Discovery 问了邻居就已经齐 interchangeable / 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 648 offersnapusage-notrestored interchangeable，或已经和 501 loadsnapusage retrieve bundled / loadsnapusage-sold-as-bundled / 658 loadsnapusage-notretrieve interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve from peers not ListSnapshots discover / not ListSnapshots 空请求 bundled / not Snapshot Discovery 正式三事（501 余量），必须分开 not ListSnapshots discover、not ListSnapshots 空请求 bundled、not Snapshot Discovery 三件事，不要和 501 / 500 / 395 / 322 / 658 / 647 / 499 / 648 / 334 / 375 糊成一句。

## 和相邻反模式

- [loadsnapusage-sold-as-bundled](loadsnapusage-sold-as-bundled.md) 是 LoadSnapshotChunk Usage retrieve 专用 bundled（501），不是本页 501 item 2 单句边界。
- [listsnapusage-sold-as-bundled](listsnapusage-sold-as-bundled.md) 是 ListSnapshots Usage discover / Snapshot type 正式二事（500），不是本页 not ListSnapshots discover 单句边界。
- [loadsnapusage-notretrieve-sold-as-bundled](loadsnapusage-notretrieve-sold-as-bundled.md) 是 501 item 1 余量 / 658 专用 Used during state sync to retrieve，不是本页 retrieve from peers 单句边界。
