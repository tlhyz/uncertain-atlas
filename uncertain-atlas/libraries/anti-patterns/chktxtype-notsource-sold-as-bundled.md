# 反模式：把 CheckTx Request type CheckTx_Recheck mempool normal recheck not external new transaction / not CheckTx_New default / not pool dedup means no replay 正式三事（484 余量） 说成已经是外部新交易 / 已经是 New default / 已经去重保证不重放

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[type ≠ bundled（484）](../../tracks/implementation/worked-example-chktxtype-notsource-vs-bundled.md)。

## 卖法

把 CheckTx Request type 这句写成已经已经是外部新交易 / 已经是 New default / 已经去重保证不重放 interchangeable，或已经和 484 chktxtype-vs-recheck bundled / chktxtype-notsource-sold-as-bundled interchangeable。

## 为什么错

官方把 CheckTx Request type 三条核心句写成三件独立的实现事。把它们卖成已经是外部新交易 / 已经是 New default / 已经去重保证不重放，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type CheckTx_Recheck 正式三事（484 余量），必须分开 not external new、not New default、not pool dedup 三件事，不要和 484 / 405 / 313 / 707 / 709 糊成一句。

## 和相邻反模式

- [chktxtype-sold-as-recheck](chktxtype-sold-as-recheck.md) 是 CheckTx Request type bundled（484），不是本页 item 2 单句边界。
- [chktxtype-notrecheck-sold-as-bundled](chktxtype-notrecheck-sold-as-bundled.md) 是 New 单句边界（707 item 1），不是本页 Recheck 边界。
