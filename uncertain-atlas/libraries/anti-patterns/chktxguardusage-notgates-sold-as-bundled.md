# 反模式：把 CheckTx Usage every node runs CheckTx before letting into local mempool not broadcast_tx others run / not in-pool gossip / not forever valid 正式三事（490 余量）说成已经别人也会跑 / 已经流言 / 已经 forever valid

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[every node runs CheckTx not forever valid ≠ bundled（490）](../../tracks/implementation/worked-example-chktxguardusage-notgates-vs-bundled.md)。

## 卖法

把 every node runs CheckTx before letting into local mempool / 每条节点先跑 CheckTx 写成已经 RPC broadcast_tx 回了就代表别的节点也会跑 CheckTx interchangeable；把先跑了才让进本地池写成已经进了本地池就开始 P2P 流言 interchangeable / 已经 Check 通过就是已进提案 interchangeable / 33 four gates interchangeable；把看见 every node 写成已经 CheckTx 过了就 forever valid interchangeable / 301 forever valid interchangeable，或已经和 490 chktxguardusage-vs-optional bundled / chktxguardusage-notgates-sold-as-bundled interchangeable / 690 chktxguardusage-notgates interchangeable。

## 为什么错

官方把 CheckTx Usage 本地池入口、别人也会跑、进池流言、forever valid 写成三件独立的实现事。把它们卖成 broadcast_tx others run interchangeable / in-pool gossip interchangeable / forever valid interchangeable，会把 not broadcast_tx others run、not in-pool gossip、not forever valid 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage every node runs CheckTx 正式三事（490 余量），必须分开 not broadcast_tx others run、not in-pool gossip、not forever valid 三件事，不要和 490 / 33 / 301 / 689 / 691 糊成一句。

## 和相邻反模式

- [chktxguardusage-sold-as-fourgates](chktxguardusage-sold-as-fourgates.md) 是 CheckTx Usage Guardian bundled（490），不是本页 item 2 单句边界。
- [chktxguardusage-notoptional-sold-as-bundled](chktxguardusage-notoptional-sold-as-bundled.md) 是 Guardian 单句边界（689 item 1），不是本页 every node 边界。
