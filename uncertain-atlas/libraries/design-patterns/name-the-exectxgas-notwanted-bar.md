# 模式：把 ExecTxResult.gas_wanted not CheckTx GasWanted / not already executing / not already settled 正式三事（393 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.gas_wanted ≠ bundled（393）](../../tracks/implementation/worked-example-exectxgas-notwanted-vs-bundled.md)。

## 三个名字

1. **gas_wanted 不是已经是 CheckTx 的 GasWanted：** 看见填了 gas_wanted，不是已经是 CheckTx GasWanted / 746 exectxgas-notwanted interchangeable。
2. **看见填了 gas_wanted 不是已经在执行：** 看见有要的气，不是已经 315 interchangeable。
3. **看见能填 不是已经交差：** 看见 gas_wanted，不是已经交差 interchangeable。

官方把 ExecTxResult.gas_wanted / gas_used / codespace 三条核心句拆成三个名字。把它们叫成一个「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.gas_wanted 正式三事（393 余量），先数清问的是 gas_wanted 是不是已经是 CheckTx 的 GasWanted、是不是已经在执行 / 315、还是看见能填是不是已经交差，再决定要不要同一次发布。393 exectxgas vs checktx bundled unbundling 在本页 item 1 启动。
