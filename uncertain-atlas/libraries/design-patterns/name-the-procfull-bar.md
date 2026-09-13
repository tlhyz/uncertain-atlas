# 模式：把 ProcessProposal 含执行所需全部信息正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**例**：[Contains all information needed to fully execute ≠ 已经执行那些交易](../../tracks/implementation/worked-example-procfull-vs-execute.md)。

## 三个名字

1. **Contains all information needed to fully execute 不是已经执行那些交易 / 已经 Finalize 跑过：** 看见含执行所需全部信息不是已经按 Finalize 交差。
2. **Request 八栏齐不是已经只有 PrepareProposalResponse.txs / 已经只有 raw proposal：** 看见 `txs` + `proposed_last_commit` + `misbehavior` + `hash` + `height` + `time` + `next_validators_hash` + `proposer_address` 不是已经 Prepare 回包就够。
3. **含执行所需全部信息不是已经是 FinalizeBlockRequest 刚决定那块的字段：** 看见拟议块上执行所需不是已经 `decided_last_commit` / 已决块 hash interchangeable。

## 为什么要分开叫

官方把 ProcessProposal 含执行所需全部信息写成三个名字。把它们叫成一个「看见 Process 含全部信息就已经执行那些交易」，会把「信息够执行」、Request 八栏齐和 Finalize 已决块字段一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 含全部信息就已经执行那些交易」，先数清问的是 Contains all information needed to fully execute 是不是已经执行那些交易、Request 八栏齐是不是已经只有 PrepareProposalResponse.txs，还是含执行所需全部信息是不是已经是 FinalizeBlockRequest 刚决定那块的字段，再决定要不要同一次发布。
