# 反模式：把 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事（310 余量）说成已经能往下走 / 已经交差 / 已经允许写进顺序逻辑

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Commit wait broadcast_tx not already can proceed ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notbroadcast-vs-bundled.md)。

## 卖法

把 Commit 里调了 broadcast_tx / 能调广播 / 发了 `/broadcast_tx_sync` 写成已经能往下走 interchangeable / 已经能继续 interchangeable / 310 commitlock bundled interchangeable / 301 proposed-removed interchangeable；把等回执 / 等 broadcast_tx 回执再往下走 写成已经交差 interchangeable / 已经 settled interchangeable；把同步内存池调用 / 写进 Commit 顺序逻辑 写成已经允许写进 Commit 顺序逻辑 interchangeable / 已经能在 Commit 里等锁 interchangeable，或已经和 310 commitlock bundled / commitlock-sold-as-rpc interchangeable / 691 commitlock-notbroadcast interchangeable。

## 为什么错

官方把 Commit 里等广播单句、already can proceed、receipt already settled、sync call already allowed 写成三件独立的实现事。把它们卖成 already can proceed interchangeable / receipt already settled interchangeable / sync call already allowed interchangeable，会把 not already can proceed、not receipt already settled、not sync call already allowed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit wait broadcast_tx not already can proceed / not receipt already settled / not sync call already allowed 正式三事（310 余量），必须分开 not already can proceed、not receipt already settled、not sync call already allowed 三件事，不要和 310 / 301 / 690 / 689 / 588 / 33 糊成一句。

## 和相邻反模式

- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit lock vs RPC bundled 全段，不是本页 Commit 里等广播 item 3 单句边界。
- [commitlock-notunlocked-sold-as-bundled](commitlock-notunlocked-sold-as-bundled.md) 是 Commit 前上锁 item 2，不是本页能调广播 ≠ 已经能往下走边界。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了 ≠ 已经从池里删掉（301），不是本页等回执 ≠ 已经交差边界。
