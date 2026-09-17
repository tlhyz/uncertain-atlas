# 模式：把 Finalize 回包末栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动 ≠ 已经在块 H 生效](../../tracks/implementation/worked-example-finrespend-vs-params.md)。

## 三个名字

1. **FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动不是已经在块 H 生效：** 看见回了 consensus_param_updates 不是已经是只填一个字段就只改这一项。
2. **FinalizeBlockResponse.app_hash 是应用状态默克尔根不是已经写进下一块头的 AppHash：** 看见回了 app_hash 不是已经是本头 AppHash。
3. **FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待不是已经是本地 timeout_commit：** 看见回了 next_block_delay 不是已经是 ConsensusParams.block 块间隔。

## 为什么要分开叫

官方把 FinalizeBlock Response 表上 `consensus_param_updates` 是对 gas、大小和其它共识相关参数的改动、`app_hash` 是应用状态默克尔根、`next_block_delay` 是这块 Commit 后再开下一高的等待写成三件事。把它们叫成一个「看见回了 Finalize 回包末栏就已经在块 H 生效」，会把已经在块 H 生效、已经写进下一块头和已经是本地 timeout_commit 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 Finalize 回包末栏就已经在块 H 生效」，先数清问的是 FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动不是已经在块 H 生效、FinalizeBlockResponse.app_hash 是应用状态默克尔根不是已经写进下一块头的 AppHash，还是 FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待不是已经是本地 timeout_commit，再决定要不要同一次发布。
