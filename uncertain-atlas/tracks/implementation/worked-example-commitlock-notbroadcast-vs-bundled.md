# 例：看见 Commit 里调了 broadcast_tx / 等回执 is not already already can proceed interchangeable / already settled interchangeable / already allowed sync mempool in Commit interchangeable

**层次**：实现 / Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事（310 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事（310 余量）/ not 691 commitlock-notbroadcast interchangeable / not 310 commitlock bundled interchangeable」，不是 Commit lock vs RPC bundled（310），也不是 default global lock not already RPC safe（689 item 1 余量）或 lock mempool before Commit not already unlocked（690 item 2 余量）。不要另写怎样调广播、怎样加锁、怎样写四门。

## 官方三件事

规范把 Requirements 里处理 `Commit` 时去发 `/broadcast_tx_sync` 或 `/broadcast_tx` 并等回执再往下走会**停死**、这些调用要拿内存池锁而 CometBFT 在 `Commit` 期间正握着这把锁、同步内存池相关调用不得写进 `Commit` 顺序逻辑 和「已经是能调广播就已经能往下走 interchangeable / 已经是等回执就已经交差 interchangeable / 已经是同步内存池调用就已经允许写进 Commit 顺序逻辑 interchangeable / 已经是 Commit lock vs RPC bundled interchangeable」分开写成三件独立的实现事，不是「看见能调广播 就已经能继续 interchangeable / 就已经交差 interchangeable / 就已经允许 interchangeable」一件事：

1. **看见 Commit 里调了 broadcast_tx / 看见能调广播 / 看见发了 `/broadcast_tx_sync` 或 `/broadcast_tx` is not already 已经能往下走 interchangeable / 已经 can proceed interchangeable / 已经能继续 interchangeable / 310 commitlock bundled interchangeable / 689 commitlock-notrpcsafe interchangeable / 690 commitlock-notunlocked interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 691 commitlock-notbroadcast interchangeable / 310 commitlock item 3 interchangeable，也不是已经 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事 bundled（310 item 3 余量） interchangeable / 310 commitlock item 3 interchangeable，也不是已经 default global lock not already RPC safe（689） interchangeable / 690 commitlock-notunlocked interchangeable / 588 finlock interchangeable，也不是已经广播已经发出 interchangeable / 已经交易已经进池 interchangeable。**  
   官方写警告：若处理 `Commit` 的逻辑去发 `/broadcast_tx_sync` 或 `/broadcast_tx`，并等回执再往下走，**会停死**。看见能调广播，不是已经能继续 interchangeable——310 钉 bundled 三事，本页从 item 3 侧钉 not already can proceed 单句。看见 Commit 里发了广播，不是已经广播已经发出 interchangeable——发出意图不是已经往下走。看见能调 `/broadcast_tx`，不是已经 Commit lock vs RPC bundled（310） interchangeable——310 钉 bundled，本页钉 item 3 第一件事。310 commitlock vs RPC bundled unbundling 在本页 item 3 启动。

2. **看见等回执 / 看见 waits for the response / 看见等 broadcast 回了再往下 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经 Finalize + Commit interchangeable / 310 commitlock bundled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 691 commitlock-notbroadcast interchangeable / 310 commitlock item 1 RPC safe interchangeable / 310 commitlock item 2 unlocked interchangeable，也不是已经 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事 bundled（310 item 3 余量） interchangeable / 310 commitlock item 3 interchangeable，也不是已经四门已经结算（33） interchangeable / 403 finafter interchangeable / 301 proposed-removed interchangeable。**  
   官方把等回执再往下走 和已经交差 / 已经能继续路径分开——等回执是停死路径上的一步，不等于已经交差，也不等于已经能往下走。看见等回执，不是已经交差 interchangeable——本页钉 not already settled 单句。看见 waits for the response，不是已经 default global lock not already RPC safe（689） interchangeable——689 另钉 item 1，本页钉 item 3 第二件事。看见等 broadcast 回了再往下，不是已经 lock mempool before Commit not already unlocked（690） interchangeable——690 另钉 item 2，本页钉 item 3 第二件事。310 commitlock vs RPC bundled unbundling 在本页 item 3 启动。

3. **看见同步内存池调用 / 看见 Synchronous mempool-related calls / 看见在 Commit 顺序逻辑里调广播 is not already 已经允许写进 Commit 顺序逻辑 interchangeable / 已经 allowed sync mempool in Commit interchangeable / 已经可以在 Commit 里等锁 interchangeable / 310 commitlock bundled interchangeable / 301 proposed-removed interchangeable / 690 commitlock-notunlocked interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 691 commitlock-notbroadcast interchangeable / 310 commitlock item 1 / 310 commitlock item 2，也不是已经 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事 bundled（310 item 3 余量） interchangeable / 310 commitlock item 3 interchangeable，也不是已经能调广播就已经允许 interchangeable / 已经等回执就已经交差 interchangeable。**  
   官方把 Synchronous mempool-related calls must be avoided as part of the sequential logic of the `Commit` function 和已经允许写进 Commit 顺序逻辑路径分开——警告是禁止，不是已经允许。看见同步内存池调用，不是已经允许 interchangeable——本页钉 not already allowed sync mempool in Commit 单句。看见在 Commit 顺序逻辑里调广播，不是已经 can proceed（本页第一件事） interchangeable——三件事分开钉。看见 Synchronous mempool-related calls，不是已经提案收了已经从池里删掉（301） interchangeable——301 另钉。310 commitlock vs RPC bundled unbundling 在本页 item 3 完成。

怎样调广播、怎样加锁、怎样写四门是规范里的做法，本页不抄。Commit lock vs RPC bundled（310）、default global lock not already RPC safe（310 item 1 余量 / 689）、lock mempool before Commit not already unlocked（310 item 2 余量 / 690）、一条连接已经是四门（307）、半写已经原子（5）、四门已经结算（33）、提案收了已经从池里删掉（301）是另外那套，本页不抄。

## 官方为什么这样拆

- **能调 broadcast_tx not already can proceed ≠ 310 / 689 / 690 interchangeable：** 官方把能调广播单句和已经能往下走路径分开。
- **等回执 not already settled ≠ 已经交差 interchangeable：** 官方把等回执单句和已经 Finalize + Commit / 四门已经结算路径分开。
- **同步内存池调用 not already allowed sync mempool in Commit ≠ 已经允许写进 Commit 顺序逻辑 interchangeable：** 官方把禁止单句和已经允许路径分开；310 commitlock vs RPC bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Commit 里调 broadcast_tx | 不是 already can proceed | 不是 default lock alone（689） |
| 等回执 | 不是 already settled | 不是四门已经结算（33） |
| 同步内存池调用 | 不是 already allowed sync mempool in Commit | 不是 Commit 前上锁 alone（690） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事（310 余量），必须分开能调广播 是不是 already can proceed interchangeable / 310 commitlock bundled interchangeable / 689 commitlock-notrpcsafe interchangeable、等回执 是不是 already settled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable、同步内存池调用 是不是 already allowed sync mempool in Commit interchangeable / 已经允许写进 Commit 顺序逻辑 interchangeable。可以跳过「看见能调广播 就已经能往下走 interchangeable / 就已经交差 interchangeable / 就已经允许 interchangeable」。不要另写怎样调广播。310 commitlock vs RPC bundled unbundling 在本页 item 3 完成（689 + 690 + 691）。

## 本页不抄

- 怎样调 `/broadcast_tx`、怎样加锁、怎样写四门。
- Commit lock vs RPC bundled。那是不变量 310。
- default global lock not already RPC safe。那是不变量 310 item 1 余量 / 689。
- lock mempool before Commit not already unlocked。那是不变量 310 item 2 余量 / 690。
- 一条连接已经是四门。那是不变量 307。
- 半写已经原子。那是不变量 5。
- 四门已经结算。那是不变量 33。
- 提案收了已经从池里删掉。那是不变量 301。
