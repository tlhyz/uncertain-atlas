# 例：看见 ExecTxResult.codespace 是码的命名空间 is not already CheckTx codespace interchangeable / not already response code interchangeable / not already settled interchangeable

**层次**：实现 / ExecTxResult.codespace not CheckTx codespace / not already response code / not already settled 正式三事（393 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExecTxResult。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExecTxResult.codespace not CheckTx codespace / not already response code / not already settled 正式三事（393 余量）/ not 748 exectxgas-notcodespace interchangeable / not 393 exectxgas-vs-checktx bundled interchangeable」，不是 ExecTxResult 气 bundled（393），也不是 CheckTx 回包 codespace 就已经是回包码（381）。不要另写怎样写 ExecTxResult 气。

## 官方三件事

1. **看见 ExecTxResult `codespace` 是码的命名空间 / 看见写了空间 / Finalize 这份码空间 is not already 已经是 CheckTx 回包那份码空间 interchangeable / 381 chktxspace interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 748 exectxgas-notcodespace interchangeable / 746 exectxgas-notwanted interchangeable / 393 exectxgas item 1 gas_wanted interchangeable，也不是已经 codespace not CheckTx codespace / not already response code / not already settled 正式三事 bundled（393 item 3 余量） interchangeable / 393 exectxgas item 3 interchangeable。**  
   官方写：`codespace` 是这个 `code` 的命名空间。看见写了空间，不是已经是 CheckTx 回包那份码空间 interchangeable——本页从 393 item 3 侧钉 not CheckTx codespace 单句。393 exectxgas vs checktx bundled unbundling 在本页 item 3 完成。

2. **看见写了空间 / 看见有命名空间 / Finalize 这份码空间 is not already 已经是回包码本身 interchangeable / 381 chktxspace interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 748 exectxgas-notcodespace interchangeable / 393 exectxgas item 2 gas_used interchangeable / 747 exectxgas-notused interchangeable。**  
   官方把命名空间和回包码本身分开——393 bundled 第三件事常与 381 混成「看见写了空间就已经是回包码 interchangeable」，本页钉 not already response code 单句。

3. **看见写了空间 / 看见能回 / Finalize 这份码空间 is not already 已经交差 interchangeable，也不是已经 ExecTxResult 气 bundled（393） interchangeable / 748 exectxgas-notcodespace interchangeable / 746 exectxgas-notwanted interchangeable。**  
   官方把能回 codespace 和已经交差分开。看见能回，不是已经交差 interchangeable。393 exectxgas vs checktx bundled unbundling 在本页 item 3 完成。

怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气是规范里的做法，本页不抄。

## 官方为什么这样拆

- **codespace not CheckTx codespace ≠ 381 interchangeable：** 官方把 Finalize 这份码空间和 CheckTx 那份码空间分开。
- **codespace not already response code ≠ 381 interchangeable：** 官方把有命名空间和回包码本身分开。
- **codespace not already settled ≠ 已经交差 interchangeable：** 官方把能回 codespace 和已经交差分开；393 exectxgas vs checktx bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExecTxResult.codespace 是码的命名空间 | 不是已经是 CheckTx 码空间（381） | 不是 gas_wanted（746/393 item 1） |
| 看见写了空间 | 不是已经是回包码（381） | 不是 ExecTxResult 气 bundled（393） |
| 看见能回 | 不是已经交差 | 不是 gas_used（747/393 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExecTxResult.codespace not CheckTx codespace / not already response code / not already settled 正式三事（393 余量），必须分开 codespace 是不是已经是 CheckTx 码空间 interchangeable / 381、是不是已经是回包码 interchangeable / 381、是不是已经交差。可以跳过「看见写了空间就已经是 CheckTx 码空间」。不要另写怎样写 ExecTxResult 气。393 exectxgas vs checktx bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExecTxResult 气、怎样填要的气、怎样填用掉的气。
- ExecTxResult 气 bundled。那是不变量 393。
- ExecTxResult.gas_wanted。那是不变量 393 item 1 余量 / 746。
- ExecTxResult.gas_used。那是不变量 393 item 2 余量 / 747。
- CheckTx 回包 codespace 就已经是回包码。那是不变量 381。
