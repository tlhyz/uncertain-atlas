# 反模式：把 CheckTx Request type CheckTx_New default full check not CheckTx_Recheck / not tx field means Recheck / not CheckTx forever valid 正式三事（484 余量） 说成已经是 Recheck / 已经 tx 栏就等于 Recheck / 已经永远有效

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[type ≠ bundled（484）](../../tracks/implementation/worked-example-chktxtype-notrecheck-vs-bundled.md)。

## 卖法

把 CheckTx Request type 这句写成已经已经是 Recheck / 已经 tx 栏就等于 Recheck / 已经永远有效 interchangeable，或已经和 484 chktxtype-vs-recheck bundled / chktxtype-notrecheck-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx Request type 三条核心句写成三件独立的实现事。把它们卖成已经是 Recheck / 已经 tx 栏就等于 Recheck / 已经永远有效，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type CheckTx_New 正式三事（484 余量），必须分开 not Recheck、not tx field means Recheck、not forever valid 三件事，不要和 484 / 391 / 301 / 708 / 709 糊成一句。

## 和相邻反模式

- [chktxtype-sold-as-recheck](chktxtype-sold-as-recheck.md) 是 CheckTx Request type bundled（484），不是本页 item 1 单句边界。
- [chktxtype-notsource-sold-as-bundled](chktxtype-notsource-sold-as-bundled.md) 是 Recheck 单句边界（708 item 2），不是本页 New 边界。
