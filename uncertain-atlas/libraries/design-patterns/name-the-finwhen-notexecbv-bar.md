# 模式：把 FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision 正式三事（472 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision ≠ bundled（472）](../../tracks/implementation/worked-example-finwhen-notexecbv-vs-bundled.md)。

## 三个名字

1. **When calling guarantee not executes block v / persist decision 不是 FinalizeBlock When calling ProcessProposal guarantee bundled：** 看见 When calling guarantee 不是已经 persist decision interchangeable，不是 472 finwhen interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable。
2. **When calling guarantee not executes block v / persist decision 不是 Application executes block v bundled：** 看见 at least one 不是已经 Application executes block v interchangeable，不是 466 executes block v interchangeable / 362 +2/3 precommit interchangeable / 584 apply candidate interchangeable。
3. **When calling guarantee not executes block v / persist decision 不是 582 not executes block v：** 看见 guarantees at least one 不是已经 360 item 1 not executes block v 单句 interchangeable，不是 582 not executes block v interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。

## 为什么要分开叫

官方把 at least one non-byzantine validator has run ProcessProposal 和 When 第 3 步 Application executes block _v_ / persist decision 写成三个名字。把它们叫成一个「看见 When calling guarantee 就已经 persist decision interchangeable / 已经 472 finwhen bundled interchangeable / 已经 466 executes block v interchangeable」，会把 not executes block v / persist decision、not 466 bundled、not 582 not executes block v 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not executes block v / persist decision 正式三事（472 余量），先数清问的是 at least one 是不是 already persist decision / executes block v、是不是 already Application executes block v、是不是 already 582 not executes block v，再决定要不要同一次发布。
