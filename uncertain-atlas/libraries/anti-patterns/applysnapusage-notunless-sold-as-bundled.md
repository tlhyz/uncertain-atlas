# 反模式：把 ApplySnapshotChunk Usage will not do unless instructed not refetch_chunks bundled / not reject_senders bundled / not unable retrieve OfferSnapshot 正式三事（502 余量）说成已经引擎自动 refetch / 已经引擎自动封邻居 / 已经 unable retrieve 换快照

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[ApplySnapshotChunk Usage will not do unless instructed not engine auto refetch ≠ bundled（502）](../../tracks/implementation/worked-example-applysnapusage-notunless-vs-bundled.md)。

## 错在哪里

把 CometBFT will not do this unless instructed by the application 写成已经 refetch_chunks 不论 result 都再拉 interchangeable / 378 applysnap interchangeable / 397 chunk 栏 interchangeable / refetch-sold-as-restored interchangeable / 656 applysnapusage-notchoose interchangeable / 502 applysnapusage refetch/ban interchangeable；把 will not do this unless instructed 写成已经 reject_senders 不论 Result 都拒这些人 interchangeable / 378 applysnap reject_senders interchangeable / 332 snapshotverify interchangeable / 651 offersnaptrust-notverify interchangeable；把 unless instructed by the application 写成已经 unable to retrieve next chunk 引擎 reject via OfferSnapshot interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 655 applysnapusage-notunable interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable，或已经和 502 applysnapusage refetch/ban bundled / 656 applysnapusage-notchoose / 653 applysnapusage-notverify / 654 applysnapusage-notinfo interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage will not do unless instructed not refetch_chunks bundled / not reject_senders bundled / not unable retrieve OfferSnapshot 正式三事（502 余量），必须分开 not refetch_chunks bundled / engine auto refetch、not reject_senders bundled / engine auto ban、not unable retrieve OfferSnapshot 三件事，不要和 502 / 378 / 485 / 655 / 656 / 653 / 654 / 401 / 648 / 499 / 647 糊成一句。

## 和相邻反模式

- [applysnapusage-refetch-sold-as-bundled](applysnapusage-refetch-sold-as-bundled.md) 是 ApplySnapshotChunk Usage refetch/ban 专用 bundled（502），不是本页 502 item 2 单句边界。
- [applysnapusage-notchoose-sold-as-bundled](applysnapusage-notchoose-sold-as-bundled.md) 是 502 item 1 余量 / 656 专用 can choose refetch/ban，不是本页 unless instructed 单句边界。
- [applysnapusage-notunable-sold-as-bundled](applysnapusage-notunable-sold-as-bundled.md) 是 485 item 3 余量 / 655 专用 unable retrieve，不是本页 not unable retrieve OfferSnapshot 单句边界。
- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch 就已经齐，不是本页 will not do unless instructed 单句边界。
