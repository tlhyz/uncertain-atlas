# 模式：把 ApplySnapshotChunk Usage can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事（502 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[ApplySnapshotChunk Usage can choose refetch/ban not refetch/ban bundled ≠ bundled（502）](../../tracks/implementation/worked-example-applysnapusage-notchoose-vs-bundled.md)。

## 三个名字

1. **can choose refetch/ban 不是 refetch_chunks bundled：** 看见 The application can choose to refetch chunks and/or ban P2P peers as appropriate，不是已经 refetch_chunks 不论 result 都再拉 interchangeable，不是 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable / 502 applysnapusage refetch/ban interchangeable / 655 applysnapusage-notunable interchangeable。
2. **can choose refetch/ban 不是 reject_senders bundled：** 看见 ban P2P peers as appropriate，不是已经 reject_senders 不论 Result 都拒这些人 interchangeable，不是 378 applysnap reject_senders interchangeable / 332 snapshotverify interchangeable / 651 offersnaptrust-notverify interchangeable / 483 offersnaptrust item 2 avoid DoS interchangeable。
3. **can choose refetch/ban 不是 RETRY bundled：** 看见 can choose refetch chunks and/or ban P2P peers，不是已经 ApplySnapshotChunk Result RETRY interchangeable，不是 398 applysnap-result interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable / applyretry-sold-as-refetch interchangeable。

## 为什么要分开叫

官方把 ApplySnapshotChunk Usage can choose refetch/ban、ApplySnapshotChunk 回包 refetch_chunks / reject_senders bundled、ApplySnapshotChunk Result RETRY 写成三个名字。把它们叫成一个「看见 can choose refetch/ban 就已经 refetch/ban bundled interchangeable / 就已经 RETRY interchangeable / 就已经封邻居就交差 interchangeable」，会把 not refetch_chunks bundled、not reject_senders bundled、not RETRY bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage can choose refetch/ban not refetch_chunks bundled / not reject_senders bundled / not RETRY bundled 正式三事（502 余量），先数清问的是 can choose refetch/ban 是不是 refetch_chunks bundled / 378 / 397 / 375，是不是 reject_senders bundled / 378 / 332 / 651，还是 can choose refetch/ban 是不是 RETRY bundled / 398 / 401 / 648，再决定要不要同一次发布。502 applysnapusage refetch/ban unbundling 在本页 item 1 启动。
