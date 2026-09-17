# 模式：把 OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled / not ListSnapshots / not Snapshot Connection 正式三事（499 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled ≠ bundled（499）](../../tracks/implementation/worked-example-offersnapusage-notlisted-vs-bundled.md)。

## 三个名字

1. **bootstrapping may accept/reject 不是 OfferSnapshot 请求 bundled：** 看见 `OfferSnapshot` is called when bootstrapping a node using state sync / application may accept or reject snapshots as appropriate，不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 396 offersnap interchangeable / 398 result 栏 interchangeable，也不是 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable。
2. **bootstrapping may accept/reject 不是 ListSnapshots 发现：** 看见 bootstrapping using state sync / may accept or reject，不是已经 ListSnapshots 发现（322） interchangeable / 322 listsnap interchangeable / 395 本地清单 interchangeable / 500 discover interchangeable。
3. **bootstrapping may accept/reject 不是 Snapshot Connection / offersnapusage bundled：** 看见 bootstrapping may accept/reject，不是已经 Snapshot Connection 门（334） interchangeable / 334 snapshotconn interchangeable / 483 Only AppHash trusted interchangeable，也不是 499 offersnapusage bundled interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable。

## 为什么要分开叫

官方把 OfferSnapshot Usage bootstrap may accept/reject、ListSnapshots 发现、Snapshot Connection / offersnapusage bundled 三事 写成三个名字。把它们叫成一个「看见 bootstrapping may accept/reject 就已经 OfferSnapshot 请求 bundled interchangeable / 就已经 ListSnapshots 问了邻居 interchangeable / 就已经必须实现快照连接 interchangeable」，会把 not OfferSnapshot bundled、not ListSnapshots、not Snapshot Connection / not offersnapusage bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled / not ListSnapshots / not Snapshot Connection 正式三事（499 余量），先数清问的是 bootstrapping may accept/reject 是不是 OfferSnapshot 请求 bundled / 396 / 398，是不是 ListSnapshots 发现 / 322 / 395 / 500，还是 bootstrapping may accept/reject 是不是 Snapshot Connection / offersnapusage bundled / 334 / 483 / 648 / 649，再决定要不要同一次发布。499 offersnapusage unbundling 在本页 item 1 启动。
