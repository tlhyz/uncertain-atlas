# 反模式：把 OfferSnapshot Result REJECT not REJECT_FORMAT / not REJECT_SNAPSHOT / not already complete 正式三事（402 余量） 说成已经拒掉这种 format / 已经 REJECT_SNAPSHOT / 已经齐

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[REJECT ≠ bundled（402）](../../tracks/implementation/worked-example-offerunk-notformat-vs-bundled.md)。

## 卖法

把 OfferSnapshot Result 余量这句写成已经已经拒掉这种 format / 已经 REJECT_SNAPSHOT / 已经齐 interchangeable，或已经和 402 offerunk-vs-crash bundled / offerunk-notformat-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot Result UNKNOWN / ACCEPT / REJECT 三条核心句写成三件独立的实现事。把它们卖成已经拒掉这种 format / 已经 REJECT_SNAPSHOT / 已经齐，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT 正式三事（402 余量），必须分开 not REJECT_FORMAT、not REJECT_SNAPSHOT、not already complete 三件事，不要和 402 / 400 / 398 / 725 / 726 糊成一句。

## 和相邻反模式

- [offerunk-sold-as-crash](offerunk-sold-as-crash.md) 是 OfferSnapshot 结果枚举余量 bundled（402），不是本页 item 3 单句边界。
- [offerunk-notrestored-sold-as-bundled](offerunk-notrestored-sold-as-bundled.md) 是 ACCEPT 单句边界（726 item 2），不是本页 REJECT 边界。
