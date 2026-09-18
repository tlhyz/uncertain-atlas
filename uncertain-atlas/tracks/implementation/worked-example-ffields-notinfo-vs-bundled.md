# 例：看见 Info app-state-info is not already handshake-aligned interchangeable / not already snapshot-replay interchangeable / not already settled interchangeable

**层次**：实现 / Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事（407 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事（407 余量）/ not 1111 ffields-notinfo interchangeable / not 407 finfields-vs-equiv bundled interchangeable」，不是 Finalize 字段余量 bundled（407），也不是 Info 用来握手对齐就已经是快照重放（370），也不是 Info 车道就已经交差（367）。不要另写怎样写 Finalize 字段余量。

## 官方三件事

1. **看见 Info 用来回应用状态信息 / 看见能回 这份栏 is not already 已经是握手对齐 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1111 ffields-notinfo interchangeable / 1109 ffields-notfour interchangeable / 407 finfields item 1 fields-not-four interchangeable，也不是已经 Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事 bundled（407 item 3 余量） interchangeable / 407 finfields item 3 interchangeable。**  
   官方写：Info 用来回应用状态信息。看见能回信息，不是已经是握手对齐 interchangeable——本页从 407 item 3 侧钉 not already handshake-aligned 单句。407 finfields vs equiv bundled unbundling 在本页 item 3 完成。

2. **看见写了应用状态 / 看见能回 / 这份栏 is not already 已经是快照重放 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1111 ffields-notinfo interchangeable / 407 finfields item 2 must-det interchangeable / 1110 ffields-notprep interchangeable，也不是已经 Info 用来握手对齐就已经是快照重放 interchangeable / 370 info-handshake interchangeable。**  
   官方把写了应用状态和已经是快照重放分开。看见写了应用状态，不是已经是快照重放 interchangeable。本页钉 not already snapshot-replay 单句。

3. **看见能查 / 看见能回 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1111 ffields-notinfo interchangeable / 1109 ffields-notfour interchangeable，也不是已经 Info 车道就已经交差 interchangeable / 367 info-lane interchangeable。**  
   官方把能查和已经交差分开。看见能查，不是已经交差 interchangeable。407 finfields vs equiv bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Info app-state-info not already handshake-aligned ≠ 已经是握手对齐 interchangeable：** 官方把回应用状态信息和握手对齐分开。
- **看见写了应用状态 not already snapshot-replay ≠ 已经是快照重放 interchangeable：** 官方把写了应用状态和已经是快照重放分开。
- **看见能查 not already settled ≠ 已经交差 interchangeable：** 官方把能查和已经交差分开；407 finfields vs equiv bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 用来回应用状态信息 | 不是已经是握手对齐 | 不是 Info 用来握手对齐就已经是快照重放（370） |
| 看见写了应用状态 | 不是已经是快照重放 | 不是 Info 车道就已经交差（367） |
| 看见能查 | 不是已经交差 | 不是填了字段就已经是四门已经结算（1109） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info app-state-info not already handshake-aligned / not already snapshot-replay / not already settled 正式三事（407 余量），必须分开是不是已经是握手对齐、是不是已经是快照重放、是不是已经交差。可以跳过「看见填了 Finalize 字段余量就已经是四门已经结算」。不要另写怎样写 Finalize 字段余量。407 finfields vs equiv bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info。
- Finalize 字段余量 bundled。那是不变量 407。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- Info 车道就已经交差。那是不变量 367。
