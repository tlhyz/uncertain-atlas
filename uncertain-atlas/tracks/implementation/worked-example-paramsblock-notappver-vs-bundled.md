# 例：看见 ConsensusParams.version 是 ABCI 应用版本 is not already app_version in header interchangeable / not already header AppHash interchangeable / not already settled interchangeable

**层次**：实现 / ConsensusParams.version not already app_version in header / not already header AppHash / not already settled 正式三事（385 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ConsensusParams。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ConsensusParams.version not already app_version in header / not already header AppHash / not already settled 正式三事（385 余量）/ not 775 paramsblock-notappver interchangeable / not 385 paramsblock-vs-maxbytes bundled interchangeable」，不是 ConsensusParams 字段 bundled（385），也不是 app_version 进每块头就已经印进本头 AppHash（370），也不是 Info 回包 version 就已经是 app_version（389/762）。不要另写怎样写 ConsensusParams 字段。

## 官方三件事

1. **看见 ConsensusParams.`version` 是 ABCI 应用版本 / 看见填了 version / ConsensusParams 这份应用版本 is not already 已经是 Info 回包 `app_version` 进了每块头 interchangeable / 370 appver interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 775 paramsblock-notappver interchangeable / 773 paramsblock-notmaxbytes interchangeable / 385 paramsblock item 1 block interchangeable，也不是已经 version not already app_version in header / not already header AppHash / not already settled 正式三事 bundled（385 item 3 余量） interchangeable / 385 paramsblock item 3 interchangeable。**  
   官方写：`version` 是 ABCI 应用版本。看见填了 version，不是已经是 Info 回包 `app_version` 进了每块头 interchangeable——本页从 385 item 3 侧钉 not already app_version in header 单句。385 paramsblock vs maxbytes bundled unbundling 在本页 item 3 完成。

2. **看见填了 version / 看见有应用版本 / ConsensusParams 这份应用版本 is not already 已经印进本头 AppHash interchangeable / 370 appver interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 775 paramsblock-notappver interchangeable / 385 paramsblock item 2 validator interchangeable / 774 paramsblock-notpubkey interchangeable，也不是已经 Info 回包 version 就已经是 app_version interchangeable / 389 infodata / 762 infodata-notappversion interchangeable。**  
   官方把这一栏和已经印进本头 AppHash 分开——385 bundled 第三件事常与 370 / 389 混成「看见填了 version 就已经是 app_version 进了头或已经印进本头 AppHash interchangeable」，本页钉 not already header AppHash 单句。

3. **看见填了 version / 看见能回 / ConsensusParams 这份应用版本 is not already 已经是握手对齐 interchangeable，也不是已经 ConsensusParams 字段 bundled（385） interchangeable / 775 paramsblock-notappver interchangeable / 773 paramsblock-notmaxbytes interchangeable。**  
   官方把能回 ConsensusParams.version 和已经是握手对齐分开。看见能回，不是已经是握手对齐 interchangeable。385 paramsblock vs maxbytes bundled unbundling 在本页 item 3 完成。

怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型是规范里的做法，本页不抄。

## 官方为什么这样拆

- **version not already app_version in header ≠ 370 interchangeable：** 官方把这一栏和 Info 回的 app_version 进头分开。
- **version not already header AppHash ≠ 370 interchangeable：** 官方把有应用版本和已经印进本头 AppHash 分开。
- **version not already settled ≠ 已经是握手对齐 interchangeable：** 官方把能回 version 和已经是握手对齐分开；385 paramsblock vs maxbytes bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ConsensusParams.version 是 ABCI 应用版本 | 不是已经是 app_version 进了头（370） | 不是 ConsensusParams.block（773/385 item 1） |
| 看见填了 version | 不是已经印进本头 AppHash（370） | 不是 Info 回包 version（389/762） |
| 看见能回 | 不是已经是握手对齐 | 不是 ConsensusParams 字段 bundled（385） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ConsensusParams.version not already app_version in header / not already header AppHash / not already settled 正式三事（385 余量），必须分开 version 是不是已经是 app_version 进了头 interchangeable / 370、是不是已经印进本头 AppHash、是不是已经是握手对齐。可以跳过「看见填了 version 就已经是 app_version 进了头」。不要另写怎样写 ConsensusParams 字段。385 paramsblock vs maxbytes bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ConsensusParams、怎样选 MaxBytes、怎样限钥型。
- ConsensusParams 字段 bundled。那是不变量 385。
- ConsensusParams.block。那是不变量 385 item 1 余量 / 773。
- ConsensusParams.validator。那是不变量 385 item 2 余量 / 774。
- app_version 进每块头就已经印进本头 AppHash。那是不变量 370。
- Info 回包 version 就已经是 app_version。那是不变量 389 / 762。
