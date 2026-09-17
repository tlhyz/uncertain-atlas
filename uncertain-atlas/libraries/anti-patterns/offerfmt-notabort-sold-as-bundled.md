# 反模式：把 OfferSnapshot Result ABORT not switched / not restored / not UNKNOWN abort-all 正式三事（400 余量） 说成已经换一份就能接着装 / 已经装完 / 已经 UNKNOWN 中止全部装回

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ABORT ≠ bundled（400）](../../tracks/implementation/worked-example-offerfmt-notabort-vs-bundled.md)。

## 卖法

把 OfferSnapshot Result 这句写成已经已经换一份就能接着装 / 已经装完 / 已经 UNKNOWN 中止全部装回 interchangeable，或已经和 400 offerfmt-vs-rejectsnap bundled / offerfmt-notabort-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER / ABORT 三条核心句写成三件独立的实现事。把它们卖成已经换一份就能接着装 / 已经装完 / 已经 UNKNOWN 中止全部装回，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result ABORT 正式三事（400 余量），必须分开 not switched、not restored、not UNKNOWN abort-all 三件事，不要和 400 / 321 / 402 / 722 / 723 糊成一句。

## 和相邻反模式

- [offerfmt-sold-as-rejectsnap](offerfmt-sold-as-rejectsnap.md) 是 OfferSnapshot 结果枚举 bundled（400），不是本页 item 3 单句边界。
- [offerfmt-notsenders-sold-as-bundled](offerfmt-notsenders-sold-as-bundled.md) 是 REJECT_SENDER 单句边界（723 item 2），不是本页 ABORT 边界。
