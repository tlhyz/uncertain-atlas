# 反模式：把只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事（324 余量）说成已经有了全部历史 / 已经五字段同一份 / 已经轻验 AppHash

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[只留两份 not already full-history-retained ≠ bundled（324）](../../tracks/implementation/worked-example-snapshottake-notretained-vs-bundled.md)。

## 卖法

把只留最近两份 / 旧快照删了 / 只留两份 写成已经有了全部历史快照 interchangeable / 已经 full-history-retained interchangeable / 已经生产者全历史交差 interchangeable / 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable；把 Hash 对上了 / Hash 相同 / 拉 chunk 时 Hash 对 写成已经五字段都相同 interchangeable / 已经 five-field-same interchangeable；把有 Hash / 任意哈希字段 / Hash 在 写成已经是轻验 AppHash interchangeable / 已经 apphash-light-check interchangeable，或已经和 324 snapshottake bundled / snapshottake-sold-as-committed interchangeable / 730 snapshottake-notretained interchangeable。

## 为什么错

官方把只留两份单句、already full-history-retained、already five-field-same、already apphash-light-check 写成三件独立的实现事。把它们卖成 already full-history-retained interchangeable / already five-field-same interchangeable / already apphash-light-check interchangeable，会把 not already full-history-retained、not already five-field-same、not already apphash-light-check 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事（324 余量），必须分开 not already full-history-retained、not already five-field-same、not already apphash-light-check 三件事，不要和 324 / 33 / 728 / 729 / 38 / 321 / 322 糊成一句。

## 和相邻反模式

- [snapshottake-sold-as-committed](snapshottake-sold-as-committed.md) 是 Taking Snapshots bundled 全段，不是本页只留两份 item 3 单句边界。
- [snapshottake-notconsistent-sold-as-bundled](snapshottake-notconsistent-sold-as-bundled.md) 是三件保证 item 2，不是本页保留与同一份边界。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 已经齐（322），不是本页生产者只留两份边界。
