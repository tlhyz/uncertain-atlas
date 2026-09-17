# 模式：把 OfferSnapshot 回包 result not already restored / not already accepted / not already settled 正式三事（396 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot。  
**例**：[OfferSnapshot ≠ bundled（396）](../../tracks/implementation/worked-example-offersnapreq-notrestored-vs-bundled.md)。

## 三个名字

1. **result 不是已经装完：** 看见回了 result，不是已经 321 interchangeable / 738 offersnapreq-notrestored interchangeable。
2. **看见回了 result 不是已经收下：** 看见有结果，不是已经 402 / 726 / 401 / 728 interchangeable。
3. **看见能回 不是已经交差：** 看见 result，不是已经交差 interchangeable。

官方把 OfferSnapshot 请求 snapshot / 回包 result / 引导时叫三条核心句拆成三个名字。把它们叫成一个「看见填了 OfferSnapshot 请求就已经是本地清单」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot 回包 result 正式三事（396 余量），先数清问的是 result 是不是已经装完 / 321、是不是已经收下 / 402 / 401、还是看见能回是不是已经交差，再决定要不要同一次发布。396 offersnap vs listed bundled unbundling 在本页 item 2 续。
