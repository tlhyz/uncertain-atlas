# 反模式：把 FinalizeBlock newly decided block fields not ProcessProposal contains all information 正式三事卖成 FinalizeBlock 含刚决定那块字段 bundled / 已经 ProcessProposal 含执行所需全部信息 / 已经 proposed block 字段 interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock newly decided block fields not ProcessProposal contains all information ≠ bundled](../../tracks/implementation/worked-example-finnewfields-notprocfull-vs-bundled.md)。

## 卖法

- 「看见 newly decided block 的字段 / 看见有刚决定那块 就已经 ProcessProposal Contains all information on the proposed block needed to fully execute it interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable / 已经 FinalizeBlock 含刚决定那块字段 bundled interchangeable。」
- 「看见 decided block 就已经 ProcessProposalRequest.proposed_last_commit interchangeable / 已经 proposed_last_commit 和 decided_last_commit 就可以混用 interchangeable / 已经 proposed 对象 interchangeable。」
- 「看见有刚决定那块 就已经只有 PrepareProposalResponse.txs 那种 raw proposal 就够 interchangeable / 已经 only raw proposal interchangeable / 已经 Request 八栏齐 interchangeable。」

## 为什么错

官方把 newly decided block 的字段、ProcessProposal 拟议块上执行所需全部信息、ProcessProposalRequest 拟议块字段写成三件独立的实现事。把它们卖成 FinalizeBlock 含刚决定那块字段 bundled、已经 ProcessProposal 含执行所需全部信息、已经 proposed block 字段 interchangeable，会把 newly decided vs Process contains all information、newly decided vs proposed/decided、newly decided vs raw proposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock newly decided block fields not ProcessProposal contains all information 正式三事，必须分开 newly decided block fields not ProcessProposal contains all information、newly decided block fields not proposed/decided interchangeable、newly decided block fields not only raw proposal enough 三个名字，不要把它们卖成 FinalizeBlock 含刚决定那块字段 bundled / 已经 ProcessProposal 含执行所需全部信息 / 已经 proposed block 字段 interchangeable。

## 和相邻反模式

- [finnewfields-sold-as-settled](finnewfields-sold-as-settled.md) 是 461 bundled 三事专用，不是本页 newly decided block fields not ProcessProposal contains all information 单句边界。
- [procfull-notfinfields-sold-as-bundled](procfull-notfinfields-sold-as-bundled.md) 是 Process Contains all information not Finalize fields，不是本页 Finalize newly decided vs Process 边界。
- [finnewfields-notsettled-sold-as-bundled](finnewfields-notsettled-sold-as-bundled.md) 是 Contains newly decided not already settled，不是本页 newly decided vs proposed 对象边界。
