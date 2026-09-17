# 反模式：把 Query 回包 key not already Query height / not already fresh / not already settled 正式三事（380 余量） 说成已经是 Query 高度 / 已经新鲜 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notheight-vs-bundled.md)。

## 卖法

把 Query 回包这句写成已经已经是 Query 高度 / 已经新鲜 / 已经交差 interchangeable，或已经和 380 queryindex-vs-store bundled / queryindex-notheight-sold-as-bundled interchangeable。

## 为什么错

官方把 Query 回包 index / key / value 三条核心句写成三件独立的实现事。把它们卖成已经是 Query 高度 / 已经新鲜 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 key 正式三事（380 余量），必须分开 not already Query height、not already fresh、not already settled 三件事，不要和 380 / 371 / 390 / 743 / 788 / 790 糊成一句。

## 和相邻反模式

- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 Query 回包 bundled（380），不是本页 item 2 单句边界。
- [queryindex-notstore-sold-as-bundled](queryindex-notstore-sold-as-bundled.md) 是 index 单句边界（788 item 1），不是本页 key 边界。
