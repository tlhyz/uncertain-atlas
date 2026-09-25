# 反模式：把立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事（374 余量）说成已经能往下走 / 已经 Commit / 已经解锁

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[立刻叫了 not already proceed ≠ bundled（374）](../../tracks/implementation/worked-example-flush-notproceed-vs-bundled.md)。

## 卖法

把立刻叫了 / 立刻 Flush 是为了做成同步请求、回包回来才算这次同步 / 立刻叫了 Flush 写成已经能往下走 interchangeable / 已经 proceed interchangeable / 已经能往下走交差 interchangeable / 374 flush bundled interchangeable / flush-sold-as-sent interchangeable；把回包回来 / Flush 回包回来 / 回包在 写成已经 Commit interchangeable / 已经 commit interchangeable / 已经 Commit 交差 interchangeable；把同步了 / 这次同步算完 / 同步完了 写成已经解锁 interchangeable / 已经 unlocked interchangeable / 已经解锁交差 interchangeable，或已经和 374 flush bundled / flush-sold-as-sent interchangeable / 871 flush-notproceed interchangeable。

## 为什么错

官方把立刻叫了、不是已经 Commit、不是已经解锁写成三件独立的实现事。把它们卖成 already proceed interchangeable / already commit interchangeable / already unlocked interchangeable，会把 not already proceed、not already commit、not already unlocked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走 not already proceed / not already commit / not already unlocked 正式三事（374 余量），必须分开 not already proceed、not already commit、not already unlocked 三件事，不要和 374 / 310 / 869 / 870 糊成一句。

## 和相邻反模式

- [flush-sold-as-sent](flush-sold-as-sent.md) 是 flush bundled 全段，不是本页立刻叫了 item 3 单句边界。
- [flush-notsent-sold-as-bundled](flush-notsent-sold-as-bundled.md) 是叫了 not already sent（374 item 1），不是本页 not already proceed 边界。
- [flush-notfourgates-sold-as-bundled](flush-notfourgates-sold-as-bundled.md) 是定期在冲 not already fourgates（374 item 2），不是本页 not already unlocked 边界。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 里等广播就已经能往下走（310），不是本页 not already proceed 单句。
