# 模式：把请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事（375 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[填了三列 not already identical ≠ bundled（375）](../../tracks/implementation/worked-example-loadchunk-notidentical-vs-bundled.md)。

## 三个名字

1. **填了三列 不是 already identical：** 看见填了三列 / 请求用 height / format / chunk（从 0 起）认这块 / 填了 height·format·chunk，不是已经是同一份 interchangeable / 已经 identical interchangeable / 已经是同一份交差 interchangeable，不是 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable。

2. **从 0 起 不是 already complete：** 看见从 0 起 / 块下标从 0 起 / 从 0 起认块，不是已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，不是 872 loadchunk-notcomplete interchangeable / 322 ListSnapshots interchangeable。

3. **有 format 不是 already selected：** 看见有 format / 应用自己的 format / 填了 format，不是已经选型 interchangeable / 已经 selected interchangeable / 已经选型交差 interchangeable，不是 368 Snapshot identical interchangeable / 375 loadchunk item 3 interchangeable。

官方把填了三列、不是已经齐、不是已经选型写成三个名字。把它们叫成一个「看见填了三列就已经是同一份 interchangeable / 就已经齐 interchangeable / 就已经选型 interchangeable」，会把 not already identical、not already complete、not already selected 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事（375 余量），先数清问的是填了三列 是不是 already identical / 375 / loadchunk-sold-as-retrieved，是不是从 0 起 是不是 already complete，还是有 format 是不是 already selected，再决定要不要同一次发布。375 loadchunk-vs-retrieved bundled unbundling 在本页 item 2 续。
