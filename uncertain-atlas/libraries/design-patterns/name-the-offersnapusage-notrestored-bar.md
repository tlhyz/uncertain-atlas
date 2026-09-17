# 模式：把 OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 / not Offer 收下之后 bundled / not LoadSnapshotChunk 正式三事（499 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 ≠ bundled（499）](../../tracks/implementation/worked-example-offersnapusage-notrestored-vs-bundled.md)。

## 三个名字

1. **upon accepting retrieve and apply 不是 Offer 装完：** 看见 Upon accepting, CometBFT will retrieve and apply snapshot chunks via `ApplySnapshotChunk`，不是已经 Offer 收下就已经装完 interchangeable，不是 321 offerrestored interchangeable / 323 transition interchangeable，也不是 499 offersnapusage bundled interchangeable / 648 offersnapusage-notrestored interchangeable。
2. **upon accepting retrieve and apply 不是 Offer 收下之后 bundled：** 看见 upon accepting retrieve and apply，不是已经 Offer 收下之后 bundled interchangeable，不是 401 offerafter interchangeable / 397 chunk 栏 interchangeable / 398 Result 枚举 interchangeable。
3. **upon accepting retrieve and apply 不是 LoadSnapshotChunk 已经齐：** 看见 upon accepting retrieve snapshot chunks，不是已经 LoadSnapshotChunk 已经齐 interchangeable，不是 375 loadsnap interchangeable / 501 loadsnapusage-retrieve interchangeable / 378 applysnap interchangeable。

## 为什么要分开叫

官方把 OfferSnapshot Usage upon accepting retrieve and apply、Offer 装完 bundled、Offer 收下之后 bundled、LoadSnapshotChunk 拉块 bundled 写成三个名字。把它们叫成一个「看见 Accept 之后 retrieve and apply 就已经 Offer 装完 interchangeable / 就已经 Offer 收下之后 bundled interchangeable / 就已经 LoadSnapshotChunk 齐 interchangeable」，会把 not Offer 装完、not Offer 收下之后 bundled、not LoadSnapshotChunk 已经齐 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 / not Offer 收下之后 bundled / not LoadSnapshotChunk 正式三事（499 余量），先数清问的是 upon accepting retrieve and apply 是不是 Offer 装完 / 321 / 323，是不是 Offer 收下之后 bundled / 401 / 397 / 398，还是 upon accepting retrieve and apply 是不是 LoadSnapshotChunk 已经齐 / 375 / 501 / 378，再决定要不要同一次发布。499 offersnapusage unbundling 在本页 item 2 续。
