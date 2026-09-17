# 反模式：把 ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事（500 余量）说成已经 ListSnapshots 空请求 bundled / 已经本地清单 / 已经问了邻居就齐

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled ≠ bundled（500）](../../tracks/implementation/worked-example-listsnapusage-notdiscover-vs-bundled.md)。

## 错在哪里

把 Used during state sync to discover available snapshots on peers 写成已经 ListSnapshots 空请求 bundled interchangeable / 395 listsnap bundled interchangeable / listsnapempty-sold-as-discovery interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap interchangeable / 659 loadsnapusage-notdiscover interchangeable；把 discover available snapshots on peers 写成已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable / listsnap-sold-as-listed interchangeable / 396 offersnap interchangeable / 368 snapshot-sold-as-identical interchangeable；把 during state sync 写成已经 Snapshot Discovery 问了邻居就已经齐 interchangeable / 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 648 offersnapusage-notrestored interchangeable，或已经和 500 listsnapusage discover bundled / listsnapusage-sold-as-bundled / 501 loadsnapusage retrieve item 2 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事（500 余量），必须分开 not ListSnapshots 空请求 bundled、not ListSnapshots 本地清单 bundled、not Snapshot Discovery 三件事，不要和 500 / 395 / 322 / 659 / 647 / 499 / 648 / 334 / 375 / 396 / 662 糊成一句。

## 和相邻反模式

- [listsnapusage-sold-as-bundled](listsnapusage-sold-as-bundled.md) 是 ListSnapshots Usage discover / Snapshot type 专用 bundled（500），不是本页 500 item 1 单句边界。
- [listsnapempty-sold-as-discovery](listsnapempty-sold-as-discovery.md) 是 ListSnapshots 空请求 bundled 三事（395），不是本页 Methods Usage discover on peers 单句边界。
- [loadsnapusage-notdiscover-sold-as-bundled](loadsnapusage-notdiscover-sold-as-bundled.md) 是 501 item 2 余量 / 659 专用 retrieve from peers，不是本页 discover on peers 单句边界。
