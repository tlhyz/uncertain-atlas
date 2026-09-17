# 反模式：把 FinalizeBlock When against newly persisted Application state not Type=RECHECK / not CheckTxState / ExecuteTxState / not finrecheck bundled 正式三事（591 余量）说成已经 Type=RECHECK / 已经 CheckTxState / ExecuteTxState / 已经 finrecheck bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock When against newly persisted Application state not Type=RECHECK ≠ bundled（591）](../../tracks/implementation/worked-example-finrecheck-nottype-vs-bundled.md)。

## 错在哪里

把 against the newly persisted Application state / 对照刚落盘的应用状态 写成已经 Type=RECHECK interchangeable，或已经 CheckTxRequest Type RECHECK interchangeable；把 re-checks against newly persisted 写成已经 CheckTxState interchangeable / ExecuteTxState interchangeable，或已经 CheckTx 只是弱过滤器 interchangeable；把 When 第 9 步 optional recheck 对象 写成已经是 FinalizeBlock When optional recheck 正式三事 bundled（591） interchangeable，或已经 finrecheck bundled interchangeable，或已经和 optionally re-checks / outstanding txs / 312 / 339 / 635 / 636 / 634 / 403 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When against newly persisted Application state not Type=RECHECK / not CheckTxState / ExecuteTxState / not finrecheck bundled 正式三事（591 余量），必须分开 not Type=RECHECK、not CheckTxState / ExecuteTxState、not finrecheck bundled 三件事，不要和 591 / 312 / 484 / 339 / 310 / 635 / 636 / 634 / 335 糊成一句。

## 和相邻反模式

- [finrecheck-notoutstanding-sold-as-bundled](finrecheck-notoutstanding-sold-as-bundled.md) 是 591 item 2 余量 / 636 专用，不是本页 591 item 3 单句边界。
- [finrecheck-notmust-sold-as-bundled](finrecheck-notmust-sold-as-bundled.md) 是 591 item 1 余量 / 635 专用，不是本页 591 item 3 单句边界。
- [finrecheck-sold-as-recheck](finrecheck-sold-as-recheck.md) 是 optional recheck（591）专用，不是本页 591 item 3 单句边界。
- [finafter-notrecheck-sold-as-bundled](finafter-notrecheck-sold-as-bundled.md) 是 403 item 3 余量 / 634 专用，不是本页 591 item 3 单句边界。
