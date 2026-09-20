# 反模式：看见 ExecTxResult.events 就当成已经印进本头 / 看见标成非确定就当成已经像 Code/Data 那样必须确定 / 看见逐笔 events 就当成已经是 FinalizeBlockResponse.events 或 CheckTxResponse.events

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields。  
**例**：[ExecTxResult.events 是给交易建索引的类型键值事件 ≠ 已经印进本头](../../tracks/implementation/worked-example-exectxevents-vs-header.md)。

## 塌法

1. 看见 `events` is Type & Key-Value events for indexing transactions (e.g. by account) / 看见 ExecTxResult.events 是给交易建索引的类型键值事件，就当成已经印进本头 LastResultsHash，或当成已经像 Code/Data 那样必须确定。
2. 看见 `events` 的 Deterministic 列是 No / 看见 ExecTxResult.events 标成非确定，就当成已经 Code / Data 编进结构再哈希进下一高度块头那种已经交差，或当成已经是共识字段。
3. 看见 `ExecTxResult` 在 `tx_results` 里逐笔出现、每笔有自己的 `events` / 看见 ExecTxResult.events 在 tx_results 里逐笔出现，就当成已经是 FinalizeBlockResponse.events 那种块级索引，或当成已经是 CheckTxResponse.events 那种池门回包。

## 为什么会出事

官方写：`events` 只供按执行里发生的事建索引。Deterministic = No。`code` 和 `data` 会编进结构，再哈希进下一高度块头的 `LastResultsHash`。`FinalizeBlockResponse.events` 是块级索引。`CheckTxResponse.events` 是池门回包。这不是已经印进本头，不是已经像 Code/Data 那样必须确定，也不是已经是块级或池门 events interchangeable。

## 和相邻反模式

- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表/Code/Data 就已经交差，不是本页这种 events 不是已经印进本头。
- [finrespbar-sold-as-header](finrespbar-sold-as-header.md) 是 FinalizeBlockResponse.events 不是已经印进本头，不是本页这种 ExecTxResult.events 逐笔位置。
- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 CheckTx 回包 events 不是已经交差，不是本页这种 Finalize 逐笔 events 不是池门回包。
