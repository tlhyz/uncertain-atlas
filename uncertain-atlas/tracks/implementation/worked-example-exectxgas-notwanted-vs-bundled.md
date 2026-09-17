# 例：看见 ExecTxResult.gas_wanted 是这笔要的气 is not already CheckTx GasWanted interchangeable / not already executing interchangeable / not already settled interchangeable

**层次**：实现 / ExecTxResult.gas_wanted not CheckTx GasWanted / not already executing / not already settled 正式三事（393 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.gas_wanted not CheckTx GasWanted / not already executing / not already settled 正式三事（393 余量）/ not 746 exectxgas-notwanted interchangeable / not 393 exectxgas-vs-checktx bundled interchangeable」，不是 ExecTxResult 气 bundled（393），也不是 CheckTx 回包 GasWanted 或 MaxGas 就已经在执行（315）。不要另写怎样写 ExecTxResult 气。

## 官方三件事

1. **看见 ExecTxResult `gas_wanted` 是这笔要的气 / 看见填了 gas_wanted / Finalize 回执里要的气 is not already 已经是 CheckTx 回包那份 GasWanted interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 746 exectxgas-notwanted interchangeable / 747 exectxgas-notused interchangeable / 393 exectxgas item 2 gas_used interchangeable，也不是已经 gas_wanted not CheckTx GasWanted / not already executing / not already settled 正式三事 bundled（393 item 1 余量） interchangeable / 393 exectxgas item 1 interchangeable。**  
   官方写：`gas_wanted` 是这笔交易要的气。看见填了 gas_wanted，不是已经是 CheckTx 回包那份 GasWanted interchangeable——本页从 393 item 1 侧钉 not CheckTx GasWanted 单句。393 exectxgas vs checktx bundled unbundling 在本页 item 1 启动。

2. **看见填了 gas_wanted / 看见有要的气 / Finalize 回执里要的气 is not already 已经是 MaxGas 那种已经在执行 interchangeable / 315 maxgas interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 746 exectxgas-notwanted interchangeable / 393 exectxgas item 3 codespace interchangeable / 748 exectxgas-notcodespace interchangeable。**  
   官方把 Finalize 回执里要的气和已经在执行分开——393 bundled 第一件事常与 315 混成「看见填了 gas_wanted 就已经在执行 interchangeable」，本页钉 not already executing 单句。

3. **看见填了 gas_wanted / 看见能填 / Finalize 回执里要的气 is not already 已经交差 interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 746 exectxgas-notwanted interchangeable / 747 exectxgas-notused interchangeable。**  
   官方把能填 gas_wanted 和已经交差分开。看见能填，不是已经交差 interchangeable。393 exectxgas vs checktx bundled unbundling 在本页 item 1 启动。

怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气是规范里的做法，本页不抄。

## 官方为什么这样拆

- **gas_wanted not CheckTx GasWanted ≠ CheckTx interchangeable：** 官方把 Finalize 回执里要的气和 CheckTx 那份 GasWanted 分开。
- **gas_wanted not already executing ≠ 315 interchangeable：** 官方把有要的气和 MaxGas 就已经在执行分开。
- **gas_wanted not already settled ≠ 已经交差 interchangeable：** 官方把能填 gas_wanted 和已经交差分开；393 exectxgas vs checktx bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.gas_wanted 是这笔要的气 | 不是已经是 CheckTx 的 GasWanted | 不是 gas_used（747/393 item 2） |
| 看见填了 gas_wanted | 不是已经在执行（315） | 不是 ExecTxResult 气 bundled（393） |
| 看见能填 | 不是已经交差 | 不是 codespace（748/393 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.gas_wanted not CheckTx GasWanted / not already executing / not already settled 正式三事（393 余量），必须分开 gas_wanted 是不是已经是 CheckTx 的 GasWanted、是不是已经在执行 interchangeable / 315、是不是已经交差。可以跳过「看见填了 gas_wanted 就已经是 CheckTx 的 GasWanted」。不要另写怎样写 ExecTxResult 气。393 exectxgas vs checktx bundled unbundling 在本页 item 1 启动；续 [`worked-example-exectxgas-notused-vs-bundled.md`](worked-example-exectxgas-notused-vs-bundled.md)（不变量 747 item 2）。

## 本页不抄

- 怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气。
- ExecTxResult 气 bundled。那是不变量 393。
- ExecTxResult.gas_used。那是不变量 393 item 2 余量 / 747。
- ExecTxResult.codespace。那是不变量 393 item 3 余量 / 748。
- MaxGas 就已经在执行。那是不变量 315。
