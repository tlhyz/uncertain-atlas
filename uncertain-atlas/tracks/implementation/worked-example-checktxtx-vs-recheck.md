# 例：看见 CheckTx 请求 tx 是请求交易字节不是已经是 Recheck；看见 CheckTx 对照当前状态验、不应用这笔描述的状态改动不是已经按 ExecuteTxState 验过；看见 CheckTx 回包 info 是附加信息不是已经是 Query 附加信息

**层次**：实现 / CheckTx 请求余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request / CheckTx Usage / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「CheckTx 请求 tx 是请求交易字节不是已经是 Recheck / CheckTx 对照当前状态验、不应用这笔描述的状态改动不是已经按 ExecuteTxState 验过 / CheckTx 回包 info 是附加信息不是已经是 Query 附加信息」，不是 CheckTxState 就已经是 ExecuteTxState，也不是 CheckTx 技术上可选、不参与处理块就已经是四门已经结算。不要另写怎样写 CheckTx 请求余栏。

## 官方三件事

规范把 CheckTx 请求 `tx` 是请求交易字节、CheckTx 对照当前状态验、不应用这笔描述的状态改动、CheckTx 回包 `info` 是附加信息写成三件独立的实现事，不是「看见填了 CheckTx 请求余栏就已经是 Recheck、已经按 ExecuteTxState 验过、已经是 Query 附加信息」一件事：

1. **看见 CheckTx 请求 `tx` 是请求交易字节 / 看见填了 tx 不是已经是 Recheck，也不是已经是四门已经结算。**  
   官方写：`tx` 是请求交易字节。看见填了 tx，不是已经是 `CheckTx_Recheck` 那种再验。看见有字节，不是已经是 CheckTx 技术上可选那种四门齐了。看见能填，不是已经交差。
2. **看见 CheckTx 对照当前状态验、不应用这笔描述的状态改动 / 看见验了 不是已经按 ExecuteTxState 验过，也不是已经参与处理块。**  
   官方写：CheckTx 对照应用当前状态验这笔交易，例如验签和余额，但不应用这笔描述的任何状态改动。看见验了，不是已经按将要执行的那份状态验过。看见对照当前状态，不是已经交差。看见没应用改动，不是已经参与处理块。
3. **看见 CheckTx 回包 `info` 是附加信息 / 看见回了信息 不是已经是 Query 附加信息，也不是已经是 CheckTx 日志。**  
   官方写：`info` 是附加信息。看见回了信息，不是已经是 Query 回包那份附加信息。看见有附加字段，不是已经是 CheckTx 回包那份日志。看见能回，不是已经交差。

怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息是规范里的做法，本页不抄。CheckTxState 就已经是 ExecuteTxState 是不变量 312，本页不抄。

## 官方为什么这样拆

- **CheckTx 请求 tx 是请求交易字节 ≠ 已经是 Recheck：** 官方把请求交易字节和再验类型分开。
- **CheckTx 对照当前状态验、不应用这笔描述的状态改动 ≠ 已经按 ExecuteTxState 验过：** 官方把对照当前状态验和不应用改动、按工作状态验分开。
- **CheckTx 回包 info 是附加信息 ≠ 已经是 Query 附加信息：** 官方把 CheckTx 这份附加信息和 Query 那份附加信息分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 请求 tx 是请求交易字节 | 不是已经是 Recheck | 不是 RECHECK 就已经是一笔新交易（312） |
| CheckTx 对照当前状态验、不应用这笔描述的状态改动 | 不是已经按 ExecuteTxState 验过 | 不是 CheckTx 技术上可选、不参与处理块就已经是四门已经结算（373） |
| CheckTx 回包 info 是附加信息 | 不是已经是 Query 附加信息 | 不是 Query 回包 info 就已经是按键查（384） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 CheckTx 请求余栏就已经是 Recheck、已经按 ExecuteTxState 验过、已经是 Query 附加信息」，必须分开 CheckTx 请求 tx 是请求交易字节是不是已经是 Recheck、CheckTx 对照当前状态验、不应用这笔描述的状态改动是不是已经按 ExecuteTxState 验过、CheckTx 回包 info 是附加信息是不是已经是 Query 附加信息。可以跳过「看见填了 CheckTx 请求余栏就已经是 Recheck」。不要另写怎样写 CheckTx 请求余栏。

## 本页不抄

- 怎样写 CheckTx 请求余栏、怎样填 tx、怎样填附加信息。
- CheckTxState 就已经是 ExecuteTxState。那是不变量 312。
- CheckTx 技术上可选、不参与处理块就已经是四门已经结算。那是不变量 373。
- Query 回包 info 就已经是按键查。那是不变量 384。
