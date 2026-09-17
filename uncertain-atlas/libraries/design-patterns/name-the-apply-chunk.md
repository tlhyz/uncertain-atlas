# 模式：把 ApplySnapshotChunk 请求三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**例**：[ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 ≠ 已经在拉块](../../tracks/implementation/worked-example-applychunk-vs-loadchunk.md)。

## 三个名字

1. **ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容不是已经在拉块：** 看见填了 chunk 不是已经齐。
2. **ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID 不是已经拒了人：** 看见填了 sender 不是已经封了。
3. **ApplySnapshotChunk 回包 result 是装这块的结果不是已经是 Offer 的结果：** 看见回了 result 不是已经装完。

## 为什么要分开叫

官方把 ApplySnapshotChunk 请求 `chunk` 是 LoadSnapshotChunk 回的那块二进制内容、请求 `sender` 是送来这块的节点 P2P ID、回包 `result` 是装这块的结果写成三件事。把它们叫成一个「看见填了 ApplySnapshotChunk 请求就已经在拉块」，会把拉块、拒这些人以及这次 Offer 的结果一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ApplySnapshotChunk 请求就已经在拉块」，先数清问的是 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容不是已经在拉块、ApplySnapshotChunk 请求 sender 是送来这块的节点 P2P ID 不是已经拒了人，还是 ApplySnapshotChunk 回包 result 是装这块的结果不是已经是 Offer 的结果，再决定要不要同一次发布。
