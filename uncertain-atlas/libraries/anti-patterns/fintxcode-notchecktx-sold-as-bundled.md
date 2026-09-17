# 反模式：把 FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed / not Process Accept / not fintxcode bundled 正式三事（585 余量）说成已经 CheckTx 过了 / 已经 Process Accept / 已经 fintxcode bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed ≠ bundled（585）](../../tracks/implementation/worked-example-fintxcode-notchecktx-vs-bundled.md)。

## 错在哪里

把 `FinalizeBlockResponse.tx_results[i].Code == 0` only if the _i_-th transaction is fully valid 写成已经 CheckTx 过了 interchangeable，或已经 CheckTx 弱过滤器 interchangeable；把 only if fully valid 写成已经 Process 回了 Accept interchangeable，或已经 ProcessProposal ACCEPT interchangeable；把 only if fully valid 写成已经是 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable，或已经 fintxcode bundled interchangeable，或已经和 Code 非零仍可能在块里 / 回了 tx_results 已经交差 / 404 / 316 / 335 / 339 / 347 / 627 / 628 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results Code==0 only if fully valid not CheckTx passed / not Process Accept / not fintxcode bundled 正式三事（585 余量），必须分开 not CheckTx passed、not Process Accept、not fintxcode bundled 三件事，不要和 585 / 404 / 316 / 335 / 339 / 347 / 627 / 628 糊成一句。

## 和相邻反模式

- [fintxcode-sold-as-absent](fintxcode-sold-as-absent.md) 是 585 fintxcode bundled 三事专用，不是本页 585 item 1 only if fully valid 单句边界。
- [checktxweak-sold-as-consensus](checktxweak-sold-as-consensus.md) 是 CheckTx 弱过滤器 bundled（339），不是本页 only if fully valid 单句边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 ExecTxResult 回执 bundled（316），不是本页 only if fully valid 单句边界。
- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Finalize 回包余量 bundled（404），不是本页 only if fully valid 单句边界。
