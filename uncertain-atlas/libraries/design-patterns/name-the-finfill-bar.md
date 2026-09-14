# 模式：把 FinalizeBlock fill all fields even if Prepare/Process passed 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock fill all fields even if Prepare/Process passed ≠ bundled](../../tracks/implementation/worked-example-finfill-bundled.md)。

## 三个名字

1. **fill all fields not no need to provide again 不是 Finalize 时的 Process 保证 bundled：** 看见 will fill up all fields 不是已经不用再给，不是 360 bundled interchangeable / 583 not refill interchangeable / 567 not no need to provide again interchangeable / 582 not every validator interchangeable。
2. **even if passed not field names match means ran Process 不是 Prepare/Process/Finalize same fields：** 看见 even if already passed 不是已经跑过 Process，不是 359 same fields interchangeable / 351 Process also on proposer interchangeable / 568 not passed means ran Process interchangeable。
3. **fill all fields not request complete means committed 不是 finfields / finpersist bundled：** 看见请求齐了 不是已经交差，不是 407 finfields interchangeable / 335 finpersist interchangeable / 569 not request complete means committed interchangeable / 584 apply candidate interchangeable。

## 为什么要分开叫

官方把 Currently / will fill up all fields / even if already passed 写成三个名字。把它们叫成一个「看见 Prepare / Process 已经给过就已经不用再给 interchangeable / 已经跑过 Process interchangeable / 已经交差 interchangeable」，会把 not no need to provide again、not field names match、not request complete means committed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock fill all fields even if Prepare/Process passed，先数清问的是 fill 是不是 already no need to provide again、even if passed 是不是 already field names match means ran Process、fill 是不是 already request complete means committed，再决定要不要同一次发布。
