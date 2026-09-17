# 模式：把 ProcessProposal candidate state not already committed 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[ProcessProposal candidate state not already committed ≠ bundled](../../tracks/implementation/worked-example-proccand-candidate-notcommitted-vs-bundled.md)。

## 三个名字

1. **candidate state not already committed 不是 ProcessProposal 候选执行 bundled：** 看见 must be kept as candidate state 不是已经改了已提交状态，不是 452 bundled interchangeable / 349 mutate committed interchangeable / 545 already committed interchangeable。
2. **ready to discard not Finalize apply candidate 不是 no re-execute：** 看见另一块决定时要能丢掉不是已经不用再在 Finalize 执行，不是 452 bundled interchangeable / 460 apply candidate interchangeable / 451 REJECT discard interchangeable。
3. **candidate not ACCEPT switched working state 不是 Process resp ACCEPT settled：** 看见留着 candidate 不是已经 Process 回了 Accept 就换工作状态，不是 452 bundled interchangeable / 430 ACCEPT settled interchangeable / 545 ACCEPT already final interchangeable。

## 为什么要分开叫

官方把 ProcessProposal candidate state not already committed 写成三个名字。把它们叫成一个「看见 Process 留着 candidate 就已经改了已提交状态 interchangeable」，会把 mutate committed state、Finalize apply candidate、Response ACCEPT 后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal candidate state not already committed 正式三事，先数清问的是 candidate state 是不是 already changed committed state、ready to discard 是不是 Finalize apply candidate interchangeable、candidate must be kept 是不是 Process ACCEPT switched working state，再决定要不要同一次发布。
