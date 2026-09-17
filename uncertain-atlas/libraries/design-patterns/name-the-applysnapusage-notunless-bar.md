# 模式：把 ApplySnapshotChunk Usage will not do unless instructed not refetch_chunks bundled / not reject_senders bundled / not unable retrieve OfferSnapshot 正式三事（502 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[ApplySnapshotChunk Usage will not do unless instructed not engine auto refetch ≠ bundled（502）](../../tracks/implementation/worked-example-applysnapusage-notunless-vs-bundled.md)。

## 三个名字

1. **will not do unless instructed 不是 refetch_chunks bundled / engine auto refetch：** 看见 CometBFT will not do this unless instructed by the application，不是已经 refetch_chunks 不论 result 都再拉 interchangeable，不是 378 applysnap interchangeable / 397 chunk 栏 interchangeable / refetch-sold-as-restored interchangeable / 502 applysnapusage refetch/ban interchangeable / 656 applysnapusage-notchoose interchangeable。
2. **will not do unless instructed 不是 reject_senders bundled / engine auto ban：** 看见 will not do this unless instructed，不是已经 reject_senders 不论 Result 都拒这些人 interchangeable，不是 378 applysnap reject_senders interchangeable / 332 snapshotverify interchangeable / 651 offersnaptrust-notverify interchangeable / 483 offersnaptrust item 2 avoid DoS interchangeable。
3. **will not do unless instructed 不是 unable retrieve OfferSnapshot：** 看见 unless instructed by the application，不是已经 unable to retrieve next chunk 引擎 reject via OfferSnapshot interchangeable，不是 485 applysnapusage verify/Info/unable interchangeable / 655 applysnapusage-notunable interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable。

## 为什么要分开叫

官方把 ApplySnapshotChunk Usage unless instructed、ApplySnapshotChunk 回包 refetch_chunks / reject_senders bundled、unable to retrieve next chunk 引擎换快照路径 写成三个名字。把它们叫成一个「看见 will not do unless instructed 就已经引擎自动 refetch interchangeable / 就已经引擎自动封邻居 interchangeable / 就已经 unable retrieve 换快照 interchangeable」，会把 not refetch_chunks bundled、not reject_senders bundled、not unable retrieve OfferSnapshot 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage will not do unless instructed not refetch_chunks bundled / not reject_senders bundled / not unable retrieve OfferSnapshot 正式三事（502 余量），先数清问的是 will not do unless instructed 是不是 refetch_chunks bundled / engine auto refetch / 378 / 397，是不是 reject_senders bundled / engine auto ban / 378 / 332 / 651，还是 unless instructed 是不是 unable retrieve OfferSnapshot / 485 / 655 / 401 / 648，再决定要不要同一次发布。502 applysnapusage refetch/ban unbundling 在本页 item 2 完成。
