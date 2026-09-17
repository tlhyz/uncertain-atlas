# 例：看见 CheckTx_New default full check is not already CheckTx_Recheck interchangeable / not already tx field means Recheck interchangeable / not already CheckTx forever valid interchangeable

**层次**：实现 / CheckTx Request type CheckTx_New default full check not CheckTx_Recheck / not tx field means Recheck / not CheckTx forever valid 正式三事（484 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState / RECHECK。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Request type CheckTx_New default full check not CheckTx_Recheck / not tx field means Recheck / not CheckTx forever valid 正式三事（484 余量）/ not 707 chktxtype-notrecheck interchangeable / not 484 chktxtype-vs-recheck bundled interchangeable」，不是 CheckTx Request type 正式三事 bundled（484），也不是 CheckTx 请求 tx 栏（391）或 CheckTx 过了就永远有效（301）。不要另写怎样实现 CheckTxState。

## 官方三件事

1. **看见 `CheckTx_New` is the default and means that a full check of the transaction is required / 看见 CheckTx_New 是默认、要做完整验 / New is not already 已经 `CheckTx_Recheck` 那种内存池正常再验 interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 707 chktxtype-notrecheck interchangeable / 708 chktxtype-notsource interchangeable / 484 chktxtype item 2 Recheck interchangeable，也不是已经 CheckTx_New default full check not CheckTx_Recheck / not tx field means Recheck / not CheckTx forever valid 正式三事 bundled（484 item 1 余量） interchangeable / 484 chktxtype item 1 interchangeable。**  
   官方 Request 表写：CheckTx_New is the default and means that a full check of the transaction is required。看见 default / full check，不是已经 CheckTx_Recheck interchangeable——本页从 484 item 1 侧钉 not Recheck 单句。484 chktxtype vs recheck bundled unbundling 在本页 item 1 启动。

2. **看见 New / 看见 default full check / 看见 Usage 这句 is not already 已经 CheckTx 请求 `tx` 是请求交易字节（391）就代表已经是 Recheck interchangeable / 391 checktxtx interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 707 chktxtype-notrecheck interchangeable / 484 chktxtype item 3 type field interchangeable / 709 chktxtype-nottxfield interchangeable。**  
   官方把 Request type 栏 New 单句和 tx 栏就等于 Recheck 分开——391 钉 tx 栏，本页钉 type 栏 not tx field means Recheck 单句。

3. **看见 full check required / 看见 Usage 这句 / New is not already 已经 CheckTx 过了就永远有效（301） interchangeable / 301 forever interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 707 chktxtype-notrecheck interchangeable / 708 chktxtype-notsource interchangeable。**  
   官方把 New 完整验和 CheckTx 过了就永远有效分开。看见 full check required，不是已经永远有效 interchangeable。484 chktxtype vs recheck bundled unbundling 在本页 item 1 启动。

怎样实现 CheckTxState、怎样再验、怎样填 type 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **CheckTx_New not CheckTx_Recheck ≠ Recheck interchangeable：** 官方把 New 默认完整验和 Recheck 再验分开。
- **CheckTx_New not tx field means Recheck ≠ 391 interchangeable：** 官方把 type 栏 New 和 tx 栏就等于 Recheck 分开。
- **CheckTx_New not CheckTx forever valid ≠ 301 interchangeable：** 官方把 full check required 和过了就永远有效分开；484 chktxtype vs recheck bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx_New default full check | 不是 CheckTx_Recheck | 不是 Recheck mempool（708/484 item 2） |
| 看见 New / default full check | 不是 tx 栏就等于 Recheck（391） | 不是 CheckTx Request type bundled（484） |
| 看见 Usage 这句 | 不是 CheckTx 过了就永远有效（301） | 不是 Request type 栏（709/484 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type CheckTx_New default full check not CheckTx_Recheck / not tx field means Recheck / not CheckTx forever valid 正式三事（484 余量），必须分开 New 是不是 Recheck、是不是 tx 栏就等于 Recheck interchangeable / 391、是不是过了就永远有效 interchangeable / 301。可以跳过「看见填了 New 就已经是 Recheck」。不要另写怎样实现 CheckTxState。484 chktxtype vs recheck bundled unbundling 在本页 item 1 启动；续 [`worked-example-chktxtype-notsource-vs-bundled.md`](worked-example-chktxtype-notsource-vs-bundled.md)（不变量 708 item 2）。

## 本页不抄

- 怎样实现 CheckTxState、怎样再验、怎样填 type。
- CheckTx Request type 正式三事 bundled。那是不变量 484。
- CheckTx_Recheck mempool normal recheck。那是不变量 484 item 2 余量 / 708。
- Request type 栏。那是不变量 484 item 3 余量 / 709。
- CheckTx 请求 tx 栏。那是不变量 391。
- CheckTx 过了就永远有效。那是不变量 301。
