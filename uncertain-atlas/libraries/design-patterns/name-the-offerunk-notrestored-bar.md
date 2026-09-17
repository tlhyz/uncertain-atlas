# 模式：把 OfferSnapshot Result ACCEPT not restored / not already complete / not ProposalStatus ACCEPT 正式三事（402 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**例**：[ACCEPT ≠ bundled（402）](../../tracks/implementation/worked-example-offerunk-notrestored-vs-bundled.md)。

## 三个名字

1. **ACCEPT 不是已经装完：** 看见回了 ACCEPT，不是已经 401 interchangeable / 726 offerunk-notrestored interchangeable。
2. **看见回了 ACCEPT 不是已经齐：** 看见开始装块，不是已经 321 interchangeable。
3. **看见开始装块 不是 Process ACCEPT：** 看见 ACCEPT，不是已经 376 / 714 interchangeable。

官方把 OfferSnapshot Result UNKNOWN / ACCEPT / REJECT 三条核心句拆成三个名字。把它们叫成一个「看见回了 OfferSnapshot 结果枚举余量就已经崩」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result ACCEPT 正式三事（402 余量），先数清问的是 ACCEPT 是不是已经装完 / 401、是不是已经齐 / 321、还是看见开始装块是不是 376 / 714，再决定要不要同一次发布。402 offerunk vs crash bundled unbundling 在本页 item 2 续。
