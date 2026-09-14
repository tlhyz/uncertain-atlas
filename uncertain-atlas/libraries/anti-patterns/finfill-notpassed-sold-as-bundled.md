# 反模式：把 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量）卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经跑过 Process / 已经字段名对得上

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock fill all fields not passed means ran Process ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notpassed-vs-bundled.md)。

## 卖法

- 「看见 even if already passed via PrepareProposalRequest or ProcessProposalRequest 就已经 field names match means ran Process interchangeable / 已经 Prepare/Process passed interchangeable。」
- 「看见字段名对得上 就已经 Prepare 和 Process / Finalize 同一套字段 interchangeable / 359 same fields interchangeable。」
- 「看见 Prepare / Process 已经传过 就已经 Process 也会在提议者那边叫 interchangeable / 351 Process also on proposer interchangeable。」

## 为什么错

官方把 even if already passed、field names match、Prepare/Process/Finalize same fields 写成独立的实现事。把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled、已经跑过 Process、已经字段名对得上，会把 not field names match、not same fields、not Process also on proposer 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量），必须分开 not field names match means ran Process、not Prepare/Process/Finalize same fields、not Process also on proposer 三个名字，不要把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 已经跑过 Process / 已经字段名对得上。

## 和相邻反模式

- [finfill-sold-as-bundled](finfill-sold-as-bundled.md) 是 473 bundled 三事专用，不是本页 even if passed not field names match 单句边界。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 359 专用，不是本页 even if passed not same fields 单句边界。
