# 反模式：把 InitChain 回包 app_hash not already header AppHash / not already no set / not already settled 正式三事（392 余量） 说成已经是本头 AppHash / 已经没有集合 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[InitChain ≠ bundled（392）](../../tracks/implementation/worked-example-initapphash-notheader-vs-bundled.md)。

## 卖法

把 InitChain 回包余栏这句写成已经已经是本头 AppHash / 已经没有集合 / 已经交差 interchangeable，或已经和 392 initapphash-vs-header bundled / initapphash-notheader-sold-as-bundled interchangeable。

## 为什么错

官方把 InitChain 回包 app_hash / Finalize 请求 hash / CommitInfo.round 三条核心句写成三件独立的实现事。把它们卖成已经是本头 AppHash / 已经没有集合 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 回包 app_hash 正式三事（392 余量），必须分开 not already header AppHash、not already no set、not already settled 三件事，不要和 392 / 147 / 495 / 756 / 757 糊成一句。

## 和相邻反模式

- [initapphash-sold-as-header](initapphash-sold-as-header.md) 是 InitChain 回包余栏 bundled（392），不是本页 item 1 单句边界。
- [initapphash-notknownhash-sold-as-bundled](initapphash-notknownhash-sold-as-bundled.md) 是 Finalize 请求 hash 单句边界（756 item 2），不是本页 app_hash 边界。
