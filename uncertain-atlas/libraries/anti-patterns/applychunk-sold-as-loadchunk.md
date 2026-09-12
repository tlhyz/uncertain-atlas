# 反模式：看见 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容就当成已经在拉块 / 看见 ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID 就当成已经拒了人 / 看见 ApplySnapshotChunk 回包 result 是装这块的结果就当成已经是 Offer 的结果

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**例**：[ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 ≠ 已经在拉块](../../tracks/implementation/worked-example-applychunk-vs-loadchunk.md)。

## 塌法

1. 看见 ApplySnapshotChunk 请求 `chunk` 是 LoadSnapshotChunk 回的那块二进制内容 / 看见填了 chunk，就当成已经在拉块，或当成已经齐。
2. 看见 ApplySnapshotChunk 请求 `sender` 是送来这块的节点 P2P ID / 看见填了 sender，就当成已经拒了人，或当成已经封了。
3. 看见 ApplySnapshotChunk 回包 `result` 是装这块的结果 / 看见回了 result，就当成已经是 Offer 的结果，或当成已经装完。

## 为什么会出事

官方写：`chunk` 是 `LoadSnapshotChunk` 回的那块二进制内容。`sender` 是送来这块的节点 P2P ID。`result` 是装这块的结果。

## 和相邻反模式

- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐，不是本页这种 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容不是已经在拉块。
- [refetch-sold-as-restored](refetch-sold-as-restored.md) 是 reject_senders 不论 Result 都拒这些人就已经能接着装，不是本页这种 ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID 不是已经拒了人。
- [offersnap-sold-as-listed](offersnap-sold-as-listed.md) 是 OfferSnapshot 回包 result 是这次 Offer 的结果就已经装完，不是本页这种 ApplySnapshotChunk 回包 result 是装这块的结果不是已经是 Offer 的结果。
