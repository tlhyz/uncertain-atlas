# 反模式：把 Query 回包 codespace not already CheckTx codespace / not already response code / not already settled 正式三事（389 余量） 说成已经是 CheckTx 码空间 / 已经是回包码 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query ≠ bundled（389）](../../tracks/implementation/worked-example-infodata-notchktxspace-vs-bundled.md)。

## 卖法

把 Info 回包余栏这句写成已经已经是 CheckTx 码空间 / 已经是回包码 / 已经交差 interchangeable，或已经和 389 infodata-vs-appversion bundled / infodata-notchktxspace-sold-as-bundled interchangeable。

## 为什么错

官方把 Info 回包 data / Info 回包 version / Query 回包 codespace 三条核心句写成三件独立的实现事。把它们卖成已经是 CheckTx 码空间 / 已经是回包码 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 codespace 正式三事（389 余量），必须分开 not already CheckTx codespace、not already response code、not already settled 三件事，不要和 389 / 381 / 393 / 748 / 761 / 762 糊成一句。

## 和相邻反模式

- [infodata-sold-as-appversion](infodata-sold-as-appversion.md) 是 Info 回包余栏 bundled（389），不是本页 item 3 单句边界。
- [exectxgas-notcodespace-sold-as-bundled](exectxgas-notcodespace-sold-as-bundled.md) 是 ExecTxResult.codespace 就已经是 CheckTx 码空间（393/748），不是本页 Query codespace 边界。
