# 模式：把立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事（374 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[立刻叫了 not already proceed ≠ bundled（374）](../../tracks/implementation/worked-example-flush-notproceed-vs-bundled.md)。

## 三个名字

1. **立刻叫了 不是 already proceed：** 看见立刻叫了 / 立刻 Flush 是为了做成同步请求、回包回来才算这次同步 / 立刻叫了 Flush，不是已经能往下走 interchangeable / 已经 proceed interchangeable / 已经能往下走交差 interchangeable，不是 374 flush bundled interchangeable / flush-sold-as-sent interchangeable。

2. **回包回来 不是 already commit：** 看见回包回来 / Flush 回包回来 / 回包在，不是已经 Commit interchangeable / 已经 commit interchangeable / 已经 Commit 交差 interchangeable，不是 310 commit-lock interchangeable / 869 flush-notsent interchangeable。

3. **同步了 不是 already unlocked：** 看见同步了 / 这次同步算完 / 同步完了，不是已经解锁 interchangeable / 已经 unlocked interchangeable / 已经解锁交差 interchangeable，不是 870 flush-notfourgates interchangeable / 310 commit-lock interchangeable。

官方把立刻叫了、不是已经 Commit、不是已经解锁写成三个名字。把它们叫成一个「看见立刻叫了就已经能往下走 interchangeable / 就已经 Commit interchangeable / 就已经解锁 interchangeable」，会把 not already proceed、not already commit、not already unlocked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事（374 余量），先数清问的是立刻叫了 是不是 already proceed / 374 / flush-sold-as-sent，是不是回包回来 是不是 already commit，还是同步了 是不是 already unlocked，再决定要不要同一次发布。374 flush-vs-sent bundled unbundling 在本页 item 3 完成。
