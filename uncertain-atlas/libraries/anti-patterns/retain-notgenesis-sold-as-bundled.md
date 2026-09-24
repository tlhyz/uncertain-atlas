# 反模式：把全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事（366 余量）说成已经能从创世再装 / 已经能给轻客户端验 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[全网都删会永久丢 not already genesis-replay ≠ bundled（366）](../../tracks/implementation/worked-example-retain-notgenesis-vs-bundled.md)。

## 卖法

把全网都删会永久丢 / 若网上所有节点都删了历史块、这些数据就永久丢了 / 能剪会丢 写成已经能从创世再装 interchangeable / 已经 genesis-replay interchangeable / 已经从创世再装交差 interchangeable / 366 retain bundled interchangeable / retain-sold-as-kept interchangeable；把开了 state sync / 除非链上开了 state sync、否则新节点加不进来 / 能引导 写成已经能给轻客户端验 interchangeable / 已经 light-check interchangeable / 已经轻客户端验交差 interchangeable；把能丢 / 能剪会永久丢 / 审计回放轻客户端还可能要用 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 366 retain bundled / retain-sold-as-kept interchangeable / 847 retain-notgenesis interchangeable。

## 为什么错

官方把全网都删会永久丢、不是已经能给轻客户端验、不是已经交差写成三件独立的实现事。把它们卖成 already genesis-replay interchangeable / already light-check interchangeable / already settled interchangeable，会把 not already genesis-replay、not already light-check、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看全网都删了会永久丢不是已经能从创世再装 not already genesis-replay / not already light-check / not already settled 正式三事（366 余量），必须分开 not already genesis-replay、not already light-check、not already settled 三件事，不要和 366 / 38 / 845 / 846 糊成一句。

## 和相邻反模式

- [retain-sold-as-kept](retain-sold-as-kept.md) 是 retain bundled 全段，不是本页全网都删会永久丢 item 3 单句边界。
- [retain-notpruning-sold-as-bundled](retain-notpruning-sold-as-bundled.md) 是 retain_height 默认 0 not already pruning（366 item 1），不是本页 not already genesis-replay 边界。
- [retain-notdeleted-sold-as-bundled](retain-notdeleted-sold-as-bundled.md) 是低于这个高度的块可以被删 not already deleted（366 item 2），不是本页 not already light-check 边界。
- [statesync-sold-as-genesis](statesync-sold-as-genesis.md) 是应用快照就已经从创世重放（38），不是本页 not already settled 单句。
