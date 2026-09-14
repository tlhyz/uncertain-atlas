# 模式：把 FinalizeBlock decided_last_commit from decided block not proposed_last_commit 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Request。  
**例**：[FinalizeBlock decided_last_commit from decided block not proposed_last_commit ≠ bundled](../../tracks/implementation/worked-example-findecided-notproposed-vs-bundled.md)。

## 三个名字

1. **decided_last_commit from decided block not proposed_last_commit 不是 FinalizeBlock decided_last_commit + misbehavior 定奖惩 bundled：** 看见 decided_last_commit 从刚决定那块拿到不是已经 ProcessProposalRequest.proposed_last_commit，不是 463 bundled interchangeable / 422 decided vs proposed interchangeable / 420 proposed_last_commit interchangeable。
2. **decided_last_commit from decided block not local_last_commit 不是 Prepare local_last_commit：** 看见 decided_last_commit 从刚决定那块拿到不是已经 PrepareProposalRequest.local_last_commit / 已经交差 local_last_commit，不是 463 bundled interchangeable / 359 Prepare 同一套 interchangeable / 418 local_last_commit interchangeable。
3. **decided_last_commit from decided block not can use means slashed 不是 558 can use not slashed：** 看见 decided_last_commit 从刚决定那块拿到不是已经可以用这两列定奖惩 / 已经 slashed，不是 463 bundled interchangeable / 558 can use not slashed interchangeable / 363 回包义务 interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock decided_last_commit from decided block not proposed_last_commit 写成三个名字。把它们叫成一个「看见 decided_last_commit 从刚决定那块拿到 就已经是 proposed_last_commit / local_last_commit / 已经 slashed」，会把 decided vs proposed commit、decided vs local commit、decided vs can use slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock decided_last_commit from decided block not proposed_last_commit 正式三事，先数清问的是 decided_last_commit from decided block 是不是 proposed_last_commit、decided_last_commit from decided block 是不是 local_last_commit、decided_last_commit from decided block 是不是 can use means slashed，再决定要不要同一次发布。
