# 反模式：把 FinalizeBlock When lock mempool Commit recheck 正式三事说成已经是 Commit 锁

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[locks mempool ≠ 已经是 Commit 锁](../../tracks/implementation/worked-example-finlock-vs-commit.md)。

## 错在哪里

把 CometBFT locks the mempool / no CheckTx on new transactions 写成已经是 Commit 锁，或已经 RPC 安全默认锁；把 calls Commit to persist application state 写成已经引擎 persist tx outputs / AppHash / ResultsHash，或已经 Finalize 改了就已经落盘；把 optionally recheck / unlock / start h+1 round 0 写成已经是 Recheck，或已经能往下走 / 已经交差，或已经和 403 / 467 / 310 / 312 / 335 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When lock mempool Commit recheck 正式三事，必须分开 locks mempool、calls Commit、optionally recheck / unlock / start h+1 三件事，不要和 403 / 467 / 310 / 312 / 335 糊成一句。
