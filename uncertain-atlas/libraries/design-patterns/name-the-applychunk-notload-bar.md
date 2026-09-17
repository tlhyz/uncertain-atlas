# 模式：把 ApplySnapshotChunk 请求 chunk not already loading / not already complete / not Usage retrieve 正式三事（397 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**例**：[ApplySnapshotChunk ≠ bundled（397）](../../tracks/implementation/worked-example-applychunk-notload-vs-bundled.md)。

## 三个名字

1. **chunk 不是已经在拉块：** 看见填了 chunk，不是已经 375 interchangeable / 740 applychunk-notload interchangeable。
2. **看见填了 chunk 不是已经齐：** 看见有这块，不是已经 375 interchangeable。
3. **看见能填 不是已经 Usage retrieve：** 看见 chunk，不是已经 501 / 660 interchangeable。

官方把 ApplySnapshotChunk 请求 chunk / sender / 回包 result 三条核心句拆成三个名字。把它们叫成一个「看见填了 ApplySnapshotChunk 请求就已经在拉块」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 请求 chunk 正式三事（397 余量），先数清问的是 chunk 是不是已经在拉块 / 375、是不是已经齐 / 375、还是看见能填是不是已经 Usage retrieve / 501 / 660，再决定要不要同一次发布。397 applychunk vs loadchunk bundled unbundling 在本页 item 1 启动。
