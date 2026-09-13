# 模式：把 LoadSnapshotChunk Usage retrieve 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[Used during state sync to retrieve ≠ LoadSnapshotChunk bundled](../../tracks/implementation/worked-example-loadsnapusage-retrieve-vs-bundled.md)。

## 三个名字

1. **Used during state sync to retrieve 不是 LoadSnapshotChunk bundled：** 看见 Methods LoadSnapshotChunk Usage retrieve，不是 375 bundled interchangeable。
2. **retrieve from peers 不是 ListSnapshots discover：** 看见从邻居拉块，不是 500 discover interchangeable。
3. **retrieve snapshot chunks 不是 ApplySnapshotChunk chunk 栏：** 看见拉块，不是 397 chunk 栏 interchangeable。

## 为什么要分开叫

官方把 LoadSnapshotChunk Usage retrieve 单句、LoadSnapshotChunk bundled（375）、ListSnapshots Usage discover（500）、ApplySnapshotChunk chunk 栏（397）写成三个名字。把它们叫成一个「看见 LoadSnapshotChunk Usage 了就已经 bundled interchangeable、已经 discover interchangeable、已经 Apply 了 interchangeable」，会把 state sync retrieve、retrieve from peers、retrieve chunks 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve 正式三事，先数清问的是 Used during state sync to retrieve 是不是 LoadSnapshotChunk bundled interchangeable / 已经装完、retrieve from peers 是不是 ListSnapshots discover interchangeable / 已经本地清单、retrieve snapshot chunks 是不是 ApplySnapshotChunk chunk 栏 interchangeable / 已经齐，再决定要不要同一次发布。
