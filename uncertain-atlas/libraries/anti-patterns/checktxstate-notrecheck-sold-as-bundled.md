# 反模式：把 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事（312 余量）说成已经是新交易 / 已经当 NEW 处理 / 已经解锁

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[RECHECK not already new transaction ≠ bundled（312）](../../tracks/implementation/worked-example-checktxstate-notrecheck-vs-bundled.md)。

## 卖法

把 Commit 之后又跑了 CheckTx / 又跑了 / 对本地池里剩下的再验 写成已经是一笔新交易 interchangeable / 已经 new transaction interchangeable / 已经是 NEW interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable；把 Type 是 RECHECK / Type 在 写成已经当 NEW 处理 interchangeable / 已经 treated as NEW interchangeable；把 Commit 回了 / Commit 返回 写成已经放下锁 interchangeable / 已经 unlocked interchangeable，或已经和 312 checktxstate bundled / checktxstate-sold-as-execute interchangeable / 697 checktxstate-notrecheck interchangeable。

## 为什么错

官方把再验单句、already new transaction、already treated as NEW、already unlocked 写成三件独立的实现事。把它们卖成 already new transaction interchangeable / already treated as NEW interchangeable / already unlocked interchangeable，会把 not already new transaction、not already treated as NEW、not already unlocked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 RECHECK 不是已经是新交易 not already new transaction / not already treated as NEW / not already unlocked 正式三事（312 余量），必须分开 not already new transaction、not already treated as NEW、not already unlocked 三件事，不要和 312 / 33 / 695 / 696 / 310 / 690 / 301 糊成一句。

## 和相邻反模式

- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState vs ExecuteTxState bundled 全段，不是本页 RECHECK item 3 单句边界。
- [checktxstate-notsame-sold-as-bundled](checktxstate-notsame-sold-as-bundled.md) 是同时在改 item 2，不是本页又跑了 ≠ 已经是新交易边界。
- [commitlock-notunlocked-sold-as-bundled](commitlock-notunlocked-sold-as-bundled.md) 是 Commit 前上锁 ≠ 已经解锁（690），不是本页 Commit 回了但 RECHECK 期间还握着锁边界。
