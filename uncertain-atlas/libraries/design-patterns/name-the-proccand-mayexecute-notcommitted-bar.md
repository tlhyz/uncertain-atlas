# 模式：把 ProcessProposal MAY fully execute not already committed 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[ProcessProposal MAY fully execute not already committed ≠ bundled](../../tracks/implementation/worked-example-proccand-mayexecute-notcommitted-vs-bundled.md)。

## 三个名字

1. **MAY fully execute not already committed 不是 ProcessProposal 候选执行 bundled：** 看见 immediate execution 不是已经交差，不是 452 bundled interchangeable / 460 Finalize apply candidate interchangeable / 147 AppHash interchangeable。
2. **MAY execute not ExecuteTxState 不是 candidate is ExecuteTxState：** 看见像 Finalize 那样跑不是已经 ExecuteTxState，不是 452 bundled interchangeable / 311 candidate interchangeable / 312 CheckTxState interchangeable。
3. **MAY execute not ACCEPT already final 不是 Process resp ACCEPT settled：** 看见 Process 回了 ACCEPT 不是已经能点名本高度最终，不是 452 bundled interchangeable / 430 ACCEPT settled interchangeable / 533 status ACCEPT interchangeable。

## 为什么要分开叫

官方把 ProcessProposal MAY fully execute not already committed 写成三个名字。把它们叫成一个「看见 Process 跑过就已经交差 interchangeable」，会把 Finalize + Commit 交差、ExecuteTxState、Response ACCEPT 后效三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal MAY fully execute not already committed 正式三事，先数清问的是 MAY fully execute 是不是 already committed、MAY execute 是不是 ExecuteTxState、Process MAY execute 是不是 ACCEPT already final，再决定要不要同一次发布。
