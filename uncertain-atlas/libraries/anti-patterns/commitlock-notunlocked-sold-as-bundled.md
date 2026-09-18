# 反模式：把 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事（310 余量）说成已经解锁 / 已经同步做完 / 已经放下锁

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[lock mempool before Commit not already unlocked ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notunlocked-vs-bundled.md)。

## 卖法

把 Commit 前锁了内存池 / 锁上了 / 冲掉内存池连接 写成已经解锁 interchangeable / 已经 unlocked interchangeable / 已经和 Commit 同步做完 interchangeable / 310 commitlock bundled interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable；把能一起更新四份状态 / 同时更新到最新已提交 写成已经更新完 interchangeable / 已经 sync done interchangeable；把 Commit 回了 / Commit 绿了 写成已经按同一条路径放下锁 interchangeable / 已经异步解锁已经做完 interchangeable，或已经和 310 commitlock bundled / commitlock-sold-as-rpc interchangeable / 690 commitlock-notunlocked interchangeable。

## 为什么错

官方把 Commit 前上锁单句、already unlocked、already sync done、Commit return already released 写成三件独立的实现事。把它们卖成 already unlocked interchangeable / already sync done interchangeable / Commit return already released interchangeable，会把 not already unlocked、not already sync done、not Commit return already released 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事（310 余量），必须分开 not already unlocked、not already sync done、not Commit return already released 三件事，不要和 310 / 588 / 592 / 689 / 691 / 5 / 33 糊成一句。

## 和相邻反模式

- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit lock vs RPC bundled 全段，不是本页 Commit 前上锁 item 2 单句边界。
- [commitlock-notrpcsafe-sold-as-bundled](commitlock-notrpcsafe-sold-as-bundled.md) 是 default global lock item 1，不是本页锁上了 ≠ 已经解锁边界。
- [finlock-sold-as-settled](finlock-sold-as-settled.md) 是 Finalize When locks mempool ≠ 已经交差（588），不是本页 Commit 前上锁 vs 解锁边界。
