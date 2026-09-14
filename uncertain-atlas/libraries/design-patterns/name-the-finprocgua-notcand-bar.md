# 模式：把 apply candidate state not ExecuteTxState 正式三事（360 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[apply candidate state not ExecuteTxState ≠ bundled（360）](../../tracks/implementation/worked-example-finprocgua-notcand-vs-bundled.md)。

## 三个名字

1. **apply candidate not ExecuteTxState 不是 Finalize 时的 Process 保证 bundled：** 看见 may apply candidate 不是已经 ExecuteTxState，不是 360 bundled interchangeable / 311 candidate is ExecuteTxState interchangeable / 408 Process whole block interchangeable。
2. **apply candidate not same block already ran means no need to execute 不是 executes block v / Process already ran：** 看见 can apply candidate 不是已经 Process 跑过就不执行，不是 466 executes block v interchangeable / 351 Process also on proposer interchangeable。
3. **apply candidate not already committed 不是 finpersist / finfields bundled：** 看见套用候选 不是已经交差，不是 335 finpersist interchangeable / 407 finfields interchangeable / 583 refill interchangeable。

## 为什么要分开叫

官方把 may apply candidate / execute according to txs / reuse memory state 写成三个名字。把它们叫成一个「看见可以套用先前候选就已经是 ExecuteTxState interchangeable / 已经同一块先跑过 interchangeable / 已经交差 interchangeable」，会把 not ExecuteTxState、not same block already ran means no need to execute、not already committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 apply candidate state not ExecuteTxState 正式三事（360 余量），先数清问的是 apply candidate 是不是 already ExecuteTxState、是不是 already same block already ran means no need to execute、是不是 already committed，再决定要不要同一次发布。
