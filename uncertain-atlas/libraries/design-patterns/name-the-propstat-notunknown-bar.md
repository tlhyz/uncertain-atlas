# 模式：把 ProposalStatus UNKNOWN always wrong crash not four gates / not VerifyStatus UNKNOWN / not OfferSnapshot UNKNOWN 正式三事（376 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[UNKNOWN ≠ bundled（376）](../../tracks/implementation/worked-example-propstat-notunknown-vs-bundled.md)。

## 三个名字

1. **UNKNOWN crash 不是已经四门齐了：** 看见回了 UNKNOWN 会崩，不是已经 33 interchangeable / 713 propstat-notunknown interchangeable。
2. **看见回了 UNKNOWN 不是 VerifyStatus UNKNOWN：** 看见会崩，不是已经 434 interchangeable。
3. **看见崩了 不是 OfferSnapshot UNKNOWN 中止装回：** 看见 Process 回包会崩，不是已经 402 interchangeable。

官方把 ProposalStatus 三条核心句拆成三个名字。把它们叫成一个「看见回了 ProposalStatus 就已经是四门已经结算」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus UNKNOWN 正式三事（376 余量），先数清问的是 UNKNOWN 是不是已经四门齐了 / 33、是不是 VerifyStatus UNKNOWN / 434、还是看见崩了是不是 Offer UNKNOWN 中止装回 / 402，再决定要不要同一次发布。376 proposalstatus vs prevote bundled unbundling 在本页 item 1 启动。
