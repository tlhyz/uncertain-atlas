# 模式：把 ProposalStatus ACCEPT prevote not settled / not must Accept / not four gates 正式三事（376 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[ACCEPT ≠ bundled（376）](../../tracks/implementation/worked-example-propstat-notaccept-vs-bundled.md)。

## 三个名字

1. **ACCEPT prevote 不是已经交差：** 看见会发 Prevote，不是已经交差 interchangeable / 714 propstat-notaccept interchangeable。
2. **看见回了 ACCEPT 不是 honest proposal 必须 Accept：** 看见会发 Prevote，不是已经 347 interchangeable。
3. **看见会发 Prevote 不是四门已经结算：** 看见 ACCEPT，不是已经 33 / 434 interchangeable。

官方把 ProposalStatus 三条核心句拆成三个名字。把它们叫成一个「看见回了 ProposalStatus 就已经是四门已经结算」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus ACCEPT 正式三事（376 余量），先数清问的是 ACCEPT 是不是已经交差、是不是 Req 3 必须 Accept / 347、还是看见会发 Prevote 是不是四门齐了 / 33，再决定要不要同一次发布。376 proposalstatus vs prevote bundled unbundling 在本页 item 2 续。
