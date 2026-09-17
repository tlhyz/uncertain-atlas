# 模式：把 ApplySnapshotChunk Result RETRY not refetch regardless / not already complete / not applysnapusage refetch 正式三事（398 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**例**：[RETRY ≠ bundled（398）](../../tracks/implementation/worked-example-applyretry-notrefetch-vs-bundled.md)。

## 三个名字

1. **RETRY 不是已经 refetch 不论 result：** 看见回了 RETRY，不是已经 378 interchangeable / 719 applyretry-notrefetch interchangeable。
2. **看见回了 RETRY 不是已经齐：** 看见能再装，不是已经齐 interchangeable。
3. **看见能再装 不是 Usage refetch/ban：** 看见 RETRY，不是已经 502 interchangeable。

官方把 ApplySnapshotChunk Result 三条核心句拆成三个名字。把它们叫成一个「看见回了 ApplySnapshotChunk 结果枚举就已经再拉」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result RETRY 正式三事（398 余量），先数清问的是 RETRY 是不是已经 refetch 不论 result / 378、是不是已经齐、还是看见能再装是不是 502，再决定要不要同一次发布。398 applyretry vs refetch bundled unbundling 在本页 item 1 启动。
