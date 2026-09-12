# 例：看见 ExecTxResult.log 是应用日志的输出不是已经是 Query 日志；看见 ExecTxResult.info 是附加信息不是已经是 CheckTx 附加信息；看见 ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略不是已经印进本头

**层次**：实现 / ExecTxResult 日志栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.log 是应用日志的输出不是已经是 Query 日志 / ExecTxResult.info 是附加信息不是已经是 CheckTx 附加信息 / ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略不是已经印进本头」，不是 Query 回包 log 就已经新鲜，也不是 CheckTx 回包 info 就已经是 Query 附加信息。不要另写怎样写 ExecTxResult 日志栏。

## 官方三件事

规范把 ExecTxResult `log` 是应用日志的输出、`info` 是附加信息、这两栏标成非确定且引擎会记日志此外忽略写成三件独立的实现事，不是「看见填了 ExecTxResult 日志栏就已经是 Query 日志、已经是 CheckTx 附加信息、已经印进本头」一件事：

1. **看见 ExecTxResult `log` 是应用日志的输出 / 看见回了日志 不是已经是 Query 日志，也不是已经新鲜。**  
   官方写：`log` 是应用日志的输出。表上 Deterministic = No。看见回了日志，不是已经是 Query 回包那份 log。看见有日志，不是已经新鲜。看见能回，不是已经交差。
2. **看见 ExecTxResult `info` 是附加信息 / 看见回了信息 不是已经是 CheckTx 附加信息，也不是已经是 Query 附加信息。**  
   官方写：`info` 是附加信息。表上 Deterministic = No。看见回了信息，不是已经是 CheckTx 回包那份 info。看见有附加字段，不是已经是 Query 回包那份附加信息。看见能回，不是已经交差。
3. **看见 ExecTxResult `log` / `info` 标成非确定、引擎会记日志此外忽略 / 看见记了日志 不是已经印进本头，也不是已经是共识。**  
   官方写：`log` 和 `info` 标成非确定。应用需求页写：Info 和 Log 是非确定的调试字段，CometBFT 会记日志，此外忽略。看见记了日志，不是已经是 Code / Data 那种编进结构、再哈希进下一高度块头的 LastResultsHash。看见标成非确定，不是已经印进本头。看见被忽略，不是已经交差。

怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息是规范里的做法，本页不抄。Query 回包 log 就已经新鲜是不变量 384，本页不抄。

## 官方为什么这样拆

- **ExecTxResult.log 是应用日志的输出 ≠ 已经是 Query 日志：** 官方把 Finalize 回执里这份日志和 Query 回包那份日志分开。
- **ExecTxResult.info 是附加信息 ≠ 已经是 CheckTx 附加信息：** 官方把 Finalize 回执里这份附加信息和 CheckTx 回包那份 info 分开。
- **ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略 ≠ 已经印进本头：** 官方把记日志、此外忽略和已经印进本头分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.log 是应用日志的输出 | 不是已经是 Query 日志 | 不是 Query 回包 log 就已经新鲜（384） |
| ExecTxResult.info 是附加信息 | 不是已经是 CheckTx 附加信息 | 不是 CheckTx 回包 info 就已经是 Query 附加信息（391） |
| ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略 | 不是已经印进本头 | 不是 Code / Data 就已经印进本头（316） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExecTxResult 日志栏就已经是 Query 日志、已经是 CheckTx 附加信息、已经印进本头」，必须分开 ExecTxResult.log 是应用日志的输出是不是已经是 Query 日志、ExecTxResult.info 是附加信息是不是已经是 CheckTx 附加信息、ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略是不是已经印进本头。可以跳过「看见填了 ExecTxResult 日志栏就已经是 Query 日志」。不要另写怎样写 ExecTxResult 日志栏。

## 本页不抄

- 怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息。
- Query 回包 log 就已经新鲜。那是不变量 384。
- CheckTx 回包 info 就已经是 Query 附加信息。那是不变量 391。
- Code / Data 就已经印进本头。那是不变量 316。
