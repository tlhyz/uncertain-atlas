# 反模式：把 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事（310 余量）说成已经能往下走 / 已经交差 / 已经允许

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Commit 里等 broadcast_tx not already can proceed ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notbroadcast-vs-bundled.md)。

## 卖法

把 Commit 里调了 broadcast_tx / 能调广播 / 发了 `/broadcast_tx_sync` 或 `/broadcast_tx` 写成已经能往下走 interchangeable / 已经 can proceed interchangeable / 已经能继续 interchangeable / 310 commitlock bundled interchangeable / 689 commitlock-notrpcsafe interchangeable / 690 commitlock-notunlocked interchangeable；把等回执 / waits for the response 写成已经交差 interchangeable / 已经 settled interchangeable；把同步内存池调用 / Synchronous mempool-related calls 写成已经允许写进 Commit 顺序逻辑 interchangeable / 已经 allowed sync mempool in Commit interchangeable，或已经和 310 commitlock bundled / commitlock-sold-as-rpc interchangeable / 691 commitlock-notbroadcast interchangeable。

## 为什么错

官方把能调广播单句、already can proceed、already settled、already allowed sync mempool in Commit 写成三件独立的实现事。把它们卖成 already can proceed interchangeable / already settled interchangeable / already allowed sync mempool in Commit interchangeable，会把 not already can proceed、not already settled、not already allowed sync mempool in Commit 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 里等 broadcast_tx not already can proceed / not already settled / not already allowed sync mempool in Commit 正式三事（310 余量），必须分开 not already can proceed、not already settled、not already allowed sync mempool in Commit 三件事，不要和 310 / 689 / 690 / 33 / 403 / 301 / 5 / 307 糊成一句。

## 和相邻反模式

- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit lock vs RPC bundled 全段，不是本页 Commit 里等广播 item 3 单句边界。
- [commitlock-notrpcsafe-sold-as-bundled](commitlock-notrpcsafe-sold-as-bundled.md) 是 default global lock item 1，不是本页能调广播 ≠ 已经能往下走边界。
- [commitlock-notunlocked-sold-as-bundled](commitlock-notunlocked-sold-as-bundled.md) 是 Commit 前上锁 item 2，不是本页等回执 ≠ 已经交差边界。
