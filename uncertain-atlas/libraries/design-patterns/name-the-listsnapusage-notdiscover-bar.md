# 模式：把 ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事（500 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots Usage。  
**例**：[ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled ≠ bundled（500）](../../tracks/implementation/worked-example-listsnapusage-notdiscover-vs-bundled.md)。

## 三个名字

1. **discover on peers during state sync 不是 ListSnapshots 空请求 bundled：** 看见 Used during state sync to discover available snapshots on peers，不是已经 ListSnapshots 空请求 bundled interchangeable，不是 395 listsnap bundled interchangeable / listsnapempty-sold-as-discovery interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage item 1 bootstrap interchangeable / 659 loadsnapusage-notdiscover interchangeable。
2. **discover on peers 不是 ListSnapshots 本地清单 bundled：** 看见 discover available snapshots on peers，不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable，不是 395 listsnap bundled interchangeable / listsnap-sold-as-listed interchangeable / 396 offersnap interchangeable / 368 snapshot-sold-as-identical interchangeable。
3. **discover on peers 不是 Snapshot Discovery：** 看见 during state sync，不是已经 Snapshot Discovery 问了邻居就已经齐 interchangeable，不是 322 listsnap discover interchangeable / 334 snapshotconn interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage item 1 bootstrap interchangeable。

## 为什么要分开叫

官方把 ListSnapshots Usage discover on peers 单句、ListSnapshots 空请求 bundled（395）、ListSnapshots 本地清单 bundled（395）、Snapshot Discovery（322）写成三个名字。把它们叫成一个「看见 discover on peers 就已经 ListSnapshots 空请求 bundled interchangeable / 就已经本地清单 interchangeable / 就已经问了邻居就齐 interchangeable」，会把 not ListSnapshots 空请求 bundled、not ListSnapshots 本地清单 bundled、not Snapshot Discovery 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots Usage discover on peers not ListSnapshots 空请求 bundled / not ListSnapshots 本地清单 bundled / not Snapshot Discovery 正式三事（500 余量），先数清问的是 discover on peers 是不是 ListSnapshots 空请求 bundled / 395 / 647，是不是 discover available snapshots on peers 是不是 ListSnapshots 本地清单 bundled / 395 / 396，还是 during state sync 是不是 Snapshot Discovery / 322 / 334 / 499，再决定要不要同一次发布。500 listsnapusage discover unbundling 在本页 item 1 启动。
