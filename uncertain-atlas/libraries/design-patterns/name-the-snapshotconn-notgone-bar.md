# 模式：把应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事（334 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**例**：[应用选择不实现 not already no-object ≠ bundled（334）](../../tracks/implementation/worked-example-snapshotconn-notgone-vs-bundled.md)。

## 三个名字

1. **选择不实现 不是 already no-object：** 看见应用选择不实现 / 快照管理可选 / 可以不实现，不是已经删掉 state sync 这个对象 interchangeable / 已经没有这条对象交差 interchangeable，不是 334 snapshotconn bundled interchangeable / 33 four gates interchangeable / snapshotconn-sold-as-required interchangeable。

2. **可选就等于从创世 不是 already genesis-only：** 看见从创世的联想 / 可选就等于从创世 / 不实现就只剩创世，不是已经从创世是唯一合法路径 interchangeable / 已经创世唯一交差 interchangeable，不是 329 query-replicated interchangeable / 334 snapshotconn item 1 interchangeable。

3. **可选就当成清单齐了 不是 already listed：** 看见可选就当成清单齐了 / 已经问过邻居 / ListSnapshots 齐了的联想，不是已经齐了快照清单 interchangeable / 已经问过邻居交差 interchangeable，不是 322 snapshotdiscover interchangeable / 334 snapshotconn item 2 interchangeable。

官方把应用选择不实现单句、already no-object、already genesis-only、already listed 写成三个名字。把它们叫成一个「看见应用选择不实现就已经没有 state sync 这条对象 interchangeable / 就已经从创世是唯一合法路径 interchangeable / 就已经 ListSnapshots 齐了 interchangeable」，会把 not already no-object、not already genesis-only、not already listed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事（334 余量），先数清问的是选择不实现 是不是 already no-object / 334 / snapshotconn-sold-as-required，是不是可选就等于从创世 是不是 already genesis-only，还是可选就当成清单齐了 是不是 already listed，再决定要不要同一次发布。334 snapshotconn vs required bundled unbundling 在本页 item 3 完成。
