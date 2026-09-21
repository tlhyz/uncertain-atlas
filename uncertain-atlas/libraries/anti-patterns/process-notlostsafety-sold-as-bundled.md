# 反模式：把 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（340 余量）说成已经丢了安全性 / 已经有引擎补丁 / 已经必须拒坏块

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[活性不能保证 not already lost-safety ≠ bundled（340）](../../tracks/implementation/worked-example-process-notlostsafety-vs-bundled.md)。

## 卖法

把活性不能保证 / Process 里有非确定 bug / 打中的进程无法守 Req 4 或 5 写成已经丢了安全性 interchangeable / 已经 lost-safety interchangeable / 已经丢安全性交差 interchangeable / 340 processdet bundled interchangeable / 327 preparetimeout interchangeable / processdet-sold-as-prepare interchangeable；把没有现成解法 / 目前没有清楚的解法 / 没有协议层补丁 写成已经有引擎补丁 interchangeable / 已经 has-patch interchangeable；把 SHOULD Accept / 通则是一律 Accept / 建议一律 Accept 写成已经必须拒坏块 interchangeable / 已经 must-reject interchangeable，或已经和 340 processdet bundled / processdet-sold-as-prepare interchangeable / 775 process-notlostsafety interchangeable。

## 为什么错

官方把活性不能保证单句、already lost-safety、already has-patch、already must-reject 写成三件独立的实现事。把它们卖成 already lost-safety interchangeable / already has-patch interchangeable / already must-reject interchangeable，会把 not already lost-safety、not already has-patch、not already must-reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（340 余量），必须分开 not already lost-safety、not already has-patch、not already must-reject 三件事，不要和 340 / 338 / 33 / 327 / 773 / 774 糊成一句。

## 和相邻反模式

- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 ProcessProposal 确定性 bundled 全段，不是本页活性不能保证 item 3 单句边界。
- [process-notlikeprepare-sold-as-bundled](process-notlikeprepare-sold-as-bundled.md) 是必须确定 ≠ 已经可以像 Prepare 那样（340 item 1），不是本页活性不能保证 ≠ 已经丢了安全性 边界。
- [process-nothonestonly-sold-as-bundled](process-nothonestonly-sold-as-bundled.md) 是两边同判 ≠ 已经只对诚实提案（340 item 2），不是本页 SHOULD Accept ≠ 已经必须拒坏块 边界。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径（327），不是本页没有现成解法 ≠ 已经有补丁 边界。
