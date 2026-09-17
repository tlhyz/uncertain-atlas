# 模式：把 MUST persist in Commit / before returning from Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事（335 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**例**：[MUST persist in Commit not already persisted in Finalize ≠ bundled（335）](../../tracks/implementation/worked-example-finpersist-notmustincommit-vs-bundled.md)。

## 三个名字

1. **MUST persist in Commit 不是 already persisted in Finalize：** 看见 Requirements 持久化 MUST 在 Commit 里做 / before returning from Commit，不是已经 Finalize 落了 interchangeable / 已经写盘 interchangeable / 683 finpersist-notmustnot interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable / 680 commitpersist-notfinpersist interchangeable / 481 commitpersist item 1 interchangeable。

2. **before returning from Commit 不是 already unlocked：** 看见返回前写完 / MUST persist in Commit 单句，不是已经解锁 interchangeable / 已经内存池锁已经放下 interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable / 310 commit-lock-vs-rpc interchangeable / 646 fincommit-notcommitlock interchangeable / 629 notsettled interchangeable。

3. **必须在 Commit 落盘 不是 Commit green can wait for broadcast：** 看见 Commit 前返回 / before returning from Commit，不是已经 Commit 绿了就能等广播 interchangeable / 已经默认锁已经 RPC 安全 interchangeable / 310 commitlock interchangeable / 681 commitpersist-notendofcall interchangeable / 399 commit-empty-echo bundled interchangeable / 481 commitpersist interchangeable。

官方把 Requirements MUST persist in Commit 单句、already persisted in Finalize（683）、already unlocked（588/310）、Commit green can wait for broadcast（310/481）写成三个名字。把它们叫成一个「看见必须在 Commit 落盘 就已经在 Finalize 落了 interchangeable / 就已经解锁 interchangeable / 就已经 Commit 绿了 interchangeable」，会把 not already persisted in Finalize、not already unlocked、not Commit green can wait for broadcast 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事（335 余量），先数清问的是 MUST persist in Commit 是不是 already persisted in Finalize / 683 / 680 / 481，是不是 before returning from Commit 是不是 already unlocked / 588 / 592 / 310 / 646，还是 Commit 前返回 是不是 Commit green can wait for broadcast / 310 / 681 / 399，再决定要不要同一次发布。335 finpersist vs commit bundled unbundling 在本页 item 2 完成。
