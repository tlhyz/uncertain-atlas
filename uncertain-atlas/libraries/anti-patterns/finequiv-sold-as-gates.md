# 反模式：把 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事说成已经是四门已经结算

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[等价于 ABCI 1.0 那三步 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finequiv-vs-abci1.md)。

## 错在哪里

把 FinalizeBlock 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock` 写成已经是四门已经结算，或已经交差；把收成一门写成已经没有 Prepare/Process，或已经 ABCI++ 只剩 Finalize interchangeable；把等价于旧三步写成已经是 Contains the fields of the newly decided block，或已经 Process 跑过 / 已经有 candidate 就不用在 Finalize 再执行，或已经和 363 / 33 / 461 / 460 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事，必须分开 equiv、仍保留 Prepare/Process、Finalize 仍要执行三件事，不要和 363 / 33 / 461 / 460 糊成一句。
