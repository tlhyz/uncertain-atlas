# 模式：把 FinalizeBlock equiv ABCI 1.0 not no Prepare/Process 正式三事（586 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock equiv not no Prepare/Process ≠ bundled（586）](../../tracks/implementation/worked-example-finequiv-notnoprep-vs-bundled.md)。

## 三个名字

1. **equiv not no Prepare/Process 不是 finequiv bundled：** 看见收成一门不是已经没有 Prepare/Process interchangeable，不是 586 finequiv interchangeable / 602 notgates interchangeable / 600 notgates item 3 interchangeable / 351 Process also on proposer interchangeable。
2. **equiv not CheckTx skip Prepare/Process 不是 validValue / Process Accept：** 看见收成一门不是已经 CheckTx 过了就可以跳过 Prepare/Process interchangeable，不是 356 validvalue interchangeable / 339 CheckTx weak filter interchangeable / 354 processwhen later interchangeable。
3. **equiv not no Prepare/Process 不是 Contains newly decided：** 看见等价不是已经 finequiv bundled interchangeable，不是 586 item 3 Contains newly decided interchangeable / 460 fincand interchangeable / 461 finnewfields interchangeable / 595 notcand interchangeable。

## 为什么要分开叫

官方把 equiv 收成一门、仍保留 Prepare/Process、586 finequiv bundled 三事 写成三个名字。把它们叫成一个「看见收成一门 就已经没有 Prepare/Process / 已经 CheckTx 过了就可以跳过 Prepare/Process / 已经 finequiv bundled interchangeable」，会把 not no Prepare/Process、not CheckTx skip Prepare/Process、not Contains newly decided / apply candidate 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock equiv ABCI 1.0 not no Prepare/Process 正式三事（586 余量），先数清问的是 equiv 是不是 already no Prepare/Process / 351 / 373、是不是 already CheckTx skip Prepare/Process / 356 / 339，还是 equiv 是不是 already finequiv bundled / 586 item 3 / 460 / 461，再决定要不要同一次发布。
