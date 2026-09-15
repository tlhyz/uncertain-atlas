# 模式：把 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed ≠ bundled（472）](../../tracks/implementation/worked-example-finwhen-notproposer-vs-bundled.md)。

## 三个名字

1. **When calling guarantee not proposer means everyone Processed 不是 FinalizeBlock When calling ProcessProposal guarantee bundled：** 看见 guarantees at least one 不是已经 proposer means everyone Processed，不是 472 finwhen interchangeable / 570 not every validator interchangeable / 466 executes block v interchangeable。
2. **When calling guarantee not proposer means everyone Processed 不是 Process 也会在提议者那边叫：** 看见 at least one 不是已经 Process 也会在提议者那边叫 interchangeable，不是 351 Process also on proposer interchangeable / 582 not proposer interchangeable / 351 Process also on proposer means ran Process interchangeable。
3. **When calling guarantee not proposer means everyone Processed 不是 582 not proposer：** 看见 guarantees at least one 不是已经 360 item 1 not proposer 单句 interchangeable，不是 582 not proposer interchangeable / 473 finfill interchangeable / 568 not passed means ran Process interchangeable。

## 为什么要分开叫

官方把 at least one non-byzantine validator has run ProcessProposal 和 proposer also Process means everyone Processed 写成三个名字。把它们叫成一个「看见 guarantees at least one 就已经 proposer means everyone Processed interchangeable / 已经 472 finwhen bundled interchangeable / 已经 582 not proposer interchangeable」，会把 not proposer means everyone Processed、not 351 proposer path、not 582 not proposer 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not proposer means everyone Processed 正式三事（472 余量），先数清问的是 at least one 是不是 already proposer means everyone Processed、是不是 already Process 也会在提议者那边叫、是不是 already 582 not proposer，再决定要不要同一次发布。
