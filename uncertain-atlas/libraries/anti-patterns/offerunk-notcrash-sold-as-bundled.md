# 反模式：把 OfferSnapshot Result UNKNOWN not ProposalStatus crash / not ABORT / not settled 正式三事（402 余量） 说成已经会崩 / 已经 ABORT / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[UNKNOWN ≠ bundled（402）](../../tracks/implementation/worked-example-offerunk-notcrash-vs-bundled.md)。

## 卖法

把 OfferSnapshot Result 余量这句写成已经已经会崩 / 已经 ABORT / 已经交差 interchangeable，或已经和 402 offerunk-vs-crash bundled / offerunk-notcrash-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot Result UNKNOWN / ACCEPT / REJECT 三条核心句写成三件独立的实现事。把它们卖成已经会崩 / 已经 ABORT / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result UNKNOWN 正式三事（402 余量），必须分开 not ProposalStatus crash、not ABORT、not settled 三件事，不要和 402 / 376 / 400 / 726 / 727 糊成一句。

## 和相邻反模式

- [offerunk-sold-as-crash](offerunk-sold-as-crash.md) 是 OfferSnapshot 结果枚举余量 bundled（402），不是本页 item 1 单句边界。
- [offerunk-notrestored-sold-as-bundled](offerunk-notrestored-sold-as-bundled.md) 是 ACCEPT 单句边界（726 item 2），不是本页 UNKNOWN 边界。
