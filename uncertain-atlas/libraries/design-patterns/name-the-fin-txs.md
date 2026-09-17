# 模式：把 Finalize 执行余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**例**：[Finalize 按应用自己的规则确定地执行 txs、再交还控制权 ≠ 已经交差](../../tracks/implementation/worked-example-fintxs-vs-control.md)。

## 三个名字

1. **Finalize 按应用自己的规则确定地执行 txs、再交还控制权不是已经交差：** 看见先跑了不是已经可以像 Prepare 那样。
2. **Process 含提案块上执行所需的全部信息不是已经是刚决定那块的字段：** 看见填了信息不是已经跑过 Process。
3. **Process 可以像在处理 Finalize 那样整块执行不是已经是 ExecuteTxState：** 看见整块跑了不是已经交差。

## 为什么要分开叫

官方把 Finalize 按应用自己的规则确定地执行 txs 再交还控制权、Process 含提案块上执行所需的全部信息、Process 可以像在处理 Finalize 那样整块执行写成三件事。把它们叫成一个「看见填了 Finalize 执行余量就已经交差」，会把交差、刚决定那块的字段和 ExecuteTxState 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 执行余量就已经交差」，先数清问的是 Finalize 按应用自己的规则确定地执行 txs、再交还控制权不是已经交差、Process 含提案块上执行所需的全部信息不是已经是刚决定那块的字段，还是 Process 可以像在处理 Finalize 那样整块执行不是已经是 ExecuteTxState，再决定要不要同一次发布。
