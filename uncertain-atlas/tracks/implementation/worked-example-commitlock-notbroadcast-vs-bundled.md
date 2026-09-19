# 例：看见 Commit 里调了 broadcast_tx 并等回执 is not already already can proceed interchangeable / receipt already settled interchangeable / sync call already allowed interchangeable

**层次**：实现 / Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事（310 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事（310 余量）/ not 691 commitlock-notbroadcast interchangeable / not 310 commitlock bundled interchangeable」，不是 Commit lock vs RPC bundled（310），也不是 default global lock not already RPC safe（689 item 1 余量）或 Commit 前上锁不是已经解锁（690 item 2 余量）。不要另写怎样调广播、怎样加锁、怎样写四门。

## 官方三件事

规范把 Requirements 里处理 `Commit` 的逻辑去发 `/broadcast_tx_sync` 或 `/broadcast_tx` 并等回执再往下走**会停死**（这些调用要拿内存池锁，而 CometBFT 在 `Commit` 期间正握着这把锁）和「已经是能调广播就已经能往下走 interchangeable / 已经是等回执就已经交差 interchangeable / 已经是同步内存池调用就已经允许写进 Commit 顺序逻辑 interchangeable / 已经是 Commit lock vs RPC bundled interchangeable」分开写成三件独立的实现事，不是「看见能调广播 就已经能继续 interchangeable / 就已经交差 interchangeable / 就已经允许写进顺序逻辑 interchangeable」一件事：

1. **看见 Commit 里调了 broadcast_tx / 看见能调广播 / 看见发了 /broadcast_tx_sync is not already 已经能往下走 interchangeable / 已经能继续 interchangeable / 已经 can proceed interchangeable / 310 commitlock bundled interchangeable / 690 commitlock-notunlocked interchangeable / 301 proposed-removed interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 691 commitlock-notbroadcast interchangeable / 310 commitlock item 3 interchangeable，也不是已经 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事 bundled（310 item 3 余量） interchangeable / 310 commitlock item 3 interchangeable，也不是已经 default global lock not already RPC safe（689） interchangeable / 588 finlock interchangeable / 5 half-write atomic interchangeable，也不是已经提案收了已经从池里删掉（301） interchangeable / proposed-sold-as-removed interchangeable。**  
   官方写警告：若处理 `Commit` 的逻辑去发 `/broadcast_tx_sync` 或 `/broadcast_tx`，并等回执再往下走，**会停死**。看见能调广播，不是已经能继续 interchangeable——310 钉 bundled 三事，本页从 item 3 侧钉 not already can proceed 单句。看见发了广播，不是已经提案收了已经从池里删掉（301） interchangeable——301 钉提案 vs 删池，本页钉 Commit 里等广播单句。看见 Commit 里调了 broadcast_tx，不是已经 Commit lock vs RPC bundled（310） interchangeable——310 钉 bundled，本页钉 item 3 第一件事。310 commitlock vs RPC bundled unbundling 在本页 item 3 启动。

2. **看见等回执 / 看见等 broadcast_tx 回执再往下走 / 看见同步等回执 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经 receipt already settled interchangeable / 310 commitlock bundled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 691 commitlock-notbroadcast interchangeable / 310 commitlock item 1 RPC safe interchangeable / 310 commitlock item 2 unlocked interchangeable，也不是已经 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事 bundled（310 item 3 余量） interchangeable / 310 commitlock item 3 interchangeable，也不是已经四门已经结算（33） interchangeable / 632 notsettled interchangeable / 已经停死就已经交差 interchangeable。**  
   官方把等回执再往下走会停死 和等回执就已经交差路径分开——回执还没来、或者根本等不到，不等于这一步已经交差。看见等回执，不是已经交差 interchangeable——本页钉 not receipt already settled 单句。看见同步等回执，不是已经 default global lock not already RPC safe（689） interchangeable——689 另钉 item 1，本页钉 item 3 第二件事。看见等回执再往下走，不是已经 Commit 前上锁不是已经解锁（690） interchangeable——690 另钉 item 2，本页钉 item 3 第二件事。310 commitlock vs RPC bundled unbundling 在本页 item 3 启动。

3. **看见同步内存池调用 / 看见把 broadcast_tx 写进 Commit 顺序逻辑 / 看见 Commit 期间要拿内存池锁 is not already 已经允许写进 Commit 顺序逻辑 interchangeable / 已经 sync call already allowed interchangeable / 已经能在 Commit 里等锁 interchangeable / 310 commitlock bundled interchangeable / 690 commitlock-notunlocked interchangeable / 588 finlock interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 691 commitlock-notbroadcast interchangeable / 310 commitlock item 1 / 310 commitlock item 2，也不是已经 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事 bundled（310 item 3 余量） interchangeable / 310 commitlock item 3 interchangeable，也不是已经内存池锁已经放下 interchangeable / 已经能往下走（本页第一件事） interchangeable。**  
   官方把这些调用要拿内存池锁、而 CometBFT 在 `Commit` 期间正握着这把锁 和同步内存池调用已经允许写进 `Commit` 顺序逻辑路径分开——锁还在手里，不等于这一类调用已经允许写进顺序逻辑。看见同步内存池调用，不是已经允许写进顺序逻辑 interchangeable——本页钉 not sync call already allowed 单句。看见要拿内存池锁，不是已经解锁（690） interchangeable——690 钉放下锁，本页钉 item 3 第三件事。看见写进 Commit 顺序逻辑，不是已经能往下走（本页第一件事） interchangeable——三件事分开钉。310 commitlock vs RPC bundled unbundling 在本页 item 3 完成。

怎样调广播、怎样加锁、怎样写四门是规范里的做法，本页不抄。Commit lock vs RPC bundled（310）、default global lock not already RPC safe（310 item 1 余量 / 689）、Commit 前上锁不是已经解锁（310 item 2 余量 / 690）、提案收了已经从池里删掉（301）、Finalize When locks mempool（588）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **Commit wait broadcast_tx not already can proceed ≠ 301 / 310 bundled interchangeable：** 官方把能调广播单句和已经能往下走 / 已经从池里删掉路径分开。
- **等回执 not receipt already settled ≠ 33 / 403 interchangeable：** 官方把等回执单句和已经交差路径分开。
- **同步内存池调用 not sync call already allowed ≠ 690 已经放下锁 interchangeable：** 官方把要拿内存池锁单句和已经允许写进 Commit 顺序逻辑路径分开；310 commitlock vs RPC bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Commit 里调 broadcast_tx | 不是 already can proceed | 不是提案已经从池里删掉（301） |
| 等回执 | 不是 receipt already settled | 不是四门已经结算（33） |
| 同步内存池调用 | 不是 sync call already allowed | 不是 Commit 前上锁 alone（690） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事（310 余量），必须分开能调广播 是不是 already can proceed interchangeable / 310 commitlock bundled interchangeable / 301 proposed-removed interchangeable、等回执 是不是 receipt already settled interchangeable / 33 four gates interchangeable / 403 finafter interchangeable、同步内存池调用 是不是 sync call already allowed interchangeable / 690 commitlock-notunlocked interchangeable。可以跳过「看见能调广播 就已经能往下走 interchangeable / 就已经交差 interchangeable / 就已经允许写进顺序逻辑 interchangeable」。不要另写怎样调广播。310 commitlock vs RPC bundled unbundling 在本页 item 3 完成（689 + 690 + 691）。

## 本页不抄

- 怎样调广播、怎样加锁、怎样写四门。
- Commit lock vs RPC bundled。那是不变量 310。
- default global lock not already RPC safe。那是不变量 310 item 1 余量 / 689。
- Commit 前上锁不是已经解锁。那是不变量 310 item 2 余量 / 690。
- 提案收了已经从池里删掉。那是不变量 301。
- Finalize When locks mempool。那是不变量 588。
- 四门已经结算。那是不变量 33。
