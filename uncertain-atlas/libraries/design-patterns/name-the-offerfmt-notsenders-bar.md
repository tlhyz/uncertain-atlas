# 模式：把 OfferSnapshot Result REJECT_SENDER not reject_senders regardless / not can continue / not chunk-response reject 正式三事（400 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[REJECT_SENDER ≠ bundled（400）](../../tracks/implementation/worked-example-offerfmt-notsenders-vs-bundled.md)。

## 三个名字

1. **REJECT_SENDER 不是已经不论 Result 都拒：** 看见回了 REJECT_SENDER，不是已经 378 interchangeable / 723 offerfmt-notsenders interchangeable。
2. **看见回了 REJECT_SENDER 不是已经能接着装：** 看见能换一份，不是已经能接着装 interchangeable。
3. **看见能换一份 不是 Usage chunk 回包拒掉：** 看见 REJECT_SENDER，不是已经 499 interchangeable。

官方把 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER / ABORT 三条核心句拆成三个名字。把它们叫成一个「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT_SENDER 正式三事（400 余量），先数清问的是 REJECT_SENDER 是不是已经不论 Result 都拒 / 378、是不是已经能接着装、还是看见能换一份是不是 499，再决定要不要同一次发布。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 2 续。
