# 模式：把 at least one non-byzantine ran Process not every validator 正式三事（360 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[at least one non-byzantine ran Process not every validator ≠ bundled（360）](../../tracks/implementation/worked-example-finprocgua-notallproc-vs-bundled.md)。

## 三个名字

1. **at least one non-byzantine ran Process not every validator 不是 Finalize 时的 Process 保证 bundled：** 看见至少一名不是已经每个验证者都跑过 Process，不是 360 bundled interchangeable / 570 not every validator interchangeable / 472 When calling interchangeable。
2. **at least one not proposer means everyone Processed 不是 Process 也会在提议者那边叫：** 看见 guarantees at least one 不是已经提议者 Process 过就代表全网都 Process 过，不是 351 Process also on proposer interchangeable / 571 not proposer interchangeable。
3. **at least one not executes block v / persist decision 不是 When calling guarantee bundled：** 看见 guarantees at least one 不是已经 persist decision interchangeable，不是 466 executes block v interchangeable / 362 +2/3 precommit interchangeable。

## 为什么要分开叫

官方把 at least one non-byzantine validator has run ProcessProposal 写成三个名字。把它们叫成一个「看见要 Finalize 了就已经每个验证者都跑过 Process interchangeable / 已经提议者 Process 过 interchangeable / 已经 Finalize 时的 Process 保证 bundled interchangeable」，会把 not every validator、not proposer means everyone Processed、not executes block v 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 at least one non-byzantine ran Process not every validator 正式三事（360 余量），先数清问的是 at least one 是不是 already every validator ran Process、是不是 already proposer means everyone Processed、是不是 already executes block v / persist decision，再决定要不要同一次发布。
