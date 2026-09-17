# 反模式：把 validator_updates 空 not already no set / not already changed set / not already InitChain empty list 正式三事（382 余量） 说成已经没有集合 / 已经改了集合 / 已经是 InitChain 那种空名单

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[validator_updates ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notnoset-vs-bundled.md)。

## 卖法

把 Finalize 请求回包这句写成已经已经没有集合 / 已经改了集合 / 已经是 InitChain 那种空名单 interchangeable，或已经和 382 syncingheight-vs-history bundled / syncingheight-notnoset-sold-as-bundled interchangeable。

## 为什么错

官方把 syncing_to_height / validator_updates 空 / Finalize events 三条核心句写成三件独立的实现事。把它们卖成已经没有集合 / 已经改了集合 / 已经是 InitChain 那种空名单，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 空 正式三事（382 余量），必须分开 not already no set、not already changed set、not already InitChain empty list 三件事，不要和 382 / 318 / 388 / 765 / 782 / 784 糊成一句。

## 和相邻反模式

- [syncingheight-nothistory-sold-as-bundled](syncingheight-nothistory-sold-as-bundled.md) 是 syncing_to_height 单句边界（782 item 1），不是本页空更新边界。
- [initparams-notnoset-sold-as-bundled](initparams-notnoset-sold-as-bundled.md) 是 InitChain 请求 validators 就已经没有集合（388/765），不是本页 Finalize 空更新边界。
