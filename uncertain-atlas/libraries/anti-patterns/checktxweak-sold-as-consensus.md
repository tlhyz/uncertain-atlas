# 反模式：看见不该验排序相关有效性就当成已经该在 CheckTx 里验 / 看见拜占庭能提案一满块无效交易就当成已经被池子挡住 / 看见 ProcessProposal 对付这种行为就当成已经是 CheckTx

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**例**：[不该验排序相关有效性 ≠ 已经该在 CheckTx 里验](../../tracks/implementation/worked-example-checktx-weak-vs-process.md)。

## 塌法

1. 看见 CheckTx 不该验所有有效性 / 看见有效性依赖排序，就当成已经该在 CheckTx 里验排序，或当成已经按将要执行的那份验过。
2. 看见拜占庭可以不在乎 CheckTx / 看见能提案一满块无效交易，就当成已经被池子挡住，或当成已经进不了共识。
3. 看见从 ABCI 1.0 起有 ProcessProposal 对付这种行为 / 看见规范点名 ProcessProposal，就当成已经是 CheckTx，或当成已经是 Finalize。

## 为什么会出事

官方写：CheckTx 只是弱过滤器，不该把影响有效性的每件事都验完，尤其是依赖排序的那些。拜占庭可以不在乎 CheckTx，想的话就能提案一满块无效交易。从 ABCI 1.0 起，对付这种行为的机制是 ProcessProposal。

## 和相邻反模式

- [checktx-notordering-sold-as-bundled](checktx-notordering-sold-as-bundled.md) 是不该验排序相关有效性不是已经该在 CheckTx 里验 item 1 单句边界，不是本页 CheckTx 弱过滤器 bundled 全段。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ 已经是 ExecuteTxState，不是本页这种不该验排序 ≠ 已经该在 CheckTx 里验。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种拜占庭能提案无效块 ≠ 已经被池子挡住。
- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是索引器 ≠ 已经保证不重放，不是本页这种 ProcessProposal 对付这种行为 ≠ 已经是 CheckTx。
