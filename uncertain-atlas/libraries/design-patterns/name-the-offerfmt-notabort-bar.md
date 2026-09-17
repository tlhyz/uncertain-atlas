# 模式：把 OfferSnapshot Result ABORT not switched / not restored / not UNKNOWN abort-all 正式三事（400 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[ABORT ≠ bundled（400）](../../tracks/implementation/worked-example-offerfmt-notabort-vs-bundled.md)。

## 三个名字

1. **ABORT 不是已经换一份就能接着装：** 看见回了 ABORT，不是已经 321 interchangeable / 724 offerfmt-notabort interchangeable。
2. **看见回了 ABORT 不是已经装完：** 看见能中止，不是已经装完 interchangeable。
3. **看见能中止 不是 UNKNOWN 中止全部装回：** 看见 ABORT，不是已经 402 interchangeable。

官方把 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER / ABORT 三条核心句拆成三个名字。把它们叫成一个「看见回了 OfferSnapshot 结果枚举就已经是拒掉这份」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result ABORT 正式三事（400 余量），先数清问的是 ABORT 是不是已经换一份就能接着装 / 321、是不是已经装完、还是看见能中止是不是 402，再决定要不要同一次发布。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 3 完成。
