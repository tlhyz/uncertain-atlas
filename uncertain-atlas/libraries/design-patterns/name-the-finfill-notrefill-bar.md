# 模式：把 FinalizeBlock fill all fields not no need to provide again 正式三事（473 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock fill all fields not no need to provide again ≠ bundled（473）](../../tracks/implementation/worked-example-finfill-notrefill-vs-bundled.md)。

## 三个名字

1. **fill all fields not no need to provide again 不是 FinalizeBlock fill all fields even if Prepare/Process passed bundled：** 看见 will fill up all fields 不是已经不用再 Finalize，不是 473 finfill interchangeable / 583 not refill interchangeable / 568 not passed means ran Process interchangeable。
2. **fill all fields not no need to provide again 不是 Finalize 时的 Process 保证 bundled：** 看见再填一遍 不是已经 at least one ran Process / persist decision，不是 360 bundled interchangeable / 582 not every validator interchangeable / 584 apply candidate interchangeable。
3. **fill all fields not no need to provide again 不是 583 not refill：** 看见 Currently 不是已经 360 item 2 refill 单句 interchangeable，不是 583 not refill interchangeable / 407 finfields interchangeable / 566 not committed interchangeable。

## 为什么要分开叫

官方把 Currently, CometBFT will fill up all fields in FinalizeBlockRequest 写成三个名字。把它们叫成一个「看见 will fill up all fields 就已经不用再给 interchangeable / 已经 473 finfill bundled interchangeable / 已经 583 not refill interchangeable」，会把 not no need to provide again、not 360 bundled、not 583 not refill 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields not no need to provide again 正式三事（473 余量），先数清问的是 fill 是不是 already no need to provide again、fill 是不是 already Finalize 时的 Process 保证 bundled、fill 是不是 already 583 not refill，再决定要不要同一次发布。
