# 反模式：把 FinalizeBlock When unlocks mempool 正式三事说成已经能收新交易

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[unlocks the mempool ≠ 已经交差](../../tracks/implementation/worked-example-finunlock-vs-lock.md)。

## 错在哪里

把 unlocks the mempool 写成已经交差，或已经四门已经结算；把 newly received transactions can now be checked 写成已经 optional recheck outstanding txs，或已经 CheckTx 技术上可选 / 不参与处理块；把 When 第 10 步 unlock after optional recheck 写成已经是 Commit 锁解锁，或已经 starts consensus for h+1 round 0，或已经和 588 / 591 / 590 / 403 / 310 / 373 / 33 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When unlocks mempool 正式三事，必须分开 unlocks the mempool、newly received transactions can now be checked、When 第 10 步 unlock after optional recheck 三件事，不要和 588 / 591 / 590 / 403 / 310 / 373 / 33 糊成一句。
