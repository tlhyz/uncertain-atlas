# 模式：把 FinalizeBlock When Application executes block v 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**例**：[FinalizeBlock When Application executes block v ≠ bundled](../../tracks/implementation/worked-example-finexecbv-bundled.md)。

## 三个名字

1. **Application executes block v 不是 persist decision / When calling guarantee：** 看见 When 第 3 步 executes block _v_ 不是已经 persist decision interchangeable，不是 472 finwhen interchangeable / 572 not execbv interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable。
2. **Application executes block v 不是 Process already ran / apply candidate：** 看见 executes block _v_ 不是已经 Process 跑过就不执行 interchangeable，不是 584 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable / 351 Process also on proposer interchangeable。
3. **Application executes block v 不是 +2/3 precommit decided / ResultHash：** 看见 Application executes block _v_ 不是已经 +2/3 precommit decided interchangeable，不是 362 +2/3 precommit interchangeable / 335 finpersist interchangeable / 147 apphash vs this block interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock When 第 3 步 Application executes block _v_、Usage 里 execute according to txs / may apply candidate、When 流程 +2/3 precommit 决定 / ResultHash 写成三个名字。把它们叫成一个「看见 Application executes block _v_ 就已经 persist decision interchangeable / 已经 apply candidate interchangeable / 已经 ResultHash interchangeable」，会把 not persist decision / When calling guarantee、not apply candidate / Process already ran、not +2/3 precommit decided / ResultHash 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v，先数清问的是 executes block v 是不是 already persist decision / When calling guarantee、是不是 already Process already ran / apply candidate、是不是 already +2/3 precommit decided / ResultHash，再决定要不要同一次发布。
