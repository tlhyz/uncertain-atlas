# 模式：把 ProcessProposal read-only checks/processes not mutate committed 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**例**：[ProcessProposal read-only checks/processes not mutate committed ≠ bundled](../../tracks/implementation/worked-example-proccand-readonly-notcommitted-vs-bundled.md)。

## 三个名字

1. **read-only checks/processes not mutate committed 不是 ProcessProposal 候选执行 bundled：** 看见 read-only 不是已经改了上一份已提交状态，不是 452 bundled interchangeable / 349 Req 9 interchangeable / 544 candidate not committed interchangeable。
2. **read-only not immediate execution committed 不是 MAY execute committed：** 看见 checks/processes 不是已经立刻执行就交差，不是 452 bundled interchangeable / 543 MAY execute interchangeable / 460 Finalize apply interchangeable。
3. **read-only not async can still Reject 不是 Process async can Reject：** 看见 read-only 不是已经 async 了还能 Reject，不是 452 bundled interchangeable / 354 async can Reject interchangeable / 541 prevote nil interchangeable。

## 为什么要分开叫

官方把 ProcessProposal read-only checks/processes not mutate committed 写成三个名字。把它们叫成一个「看见 Process 处理了拟议块就已经改了上一份已提交状态 interchangeable」，会把 Req 9 mutate committed、MAY execute committed、async can still Reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal read-only checks/processes not mutate committed 正式三事，先数清问的是 read-only 是不是 mutate committed、read-only 是不是 immediate execution committed、read-only 是不是 async can still Reject，再决定要不要同一次发布。
