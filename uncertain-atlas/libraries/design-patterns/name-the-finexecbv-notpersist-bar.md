# 模式：把 FinalizeBlock When Application executes block v not persist decision / When calling guarantee 正式三事（466 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When / Usage。  
**例**：[FinalizeBlock When Application executes block v not persist decision / When calling guarantee ≠ bundled（466）](../../tracks/implementation/worked-example-finexecbv-notpersist-vs-bundled.md)。

## 三个名字

1. **executes block v not persist decision / When calling guarantee 不是 FinalizeBlock When Application executes block v bundled：** 看见 Application executes block _v_ 不是已经 persist decision interchangeable，不是 466 finexecbv interchangeable / 584 apply candidate interchangeable / 362 +2/3 precommit interchangeable。
2. **executes block v not persist decision / When calling guarantee 不是 FinalizeBlock When calling ProcessProposal guarantee bundled：** 看见 When 第 3 步 executes block _v_ 不是已经 When calling guarantee / persist decision interchangeable，不是 472 finwhen interchangeable / 570 not every validator interchangeable / 571 not proposer interchangeable。
3. **executes block v not persist decision / When calling guarantee 不是 572 not execbv：** 看见 Application executes block _v_ 不是已经 472 item 3 not executes block v 单句 interchangeable，不是 572 not execbv interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock When 第 3 步 Application executes block _v_ 和 persist decision / When calling guarantee 写成三个名字。把它们叫成一个「看见 Application executes block _v_ 就已经 persist decision interchangeable / 已经 466 finexecbv bundled interchangeable / 已经 472 When calling interchangeable」，会把 not persist decision / When calling guarantee、not 472 bundled、not 572 not execbv 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When Application executes block v not persist decision / When calling guarantee 正式三事（466 余量），先数清问的是 executes block v 是不是 already persist decision / When calling guarantee、是不是 already When calling guarantee / persist decision、是不是 already 572 not execbv，再决定要不要同一次发布。
