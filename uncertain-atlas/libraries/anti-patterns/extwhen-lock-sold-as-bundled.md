# 反模式：把 ExtendVote When lock values 正式三事卖成 +2/3 prevote 锁住 bundled / validValue 跳过 Prepare / ExtendVote When 正式流程

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[lock values ≠ bundled](../../tracks/implementation/worked-example-extwhen-lock-vs-bundled.md)。

## 卖法

- 「看见 sets lockedValue and validValue to v 就已经 +2/3 prevote 锁住 bundled interchangeable / 已经会调 ExtendVote interchangeable。」
- 「看见 sets lockedRound and validRound to r 就已经 validValue 跳过 Prepare interchangeable / 已经 locked interchangeable。」
- 「看见 step 1 before ExtendVote call 就已经 ExtendVote When 正式流程 interchangeable / 已经广播 Precommit interchangeable。」

## 为什么错

官方把 sets lockedValue/validValue、sets lockedRound/validRound、step 1 before ExtendVote call 写成三件独立的实现事。把它们卖成 +2/3 prevote 锁住 bundled、validValue 跳过 Prepare、ExtendVote When 正式流程，会把 lock values、round 赋值、call 顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When lock values 正式三事，必须分开 sets lockedValue/validValue、sets lockedRound/validRound、step 1 before ExtendVote call 三个名字，不要把它们卖成 +2/3 prevote 锁住 bundled / validValue 跳过 Prepare / ExtendVote When 正式流程。

## 和相邻反模式

- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 ExtendVote 何时调用三事，不是本页 step 1 lockedValue/validValue 单句专用边界。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是 ExtendVote When 正式流程三事，不是本页 step 1 before ExtendVote call 单句专用边界。
