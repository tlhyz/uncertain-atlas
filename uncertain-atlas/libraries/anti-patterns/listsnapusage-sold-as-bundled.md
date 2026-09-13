# 反模式：把 ListSnapshots Usage discover / Snapshot type 正式二事卖成 ListSnapshots 空请求 bundled / Snapshot 类型 five fields 对上

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[discover on peers during state sync ≠ ListSnapshots 空请求 bundled](../../tracks/implementation/worked-example-listsnapusage-discover-vs-bundled.md)。

## 卖法

- 「看见 Used during state sync to discover on peers / 看见 ListSnapshots Usage 了就已经空请求 bundled interchangeable / 已经本地清单 interchangeable / 已经问了邻居就齐。」
- 「看见 See Snapshot data type for details / 看见 five fields 对上就已经装完 / 已经同一份 interchangeable。」

## 为什么错

官方把 Used during state sync to discover available snapshots on peers、See `Snapshot` data type for details 写成两件独立的实现事。把它们卖成 ListSnapshots 空请求 bundled、Snapshot 类型 five fields 对上，会把 discover on peers、See Snapshot data type 两条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots Usage discover / Snapshot type 正式二事，必须分开 discover on peers during state sync、See Snapshot data type for details 两个名字，不要把它们卖成 ListSnapshots 空请求 bundled / Snapshot 类型 five fields 对上。

## 和相邻反模式

- [loadsnapusage-sold-as-bundled](loadsnapusage-sold-as-bundled.md) 是 LoadSnapshotChunk Usage retrieve 正式三事，不是本页 See Snapshot data type for details。
- [listsnapempty-sold-as-discovery](listsnapempty-sold-as-discovery.md) 是 ListSnapshots 空请求 bundled 三事，不是本页 Methods Usage discover 单句专用边界。
- [offersnapusage-bootstrap-sold-as-bundled](offersnapusage-bootstrap-sold-as-bundled.md) 是 OfferSnapshot Usage bootstrap accept/reject 正式三事，不是本页 ListSnapshots Usage 正式二事。
