# 模式：把 OfferSnapshot Usage reject in chunk response not ABORT / not REJECT_SNAPSHOT / not Offer 收下之后 bundled 正式三事（499 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[OfferSnapshot Usage reject in chunk response not ABORT ≠ bundled（499）](../../tracks/implementation/worked-example-offersnapusage-notreject-vs-bundled.md)。

## 三个名字

1. **reject in chunk response 不是 ABORT：** 看见 reject a snapshot in the chunk response / prepared to accept further OfferSnapshot calls，不是已经 OfferSnapshot Result ABORT interchangeable，不是 400 offerabort interchangeable / 376 offerfmt interchangeable，也不是 499 offersnapusage bundled interchangeable / 649 offersnapusage-notreject interchangeable。
2. **reject in chunk response 不是 REJECT_SNAPSHOT：** 看见 reject in chunk response，不是已经 ApplySnapshotChunk Result REJECT_SNAPSHOT interchangeable，不是 398 applysnap-result interchangeable / 397 chunk 栏 interchangeable / 378 applysnap interchangeable。
3. **reject in chunk response 不是 Offer 收下之后 bundled：** 看见 reject in chunk response / further Offer，不是已经 Offer 收下之后 bundled interchangeable，不是 401 offerafter interchangeable / 321 offerrestored interchangeable / 648 offersnapusage-notrestored interchangeable。

## 为什么要分开叫

官方把 OfferSnapshot Usage reject in chunk response / prepared for further Offer、OfferSnapshot Result ABORT、ApplySnapshotChunk Result REJECT_SNAPSHOT、Offer 收下之后 bundled 写成三个名字。把它们叫成一个「看见 reject in chunk response 就已经 ABORT interchangeable / 就已经 REJECT_SNAPSHOT interchangeable / 就已经 Offer 收下之后 bundled interchangeable」，会把 not ABORT、not REJECT_SNAPSHOT、not Offer 收下之后 bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage reject in chunk response not ABORT / not REJECT_SNAPSHOT / not Offer 收下之后 bundled 正式三事（499 余量），先数清问的是 reject in chunk response 是不是 ABORT / 400 / 376，是不是 REJECT_SNAPSHOT / 398 / 397 / 378，还是 reject in chunk response 是不是 Offer 收下之后 bundled / 401 / 321 / 648，再决定要不要同一次发布。499 offersnapusage unbundling 在本页 item 3 完成。
