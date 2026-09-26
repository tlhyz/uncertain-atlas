# 反模式：看见 syncing_to_height 同步或重放时是目标高、否则等于本高就当成已经有完整历史 / 看见 validator_updates 空则引擎保持当前集合就当成已经没有集合 / 看见 Finalize 回包 events 标成非确定就当成已经必须确定

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**例**：[syncing_to_height 同步或重放时是目标高、否则等于本高 ≠ 已经有完整历史](../../tracks/implementation/worked-example-syncingheight-vs-history.md)。

## 塌法

1. 看见 `syncing_to_height` 同步或重放时是目标高、否则等于本高 / 看见填了目标，就当成已经有完整历史，或当成已经是快照重放。
2. 看见 `validator_updates` 空则引擎保持当前集合 / 看见空着，就当成已经没有集合，或当成已经改了集合。
3. 看见 Finalize 回包 `events` 标成非确定 / 看见回了事件，就当成已经必须确定，或当成已经交差。

## 为什么会出事

官方写：节点在同步或重放块时，`syncing_to_height` 等于目标高度。否则 `syncing_to_height` 等于本高。`validator_updates` 或 `consensus_param_updates` 可以空。空着时，CometBFT 保持当前值。`events` 的 Deterministic 列是 No。

## 和相邻反模式

- [syncingheight-nothistory-sold-as-bundled](syncingheight-nothistory-sold-as-bundled.md) 是 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史 not already history / not already restored / not already settled 正式三事（382 item 1），不是本页 bundled 全段 alone。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是切进共识就已经有从创世的完整历史，不是本页这种 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 空名单就已经没有集合，不是本页这种 validator_updates 空则引擎保持当前集合不是已经没有集合。
- [finalizedet-sold-as-prepare](finalizedet-sold-as-prepare.md) 是 Finalize 算出的状态就必须只依赖上一份状态和决定块，不是本页这种 Finalize 回包 events 标成非确定不是已经必须确定。
