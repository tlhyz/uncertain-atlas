# 模式：把 ExecTxResult 气三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.gas_wanted 是这笔要的气 ≠ 已经是 CheckTx 的 GasWanted](../../tracks/implementation/worked-example-exectxgas-vs-checktx.md)。

## 三个名字

1. **ExecTxResult.gas_wanted 是这笔要的气不是已经是 CheckTx 的 GasWanted：** 看见填了 gas_wanted 不是已经在执行。
2. **ExecTxResult.gas_used 是这笔用掉的气不是已经算进共识：** 看见填了 gas_used 不是已经印进本头。
3. **ExecTxResult.codespace 是码的命名空间不是已经是 CheckTx 码空间：** 看见写了空间不是已经是回包码。

## 为什么要分开叫

官方把 ExecTxResult `gas_wanted` 是这笔要的气、`gas_used` 是这笔用掉的气、`codespace` 是码的命名空间写成三件事。把它们叫成一个「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted」，会把 CheckTx 的 GasWanted、已经算进共识和 CheckTx 码空间一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExecTxResult 气就已经是 CheckTx 的 GasWanted」，先数清问的是 ExecTxResult.gas_wanted 是这笔要的气不是已经是 CheckTx 的 GasWanted、ExecTxResult.gas_used 是这笔用掉的气不是已经算进共识，还是 ExecTxResult.codespace 是码的命名空间不是已经是 CheckTx 码空间，再决定要不要同一次发布。
