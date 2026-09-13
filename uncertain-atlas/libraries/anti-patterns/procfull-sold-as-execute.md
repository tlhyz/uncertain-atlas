# 反模式：看见 Process 含全部信息就当成已经执行那些交易 / 看见八栏齐就当成已经只有 PrepareProposalResponse.txs / 看见能 fully execute 就当成已经是 FinalizeBlockRequest 字段

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**例**：[Contains all information needed to fully execute ≠ 已经执行那些交易](../../tracks/implementation/worked-example-procfull-vs-execute.md)。

## 塌法

1. 看见 ProcessProposal Contains all information on the proposed block needed to fully execute it / 看见含执行所需全部信息，就当成已经执行那些交易，或当成已经 Finalize 跑过。
2. 看见 `ProcessProposalRequest` 有 `txs` + `proposed_last_commit` + `misbehavior` + `hash` + `height` + `time` + `next_validators_hash` + `proposer_address` / 看见八栏齐，就当成已经只有 `PrepareProposalResponse.txs`，或当成已经只有 raw proposal。
3. 看见含提案块上执行所需的全部信息 / 看见填了信息，就当成已经是 `FinalizeBlockRequest` 刚决定那块的字段，或当成已经只有 txs 字段就够。

## 为什么会出事

官方写：Contains all information on the proposed block needed to fully execute it。Request 表写八栏，而 `PrepareProposalResponse` 只有 `txs`。Finalize 请求栏是已决块字段。这不是已经执行那些交易，不是已经只有 Prepare 回包，也不是已经 Finalize 含刚决定那块的字段 interchangeable。

## 和相邻反模式

- [fintxs-sold-as-control](fintxs-sold-as-control.md) 是 Finalize 执行余量 bundled，不是本页这种 ProcessProposal Usage 单独切片。
- [procreq-sold-as-extreq](procreq-sold-as-extreq.md) 是 Process 请求栏单栏 bundled，不是本页这种 Request 八栏齐 vs Prepare 回包只有 txs。
- [proccand-sold-as-commit](proccand-sold-as-commit.md) 是 Process MAY 整块执行 / candidate state / read-only bundled，不是本页这种「信息够执行」不是「已经执行」。
