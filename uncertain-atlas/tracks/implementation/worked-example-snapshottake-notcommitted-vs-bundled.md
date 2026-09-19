# 例：看见标了这个高度 / 看见拍了快照 / 看见字段在 is not already already post-commit interchangeable / already no-higher-height interchangeable / already height-isolated interchangeable

**层次**：实现 / 拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事（324 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事（324 余量）/ not 728 snapshottake-notcommitted interchangeable / not 324 snapshottake bundled interchangeable」，不是 Taking Snapshots bundled（324），也不是没停链不是已经一致（729 item 2 余量）或只留最近两份不是已经有了全部历史快照（730 item 3 余量）。不要另写怎样拍快照或怎样切块。

## 官方三件事

规范把 Requirements 里快照有 `Height`、必须在该高度已经 Commit 之后拍、而且不得含任何更高高度的数据 和「已经是标了高度就已经交差之后拍 interchangeable / 已经是拍了就已经没有更高高度 interchangeable / 已经是字段在就已经隔离在这一高度 interchangeable / 已经是 Taking Snapshots bundled interchangeable」分开写成三件独立的实现事，不是「看见标了这个高度 / 看见拍了快照就已经交差之后拍 interchangeable / 就已经没有更高高度 interchangeable / 就已经隔离在这一高度 interchangeable」一件事：

1. **看见标了这个高度 / 看见拍了快照 / 看见 Height 字段在 is not already 已经在交差之后拍的 interchangeable / 已经 post-commit interchangeable / 已经先 Commit 再拍交差 interchangeable / 324 snapshottake bundled interchangeable / 33 four gates interchangeable / snapshottake-sold-as-committed interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 728 snapshottake-notcommitted interchangeable / 324 snapshottake item 1 interchangeable，也不是已经拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事 bundled（324 item 1 余量） interchangeable / 324 snapshottake item 1 interchangeable，也不是已经没停链不是已经一致（729） interchangeable / 730 snapshottake-notretained interchangeable / 38 apphash interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：快照有 `Height`。必须在**该高度已经 Commit 之后**拍。看见标了这个高度，不是已经交差之后拍 interchangeable——324 钉 bundled 三事，本页从 item 1 侧钉 not already post-commit 单句。看见拍了快照，不是已经 Taking Snapshots bundled（324） interchangeable——324 钉 bundled，本页钉 item 1 第一件事。看见 Height 字段在，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉信任边界，本页钉生产者拍高度。324 snapshottake vs commit bundled unbundling 在本页 item 1 启动。

2. **看见拍了 / 看见已经拍了这份 / 看见标了高度之后 is not already 已经没有更高高度的数据 interchangeable / 已经 no-higher-height interchangeable / 已经不含更高高度交差 interchangeable / 324 snapshottake bundled interchangeable / 323 snapshotswitch interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 728 snapshottake-notcommitted interchangeable / 324 snapshottake item 2 没停链 interchangeable / 324 snapshottake item 3 只留两份 interchangeable，也不是已经拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事 bundled（324 item 1 余量） interchangeable / 324 snapshottake item 1 interchangeable，也不是已经交差之后拍（本页第一件事） interchangeable。**  
   官方把拍了和不得含任何更高高度的数据分开——拍了，不等于已经没有更高高度。看见拍了，不是已经 no-higher-height interchangeable——本页钉 not already no-higher-height 单句。看见已经拍了这份，不是已经切进共识不是已经有完整历史（323） interchangeable——323 另钉切共识，本页钉生产者拍高度。看见标了高度之后，不是已经交差之后拍（本页第一件事） interchangeable——三件事分开钉。324 snapshottake vs commit bundled unbundling 在本页 item 1 启动。

3. **看见字段在 / 看见 Height 在 / 看见标了高度 is not already 已经隔离在这一高度 interchangeable / 已经 height-isolated interchangeable / 已经单一高度隔离交差 interchangeable / 324 snapshottake bundled interchangeable / 321 snapshotrestore interchangeable，也不是已经 Taking Snapshots bundled（324） interchangeable / 728 snapshottake-notcommitted interchangeable / 324 snapshottake item 2 / 324 snapshottake item 3，也不是已经拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事 bundled（324 item 1 余量） interchangeable / 324 snapshottake item 1 interchangeable，也不是已经交差之后拍（本页第一件事） interchangeable / 已经没有更高高度（本页第二件事） interchangeable。**  
   官方把标了高度字段和已经隔离在单一高度路径分开——字段在，不等于已经隔离。看见字段在，不是已经 height-isolated interchangeable——本页钉 not already height-isolated 单句。看见 Height 在，不是已经没停链就已经一致（324 item 2 / Consistent） interchangeable——Consistent 是 item 2，本页钉 item 1 第三件事。看见标了高度，不是已经 Offer 收下就已经装完（321） interchangeable——321 另钉装回。324 snapshottake vs commit bundled unbundling 在本页 item 1 完成。

怎样用 RocksDB / MVCC 拍、怎样切成 10 MB、把最近两份当产品常数是规范里的取值或做法，本页不抄。Taking Snapshots bundled（324）、没停链不是已经一致（324 item 2 余量 / 729）、只留最近两份不是已经有了全部历史快照（324 item 3 余量 / 730）、只有 AppHash 可信任（38）、Offer 收下已经装完（321）、切进共识已经有完整历史（323）是另外那套，本页不抄。

## 官方为什么这样拆

- **标了高度 not already post-commit ≠ 324 / 33 interchangeable：** 官方把标高度和必须先 Commit 分开。
- **拍了 not already no-higher-height ≠ 已经没有更高高度 interchangeable：** 官方把拍了和不得含更高高度分开。
- **字段在 not already height-isolated ≠ 已经隔离在这一高度 interchangeable：** 官方把字段在和已经隔离在单一高度分开；324 snapshottake vs commit bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 标了这个高度 | 不是 already post-commit | 不是 Only AppHash alone（38） |
| 拍了 | 不是 already no-higher-height | 不是切进共识 alone（323） |
| 字段在 | 不是 already height-isolated | 不是没停链 Consistent alone（324 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拍了这个高度不是已经交差之后拍的 not already post-commit / not already no-higher-height / not already height-isolated 正式三事（324 余量），必须分开标了这个高度 是不是 already post-commit interchangeable / 324 snapshottake bundled interchangeable / snapshottake-sold-as-committed interchangeable、拍了 是不是 already no-higher-height interchangeable、字段在 是不是 already height-isolated interchangeable。可以跳过「看见标了这个高度就已经交差之后拍 interchangeable / 就已经没有更高高度 interchangeable / 就已经隔离在这一高度 interchangeable」。不要另写怎样拍快照。324 snapshottake vs commit bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshottake-notconsistent-vs-bundled.md`](worked-example-snapshottake-notconsistent-vs-bundled.md)（不变量 729 item 2）。

## 本页不抄

- 怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份或 10 MB 当产品常数。
- Taking Snapshots bundled。那是不变量 324。
- 没停链不是已经一致。那是不变量 324 item 2 余量 / 729。
- 只留最近两份不是已经有了全部历史快照。那是不变量 324 item 3 余量 / 730。
- 只有 AppHash 可信任。那是不变量 38。
- Offer 收下已经装完。那是不变量 321。
- 切进共识已经有完整历史。那是不变量 323。
