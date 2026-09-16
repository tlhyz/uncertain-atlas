# 反模式：把 FinalizeBlock When locks mempool 正式三事说成已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[CometBFT locks mempool ≠ 已经交差](../../tracks/implementation/worked-example-finlock-vs-commitlock.md)。

## 错在哪里

把 CometBFT locks the mempool 写成已经交差，或已经四门已经结算；把 no calls to CheckTx on new transactions 写成已经 CheckTx 技术上可选 / 不参与处理块，或已经进了池 / 已经开始流言；把 locks mempool after persist 写成已经是 Commit 锁，或已经解锁，或已经是 Recheck，或已经和 403 / 310 / 312 / 373 / 33 / 587 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When locks mempool 正式三事，必须分开 CometBFT locks the mempool、no calls to CheckTx on new transactions、locks mempool after persist 三件事，不要和 403 / 310 / 312 / 373 / 33 / 587 糊成一句。
