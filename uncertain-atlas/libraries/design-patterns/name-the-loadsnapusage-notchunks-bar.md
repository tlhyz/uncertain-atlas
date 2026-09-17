# 模式：把 LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事（501 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 ≠ bundled（501）](../../tracks/implementation/worked-example-loadsnapusage-notchunks-vs-bundled.md)。

## 三个名字

1. **retrieve snapshot chunks 不是 ApplySnapshotChunk chunk 栏：** 看见 retrieve snapshot chunks，不是已经 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回包 interchangeable，不是 397 applysnap-chunk interchangeable / applychunk-sold-as-loadchunk interchangeable / 378 applysnap interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage item 2 upon accepting retrieve and apply interchangeable。
2. **retrieve snapshot chunks 不是 ACCEPT bundled：** 看见 retrieve chunks，不是已经 ApplySnapshotChunk Result ACCEPT interchangeable，不是 401 offerafter interchangeable / 398 applysnap-result interchangeable / applyaccept-sold-as-restored interchangeable / 648 offersnapusage-notrestored interchangeable / 485 applysnapusage verify/Info/unable interchangeable。
3. **retrieve snapshot chunks 不是 LoadSnapshotChunk 已经齐：** 看见 snapshot chunks from peers，不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 interchangeable，不是 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable / 483 offersnaptrust interchangeable / 653 applysnapusage-notverify interchangeable / 332 snapshotverify interchangeable / 658 loadsnapusage-notretrieve interchangeable。

## 为什么要分开叫

官方把 LoadSnapshotChunk Usage retrieve snapshot chunks 单句、ApplySnapshotChunk chunk 栏 bundled（397）、ApplySnapshotChunk Result ACCEPT（401）、LoadSnapshotChunk bundled / Only AppHash（375/483）写成三个名字。把它们叫成一个「看见 retrieve snapshot chunks 就已经 ApplySnapshotChunk chunk 栏 interchangeable / 就已经 ACCEPT interchangeable / 就已经 LoadSnapshotChunk 已经齐 interchangeable」，会把 not ApplySnapshotChunk chunk 栏、not ACCEPT bundled、not LoadSnapshotChunk 已经齐 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事（501 余量），先数清问的是 retrieve snapshot chunks 是不是 ApplySnapshotChunk chunk 栏 / 397 / 378，是不是 retrieve chunks 是不是 ACCEPT bundled / 401 / 398 / 648，还是 snapshot chunks from peers 是不是 LoadSnapshotChunk 已经齐 / 375 / 483 / 653 / 332，再决定要不要同一次发布。501 loadsnapusage retrieve unbundling 在本页 item 3 完成。
