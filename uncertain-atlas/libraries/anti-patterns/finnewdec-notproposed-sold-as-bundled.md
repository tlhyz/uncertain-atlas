# 反模式：把 FinalizeBlock newly decided block not proposed block 正式三事（474 余量）卖成 FinalizeBlock Contains newly decided block fields bundled / ProcessProposal 含执行所需全部信息 / proposed block 字段

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock newly decided block not proposed block ≠ bundled（474）](../../tracks/implementation/worked-example-finnewdec-notproposed-vs-bundled.md)。

## 卖法

- 「看见 newly decided block / 看见刚决定那块 就已经 proposed block interchangeable / 已经 ProcessProposal 含执行所需全部信息 interchangeable。」
- 「看见 newly decided block 就已经 ProcessProposalRequest.proposed_last_commit interchangeable / 已经 proposed 对象 interchangeable。」
- 「看见 newly decided block 就已经只有 raw proposal / PrepareProposalResponse.txs interchangeable。」

## 为什么错

官方把 newly decided block 对象、ProcessProposal Contains all information on the proposed block needed to fully execute it、ProcessProposalRequest 拟议块字段写成三件独立的实现事。把它们卖成 FinalizeBlock Contains newly decided block fields bundled、ProcessProposal 含执行所需全部信息、proposed block 字段，会把 newly decided not proposed、newly decided not proposed_last_commit、newly decided not raw proposal enough 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock newly decided block not proposed block 正式三事（474 余量），必须分开 newly decided not proposed block、newly decided not proposed_last_commit from proposed block、newly decided not only raw proposal enough 三个名字，不要把它们卖成 FinalizeBlock Contains newly decided block fields bundled / ProcessProposal 含执行所需全部信息 / proposed block 字段。

## 和相邻反模式

- [finnewdec-sold-as-settled](finnewdec-sold-as-settled.md) 是 474 bundled 三事专用，不是本页 newly decided not proposed 单句边界。
- [finnewdec-notsettled-sold-as-bundled](finnewdec-notsettled-sold-as-bundled.md) 是 564 Contains not settled，不是本页 newly decided vs proposed 边界。
- [finnewfields-notprocfull-sold-as-bundled](finnewfields-notprocfull-sold-as-bundled.md) 是 556 461 bundled item 2 余量，不是本页 474 bundled item 2 边界。
