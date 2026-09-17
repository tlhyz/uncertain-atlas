# 模式：把 FinalizeBlock When persist decision not executes block v / 已经交差 正式三事（478 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When step 1。  
**例**：[FinalizeBlock When persist decision not executes block v ≠ bundled（478）](../../tracks/implementation/worked-example-finpersist-notpersist-vs-bundled.md)。

## 三个名字

1. **persist decision 不是 executes block v：** 看见 persists _v_ as the decision for height _h_ 不是已经 Application executes block _v_ interchangeable，不是 466 executes block v interchangeable / 572 not execbv interchangeable / 584 apply candidate interchangeable。
2. **persist decision 不是 已经交差 / persist outputs：** 看见 persist decision 不是已经 Finalize + Commit 交差 interchangeable，不是 33 four gates interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable / 601 notsettled interchangeable。
3. **persist decision 不是 finpersist bundled：** 看见 persist decision 不是已经 finpersist bundled interchangeable，不是 478 item 2 calls FinalizeBlock interchangeable / 478 item 3 synchronous call interchangeable / 362 +2/3 precommit interchangeable / 602 notgates interchangeable。

## 为什么要分开叫

官方把 persist _v_ as decision、calls FinalizeBlock、synchronous call 和 executes block v、Finalize + Commit 交差、decides trigger 写成三个名字。把它们叫成一个「看见 persist decision 就已经 executes block v、已经交差、已经 finpersist bundled interchangeable」，会把 not executes block v、not 交差、not finpersist bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When persist decision not executes block v / 已经交差 正式三事（478 余量），先数清问的是 persist decision 是不是 already executes block v / 466 / 572，是不是 already 交差 / 33 / 587，还是 persist decision 是不是 already finpersist bundled / 478 item 2 / 478 item 3 / 362，再决定要不要同一次发布。
