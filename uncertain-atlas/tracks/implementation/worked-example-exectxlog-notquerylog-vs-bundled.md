# 例：看见 ExecTxResult.log 是应用日志的输出 is not already Query log interchangeable / not already fresh interchangeable / not already settled interchangeable

**层次**：实现 / ExecTxResult.log not already Query log / not already fresh / not already settled 正式三事（414 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.log not already Query log / not already fresh / not already settled 正式三事（414 余量）/ not 758 exectxlog-notquerylog interchangeable / not 414 exectxlog-vs-querylog bundled interchangeable」，不是 ExecTxResult 日志栏 bundled（414），也不是 Query 回包 log 就已经新鲜（384），也不是 CheckTx 回包 log 就已经是 Query 日志（390/745）。不要另写怎样写 ExecTxResult 日志栏。

## 官方三件事

1. **看见 ExecTxResult `log` 是应用日志的输出 / 看见回了日志 / Finalize 回执里这份日志 is not already 已经是 Query 回包那份 log interchangeable / 384 querylog interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 758 exectxlog-notquerylog interchangeable / 759 exectxlog-notchecktxinfo interchangeable / 414 exectxlog item 2 info interchangeable，也不是已经 log not already Query log / not already fresh / not already settled 正式三事 bundled（414 item 1 余量） interchangeable / 414 exectxlog item 1 interchangeable。**  
   官方写：`log` 是应用日志的输出。表上 Deterministic = No。看见回了日志，不是已经是 Query 回包那份 log interchangeable——本页从 414 item 1 侧钉 not already Query log 单句。414 exectxlog vs querylog bundled unbundling 在本页 item 1 启动。

2. **看见回了日志 / 看见有日志 / Finalize 回执里这份日志 is not already 已经新鲜 interchangeable / 384 querylog interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 758 exectxlog-notquerylog interchangeable / 414 exectxlog item 3 nondet interchangeable / 760 exectxlog-notheader interchangeable，也不是已经 CheckTx 回包 log 就已经是 Query 日志 interchangeable / 390 proofop / 745 proofop-notquerylog interchangeable。**  
   官方把 Finalize 回执里这份日志和已经新鲜分开——414 bundled 第一件事常与 384 / 390 混成「看见回了 ExecTxResult.log 就已经是 Query 日志或已经新鲜 interchangeable」，本页钉 not already fresh 单句。

3. **看见回了日志 / 看见能回 / Finalize 回执里这份日志 is not already 已经交差 interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 758 exectxlog-notquerylog interchangeable / 759 exectxlog-notchecktxinfo interchangeable。**  
   官方把能回 ExecTxResult.log 和已经交差分开。看见能回，不是已经交差 interchangeable。414 exectxlog vs querylog bundled unbundling 在本页 item 1 启动。

怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **log not already Query log ≠ 384 interchangeable：** 官方把 Finalize 回执里这份日志和 Query 回包那份日志分开。
- **log not already fresh ≠ 384/390 interchangeable：** 官方把有日志和已经新鲜 / CheckTx 回包 log 就已经是 Query 日志分开。
- **log not already settled ≠ 已经交差 interchangeable：** 官方把能回 ExecTxResult.log 和已经交差分开；414 exectxlog vs querylog bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.log 是应用日志的输出 | 不是已经是 Query 日志（384） | 不是 ExecTxResult.info（759/414 item 2） |
| 看见回了日志 | 不是已经新鲜（384） | 不是 CheckTx 回包 log（390/745） |
| 看见能回 | 不是已经交差 | 不是 ExecTxResult 日志栏 bundled（414） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.log not already Query log / not already fresh / not already settled 正式三事（414 余量），必须分开 log 是不是已经是 Query 日志 interchangeable / 384、是不是已经新鲜、是不是已经交差。可以跳过「看见回了 ExecTxResult.log 就已经是 Query 日志」。不要另写怎样写 ExecTxResult 日志栏。414 exectxlog vs querylog bundled unbundling 在本页 item 1 启动；续 [`worked-example-exectxlog-notchecktxinfo-vs-bundled.md`](worked-example-exectxlog-notchecktxinfo-vs-bundled.md)（不变量 759 item 2）。

## 本页不抄

- 怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息。
- ExecTxResult 日志栏 bundled。那是不变量 414。
- ExecTxResult.info。那是不变量 414 item 2 余量 / 759。
- ExecTxResult.log / info 非确定、此外忽略。那是不变量 414 item 3 余量 / 760。
- Query 回包 log 就已经新鲜。那是不变量 384。
- CheckTx 回包 log 就已经是 Query 日志。那是不变量 390 / 745。
