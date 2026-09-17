# 模式：把 LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事（501 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled ≠ bundled（501）](../../tracks/implementation/worked-example-loadsnapusage-notretrieve-vs-bundled.md)。

## 三个名字

1. **Used during state sync to retrieve 不是 LoadSnapshotChunk bundled：** 看见 Used during state sync to retrieve snapshot chunks from peers，不是已经 LoadSnapshotChunk height/format/chunk bundled interchangeable，不是 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable / 378 applysnap interchangeable / 501 loadsnapusage retrieve interchangeable / 648 offersnapusage-notrestored interchangeable。
2. **Used during state sync to retrieve 不是 Offer 装完：** 看见 during state sync retrieve snapshot chunks，不是已经 Offer 收下就已经装完 interchangeable，不是 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage item 2 upon accepting retrieve and apply interchangeable。
3. **Used during state sync to retrieve 不是 Transition to Consensus：** 看见 used during state sync，不是已经 Transition to Consensus 已经切进共识 interchangeable，不是 323 transition interchangeable / 370 infover interchangeable / 652 offersnaptrust-nottransition interchangeable / 485 applysnapusage verify/Info/unable interchangeable。

## 为什么要分开叫

官方把 LoadSnapshotChunk Usage retrieve 单句、LoadSnapshotChunk bundled（375）、Offer 装完 / Accept 后拉块并装（321/401）、Transition to Consensus（323）写成三个名字。把它们叫成一个「看见 Used during state sync to retrieve 就已经 LoadSnapshotChunk bundled interchangeable / 就已经 Offer 装完 interchangeable / 就已经 Transition interchangeable」，会把 not LoadSnapshotChunk bundled、not Offer 装完、not Transition to Consensus 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事（501 余量），先数清问的是 Used during state sync to retrieve 是不是 LoadSnapshotChunk bundled / 375 / loadchunk-sold-as-retrieved，是不是 during state sync retrieve 是不是 Offer 装完 / 321 / 401 / 648，还是 used during state sync 是不是 Transition to Consensus / 323 / 370 / 652，再决定要不要同一次发布。501 loadsnapusage retrieve unbundling 在本页 item 1 启动。
