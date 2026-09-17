# 反模式：把 OfferSnapshot Result REJECT_SENDER not reject_senders regardless / not can continue / not chunk-response reject 正式三事（400 余量） 说成已经不论 Result 都拒 / 已经能接着装 / 已经 Usage chunk 回包拒掉

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[REJECT_SENDER ≠ bundled（400）](../../tracks/implementation/worked-example-offerfmt-notsenders-vs-bundled.md)。

## 卖法

把 OfferSnapshot Result 这句写成已经已经不论 Result 都拒 / 已经能接着装 / 已经 Usage chunk 回包拒掉 interchangeable，或已经和 400 offerfmt-vs-rejectsnap bundled / offerfmt-notsenders-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER / ABORT 三条核心句写成三件独立的实现事。把它们卖成已经不论 Result 都拒 / 已经能接着装 / 已经 Usage chunk 回包拒掉，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT_SENDER 正式三事（400 余量），必须分开 not reject_senders regardless、not can continue、not chunk-response reject 三件事，不要和 400 / 378 / 499 / 722 / 724 糊成一句。

## 和相邻反模式

- [offerfmt-sold-as-rejectsnap](offerfmt-sold-as-rejectsnap.md) 是 OfferSnapshot 结果枚举 bundled（400），不是本页 item 2 单句边界。
- [offerfmt-notrejectsnap-sold-as-bundled](offerfmt-notrejectsnap-sold-as-bundled.md) 是 REJECT_FORMAT 单句边界（722 item 1），不是本页 REJECT_SENDER 边界。
