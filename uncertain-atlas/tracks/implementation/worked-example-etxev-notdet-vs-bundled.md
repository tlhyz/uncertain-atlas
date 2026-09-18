# 例：看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定不是已经是共识字段；看见ExecTxResult.events marked non-deterministic is not already like Code/Data不是已经编进结构再哈希；看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定不是已经必须确定

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields events 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxEv tx events marked non-deterministic not already consensus-field / not already hashed / not already 316-det 正式三事（446 余量）/ not 1363 etxev-notdet interchangeable / not 446 exectxevents-vs-header bundled interchangeable」，不是 exectxevents vs header bundled（446），也不是已经 FinalizeBlockResponse.events 标成非确定（431），也不是已经 Code / Data 必须确定（316）。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。

## 官方三件事

1. **看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定 / 看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定 这份对象 is not already 已经是共识字段 interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1363 etxev-notdet interchangeable / 1362 etxev-notidx interchangeable，也不是已经 ExecTxEv tx events marked non-deterministic not already consensus-field / not already hashed / not already 316-det 正式三事 bundled（446 item 2 余量） interchangeable / 446 etxev item 2 interchangeable。**  
   官方把ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定和已经是共识字段写成两件。看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定，不是已经是共识字段。

2. **看见ExecTxResult.events marked non-deterministic is not already like Code/Data / 看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定 / 这份对象 is not already 已经编进结构再哈希 interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1363 etxev-notdet interchangeable / 1364 etxev-notlvl interchangeable，也不是已经 FinalizeBlockResponse.events 标成非确定 interchangeable / 431 FinalizeBlockResponse.events 标成非确定 interchangeable。**  
   官方把ExecTxResult.events marked non-deterministic is not already like Code/Data和已经编进结构再哈希写成两件。看见ExecTxResult.events marked non-deterministic is not already like Code/Data，不是已经编进结构再哈希。

3. **看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定 / 看见ExecTxResult.events marked non-deterministic is not already like Code/Data / 这份对象 is not already 已经必须确定 interchangeable，也不是已经 exectxevents vs header bundled（446） interchangeable / 1363 etxev-notdet interchangeable / 1362 etxev-notidx interchangeable，也不是已经 Code / Data 必须确定 interchangeable / 316 Code / Data 必须确定 interchangeable。**  
   官方把ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定和已经必须确定写成两件。看见ExecTxResult.events 标成非确定不是已经像 Code/Data 必须确定，不是已经必须确定。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。

## 官方为什么这样拆

- **Deterministic = No 不是已经是共识字段 interchangeable：官方把 No 列和 Yes 列分开。**
- **看见有 events 不是已经进了 LastResultsHash。**
- **看见标成非确定 不是已经 Finalize 状态必须确定那种必须确定。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是共识字段 | 不是已经是共识字段 | 不是已经FinalizeBlockResponse.events 标成非确定（431） |
| 已经编进结构再哈希 | 不是已经编进结构再哈希 | 不是已经Code / Data 必须确定（316） |
| 已经必须确定 | 不是已经必须确定 | 不是已经1362 etxev-notidx |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxEv tx events marked non-deterministic not already consensus-field / not already hashed / not already 316-det 正式三事（446 余量），必须分开是不是已经是共识字段、是不是已经编进结构再哈希、是不是已经必须确定。可以跳过「看见 ExecTxResult 里填了 events 就已经印进本头」。不要另写 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。446 ExecTxResult events vs header bundled unbundling 在本页 item 2 续；续 [`worked-example-etxev-notlvl-vs-bundled.md`](worked-example-etxev-notlvl-vs-bundled.md)（不变量 1364 item 3）。

## 本页不抄

- 怎样写 ExecTxResult events 栏、怎样填 events、怎样建索引。
- 怎样把 events 印进 LastResultsHash、怎样把逐笔 events 写成块级 events、怎样把 Finalize events 写成 CheckTx events。
