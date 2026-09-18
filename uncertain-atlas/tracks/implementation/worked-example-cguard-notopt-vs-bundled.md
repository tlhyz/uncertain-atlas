# 例：看见 CheckTx mempool-guard is not already technically-optional interchangeable / not already four-gates interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事（405 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事（405 余量）/ not 1103 cguard-notopt interchangeable / not 405 checktxguard-vs-optional bundled interchangeable」，不是 CheckTx 守卫余量 bundled（405），也不是 CheckTx 技术上可选、不参与处理块就已经是四门已经结算（373），也不是 CheckTx 弱守卫就已经交差（339）。不要另写怎样写 CheckTx 守卫余量。

## 官方三件事

1. **看见 CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池 / 看见先跑了 这份栏 is not already 已经是技术上可选 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1103 cguard-notopt interchangeable / 1104 cguard-notreplay interchangeable / 405 checktxguard item 2 source-not-replay interchangeable，也不是已经 CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事 bundled（405 item 1 余量） interchangeable / 405 checktxguard item 1 interchangeable。**  
   官方写：CheckTx 是内存池的守卫；每条节点在让一笔交易进自己本地池之前，都先跑 CheckTx。看见先跑了，不是已经是技术上可选 interchangeable——本页从 405 item 1 侧钉 not already technically-optional 单句。405 checktxguard vs optional bundled unbundling 在本页 item 1 启动。

2. **看见守着本地池 / 看见先跑了 / 这份栏 is not already 已经是四门已经结算 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1103 cguard-notopt interchangeable / 405 checktxguard item 3 type-not-proof interchangeable / 1105 cguard-notproof interchangeable，也不是已经 CheckTx 技术上可选、不参与处理块就已经是四门已经结算 interchangeable / 373 checktx-optional interchangeable。**  
   官方把守着本地池和已经是四门已经结算分开。看见守着本地池，不是已经是四门已经结算 interchangeable。本页钉 not already four-gates 单句。

3. **看见每条节点都跑 / 看见先跑了 / 这份栏 is not already 已经交差 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1103 cguard-notopt interchangeable / 1104 cguard-notreplay interchangeable，也不是已经 CheckTx 弱守卫就已经交差 interchangeable / 339 checktx-weak interchangeable。**  
   官方把每条节点都跑和已经交差分开。看见每条节点都跑，不是已经交差 interchangeable。405 checktxguard vs optional bundled unbundling 在本页 item 1 启动。

怎样写 CheckTx 守卫余量、怎样挑邻居、怎样编 type 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **CheckTx mempool-guard not already technically-optional ≠ 已经是技术上可选 interchangeable：** 官方把本地池入口守卫和技术上可选分开。
- **看见守着本地池 not already four-gates ≠ 已经是四门已经结算 interchangeable：** 官方把守着本地池和已经是四门已经结算分开。
- **看见每条节点都跑 not already settled ≠ 已经交差 interchangeable：** 官方把每条节点都跑和已经交差分开；405 checktxguard vs optional bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 是内存池的守卫、每条节点先跑 CheckTx 才让交易进本地池 | 不是已经是技术上可选 | 不是 CheckTx 技术上可选、不参与处理块就已经是四门已经结算（373） |
| 看见守着本地池 | 不是已经是四门已经结算 | 不是 CheckTx 弱守卫就已经交差（339） |
| 看见每条节点都跑 | 不是已经交差 | 不是送来了就已经保证不重放（1104） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事（405 余量），必须分开是不是已经是技术上可选、是不是已经是四门已经结算、是不是已经交差。可以跳过「看见回了 CheckTx 守卫余量就已经是技术上可选」。不要另写怎样写 CheckTx 守卫余量。405 checktxguard vs optional bundled unbundling 在本页 item 1 启动；续 [`worked-example-cguard-notreplay-vs-bundled.md`](worked-example-cguard-notreplay-vs-bundled.md)（不变量 1104 item 2）。

## 本页不抄

- 怎样写 CheckTx 守卫余量、怎样挑邻居、怎样编 type。
- CheckTx 守卫余量 bundled。那是不变量 405。
- CheckTx 技术上可选、不参与处理块就已经是四门已经结算。那是不变量 373。
- CheckTx 弱守卫就已经交差。那是不变量 339。
