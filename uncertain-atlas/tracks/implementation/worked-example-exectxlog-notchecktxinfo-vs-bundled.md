# 例：看见 ExecTxResult.info 是附加信息 is not already CheckTx info interchangeable / not already Query info interchangeable / not already settled interchangeable

**层次**：实现 / ExecTxResult.info not already CheckTx info / not already Query info / not already settled 正式三事（414 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.info not already CheckTx info / not already Query info / not already settled 正式三事（414 余量）/ not 759 exectxlog-notchecktxinfo interchangeable / not 414 exectxlog-vs-querylog bundled interchangeable」，不是 ExecTxResult 日志栏 bundled（414），也不是 CheckTx 回包 info 就已经是 Query 附加信息（391/754）。不要另写怎样写 ExecTxResult 日志栏。

## 官方三件事

1. **看见 ExecTxResult `info` 是附加信息 / 看见回了信息 / Finalize 回执里这份附加信息 is not already 已经是 CheckTx 回包那份 info interchangeable / 391 checktxtx / 754 checktxtx-notqueryinfo interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 759 exectxlog-notchecktxinfo interchangeable / 758 exectxlog-notquerylog interchangeable / 414 exectxlog item 1 log interchangeable，也不是已经 info not already CheckTx info / not already Query info / not already settled 正式三事 bundled（414 item 2 余量） interchangeable / 414 exectxlog item 2 interchangeable。**  
   官方写：`info` 是附加信息。表上 Deterministic = No。看见回了信息，不是已经是 CheckTx 回包那份 info interchangeable——本页从 414 item 2 侧钉 not already CheckTx info 单句。414 exectxlog vs querylog bundled unbundling 在本页 item 2 续。

2. **看见回了信息 / 看见有附加字段 / Finalize 回执里这份附加信息 is not already 已经是 Query 回包那份附加信息 interchangeable / 384 queryinfo interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 759 exectxlog-notchecktxinfo interchangeable / 414 exectxlog item 3 nondet interchangeable / 760 exectxlog-notheader interchangeable。**  
   官方把 Finalize 回执里这份附加信息和 Query 那份附加信息分开——414 bundled 第二件事常与 391 / 384 混成「看见回了 ExecTxResult.info 就已经是 CheckTx 或 Query 附加信息 interchangeable」，本页钉 not already Query info 单句。

3. **看见回了信息 / 看见能回 / Finalize 回执里这份附加信息 is not already 已经交差 interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 759 exectxlog-notchecktxinfo interchangeable / 758 exectxlog-notquerylog interchangeable。**  
   官方把能回 ExecTxResult.info 和已经交差分开。看见能回，不是已经交差 interchangeable。414 exectxlog vs querylog bundled unbundling 在本页 item 2 续。

怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **info not already CheckTx info ≠ 391/754 interchangeable：** 官方把 Finalize 回执里这份附加信息和 CheckTx 回包那份 info 分开。
- **info not already Query info ≠ 384 interchangeable：** 官方把有附加字段和 Query 回包那份附加信息分开。
- **info not already settled ≠ 已经交差 interchangeable：** 官方把能回 ExecTxResult.info 和已经交差分开；414 exectxlog vs querylog bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.info 是附加信息 | 不是已经是 CheckTx 附加信息（391/754） | 不是 ExecTxResult.log（758/414 item 1） |
| 看见回了信息 | 不是已经是 Query 附加信息（384） | 不是 ExecTxResult 日志栏 bundled（414） |
| 看见能回 | 不是已经交差 | 不是 log / info 非确定（760/414 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.info not already CheckTx info / not already Query info / not already settled 正式三事（414 余量），必须分开 info 是不是已经是 CheckTx 附加信息 interchangeable / 391、是不是已经是 Query 附加信息 interchangeable / 384、是不是已经交差。可以跳过「看见回了 ExecTxResult.info 就已经是 CheckTx 附加信息」。不要另写怎样写 ExecTxResult 日志栏。414 exectxlog vs querylog bundled unbundling 在本页 item 2 续；完成 [`worked-example-exectxlog-notheader-vs-bundled.md`](worked-example-exectxlog-notheader-vs-bundled.md)（不变量 760 item 3）。

## 本页不抄

- 怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息。
- ExecTxResult 日志栏 bundled。那是不变量 414。
- ExecTxResult.log。那是不变量 414 item 1 余量 / 758。
- ExecTxResult.log / info 非确定、此外忽略。那是不变量 414 item 3 余量 / 760。
- CheckTx 回包 info 就已经是 Query 附加信息。那是不变量 391 / 754。
- Query 回包 info 就已经是按键查。那是不变量 384。
