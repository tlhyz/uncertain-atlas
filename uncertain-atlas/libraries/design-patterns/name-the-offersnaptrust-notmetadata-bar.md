# 模式：把 OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事（483 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata ≠ bundled（483）](../../tracks/implementation/worked-example-offersnaptrust-notmetadata-vs-bundled.md)。

## 三个名字

1. **Only AppHash can be trusted 不是 Snapshot metadata：** 看见 Only AppHash can be trusted, as it has been verified by the light client，不是已经 Snapshot.hash / metadata / 五个字段都对上就可信 interchangeable，不是 368 snapshot-sold-as-identical interchangeable / 395 本地清单 interchangeable，也不是 483 offersnaptrust bundled interchangeable / 650 offersnaptrust-notmetadata interchangeable。
2. **Only AppHash can be trusted 不是 hash 比对就够：** 看见 only AppHash / light client verified，不是已经引擎 hash 比对就等于轻验 interchangeable，不是 368 hash comparison interchangeable / 651 offersnaptrust-notverify interchangeable / 332 snapshotverify interchangeable。
3. **Only AppHash can be trusted 不是 OfferSnapshot app_hash：** 看见 Only AppHash can be trusted，不是已经 OfferSnapshot 请求 app_hash 填了 interchangeable，不是 396 offersnap interchangeable / 398 result 栏 interchangeable / 652 offersnaptrust-nottransition interchangeable。

## 为什么要分开叫

官方把 OfferSnapshot Usage Only AppHash can be trusted、Snapshot 元数据/全字段对上、引擎 hash 比较、OfferSnapshot 请求 app_hash 栏 写成三个名字。把它们叫成一个「看见 Only AppHash can be trusted 就已经 Snapshot 字段都可信 interchangeable / 就已经 hash 比对 interchangeable / 就已经 Offer 了 AppHash interchangeable」，会把 not Snapshot metadata、not hash comparison、not OfferSnapshot app_hash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事（483 余量），先数清问的是 Only AppHash can be trusted 是不是 Snapshot metadata / 368 / 395，是不是 hash 比对 / 368 / 651 / 332，还是 Only AppHash can be trusted 是不是 OfferSnapshot app_hash / 396 / 398 / 652，再决定要不要同一次发布。483 offersnaptrust unbundling 在本页 item 1 启动。
