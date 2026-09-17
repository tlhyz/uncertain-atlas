# 模式：把 Finalize 请求末栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**例**：[FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址 ≠ 已经正在造这份提案](../../tracks/implementation/worked-example-finreqend-vs-procreq.md)。

## 三个名字

1. **FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案：** 看见填了 proposer_address 不是已经知道本头哈希。
2. **FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头：** 看见填了 time 不是已经是 PrepareProposalRequest.time。
3. **FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史：** 看见填了 syncing_to_height 不是已经是快照重放。

## 为什么要分开叫

官方把 FinalizeBlock Request 表上 `proposer_address` 是造了这份提案的验证者地址、`time` 是已决块的时间戳、`syncing_to_height` 在同步或重放时等于目标高、否则等于本高写成三件事。把它们叫成一个「看见填了 Finalize 请求末栏就已经正在造这份提案」，会把已经正在造这份提案、已经对上了拟议块头和已经有完整历史一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 请求末栏就已经正在造这份提案」，先数清问的是 FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案、FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头，还是 FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史，再决定要不要同一次发布。
