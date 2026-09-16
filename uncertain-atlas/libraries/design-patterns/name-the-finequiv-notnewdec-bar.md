# 模式：把 FinalizeBlock equiv ABCI 1.0 not Contains newly decided / apply candidate 正式三事（586 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock equiv not Contains newly decided / apply candidate ≠ bundled（586）](../../tracks/implementation/worked-example-finequiv-notnewdec-vs-bundled.md)。

## 三个名字

1. **equiv not Contains newly decided 不是 finnewfields / finnewdec bundled：** 看见收成一门不是已经 Contains the fields of the newly decided block interchangeable，不是 461 finnewfields interchangeable / 474 finnewdec interchangeable / 407 finfields interchangeable / 473 finfill interchangeable。
2. **equiv not apply candidate 不是 fincand / executes block v：** 看见收成一门不是已经 Process 跑过就不用在 Finalize 再执行 interchangeable，不是 460 fincand interchangeable / 466 executes block v interchangeable / 577 apply candidate interchangeable / 584 apply candidate interchangeable / 578 not no re-execute interchangeable。
3. **equiv not Contains newly decided / apply candidate 不是 finequiv bundled：** 看见等价不是已经 finequiv bundled interchangeable，不是 602 notgates interchangeable / 603 notnoprep interchangeable / 600 notgates item 3 interchangeable / 363 finresp interchangeable。

## 为什么要分开叫

官方把 equiv 收成一门、Contains the fields of the newly decided block、execute txs / apply candidate state 写成三个名字。把它们叫成一个「看见收成一门 就已经 Contains newly decided block fields / 已经 Process 跑过就不用在 Finalize 再执行 / 已经 finequiv bundled interchangeable」，会把 not Contains newly decided、not apply candidate / previously executed、not finequiv bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not Contains newly decided / apply candidate 正式三事（586 余量），先数清问的是 equiv 是不是 already Contains newly decided / 461 / 474，是不是 already Process 跑过就不用在 Finalize 再执行 / 460 / 466 / 577，还是 equiv 是不是 already finequiv bundled / 602 / 603 / 600 item 3，再决定要不要同一次发布。
