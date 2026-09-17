# 例：看见 CheckTx 回包 codespace 是码的命名空间 is not already response code interchangeable / not already not-in-block interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx 回包 codespace not already response code / not already not-in-block / not already settled 正式三事（381 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 回包 codespace not already response code / not already not-in-block / not already settled 正式三事（381 余量）/ not 785 checktxspace-notcode interchangeable / not 381 checktxspace-vs-code bundled interchangeable」，不是 CheckTx 回包 bundled（381），也不是引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373），也不是 ExecTxResult.codespace 就已经是 CheckTx 码空间（393/748）。不要另写怎样写 CheckTx 回包。

## 官方三件事

1. **看见 CheckTx 回包 `codespace` 是码的命名空间 / 看见写了空间 / CheckTx 这份码空间 is not already 已经是回包码本身 interchangeable / 373 chktxcode interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 785 checktxspace-notcode interchangeable / 786 checktxspace-notsettled interchangeable / 381 checktxspace item 2 events interchangeable，也不是已经 codespace not already response code / not already not-in-block / not already settled 正式三事 bundled（381 item 1 余量） interchangeable / 381 checktxspace item 1 interchangeable。**  
   官方写：`codespace` 是这个 `code` 的命名空间。看见写了空间，不是已经是回包码本身 interchangeable——本页从 381 item 1 侧钉 not already response code 单句。381 checktxspace vs code bundled unbundling 在本页 item 1 启动。

2. **看见写了空间 / 看见有命名空间 / CheckTx 这份码空间 is not already 已经没进块 interchangeable / 373 chktxcode interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 785 checktxspace-notcode interchangeable / 381 checktxspace item 3 lane_id interchangeable / 787 checktxspace-notlane interchangeable，也不是已经 ExecTxResult.codespace 就已经是 CheckTx 码空间 interchangeable / 393 exectxgas / 748 exectxgas-notcodespace interchangeable。**  
   官方把有命名空间和已经没进块分开——381 bundled 第一件事常与 373 / 393 混成「看见写了空间就已经是回包码或已经没进块 interchangeable」，本页钉 not already not-in-block 单句。

3. **看见写了空间 / 看见能回 / CheckTx 这份码空间 is not already 已经交差 interchangeable，也不是已经 CheckTx 回包 bundled（381） interchangeable / 785 checktxspace-notcode interchangeable / 786 checktxspace-notsettled interchangeable。**  
   官方把能回 codespace 和已经交差分开。看见能回，不是已经交差 interchangeable。381 checktxspace vs code bundled unbundling 在本页 item 1 启动。

怎样写 CheckTx 回包、怎样填码空间、怎样选道是规范里的做法，本页不抄。

## 官方为什么这样拆

- **codespace not already response code ≠ 373 interchangeable：** 官方把码的命名空间和回包码本身分开。
- **codespace not already not-in-block ≠ 已经没进块 interchangeable：** 官方把有命名空间和已经没进块分开。
- **codespace not already settled ≠ 已经交差 interchangeable：** 官方把能回 codespace 和已经交差分开；381 checktxspace vs code bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 回包 codespace 是码的命名空间 | 不是已经是回包码（373） | 不是 CheckTx 回包 events（786/381 item 2） |
| 看见写了空间 | 不是已经没进块 | 不是 CheckTx 回包 bundled（381） |
| 看见能回 | 不是已经交差 | 不是 ExecTxResult.codespace（393/748） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 codespace not already response code / not already not-in-block / not already settled 正式三事（381 余量），必须分开 codespace 是不是已经是回包码 interchangeable / 373、是不是已经没进块、是不是已经交差。可以跳过「看见写了空间就已经是回包码」。不要另写怎样写 CheckTx 回包。381 checktxspace vs code bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktxspace-notsettled-vs-bundled.md`](worked-example-checktxspace-notsettled-vs-bundled.md)（不变量 786 item 2）。

## 本页不抄

- 怎样写 CheckTx 回包、怎样填码空间、怎样选道。
- CheckTx 回包 bundled。那是不变量 381。
- CheckTx 回包 events。那是不变量 381 item 2 余量 / 786。
- CheckTx 的 lane_id。那是不变量 381 item 3 余量 / 787。
- 引擎对回包码不再赋予别的含义就已经被引擎用了 Data。那是不变量 373。
- ExecTxResult.codespace 就已经是 CheckTx 码空间。那是不变量 393 / 748。
