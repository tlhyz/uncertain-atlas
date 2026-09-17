# 模式：把 ApplySnapshotChunk Result ACCEPT not already complete / not this-chunk result / not Offer ACCEPT 正式三事（401 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**例**：[ApplySnapshotChunk ≠ bundled（401）](../../tracks/implementation/worked-example-offerafter-notcomplete-vs-bundled.md)。

## 三个名字

1. **Apply ACCEPT 不是已经齐：** 看见回了 ACCEPT，不是已经 321 interchangeable / 730 offerafter-notcomplete interchangeable。
2. **看见回了 ACCEPT 不是已经是装这块的结果：** 看见能收这块，不是已经 397 interchangeable。
3. **看见能收这块 不是已经 Offer ACCEPT：** 看见 Apply ACCEPT，不是已经 402 / 726 interchangeable。

官方把 Offer 收下之后才去拉块并装 / 回包拒还要再收 Offer / Apply ACCEPT 这块收下了三条核心句拆成三个名字。把它们叫成一个「看见收下了就已经装完」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result ACCEPT 正式三事（401 余量），先数清问的是 Apply ACCEPT 是不是已经齐 / 321、是不是已经是装这块的结果 / 397、还是看见能收这块是不是已经 Offer ACCEPT / 402 / 726，再决定要不要同一次发布。401 offeraccept vs restored bundled unbundling 在本页 item 3 完成。
