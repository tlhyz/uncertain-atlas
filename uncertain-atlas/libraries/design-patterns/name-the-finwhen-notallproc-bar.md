# 模式：把 FinalizeBlock When calling ProcessProposal guarantee not every validator 正式三事（472 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not every validator ≠ bundled（472）](../../tracks/implementation/worked-example-finwhen-notallproc-vs-bundled.md)。

## 三个名字

1. **When calling guarantee not every validator 不是 FinalizeBlock When calling ProcessProposal guarantee bundled：** 看见 When calling / guarantees at least one 不是已经 every validator ran Process，不是 472 finwhen interchangeable / 571 not proposer interchangeable / 466 executes block v interchangeable。
2. **When calling guarantee not every validator 不是 Finalize 时的 Process 保证 bundled：** 看见 guarantees at least one 不是已经每个验证者都跑过 Process / persist decision，不是 360 bundled interchangeable / 582 not every validator interchangeable / 584 apply candidate interchangeable。
3. **When calling guarantee not every validator 不是 582 not every validator：** 看见 When calling 不是已经 360 item 1 at least one 单句 interchangeable，不是 582 not every validator interchangeable / 351 Process also on proposer interchangeable / 473 finfill interchangeable。

## 为什么要分开叫

官方把 When calling `FinalizeBlock` / guarantees at least one non-byzantine validator has run ProcessProposal 写成三个名字。把它们叫成一个「看见 When calling guarantee 就已经 every validator ran Process interchangeable / 已经 472 finwhen bundled interchangeable / 已经 582 not every validator interchangeable」，会把 not every validator、not 360 bundled、not 582 not every validator 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not every validator 正式三事（472 余量），先数清问的是 When calling 是不是 already every validator ran Process、When calling 是不是 already Finalize 时的 Process 保证 bundled、When calling 是不是 already 582 not every validator，再决定要不要同一次发布。
