# 例：看见 ExecTxResult.events 是给交易建索引的类型键值事件不是已经印进本头；看见 ExecTxResult.events 标成非确定不是已经像 Code/Data 那样必须确定；看见 ExecTxResult.events 在 tx_results 里逐笔出现不是已经是 FinalizeBlockResponse.events 那种块级索引

**层次**：实现 / ExecTxResult events 栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult Fields。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.events 是给交易建索引的类型键值事件不是已经印进本头 / ExecTxResult.events 标成非确定不是已经像 Code/Data 那样必须确定 / ExecTxResult.events 在 tx_results 里逐笔出现不是已经是 FinalizeBlockResponse.events 那种块级索引」，不是 Code / Data 就已经印进本头，也不是 CheckTx 回包 events 就已经交差。不要另写怎样写 ExecTxResult events 栏。

## 官方三件事

规范把 ExecTxResult `events` 是给交易建索引的类型键值事件、`events` 标成非确定、这笔 events 在 `tx_results` 里逐笔出现写成三件独立的实现事，不是「看见 ExecTxResult 里填了 events 就已经印进本头、已经是块级事件、已经是 CheckTx 回包」一件事：

1. **看见 ExecTxResult `events` 是给交易建索引的类型键值事件 / 看见回了 events 不是已经印进本头 LastResultsHash，也不是已经像 Code/Data 那样必须确定。**  
   官方写：`events` is Type & Key-Value events for indexing transactions (e.g. by account). 表上 Deterministic = No。应用需求页写：`Events` 只供 CometBFT 按执行里发生的事建索引、以后按事件查询。看见回了 events，不是已经 Code / Data 编进结构、再哈希进下一高度块头的 `LastResultsHash`。看见能指索引，不是已经印进本头。看见标成非确定，不是已经像 `code` / `data` 那样 Deterministic = Yes。
2. **看见 ExecTxResult `events` 标成非确定 / 看见有 events 不是已经 Code / Data 编进结构再哈希进下一高度块头那种已经交差，也不是已经是共识字段。**  
   官方写：`events` 的 Deterministic 列是 No。`code` 和 `data` 必须确定，会编进一份结构，再哈希进下一高度块头的 `LastResultsHash`。看见有 events，不是已经进了那份哈希。看见标成非确定，不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块那种必须确定。看见能建索引，不是已经交差。
3. **看见 ExecTxResult `events` 在 `tx_results` 里逐笔出现 / 看见每笔有 events 不是已经是 FinalizeBlockResponse.events 那种块级索引，也不是已经是 CheckTxResponse.events 那种池门回包。**  
   官方写：`ExecTxResult` 是 `FinalizeBlockResponse.tx_results` 里执行这块各笔交易得到的结果列表中的元素。每笔 `ExecTxResult` 有自己的 `events`。`FinalizeBlockResponse.events` 另是块级 Type & Key-Value events for indexing。`CheckTxResponse.events` 另是池门回包里的类型键值。看见逐笔 events，不是已经是块级 events。看见 Finalize 回执里 events，不是已经 CheckTx 回包 events interchangeable。

怎样写 ExecTxResult events 栏、怎样填 events、怎样建索引是规范里的做法，本页不抄。Code / Data 就已经印进本头是不变量 316 的另一切片，FinalizeBlockResponse.events 是不变量 431，CheckTx 回包 events 是不变量 381，本页不抄。

## 官方为什么这样拆

- **ExecTxResult.events 是给交易建索引的类型键值事件 ≠ 已经印进本头：** 官方把索引事件和 LastResultsHash 分开。
- **ExecTxResult.events 标成非确定 ≠ 已经像 Code/Data 那样必须确定：** 官方把 Deterministic = No 和 Yes 字段分开。
- **ExecTxResult.events 在 tx_results 里逐笔出现 ≠ 已经是 FinalizeBlockResponse.events / CheckTxResponse.events：** 官方把逐笔回执、块级回包、池门回包分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.events 是给交易建索引的类型键值事件 | 不是已经印进本头 | 不是 Code / Data 就已经印进本头（316） |
| ExecTxResult.events 标成非确定 | 不是已经像 Code/Data 那样必须确定 | 不是 FinalizeBlockResponse.events 标成非确定（431） |
| ExecTxResult.events 在 tx_results 里逐笔出现 | 不是已经是块级 events | 不是 CheckTx 回包 events 就已经交差（381） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 ExecTxResult 里填了 events 就已经印进本头、已经是块级事件、已经是 CheckTx 回包」，必须分开 ExecTxResult.events 是给交易建索引的类型键值事件是不是已经印进本头、ExecTxResult.events 标成非确定是不是已经像 Code/Data 那样必须确定、ExecTxResult.events 在 tx_results 里逐笔出现是不是已经是 FinalizeBlockResponse.events / CheckTxResponse.events。可以跳过「看见 ExecTxResult 里填了 events 就已经印进本头」。不要另写怎样写 ExecTxResult events 栏。

## 本页不抄

- 怎样写 ExecTxResult events 栏、怎样填 events、怎样建索引。
- Code / Data 就已经印进本头。那是不变量 316。
- FinalizeBlockResponse.events 是给索引用的类型键值事件。那是不变量 431。
- CheckTx 回包 events 是给索引用的类型键值。那是不变量 381。
