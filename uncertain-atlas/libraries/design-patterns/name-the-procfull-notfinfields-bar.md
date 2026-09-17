# 模式：把 ProcessProposal Contains all information not Finalize newly decided fields 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**例**：[ProcessProposal Contains all information not Finalize newly decided fields ≠ bundled](../../tracks/implementation/worked-example-procfull-notfinfields-vs-bundled.md)。

## 三个名字

1. **Contains all information not Finalize newly decided fields 不是 ProcessProposal 含执行所需全部信息 bundled：** 看见拟议块上执行所需不是已经是 FinalizeBlockRequest 刚决定那块的字段，不是 453 bundled interchangeable / 461 newly decided interchangeable / 363 fill all fields interchangeable。
2. **Contains all information not proposed/decided interchangeable 不是 hash/decided_last_commit 混用：** 看见拟议块执行所需不是已经 FinalizeBlockRequest.hash 是已决块的哈希，不是 453 bundled interchangeable / 420 proposed_last_commit interchangeable / 428 Finalize hash interchangeable。
3. **Contains all information not only txs enough 不是 Request 八栏齐 only txs：** 看见含执行所需全部信息不是已经只有 txs 字段就够 fully execute，不是 453 bundled interchangeable / 548 only txs enough interchangeable / 419 Process req txs interchangeable。

## 为什么要分开叫

官方把 ProcessProposal Contains all information not Finalize newly decided fields 写成三个名字。把它们叫成一个「看见 Process 含全部信息就已经是 Finalize 字段」，会把 newly decided fields、proposed/decided 混用、only txs enough 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Contains all information not Finalize newly decided fields 正式三事，先数清问的是 Contains all information 是不是 Finalize newly decided fields、Contains all information 是不是 proposed/decided interchangeable、Contains all information 是不是 only txs enough，再决定要不要同一次发布。
