# 例：看见 CheckTxState 和 ExecuteTxState 同时在改 / 两条连接都在说话 is not already already same state interchangeable / already merged interchangeable / already shared working state interchangeable

**层次**：实现 / 同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事（312 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事（312 余量）/ not 696 checktxstate-notsame interchangeable / not 312 checktxstate bundled interchangeable」，不是 CheckTxState vs ExecuteTxState bundled（312），也不是 CheckTx 过了不是已经按 ExecuteTxState 验过（695 item 1 余量）或 RECHECK 不是已经是新交易（697 item 3 余量）。不要另写怎样实现两份状态或怎样再验。

## 官方三件事

规范把 Requirements 里共识实例进行当中 *CheckTxState* 可以和 *ExecuteTxState* **同时更新**、因为共识连接和内存池连接上的消息可以并发 和「已经是两边都在改就已经同一份 interchangeable / 已经是并发就已经合并 interchangeable / 已经是都叫 CheckTx / Finalize 就已经共用一份工作状态 interchangeable / 已经是 CheckTxState vs ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见同时在改 就已经同一份 interchangeable / 就已经合并 interchangeable / 就已经共用一份 interchangeable」一件事：

1. **看见 CheckTxState 和 ExecuteTxState 同时在改 / 看见两边都在改 / 看见 may be updated concurrently is not already 已经同一份状态 interchangeable / 已经 same state interchangeable / 已经一份状态 interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 696 checktxstate-notsame interchangeable / 312 checktxstate item 2 interchangeable，也不是已经同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事 bundled（312 item 2 余量） interchangeable / 312 checktxstate item 2 interchangeable，也不是已经 CheckTx 过了不是已经按 ExecuteTxState 验过（695） interchangeable / 697 checktxstate-notrecheck interchangeable / 310 commitlock interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：共识实例进行当中，*CheckTxState* 可以和 *ExecuteTxState* **同时更新**。看见两边都在改，不是已经同一份 interchangeable——312 钉 bundled 三事，本页从 item 2 侧钉 not already same state 单句。看见同时在改，不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable——312 钉 bundled，本页钉 item 2 第一件事。看见 may be updated concurrently，不是已经 CheckTx 过了不是已经按 ExecuteTxState 验过（695） interchangeable——695 另钉 item 1，本页钉 item 2 第一件事。312 checktxstate vs execute bundled unbundling 在本页 item 2 启动。

2. **看见共识和内存池两条连接都在说话 / 看见消息可以并发 / 看见两条连接并发 is not already 已经合并 interchangeable / 已经 merged interchangeable / 已经并成一份 interchangeable / 312 checktxstate bundled interchangeable / 307 conn interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 696 checktxstate-notsame interchangeable / 312 checktxstate item 1 CheckTx 过了 interchangeable / 312 checktxstate item 3 RECHECK interchangeable，也不是已经同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事 bundled（312 item 2 余量） interchangeable / 312 checktxstate item 2 interchangeable，也不是已经同一份（本页第一件事） interchangeable。**  
   官方把共识连接和内存池连接上的消息可以并发 和已经合并路径分开——并发更新两份，不等于已经并成一份。看见两条连接都在说话，不是已经合并 interchangeable——本页钉 not already merged 单句。看见消息可以并发，不是已经 CheckTx 过了不是已经按 ExecuteTxState 验过（695） interchangeable——695 另钉 item 1，本页钉 item 2 第二件事。看见两条连接并发，不是已经 RECHECK 不是已经是新交易（697） interchangeable——697 另钉 item 3，本页钉 item 2 第二件事。312 checktxstate vs execute bundled unbundling 在本页 item 2 启动。

3. **看见都叫 CheckTx / Finalize / 看见两边都在处理交易相关调用 / 看见共识和内存池都在动 is not already 已经共用一份工作状态 interchangeable / 已经 shared working state interchangeable / 已经共用 ExecuteTxState interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable / 311 candidate interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 696 checktxstate-notsame interchangeable / 312 checktxstate item 1 / 312 checktxstate item 3，也不是已经同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事 bundled（312 item 2 余量） interchangeable / 312 checktxstate item 2 interchangeable，也不是已经同一份（本页第一件事） interchangeable / 已经合并（本页第二件事） interchangeable。**  
   官方把两边都在说话 和已经共用一份工作状态路径分开——都叫 CheckTx / Finalize 不等于已经共用 ExecuteTxState。看见都叫 CheckTx / Finalize，不是已经共用一份工作状态 interchangeable——本页钉 not already shared working state 单句。看见两边都在处理交易相关调用，不是已经同一份（本页第一件事） interchangeable——三件事分开钉。看见共识和内存池都在动，不是已经候选已经是 ExecuteTxState（311） interchangeable——311 另钉。312 checktxstate vs execute bundled unbundling 在本页 item 2 完成。

怎样实现两份状态、怎样再验、怎样写四门是规范里的做法，本页不抄。CheckTxState vs ExecuteTxState bundled（312）、CheckTx 过了不是已经按 ExecuteTxState 验过（312 item 1 余量 / 695）、RECHECK 不是已经是新交易（312 item 3 余量 / 697）、候选已经是 ExecuteTxState（311）、默认锁已经 RPC 安全（310）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **两边都在改 not already same state ≠ 312 / 33 interchangeable：** 官方把同时更新单句和已经同一份路径分开。
- **两条连接并发 not already merged ≠ 已经并成一份 interchangeable：** 官方把可以并发单句和已经合并路径分开。
- **都叫 CheckTx / Finalize not already shared working state ≠ 已经共用 ExecuteTxState interchangeable：** 官方把两边都在动单句和已经共用一份工作状态路径分开；312 checktxstate vs execute bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 两边都在改 | 不是 already same state | 不是 CheckTx 过了 alone（695） |
| 两条连接并发 | 不是 already merged | 不是 RECHECK alone（697） |
| 都叫 CheckTx / Finalize | 不是 already shared working state | 不是候选 already ExecuteTxState（311） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同时在改不是已经同一份 not already same state / not already merged / not already shared working state 正式三事（312 余量），必须分开两边都在改 是不是 already same state interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable、两条连接并发 是不是 already merged interchangeable、都叫 CheckTx / Finalize 是不是 already shared working state interchangeable。可以跳过「看见同时在改 就已经同一份 interchangeable / 就已经合并 interchangeable / 就已经共用一份 interchangeable」。不要另写怎样实现两份状态。312 checktxstate vs execute bundled unbundling 在本页 item 2 完成；续 [`worked-example-checktxstate-notrecheck-vs-bundled.md`](worked-example-checktxstate-notrecheck-vs-bundled.md)（不变量 697 item 3）。

## 本页不抄

- 怎样实现两份状态、怎样再验、怎样写四门。
- CheckTxState vs ExecuteTxState bundled。那是不变量 312。
- CheckTx 过了不是已经按 ExecuteTxState 验过。那是不变量 312 item 1 余量 / 695。
- RECHECK 不是已经是新交易。那是不变量 312 item 3 余量 / 697。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 默认锁已经 RPC 安全。那是不变量 310。
- 四门已经结算。那是不变量 33。
