# 模式：把 在装这块的回包里拒掉这份、还要再收 Offer not ABORT / not REJECT_SNAPSHOT / not Usage reject 正式三事（401 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**例**：[在装这块的回包里拒掉这份、还要再收 ≠ bundled（401）](../../tracks/implementation/worked-example-offerafter-notabort-vs-bundled.md)。

## 三个名字

1. **回包拒还要再收 Offer 不是已经 ABORT：** 看见在装这块时拒了，不是已经 400 / 724 interchangeable / 729 offerafter-notabort interchangeable。
2. **看见在装这块时拒了 不是已经 REJECT_SNAPSHOT：** 看见还能再收 Offer，不是已经 398 / 721 interchangeable。
3. **看见还能再收 Offer 不是已经 Usage reject：** 看见回包拒，不是已经 499 / 649 interchangeable。

官方把 Offer 收下之后才去拉块并装 / 回包拒还要再收 Offer / Apply ACCEPT 这块收下了三条核心句拆成三个名字。把它们叫成一个「看见收下了就已经装完」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包拒还要再收 Offer 正式三事（401 余量），先数清问的是回包拒是不是已经 ABORT / 400 / 724、是不是已经 REJECT_SNAPSHOT / 398 / 721、还是看见还能再收是不是已经 Usage reject / 499 / 649，再决定要不要同一次发布。401 offeraccept vs restored bundled unbundling 在本页 item 2 续。
