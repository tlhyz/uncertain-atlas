# 模式：把 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock fill all fields not passed means ran Process ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notpassedran-vs-bundled.md)。

## 三个名字

1. **even if passed not field names match means ran Process 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled：** 看见 even if passed 不是已经字段名对得上就代表已经跑过 Process，不是 473 bundled interchangeable / 359 Prepare 同一套字段 interchangeable / 360 Process guarantee interchangeable。
2. **even if passed not newly decided/proposed interchangeable 不是 556 not ProcessProposal full info：** 看见 even if passed 不是已经 newly decided 和 proposed interchangeable，不是 473 bundled interchangeable / 556 not ProcessProposal full info interchangeable / 565 not proposed block interchangeable。
3. **even if passed not previously executed interchangeable 不是 460 apply candidate：** 看见 even if passed 不是已经 previously executed / 套用候选 interchangeable，不是 473 bundled interchangeable / 460 apply candidate interchangeable / 546 not already executed interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock fill all fields not passed means ran Process 写成三个名字。把它们叫成一个「看见 even if passed 就已经字段名对得上就代表已经跑过 Process / newly decided 和 proposed interchangeable / previously executed interchangeable」，会把 not field names match、not newly decided/proposed、not previously executed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not passed means ran Process 正式三事（473 余量），先数清问的是 even if passed 是不是 field names match means ran Process、even if passed 是不是 newly decided/proposed interchangeable、even if passed 是不是 previously executed interchangeable，再决定要不要同一次发布。
