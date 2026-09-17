# 模式：把 OfferSnapshot Result REJECT_FORMAT not REJECT_SNAPSHOT / not already complete / not Offer REJECT 正式三事（400 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[REJECT_FORMAT ≠ bundled（400）](../../tracks/implementation/worked-example-offerfmt-notrejectsnap-vs-bundled.md)。

## 三个名字

1. **REJECT_FORMAT 不是已经拒掉这份：** 看见回了 REJECT_FORMAT，不是已经 398 / 721 interchangeable / 722 offerfmt-notrejectsnap interchangeable。
2. **看见回了 REJECT_FORMAT 不是已经齐：** 看见能换一份，不是已经齐 interchangeable。
3. **看见能换一份 不是 Offer REJECT：** 看见 REJECT_FORMAT，不是已经 402 interchangeable。

官方把 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER / ABORT 三条核心句拆成三个名字。把它们叫成一个「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT_FORMAT 正式三事（400 余量），先数清问的是 REJECT_FORMAT 是不是已经拒掉这份 / 398 / 721、是不是已经齐、还是看见能换一份是不是 402，再决定要不要同一次发布。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 1 启动。
