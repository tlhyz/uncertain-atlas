# 模式：把 Finalize 含刚决定那块的字段 not already settled 正式三事（407 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**例**：[Finalize 含刚决定那块的字段 not already settled ≠ bundled（407）](../../tracks/implementation/worked-example-finfields-notsettled-vs-bundled.md)。

## 三个名字

1. **Finalize 含刚决定那块的字段 not already four gates settled 不是 Finalize 字段余量 bundled：** 看见填了字段不是已经四门已经结算，不是 407 bundled interchangeable / 465 ABCI equiv interchangeable / 363 fill all fields interchangeable。
2. **Finalize 含刚决定那块的字段 not already ran Process 不是 Prepare 同一套字段：** 看见填了字段不是已经 Prepare / Process 同一套字段就已经跑过 Process，不是 407 bundled interchangeable / 359 Prepare 同一套字段 interchangeable / 360 Process guarantee interchangeable。
3. **Finalize 含刚决定那块的字段 not Contains bundled interchangeable 不是 461 / 474 newly decided bundled：** 看见填了字段不是已经 Contains newly decided block fields bundled interchangeable，不是 407 bundled interchangeable / 461 bundled interchangeable / 474 bundled interchangeable。

## 为什么要分开叫

官方把 Finalize 含刚决定那块的字段 not already settled 写成三个名字。把它们叫成一个「看见填了 Finalize 字段余量就已经四门已经结算 interchangeable / 已经跑过 Process interchangeable / 已经 Contains bundled interchangeable」，会把 not four gates settled、not ran Process、not Contains bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 含刚决定那块的字段 not already settled 正式三事（407 余量），先数清问的是 Finalize 含刚决定那块的字段 是不是 already four gates settled、是不是 already ran Process、是不是 Contains bundled interchangeable，再决定要不要同一次发布。
