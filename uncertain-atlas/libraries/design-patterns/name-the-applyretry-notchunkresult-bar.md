# 模式：把 ApplySnapshotChunk Result REJECT_SNAPSHOT not this-chunk result / not rejected senders / not Offer REJECT_FORMAT 正式三事（398 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**例**：[REJECT_SNAPSHOT ≠ bundled（398）](../../tracks/implementation/worked-example-applyretry-notchunkresult-vs-bundled.md)。

## 三个名字

1. **REJECT_SNAPSHOT 不是已经是装这块的结果：** 看见回了 REJECT_SNAPSHOT，不是已经 397 interchangeable / 721 applyretry-notchunkresult interchangeable。
2. **看见回了 REJECT_SNAPSHOT 不是已经拒了人：** 看见能换一份，不是已经 378 interchangeable。
3. **看见能换一份 不是 Offer REJECT_FORMAT：** 看见 REJECT_SNAPSHOT，不是已经 400 interchangeable。

官方把 ApplySnapshotChunk Result 三条核心句拆成三个名字。把它们叫成一个「看见回了 ApplySnapshotChunk 结果枚举就已经再拉」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result REJECT_SNAPSHOT 正式三事（398 余量），先数清问的是 REJECT_SNAPSHOT 是不是已经是装这块的结果 / 397、是不是已经拒了人 / 378、还是看见能换一份是不是 400，再决定要不要同一次发布。398 applyretry vs refetch bundled unbundling 在本页 item 3 完成。
