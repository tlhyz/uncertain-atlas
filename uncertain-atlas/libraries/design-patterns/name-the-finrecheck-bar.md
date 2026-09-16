# 模式：把 FinalizeBlock When optional recheck 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 9。  
**例**：[optionally re-checks ≠ 已经必须再验](../../tracks/implementation/worked-example-finrecheck-vs-recheck.md)。

## 三个名字

1. **optionally re-checks 不是已经必须再验：** 看见 When 第 9 步 optional，不是已经必须再验才能开下一高。
2. **all outstanding transactions in the mempool 不是已经 new transactions：** 看见再验 outstanding，不是已经新交易不进 CheckTx interchangeable。
3. **against newly persisted Application state 不是已经 Type=RECHECK：** 看见对照刚落盘状态，不是已经 CheckTx Type 栏 interchangeable。

## 为什么要分开叫

官方把 When 第 9 步 optionally re-checks all outstanding transactions in the mempool against the newly persisted Application state 写成三个名字。把它们叫成一个「看见再验了就已经是 Recheck / 已经交差」，会把 optional、outstanding vs new、newly persisted vs Type 栏三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 When 第 9 步再验了就已经交差」，先数清问的是 optionally re-checks 是不是已经必须再验、all outstanding transactions in the mempool 是不是已经 new transactions / 已经 CheckTx 过了，还是 against newly persisted Application state 是不是已经 CheckTxState / ExecuteTxState / 已经 Type=RECHECK bundled，再决定要不要同一次发布。
