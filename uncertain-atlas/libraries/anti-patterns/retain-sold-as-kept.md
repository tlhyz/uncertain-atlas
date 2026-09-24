# 反模式：看见 retain_height 默认 0 就当成已经在剪 / 看见低于这个高度的块可以被删就当成已经没有历史 / 看见全网都删了会永久丢就当成已经能从创世再装

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[retain_height 默认 0 ≠ 已经在剪](../../tracks/implementation/worked-example-retain-vs-kept.md)。

## 塌法

1. 看见 `retain_height` 默认 0、表示全留 / 看见没填，就当成已经在剪，或当成已经交差。
2. 看见低于这个高度的块可以被删 / 看见回了高度，就当成已经是这个节点快照截断，或当成已经没有历史。
3. 看见全网都删了会永久丢、除非开了 state sync / 看见能剪，就当成已经能从创世再装，或当成已经能给轻客户端验。

## 为什么会出事

官方写：`CommitResponse.retain_height` 默认是 `0`，表示全留。低于这个高度的块可以被删。若网上所有节点都删了历史块，这些数据就永久丢了；除非链上开了 state sync，否则新节点加不进来。审计、回放没落盘的高度、轻客户端核验也可能还要用这些历史块。

## 和相邻反模式

- [retain-notpruning-sold-as-bundled](retain-notpruning-sold-as-bundled.md) 是 retain_height 默认 0 not already pruning / not already settled / not already no-history 正式三事（366 item 1），不是本页 bundled 全段 alone。
- [retain-notdeleted-sold-as-bundled](retain-notdeleted-sold-as-bundled.md) 是低于这个高度的块可以被删 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 item 2），不是本页 bundled 全段 alone。
- [crashsteps-sold-as-committed](crashsteps-sold-as-committed.md) 是崩溃三步就已经 Commit，不是本页这种 retain_height 默认 0 不是已经在剪。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是切进共识就已经有完整历史，不是本页这种低于这个高度的块可以被删不是已经没有历史。
- [statesync-sold-as-genesis](statesync-sold-as-genesis.md) 是应用快照就已经从创世重放，不是本页这种全网都删了会永久丢不是已经能从创世再装。
