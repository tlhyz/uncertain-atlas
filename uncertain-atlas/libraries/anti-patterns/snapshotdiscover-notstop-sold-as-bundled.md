# 反模式：把 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事（322 余量）说成已经没有快照 / 已经停 / 已经发现完

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[被拒 not already no-snapshots ≠ bundled（322）](../../tracks/implementation/worked-example-snapshotdiscover-notstop-vs-bundled.md)。

## 卖法

把被拒 / Offer 被拒 / 拒掉这份快照 写成已经没有快照 interchangeable / 已经 no-snapshots interchangeable / 已经没有快照交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable；把拒了邻居 / 拒了格式或邻居 / 拒这种格式 写成已经停 interchangeable / 已经 stopped interchangeable；把能中止 / 应用可以中止 / 中止发现 写成已经发现完 interchangeable / 已经 discovery-done interchangeable，或已经和 322 snapshotdiscover bundled / snapshotdiscover-sold-as-listed interchangeable / 724 snapshotdiscover-notstop interchangeable。

## 为什么错

官方把被拒单句、already no-snapshots、already stopped、already discovery-done 写成三件独立的实现事。把它们卖成 already no-snapshots interchangeable / already stopped interchangeable / already discovery-done interchangeable，会把 not already no-snapshots、not already stopped、not already discovery-done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事（322 余量），必须分开 not already no-snapshots、not already stopped、not already discovery-done 三件事，不要和 322 / 33 / 722 / 723 / 321 / 38 / 314 糊成一句。

## 和相邻反模式

- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 Snapshot Discovery bundled 全段，不是本页 Offer 被拒 item 3 单句边界。
- [snapshotdiscover-notaccepted-sold-as-bundled](snapshotdiscover-notaccepted-sold-as-bundled.md) 是挑了最高 item 2，不是本页被拒边界。
- [snapshotdiscover-notall-sold-as-bundled](snapshotdiscover-notall-sold-as-bundled.md) 是 ListSnapshots 回了 item 1，不是本页被拒边界。
