# 例：看见 CheckTx 过了不是已经按 ExecuteTxState 验过；看见两份状态同时在改不是已经同一份；看见 RECHECK 不是已经是一笔新交易

**层次**：实现 / CheckTxState。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「CheckTxState 不是已经是 ExecuteTxState / 同时在改不是已经同一份 / RECHECK 不是已经是新交易」，不是候选已经是工作状态，也不是提案收了已经从池里删掉。不要另写怎样实现 CheckTx 或怎样再验。

## 官方三件事

规范把内存池连接上的 CheckTxState 写成三件独立的实现事，不是「看见 CheckTx 过了就已经按将要执行的那份状态验过、已经同一份、已经是新交易」一件事：

1. **看见 CheckTx 过了 / 看见进了池并开始流言 不是已经按 ExecuteTxState 验过，也不是已经按将要执行的那份状态验过。**  
   官方写：内存池连接维持一份 *CheckTxState*。进来的交易按这份状态顺序验。没报错才进池，CometBFT 才开始流言。*CheckTxState* 应在每次 `Commit` 结束时重置成最新已提交状态。官方还写：CheckTx 只是弱过滤器，不能保证验的就是以后作为（可能的）决定块去执行时那一份状态。看见过了，不是已经按工作状态验。看见进了池，不是已经按将要执行的那份验。看见重置了，不是已经和 ExecuteTxState 同一份。
2. **看见 CheckTxState 和 ExecuteTxState 同时在改 / 看见共识和内存池两条连接都在说话 不是已经同一份状态。**  
   官方写：共识实例进行当中，*CheckTxState* 可以和 *ExecuteTxState* **同时更新**，因为共识连接和内存池连接上的消息可以并发。看见两边都在改，不是已经同一份。看见并发，不是已经合并。看见都叫 CheckTx / Finalize，不是已经共用一份工作状态。
3. **看见 Commit 之后又跑了 CheckTx / 看见 Type 是 RECHECK 不是已经是一笔新交易，也不是已经解锁。**  
   官方写：`Commit` 返回之后，**还握着内存池锁**，会对本地池里剩下的、已经滤掉本块交易的那些，再跑一遍 CheckTx。`CheckTxRequest` 的 `Type` 标明这是新交易（`CHECK_TX_TYPE_NEW`）还是再验（`CHECK_TX_TYPE_RECHECK`）。再验完才解锁，新交易才能再走 CheckTx。看见又跑了，不是已经是新交易。看见 Type 在，不是已经当 NEW 处理。看见 Commit 回了，不是锁已经放下。

怎样实现两份状态、怎样再验、索引器去重是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **CheckTx 过了 ≠ 已经按 ExecuteTxState 验过：** 官方把 CheckTxState、最新已提交、将要执行的那份分开。
- **同时在改 ≠ 已经同一份：** 官方把两条连接上可以并发更新写成两份状态。
- **RECHECK ≠ 已经是新交易：** 官方把 Commit 之后还握着锁再验，和新交易进来分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTxState | 不是已经按 ExecuteTxState 验过 | 不是候选已经是 ExecuteTxState（311） |
| 两份状态同时在改 | 不是已经同一份 | 不是默认锁已经 RPC 安全（310） |
| RECHECK | 不是已经是新交易，也不是已经解锁 | 不是提案收了已经从池里删掉（301） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「CheckTx 已经过了」，必须分开 CheckTxState 是不是已经按 ExecuteTxState 验过、两份状态是不是已经同一份、RECHECK 是不是已经是新交易。可以跳过「看见过了就已经按将要执行的那份验过」。不要另写怎样实现 CheckTx 或怎样再验。312 checktxstate vs execute bundled unbundling 完成（695 + 696 + 697）；精读 [`worked-example-checktxstate-notexecute-vs-bundled.md`](worked-example-checktxstate-notexecute-vs-bundled.md)（不变量 695 item 1）；[`worked-example-checktxstate-notsame-vs-bundled.md`](worked-example-checktxstate-notsame-vs-bundled.md)（不变量 696 item 2）；[`worked-example-checktxstate-notrecheck-vs-bundled.md`](worked-example-checktxstate-notrecheck-vs-bundled.md)（不变量 697 item 3）。

## 本页不抄

- 怎样实现 CheckTxState、怎样再验、索引器去重。
- 怎样写四门。那是不变量 33。
- Replay 保护公式。那是另一对象。
