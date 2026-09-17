# 反模式：把 ProposalStatus UNKNOWN always wrong crash not four gates / not VerifyStatus UNKNOWN / not OfferSnapshot UNKNOWN 正式三事（376 余量） 说成已经是四门已经结算 / 已经是 VerifyStatus UNKNOWN / 已经是 Offer UNKNOWN 中止装回

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[UNKNOWN ≠ bundled（376）](../../tracks/implementation/worked-example-propstat-notunknown-vs-bundled.md)。

## 卖法

把 ProposalStatus 这句写成已经已经是四门已经结算 / 已经是 VerifyStatus UNKNOWN / 已经是 Offer UNKNOWN 中止装回 interchangeable，或已经和 376 proposalstatus-vs-prevote bundled / propstat-notunknown-sold-as-bundled interchangeable。

## 为什么错

官方把 ProposalStatus 三条核心句写成三件独立的实现事。把它们卖成已经是四门已经结算 / 已经是 VerifyStatus UNKNOWN / 已经是 Offer UNKNOWN 中止装回，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus UNKNOWN 正式三事（376 余量），必须分开 not four gates、not VerifyStatus UNKNOWN、not OfferSnapshot UNKNOWN 三件事，不要和 376 / 33 / 434 / 402 / 714 / 715 糊成一句。

## 和相邻反模式

- [proposalstatus-sold-as-prevote](proposalstatus-sold-as-prevote.md) 是 ProposalStatus bundled（376），不是本页 item 1 单句边界。
- [propstat-notaccept-sold-as-bundled](propstat-notaccept-sold-as-bundled.md) 是 ACCEPT 单句边界（714 item 2），不是本页 UNKNOWN 边界。
