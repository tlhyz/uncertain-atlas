# 例：看见 ExecTxResult.gas_used 是这笔用掉的气 is not already counted into consensus interchangeable / not already printed in header interchangeable / not already settled interchangeable

**层次**：实现 / ExecTxResult.gas_used not already counted into consensus / not already printed in header / not already settled 正式三事（393 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.gas_used not already counted into consensus / not already printed in header / not already settled 正式三事（393 余量）/ not 747 exectxgas-notused interchangeable / not 393 exectxgas-vs-checktx bundled interchangeable」，不是 ExecTxResult 气 bundled（393），也不是 CheckTx 那份 GasUsed 已经被引擎算进共识或 Code / Data 就已经印进本头（316）。不要另写怎样写 ExecTxResult 气。

## 官方三件事

1. **看见 ExecTxResult `gas_used` 是这笔用掉的气 / 看见填了 gas_used / Finalize 回执里用掉的气 is not already 已经是 CheckTx 那份 GasUsed 已经被引擎算进共识 interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 747 exectxgas-notused interchangeable / 746 exectxgas-notwanted interchangeable / 393 exectxgas item 1 gas_wanted interchangeable，也不是已经 gas_used not already counted into consensus / not already printed in header / not already settled 正式三事 bundled（393 item 2 余量） interchangeable / 393 exectxgas item 2 interchangeable。**  
   官方写：`gas_used` 是这笔交易用掉的气。看见填了 gas_used，不是已经是 CheckTx 那份 GasUsed 已经被引擎算进共识 interchangeable——本页从 393 item 2 侧钉 not already counted into consensus 单句。393 exectxgas vs checktx bundled unbundling 在本页 item 2 续。

2. **看见填了 gas_used / 看见有用掉的气 / Finalize 回执里用掉的气 is not already 已经是 Code / Data 印进本头 interchangeable / 316 codedata interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 747 exectxgas-notused interchangeable / 393 exectxgas item 3 codespace interchangeable / 748 exectxgas-notcodespace interchangeable。**  
   官方把 Finalize 回执里用掉的气和已经印进本头分开——393 bundled 第二件事常与 316 混成「看见填了 gas_used 就已经印进本头 interchangeable」，本页钉 not already printed in header 单句。

3. **看见填了 gas_used / 看见能回 / Finalize 回执里用掉的气 is not already 已经交差 interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 747 exectxgas-notused interchangeable / 746 exectxgas-notwanted interchangeable。**  
   官方把能回 gas_used 和已经交差分开。看见能回，不是已经交差 interchangeable。393 exectxgas vs checktx bundled unbundling 在本页 item 2 续。

怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气是规范里的做法，本页不抄。

## 官方为什么这样拆

- **gas_used not already counted into consensus ≠ CheckTx GasUsed interchangeable：** 官方把 Finalize 回执里用掉的气和引擎已经按气验过分开。
- **gas_used not already printed in header ≠ 316 interchangeable：** 官方把有用掉的气和 Code / Data 就已经印进本头分开。
- **gas_used not already settled ≠ 已经交差 interchangeable：** 官方把能回 gas_used 和已经交差分开；393 exectxgas vs checktx bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.gas_used 是这笔用掉的气 | 不是已经算进共识 | 不是 gas_wanted（746/393 item 1） |
| 看见填了 gas_used | 不是已经印进本头（316） | 不是 ExecTxResult 气 bundled（393） |
| 看见能回 | 不是已经交差 | 不是 codespace（748/393 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.gas_used not already counted into consensus / not already printed in header / not already settled 正式三事（393 余量），必须分开 gas_used 是不是已经算进共识、是不是已经印进本头 interchangeable / 316、是不是已经交差。可以跳过「看见填了 gas_used 就已经算进共识」。不要另写怎样写 ExecTxResult 气。393 exectxgas vs checktx bundled unbundling 在本页 item 2 续；完成 [`worked-example-exectxgas-notcodespace-vs-bundled.md`](worked-example-exectxgas-notcodespace-vs-bundled.md)（不变量 748 item 3）。

## 本页不抄

- 怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气。
- ExecTxResult 气 bundled。那是不变量 393。
- ExecTxResult.gas_wanted。那是不变量 393 item 1 余量 / 746。
- ExecTxResult.codespace。那是不变量 393 item 3 余量 / 748。
- Code / Data 就已经印进本头。那是不变量 316。
