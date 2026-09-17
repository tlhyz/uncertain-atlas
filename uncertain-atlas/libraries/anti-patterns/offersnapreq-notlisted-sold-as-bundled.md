# 反模式：把 OfferSnapshot 请求 snapshot not local list / not already identical / not already settled 正式三事（396 余量） 说成已经是本地清单 / 已经是同一份 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[OfferSnapshot ≠ bundled（396）](../../tracks/implementation/worked-example-offersnapreq-notlisted-vs-bundled.md)。

## 卖法

把 OfferSnapshot 请求这句写成已经已经是本地清单 / 已经是同一份 / 已经交差 interchangeable，或已经和 396 offersnap-vs-listed bundled / offersnapreq-notlisted-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot 请求 snapshot / 回包 result / 引导时叫三条核心句写成三件独立的实现事。把它们卖成已经是本地清单 / 已经是同一份 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot 请求 snapshot 正式三事（396 余量），必须分开 not local list、not already identical、not already settled 三件事，不要和 396 / 395 / 735 / 368 / 738 / 739 糊成一句。

## 和相邻反模式

- [offersnap-sold-as-listed](offersnap-sold-as-listed.md) 是 OfferSnapshot 请求 bundled（396），不是本页 item 1 单句边界。
- [offersnapreq-notrestored-sold-as-bundled](offersnapreq-notrestored-sold-as-bundled.md) 是回包 result 单句边界（738 item 2），不是本页 snapshot 边界。
