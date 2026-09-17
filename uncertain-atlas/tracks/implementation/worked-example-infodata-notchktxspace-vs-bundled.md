# 例：看见 Query 回包 codespace 是码的命名空间 is not already CheckTx codespace interchangeable / not already response code interchangeable / not already settled interchangeable

**层次**：实现 / Query 回包 codespace not already CheckTx codespace / not already response code / not already settled 正式三事（389 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回包 codespace not already CheckTx codespace / not already response code / not already settled 正式三事（389 余量）/ not 763 infodata-notchktxspace interchangeable / not 389 infodata-vs-appversion bundled interchangeable」，不是 Info 回包余栏 bundled（389），也不是 CheckTx 回包 codespace 就已经是回包码（381），也不是 ExecTxResult.codespace 就已经是 CheckTx 码空间（393/748）。不要另写怎样写 Info 回包余栏。

## 官方三件事

1. **看见 Query 回包 `codespace` 是码的命名空间 / 看见写了空间 / Query 这份码空间 is not already 已经是 CheckTx 回包那份码空间 interchangeable / 381 chktxspace interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 763 infodata-notchktxspace interchangeable / 761 infodata-nothandshake interchangeable / 389 infodata item 1 data interchangeable，也不是已经 codespace not already CheckTx codespace / not already response code / not already settled 正式三事 bundled（389 item 3 余量） interchangeable / 389 infodata item 3 interchangeable。**  
   官方写：`codespace` 是这个 `code` 的命名空间。看见写了空间，不是已经是 CheckTx 回包那份码空间 interchangeable——本页从 389 item 3 侧钉 not already CheckTx codespace 单句。389 infodata vs appversion bundled unbundling 在本页 item 3 完成。

2. **看见写了空间 / 看见有命名空间 / Query 这份码空间 is not already 已经是 Query 回包码本身 interchangeable / 381 chktxspace interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 763 infodata-notchktxspace interchangeable / 389 infodata item 2 version interchangeable / 762 infodata-notappversion interchangeable，也不是已经 ExecTxResult.codespace 就已经是 CheckTx 码空间 interchangeable / 393 exectxgas / 748 exectxgas-notcodespace interchangeable。**  
   官方把 Query 这份码空间和回包码本身分开——389 bundled 第三件事常与 381 / 393 混成「看见写了空间就已经是 CheckTx 码空间或已经是回包码 interchangeable」，本页钉 not already response code 单句。

3. **看见写了空间 / 看见能回 / Query 这份码空间 is not already 已经交差 interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 763 infodata-notchktxspace interchangeable / 761 infodata-nothandshake interchangeable。**  
   官方把能回 Query 回包 codespace 和已经交差分开。看见能回，不是已经交差 interchangeable。389 infodata vs appversion bundled unbundling 在本页 item 3 完成。

怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本是规范里的做法，本页不抄。

## 官方为什么这样拆

- **codespace not already CheckTx codespace ≠ 381 interchangeable：** 官方把 Query 这份码空间和 CheckTx 那份码空间分开。
- **codespace not already response code ≠ 381 interchangeable：** 官方把有命名空间和回包码本身分开。
- **codespace not already settled ≠ 已经交差 interchangeable：** 官方把能回 codespace 和已经交差分开；389 infodata vs appversion bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 codespace 是码的命名空间 | 不是已经是 CheckTx 码空间（381） | 不是 Info 回包 data（761/389 item 1） |
| 看见写了空间 | 不是已经是回包码（381） | 不是 ExecTxResult.codespace（393/748） |
| 看见能回 | 不是已经交差 | 不是 Info 回包余栏 bundled（389） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 codespace not already CheckTx codespace / not already response code / not already settled 正式三事（389 余量），必须分开 codespace 是不是已经是 CheckTx 码空间 interchangeable / 381、是不是已经是回包码 interchangeable / 381、是不是已经交差。可以跳过「看见写了空间就已经是 CheckTx 码空间」。不要另写怎样写 Info 回包余栏。389 infodata vs appversion bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本。
- Info 回包余栏 bundled。那是不变量 389。
- Info 回包 data。那是不变量 389 item 1 余量 / 761。
- Info 回包 version。那是不变量 389 item 2 余量 / 762。
- CheckTx 回包 codespace 就已经是回包码。那是不变量 381。
- ExecTxResult.codespace 就已经是 CheckTx 码空间。那是不变量 393 / 748。
