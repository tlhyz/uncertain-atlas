# 模式：把 ProposalStatus REJECT prevote nil not can change later / not already not in block / not VerifyStatus REJECT 正式三事（376 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[REJECT ≠ bundled（376）](../../tracks/implementation/worked-example-propstat-notreject-vs-bundled.md)。

## 三个名字

1. **REJECT prevote nil 不是已经能稍后改裁决：** 看见回了 REJECT，不是已经 354 interchangeable / 715 propstat-notreject interchangeable。
2. **看见回了 REJECT 不是已经没进块：** 看见发了 nil，不是已经没进块 interchangeable。
3. **看见发了 nil 不是 VerifyStatus REJECT：** 看见 Process REJECT，不是已经 434 / 455 interchangeable。

官方把 ProposalStatus 三条核心句拆成三个名字。把它们叫成一个「看见回了 ProposalStatus 就已经是四门已经结算」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus REJECT 正式三事（376 余量），先数清问的是 REJECT 是不是已经能稍后改裁决 / 354、是不是已经没进块、还是看见发了 nil 是不是 Verify REJECT / 434 / 455，再决定要不要同一次发布。376 proposalstatus vs prevote bundled unbundling 在本页 item 3 完成。
