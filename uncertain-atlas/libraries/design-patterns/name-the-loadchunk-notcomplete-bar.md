# 模式：把 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[在拉 not already complete ≠ bundled（375）](../../tracks/implementation/worked-example-loadchunk-notcomplete-vs-bundled.md)。

## 三个名字

1. **在拉 不是 already complete：** 看见在拉 / LoadSnapshotChunk 用来从邻居拉快照块 / 在拉块，不是已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，不是 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable。

2. **问了邻居 不是 already all：** 看见问了邻居 / 从邻居拉 / 问邻居，不是已经有了全部快照 interchangeable / 已经 all interchangeable / 已经有了全部快照交差 interchangeable，不是 322 ListSnapshots interchangeable / 368 Snapshot identical interchangeable。

3. **能拉 不是 already restored：** 看见能拉 / 能拉快照块 / 能拉块，不是已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable，不是 321 Offer restored interchangeable / 375 loadchunk item 2 interchangeable。

官方把在拉、不是已经有了全部快照、不是已经装完写成三个名字。把它们叫成一个「看见在拉就已经齐 interchangeable / 就已经有了全部快照 interchangeable / 就已经装完 interchangeable」，会把 not already complete、not already all、not already restored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 余量），先数清问的是在拉 是不是 already complete / 375 / loadchunk-sold-as-retrieved，是不是问了邻居 是不是 already all，还是能拉 是不是 already restored，再决定要不要同一次发布。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 1 启动。
