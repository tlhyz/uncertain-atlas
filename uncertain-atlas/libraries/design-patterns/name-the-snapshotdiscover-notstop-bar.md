# 模式：把 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事（322 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**例**：[被拒 not already no-snapshots ≠ bundled（322）](../../tracks/implementation/worked-example-snapshotdiscover-notstop-vs-bundled.md)。

## 三个名字

1. **被拒 不是 already no-snapshots：** 看见 Offer 被拒 / 拒掉这份快照，不是已经没有快照 interchangeable / 已经没有快照交差 interchangeable，不是 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable。

2. **拒了邻居 不是 already stopped：** 看见拒了格式或邻居 / 拒这种格式，不是已经停 interchangeable / 已经发现停交差 interchangeable，不是 322 snapshotdiscover item 2 interchangeable / 723 snapshotdiscover-notaccepted interchangeable。

3. **能中止 不是 already discovery-done：** 看见应用可以中止 / 中止发现，不是已经发现完 interchangeable / 已经发现完交差 interchangeable，不是 322 snapshotdiscover item 1 interchangeable / 722 snapshotdiscover-notall interchangeable。

官方把被拒单句、already no-snapshots、already stopped、already discovery-done 写成三个名字。把它们叫成一个「看见 Offer 被拒就已经没有快照 interchangeable / 就已经停 interchangeable / 就已经发现完 interchangeable」，会把 not already no-snapshots、not already stopped、not already discovery-done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事（322 余量），先数清问的是被拒 是不是 already no-snapshots / 322 / snapshotdiscover-sold-as-listed，是不是拒了邻居 是不是 already stopped，还是能中止 是不是 already discovery-done，再决定要不要同一次发布。322 snapshotdiscover vs offer bundled unbundling 在本页 item 3 完成。
