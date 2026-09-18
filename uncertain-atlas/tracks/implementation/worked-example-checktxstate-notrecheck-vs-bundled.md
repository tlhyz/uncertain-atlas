# 例：看见 Commit 之后又跑了 CheckTx / Type 是 RECHECK is not already already new transaction interchangeable / already treated as NEW interchangeable / already unlocked interchangeable

**层次**：实现 / RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事（312 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事（312 余量）/ not 697 checktxstate-notrecheck interchangeable / not 312 checktxstate bundled interchangeable」，不是 CheckTxState vs ExecuteTxState bundled（312），也不是 CheckTx 过了不是已经按 ExecuteTxState 验过（695 item 1 余量）或同时在改不是已经同一份（696 item 2 余量）。不要另写怎样再验或怎样加锁。

## 官方三件事

规范把 Requirements 里 `Commit` 返回之后**还握着内存池锁**、对本地池里剩下的已经滤掉本块交易的那些再跑一遍 CheckTx、`CheckTxRequest` 的 `Type` 标明这是新交易（`CHECK_TX_TYPE_NEW`）还是再验（`CHECK_TX_TYPE_RECHECK`）、再验完才解锁新交易才能再走 CheckTx 和「已经是又跑了就已经是新交易 interchangeable / 已经是 Type 在就已经当 NEW 处理 interchangeable / 已经是 Commit 回了就已经放下锁 interchangeable / 已经是 CheckTxState vs ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见又跑了 就已经是新交易 interchangeable / 就已经当 NEW 处理 interchangeable / 就已经解锁 interchangeable」一件事：

1. **看见 Commit 之后又跑了 CheckTx / 看见又跑了 / 看见对本地池里剩下的再验 is not already 已经是一笔新交易 interchangeable / 已经 new transaction interchangeable / 已经是 NEW interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 697 checktxstate-notrecheck interchangeable / 312 checktxstate item 3 interchangeable，也不是已经 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事 bundled（312 item 3 余量） interchangeable / 312 checktxstate item 3 interchangeable，也不是已经 CheckTx 过了不是已经按 ExecuteTxState 验过（695） interchangeable / 696 checktxstate-notsame interchangeable / 310 commitlock interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`Commit` 返回之后，还握着内存池锁，会对本地池里剩下的、已经滤掉本块交易的那些，再跑一遍 CheckTx。看见又跑了，不是已经是新交易 interchangeable——312 钉 bundled 三事，本页从 item 3 侧钉 not already new transaction 单句。看见对本地池里剩下的再验，不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable——312 钉 bundled，本页钉 item 3 第一件事。看见 Commit 之后又跑了 CheckTx，不是已经 CheckTx 过了不是已经按 ExecuteTxState 验过（695） interchangeable——695 另钉 item 1，本页钉 item 3 第一件事。312 checktxstate vs execute bundled unbundling 在本页 item 3 启动。

2. **看见 Type 是 RECHECK / 看见 Type 在 / 看见 CheckTxRequest.Type 标明再验 is not already 已经当 NEW 处理 interchangeable / 已经 treated as NEW interchangeable / 已经 CHECK_TX_TYPE_NEW interchangeable / 312 checktxstate bundled interchangeable / 301 proposed-removed interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 697 checktxstate-notrecheck interchangeable / 312 checktxstate item 1 CheckTx 过了 interchangeable / 312 checktxstate item 2 同时在改 interchangeable，也不是已经 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事 bundled（312 item 3 余量） interchangeable / 312 checktxstate item 3 interchangeable，也不是已经是新交易（本页第一件事） interchangeable。**  
   官方把 `Type` 标明 `CHECK_TX_TYPE_NEW` 与 `CHECK_TX_TYPE_RECHECK` 和 Type 在就已经当 NEW 处理路径分开——看见 Type 在，不是已经当 NEW 处理。看见 Type 是 RECHECK，不是已经当 NEW 处理 interchangeable——本页钉 not already treated as NEW 单句。看见 Type 在，不是已经 CheckTx 过了不是已经按 ExecuteTxState 验过（695） interchangeable——695 另钉 item 1，本页钉 item 3 第二件事。看见 CheckTxRequest.Type 标明再验，不是已经同时在改不是已经同一份（696） interchangeable——696 另钉 item 2，本页钉 item 3 第二件事。312 checktxstate vs execute bundled unbundling 在本页 item 3 启动。

3. **看见 Commit 回了 / 看见 Commit 返回 / 看见应用 Commit 绿了 is not already 已经放下锁 interchangeable / 已经 unlocked interchangeable / 已经内存池锁已经放开 interchangeable / 312 checktxstate bundled interchangeable / 310 commitlock interchangeable / 690 commitlock-notunlocked interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 697 checktxstate-notrecheck interchangeable / 312 checktxstate item 1 / 312 checktxstate item 2，也不是已经 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事 bundled（312 item 3 余量） interchangeable / 312 checktxstate item 3 interchangeable，也不是已经是新交易（本页第一件事） interchangeable / 已经当 NEW 处理（本页第二件事） interchangeable。**  
   官方把 `Commit` 返回之后还握着内存池锁、再验完才解锁 和 Commit 回了就已经放下锁路径分开——Commit 返回不等于锁已经放下；再验完才解锁，新交易才能再走 CheckTx。看见 Commit 回了，不是已经放下锁 interchangeable——本页钉 not already unlocked 单句。看见 Commit 绿了，不是已经是新交易（本页第一件事） interchangeable——三件事分开钉。看见应用 Commit 返回，不是已经 Commit lock vs RPC unlocked（690） interchangeable——690 另钉 Commit 前上锁侧，本页钉 RECHECK 期间还握着锁。312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。

怎样再验、怎样加锁、怎样写四门是规范里的做法，本页不抄。CheckTxState vs ExecuteTxState bundled（312）、CheckTx 过了不是已经按 ExecuteTxState 验过（312 item 1 余量 / 695）、同时在改不是已经同一份（312 item 2 余量 / 696）、Commit 前上锁不是已经解锁（310 / 690）、提案收了已经从池里删掉（301）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **又跑了 not already new transaction ≠ 312 / 33 interchangeable：** 官方把再验单句和已经是新交易路径分开。
- **Type 是 RECHECK not already treated as NEW ≠ 已经当 NEW 处理 interchangeable：** 官方把 Type 标明再验单句和已经当 NEW 处理路径分开。
- **Commit 回了 not already unlocked ≠ 已经放下锁 interchangeable：** 官方把 Commit 返回还握着锁单句和已经解锁路径分开；312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Commit 之后又跑了 CheckTx | 不是 already new transaction | 不是 CheckTx 过了 alone（695） |
| Type 是 RECHECK | 不是 already treated as NEW | 不是同时在改 alone（696） |
| Commit 回了 | 不是 already unlocked | 不是 Commit 前上锁 alone（690） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事（312 余量），必须分开又跑了 是不是 already new transaction interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable、Type 是 RECHECK 是不是 already treated as NEW interchangeable、Commit 回了 是不是 already unlocked interchangeable / 310 commitlock interchangeable / 690 commitlock-notunlocked interchangeable。可以跳过「看见又跑了 就已经是新交易 interchangeable / 就已经当 NEW 处理 interchangeable / 就已经解锁 interchangeable」。不要另写怎样再验。312 checktxstate vs execute bundled unbundling 在本页 item 3 完成（695 + 696 + 697）。

## 本页不抄

- 怎样再验、怎样加锁、怎样写四门。
- CheckTxState vs ExecuteTxState bundled。那是不变量 312。
- CheckTx 过了不是已经按 ExecuteTxState 验过。那是不变量 312 item 1 余量 / 695。
- 同时在改不是已经同一份。那是不变量 312 item 2 余量 / 696。
- Commit 前上锁不是已经解锁。那是不变量 310 / 690。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
