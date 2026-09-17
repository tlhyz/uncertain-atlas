# 模式：把 ApplySnapshotChunk 请求 sender not reject_senders / not already banned / not REJECT_SENDER 正式三事（397 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk。  
**例**：[ApplySnapshotChunk ≠ bundled（397）](../../tracks/implementation/worked-example-applychunk-notsenders-vs-bundled.md)。

## 三个名字

1. **sender 不是已经拒了人：** 看见填了 sender，不是已经 378 interchangeable / 741 applychunk-notsenders interchangeable。
2. **看见填了 sender 不是已经封了：** 看见有人，不是已经 378 interchangeable。
3. **看见能填 不是已经 REJECT_SENDER：** 看见 sender，不是已经 400 / 723 interchangeable。

官方把 ApplySnapshotChunk 请求 chunk / sender / 回包 result 三条核心句拆成三个名字。把它们叫成一个「看见填了 ApplySnapshotChunk 请求就已经在拉块」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk 请求 sender 正式三事（397 余量），先数清问的是 sender 是不是已经拒了人 / 378、是不是已经封了 / 378、还是看见能填是不是已经 REJECT_SENDER / 400 / 723，再决定要不要同一次发布。397 applychunk vs loadchunk bundled unbundling 在本页 item 2 续。
