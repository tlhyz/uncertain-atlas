# 反模式：把 FinalizeBlock When calls Commit instruct persist 正式三事说成已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[CometBFT calls Commit ≠ 已经交差](../../tracks/implementation/worked-example-fincommit-vs-persist.md)。

## 错在哪里

把 CometBFT calls Commit 写成已经交差，或已经四门已经结算；把 instruct the Application to persist its state 写成已经引擎 persist tx outputs / AppHash / ResultsHash，或已经 Commit Usage Signal persist bundled interchangeable；把 When 第 8 步 calls Commit after lock mempool 写成已经是 Commit 锁，或已经 optional recheck / unlock / 已经是 Recheck，或已经和 335 / 481 / 587 / 588 / 403 / 399 / 33 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calls Commit instruct persist 正式三事，必须分开 CometBFT calls Commit、instruct Application to persist its state、When 第 8 步 calls Commit after lock mempool 三件事，不要和 335 / 481 / 587 / 588 / 403 / 399 / 33 糊成一句。
