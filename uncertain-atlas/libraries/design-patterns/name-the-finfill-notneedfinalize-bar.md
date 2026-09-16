# 模式：把 FinalizeBlock fill all fields not already don't need Finalize 正式三事（473 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock fill all fields not already don't need Finalize ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notneedfinalize-vs-bundled.md)。

## 三个名字

1. **will fill up all fields not already don't need Finalize 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled：** 看见 will fill up all fields 不是已经 Prepare/Process 给过就不用再 Finalize，不是 473 bundled interchangeable / 363 fill all fields interchangeable / 465 ABCI equiv interchangeable。
2. **will fill up all fields not already committed 不是 460 apply candidate：** 看见引擎填齐不是已经 Finalize + Commit 交差，不是 473 bundled interchangeable / 460 apply candidate interchangeable / 452 candidate interchangeable。
3. **will fill up all fields not Contains bundled interchangeable 不是 461 newly decided bundled：** 看见 will fill up 不是已经 Contains newly decided block fields bundled interchangeable，不是 473 bundled interchangeable / 461 bundled interchangeable / 474 bundled interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock fill all fields not already don't need Finalize 写成三个名字。把它们叫成一个「看见 will fill up all fields 就已经 Prepare/Process 给过就不用再 Finalize / 已经交差 interchangeable」，会把 not don't need Finalize、not already committed、not Contains bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not already don't need Finalize 正式三事（473 余量），先数清问的是 will fill up all fields 是不是 already don't need Finalize、will fill up all fields 是不是 already committed、will fill up all fields 是不是 Contains bundled interchangeable，再决定要不要同一次发布。
