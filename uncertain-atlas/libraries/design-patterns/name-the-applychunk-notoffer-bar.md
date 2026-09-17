# 模式：把 ApplySnapshotChunk 回包 result not Offer result / not already restored / not Apply Result enum 正式三事（397 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**例**：[ApplySnapshotChunk ≠ bundled（397）](../../tracks/implementation/worked-example-applychunk-notoffer-vs-bundled.md)。

## 三个名字

1. **result 不是已经是 Offer 的结果：** 看见回了 result，不是已经 396 / 738 interchangeable / 742 applychunk-notoffer interchangeable。
2. **看见回了 result 不是已经装完：** 看见有结果，不是已经 321 interchangeable。
3. **看见能回 不是已经 Apply Result 枚举：** 看见 result，不是已经 398 / 719–721 interchangeable。

官方把 ApplySnapshotChunk 请求 chunk / sender / 回包 result 三条核心句拆成三个名字。把它们叫成一个「看见填了 ApplySnapshotChunk 请求就已经在拉块」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 回包 result 正式三事（397 余量），先数清问的是 result 是不是已经是 Offer 的结果 / 396 / 738、是不是已经装完 / 321、还是看见能回是不是已经 Apply Result 枚举 / 398，再决定要不要同一次发布。397 applychunk vs loadchunk bundled unbundling 在本页 item 3 完成。
