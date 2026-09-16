# 模式：把 FinalizeBlock newly decided block fields not ProcessProposal contains all information 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock newly decided block fields not ProcessProposal contains all information ≠ bundled](../../tracks/implementation/worked-example-finnewfields-notprocfull-vs-bundled.md)。

## 三个名字

1. **newly decided block fields not ProcessProposal contains all information 不是 FinalizeBlock 含刚决定那块字段 bundled：** 看见 newly decided 字段不是已经 ProcessProposal 含执行所需全部信息，不是 461 bundled interchangeable / 453 bundled interchangeable / 549 not Finalize fields interchangeable。
2. **newly decided block fields not proposed/decided interchangeable 不是 422 decided vs proposed：** 看见 decided block 不是已经 proposed_last_commit interchangeable，不是 461 bundled interchangeable / 422 decided vs proposed interchangeable / 420 proposed_last_commit interchangeable。
3. **newly decided block fields not only raw proposal enough 不是 548 only Prepare txs：** 看见有刚决定那块不是已经 only raw proposal 就够，不是 461 bundled interchangeable / 548 Request 八栏齐 interchangeable / 549 only txs enough interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock newly decided block fields not ProcessProposal contains all information 写成三个名字。把它们叫成一个「看见 newly decided 字段就已经 Process 含全部信息」，会把 newly decided vs proposed 对象、proposed vs decided 请求栏、newly decided vs raw proposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock newly decided block fields not ProcessProposal contains all information 正式三事，先数清问的是 newly decided block fields 是不是 ProcessProposal contains all information interchangeable、newly decided block fields 是不是 proposed/decided interchangeable、newly decided block fields 是不是 only raw proposal enough，再决定要不要同一次发布。
