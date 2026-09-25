# 模式：把 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事（376 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[回了 ACCEPT not already settled ≠ bundled（376）](../../tracks/implementation/worked-example-proposalstatus-notsettled-vs-bundled.md)。

## 三个名字

1. **回了 ACCEPT 不是 already settled：** 看见回了 ACCEPT / ACCEPT 表示应用认为提案合法、共识会发 Prevote / 回了 ACCEPT 状态，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable。

2. **会发 Prevote 不是 already mustaccept：** 看见会发 Prevote / 共识会发 Prevote / 发了 Prevote，不是已经必须 Accept interchangeable / 已经 mustaccept interchangeable / 已经必须 Accept 交差 interchangeable，不是 347 must Accept interchangeable / 875 proposalstatus-notfourgates interchangeable。

3. **合法 不是 already fourgates：** 看见合法 / 应用认为提案合法 / 合法状态，不是已经过了四门 interchangeable / 已经 fourgates interchangeable / 已经过了四门交差 interchangeable，不是 33 four gates interchangeable / 376 proposalstatus item 3 interchangeable。

官方把回了 ACCEPT、不是已经必须 Accept、不是已经过了四门写成三个名字。把它们叫成一个「看见回了 ACCEPT 就已经交差 interchangeable / 就已经必须 Accept interchangeable / 就已经过了四门 interchangeable」，会把 not already settled、not already mustaccept、not already fourgates 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事（376 余量），先数清问的是回了 ACCEPT 是不是 already settled / 376 / proposalstatus-sold-as-prevote，是不是会发 Prevote 是不是 already mustaccept，还是合法 是不是 already fourgates，再决定要不要同一次发布。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 2 续。
