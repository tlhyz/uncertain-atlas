# 模式：把 FinalizeBlock newly decided block not proposed block 正式三事（474 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock newly decided block not proposed block ≠ bundled（474）](../../tracks/implementation/worked-example-finnewdec-notproposed-vs-bundled.md)。

## 三个名字

1. **newly decided block not proposed block / ProcessProposal contains all information 不是 FinalizeBlock Contains newly decided block fields bundled：** 看见 newly decided block 不是 proposed block，不是 474 bundled interchangeable / 453 ProcessProposal contains all information interchangeable / 549 not Finalize fields interchangeable。
2. **newly decided block not proposed_last_commit from proposed block 不是 420 Process proposed_last_commit：** 看见 decided block 不是 proposed_last_commit 那种 proposed 对象，不是 474 bundled interchangeable / 422 decided vs proposed interchangeable / 422 decided not proposed interchangeable。
3. **newly decided block not only raw proposal enough 不是 503 Prepare raw proposal：** 看见 newly decided block 不是只有 raw proposal / txs 就够，不是 474 bundled interchangeable / 503 raw proposal interchangeable / 548 Request 八栏齐 interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock newly decided block not proposed block 写成三个名字。把它们叫成一个「看见 newly decided block 就已经 ProcessProposal 含执行所需全部信息 / proposed_last_commit / raw proposal interchangeable」，会把 newly decided vs proposed、newly decided vs proposed_last_commit、newly decided vs raw proposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock newly decided block not proposed block 正式三事（474 余量），先数清问的是 newly decided block 是不是 proposed block / ProcessProposal contains all information、newly decided block 是不是 proposed_last_commit from proposed block、newly decided block 是不是 only raw proposal enough，再决定要不要同一次发布。
