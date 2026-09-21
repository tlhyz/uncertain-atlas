# 反模式：把应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事（334 余量）说成已经没有这条对象 / 已经从创世是唯一合法路径 / 已经 ListSnapshots 齐了

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[应用选择不实现 not already no-object ≠ bundled（334）](../../tracks/implementation/worked-example-snapshotconn-notgone-vs-bundled.md)。

## 卖法

把应用选择不实现 / 快照管理可选 / 可以不实现 写成已经删掉 state sync 这个对象 interchangeable / 已经 no-object interchangeable / 已经没有这条对象交差 interchangeable / 334 snapshotconn bundled interchangeable / 33 four gates interchangeable / snapshotconn-sold-as-required interchangeable；把从创世的联想 / 可选就等于从创世 / 不实现就只剩创世 写成已经从创世是唯一合法路径 interchangeable / 已经 genesis-only interchangeable；把可选就当成清单齐了 / 已经问过邻居 / ListSnapshots 齐了的联想 写成已经齐了快照清单 interchangeable / 已经 listed interchangeable，或已经和 334 snapshotconn bundled / snapshotconn-sold-as-required interchangeable / 760 snapshotconn-notgone interchangeable。

## 为什么错

官方把应用选择不实现单句、already no-object、already genesis-only、already listed 写成三件独立的实现事。把它们卖成 already no-object interchangeable / already genesis-only interchangeable / already listed interchangeable，会把 not already no-object、not already genesis-only、not already listed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用选择不实现不是已经没有 state sync 这条对象 not already no-object / not already genesis-only / not already listed 正式三事（334 余量），必须分开 not already no-object、not already genesis-only、not already listed 三件事，不要和 334 / 33 / 322 / 329 / 38 / 758 / 759 糊成一句。

## 和相邻反模式

- [snapshotconn-sold-as-required](snapshotconn-sold-as-required.md) 是 Snapshot Connection bundled 全段，不是本页选择不实现 item 3 单句边界。
- [snapshotconn-notrequired-sold-as-bundled](snapshotconn-notrequired-sold-as-bundled.md) 是四门里有 Snapshot Connection item 1，不是本页对象还在边界。
- [snapshotconn-notbothends-sold-as-bundled](snapshotconn-notbothends-sold-as-bundled.md) 是两头都做 item 2，不是本页可选边界。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是 Query 回了 ≠ 已经是正常运转必须有（329），不是本页快照连接可选边界。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了 ≠ 已经齐（322），不是本页可选就当成清单齐了单句边界。
