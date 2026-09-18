# 模式：把 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事（310 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[lock mempool before Commit not already unlocked ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notunlocked-vs-bundled.md)。

## 三个名字

1. **锁上了 不是 already unlocked：** 看见 Commit 前锁了内存池 / 冲掉内存池连接，不是已经解锁 interchangeable / 已经和 Commit 同步做完 interchangeable，不是 310 commitlock bundled interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable。

2. **能一起更新 不是 already sync done：** 看见同时把四条连接的状态更新到最新已提交 / 好一起更新，不是已经更新完 interchangeable / 已经和 Commit 同步做完 interchangeable，不是 310 commitlock item 1 interchangeable / 689 commitlock-notrpcsafe interchangeable。

3. **Commit 回了 不是 Commit return already released：** 看见 Commit 返回 / 应用 Commit 绿了，不是已经按同一条路径放下锁 interchangeable / 已经异步解锁已经做完 interchangeable，不是 310 commitlock item 3 interchangeable / 691 commitlock-notbroadcast interchangeable。

官方把 Commit 前上锁单句、already unlocked、already sync done、Commit return already released 写成三个名字。把它们叫成一个「看见锁上了 就已经解锁 interchangeable / 就已经同步做完 interchangeable / 就已经放下锁 interchangeable」，会把 not already unlocked、not already sync done、not Commit return already released 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事（310 余量），先数清问的是锁上了 是不是 already unlocked / 310 / 588，是不是能一起更新 是不是 already sync done，还是 Commit 回了 是不是 already released，再决定要不要同一次发布。310 commitlock vs RPC bundled unbundling 在本页 item 2 完成。
