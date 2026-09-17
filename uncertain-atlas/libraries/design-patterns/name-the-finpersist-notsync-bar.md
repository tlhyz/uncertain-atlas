# 模式：把 FinalizeBlock When synchronous call not decides trigger / Process sync 正式三事（478 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 2。  
**例**：[FinalizeBlock When synchronous call not decides trigger ≠ bundled（478）](../../tracks/implementation/worked-example-finpersist-notsync-vs-bundled.md)。

## 三个名字

1. **synchronous call 不是 Process sync / 异步：** 看见 The call is synchronous 不是已经 ProcessProposal 同步 interchangeable，不是 354 processwhen synchronous interchangeable / 354 Process 同步 interchangeable / 338 Prepare nondet interchangeable。
2. **synchronous call 不是 decides trigger：** 看见 synchronous call 不是已经 +2/3 precommit 决定 interchangeable，不是 362 finwhen interchangeable / 479 fintrigger interchangeable / 362 +2/3 precommit interchangeable / 606 notoutputs interchangeable。
3. **synchronous call 不是 finpersist bundled：** 看见 The call is synchronous 不是已经 finpersist bundled interchangeable，不是 605 notpersist interchangeable / 606 notoutputs interchangeable / 478 item 1 persist decision interchangeable / 478 item 2 calls FinalizeBlock interchangeable。

## 为什么要分开叫

官方把 persist decision、calls FinalizeBlock、synchronous call 和 executes block v、persist outputs、+2/3 precommit 决定、Process 同步 写成三个名字。把它们叫成一个「看见 synchronous call 就已经 Process 同步、已经 +2/3 precommit 决定 interchangeable、已经 finpersist bundled interchangeable」，会把 not Process sync、not decides trigger、not finpersist bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When synchronous call not decides trigger / Process sync 正式三事（478 余量），先数清问的是 synchronous call 是不是 already Process 同步 / 354，是不是 already +2/3 precommit 决定 / 362 / 479，还是 synchronous call 是不是 already finpersist bundled / 605 / 606，再决定要不要同一次发布。
