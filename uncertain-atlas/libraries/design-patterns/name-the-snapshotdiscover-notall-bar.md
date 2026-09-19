# 模式：把 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事（322 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**例**：[问了邻居 not already all-snapshots ≠ bundled（322）](../../tracks/implementation/worked-example-snapshotdiscover-notall-vs-bundled.md)。

## 三个名字

1. **问了邻居 不是 already all-snapshots：** 看见 ListSnapshots 回了 / 邻居报了快照，不是已经有了全部快照 interchangeable / 已经齐交差 interchangeable，不是 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable。

2. **回了 不是 already no-cap：** 看见 ListSnapshots 回了 / 每个节点限 10 份，不是已经没有上限 interchangeable / 已经无限快照交差 interchangeable，不是 322 snapshotdiscover item 2 interchangeable / 723 snapshotdiscover-notaccepted interchangeable。

3. **看见 10 不是 already product-default-10：** 看见每节点 10 份 / 限 10，不是已经是不确定默认 interchangeable / 已经把 10 当产品常数交差 interchangeable，不是 322 snapshotdiscover item 3 interchangeable / 724 snapshotdiscover-notstop interchangeable。

官方把问了邻居单句、already all-snapshots、already no-cap、already product-default-10 写成三个名字。把它们叫成一个「看见问了邻居就已经有了全部快照 interchangeable / 就已经没有上限 interchangeable / 就已经是不确定默认 interchangeable」，会把 not already all-snapshots、not already no-cap、not already product-default-10 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ListSnapshots 回了不是已经有了全部快照 not already all-snapshots / not already no-cap / not already product-default-10 正式三事（322 余量），先数清问的是问了邻居 是不是 already all-snapshots / 322 / snapshotdiscover-sold-as-listed，是不是回了 是不是 already no-cap，还是看见 10 是不是 already product-default-10，再决定要不要同一次发布。不要把每节点 10 份当不确定默认。322 snapshotdiscover vs offer bundled unbundling 在本页 item 1 启动。
