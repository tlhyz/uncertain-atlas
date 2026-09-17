# 模式：把 ExecTxResult.codespace not CheckTx codespace / not already response code / not already settled 正式三事（393 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.codespace ≠ bundled（393）](../../tracks/implementation/worked-example-exectxgas-notcodespace-vs-bundled.md)。

## 三个名字

1. **codespace 不是已经是 CheckTx 码空间：** 看见写了空间，不是已经 381 interchangeable / 748 exectxgas-notcodespace interchangeable。
2. **看见写了空间 不是已经是回包码：** 看见有命名空间，不是已经 381 interchangeable。
3. **看见能回 不是已经交差：** 看见 codespace，不是已经交差 interchangeable。

官方把 ExecTxResult.gas_wanted / gas_used / codespace 三条核心句拆成三个名字。把它们叫成一个「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.codespace 正式三事（393 余量），先数清问的是 codespace 是不是已经是 CheckTx 码空间 / 381、是不是已经是回包码 / 381、还是看见能回是不是已经交差，再决定要不要同一次发布。393 exectxgas vs checktx bundled unbundling 在本页 item 3 完成。
