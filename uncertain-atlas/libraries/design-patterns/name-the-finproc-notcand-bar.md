# 模式：把 FinalizeBlock When calling ProcessProposal guarantee not apply candidate 正式三事（472 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock When calling ProcessProposal guarantee not apply candidate ≠ bundled（472）](../../tracks/implementation/worked-example-finproc-notcand-vs-bundled.md)。

## 三个名字

1. **has run not apply candidate / previously executed 不是 FinalizeBlock When calling ProcessProposal guarantee bundled：** 看见 has run ProcessProposal on that block 不是已经套用 candidate 就不需要 guarantee，不是 472 bundled interchangeable / 460 apply candidate interchangeable / 568 even if passed interchangeable。
2. **has run not Process MAY fully execute committed 不是 ProcessProposal 候选执行 bundled：** 看见 has run 不是已经 Process MAY 整块执行交差，不是 472 bundled interchangeable / 452 candidate interchangeable / 543 MAY execute not committed interchangeable。
3. **has run on decided block not VVE proposed no guarantee 不是 VerifyVoteExtension 拟议块无保证：** 看见 has run 不是已经 VVE hash 指拟议块无 guarantee，不是 472 bundled interchangeable / 418 VVE proposed interchangeable / 353 hash points interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock When calling ProcessProposal guarantee not apply candidate 写成三个名字。把它们叫成一个「看见对这块跑过 Process 就已经套用 candidate interchangeable / 已经 Process MAY execute interchangeable / 已经拟议块无保证 interchangeable」，会把 not apply candidate、not MAY execute committed、not VVE proposed no guarantee 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When calling ProcessProposal guarantee not apply candidate 正式三事（472 余量），先数清问的是 has run 是不是 already apply candidate / previously executed、has run 是不是 already Process MAY fully execute committed、has run 是不是 already VVE proposed block no guarantee，再决定要不要同一次发布。
