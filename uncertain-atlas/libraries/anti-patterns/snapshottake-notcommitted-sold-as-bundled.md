# 反模式：把拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事（324 余量）说成已经交差之后拍 / 已经没有更高高度 / 已经隔离在这一高度

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[标了高度 not already post-commit ≠ bundled（324）](../../tracks/implementation/worked-example-snapshottake-notcommitted-vs-bundled.md)。

## 卖法

把标了这个高度 / 拍了快照 / Height 字段在 写成已经在交差之后拍的 interchangeable / 已经 post-commit interchangeable / 已经先 Commit 再拍交差 interchangeable / 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable；把拍了 / 已经拍了这份 / 标了高度之后 写成已经没有更高高度的数据 interchangeable / 已经 no-higher-height interchangeable；把字段在 / Height 在 / 标了高度 写成已经隔离在这一高度 interchangeable / 已经 height-isolated interchangeable，或已经和 324 snapshottake bundled / snapshottake-sold-as-committed interchangeable / 728 snapshottake-notcommitted interchangeable。

## 为什么错

官方把标了高度单句、already post-commit、already no-higher-height、already height-isolated 写成三件独立的实现事。把它们卖成 already post-commit interchangeable / already no-higher-height interchangeable / already height-isolated interchangeable，会把 not already post-commit、not already no-higher-height、not already height-isolated 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事（324 余量），必须分开 not already post-commit、not already no-higher-height、not already height-isolated 三件事，不要和 324 / 33 / 38 / 321 / 323 / 729 / 730 糊成一句。

## 和相邻反模式

- [snapshottake-sold-as-committed](snapshottake-sold-as-committed.md) 是 Taking Snapshots bundled 全段，不是本页拍高度 item 1 单句边界。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是切进共识已经有完整历史（323），不是本页生产者拍高度边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下已经装完（321），不是本页先 Commit 再拍边界。
