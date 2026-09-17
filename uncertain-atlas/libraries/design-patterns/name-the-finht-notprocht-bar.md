# 模式：把 FinalizeBlock Finalize match header not ProcessProposal match 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock Finalize match header not ProcessProposal match ≠ bundled](../../tracks/implementation/worked-example-finht-notprocht-vs-bundled.md)。

## 三个名字

1. **Finalize match header not ProcessProposal match 不是 FinalizeBlock height/time 对上拟议块头 bundled：** 看见 Finalize 这边 match 不是已经 ProcessProposal height/time match interchangeable，不是 462 bundled interchangeable / 454 Process match interchangeable / 551 Process not Finalize fields interchangeable。
2. **Finalize match header not know hash 不是 428 Finalize hash：** 看见 match header 不是已经知道本头哈希，不是 462 bundled interchangeable / 428 Finalize hash interchangeable / 417 header fields bundled interchangeable。
3. **Finalize match header not newly decided block fields 不是 461 newly decided：** 看见 Finalize match 不是已经 newly decided block 字段 interchangeable，不是 462 bundled interchangeable / 461 newly decided interchangeable / 363 fill all fields interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock Finalize match header not ProcessProposal match 写成三个名字。把它们叫成一个「看见 Finalize match header 就已经是 ProcessProposal match interchangeable」，会把 Finalize vs Process match、Finalize match vs know hash、Finalize match vs newly decided block fields 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Finalize match header not ProcessProposal match 正式三事，先数清问的是 Finalize match header 是不是 ProcessProposal height/time match interchangeable、Finalize match header 是不是 know hash interchangeable、Finalize match header 是不是 newly decided block fields interchangeable，再决定要不要同一次发布。
