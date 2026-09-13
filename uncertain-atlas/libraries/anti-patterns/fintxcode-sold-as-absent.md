# 反模式：把 FinalizeBlock tx_results Code==0 完全合法正式三事说成已经 CheckTx 过了

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Code == 0 only if fully valid ≠ 已经 CheckTx 过了](../../tracks/implementation/worked-example-fintxcode-vs-invalid.md)。

## 错在哪里

把 `FinalizeBlockResponse.tx_results[i].Code == 0` only if the i-th transaction is fully valid 写成已经 CheckTx 过了，或已经 Process 回了 Accept；把 Code == 0 only if fully valid 写成已经 Code != 0 那种没进块，或已经无效就不在块里；把回了 tx_results 写成已经 Finalize 改了就已经交差，或已经 Code / Data 印进本头，或已经和 404 / 316 / 335 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock tx_results Code==0 完全合法正式三事，必须分开 only if fully valid、Code 非零仍可能在块里、回了 tx_results 三件事，不要和 404 / 316 / 335 / 339 糊成一句。
