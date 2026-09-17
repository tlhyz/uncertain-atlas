# 模式：把 VerifyVoteExtension Usage unless really know liveness implications 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage unless really know liveness implications 句。  
**例**：[unless really know liveness implications ≠ bundled](../../tracks/implementation/worked-example-verifyaccept-liveness-vs-bundled.md)。

## 三个名字

1. **unless really know liveness implications 不是 free filter：** 看见 unless really know，不是 457 bundled interchangeable / 527 SHOULD always Accept interchangeable / 34 block invalid interchangeable。
2. **not free filter reject whole precommit 不是 Verify REJECT = block invalid：** 看见不是免费过滤，不是 457 bundled interchangeable / 34 whole precommit invalid interchangeable / 433 REJECT whole vote interchangeable。
3. **can Reject not no cost 不是 can't Reject：** 看见可以 Reject 有代价，不是 457 bundled interchangeable / 529 can't Reject interchangeable / 341 nondet liveness interchangeable。

## 为什么要分开叫

官方把 unless really know liveness implications、not free filter reject whole precommit、can Reject not no cost、Verify SHOULD Accept bundled（457）、SHOULD always set ACCEPT（527）、SHOULD Accept default strategy（529）写成三个名字。把它们叫成一个「看见除非真的知道活性代价 就已经拒整张 Precommit 是免费过滤 interchangeable」，会把 unless 条件、not free filter、REJECT 有 liveness 代价三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage unless really know liveness implications 正式三事，先数清问的是 unless really know 是不是 free filter、not free filter 是不是 block invalid (34)、can Reject 是不是 no cost / can't Reject，再决定要不要同一次发布。
