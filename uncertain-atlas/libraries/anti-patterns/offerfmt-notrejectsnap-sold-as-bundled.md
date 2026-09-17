# 反模式：把 OfferSnapshot Result REJECT_FORMAT not REJECT_SNAPSHOT / not already complete / not Offer REJECT 正式三事（400 余量） 说成已经是拒掉这份 / 已经齐 / 已经 Offer REJECT

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[REJECT_FORMAT ≠ bundled（400）](../../tracks/implementation/worked-example-offerfmt-notrejectsnap-vs-bundled.md)。

## 卖法

把 OfferSnapshot Result 这句写成已经已经是拒掉这份 / 已经齐 / 已经 Offer REJECT interchangeable，或已经和 400 offerfmt-vs-rejectsnap bundled / offerfmt-notrejectsnap-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER / ABORT 三条核心句写成三件独立的实现事。把它们卖成已经是拒掉这份 / 已经齐 / 已经 Offer REJECT，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT_FORMAT 正式三事（400 余量），必须分开 not REJECT_SNAPSHOT、not already complete、not Offer REJECT 三件事，不要和 400 / 398 / 402 / 723 / 724 糊成一句。

## 和相邻反模式

- [offerfmt-sold-as-rejectsnap](offerfmt-sold-as-rejectsnap.md) 是 OfferSnapshot 结果枚举 bundled（400），不是本页 item 1 单句边界。
- [offerfmt-notsenders-sold-as-bundled](offerfmt-notsenders-sold-as-bundled.md) 是 REJECT_SENDER 单句边界（723 item 2），不是本页 REJECT_FORMAT 边界。
