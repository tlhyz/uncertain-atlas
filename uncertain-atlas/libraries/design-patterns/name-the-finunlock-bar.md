# 模式：把 FinalizeBlock When unlocks mempool 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 10。  
**例**：[unlocks the mempool ≠ 已经交差](../../tracks/implementation/worked-example-finunlock-vs-lock.md)。

## 三个名字

1. **unlocks the mempool 不是已经交差：** 看见 When 第 10 步解锁，不是已经 Finalize + Commit 交差。
2. **newly received transactions can now be checked 不是已经 optional recheck：** 看见新交易现在可以 CheckTx，不是已经再验 outstanding interchangeable。
3. **When 第 10 步 unlock after optional recheck 不是已经开下一高 round 0：** 看见 unlock，不是已经 step 11 开下一高 interchangeable。

## 为什么要分开叫

官方把 When 第 10 步 unlocks the mempool — newly received transactions can now be checked 写成三个名字。把它们叫成一个「看见解锁了就已经能收新交易 / 已经开下一高」，会把 unlock、newly received vs outstanding、step 10 vs step 11 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见解锁了就已经交差」，先数清问的是 unlocks the mempool 是不是已经交差、newly received transactions can now be checked 是不是已经 optional recheck / 已经 CheckTx 技术上可选，还是 When 第 10 步 unlock after optional recheck 是不是已经是 Commit 锁解锁 / 已经开下一高 round 0，再决定要不要同一次发布。
