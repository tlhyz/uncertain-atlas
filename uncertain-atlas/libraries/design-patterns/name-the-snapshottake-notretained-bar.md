# 模式：把只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事（324 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**例**：[只留两份 not already full-history-retained ≠ bundled（324）](../../tracks/implementation/worked-example-snapshottake-notretained-vs-bundled.md)。

## 三个名字

1. **只留最近两份 不是 already full-history-retained：** 看见只留最近两份 / 旧快照删了 / 只留两份，不是已经有了全部历史快照 interchangeable / 已经生产者全历史交差 interchangeable，不是 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable。

2. **Hash 对上 不是 already five-field-same：** 看见 Hash 对上了 / Hash 相同 / 拉 chunk 时 Hash 对，不是已经五字段都相同 interchangeable / 已经 Height/Format/Chunks/Hash/Metadata 交差 interchangeable，不是 321 snapshotrestore interchangeable / 324 snapshottake item 1 interchangeable。

3. **有 Hash 不是 already apphash-light-check：** 看见有 Hash / 任意哈希字段 / Hash 在，不是已经是轻验 AppHash interchangeable / 已经 AppHash 轻验交差 interchangeable，不是 38 apphash interchangeable / 324 snapshottake item 2 interchangeable。

官方把只留两份单句、already full-history-retained、already five-field-same、already apphash-light-check 写成三个名字。把它们叫成一个「看见只留最近两份就已经有了全部历史 interchangeable / 就已经五字段同一份 interchangeable / 就已经轻验 AppHash interchangeable」，会把 not already full-history-retained、not already five-field-same、not already apphash-light-check 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只留最近两份不是已经有了全部历史快照 not already full-history-retained / not already five-field-same / not already apphash-light-check 正式三事（324 余量），先数清问的是只留最近两份 是不是 already full-history-retained / 324 / snapshottake-sold-as-committed，是不是 Hash 对上 是不是 already five-field-same，还是有 Hash 是不是 already apphash-light-check，再决定要不要同一次发布。324 snapshottake vs commit bundled unbundling 在本页 item 3 完成。
