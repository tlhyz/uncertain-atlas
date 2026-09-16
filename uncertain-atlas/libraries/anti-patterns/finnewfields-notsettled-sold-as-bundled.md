# 反模式：把 FinalizeBlock Contains newly decided block fields not already settled 正式三事卖成 FinalizeBlock 含刚决定那块字段 bundled / 已经四门已经结算 / 已经跑过 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock Contains newly decided block fields not already settled ≠ bundled](../../tracks/implementation/worked-example-finnewfields-notsettled-vs-bundled.md)。

## 卖法

- 「看见 FinalizeBlock Contains the fields of the newly decided block / 看见含刚决定那块的字段 就已经四门已经结算 interchangeable / 已经 ABCI 1.0 三步 interchangeable / 已经 FinalizeBlock 含刚决定那块字段 bundled interchangeable。」
- 「看见 newly decided block 就已经跑过 Process interchangeable / 已经 Prepare / Process 同一套字段 interchangeable / 已经 Finalize 时的 Process 保证 interchangeable。」
- 「看见含刚决定那块的字段 就已经 Process 回了 Accept 就换工作状态 interchangeable / 已经 candidate not committed interchangeable / 已经 ProcessProposal 候选执行 interchangeable。」

## 为什么错

官方把 Contains the fields of the newly decided block、Process 调用之前就已经跑过 Process、Process 回了 Accept 就换工作状态写成三件独立的实现事。把它们卖成 FinalizeBlock 含刚决定那块字段 bundled、已经四门已经结算、已经跑过 Process，会把 Contains newly decided not settled、Contains newly decided not ran Process、Contains newly decided not ACCEPT switched 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Contains newly decided block fields not already settled 正式三事，必须分开 Contains newly decided block fields not already four gates settled、Contains newly decided block fields not already ran Process、Contains newly decided block fields not Process ACCEPT switched working state 三个名字，不要把它们卖成 FinalizeBlock 含刚决定那块字段 bundled / 已经四门已经结算 / 已经跑过 Process。

## 和相邻反模式

- [finnewfields-sold-as-settled](finnewfields-sold-as-settled.md) 是 461 bundled 三事专用，不是本页 Contains newly decided block fields not already settled 单句边界。
- [finnewdec-sold-as-settled](finnewdec-sold-as-settled.md) 是 474 Contains newly decided bundled，不是本页 not already four gates settled 边界。
- [procfull-notexecuted-sold-as-bundled](procfull-notexecuted-sold-as-bundled.md) 是 Process Contains all information not already executed，不是本页 Contains newly decided not ran Process 边界。
