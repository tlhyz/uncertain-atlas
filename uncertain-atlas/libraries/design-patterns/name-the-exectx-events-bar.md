# 模式：把 ExecTxResult events 栏正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields。  
**例**：[ExecTxResult.events 是给交易建索引的类型键值事件 ≠ 已经印进本头](../../tracks/implementation/worked-example-exectxevents-vs-header.md)。

## 三个名字

1. **ExecTxResult.events 是给交易建索引的类型键值事件不是已经印进本头 / 已经像 Code/Data 那样必须确定：** 看见回了 events 不是 LastResultsHash。
2. **ExecTxResult.events 标成非确定不是已经 Code / Data 编进结构再哈希进下一高度块头那种已经交差：** 看见 Deterministic = No 不是 Yes 字段。
3. **ExecTxResult.events 在 tx_results 里逐笔出现不是已经是 FinalizeBlockResponse.events / CheckTxResponse.events：** 看见逐笔 events 不是块级或池门回包。

## 为什么要分开叫

官方把 ExecTxResult `events` 索引用途、非确定标记、逐笔位置写成三个名字。把它们叫成一个「看见 ExecTxResult 里填了 events 就已经印进本头」，会把逐笔 events 和块级 events、CheckTx events 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 ExecTxResult 里填了 events 就已经印进本头」，先数清问的是 ExecTxResult.events 是给交易建索引的类型键值事件不是已经印进本头、ExecTxResult.events 标成非确定不是已经像 Code/Data 那样必须确定，还是 ExecTxResult.events 在 tx_results 里逐笔出现不是已经是 FinalizeBlockResponse.events / CheckTxResponse.events，再决定要不要同一次发布。
