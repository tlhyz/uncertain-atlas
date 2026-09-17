# 反模式：把 CheckTx Usage may come from another node not gossip verified / not removed from pool / not forever valid 正式三事（488 余量）说成已经流言验过 / 已经从池里删掉 / 已经 forever valid

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[may come from another node not removed from pool ≠ bundled（488）](../../tracks/implementation/worked-example-chktxsource-notremoved-vs-bundled.md)。

## 卖法

把 may come from another node / 能来自另一节点 写成已经 P2P 流言就代表全网已经验过 interchangeable / 已经流言广播就代表来源已经验过 interchangeable；把能来自邻居写成已经从池里删掉 / 提案收了 interchangeable / 301 proposed-vs-removed interchangeable；把看见邻居送来写成已经 CheckTx 过了就永远有效 interchangeable / 301 forever valid interchangeable，或已经和 488 chktxsource-vs-recheck bundled / chktxsource-notremoved-sold-as-bundled interchangeable / 684 chktxsource-notremoved interchangeable。

## 为什么错

官方把 CheckTx Usage 邻居来源、流言验完、从池里删掉、forever valid 写成三件独立的实现事。把它们卖成 gossip verified interchangeable / removed from pool interchangeable / forever valid interchangeable，会把 not gossip verified、not removed from pool、not forever valid 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from another node 正式三事（488 余量），必须分开 not gossip verified、not removed from pool、not forever valid 三件事，不要和 488 / 301 / 33 / 405 / 683 / 685 糊成一句。

## 和相邻反模式

- [chktxsource-sold-as-replay](chktxsource-sold-as-replay.md) 是 CheckTx Usage tx source bundled（488），不是本页 item 2 单句边界。
- [chktxsource-notrecheck-sold-as-bundled](chktxsource-notrecheck-sold-as-bundled.md) 是 external user 单句边界（683 item 1），不是本页 another node 边界。
