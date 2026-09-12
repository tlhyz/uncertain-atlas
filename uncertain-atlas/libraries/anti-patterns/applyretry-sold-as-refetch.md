# 反模式：看见 ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders 就当成已经再拉 / 看见 ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块就当成已经换一份 / 看见 ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份就当成已经是装这块的结果

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**例**：[ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders ≠ 已经再拉](../../tracks/implementation/worked-example-applyretry-vs-refetch.md)。

## 塌法

1. 看见 ApplySnapshotChunk Result `RETRY` 是再装这块、按需配合 RefetchChunks 和 RejectSenders / 看见回了 RETRY，就当成已经再拉，或当成已经齐。
2. 看见 ApplySnapshotChunk Result `RETRY_SNAPSHOT` 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块 / 看见回了 RETRY_SNAPSHOT，就当成已经换一份，或当成已经装完。
3. 看见 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 是拒掉这份、换一份 / 看见回了 REJECT_SNAPSHOT，就当成已经是装这块的结果，或当成已经拒了人。

## 为什么会出事

官方写：`RETRY` 是再装这块，按需配合 `RefetchChunks` 和 `RejectSenders`。`RETRY_SNAPSHOT` 是从 `OfferSnapshot` 重来这份，除非另有指令否则复用已拉块。`REJECT_SNAPSHOT` 是拒掉这份，换一份。

## 和相邻反模式

- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 refetch_chunks 不论 result 都再拉再装就已经齐，不是本页这种 ApplySnapshotChunk Result RETRY 是再装这块、按需配合 RefetchChunks 和 RejectSenders 不是已经再拉。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是拉失败换一份就已经能接着装，不是本页这种 ApplySnapshotChunk Result RETRY_SNAPSHOT 是从 OfferSnapshot 重来这份、除非另有指令否则复用已拉块不是已经换一份。
- [applychunk-sold-as-loadchunk](applychunk-sold-as-loadchunk.md) 是 ApplySnapshotChunk 回包 result 是装这块的结果就已经是 Offer 的结果，不是本页这种 ApplySnapshotChunk Result REJECT_SNAPSHOT 是拒掉这份、换一份不是已经是装这块的结果。
