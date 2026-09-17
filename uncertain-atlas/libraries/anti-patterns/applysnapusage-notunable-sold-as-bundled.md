# 反模式：把 ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事（485 余量）说成已经 refetch 就齐 / 已经 REJECT_SNAPSHOT 回包 / 已经装完又对上 LastBlockAppHash

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders ≠ bundled（485）](../../tracks/implementation/worked-example-applysnapusage-notunable-vs-bundled.md)。

## 错在哪里

把 If CometBFT is unable to retrieve the next chunk after some time … 写成已经 refetch_chunks / reject_senders interchangeable / 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable；把 reject the snapshot and try a different one via `OfferSnapshot` 写成已经 ApplySnapshotChunk Result REJECT_SNAPSHOT interchangeable / 398 applysnap-result interchangeable / 649 offersnapusage-notreject interchangeable / 400 offerabort interchangeable；把 reset and accept it or abort as appropriate 写成已经装完又对上 LastBlockAppHash interchangeable / 332 snapshotverify interchangeable / 654 applysnapusage-notinfo interchangeable / 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable，或已经和 485 applysnapusage bundled / 653 applysnapusage-notverify / 654 applysnapusage-notinfo / 499 offersnapusage bundled interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事（485 余量），必须分开 not refetch/reject_senders、not REJECT_SNAPSHOT bundled、not already matched LastBlockAppHash 三件事，不要和 485 / 378 / 398 / 332 / 653 / 654 / 321 / 401 / 648 / 499 / 647 / 649 糊成一句。

## 和相邻反模式

- [applysnapusage-sold-as-restored](applysnapusage-sold-as-restored.md) 是 ApplySnapshotChunk Usage verify/Info/unable 专用 bundled（485），不是本页 485 item 3 单句边界。
- [applysnapusage-notverify-sold-as-bundled](applysnapusage-notverify-sold-as-bundled.md) 是 485 item 1 余量 / 653 专用，不是本页 unable to retrieve next chunk 单句边界。
- [applysnapusage-notinfo-sold-as-bundled](applysnapusage-notinfo-sold-as-bundled.md) 是 485 item 2 余量 / 654 专用，不是本页 reset and accept or abort 单句边界。
- [applysnapusage-refetch-sold-as-bundled](applysnapusage-refetch-sold-as-bundled.md) 是 ApplySnapshotChunk 再拉 refetch/reject_senders（378）专用，不是本页 not refetch/reject_senders 单句边界。
- [offersnapusage-notreject-sold-as-bundled](offersnapusage-notreject-sold-as-bundled.md) 是 499 item 3 余量 / 649 专用 reject in chunk response，不是本页 not REJECT_SNAPSHOT bundled 单句边界。
