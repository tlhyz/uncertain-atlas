# 例：看见 Query optional Merkle-proof is not already apphash-aligned interchangeable / not already prove-flagged interchangeable / not already settled interchangeable

**层次**：实现 / Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事（406 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事（406 余量）/ not 1108 sheight-notprove interchangeable / not 406 snapheight-vs-queryh bundled interchangeable」，不是 Snapshot 高度余量 bundled（406），也不是 Query 请求 prove 就已经对上 AppHash（383），也不是 Query 锚就已经对上 AppHash（1101）。不要另写怎样写 Snapshot 高度余量。

## 官方三件事

1. **看见 Query 可以可选回默克尔证明 / 看见能回证明 这份栏 is not already 已经对上 AppHash interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1108 sheight-notprove interchangeable / 1106 sheight-notqueryh interchangeable / 406 snapheight item 1 height-not-query interchangeable，也不是已经 Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事 bundled（406 item 3 余量） interchangeable / 406 snapheight item 3 interchangeable。**  
   官方写：Query 可以可选回默克尔证明。看见能回证明，不是已经对上 AppHash interchangeable——本页从 406 item 3 侧钉 not already apphash-aligned 单句。406 snapheight vs queryh bundled unbundling 在本页 item 3 完成。

2. **看见有证明 / 看见能回证明 / 这份栏 is not already 已经勾了 prove interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1108 sheight-notprove interchangeable / 406 snapheight item 2 metadata-not-allfields interchangeable / 1107 sheight-notmeta interchangeable，也不是已经 Query 请求 prove 就已经对上 AppHash interchangeable / 383 query-prove interchangeable。**  
   官方把有证明和已经勾了 prove 分开。看见有证明，不是已经勾了 prove interchangeable。本页钉 not already prove-flagged 单句。

3. **看见能查 / 看见能回证明 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Snapshot 高度余量 bundled（406） interchangeable / 1108 sheight-notprove interchangeable / 1106 sheight-notqueryh interchangeable，也不是已经 Query 锚就已经对上 AppHash interchangeable / 1101 fhash-notalign interchangeable。**  
   官方把能查和已经交差分开。看见能查，不是已经交差 interchangeable。406 snapheight vs queryh bundled unbundling 在本页 item 3 完成。

怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Query optional Merkle-proof not already apphash-aligned ≠ 已经对上 AppHash interchangeable：** 官方把可以回证明和已经对上分开。
- **看见有证明 not already prove-flagged ≠ 已经勾了 prove interchangeable：** 官方把有证明和已经勾了 prove 分开。
- **看见能查 not already settled ≠ 已经交差 interchangeable：** 官方把能查和已经交差分开；406 snapheight vs queryh bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 可以可选回默克尔证明 | 不是已经对上 AppHash | 不是 Query 请求 prove 就已经对上 AppHash（383） |
| 看见有证明 | 不是已经勾了 prove | 不是 Query 锚就已经对上 AppHash（1101） |
| 看见能查 | 不是已经交差 | 不是写了 type 就已经是 ProofOp 类型（1105） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事（406 余量），必须分开是不是已经对上 AppHash、是不是已经勾了 prove、是不是已经交差。可以跳过「看见填了 Snapshot 高度余量就已经是 Query 高度」。不要另写怎样写 Snapshot 高度余量。406 snapheight vs queryh bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Snapshot 高度余量、怎样填 metadata、怎样回证明。
- Snapshot 高度余量 bundled。那是不变量 406。
- Query 请求 prove 就已经对上 AppHash。那是不变量 383。
- Query 锚就已经对上 AppHash。那是不变量 1101。
