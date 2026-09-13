# 反模式：看见 FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动就当成已经在块 H 生效 / 看见 FinalizeBlockResponse.app_hash 是应用状态默克尔根就当成已经写进下一块头的 AppHash / 看见 FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待就当成已经是本地 timeout_commit

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**例**：[FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动 ≠ 已经在块 H 生效](../../tracks/implementation/worked-example-finrespend-vs-params.md)。

## 塌法

1. 看见 `FinalizeBlockResponse.consensus_param_updates` 是对 gas、大小和其它共识相关参数的改动 / 看见回了 consensus_param_updates，就当成已经在块 H 生效，或当成已经是只填一个字段就只改这一项。
2. 看见 `FinalizeBlockResponse.app_hash` 是应用状态默克尔根 / 看见回了 app_hash，就当成已经写进下一块头的 AppHash，或当成已经是本头 AppHash。
3. 看见 `FinalizeBlockResponse.next_block_delay` 是这块 Commit 后再开下一高的等待 / 看见回了 next_block_delay，就当成已经是本地 timeout_commit，或当成已经是 ConsensusParams.block 块间隔。

## 为什么会出事

官方写：块 H 返回的 `consensus_param_updates` 用于块 H+1 的共识参数。`app_hash` 会作为下一块头的 `Header.AppHash`。`next_block_delay` 以前叫 `timeout_commit`，但是非确定字段，各节点可以回不同值。看见回了 Finalize 回包末栏，不是已经在块 H 生效，也不是已经写进下一块头，也不是已经是本地 timeout_commit。

## 和相邻反模式

- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是只改一个字段就只改这一项，不是本页这种 FinalizeBlockResponse.consensus_param_updates 是对 gas、大小和其它共识相关参数的改动不是已经在块 H 生效。
- [finapphash-sold-as-header](finapphash-sold-as-header.md) 是 Finalize 回包 app_hash 可以空或硬编码就已经印进本头，不是本页这种 FinalizeBlockResponse.app_hash 是应用状态默克尔根不是已经写进下一块头的 AppHash。
- [app-delay-sold-as-slot](app-delay-sold-as-slot.md) 是 post-commit 等待已经标成非确定性，不是本页这种 FinalizeBlockResponse.next_block_delay 是这块 Commit 后再开下一高的等待不是已经是本地 timeout_commit。
