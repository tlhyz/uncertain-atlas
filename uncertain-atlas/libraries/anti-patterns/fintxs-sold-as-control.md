# 反模式：看见 Finalize 按应用自己的规则确定地执行 txs、再交还控制权就当成已经交差 / 看见 Process 含提案块上执行所需的全部信息就当成已经是刚决定那块的字段 / 看见 Process 可以像在处理 Finalize 那样整块执行就当成已经是 ExecuteTxState

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**例**：[Finalize 按应用自己的规则确定地执行 txs、再交还控制权 ≠ 已经交差](../../tracks/implementation/worked-example-fintxs-vs-control.md)。

## 塌法

1. 看见 Finalize 按应用自己的规则确定地执行 `txs`、再交还控制权 / 看见先跑了，就当成已经交差，或当成已经可以像 Prepare 那样。
2. 看见 Process 含提案块上执行所需的全部信息 / 看见填了信息，就当成已经是刚决定那块的字段，或当成已经跑过 Process。
3. 看见 Process 可以像在处理 Finalize 那样整块执行 / 看见整块跑了，就当成已经是 ExecuteTxState，或当成已经交差。

## 为什么会出事

官方写：应用按自己定的规则，确定地执行 `FinalizeBlockRequest.txs` 里的交易，再把控制权交还给 CometBFT。`ProcessProposal` 含提案块上执行所需的全部信息。应用可以像在处理 `FinalizeBlock` 那样整块执行。

## 和相邻反模式

- [finfields-sold-as-equiv](finfields-sold-as-equiv.md) 是 Finalize 实现必须确定、因为它在状态机复制里推进应用状态就已经可以像 Prepare 那样，不是本页这种 Finalize 按应用自己的规则确定地执行 txs、再交还控制权不是已经交差。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process，不是本页这种 Process 含提案块上执行所需的全部信息不是已经是刚决定那块的字段。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选已经是 ExecuteTxState，不是本页这种 Process 可以像在处理 Finalize 那样整块执行不是已经是 ExecuteTxState。
