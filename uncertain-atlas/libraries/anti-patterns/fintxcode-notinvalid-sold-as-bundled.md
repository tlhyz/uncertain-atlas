# 反模式：把 FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block / not no index / not fintxcode bundled 正式三事（585 余量）说成已经 Code != 0 那种没进块 / 已经没索引 / 已经 fintxcode bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block ≠ bundled（585）](../../tracks/implementation/worked-example-fintxcode-notinvalid-vs-bundled.md)。

## 错在哪里

把 Code == 0 only if fully valid 写成已经 Code != 0 那种没进块 interchangeable，或已经 Code 非零仍可能在块里 interchangeable；把 only if fully valid 写成已经无效就不建索引 interchangeable，或已经没索引就等于没进块 interchangeable；把 only if fully valid 写成已经是 FinalizeBlock tx_results Code==0 完全合法正式三事 bundled（585） interchangeable，或已经 fintxcode bundled interchangeable，或已经和 CheckTx 过了 / 回了 tx_results 已经交差 / 404 / 316 / 335 / 312 / 626 / 628 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse tx_results Code==0 only if fully valid not Code != 0 still in block / not no index / not fintxcode bundled 正式三事（585 余量），必须分开 not still in block、not no index、not fintxcode bundled 三件事，不要和 585 / 316 / 312 / 404 / 626 / 628 糊成一句。

## 和相邻反模式

- [fintxcode-notchecktx-sold-as-bundled](fintxcode-notchecktx-sold-as-bundled.md) 是 only if fully valid not CheckTx passed（585 item 1 余量 / 626），不是本页 585 item 2 单句边界。
- [fintxcode-sold-as-absent](fintxcode-sold-as-absent.md) 是 585 fintxcode bundled 三事专用，不是本页 585 item 2 单句边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 ExecTxResult 回执 bundled（316），不是本页 only if fully valid 单句边界。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是 CheckTx 可选 bundled（312），不是本页 only if fully valid 单句边界。
