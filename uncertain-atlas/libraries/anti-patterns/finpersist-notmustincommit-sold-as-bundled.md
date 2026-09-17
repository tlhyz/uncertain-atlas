# 反模式：把 MUST persist in Commit / before returning from Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事（335 余量）说成已经在 Finalize 落了 / 已经解锁 / 已经 Commit 绿了

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[MUST persist in Commit not already persisted in Finalize ≠ bundled（335）](../../tracks/implementation/worked-example-finpersist-notmustincommit-vs-bundled.md)。

## 卖法

把持久化 MUST 在 `Commit` 里做 / 应用应在 Commit 里持久化自己的状态 / before returning from Commit 写成已经 Finalize 落了 interchangeable / 已经写盘 interchangeable / 683 finpersist-notmustnot interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable / 680 commitpersist-notfinpersist interchangeable / 481 commitpersist item 1 persist signal interchangeable；把返回前写完 / MUST persist in Commit 单句 写成已经解锁 interchangeable / 已经内存池锁已经放下 interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable / 310 commit-lock-vs-rpc interchangeable / 646 fincommit-notcommitlock interchangeable / 629 notsettled interchangeable / 632 notsettled interchangeable；把 Commit 前返回 / before returning from Commit 写成已经 Commit 绿了就能等广播 interchangeable / 已经默认锁已经 RPC 安全 interchangeable / 310 commitlock interchangeable / 681 commitpersist-notendofcall interchangeable / 399 commit-empty-echo bundled interchangeable / 481 commitpersist interchangeable，或已经和 335 finpersist-vs-commit bundled / finalizepersist-sold-as-committed interchangeable / 684 finpersist-notmustincommit interchangeable。

## 为什么错

官方把 Requirements MUST persist in Commit 单句、already persisted in Finalize（683）、already unlocked（588/592/310）、Commit green can wait for broadcast（310/481/681）写成三件独立的实现事。把它们卖成 already persisted in Finalize interchangeable / already unlocked interchangeable / Commit green can wait for broadcast interchangeable，会把 not already persisted in Finalize、not already unlocked、not Commit green can wait for broadcast 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事（335 余量），必须分开 not already persisted in Finalize、not already unlocked、not Commit green can wait for broadcast 三件事，不要和 335 / 683 / 680 / 481 / 588 / 592 / 310 / 646 / 681 / 399 糊成一句。

## 和相邻反模式

- [finpersist-notmustnot-sold-as-bundled](finpersist-notmustnot-sold-as-bundled.md) 是 MUST NOT persist in Finalize vs already persisted（335 item 1 余量 / 683），不是本页 MUST persist in Commit 单句边界。
- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 FinalizeBlock 落盘禁令 bundled 全段，不是本页 MUST persist in Commit item 2 单句边界。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是默认锁已经 RPC 安全 bundled（310），不是本页 Requirements MUST persist in Commit 单句边界。
