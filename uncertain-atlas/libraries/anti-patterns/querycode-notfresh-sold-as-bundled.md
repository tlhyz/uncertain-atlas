# 反模式：把 Query 回包 log not already fresh / not already replicated / not already settled 正式三事（384 余量） 说成已经新鲜 / 已经复制到各节点 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query ≠ bundled（384）](../../tracks/implementation/worked-example-querycode-notfresh-vs-bundled.md)。

## 卖法

把 Query 回包码这句写成已经已经新鲜 / 已经复制到各节点 / 已经交差 interchangeable，或已经和 384 querycode-vs-consensus bundled / querycode-notfresh-sold-as-bundled interchangeable。

## 为什么错

官方把 Query 回包 code / log / info 三条核心句写成三件独立的实现事。把它们卖成已经新鲜 / 已经复制到各节点 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 log 正式三事（384 余量），必须分开 not already fresh、not already replicated、not already settled 三件事，不要和 384 / 329 / 414 / 758 / 390 / 745 / 776 / 778 糊成一句。

## 和相邻反模式

- [querycode-sold-as-consensus](querycode-sold-as-consensus.md) 是 Query 回包码 bundled（384），不是本页 item 2 单句边界。
- [querycode-notconsensus-sold-as-bundled](querycode-notconsensus-sold-as-bundled.md) 是 code 单句边界（776 item 1），不是本页 log 边界。
