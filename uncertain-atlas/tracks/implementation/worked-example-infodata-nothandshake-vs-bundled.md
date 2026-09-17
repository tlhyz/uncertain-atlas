# 例：看见 Info 回包 data 是任意信息 is not already handshake interchangeable / not already snapshot replay interchangeable / not already settled interchangeable

**层次**：实现 / Info 回包 data not already handshake / not already snapshot replay / not already settled 正式三事（389 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Response / Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info 回包 data not already handshake / not already snapshot replay / not already settled 正式三事（389 余量）/ not 761 infodata-nothandshake interchangeable / not 389 infodata-vs-appversion bundled interchangeable」，不是 Info 回包余栏 bundled（389），也不是 Info 用来握手对齐就已经是快照重放（370）。不要另写怎样写 Info 回包余栏。

## 官方三件事

1. **看见 Info 回包 `data` 是任意信息 / 看见回了 data / Info 这份任意字段 is not already 已经握手对齐 interchangeable / 370 handshake interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 761 infodata-nothandshake interchangeable / 762 infodata-notappversion interchangeable / 389 infodata item 2 version interchangeable，也不是已经 data not already handshake / not already snapshot replay / not already settled 正式三事 bundled（389 item 1 余量） interchangeable / 389 infodata item 1 interchangeable。**  
   官方写：`data` 是一些任意信息。看见回了 data，不是已经握手对齐 interchangeable——本页从 389 item 1 侧钉 not already handshake 单句。389 infodata vs appversion bundled unbundling 在本页 item 1 启动。

2. **看见回了 data / 看见有任意字段 / Info 这份任意字段 is not already 已经是快照重放 interchangeable / 370 handshake interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 761 infodata-nothandshake interchangeable / 389 infodata item 3 codespace interchangeable / 763 infodata-notchktxspace interchangeable。**  
   官方把回包里的任意信息和已经是快照重放分开——389 bundled 第一件事常与 370 混成「看见回了 data 就已经握手对齐或已经是快照重放 interchangeable」，本页钉 not already snapshot replay 单句。

3. **看见回了 data / 看见能填 / Info 这份任意字段 is not already 已经交差 interchangeable，也不是已经 Info 回包余栏 bundled（389） interchangeable / 761 infodata-nothandshake interchangeable / 762 infodata-notappversion interchangeable。**  
   官方把能填 Info 回包 data 和已经交差分开。看见能填，不是已经交差 interchangeable。389 infodata vs appversion bundled unbundling 在本页 item 1 启动。

怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本是规范里的做法，本页不抄。

## 官方为什么这样拆

- **data not already handshake ≠ 370 interchangeable：** 官方把回包里的任意信息和握手对齐分开。
- **data not already snapshot replay ≠ 370 interchangeable：** 官方把有任意字段和已经是快照重放分开。
- **data not already settled ≠ 已经交差 interchangeable：** 官方把能填 data 和已经交差分开；389 infodata vs appversion bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 回包 data 是任意信息 | 不是已经是握手对齐（370） | 不是 Info 回包 version（762/389 item 2） |
| 看见回了 data | 不是已经是快照重放（370） | 不是 Info 回包余栏 bundled（389） |
| 看见能填 | 不是已经交差 | 不是 Query codespace（763/389 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 回包 data not already handshake / not already snapshot replay / not already settled 正式三事（389 余量），必须分开 data 是不是已经握手对齐 interchangeable / 370、是不是已经是快照重放 interchangeable / 370、是不是已经交差。可以跳过「看见回了 data 就已经是握手对齐」。不要另写怎样写 Info 回包余栏。389 infodata vs appversion bundled unbundling 在本页 item 1 启动；续 [`worked-example-infodata-notappversion-vs-bundled.md`](worked-example-infodata-notappversion-vs-bundled.md)（不变量 762 item 2）。

## 本页不抄

- 怎样写 Info 回包余栏、怎样填任意信息、怎样填应用版本。
- Info 回包余栏 bundled。那是不变量 389。
- Info 回包 version。那是不变量 389 item 2 余量 / 762。
- Query 回包 codespace。那是不变量 389 item 3 余量 / 763。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
