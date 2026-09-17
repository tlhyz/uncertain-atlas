# 模式：把 ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事（485 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders ≠ bundled（485）](../../tracks/implementation/worked-example-applysnapusage-notunable-vs-bundled.md)。

## 三个名字

1. **unable to retrieve next chunk 不是 refetch/reject_senders：** 看见 If CometBFT is unable to retrieve the next chunk after some time …，不是已经 refetch_chunks / reject_senders interchangeable，不是 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable。
2. **unable to retrieve next chunk 不是 REJECT_SNAPSHOT bundled：** 看见 reject the snapshot and try a different one via `OfferSnapshot`，不是已经 ApplySnapshotChunk Result REJECT_SNAPSHOT interchangeable，不是 398 applysnap-result interchangeable / 649 offersnapusage-notreject interchangeable / 400 offerabort interchangeable / 401 offerafter interchangeable。
3. **unable to retrieve next chunk 不是 already matched LastBlockAppHash：** 看见 reset and accept it or abort as appropriate，不是已经装完又对上 LastBlockAppHash interchangeable，不是 332 snapshotverify interchangeable / 654 applysnapusage-notinfo interchangeable / 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable。

## 为什么要分开叫

官方把 ApplySnapshotChunk Usage unable to retrieve next chunk、ApplySnapshotChunk 再拉 refetch/reject_senders、ApplySnapshotChunk Result REJECT_SNAPSHOT、Snapshot Verification 装完又对上 LastBlockAppHash 写成三个名字。把它们叫成一个「看见 unable to retrieve next chunk 就已经 refetch 就齐 interchangeable / 就已经 REJECT_SNAPSHOT 回包 interchangeable / 就已经 reset 就代表装完 interchangeable」，会把 not refetch/reject_senders、not REJECT_SNAPSHOT bundled、not already matched LastBlockAppHash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事（485 余量），先数清问的是 unable to retrieve next chunk 是不是 refetch/reject_senders / 378 / 397 / 375，是不是 reject via OfferSnapshot 是不是 REJECT_SNAPSHOT bundled / 398 / 649 / 400，还是 reset and accept or abort 是不是 already matched LastBlockAppHash / 332 / 654 / 321 / 401 / 648，再决定要不要同一次发布。485 applysnapusage unbundling 在本页 item 3 完成。
