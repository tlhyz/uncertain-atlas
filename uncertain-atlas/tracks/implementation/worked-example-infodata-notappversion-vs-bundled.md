# 例：看见 Info 回包 version 是应用软件语义版本 is not already app_version interchangeable / not already header AppHash interchangeable / not already settled interchangeable

**层次**：实现 / Info 回包 version not already app_version / not already header AppHash / not already settled 正式三事（389 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info 回包 version not already app_version / not already header AppHash / not already settled 正式三事（389 余量）/ not 762 infodata-notappversion interchangeable / not 389 infodata-vs-appversion bundled interchangeable」，不是 Info 回包余栏 bundled（389），也不是 Info 请求 version 就已经是 app_version（379）。不要另写怎样写 Info 回包余栏。

## 官方三件事

1. **看见 Info 回包 `version` 是应用软件语义版本 / 看见回了应用版本 / Info 这份语义版本 is not already 已经是回包里的 `app_version` interchangeable / 379 infover interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 762 infodata-notappversion interchangeable / 761 infodata-nothandshake interchangeable / 389 infodata item 1 data interchangeable，也不是已经 version not already app_version / not already header AppHash / not already settled 正式三事 bundled（389 item 2 余量） interchangeable / 389 infodata item 2 interchangeable。**  
   官方写：`version` 是应用软件的语义版本。看见回了应用版本，不是已经是回包里的 `app_version` interchangeable——本页从 389 item 2 侧钉 not already app_version 单句。389 infodata vs appversion bundled unbundling 在本页 item 2 续。

2. **看见回了应用版本 / 看见有语义版本 / Info 这份语义版本 is not already 已经印进每块头 interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 762 infodata-notappversion interchangeable / 389 infodata item 3 codespace interchangeable / 763 infodata-notchktxspace interchangeable。**  
   官方把应用软件语义版本和已经印进每块头分开——389 bundled 第二件事常与 379 混成「看见回了 version 就已经是 app_version 或已经印进本头 interchangeable」，本页钉 not already header AppHash 单句。

3. **看见回了应用版本 / 看见能回 / Info 这份语义版本 is not already 已经交差 interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 762 infodata-notappversion interchangeable / 761 infodata-nothandshake interchangeable。**  
   官方把能回 Info 回包 version 和已经交差分开。看见能回，不是已经交差 interchangeable。389 infodata vs appversion bundled unbundling 在本页 item 2 续。

怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本是规范里的做法，本页不抄。

## 官方为什么这样拆

- **version not already app_version ≠ 379 interchangeable：** 官方把应用软件语义版本和会进每块头的 app_version 分开。
- **version not already header AppHash ≠ 已经印进本头 interchangeable：** 官方把有语义版本和已经印进每块头分开。
- **version not already settled ≠ 已经交差 interchangeable：** 官方把能回 version 和已经交差分开；389 infodata vs appversion bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 回包 version 是应用软件语义版本 | 不是已经是 app_version（379） | 不是 Info 回包 data（761/389 item 1） |
| 看见回了应用版本 | 不是已经印进本头 | 不是 Info 回包余栏 bundled（389） |
| 看见能回 | 不是已经交差 | 不是 Query codespace（763/389 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 回包 version not already app_version / not already header AppHash / not already settled 正式三事（389 余量），必须分开 version 是不是已经是 app_version interchangeable / 379、是不是已经印进本头、是不是已经交差。可以跳过「看见回了 version 就已经是 app_version」。不要另写怎样写 Info 回包余栏。389 infodata vs appversion bundled unbundling 在本页 item 2 续；完成 [`worked-example-infodata-notchktxspace-vs-bundled.md`](worked-example-infodata-notchktxspace-vs-bundled.md)（不变量 763 item 3）。

## 本页不抄

- 怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本。
- Info 回包余栏 bundled。那是不变量 389。
- Info 回包 data。那是不变量 389 item 1 余量 / 761。
- Query 回包 codespace。那是不变量 389 item 3 余量 / 763。
- Info 请求 version 就已经是 app_version。那是不变量 379。
