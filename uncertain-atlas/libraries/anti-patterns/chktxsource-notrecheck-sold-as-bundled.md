# 反模式：把 CheckTx Usage may come from an external user not CheckTx_Recheck / not CheckTx_New bundled / not broadcast_tx once 正式三事（488 余量）说成已经 Recheck / 已经 New bundled / 已经 broadcast_tx once

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[may come from an external user not CheckTx_Recheck ≠ bundled（488）](../../tracks/implementation/worked-example-chktxsource-notrecheck-vs-bundled.md)。

## 卖法

把 may come from an external user / 能来自外部用户 写成已经 CheckTx_Recheck interchangeable / 484 chktxtype Recheck interchangeable / 已经 Type=RECHECK interchangeable；把能来自外部用户写成已经 CheckTx_New bundled 就代表来源验完 interchangeable / 484 chktxtype New interchangeable；把看见外部用户送来写成已经 RPC broadcast_tx 就代表全网只收一次 interchangeable / 313 bundled interchangeable，或已经和 488 chktxsource-vs-recheck bundled / chktxsource-notrecheck-sold-as-bundled interchangeable / 683 chktxsource-notrecheck interchangeable。

## 为什么错

官方把 CheckTx Usage 外部用户来源、Recheck、New bundled、broadcast_tx once 写成三件独立的实现事。把它们卖成 Recheck interchangeable / New bundled interchangeable / broadcast_tx once interchangeable，会把 not Recheck、not New bundled、not broadcast_tx once 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from an external user 正式三事（488 余量），必须分开 not Recheck、not New bundled、not broadcast_tx once 三件事，不要和 488 / 484 / 313 / 391 / 684 / 685 糊成一句。

## 和相邻反模式

- [chktxsource-sold-as-replay](chktxsource-sold-as-replay.md) 是 CheckTx Usage tx source bundled（488），不是本页 item 1 单句边界。
- [chktxsource-notremoved-sold-as-bundled](chktxsource-notremoved-sold-as-bundled.md) 是 another node 单句边界（684 item 2），不是本页 external user 边界。
