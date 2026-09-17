# 反模式：把 Query 回包 info not already key lookup / not already AppHash matched / not already settled 正式三事（384 余量） 说成已经是按键查 / 已经对上 AppHash / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query ≠ bundled（384）](../../tracks/implementation/worked-example-querycode-notkey-vs-bundled.md)。

## 卖法

把 Query 回包码这句写成已经已经是按键查 / 已经对上 AppHash / 已经交差 interchangeable，或已经和 384 querycode-vs-consensus bundled / querycode-notkey-sold-as-bundled interchangeable。

## 为什么错

官方把 Query 回包 code / log / info 三条核心句写成三件独立的实现事。把它们卖成已经是按键查 / 已经对上 AppHash / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 info 正式三事（384 余量），必须分开 not already key lookup、not already AppHash matched、not already settled 三件事，不要和 384 / 380 / 391 / 754 / 414 / 759 / 776 / 777 糊成一句。

## 和相邻反模式

- [querycode-sold-as-consensus](querycode-sold-as-consensus.md) 是 Query 回包码 bundled（384），不是本页 item 3 单句边界。
- [querycode-notfresh-sold-as-bundled](querycode-notfresh-sold-as-bundled.md) 是 log 单句边界（777 item 2），不是本页 info 边界。
