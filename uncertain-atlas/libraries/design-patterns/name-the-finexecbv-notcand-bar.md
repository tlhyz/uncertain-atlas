# 模式：把 FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（466 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**例**：[FinalizeBlock When Application executes block v not apply candidate / Process already ran ≠ bundled（466）](../../tracks/implementation/worked-example-finexecbv-notcand-vs-bundled.md)。

## 三个名字

1. **executes block v not Process already ran / apply candidate 不是 FinalizeBlock When Application executes block v bundled：** 看见 execute according to txs / Application executes block _v_ 不是已经 Process 跑过就不执行 interchangeable，不是 466 finexecbv interchangeable / 573 not persist interchangeable / 362 +2/3 precommit interchangeable。
2. **executes block v not apply candidate / Process already ran 不是 apply candidate state not ExecuteTxState bundled：** 看见 may apply candidate 不是已经 ExecuteTxState / previously executed interchangeable，不是 584 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable / 408 Process whole block interchangeable。
3. **executes block v not Process already ran / apply candidate 不是 351 Process also on proposer：** 看见 Application executes block _v_ 不是已经 Process 也会在提议者那边叫 interchangeable，不是 351 Process also on proposer interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。

## 为什么要分开叫

官方把 Application executes block _v_、execute according to txs、may apply a candidate state from previous Prepare or Process 写成三个名字。把它们叫成一个「看见 Application executes block _v_ 就已经 Process 跑过就不执行 interchangeable / 已经 466 finexecbv bundled interchangeable / 已经 584 apply candidate interchangeable」，会把 not Process already ran、not apply candidate / ExecuteTxState、not 351 Process also on proposer 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not apply candidate / Process already ran 正式三事（466 余量），先数清问的是 executes block v 是不是 already Process already ran / no need to execute、是不是 already apply candidate / ExecuteTxState、是不是 already Process also on proposer means ran Process，再决定要不要同一次发布。
