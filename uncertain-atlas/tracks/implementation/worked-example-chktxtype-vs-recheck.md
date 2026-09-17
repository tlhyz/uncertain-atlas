# 例：看见 `CheckTx_New` 不是已经 `CheckTx_Recheck` / 已经从池里再验；看见 `CheckTx_Recheck` 不是已经外部新交易 / 已经 full check 交差；看见 Request `type` 栏 不是已经 `tx` 字节栏 / 已经 Commit 后再验 interchangeable

**层次**：实现 / CheckTx Request type 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`；[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState / RECHECK。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx_New 不是 Recheck / CheckTx_Recheck 不是外部新交易 / Request type 不是 tx 栏或 Commit 后再验 interchangeable」，不是 CheckTxState 与 ExecuteTxState bundled（312），也不是 CheckTx 请求 tx 栏 bundled（391）。不要另写怎样实现 CheckTxState、怎样再验。

## 官方三件事

规范把 CheckTx Request `type` 栏里 `CheckTx_New` / `CheckTx_Recheck` 和 app requirements 里 Commit 后再验时 `Type` 标明，写成三件独立的实现事，不是「看见填了 CheckTx 请求就已经是 Recheck、已经是新交易、已经永远有效」一件事：

1. **看见 `CheckTx_New` is the default and means that a full check of the transaction is required / 看见 CheckTx_New 是默认、要做完整验 不是已经 `CheckTx_Recheck` 那种内存池正常再验 interchangeable，也不是已经填了 `tx` 字节（391）就代表已经是 Recheck，也不是已经 CheckTx 过了就永远有效（301）。**  
   官方 Request 表写：`type` is One of `CheckTx_New` or `CheckTx_Recheck`。`CheckTx_New` is the default and means that a full check of the transaction is required。看见 default / full check，不是已经 `CheckTx_Recheck` 那种 mempool initiating a normal recheck interchangeable。看见 New，不是已经 CheckTx 请求 `tx` 是请求交易字节（391） bundled 第二句「不是已经是 Recheck」 interchangeable——391 钉 tx 栏，本页钉 type 栏。看见 full check required，不是已经提案收了就从池里删掉 / CheckTx 过了就永远有效（301） interchangeable。
2. **看见 `CheckTx_Recheck` types are used when the mempool is initiating a normal recheck of a transaction / 看见 CheckTx_Recheck 是内存池发起正常再验 不是已经外部用户 / 另一节点送来的新交易（405），也不是已经 `CheckTx_New` default full check interchangeable，也不是已经内存池去重就保证不重放（313）。**  
   官方 Request 表写：`CheckTx_Recheck` types are used when the mempool is initiating a normal recheck of a transaction。看见 initiating a normal recheck，不是已经外部新 tx 第一次进池那种 New interchangeable。看见 Recheck，不是已经 duplicate pool admission 就当成已经应用级重放保护（313） interchangeable。App requirements 写：`Commit` 返回之后会对本地池里剩下的再跑 CheckTx；`CheckTxRequest` 的 `Type` 标明 `CHECK_TX_TYPE_NEW` 与 `CHECK_TX_TYPE_RECHECK`（312）。看见 Recheck type，不是已经 Finalize When optionally recheck（468）就不需要读 `Type` interchangeable——468 钉 When 流程，本页钉 Request type 栏语义。
3. **看见 Request `type` 栏标明 New 还是 Recheck / 看见 Type 在 不是已经只看 `tx` 字节就知道是哪种调用，也不是已经 Commit 后再验（312 / 468）就不需要读 `type` interchangeable，也不是已经 CheckTx 请求余栏（391） bundled 就代表 type 已经验完。**  
   官方把 Request `type` 栏和 `tx` 栏分开写。看见有 type 字段，不是已经填了 tx 就等于已经知道 New vs Recheck。看见 Type 标明，不是已经 CheckTxState 与 ExecuteTxState（312） bundled 第三件事 interchangeable——312 钉 app requirements 流程，本页钉 Methods Request type 栏。看见 New / Recheck 枚举，不是已经 CheckTx 对照当前状态验、不应用改动（391 Usage bundled）就代表 type 已经交差 interchangeable。

怎样实现 CheckTxState、怎样再验、怎样区分 New/Recheck 是规范里的做法，本页不抄。CheckTxState 与 RECHECK 流程（312）是 app requirements 那套，CheckTx 请求 tx 栏（391）是 tx / Usage / info 那套，Finalize When recheck（468）是 lock mempool Commit recheck 那套，本页不抄。

## 官方为什么这样拆

- **CheckTx_New default full check ≠ CheckTx_Recheck / tx 栏就等于 Recheck：** 官方把 New 默认完整验和 Recheck 再验、tx 字节栏分开。
- **CheckTx_Recheck mempool normal recheck ≠ 外部新交易 / 去重保证不重放：** 官方把内存池发起再验和外部 admission、池去重分开。
- **Request type 栏 ≠ tx 栏 / Commit 后再验不需要读 Type：** 官方把 Methods Request type 和 tx 栏、When 流程 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx_New default full check | 不是 CheckTx_Recheck | 不是 CheckTx 请求 tx 栏（391） |
| CheckTx_Recheck mempool recheck | 不是外部新交易 | 不是内存池去重（313） |
| Request type 栏 | 不是 tx 栏就知道种类 | 不是 CheckTxState RECHECK 流程（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 CheckTx 请求就已经是 Recheck、已经是新交易、已经永远有效」，必须分开 CheckTx_New 是不是 CheckTx_Recheck / tx 栏就等于 Recheck、CheckTx_Recheck 是不是外部新交易 / 去重保证不重放、Request type 栏是不是 tx 栏或 Commit 后再验 interchangeable。可以跳过「看见填了 CheckTx 请求就已经是 Recheck」。不要另写怎样实现 CheckTxState。

## 本页不抄

- 怎样实现 CheckTxState、怎样再验、怎样填 type。
- CheckTxState 与 ExecuteTxState / RECHECK 流程。那是不变量 312。
- CheckTx 请求 tx 栏 / Usage / info。那是不变量 391。
- Finalize When lock mempool Commit recheck。那是不变量 468。
- 提案收了 / CheckTx 过了就永远有效。那是不变量 301。
- 内存池去重 / 应用级重放保护。那是不变量 313。
