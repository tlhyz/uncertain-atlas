# 例：看见 Snapshot.height after-Commit is not already Query-height interchangeable / not already loaded interchangeable / not already settled interchangeable

**层次**：实现 / Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事（406 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事（406 余量）/ not 1106 sheight-notqueryh interchangeable / not 406 snapheight-vs-queryh bundled interchangeable」，不是 Snapshot 高度余量 bundled（406），也不是这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash（371），也不是快照装回就已经交差（321）。不要另写怎样写 Snapshot 高度余量。

## 官方三件事

1. **看见 Snapshot height 是拍快照的高度（Commit 之后） / 看见填了 height 这份栏 is not already 已经是 Query 高度 interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1106 sheight-notqueryh interchangeable / 1107 sheight-notmeta interchangeable / 406 snapheight item 2 metadata-not-allfields interchangeable，也不是已经 Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事 bundled（406 item 1 余量） interchangeable / 406 snapheight item 1 interchangeable。**  
   官方写：height 是拍这份快照的高度（在 Commit 之后）。看见填了 height，不是已经是 Query 高度 interchangeable——本页从 406 item 1 侧钉 not already Query-height 单句。406 snapheight vs queryh bundled unbundling 在本页 item 1 启动。

2. **看见写成 Commit 之后 / 看见填了 height / 这份栏 is not already 已经装完 interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1106 sheight-notqueryh interchangeable / 406 snapheight item 3 query-not-prove interchangeable / 1108 sheight-notprove interchangeable，也不是已经这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash interchangeable / 371 query-height interchangeable。**  
   官方把写成 Commit 之后和已经装完分开。看见写成 Commit 之后，不是已经装完 interchangeable。本页钉 not already loaded 单句。

3. **看见有高度 / 看见填了 height / 这份栏 is not already 已经交差 interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1106 sheight-notqueryh interchangeable / 1107 sheight-notmeta interchangeable，也不是已经快照装回就已经交差 interchangeable / 321 snapshot-restore interchangeable。**  
   官方把有高度和已经交差分开。看见有高度，不是已经交差 interchangeable。406 snapheight vs queryh bundled unbundling 在本页 item 1 启动。

怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Snapshot.height after-Commit not already Query-height ≠ 已经是 Query 高度 interchangeable：** 官方把拍快照的高度和 Query 那份高度分开。
- **看见写成 Commit 之后 not already loaded ≠ 已经装完 interchangeable：** 官方把写成 Commit 之后和已经装完分开。
- **看见有高度 not already settled ≠ 已经交差 interchangeable：** 官方把有高度和已经交差分开；406 snapheight vs queryh bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Snapshot.height 是拍快照的高度（Commit 之后） | 不是已经是 Query 高度 | 不是这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash（371） |
| 看见写成 Commit 之后 | 不是已经装完 | 不是快照装回就已经交差（321） |
| 看见有高度 | 不是已经交差 | 不是填了 metadata 就已经全字段对上（1107） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Snapshot.height after-Commit not already Query-height / not already loaded / not already settled 正式三事（406 余量），必须分开是不是已经是 Query 高度、是不是已经装完、是不是已经交差。可以跳过「看见填了 Snapshot 高度余量就已经是 Query 高度」。不要另写怎样写 Snapshot 高度余量。406 snapheight vs queryh bundled unbundling 在本页 item 1 启动；续 [`worked-example-sheight-notmeta-vs-bundled.md`](worked-example-sheight-notmeta-vs-bundled.md)（不变量 1107 item 2）。

## 本页不抄

- 怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明。
- Snapshot 高度余量 bundled。那是不变量 406。
- 这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash。那是不变量 371。
- 快照装回就已经交差。那是不变量 321。
