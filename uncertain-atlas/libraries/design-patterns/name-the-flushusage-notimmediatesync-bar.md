# 模式：把 Flush Usage Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事（493 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[Flush Usage Called immediately for sync request returns when Flush response comes back not Echo Response Message ≠ bundled（493）](../../tracks/implementation/worked-example-flushusage-notimmediatesync-vs-bundled.md)。

## 三个名字

1. **Called immediately for sync request returns when Flush response comes back 不是 Echo Response Message：** 看见 Methods Flush Usage 同步回包，不是已经 Echo Response Message the input string interchangeable，不是 492 echousage-vs-flush interchangeable / 493 flushusage-vs-echo bundled interchangeable / 673 flushusage-notimmediatesync interchangeable。

2. **immediately for sync request / Flush response comes back 不是 Commit 锁等广播：** 看见立刻 Flush 做成同步请求、回包回来才算这次同步，不是已经 Commit 里等广播就已经能往下走 interchangeable，不是 310 commit-lock-vs-rpc interchangeable / 481 commitpersist interchangeable / 672 flushusage-notperiodicasync interchangeable。

3. **returns when Flush response comes back 不是 commit-empty-echo bundled 第三件事：** 看见 Flush response comes back，不是已经 Echo 用来测实现就已经刷完 interchangeable，不是 399 commit-empty-echo bundled interchangeable / 399 commit-empty-echo item 3 interchangeable / 671 flushusage-notechoqueued interchangeable。

官方把 Flush Usage immediately for sync request / Flush response comes back 单句、Echo Response Message 栏（492）、Commit 锁（310）、Commit 空请求 bundled 第三件事（399）写成三个名字。把它们叫成一个「看见 Called immediately for sync request returns when Flush response comes back 就已经 Echo 回包 Message interchangeable / 就已经 Commit 能往下走 interchangeable / 就已经 commit-empty-echo bundled 第三件事 interchangeable」，会把 not Echo Response Message、not Commit lock、not commit-empty-echo bundled item 3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事（493 余量），先数清问的是 Called immediately for sync request 是不是 Echo Response Message / 492 / 493 bundled，是不是 Flush response comes back 是不是 Commit lock / 310 / 481，还是 returns when Flush response comes back 是不是 commit-empty-echo bundled item 3 / 399 / 672，再决定要不要同一次发布。493 flushusage vs echo bundled unbundling 在本页 item 3 完成。
