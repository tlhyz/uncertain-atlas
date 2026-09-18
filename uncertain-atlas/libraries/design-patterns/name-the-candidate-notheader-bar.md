# 模式：把 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事（311 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[Prepare 没有头哈希 not already have header hash ≠ bundled（311）](../../tracks/implementation/worked-example-candidate-notheader-vs-bundled.md)。

## 三个名字

1. **Prepare 来了 不是 already have header hash：** 看见 PrepareProposal 披露了提案 / 两门给的字段差不多，不是已经有本头哈希 interchangeable / 已经知道本头 interchangeable，不是 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable。

2. **Process 有哈希 不是 Prepare already had hash：** 看见 ProcessProposal 交了块头哈希 / Process 字段里有 hash，不是 Prepare 当时已经有 interchangeable / 已经两门同一时刻都有哈希 interchangeable，不是 311 candidate item 2 interchangeable / 693 candidate-notexecute interchangeable。

3. **字段齐了 不是 already decided block identity：** 看见交易列表 LastCommit 时间 NextValidatorsHash 提议者都有了，不是已经能当决定块的身份 interchangeable / 已经是本高度最终块身份 interchangeable，不是 311 candidate item 3 interchangeable / 694 candidate-notdiscarded interchangeable。

官方把 Prepare 披露单句、already have header hash、Prepare already had hash、already decided block identity 写成三个名字。把它们叫成一个「看见 Prepare 披露了 就已经知道本头 interchangeable / 就已经 Prepare 当时有哈希 interchangeable / 就已经是决定块身份 interchangeable」，会把 not already have header hash、not Prepare already had hash、not already decided block identity 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有头哈希 not already have header hash / not Prepare already had hash / not already decided block identity 正式三事（311 余量），先数清问的是 Prepare 来了 是不是 already have header hash / 311 / 33，是不是 Process 有哈希 是不是 Prepare already had hash，还是字段齐了 是不是 already decided block identity，再决定要不要同一次发布。311 candidate vs execute bundled unbundling 在本页 item 1 完成。
