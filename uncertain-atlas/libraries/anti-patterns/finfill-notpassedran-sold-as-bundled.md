# 反模式：把 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量）卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 字段名对得上就代表已经跑过 Process / newly decided 和 proposed interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[FinalizeBlock fill all fields not passed means ran Process ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notpassedran-vs-bundled.md)。

## 卖法

- 「看见 even if they were already passed on via PrepareProposalRequest or ProcessProposalRequest / 看见即使 Prepare / Process 已经传过 就已经字段名对得上就代表已经跑过 Process interchangeable。」
- 「看见 even if passed 就已经 newly decided block 的字段和 proposed block 字段 interchangeable / 已经 Prepare/Process 同一套字段 interchangeable。」
- 「看见 even if passed 就已经 previously executed interchangeable / 已经套用先前 candidate interchangeable。」

## 为什么错

官方把 even if they were already passed on via PrepareProposalRequest or ProcessProposalRequest、字段名对得上就代表已经跑过 Process、Prepare/Process 传过和 newly decided vs proposed 对象分开写成三件独立的实现事。把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled、字段名对得上就代表已经跑过 Process、newly decided 和 proposed interchangeable，会把 not field names match、not newly decided/proposed、not previously executed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量），必须分开 even if passed not field names match means ran Process、even if passed not newly decided/proposed interchangeable、even if passed not previously executed interchangeable 三个名字，不要把它们卖成 FinalizeBlock fill all fields even if Prepare/Process passed bundled / 字段名对得上就代表已经跑过 Process / newly decided 和 proposed interchangeable。

## 和相邻反模式

- [finfill-notneedfinalize-sold-as-bundled](finfill-notneedfinalize-sold-as-bundled.md) 是 567 473 item 1 余量，不是本页 even if passed 单句边界。
- [finnewfields-notdecprop-sold-as-bundled](finnewfields-notdecprop-sold-as-bundled.md) 是 557 461 bundled item 3 余量，不是本页 even if passed not newly decided/proposed 边界。
