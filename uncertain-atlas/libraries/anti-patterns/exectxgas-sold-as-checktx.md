# 反模式：看见 ExecTxResult.gas_wanted 是这笔要的气就当成已经是 CheckTx 的 GasWanted / 看见 ExecTxResult.gas_used 是这笔用掉的气就当成已经算进共识 / 看见 ExecTxResult.codespace 是码的命名空间就当成已经是 CheckTx 码空间

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**例**：[ExecTxResult.gas_wanted 是这笔要的气 ≠ 已经是 CheckTx 的 GasWanted](../../tracks/implementation/worked-example-exectxgas-vs-checktx.md)。

## 塌法

1. 看见 ExecTxResult `gas_wanted` 是这笔要的气 / 看见填了 gas_wanted，就当成已经是 CheckTx 的 GasWanted，或当成已经在执行。
2. 看见 ExecTxResult `gas_used` 是这笔用掉的气 / 看见填了 gas_used，就当成已经算进共识，或当成已经印进本头。
3. 看见 ExecTxResult `codespace` 是码的命名空间 / 看见写了空间，就当成已经是 CheckTx 码空间，或当成已经是回包码。

## 为什么会出事

官方写：`gas_wanted` 是这笔交易要的气。`gas_used` 是这笔交易用掉的气。`codespace` 是这个 `code` 的命名空间。

## 和相邻反模式

- [maxgas-sold-as-enforced](maxgas-sold-as-enforced.md) 是 MaxGas 就已经在执行，不是本页这种 ExecTxResult.gas_wanted 是这笔要的气不是已经是 CheckTx 的 GasWanted。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Code / Data 就已经印进本头，不是本页这种 ExecTxResult.gas_used 是这笔用掉的气不是已经算进共识。
- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 CheckTx 回包 codespace 就已经是回包码，不是本页这种 ExecTxResult.codespace 是码的命名空间不是已经是 CheckTx 码空间。
