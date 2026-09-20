# 例：看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头不是已经印进本头 LastResultsHash；看见ExecTxResult.events are type-kv index events is not already in the header不是已经像 Code/Data 必须确定；看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头不是已经交差

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields events 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxEv tx events are index kv not already LastResultsHash / not already Code-Data-det / not already in-header 正式三事（446 余量）/ not 1362 etxev-notidx interchangeable / not 446 exectxevents-vs-header bundled interchangeable」，不是 exectxevents vs header bundled（446），也不是已经 Code / Data 就已经印进本头（316），也不是已经 FinalizeBlockResponse.events 栏（431）。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。

## 官方三件事

1. **看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头 / 看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头 这份对象 is not already 已经印进本头 LastResultsHash interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1362 etxev-notidx interchangeable / 1363 etxev-notdet interchangeable，也不是已经 ExecTxEv tx events are index kv not already LastResultsHash / not already Code-Data-det / not already in-header 正式三事 bundled（446 item 1 余量） interchangeable / 446 etxev item 1 interchangeable。**  
   官方把ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头和已经印进本头 LastResultsHash写成两件。看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头，不是已经印进本头 LastResultsHash。

2. **看见ExecTxResult.events are type-kv index events is not already in the header / 看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头 / 这份对象 is not already 已经像 Code/Data 必须确定 interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1362 etxev-notidx interchangeable / 1364 etxev-notlvl interchangeable，也不是已经 Code / Data 就已经印进本头 interchangeable / 316 Code / Data 就已经印进本头 interchangeable。**  
   官方把ExecTxResult.events are type-kv index events is not already in the header和已经像 Code/Data 必须确定写成两件。看见ExecTxResult.events are type-kv index events is not already in the header，不是已经像 Code/Data 必须确定。

3. **看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头 / 看见ExecTxResult.events are type-kv index events is not already in the header / 这份对象 is not already 已经交差 interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1362 etxev-notidx interchangeable / 1363 etxev-notdet interchangeable，也不是已经 FinalizeBlockResponse.events 栏 interchangeable / 431 FinalizeBlockResponse.events 栏 interchangeable。**  
   官方把ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头和已经交差写成两件。看见ExecTxResult.events 是给交易建索引的类型键值不是已经印进本头，不是已经交差。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。

## 官方为什么这样拆

- **索引事件 不是已经印进本头 interchangeable：官方把 Events 建索引和 LastResultsHash 分开。**
- **看见能指索引 不是已经像 code/data 那样 Deterministic = Yes。**
- **看见回了 events 不是已经 Code/Data 编进结构再哈希。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经印进本头 LastResultsHash | 不是已经印进本头 LastResultsHash | 不是已经Code / Data 就已经印进本头（316） |
| 已经像 Code/Data 必须确定 | 不是已经像 Code/Data 必须确定 | 不是已经FinalizeBlockResponse.events 栏（431） |
| 已经交差 | 不是已经交差 | 不是已经1363 etxev-notdet |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxEv tx events are index kv not already LastResultsHash / not already Code-Data-det / not already in-header 正式三事（446 余量），必须分开是不是已经印进本头 LastResultsHash、是不是已经像 Code/Data 必须确定、是不是已经交差。可以跳过「看见 ExecTxResult 里填了 events 就已经印进本头」。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。446 ExecTxResult events vs header bundled unbundling 在本页 item 1 启动；续 [`worked-example-etxev-notdet-vs-bundled.md`](worked-example-etxev-notdet-vs-bundled.md)（不变量 1363 item 2）。

## 本页不抄

- 怎样写 ExecTxResult events 栏、怎样填 events、怎样建索引。
- 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。
