# 例：看见 CheckTx source-from-user-or-peer is not already no-replay interchangeable / not already app-protected interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事（405 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事（405 余量）/ not 1104 cguard-notreplay interchangeable / not 405 checktxguard-vs-optional bundled interchangeable」，不是 CheckTx 守卫余量 bundled（405），也不是内存池去重就已经保证不重放（313），也不是 CheckTx 振荡就已经从池里删掉（328）。不要另写怎样写 CheckTx 守卫余量。

## 官方三件事

1. **看见这笔可以来自外部用户、也可以来自另一节点 / 看见送来了 这份栏 is not already 已经保证不重放 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1104 cguard-notreplay interchangeable / 1103 cguard-notopt interchangeable / 405 checktxguard item 1 guard-not-optional interchangeable，也不是已经 CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事 bundled（405 item 2 余量） interchangeable / 405 checktxguard item 2 interchangeable。**  
   官方写：这笔交易可以来自外部用户，也可以来自另一节点。看见送来了，不是已经保证不重放 interchangeable——本页从 405 item 2 侧钉 not already no-replay 单句。405 checktxguard vs optional bundled unbundling 在本页 item 2 续。

2. **看见能来自邻居 / 看见送来了 / 这份栏 is not already 已经过了 CheckTx 就有应用级保护 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1104 cguard-notreplay interchangeable / 405 checktxguard item 3 type-not-proof interchangeable / 1105 cguard-notproof interchangeable，也不是已经内存池去重就已经保证不重放 interchangeable / 313 replay interchangeable。**  
   官方把能来自邻居和已经过了 CheckTx 就有应用级保护分开。看见能来自邻居，不是已经过了 CheckTx 就有应用级保护 interchangeable。本页钉 not already app-protected 单句。

3. **看见能来自用户 / 看见送来了 / 这份栏 is not already 已经交差 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1104 cguard-notreplay interchangeable / 1103 cguard-notopt interchangeable，也不是已经 CheckTx 振荡就已经从池里删掉 interchangeable / 328 checktx-oscillate interchangeable。**  
   官方把能来自用户和已经交差分开。看见能来自用户，不是已经交差 interchangeable。405 checktxguard vs optional bundled unbundling 在本页 item 2 续。

怎样写 CheckTx 守卫余量、怎样挑邻居、怎样编 type 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **CheckTx source-from-user-or-peer not already no-replay ≠ 已经保证不重放 interchangeable：** 官方把送来的来源和已经保证不重放分开。
- **看见能来自邻居 not already app-protected ≠ 已经过了 CheckTx 就有应用级保护 interchangeable：** 官方把能来自邻居和已经过了 CheckTx 就有应用级保护分开。
- **看见能来自用户 not already settled ≠ 已经交差 interchangeable：** 官方把能来自用户和已经交差分开；405 checktxguard vs optional bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 这笔可以来自外部用户、也可以来自另一节点 | 不是已经保证不重放 | 不是内存池去重就已经保证不重放（313） |
| 看见能来自邻居 | 不是已经过了 CheckTx 就有应用级保护 | 不是 CheckTx 振荡就已经从池里删掉（328） |
| 看见能来自用户 | 不是已经交差 | 不是写了 type 就已经是 ProofOp 类型（1105） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx source-from-user-or-peer not already no-replay / not already app-protected / not already settled 正式三事（405 余量），必须分开是不是已经保证不重放、是不是已经过了 CheckTx 就有应用级保护、是不是已经交差。可以跳过「看见回了 CheckTx 守卫余量就已经是技术上可选」。不要另写怎样写 CheckTx 守卫余量。405 checktxguard vs optional bundled unbundling 在本页 item 2 续；续 [`worked-example-cguard-notproof-vs-bundled.md`](worked-example-cguard-notproof-vs-bundled.md)（不变量 1105 item 3）。

## 本页不抄

- 怎样写 CheckTx 守卫余量、怎样挑邻居、怎样编 type。
- CheckTx 守卫余量 bundled。那是不变量 405。
- 内存池去重就已经保证不重放。那是不变量 313。
- CheckTx 振荡就已经从池里删掉。那是不变量 328。
