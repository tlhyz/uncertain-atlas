# 反模式：把 LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事（501 余量）说成已经 ApplySnapshotChunk chunk 栏 / 已经 ACCEPT / 已经 LoadSnapshotChunk 已经齐

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 ≠ bundled（501）](../../tracks/implementation/worked-example-loadsnapusage-notchunks-vs-bundled.md)。

## 错在哪里

把 retrieve snapshot chunks 写成已经 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回包 interchangeable / 397 applysnap-chunk interchangeable / applychunk-sold-as-loadchunk interchangeable / 378 applysnap interchangeable / 648 offersnapusage-notrestored interchangeable / 499 offersnapusage item 2 upon accepting retrieve and apply interchangeable；把 retrieve chunks 写成已经 ApplySnapshotChunk Result ACCEPT interchangeable / 401 offerafter interchangeable / 398 applysnap-result interchangeable / applyaccept-sold-as-restored interchangeable / 485 applysnapusage verify/Info/unable interchangeable；把 snapshot chunks from peers 写成已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐 interchangeable / 375 loadsnap interchangeable / 483 offersnaptrust interchangeable / 653 applysnapusage-notverify interchangeable / 332 snapshotverify interchangeable / 658 loadsnapusage-notretrieve interchangeable，或已经和 501 loadsnapusage retrieve bundled / loadsnapusage-sold-as-bundled / 659 loadsnapusage-notdiscover interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve snapshot chunks not ApplySnapshotChunk chunk 栏 / not ACCEPT bundled / not LoadSnapshotChunk 已经齐 正式三事（501 余量），必须分开 not ApplySnapshotChunk chunk 栏、not ACCEPT bundled、not LoadSnapshotChunk 已经齐 三件事，不要和 501 / 397 / 401 / 375 / 483 / 658 / 659 / 648 / 499 / 378 / 653 / 654 / 332 糊成一句。

## 和相邻反模式

- [loadsnapusage-sold-as-bundled](loadsnapusage-sold-as-bundled.md) 是 LoadSnapshotChunk Usage retrieve 专用 bundled（501），不是本页 501 item 3 单句边界。
- [applychunk-sold-as-loadchunk](applychunk-sold-as-loadchunk.md) 是 ApplySnapshotChunk chunk 栏 bundled 三事（397），不是本页 not ApplySnapshotChunk chunk 栏 单句边界。
- [loadsnapusage-notdiscover-sold-as-bundled](loadsnapusage-notdiscover-sold-as-bundled.md) 是 501 item 2 余量 / 659 专用 retrieve from peers，不是本页 retrieve snapshot chunks 单句边界。
