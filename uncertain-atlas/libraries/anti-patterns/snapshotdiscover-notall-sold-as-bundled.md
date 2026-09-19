# 反模式：把 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事（322 余量）说成已经有了全部快照 / 已经没有上限 / 已经是不确定默认

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[问了邻居 not already all-snapshots ≠ bundled（322）](../../tracks/implementation/worked-example-snapshotdiscover-notall-vs-bundled.md)。

## 卖法

把问了邻居 / ListSnapshots 回了 / 邻居报了快照 写成已经有了全部快照 interchangeable / 已经 all-snapshots interchangeable / 已经齐交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable；把回了 / ListSnapshots 回了 / 每个节点限 10 份 写成已经没有上限 interchangeable / 已经 no-cap interchangeable；把看见 10 / 每节点 10 份 / 限 10 写成已经是不确定默认 interchangeable / 已经 product-default-10 interchangeable，或已经和 322 snapshotdiscover bundled / snapshotdiscover-sold-as-listed interchangeable / 722 snapshotdiscover-notall interchangeable。

## 为什么错

官方把问了邻居单句、already all-snapshots、already no-cap、already product-default-10 写成三件独立的实现事。把它们卖成 already all-snapshots interchangeable / already no-cap interchangeable / already product-default-10 interchangeable，会把 not already all-snapshots、not already no-cap、not already product-default-10 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事（322 余量），必须分开 not already all-snapshots、not already no-cap、not already product-default-10 三件事，不要和 322 / 33 / 321 / 723 / 724 / 38 / 314 糊成一句。不要把每节点 10 份当不确定默认。

## 和相邻反模式

- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 Snapshot Discovery bundled 全段，不是本页 ListSnapshots 回了 item 1 单句边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Snapshot Restoration（321），不是本页 Discovery 边界。
- [listsnapempty-sold-as-discovery](listsnapempty-sold-as-discovery.md) 是空请求栏，不是本页每节点限 10 份边界。
