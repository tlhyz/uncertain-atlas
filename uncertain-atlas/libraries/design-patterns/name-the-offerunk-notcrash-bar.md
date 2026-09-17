# 模式：把 OfferSnapshot Result UNKNOWN not ProposalStatus crash / not ABORT / not settled 正式三事（402 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[UNKNOWN ≠ bundled（402）](../../tracks/implementation/worked-example-offerunk-notcrash-vs-bundled.md)。

## 三个名字

1. **UNKNOWN 不是已经会崩：** 看见回了 UNKNOWN，不是已经 376 / 713 interchangeable / 725 offerunk-notcrash interchangeable。
2. **看见回了 UNKNOWN 不是已经 ABORT：** 看见能中止全部装回，不是已经 400 / 724 interchangeable。
3. **看见能中止全部装回 不是已经交差：** 看见 UNKNOWN，不是已经交差 interchangeable。

官方把 OfferSnapshot Result UNKNOWN / ACCEPT / REJECT 三条核心句拆成三个名字。把它们叫成一个「看见回了 OfferSnapshot 结果枚举余量就已经崩」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result UNKNOWN 正式三事（402 余量），先数清问的是 UNKNOWN 是不是已经会崩 / 376 / 713、是不是已经 ABORT / 400 / 724、还是看见能中止是不是已经交差，再决定要不要同一次发布。402 offerunk vs crash bundled unbundling 在本页 item 1 启动。
