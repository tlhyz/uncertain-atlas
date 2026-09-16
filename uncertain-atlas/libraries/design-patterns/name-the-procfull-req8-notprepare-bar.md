# 模式：把 ProcessProposal Request 八栏齐 not only Prepare txs 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**例**：[ProcessProposal Request 八栏齐 not only Prepare txs ≠ bundled](../../tracks/implementation/worked-example-procfull-req8-notprepare-vs-bundled.md)。

## 三个名字

1. **Request 八栏齐 not only Prepare txs 不是 ProcessProposal 含执行所需全部信息 bundled：** 看见八栏齐不是已经只有 PrepareProposalResponse.txs，不是 453 bundled interchangeable / 506 Prepare return interchangeable / 351 Process follows Prepare interchangeable。
2. **Request 八栏齐 not only raw proposal 不是 Prepare raw proposal：** 看见八栏齐不是已经只有 raw proposal，不是 453 bundled interchangeable / 503 raw proposal interchangeable / 423 PrepareRequest.txs interchangeable。
3. **Request 八栏齐 not only txs enough 不是 Process req txs column：** 看见八栏齐不是已经只有 txs 就够 fully execute，不是 453 bundled interchangeable / 419 Process req txs interchangeable / 420 / 427 req rest/end interchangeable。

## 为什么要分开叫

官方把 ProcessProposal Request 八栏齐 not only Prepare txs 写成三个名字。把它们叫成一个「看见 Process 八栏齐就已经只有 Prepare 回包」，会把 Prepare resp only txs、raw proposal only、txs column enough 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Request 八栏齐 not only Prepare txs 正式三事，先数清问的是 Request 八栏齐 是不是 only PrepareProposalResponse.txs、Request 八栏齐 是不是 only raw proposal、Request 八栏齐 是不是 only txs enough，再决定要不要同一次发布。
