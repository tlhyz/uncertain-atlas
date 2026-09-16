# 反模式：把 FinalizeBlockResponse tx_results returned not Finalize changed already settled / not Code Data printed in this header LastResultsHash / not fintxcode bundled 正式三事（585 余量）说成已经 Finalize 改了就已经交差 / 已经 Code Data 印进本头 / 已经 fintxcode bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse tx_results returned not Finalize changed already settled ≠ bundled（585）](../../tracks/implementation/worked-example-fintxcode-notsettled-vs-bundled.md)。

## 错在哪里

把回了 `tx_results` / 看见有 Code 写成已经 Finalize 改了就已经交差 interchangeable，或已经 Finalize + Commit 交差 interchangeable；把 tx_results 写成已经 Code / Data 印进本头 LastResultsHash interchangeable，或已经是本头 LastResultsHash interchangeable；把 tx_results 写成已经是 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable，或已经 fintxcode bundled interchangeable，或已经和 only if fully valid / CheckTx 过了 / Code 非零仍可能在块里 / 404 / 316 / 335 / 626 / 627 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results returned not Finalize changed already settled / not Code Data printed in this header LastResultsHash / not fintxcode bundled 正式三事（585 余量），必须分开 not already settled、not Code Data printed in this header、not fintxcode bundled 三件事，不要和 585 / 316 / 335 / 404 / 626 / 627 糊成一句。

## 和相邻反模式

- [fintxcode-notchecktx-sold-as-bundled](fintxcode-notchecktx-sold-as-bundled.md) 是 only if fully valid not CheckTx passed（585 item 1 余量 / 626），不是本页 585 item 3 单句边界。
- [fintxcode-notinvalid-sold-as-bundled](fintxcode-notinvalid-sold-as-bundled.md) 是 only if fully valid not still in block（585 item 2 余量 / 627），不是本页 585 item 3 单句边界。
- [fintxcode-sold-as-absent](fintxcode-sold-as-absent.md) 是 585 fintxcode bundled 三事专用，不是本页 585 item 3 单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 Finalize 落盘禁令 bundled（335），不是本页 tx_results returned 单句边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 ExecTxResult 回执 bundled（316），不是本页 tx_results returned 单句边界。
