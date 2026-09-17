# 反模式：把 Query 回包 height not already request height / not already fresh / not already header AppHash 正式三事（383 余量） 说成已经是请求高度 / 已经新鲜 / 已经印进本头 AppHash

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notreqh-vs-bundled.md)。

## 卖法

把 Query 证明回包这句写成已经已经是请求高度 / 已经新鲜 / 已经印进本头 AppHash interchangeable，或已经和 383 queryprove-vs-proof bundled / queryprove-notreqh-sold-as-bundled interchangeable。

## 为什么错

官方把 Query 请求 prove / 回包 proof_ops / 回包 height 三条核心句写成三件独立的实现事。把它们卖成已经是请求高度 / 已经新鲜 / 已经印进本头 AppHash，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 height 正式三事（383 余量），必须分开 not already request height、not already fresh、not already header AppHash 三件事，不要和 383 / 371 / 779 / 780 糊成一句。

## 和相邻反模式

- [queryprove-notstore-sold-as-bundled](queryprove-notstore-sold-as-bundled.md) 是 proof_ops 单句边界（780 item 2），不是本页 height 边界。
- [querycode-notfresh-sold-as-bundled](querycode-notfresh-sold-as-bundled.md) 是 Query 回包 log 就已经新鲜（384/777），不是本页 height 边界。
