# 反模式：把 ApplySnapshotChunk Usage can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事（502 余量）说成已经 refetch/ban bundled / 已经 RETRY / 已经封邻居就交差

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[ApplySnapshotChunk Usage can choose refetch/ban not refetch/ban bundled ≠ bundled（502）](../../tracks/implementation/worked-example-applysnapusage-notchoose-vs-bundled.md)。

## 错在哪里

把 The application can choose to refetch chunks and/or ban P2P peers as appropriate 写成已经 refetch_chunks 不论 result 都再拉 interchangeable / 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 655 applysnapusage-notunable interchangeable / 502 applysnapusage refetch/ban interchangeable；把 ban P2P peers as appropriate 写成已经 reject_senders 不论 Result 都拒这些人 interchangeable / 332 snapshotverify interchangeable / 651 offersnaptrust-notverify interchangeable；把 can choose refetch/ban 写成已经 ApplySnapshotChunk Result RETRY interchangeable / 398 applysnap-result interchangeable / 401 offerafter interchangeable / applyretry-sold-as-refetch interchangeable，或已经和 502 applysnapusage refetch/ban bundled / 657 applysnapusage-notunless / 485 applysnapusage verify/Info/unable interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事（502 余量），必须分开 not refetch_chunks bundled、not reject_senders bundled、not RETRY bundled 三件事，不要和 502 / 378 / 398 / 332 / 485 / 655 / 653 / 654 / 401 / 648 / 499 / 647 糊成一句。

## 和相邻反模式

- [applysnapusage-refetch-sold-as-bundled](applysnapusage-refetch-sold-as-bundled.md) 是 ApplySnapshotChunk Usage refetch/ban 专用 bundled（502），不是本页 502 item 1 单句边界。
- [applysnapusage-notunable-sold-as-bundled](applysnapusage-notunable-sold-as-bundled.md) 是 485 item 3 余量 / 655 专用 unable retrieve，不是本页 can choose refetch/ban 单句边界。
- [applyretry-sold-as-refetch](applyretry-sold-as-refetch.md) 是 ApplySnapshotChunk Result RETRY bundled（398）专用，不是本页 not RETRY bundled 单句边界。
- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch 就已经齐，不是本页 can choose refetch/ban 单句边界。
