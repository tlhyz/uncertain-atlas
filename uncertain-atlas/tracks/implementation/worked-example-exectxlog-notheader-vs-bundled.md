# 例：看见 ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略 is not already printed in header interchangeable / not already consensus interchangeable / not already settled interchangeable

**层次**：实现 / ExecTxResult.log / info 非确定 not already printed in header / not already consensus / not already settled 正式三事（414 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.log / info 非确定 not already printed in header / not already consensus / not already settled 正式三事（414 余量）/ not 760 exectxlog-notheader interchangeable / not 414 exectxlog-vs-querylog bundled interchangeable」，不是 ExecTxResult 日志栏 bundled（414），也不是 Code / Data 就已经印进本头（316）。不要另写怎样写 ExecTxResult 日志栏。

## 官方三件事

1. **看见 ExecTxResult `log` / `info` 标成非确定、引擎会记日志此外忽略 / 看见记了日志 / Finalize 回执里这两栏 is not already 已经是 Code / Data 那种编进结构、再哈希进下一高度块头的 LastResultsHash interchangeable / 316 codedata interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 760 exectxlog-notheader interchangeable / 758 exectxlog-notquerylog interchangeable / 414 exectxlog item 1 log interchangeable，也不是已经 nondet not already printed in header / not already consensus / not already settled 正式三事 bundled（414 item 3 余量） interchangeable / 414 exectxlog item 3 interchangeable。**  
   官方写：`log` 和 `info` 标成非确定。应用需求页写：Info 和 Log 是非确定的调试字段，CometBFT 会记日志，此外忽略。看见记了日志，不是已经印进本头 interchangeable——本页从 414 item 3 侧钉 not already printed in header 单句。414 exectxlog vs querylog bundled unbundling 在本页 item 3 完成。

2. **看见记了日志 / 看见标成非确定 / Finalize 回执里这两栏 is not already 已经是共识 interchangeable / 316 codedata interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 760 exectxlog-notheader interchangeable / 414 exectxlog item 2 info interchangeable / 759 exectxlog-notchecktxinfo interchangeable。**  
   官方把记日志、此外忽略和已经是共识分开——414 bundled 第三件事常与 316 混成「看见记了日志就已经印进本头或已经是共识 interchangeable」，本页钉 not already consensus 单句。

3. **看见记了日志 / 看见被忽略 / Finalize 回执里这两栏 is not already 已经交差 interchangeable，也不是已经 ExecTxResult 日志栏 bundled（414） interchangeable / 760 exectxlog-notheader interchangeable / 758 exectxlog-notquerylog interchangeable。**  
   官方把被忽略和已经交差分开。看见被忽略，不是已经交差 interchangeable。414 exectxlog vs querylog bundled unbundling 在本页 item 3 完成。

怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息是规范里的做法，本页不抄。

## 官方为什么这样拆

- **nondet not already printed in header ≠ 316 interchangeable：** 官方把记日志、此外忽略和已经印进本头分开。
- **nondet not already consensus ≠ 316 interchangeable：** 官方把标成非确定和已经是共识字段分开。
- **nondet not already settled ≠ 已经交差 interchangeable：** 官方把被忽略和已经交差分开；414 exectxlog vs querylog bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.log / info 标成非确定、引擎会记日志此外忽略 | 不是已经印进本头（316） | 不是 ExecTxResult.log（758/414 item 1） |
| 看见记了日志 | 不是已经是共识（316） | 不是 ExecTxResult 日志栏 bundled（414） |
| 看见被忽略 | 不是已经交差 | 不是 ExecTxResult.info（759/414 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.log / info 非确定 not already printed in header / not already consensus / not already settled 正式三事（414 余量），必须分开是不是已经印进本头 interchangeable / 316、是不是已经是共识 interchangeable / 316、是不是已经交差。可以跳过「看见记了日志就已经印进本头」。不要另写怎样写 ExecTxResult 日志栏。414 exectxlog vs querylog bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExecTxResult 日志栏、怎样填日志、怎样填附加信息。
- ExecTxResult 日志栏 bundled。那是不变量 414。
- ExecTxResult.log。那是不变量 414 item 1 余量 / 758。
- ExecTxResult.info。那是不变量 414 item 2 余量 / 759。
- Code / Data 就已经印进本头。那是不变量 316。
