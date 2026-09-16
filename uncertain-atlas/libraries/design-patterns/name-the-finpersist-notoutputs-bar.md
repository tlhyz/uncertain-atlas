# 模式：把 FinalizeBlock When calls FinalizeBlock not persist outputs / 362 decides trigger 正式三事（478 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 2。  
**例**：[FinalizeBlock When calls FinalizeBlock not persist outputs ≠ bundled（478）](../../tracks/implementation/worked-example-finpersist-notoutputs-vs-bundled.md)。

## 三个名字

1. **calls FinalizeBlock 不是 persist outputs：** 看见 calls FinalizeBlock with _v_'s data 不是已经 persist tx outputs / AppHash / ResultsHash interchangeable，不是 587 finreturn interchangeable / 467 finpersist interchangeable / 335 finpersist interchangeable / 316 ExecTxResult interchangeable。
2. **calls FinalizeBlock 不是 decides trigger：** 看见 with _v_'s data 不是已经 +2/3 precommit 决定 interchangeable，不是 362 finwhen interchangeable / 479 fintrigger interchangeable / 362 +2/3 precommit interchangeable / 605 notpersist interchangeable。
3. **calls FinalizeBlock 不是 finpersist bundled：** 看见 calls FinalizeBlock 不是已经 finpersist bundled interchangeable，不是 605 notpersist interchangeable / 478 item 1 persist decision interchangeable / 478 item 3 synchronous call interchangeable / 354 processwhen synchronous interchangeable。

## 为什么要分开叫

官方把 calls FinalizeBlock、synchronous call、persist decision 和 persist tx outputs / AppHash / ResultsHash、+2/3 precommit 决定、finpersist bundled 写成三个名字。把它们叫成一个「看见 calls FinalizeBlock 就已经 persist outputs、已经 +2/3 precommit 决定 interchangeable、已经 finpersist bundled interchangeable」，会把 not persist outputs、not decides trigger、not finpersist bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calls FinalizeBlock not persist outputs / 362 decides trigger 正式三事（478 余量），先数清问的是 calls FinalizeBlock 是不是 already persist outputs / 587 / 467，是不是 already +2/3 precommit 决定 / 362 / 479，还是 calls FinalizeBlock 是不是 already finpersist bundled / 605 / 478 item 3，再决定要不要同一次发布。
