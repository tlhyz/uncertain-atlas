# 反模式：把 Query 请求 prove not already AppHash matched / not already one-layer tree / not already settled 正式三事（383 余量） 说成已经对上 AppHash / 已经是一层树 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notapphash-vs-bundled.md)。

## 卖法

把 Query 证明回包这句写成已经已经对上 AppHash / 已经是一层树 / 已经交差 interchangeable，或已经和 383 queryprove-vs-proof bundled / queryprove-notapphash-sold-as-bundled interchangeable。

## 为什么错

官方把 Query 请求 prove / 回包 proof_ops / 回包 height 三条核心句写成三件独立的实现事。把它们卖成已经对上 AppHash / 已经是一层树 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 请求 prove 正式三事（383 余量），必须分开 not already AppHash matched、not already one-layer tree、not already settled 三件事，不要和 383 / 325 / 780 / 781 糊成一句。

## 和相邻反模式

- [querycode-notkey-sold-as-bundled](querycode-notkey-sold-as-bundled.md) 是 Query 回包 info 就已经是按键查（384/778），不是本页 prove 边界。
- [querycode-notconsensus-sold-as-bundled](querycode-notconsensus-sold-as-bundled.md) 是 Query 回包 code 就已经过了共识（384/776），不是本页 prove 边界。
