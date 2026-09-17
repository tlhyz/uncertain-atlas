# 反模式：看见 CheckTx 过了就当成已经按 ExecuteTxState 验过 / 看见两份状态同时在改就当成已经同一份 / 看见 RECHECK 就当成已经是新交易

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[CheckTxState ≠ 已经是 ExecuteTxState](../../tracks/implementation/worked-example-checktxstate-vs-execute.md)。

## 塌法

1. 看见 CheckTx 过了 / 看见进了池并开始流言，就当成已经按 ExecuteTxState 验过，或当成已经按将要执行的那份状态验过。
2. 看见 CheckTxState 和 ExecuteTxState 同时在改，就当成已经同一份状态。
3. 看见 Commit 之后又跑了 CheckTx / 看见 Type 是 RECHECK，就当成已经是一笔新交易，或当成已经解锁。

## 为什么会出事

官方写：CheckTx 验的是 CheckTxState，每次 Commit 结束才重置成最新已提交，而且不能保证就是以后执行时那一份。共识进行当中两份状态可以同时更新。Commit 返回之后还握着锁再验，Type 标明 NEW 还是 RECHECK。

## 和相邻反模式

- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选 ≠ 已经是 ExecuteTxState，不是本页这种 CheckTxState。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页。
