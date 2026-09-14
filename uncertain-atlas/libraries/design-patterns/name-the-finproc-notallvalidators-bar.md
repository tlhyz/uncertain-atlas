# 模式：把 FinalizeBlock When calling ProcessProposal guarantee not already every validator 正式三事（472 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not already every validator ≠ bundled（472）](../../tracks/implementation/worked-example-finproc-notallvalidators-vs-bundled.md)。

## 三个名字

1. **When calling / consensus guarantees not every validator 不是 FinalizeBlock When calling ProcessProposal guarantee bundled：** 看见 When calling FinalizeBlock / consensus guarantees 不是已经每个验证者都跑过 Process，不是 472 bundled interchangeable / 360 Process guarantee interchangeable / 466 executes block v interchangeable。
2. **When calling not executes block v / persist decision 不是 Application executes block v：** 看见 When calling 不是已经 Application executes block v / persist decision，不是 472 bundled interchangeable / 466 executes block v interchangeable / 362 +2/3 precommit interchangeable。
3. **When calling not +2/3 precommit already Finalize 不是 +2/3 precommit same id(v)：** 看见 When calling 不是已经 +2/3 precommit 就会 Finalize，不是 472 bundled interchangeable / 362 When interchangeable / 360 bundled interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock When calling ProcessProposal guarantee not already every validator 写成三个名字。把它们叫成一个「看见要 Finalize 了就已经每个验证者都跑过 Process / 已经 Application executes block v / 已经 +2/3 precommit interchangeable」，会把 not every validator、not executes block v、not +2/3 precommit already Finalize 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not already every validator 正式三事（472 余量），先数清问的是 When calling 是不是 already every validator ran Process、When calling 是不是 already executes block v / persist decision、When calling 是不是 already +2/3 precommit will Finalize，再决定要不要同一次发布。
