# 模式：把 OfferSnapshot Result REJECT not REJECT_FORMAT / not REJECT_SNAPSHOT / not already complete 正式三事（402 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[REJECT ≠ bundled（402）](../../tracks/implementation/worked-example-offerunk-notformat-vs-bundled.md)。

## 三个名字

1. **REJECT 不是已经拒掉这种 format：** 看见回了 REJECT，不是已经 400 / 722 interchangeable / 727 offerunk-notformat interchangeable。
2. **看见回了 REJECT 不是已经 REJECT_SNAPSHOT：** 看见能换一份，不是已经 398 / 721 interchangeable。
3. **看见能换一份 不是已经齐：** 看见 REJECT，不是已经齐 interchangeable。

官方把 OfferSnapshot Result UNKNOWN / ACCEPT / REJECT 三条核心句拆成三个名字。把它们叫成一个「看见回了 OfferSnapshot 结果枚举余量就已经崩」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT 正式三事（402 余量），先数清问的是 REJECT 是不是已经拒掉这种 format / 400 / 722、是不是已经 REJECT_SNAPSHOT / 398 / 721、还是看见能换一份是不是已经齐，再决定要不要同一次发布。402 offerunk vs crash bundled unbundling 在本页 item 3 完成。
