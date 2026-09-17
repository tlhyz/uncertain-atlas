# 模式：把 ListSnapshots Usage See Snapshot data type for details not Snapshot 类型 bundled / not Offer 装完 / not ListSnapshots 本地清单就已经是同一份 正式三事（500 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots Usage。  
**例**：[ListSnapshots Usage See Snapshot data type not Snapshot 类型 bundled ≠ bundled（500）](../../tracks/implementation/worked-example-listsnapusage-notsnaptype-vs-bundled.md)。

## 三个名字

1. **See Snapshot data type for details 不是 Snapshot 类型 bundled：** 看见 See `Snapshot` data type for details，不是已经 Snapshot 类型 five fields / format / hash / chunks bundled interchangeable，不是 368 snapshot-sold-as-identical interchangeable / 650 offersnaptrust-notmetadata interchangeable / 396 offersnap interchangeable / 647 offersnapusage-notlisted interchangeable。
2. **See Snapshot data type for details 不是 Offer 装完：** 看见 for details，不是已经 Offer 收下就已经装完 interchangeable，不是 321 offerrestored interchangeable / 648 offersnapusage-notrestored interchangeable / 401 offerafter interchangeable / 499 offersnapusage item 2 upon accepting retrieve and apply interchangeable。
3. **See Snapshot data type for details 不是 ListSnapshots 本地清单就已经是同一份：** 看见 Snapshot data type，不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单 interchangeable，不是 395 listsnap bundled interchangeable / listsnap-sold-as-listed interchangeable / 483 offersnaptrust interchangeable / 653 applysnapusage-notverify interchangeable / 332 snapshotverify interchangeable / 661 listsnapusage-notdiscover interchangeable。

## 为什么要分开叫

官方把 ListSnapshots Usage See Snapshot data type 单句、Snapshot 类型 bundled（368）、Offer 装完（321/401）、ListSnapshots 本地清单 / Only AppHash（395/483）写成三个名字。把它们叫成一个「看见 See Snapshot data type 就已经 five fields 对上 interchangeable / 就已经装完 interchangeable / 就已经 Only AppHash interchangeable」，会把 not Snapshot 类型 bundled、not Offer 装完、not ListSnapshots 本地清单就已经是同一份 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots Usage See Snapshot data type for details not Snapshot 类型 bundled / not Offer 装完 / not ListSnapshots 本地清单就已经是同一份 正式三事（500 余量），先数清问的是 See Snapshot data type 是不是 Snapshot 类型 bundled / 368 / 650，是不是 for details 是不是 Offer 装完 / 321 / 648 / 401，还是 Snapshot data type 是不是 ListSnapshots 本地清单就已经是同一份 / 395 / 483 / 653 / 332，再决定要不要同一次发布。500 listsnapusage discover unbundling 在本页 item 2 完成。
