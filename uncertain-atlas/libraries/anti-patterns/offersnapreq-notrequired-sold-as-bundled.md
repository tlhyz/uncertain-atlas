# 反模式：把 OfferSnapshot 引导时叫 not Snapshot Connection required / not already transitioned / not Usage bootstrap 正式三事（396 余量） 说成已经必须实现快照连接 / 已经切进共识 / 已经 Usage bootstrap

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[OfferSnapshot ≠ bundled（396）](../../tracks/implementation/worked-example-offersnapreq-notrequired-vs-bundled.md)。

## 卖法

把 OfferSnapshot 请求这句写成已经已经必须实现快照连接 / 已经切进共识 / 已经 Usage bootstrap interchangeable，或已经和 396 offersnap-vs-listed bundled / offersnapreq-notrequired-sold-as-bundled interchangeable。

## 为什么错

官方把 OfferSnapshot 请求 snapshot / 回包 result / 引导时叫三条核心句写成三件独立的实现事。把它们卖成已经必须实现快照连接 / 已经切进共识 / 已经 Usage bootstrap，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot 引导时叫 正式三事（396 余量），必须分开 not Snapshot Connection required、not already transitioned、not Usage bootstrap 三件事，不要和 396 / 334 / 323 / 499 / 647 / 737 / 738 糊成一句。

## 和相邻反模式

- [offersnap-sold-as-listed](offersnap-sold-as-listed.md) 是 OfferSnapshot 请求 bundled（396），不是本页 item 3 单句边界。
- [offersnapreq-notrestored-sold-as-bundled](offersnapreq-notrestored-sold-as-bundled.md) 是回包 result 单句边界（738 item 2），不是本页引导时叫边界。
