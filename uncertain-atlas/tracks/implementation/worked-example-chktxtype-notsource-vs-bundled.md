# 例：看见 CheckTx_Recheck mempool normal recheck is not already external new transaction interchangeable / not already CheckTx_New default interchangeable / not already pool dedup means no replay interchangeable

**层次**：实现 / CheckTx Request type CheckTx_Recheck mempool normal recheck not external new transaction / not CheckTx_New default / not pool dedup means no replay 正式三事（484 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState / RECHECK。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Request type CheckTx_Recheck mempool normal recheck not external new transaction / not CheckTx_New default / not pool dedup means no replay 正式三事（484 余量）/ not 708 chktxtype-notsource interchangeable / not 484 chktxtype-vs-recheck bundled interchangeable」，不是 CheckTx Request type 正式三事 bundled（484），也不是外部新交易（405）或内存池去重（313）。不要另写怎样再验。

## 官方三件事

1. **看见 `CheckTx_Recheck` types are used when the mempool is initiating a normal recheck of a transaction / 看见 CheckTx_Recheck 是内存池发起正常再验 / Recheck is not already 已经外部用户 / 另一节点送来的新交易（405） interchangeable / 405 chktxsource interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 708 chktxtype-notsource interchangeable / 707 chktxtype-notrecheck interchangeable / 484 chktxtype item 1 New interchangeable，也不是已经 CheckTx_Recheck mempool normal recheck not external new transaction / not CheckTx_New default / not pool dedup means no replay 正式三事 bundled（484 item 2 余量） interchangeable / 484 chktxtype item 2 interchangeable。**  
   官方 Request 表写：CheckTx_Recheck types are used when the mempool is initiating a normal recheck of a transaction。看见 initiating a normal recheck，不是已经外部新交易 interchangeable——405 钉来源，本页从 484 item 2 侧钉 not external new 单句。484 chktxtype vs recheck bundled unbundling 在本页 item 2 续。

2. **看见 Recheck / 看见 mempool initiating / 看见 Usage 这句 is not already 已经 `CheckTx_New` default full check interchangeable / 707 chktxtype-notrecheck interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 708 chktxtype-notsource interchangeable / 484 chktxtype item 3 type field interchangeable / 709 chktxtype-nottxfield interchangeable。**  
   官方把 Recheck 再验和 New 默认完整验分开——484 bundled 第二件事常与第一件事混成「看见 Recheck 就已经是 New full check interchangeable」，本页钉 not CheckTx_New default 单句。

3. **看见 Recheck / 看见 Usage 这句 / mempool recheck is not already 已经内存池去重就保证不重放（313） interchangeable / 313 dedup interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 708 chktxtype-notsource interchangeable / 707 chktxtype-notrecheck interchangeable。**  
   官方把 Recheck 再验和内存池去重保证不重放分开。看见 Recheck type，不是已经应用级重放保护 interchangeable。484 chktxtype vs recheck bundled unbundling 在本页 item 2 续。

怎样实现 CheckTxState、怎样再验、怎样填 type 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **CheckTx_Recheck not external new transaction ≠ 405 interchangeable：** 官方把内存池发起再验和外部新交易分开。
- **CheckTx_Recheck not CheckTx_New default ≠ 484 item 1 interchangeable：** 官方把 Recheck 再验和 New 默认完整验分开。
- **CheckTx_Recheck not pool dedup means no replay ≠ 313 interchangeable：** 官方把 Recheck 和去重保证不重放分开；484 chktxtype vs recheck bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx_Recheck mempool recheck | 不是外部新交易（405） | 不是 CheckTx_New（707/484 item 1） |
| 看见 Recheck / mempool initiating | 不是 New default full check | 不是 Request type 栏（709/484 item 3） |
| 看见 Usage 这句 | 不是内存池去重保证不重放（313） | 不是 CheckTx Request type bundled（484） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type CheckTx_Recheck mempool normal recheck not external new transaction / not CheckTx_New default / not pool dedup means no replay 正式三事（484 余量），必须分开 Recheck 是不是外部新交易 interchangeable / 405、是不是 New default、是不是去重保证不重放 interchangeable / 313。可以跳过「看见 Recheck 就已经是新交易」。不要另写怎样再验。484 chktxtype vs recheck bundled unbundling 在本页 item 2 续；完成 [`worked-example-chktxtype-nottxfield-vs-bundled.md`](worked-example-chktxtype-nottxfield-vs-bundled.md)（不变量 709 item 3）。

## 本页不抄

- 怎样实现 CheckTxState、怎样再验、怎样填 type。
- CheckTx Request type 正式三事 bundled。那是不变量 484。
- CheckTx_New default full check。那是不变量 484 item 1 余量 / 707。
- Request type 栏。那是不变量 484 item 3 余量 / 709。
- CheckTx Usage tx source。那是不变量 405 / 488。
- 内存池去重。那是不变量 313。
