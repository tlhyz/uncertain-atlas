# 模式：把 Offer 收下之后才去拉块并装 not already restored / not already complete / not already settled 正式三事（401 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**例**：[Offer ≠ bundled（401）](../../tracks/implementation/worked-example-offerafter-notrestored-vs-bundled.md)。

## 三个名字

1. **收下之后才去拉装 不是已经装完：** 看见收下了，不是已经 321 interchangeable / 728 offerafter-notrestored interchangeable。
2. **看见收下了 不是已经齐：** 看见在拉，不是已经 321 interchangeable。
3. **看见在拉 不是已经交差：** 看见收下之后才去拉装，不是已经交差 / 499 / 648 interchangeable。

官方把 Offer 收下之后才去拉块并装 / 回包拒还要再收 Offer / Apply ACCEPT 这块收下了三条核心句拆成三个名字。把它们叫成一个「看见收下了就已经装完」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下之后才去拉块并装 正式三事（401 余量），先数清问的是收下之后才去拉装是不是已经装完 / 321、是不是已经齐 / 321、还是看见在拉是不是已经交差 / 499 / 648，再决定要不要同一次发布。401 offeraccept vs restored bundled unbundling 在本页 item 1 启动。
