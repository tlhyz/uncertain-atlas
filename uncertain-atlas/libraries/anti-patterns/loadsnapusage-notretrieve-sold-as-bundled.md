# 反模式：把 LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事（501 余量）说成已经 LoadSnapshotChunk bundled / 已经 Offer 装完 / 已经 Transition to Consensus

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled ≠ bundled（501）](../../tracks/implementation/worked-example-loadsnapusage-notretrieve-vs-bundled.md)。

## 错在哪里

把 Used during state sync to retrieve snapshot chunks from peers 写成已经 LoadSnapshotChunk height/format/chunk bundled interchangeable / 375 loadsnap interchangeable / loadchunk-sold-as-retrieved interchangeable / 378 applysnap interchangeable / 501 loadsnapusage retrieve interchangeable / 648 offersnapusage-notrestored interchangeable；把 during state sync retrieve snapshot chunks 写成已经 Offer 收下就已经装完 interchangeable / 321 offerrestored interchangeable / 401 offerafter interchangeable / 499 offersnapusage item 2 upon accepting retrieve and apply interchangeable；把 used during state sync 写成已经 Transition to Consensus 已经切进共识 interchangeable / 323 transition interchangeable / 370 infover interchangeable / 652 offersnaptrust-nottransition interchangeable / 485 applysnapusage verify/Info/unable interchangeable，或已经和 501 loadsnapusage retrieve bundled / loadsnapusage-sold-as-bundled interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage Used during state sync to retrieve not LoadSnapshotChunk bundled / not Offer 装完 / not Transition to Consensus 正式三事（501 余量），必须分开 not LoadSnapshotChunk bundled、not Offer 装完、not Transition to Consensus 三件事，不要和 501 / 375 / 321 / 401 / 323 / 648 / 499 / 647 / 500 / 395 / 322 糊成一句。

## 和相邻反模式

- [loadsnapusage-sold-as-bundled](loadsnapusage-sold-as-bundled.md) 是 LoadSnapshotChunk Usage retrieve 专用 bundled（501），不是本页 501 item 1 单句边界。
- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 LoadSnapshotChunk bundled 三事（375），不是本页 Methods Usage retrieve 单句边界。
- [offersnapusage-notrestored-sold-as-bundled](offersnapusage-notrestored-sold-as-bundled.md) 是 499 item 2 余量 / 648 专用 upon accepting retrieve and apply，不是本页 not Offer 装完 单句边界。
