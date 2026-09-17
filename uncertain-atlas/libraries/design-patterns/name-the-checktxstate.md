# 模式：把 CheckTxState 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[CheckTxState ≠ 已经是 ExecuteTxState](../../tracks/implementation/worked-example-checktxstate-vs-execute.md)。

## 三个名字

1. **CheckTxState 不是已经按 ExecuteTxState 验过：** 看见 CheckTx 过了不是已经按将要执行的那份状态验过。
2. **同时在改不是已经同一份：** 看见两份状态同时更新不是已经合并。
3. **RECHECK 不是已经是新交易：** 看见 Commit 之后又跑了 CheckTx 不是已经解锁。

## 为什么要分开叫

官方把 CheckTxState、ExecuteTxState、RECHECK 再验写成三件事。把它们叫成一个「看见 CheckTx 过了就已经按将要执行的那份验过」，会把候选、Commit 锁和池交接一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「CheckTx 已经过了」，先数清问的是 CheckTxState 不是已经按 ExecuteTxState 验过、同时在改不是已经同一份，还是 RECHECK 不是已经是新交易，再决定要不要同一次发布。
