# 例：看见 Info 用来握手对齐 is not already snapshot replay interchangeable / not already QueryState interchangeable / not already settled interchangeable

**层次**：实现 / Info 握手 not already snapshot replay / not already QueryState / not already settled 正式三事（370 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info 握手 not already snapshot replay / not already QueryState / not already settled 正式三事（370 余量）/ not 815 info-notreplay interchangeable / not 370 info-vs-handshake bundled interchangeable」，不是 Info 握手 bundled（370），也不是 QueryState 就已经是 ExecuteTxState（314），也不是 Info Usage 握手就已经是 370 bundled（494/669），也不是 Info 回包 data 就已经是握手（389/761），也不是 Info 请求 abci_version 就已经是握手（379/793）。不要另写怎样写 Info 握手。

## 官方三件事

1. **看见 Info 用来在启动或恢复时让引擎和应用握手对齐 / 看见能回 / 这份握手 is not already 已经是快照重放 interchangeable / 314 querystate interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 815 info-notreplay interchangeable / 816 info-notapphash interchangeable / 370 info item 2 app_version interchangeable，也不是已经 Info 握手 not already snapshot replay / not already QueryState / not already settled 正式三事 bundled（370 item 1 余量） interchangeable / 370 info item 1 interchangeable。**  
   官方写：Info 用来回报应用状态。启动或恢复时，CometBFT 用这次握手和应用对齐。看见能回，不是已经是快照重放 interchangeable——本页从 370 item 1 侧钉 not already snapshot replay 单句。370 info vs handshake bundled unbundling 在本页 item 1 启动。

2. **看见能回 / 看见握手了 / 这份握手 is not already 已经是 QueryState interchangeable / 314 querystate interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 815 info-notreplay interchangeable / 370 info item 3 last_block interchangeable / 817 info-notpersist interchangeable，也不是已经 Info Usage 握手就已经是 370 bundled interchangeable / 494 infousage / 669 infousage-nothandshake interchangeable，也不是已经 Info 回包 data 就已经是握手 interchangeable / 389 infodata / 761 infodata-nothandshake interchangeable。**  
   官方把握手了和已经是 QueryState 分开——370 bundled 第一件事常与 314 / 494 / 389 混成「看见能回 Info 就已经是快照重放或已经是 QueryState interchangeable」，本页钉 not already QueryState 单句。

3. **看见能回 / 看见对齐了 / 这份握手 is not already 已经交差 interchangeable，也不是已经 Info 握手 bundled（370） interchangeable / 815 info-notreplay interchangeable / 816 info-notapphash interchangeable，也不是已经 Info 请求 abci_version 就已经是握手 interchangeable / 379 infover / 793 infover-nothandshake interchangeable。**  
   官方把对齐了和已经交差分开。看见对齐了，不是已经交差 interchangeable。370 info vs handshake bundled unbundling 在本页 item 1 启动。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Info 握手 not already snapshot replay ≠ 314 interchangeable：** 官方把握手对齐和快照重放分开。
- **看见握手了 not already QueryState ≠ 已经是 QueryState interchangeable：** 官方把握手了和已经是 QueryState 分开。
- **看见对齐了 not already settled ≠ 已经交差 interchangeable：** 官方把对齐了和已经交差分开；370 info vs handshake bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 用来握手对齐 | 不是已经是快照重放（314） | 不是 app_version 进头（816/370 item 2） |
| 看见握手了 | 不是已经是 QueryState | 不是 Info Usage 握手（494/669） |
| 看见对齐了 | 不是已经交差 | 不是 Info 回包 data（389/761） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 握手 not already snapshot replay / not already QueryState / not already settled 正式三事（370 余量），必须分开是不是已经是快照重放 interchangeable / 314、是不是已经是 QueryState、是不是已经交差。可以跳过「看见能回 Info 就已经是快照重放」。不要另写怎样写 Info 握手。370 info vs handshake bundled unbundling 在本页 item 1 启动；续 [`worked-example-info-notapphash-vs-bundled.md`](worked-example-info-notapphash-vs-bundled.md)（不变量 816 item 2）。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Info 握手 bundled。那是不变量 370。
- app_version 进每块头。那是不变量 370 item 2 余量 / 816。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- Info Usage 握手就已经是 370 bundled。那是不变量 494 / 669。
