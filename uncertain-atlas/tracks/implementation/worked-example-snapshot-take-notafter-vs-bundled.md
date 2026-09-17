# 例：看见拍了这个高度 is not already after-commit interchangeable / not already no-higher interchangeable / not already settled interchangeable

**层次**：实现 / 拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事（324 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事（324 余量）/ not 950 snapshot-take-notafter interchangeable / not 324 snapshot-take-vs-commit bundled interchangeable」，不是快照 bundled（324），也不是只有 AppHash 可信任（38），也不是 Offer 收下已经装完（321）。不要另写怎样拍快照或怎样切块。

## 官方三件事

1. **看见标了这个高度 / 看见拍了快照 这份快照 is not already 已经在交差之后拍的 interchangeable，也不是已经快照 bundled（324） interchangeable / 950 snapshot-take-notafter interchangeable / 951 snapshot-take-notcons interchangeable / 324 snapshot-take item 2 没停链 interchangeable，也不是已经拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事 bundled（324 item 1 余量） interchangeable / 324 snapshot-take item 1 interchangeable。**  
   官方写：快照有 Height。必须在该高度已经 Commit 之后拍，而且不得含任何更高高度的数据。看见标了高度，不是已经交差之后拍 interchangeable——本页从 324 item 1 侧钉 not already after-commit 单句。324 snapshot-take vs commit bundled unbundling 在本页 item 1 启动。

2. **看见拍了 / 看见标了高度 / 这份快照 is not already 已经没有更高高度的数据 interchangeable，也不是已经快照 bundled（324） interchangeable / 950 snapshot-take-notafter interchangeable / 324 snapshot-take item 3 只留两份 interchangeable / 952 snapshot-take-notall interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-only interchangeable。**  
   官方把标高度和不得含更高高度分开——324 bundled 第一件事常与 38 混成「看见拍了就已经交差之后拍或已经可信任 interchangeable」，本页钉 not already no-higher 单句。

3. **看见字段在 / 看见拍了 / 这份快照 is not already 已经交差 interchangeable，也不是已经快照 bundled（324） interchangeable / 950 snapshot-take-notafter interchangeable / 951 snapshot-take-notcons interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 snapshot-restore interchangeable。**  
   官方把字段在和已经隔离在这一高度分开。看见字段在，不是已经交差 interchangeable。324 snapshot-take vs commit bundled unbundling 在本页 item 1 启动。

怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份当产品常数是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **拍了这个高度 not already after-commit ≠ 已经交差之后拍的 interchangeable：** 官方把标高度和必须先 Commit 分开。
- **看见拍了 not already no-higher ≠ 已经没有更高高度的数据 interchangeable：** 官方把拍了和不得含更高高度分开。
- **看见字段在 not already settled ≠ 已经交差 interchangeable：** 官方把字段在和已经隔离在这一高度分开；324 snapshot-take vs commit bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 拍了这个高度 | 不是已经交差之后拍的 | 不是只有 AppHash 可信任（38） |
| 看见拍了 | 不是已经没有更高高度的数据 | 不是 Offer 收下已经装完（321） |
| 看见字段在 | 不是已经交差 | 不是没停链就已经一致（951） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拍了这个高度 not already after-commit / not already no-higher / not already settled 正式三事（324 余量），必须分开是不是已经交差之后拍的、是不是已经没有更高高度的数据、是不是已经交差。可以跳过「看见拍了就已经交差之后拍」。不要另写怎样拍快照或怎样切块。不要把最近两份当不确定默认。324 snapshot-take vs commit bundled unbundling 在本页 item 1 启动；续 [`worked-example-snapshot-take-notcons-vs-bundled.md`](worked-example-snapshot-take-notcons-vs-bundled.md)（不变量 951 item 2）。

## 本页不抄

- 怎样用 RocksDB / MVCC 拍、怎样切块、把最近两份当产品常数。
- 快照 bundled。那是不变量 324。
- 只有 AppHash 可信任。那是不变量 38。
- Offer 收下已经装完。那是不变量 321。
