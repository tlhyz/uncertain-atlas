# 模式：把拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事（324 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**例**：[标了高度 not already post-commit ≠ bundled（324）](../../tracks/implementation/worked-example-snapshottake-notcommitted-vs-bundled.md)。

## 三个名字

1. **标了这个高度 不是 already post-commit：** 看见标了这个高度 / 拍了快照 / Height 字段在，不是已经在交差之后拍的 interchangeable / 已经先 Commit 再拍交差 interchangeable，不是 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable。

2. **拍了 不是 already no-higher-height：** 看见拍了 / 已经拍了这份 / 标了高度之后，不是已经没有更高高度的数据 interchangeable / 已经不含更高高度交差 interchangeable，不是 323 snapshotswitch interchangeable / 324 snapshottake item 3 interchangeable。

3. **字段在 不是 already height-isolated：** 看见 Height 在 / 标了高度，不是已经隔离在这一高度 interchangeable / 已经单一高度隔离交差 interchangeable，不是 321 snapshotrestore interchangeable / 324 snapshottake item 2 interchangeable。

官方把标了高度单句、already post-commit、already no-higher-height、already height-isolated 写成三个名字。把它们叫成一个「看见标了这个高度就已经交差之后拍 interchangeable / 就已经没有更高高度 interchangeable / 就已经隔离在这一高度 interchangeable」，会把 not already post-commit、not already no-higher-height、not already height-isolated 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事（324 余量），先数清问的是标了这个高度 是不是 already post-commit / 324 / snapshottake-sold-as-committed，是不是拍了 是不是 already no-higher-height，还是字段在 是不是 already height-isolated，再决定要不要同一次发布。324 snapshottake vs commit bundled unbundling 在本页 item 1 启动。
