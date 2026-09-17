# 例：看见 Request type field is not already tx field tells New vs Recheck interchangeable / not already Commit then recheck needs no type interchangeable / not already CheckTx request rest bundled interchangeable

**层次**：实现 / CheckTx Request type field not tx field tells New vs Recheck / not Commit then recheck needs no type / not CheckTx request rest bundled 正式三事（484 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState / RECHECK。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Request type field not tx field tells New vs Recheck / not Commit then recheck needs no type / not CheckTx request rest bundled 正式三事（484 余量）/ not 709 chktxtype-nottxfield interchangeable / not 484 chktxtype-vs-recheck bundled interchangeable」，不是 CheckTx Request type 正式三事 bundled（484），也不是 CheckTx 请求 tx 栏（391）或 CheckTxState RECHECK 流程（312）。不要另写怎样填 type。

## 官方三件事

1. **看见 Request `type` 栏标明 New 还是 Recheck / 看见 Type 在 / type field is not already 已经只看 `tx` 字节就知道是哪种调用 interchangeable / 391 checktxtx interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 709 chktxtype-nottxfield interchangeable / 707 chktxtype-notrecheck interchangeable / 484 chktxtype item 1 New interchangeable，也不是已经 Request type field not tx field tells New vs Recheck / not Commit then recheck needs no type / not CheckTx request rest bundled 正式三事 bundled（484 item 3 余量） interchangeable / 484 chktxtype item 3 interchangeable。**  
   官方把 Request type 栏和 tx 栏分开写。看见有 type 字段，不是已经填了 tx 就等于已经知道 New vs Recheck interchangeable——本页从 484 item 3 侧钉 not tx field tells New vs Recheck 单句。484 chktxtype vs recheck bundled unbundling 在本页 item 3 完成。

2. **看见 Type 标明 / 看见 Usage 这句 / type field is not already 已经 Commit 后再验（312 / 468）就不需要读 `type` interchangeable / 312 checktxstate interchangeable / 468 finrecheck interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 709 chktxtype-nottxfield interchangeable / 484 chktxtype item 2 Recheck interchangeable / 708 chktxtype-notsource interchangeable。**  
   官方把 Methods Request type 栏和 When / app requirements 再验流程分开——312/468 钉流程，本页钉 type 栏语义 not Commit then recheck needs no type 单句。

3. **看见 New / Recheck 枚举 / 看见 Usage 这句 / type field is not already 已经 CheckTx 请求余栏（391） bundled 就代表 type 已经验完 interchangeable / 391 checktxtx interchangeable，也不是已经 CheckTx Request type 正式三事 bundled（484） interchangeable / 709 chktxtype-nottxfield interchangeable / 707 chktxtype-notrecheck interchangeable。**  
   官方把 type 栏和请求余栏 bundled 分开。看见 Type 标明，不是已经 391 bundled 交差 interchangeable。484 chktxtype vs recheck bundled unbundling 在本页 item 3 完成。

怎样实现 CheckTxState、怎样再验、怎样填 type 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Request type field not tx field tells New vs Recheck ≠ 391 interchangeable：** 官方把 type 栏和 tx 栏分开。
- **Request type field not Commit then recheck needs no type ≠ 312 / 468 interchangeable：** 官方把 type 栏语义和 When / app requirements 再验流程分开。
- **Request type field not CheckTx request rest bundled ≠ 391 interchangeable：** 官方把 type 栏和请求余栏 bundled 分开；484 chktxtype vs recheck bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Request type 栏 | 不是 tx 栏就知道种类（391） | 不是 CheckTx_New（707/484 item 1） |
| 看见 Type 标明 | 不是 Commit 后再验不需要读 type（312 / 468） | 不是 Recheck mempool（708/484 item 2） |
| 看见 Usage 这句 | 不是 CheckTx 请求余栏 bundled（391） | 不是 CheckTx Request type bundled（484） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type field not tx field tells New vs Recheck / not Commit then recheck needs no type / not CheckTx request rest bundled 正式三事（484 余量），必须分开 type 栏是不是 tx 栏就知道种类 interchangeable / 391、是不是 Commit 后再验不需要读 type interchangeable / 312 / 468、是不是请求余栏 bundled interchangeable。可以跳过「看见填了 type 就已经交差」。不要另写怎样填 type。484 chktxtype vs recheck bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现 CheckTxState、怎样再验、怎样填 type。
- CheckTx Request type 正式三事 bundled。那是不变量 484。
- CheckTx_New default full check。那是不变量 484 item 1 余量 / 707。
- CheckTx_Recheck mempool normal recheck。那是不变量 484 item 2 余量 / 708。
- CheckTx 请求 tx 栏 / Usage / info。那是不变量 391。
- CheckTxState 与 ExecuteTxState / RECHECK 流程。那是不变量 312。
- Finalize When lock mempool Commit recheck。那是不变量 468。
