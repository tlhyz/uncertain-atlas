# 例：看见 Snapshot.metadata arbitrary is not already all-fields-match interchangeable / not already incrementally-verified interchangeable / not already settled interchangeable

**层次**：实现 / Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事（406 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事（406 余量）/ not 1107 sheight-notmeta interchangeable / not 406 snapheight-vs-queryh bundled interchangeable」，不是 Snapshot 高度余量 bundled（406），也不是快照全字段（含 Metadata）对上就已经装完（368），也不是快照验过就已经交差（332）。不要另写怎样写 Snapshot 高度余量。

## 官方三件事

1. **看见 Snapshot metadata 是任意应用元数据、例如块哈希或其他核对数据 / 看见填了 metadata 这份栏 is not already 已经全字段对上 interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1107 sheight-notmeta interchangeable / 1106 sheight-notqueryh interchangeable / 406 snapheight item 1 height-not-query interchangeable，也不是已经 Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事 bundled（406 item 2 余量） interchangeable / 406 snapheight item 2 interchangeable。**  
   官方写：metadata 是任意应用元数据，例如 chunk 哈希或其他核对数据。看见填了 metadata，不是已经全字段对上 interchangeable——本页从 406 item 2 侧钉 not already all-fields-match 单句。406 snapheight vs queryh bundled unbundling 在本页 item 2 续。

2. **看见有块哈希 / 看见填了 metadata / 这份栏 is not already 已经在装回当中增量验过 interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1107 sheight-notmeta interchangeable / 406 snapheight item 3 query-not-prove interchangeable / 1108 sheight-notprove interchangeable，也不是已经快照全字段（含 Metadata）对上就已经装完 interchangeable / 368 snapshot-fields interchangeable。**  
   官方把有块哈希和已经在装回当中增量验过分开。看见有块哈希，不是已经在装回当中增量验过 interchangeable。本页钉 not already incrementally-verified 单句。

3. **看见能填 / 看见填了 metadata / 这份栏 is not already 已经交差 interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1107 sheight-notmeta interchangeable / 1106 sheight-notqueryh interchangeable，也不是已经快照验过就已经交差 interchangeable / 332 snapshot-verify interchangeable。**  
   官方把能填和已经交差分开。看见能填，不是已经交差 interchangeable。406 snapheight vs queryh bundled unbundling 在本页 item 2 续。

怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Snapshot.metadata arbitrary not already all-fields-match ≠ 已经全字段对上 interchangeable：** 官方把任意元数据和全字段对上才算同一份分开。
- **看见有块哈希 not already incrementally-verified ≠ 已经在装回当中增量验过 interchangeable：** 官方把有块哈希和已经在装回当中增量验过分开。
- **看见能填 not already settled ≠ 已经交差 interchangeable：** 官方把能填和已经交差分开；406 snapheight vs queryh bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据 | 不是已经全字段对上 | 不是快照全字段（含 Metadata）对上就已经装完（368） |
| 看见有块哈希 | 不是已经在装回当中增量验过 | 不是快照验过就已经交差（332） |
| 看见能填 | 不是已经交差 | 不是能回证明就已经对上 AppHash（1108） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Snapshot.metadata arbitrary not already all-fields-match / not already incrementally-verified / not already settled 正式三事（406 余量），必须分开是不是已经全字段对上、是不是已经在装回当中增量验过、是不是已经交差。可以跳过「看见填了 Snapshot 高度余量就已经是 Query 高度」。不要另写怎样写 Snapshot 高度余量。406 snapheight vs queryh bundled unbundling 在本页 item 2 续；续 [`worked-example-sheight-notprove-vs-bundled.md`](worked-example-sheight-notprove-vs-bundled.md)（不变量 1108 item 3）。

## 本页不抄

- 怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明。
- Snapshot 高度余量 bundled。那是不变量 406。
- 快照全字段（含 Metadata）对上就已经装完。那是不变量 368。
- 快照验过就已经交差。那是不变量 332。
