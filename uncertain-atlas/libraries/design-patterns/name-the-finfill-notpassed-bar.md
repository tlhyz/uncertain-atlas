# 模式：把 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock fill all fields not passed means ran Process ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notpassed-vs-bundled.md)。

## 三个名字

1. **even if passed not field names match means ran Process 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled：** 看见 even if already passed 不是已经跑过 Process，不是 473 finfill interchangeable / 583 not refill interchangeable / 360 bundled interchangeable。
2. **even if passed not Prepare/Process/Finalize same fields 不是 359 same fields：** 看见字段名对得上 不是已经 Prepare/Process/Finalize same fields interchangeable，不是 359 same fields interchangeable / 473 finfill interchangeable。
3. **even if passed not Process also on proposer 不是 351 Process also on proposer：** 看见 Prepare / Process 已经传过 不是已经提议者 Process 过就代表已经跑过 Process，不是 351 Process also on proposer interchangeable / 582 not every validator interchangeable。

## 为什么要分开叫

官方把 even if already passed via PrepareProposalRequest or ProcessProposalRequest 写成三个名字。把它们叫成一个「看见 Prepare / Process 已经传过就已经跑过 Process interchangeable / 已经字段名对得上 interchangeable / 已经 Prepare/Process passed interchangeable」，会把 not field names match、not same fields、not Process also on proposer 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量），先数清问的是 even if passed 是不是 already field names match means ran Process、even if passed 是不是 already Prepare/Process/Finalize same fields、even if passed 是不是 already Process also on proposer means ran Process，再决定要不要同一次发布。
