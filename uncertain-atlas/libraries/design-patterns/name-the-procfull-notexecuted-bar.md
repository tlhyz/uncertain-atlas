# 模式：把 ProcessProposal Contains all information not already executed 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[ProcessProposal Contains all information not already executed ≠ bundled](../../tracks/implementation/worked-example-procfull-notexecuted-vs-bundled.md)。

## 三个名字

1. **Contains all information not already executed 不是 ProcessProposal 含执行所需全部信息 bundled：** 看见含执行所需全部信息不是已经执行那些交易 / Finalize 跑过，不是 453 bundled interchangeable / 452 immediate execution interchangeable / 460 Finalize apply interchangeable。
2. **Contains all information not MAY execute committed 不是 Process MAY execute committed：** 看见含执行所需全部信息不是已经 Process MAY 整块执行交差，不是 453 bundled interchangeable / 543 MAY execute interchangeable / 544 candidate not committed interchangeable。
3. **Contains all information not read-only settled 不是 read-only checks/processes committed：** 看见含执行所需全部信息不是已经 read-only 处理交差，不是 453 bundled interchangeable / 545 read-only interchangeable / 430 ACCEPT settled interchangeable。

## 为什么要分开叫

官方把 ProcessProposal Contains all information not already executed 写成三个名字。把它们叫成一个「看见 Process 含全部信息就已经执行那些交易」，会把 already executed / MAY execute committed、read-only settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Contains all information not already executed 正式三事，先数清问的是 Contains all information 是不是 already executed those txs / Finalize already ran、Contains all information 是不是 MAY execute already committed、Contains all information 是不是 read-only already settled，再决定要不要同一次发布。
