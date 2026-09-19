# 例：看见被拒 / 看见拒了邻居 / 看见能中止 is not already already no-snapshots interchangeable / already stopped interchangeable / already discovery-done interchangeable

**层次**：实现 / Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事（322 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事（322 余量）/ not 724 snapshotdiscover-notstop interchangeable / not 322 snapshotdiscover bundled interchangeable」，不是 Snapshot Discovery bundled（322），也不是 ListSnapshots 回了不是已经有了全部快照（722 item 1 余量）或挑了最高不是已经收下（723 item 2 余量）。不要另写怎样列快照或怎样挑。

## 官方三件事

规范把 Requirements 里应用可以收下、拒掉、拒这种格式、拒这个邻居以及别的回法、CometBFT **会继续发现并继续 Offer** 直到有一份被收下或应用中止 和「已经是被拒就已经没有快照 interchangeable / 已经是拒了邻居就已经停 interchangeable / 已经是能中止就已经发现完 interchangeable / 已经是 Snapshot Discovery bundled interchangeable」分开写成三件独立的实现事，不是「看见 Offer 被拒就已经没有快照 interchangeable / 就已经停 interchangeable / 就已经发现完 interchangeable」一件事：

1. **看见被拒 / 看见 Offer 被拒 / 看见拒掉这份快照 is not already 已经没有快照 interchangeable / 已经 no-snapshots interchangeable / 已经没有快照交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 724 snapshotdiscover-notstop interchangeable / 322 snapshotdiscover item 3 interchangeable，也不是已经 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事 bundled（322 item 3 余量） interchangeable / 322 snapshotdiscover item 3 interchangeable，也不是已经 ListSnapshots 回了不是已经有了全部快照（722） interchangeable / 723 snapshotdiscover-notaccepted interchangeable / 321 snapshotrestore interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：CometBFT **会继续发现并继续 Offer**，直到有一份被收下，或应用中止。看见被拒，不是已经没有快照 interchangeable——322 钉 bundled 三事，本页从 item 3 侧钉 not already no-snapshots 单句。看见 Offer 被拒，不是已经 Snapshot Discovery bundled（322） interchangeable——322 钉 bundled，本页钉 item 3 第一件事。看见拒掉这份快照，不是已经 ListSnapshots 回了不是已经有了全部快照（722） interchangeable——722 另钉 item 1，本页钉 item 3 第一件事。322 snapshotdiscover vs offer bundled unbundling 在本页 item 3 启动。

2. **看见拒了邻居 / 看见拒了格式或邻居 / 看见拒这种格式 is not already 已经停 interchangeable / 已经 stopped interchangeable / 已经发现停交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 314 querystate interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 724 snapshotdiscover-notstop interchangeable / 322 snapshotdiscover item 1 ListSnapshots interchangeable / 322 snapshotdiscover item 2 挑了最高 interchangeable，也不是已经 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事 bundled（322 item 3 余量） interchangeable / 322 snapshotdiscover item 3 interchangeable，也不是已经没有快照（本页第一件事） interchangeable。**  
   官方把拒邻居/格式和已经停路径分开——拒了邻居，不等于已经停。看见拒了邻居，不是已经 stopped interchangeable——本页钉 not already stopped 单句。看见拒了格式或邻居，不是已经挑了最高不是已经收下（723） interchangeable——723 另钉 item 2，本页钉 item 3 第二件事。看见拒这种格式，不是已经启动对齐已经是快照重放（314） interchangeable——314 另钉，本页钉 item 3 第二件事。322 snapshotdiscover vs offer bundled unbundling 在本页 item 3 启动。

3. **看见能中止 / 看见应用可以中止 / 看见中止发现 is not already 已经发现完 interchangeable / 已经 discovery-done interchangeable / 已经发现完交差 interchangeable / 322 snapshotdiscover bundled interchangeable / 723 snapshotdiscover-notaccepted interchangeable，也不是已经 Snapshot Discovery bundled（322） interchangeable / 724 snapshotdiscover-notstop interchangeable / 322 snapshotdiscover item 1 / 322 snapshotdiscover item 2，也不是已经 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事 bundled（322 item 3 余量） interchangeable / 322 snapshotdiscover item 3 interchangeable，也不是已经没有快照（本页第一件事） interchangeable / 已经停（本页第二件事） interchangeable。**  
   官方把应用可以中止和已经发现完路径分开——能中止，不等于已经发现完。看见能中止，不是已经 discovery-done interchangeable——本页钉 not already discovery-done 单句。看见应用可以中止，不是已经没有快照（本页第一件事） interchangeable——三件事分开钉。看见中止发现，不是已经停（本页第二件事） interchangeable——中止是应用选择，不是拒一次就停。322 snapshotdiscover vs offer bundled unbundling 在本页 item 3 完成。

怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数是规范里的取值或做法，本页不抄。Snapshot Discovery bundled（322）、ListSnapshots 回了不是已经有了全部快照（322 item 1 余量 / 722）、挑了最高不是已经收下（322 item 2 余量 / 723）、Offer 收下已经装完（321）、只有 AppHash 可信任（38）、启动对齐当快照重放（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **被拒 not already no-snapshots ≠ 322 / 33 interchangeable：** 官方把继续发现并继续 Offer 和已经没有快照路径分开。
- **拒了邻居 not already stopped ≠ 已经停 interchangeable：** 官方把拒邻居/格式单句和已经停路径分开。
- **能中止 not already discovery-done ≠ 已经发现完 interchangeable：** 官方把应用中止选择和已经发现完路径分开；322 snapshotdiscover vs offer bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 被拒 | 不是 already no-snapshots | 不是 ListSnapshots 齐 alone（722） |
| 拒了邻居 | 不是 already stopped | 不是挑了最高 alone（723） |
| 能中止 | 不是 already discovery-done | 不是启动对齐 alone（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 被拒不是已经停 not already no-snapshots / not already stopped / not already discovery-done 正式三事（322 余量），必须分开被拒 是不是 already no-snapshots interchangeable / 322 snapshotdiscover bundled interchangeable / snapshotdiscover-sold-as-listed interchangeable、拒了邻居 是不是 already stopped interchangeable、能中止 是不是 already discovery-done interchangeable。可以跳过「看见 Offer 被拒就已经没有快照 interchangeable / 就已经停 interchangeable / 就已经发现完 interchangeable」。不要另写怎样列快照。322 snapshotdiscover vs offer bundled unbundling 在本页 item 3 完成（722 + 723 + 724）。

## 本页不抄

- 怎样实现 `ListSnapshots`、怎样挑、把 10 当产品常数。
- Snapshot Discovery bundled。那是不变量 322。
- ListSnapshots 回了不是已经有了全部快照。那是不变量 322 item 1 余量 / 722。
- 挑了最高不是已经收下。那是不变量 322 item 2 余量 / 723。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
- 启动对齐当快照重放。那是不变量 314。
