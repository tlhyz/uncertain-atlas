# 反模式：把 LoadSnapshotChunk Usage retrieve 正式三事卖成 LoadSnapshotChunk bundled / ListSnapshots discover / ApplySnapshotChunk 已经在装

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Used during state sync to retrieve ≠ LoadSnapshotChunk bundled](../../tracks/implementation/worked-example-loadsnapusage-retrieve-vs-bundled.md)。

## 卖法

- 「看见 Used during state sync to retrieve snapshot chunks from peers / 看见 LoadSnapshotChunk Usage 了就已经 height/format/chunk bundled interchangeable / 已经装完 interchangeable。」
- 「看见 retrieve from peers / 看见 ListSnapshots discover interchangeable / 已经本地清单 interchangeable / 已经问了邻居就齐。」
- 「看见 retrieve snapshot chunks / 看见 ApplySnapshotChunk chunk 栏 interchangeable / 已经 ACCEPT interchangeable / 已经齐 interchangeable。」

## 为什么错

官方把 Used during state sync to retrieve snapshot chunks from peers 写成一件独立的 Methods Usage 实现事。把它卖成 LoadSnapshotChunk bundled、ListSnapshots discover、ApplySnapshotChunk 已经在装，会把 state sync retrieve、retrieve from peers、retrieve chunks 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk Usage retrieve 正式三事，必须分开 Used during state sync to retrieve、retrieve from peers、retrieve snapshot chunks 三个名字，不要把它们卖成 LoadSnapshotChunk bundled / ListSnapshots discover / ApplySnapshotChunk 已经在装。

## 和相邻反模式

- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 LoadSnapshotChunk bundled 三事，不是本页 Methods Usage retrieve 单句专用边界。
- [listsnapusage-sold-as-bundled](listsnapusage-sold-as-bundled.md) 是 ListSnapshots Usage discover / Snapshot type 正式二事，不是本页 LoadSnapshotChunk Usage retrieve 正式三事。
- [applychunk-sold-as-loadchunk](applychunk-sold-as-loadchunk.md) 是 ApplySnapshotChunk chunk 栏 bundled 三事，不是本页 Usage retrieve 单句专用边界。
