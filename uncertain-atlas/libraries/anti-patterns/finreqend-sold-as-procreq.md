# 反模式：看见 FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址就当成已经正在造这份提案 / 看见 FinalizeBlockRequest.time 是已决块的时间戳就当成已经对上了拟议块头 / 看见 FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高就当成已经有完整历史

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**例**：[FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址 ≠ 已经正在造这份提案](../../tracks/implementation/worked-example-finreqend-vs-procreq.md)。

## 塌法

1. 看见 `FinalizeBlockRequest.proposer_address` 是造了这份提案的验证者地址 / 看见填了 proposer_address，就当成已经正在造这份提案，或当成已经知道本头哈希。
2. 看见 `FinalizeBlockRequest.time` 是已决块的时间戳 / 看见填了 time，就当成已经对上了拟议块头，或当成已经是 PrepareProposalRequest.time。
3. 看见 `FinalizeBlockRequest.syncing_to_height` 同步或重放时是目标高、否则等于本高 / 看见填了 syncing_to_height，就当成已经有完整历史，或当成已经是快照重放。

## 为什么会出事

官方写：`proposer_address` 是造了这份提案的验证者地址。`time` 是已决块的时间戳。节点在同步或重放块时 `syncing_to_height` 等于目标高度，否则等于本高。看见填了栏，不是已经正在造这份提案，也不是已经对上了拟议块头，也不是已经有完整历史。

## 和相邻反模式

- [procreqend-sold-as-prepreq](procreqend-sold-as-prepreq.md) 是 ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案，不是本页这种 FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址不是已经正在造这份提案。
- [prepreqend-sold-as-finreq](prepreqend-sold-as-finreq.md) 是 PrepareProposalRequest.time 是将要提议那块的时间戳不是已经对上了拟议块头，不是本页这种 FinalizeBlockRequest.time 是已决块的时间戳不是已经对上了拟议块头。
- [syncingheight-sold-as-history](syncingheight-sold-as-history.md) 是 syncing_to_height 同步或重放时是目标高、否则等于本高就已经有完整历史，不是本页这种 FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史。
