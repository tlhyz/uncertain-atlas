# 模式：把 ApplySnapshotChunk Result RETRY_SNAPSHOT not switched / not restored / not Offer accepted 正式三事（398 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Result。  
**例**：[RETRY_SNAPSHOT ≠ bundled（398）](../../tracks/implementation/worked-example-applyretry-notswitch-vs-bundled.md)。

## 三个名字

1. **RETRY_SNAPSHOT 不是已经换一份就能接着装：** 看见回了 RETRY_SNAPSHOT，不是已经 321 interchangeable / 720 applyretry-notswitch interchangeable。
2. **看见回了 RETRY_SNAPSHOT 不是已经装完：** 看见能重来这份，不是已经装完 interchangeable。
3. **看见能重来这份 不是 Offer 收下就已经装完：** 看见 RETRY_SNAPSHOT，不是已经 321 / 401 interchangeable。

官方把 ApplySnapshotChunk Result 三条核心句拆成三个名字。把它们叫成一个「看见回了 ApplySnapshotChunk 结果枚举就已经再拉」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result RETRY_SNAPSHOT 正式三事（398 余量），先数清问的是 RETRY_SNAPSHOT 是不是已经换一份就能接着装 / 321、是不是已经装完、还是看见能重来这份是不是 401，再决定要不要同一次发布。398 applyretry vs refetch bundled unbundling 在本页 item 2 续。
