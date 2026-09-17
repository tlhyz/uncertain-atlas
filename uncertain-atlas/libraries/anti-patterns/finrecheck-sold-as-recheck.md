# 反模式：把 FinalizeBlock When optional recheck 正式三事说成已经是 Recheck

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[optionally re-checks ≠ 已经必须再验](../../tracks/implementation/worked-example-finrecheck-vs-recheck.md)。

## 错在哪里

把 optionally re-checks 写成已经必须再验，或已经交差 / 已经四门已经结算；把 all outstanding transactions in the mempool 写成已经 new transactions，或已经 CheckTx 过了就永远有效；把 against the newly persisted Application state 写成已经 CheckTxState / ExecuteTxState，或已经 `CheckTx` 的 `Type` 标明 `RECHECK`，或已经和 403 / 588 / 590 / 312 / 484 / 301 / 33 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When optional recheck 正式三事，必须分开 optionally re-checks、all outstanding transactions in the mempool、against newly persisted Application state 三件事，不要和 403 / 588 / 590 / 312 / 484 / 301 / 33 糊成一句。
