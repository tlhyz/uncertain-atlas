# 模式：把 ExecTxResult.gas_used not already counted into consensus / not already printed in header / not already settled 正式三事（393 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.gas_used ≠ bundled（393）](../../tracks/implementation/worked-example-exectxgas-notused-vs-bundled.md)。

## 三个名字

1. **gas_used 不是已经算进共识：** 看见填了 gas_used，不是已经算进共识 / 747 exectxgas-notused interchangeable。
2. **看见填了 gas_used 不是已经印进本头：** 看见有用掉的气，不是已经 316 interchangeable。
3. **看见能回 不是已经交差：** 看见 gas_used，不是已经交差 interchangeable。

官方把 ExecTxResult.gas_wanted / gas_used / codespace 三条核心句拆成三个名字。把它们叫成一个「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.gas_used 正式三事（393 余量），先数清问的是 gas_used 是不是已经算进共识、是不是已经印进本头 / 316、还是看见能回是不是已经交差，再决定要不要同一次发布。393 exectxgas vs checktx bundled unbundling 在本页 item 2 续。
