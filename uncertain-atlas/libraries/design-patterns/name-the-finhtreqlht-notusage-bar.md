# 模式：把 FinalizeBlock Request height/time 栏 not Usage match 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock Request height/time 栏 not Usage match ≠ bundled](../../tracks/implementation/worked-example-finhtreqlht-notusage-vs-bundled.md)。

## 三个名字

1. **Request height/time 栏 not Usage match 不是 FinalizeBlock height/time 对上拟议块头 bundled：** 看见填了 height / time 不是已经 Usage 那种 match the values from the header，不是 462 bundled interchangeable / 422 height 单栏 interchangeable / 552 not verified interchangeable。
2. **Request height/time 栏 not verified vote timestamp 不是 304 Timestamp verified：** 看见填了 time 不是已经 ExtendVoteRequest.time 那种已经验过票上 Timestamp，不是 462 bundled interchangeable / 304 Timestamp verified interchangeable / 372 Misbehavior.time interchangeable。
3. **Request height/time 栏 not ProcessProposalRequest height/time interchangeable 不是 454 Process match：** 看见有 height / time 栏不是已经 ProcessProposalRequest.height / time interchangeable，不是 462 bundled interchangeable / 454 Process height/time match interchangeable / 550 Process Request not Usage match interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock Request height/time 栏 not Usage match 写成三个名字。把它们叫成一个「看见填了 height/time 就已经 Usage 那种对上了」，会把 Request 栏描述、Usage match 和 ProcessProposalRequest.height / time 栏三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Request height/time 栏 not Usage match 正式三事，先数清问的是 Request height / time 栏 是不是 already Usage match、Request height / time 栏 是不是 already verified vote timestamp、Request height / time 栏 是不是 already ProcessProposalRequest.height / time interchangeable，再决定要不要同一次发布。
