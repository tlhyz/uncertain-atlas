# 模式：把 ProcessProposal REJECT consensus assume not can't execute candidate 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[ProcessProposal REJECT not can't execute candidate ≠ bundled](../../tracks/implementation/worked-example-procreject-assume-notexecute-vs-bundled.md)。

## 三个名字

1. **REJECT not can't execute candidate 不是 Process REJECT consensus assume bundled：** 看见 REJECT 不是已经不能 MAY 整块执行，不是 533 bundled interchangeable / 452 already committed interchangeable / 533 can't execute interchangeable。
2. **candidate state not already committed 不是 ExecuteTxState：** 看见 candidate state 不是已经改了已提交状态，不是 533 bundled interchangeable / 452 MAY execute interchangeable / 311 candidate interchangeable。
3. **REJECT assume not already settled 不是 Finalize + Commit：** 看见 assumes not valid 不是已经 Process 跑过就意味着已经交差，不是 533 bundled interchangeable / 452 committed interchangeable / 430 ACCEPT settled interchangeable。

## 为什么要分开叫

官方把 ProcessProposal REJECT consensus assume not can't execute candidate 写成三个名字。把它们叫成一个「看见 Process 回了 REJECT 就已经不能整块执行候选 interchangeable」，会把 MAY execute、candidate state、Finalize + Commit 交差三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT consensus assume not can't execute candidate 正式三事，先数清问的是 REJECT not can't execute candidate 是不是 already can't execute / 452 committed interchangeable、candidate state 是不是 already committed interchangeable、REJECT assume 是不是 Finalize + Commit already settled interchangeable，再决定要不要同一次发布。
