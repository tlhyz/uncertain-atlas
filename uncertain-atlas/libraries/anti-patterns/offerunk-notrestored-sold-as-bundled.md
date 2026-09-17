# 反模式：把 OfferSnapshot Result ACCEPT not restored / not already complete / not ProposalStatus ACCEPT 正式三事（402 余量） 说成已经装完 / 已经齐 / 已经 Process ACCEPT

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ACCEPT ≠ bundled（402）](../../tracks/implementation/worked-example-offerunk-notrestored-vs-bundled.md)。

## 卖法

把 OfferSnapshot Result 余量这句写成已经已经装完 / 已经齐 / 已经 Process ACCEPT interchangeable，或已经和 402 offerunk-vs-crash bundled / offerunk-notrestored-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot Result UNKNOWN / ACCEPT / REJECT 三条核心句写成三件独立的实现事。把它们卖成已经装完 / 已经齐 / 已经 Process ACCEPT，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result ACCEPT 正式三事（402 余量），必须分开 not restored、not already complete、not ProposalStatus ACCEPT 三件事，不要和 402 / 401 / 321 / 376 / 725 / 727 糊成一句。

## 和相邻反模式

- [offerunk-sold-as-crash](offerunk-sold-as-crash.md) 是 OfferSnapshot 结果枚举余量 bundled（402），不是本页 item 2 单句边界。
- [offerunk-notcrash-sold-as-bundled](offerunk-notcrash-sold-as-bundled.md) 是 UNKNOWN 单句边界（725 item 1），不是本页 ACCEPT 边界。
