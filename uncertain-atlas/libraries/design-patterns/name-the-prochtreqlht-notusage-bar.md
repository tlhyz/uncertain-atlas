# 模式：把 ProcessProposal Request height/time 栏 not Usage match 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**例**：[ProcessProposal Request height/time 栏 not Usage match ≠ bundled](../../tracks/implementation/worked-example-prochtreqlht-notusage-vs-bundled.md)。

## 三个名字

1. **Request height/time 栏 not Usage match 不是 ProcessProposal height/time 对上拟议块头 bundled：** 看见填了 height / time 不是已经 Usage 那种 match the values from the header，不是 454 bundled interchangeable / 419 height 单栏 interchangeable / 549 not verified interchangeable。
2. **Request height/time 栏 not verified vote timestamp 不是 304 Timestamp verified：** 看见填了 time 不是已经 ExtendVoteRequest.time 那种已经验过票上 Timestamp，不是 454 bundled interchangeable / 304 Timestamp verified interchangeable / 372 Misbehavior.time interchangeable。
3. **Request height/time 栏 not Process height/time match bundled 不是 417 bundled：** 看见有 height / time 栏不是已经 Process height/time match header bundled，不是 454 bundled interchangeable / 417 header fields bundled interchangeable / 419 / 420 单栏 interchangeable。

## 为什么要分开叫

官方把 ProcessProposal Request height/time 栏 not Usage match 写成三个名字。把它们叫成一个「看见填了 height/time 就已经 Usage 那种对上了」，会把 Request 栏描述、Usage match 和票上 Timestamp 验过三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Request height/time 栏 not Usage match 正式三事，先数清问的是 Request height / time 栏 是不是 already Usage match、Request height / time 栏 是不是 already verified vote timestamp、Request height / time 栏 是不是 already Process height/time match bundled，再决定要不要同一次发布。
