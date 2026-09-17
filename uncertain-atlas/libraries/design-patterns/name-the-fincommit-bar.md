# 模式：把 FinalizeBlock When calls Commit instruct persist 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 8。  
**例**：[CometBFT calls Commit ≠ 已经交差](../../tracks/implementation/worked-example-fincommit-vs-persist.md)。

## 三个名字

1. **CometBFT calls Commit 不是已经交差：** 看见 When 第 8 步叫 Commit，不是已经 Finalize + Commit 交差。
2. **instruct Application to persist its state 不是已经引擎 persist 这三份：** 看见 instruct persist，不是已经 CometBFT persists tx outputs / AppHash / ResultsHash interchangeable。
3. **When 第 8 步 calls Commit after lock mempool 不是已经是 Commit 锁 / 已经 Commit Usage signal bundled：** 看见 lock 之后才 Commit，不是已经 Commit 锁 / recheck / unlock interchangeable。

## 为什么要分开叫

官方把 When 第 8 步 calls `Commit` to instruct the Application to persist its state 写成三个名字。把它们叫成一个「看见 When 第 8 步叫了 Commit 就已经交差、已经在 Finalize 落了」，会把交差、引擎 persist 这三份、Commit Usage signal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 Commit 就已经交差」，先数清问的是 CometBFT calls Commit 是不是已经交差、instruct Application to persist its state 是不是已经引擎 persist 这三份 / 已经 Commit Usage signal bundled，还是 When 第 8 步 calls Commit after lock mempool 是不是已经是 Commit 锁 / 已经 recheck / unlock，再决定要不要同一次发布。
