# 反模式：把 FinalizeBlock 含刚决定那块字段正式三事说成已经四门已经结算

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[Contains the fields of the newly decided block ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finnewfields-vs-gates.md)。

## 错在哪里

把 Contains the fields of the newly decided block 写成已经是四门已经结算，或已经跑过 Process；把 newly decided block 的字段 写成已经是 ProcessProposal Contains all information needed to fully execute it，或已经是 ProcessProposalRequest 拟议块字段 interchangeable；把 CometBFT will fill up all fields even if already passed via Prepare/Process 写成已经 decided_last_commit 和 proposed_last_commit 就可以混用，或已经和 407 / 422 / 453 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock 含刚决定那块字段正式三事，必须分开 Contains the fields of the newly decided block、newly decided block 的字段、全部字段填齐即使 Prepare/Process 已经传过三件事，不要和 407 / 422 / 453 / 363 糊成一句。
