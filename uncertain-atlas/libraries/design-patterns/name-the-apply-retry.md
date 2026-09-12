# 模式：把 ApplySnapshotChunk 结果枚举三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**例**：[ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders ≠ 已经再拉](../../tracks/implementation/worked-example-applyretry-vs-refetch.md)。

## 三个名字

1. **ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders 不是已经再拉：** 看见回了 RETRY 不是已经齐。
2. **ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块不是已经换一份：** 看见回了 RETRY_SNAPSHOT 不是已经装完。
3. **ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份不是已经是装这块的结果：** 看见回了 REJECT_SNAPSHOT 不是已经拒了人。

## 为什么要分开叫

官方把 ApplySnapshotChunk Result `RETRY` 是再装这块、按需配合 RefetchChunks 和 RejectSenders、`RETRY_SNAPSHOT` 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块、`REJECT_SNAPSHOT` 是拒掉这份、换一份写成三件事。把它们叫成一个「看见回了 ApplySnapshotChunk 结果枚举就已经再拉」，会把不论 result 都再拉、拉失败换一份和装这块的结果字段一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 ApplySnapshotChunk 结果枚举就已经再拉」，先数清问的是 ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders 不是已经再拉、ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块不是已经换一份，还是 ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份不是已经是装这块的结果，再决定要不要同一次发布。
