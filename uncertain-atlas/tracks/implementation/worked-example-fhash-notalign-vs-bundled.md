# 例：看见 Query proof-anchor is not already apphash-aligned interchangeable / not already keyed-lookup interchangeable / not already settled interchangeable

**层次**：实现 / Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事（404 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事（404 余量）/ not 1101 fhash-notalign interchangeable / not 404 finapphash-vs-header bundled interchangeable」，不是 Finalize 回包余量 bundled（404），也不是 ProofOp.type 就已经是按键查（325），也不是 Query 回了 Proof 就已经对上 AppHash（325）。不要另写怎样写 Finalize 回包余量。

## 官方三件事

1. **看见以后 Query 可以拿这份根当锚回证明 / 看见能回证明 这份栏 is not already 已经对上 AppHash interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1101 fhash-notalign interchangeable / 1100 fhash-notheader interchangeable / 404 finapphash item 1 empty-det interchangeable，也不是已经 Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事 bundled（404 item 2 余量） interchangeable / 404 finapphash item 2 interchangeable。**  
   官方写：以后叫 Query，可以回以这份默克尔根为锚的应用状态证明。看见能回证明，不是已经对上 AppHash interchangeable——本页从 404 item 2 侧钉 not already apphash-aligned 单句。404 finapphash vs header bundled unbundling 在本页 item 2 续。

2. **看见有锚 / 看见能回证明 / 这份栏 is not already 已经是按键查 interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1101 fhash-notalign interchangeable / 404 finapphash item 3 code0 interchangeable / 1102 fhash-notout interchangeable，也不是已经 ProofOp.type 就已经是按键查 interchangeable / 325 query-proof interchangeable。**  
   官方把有锚和已经是按键查分开。看见有锚，不是已经是按键查 interchangeable。本页钉 not already keyed-lookup 单句。

3. **看见能查 / 看见能回证明 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1101 fhash-notalign interchangeable / 1100 fhash-notheader interchangeable，也不是已经 events 就已经印进本头 interchangeable / 431 finrespbar interchangeable。**  
   官方把能查和已经交差分开。看见能查，不是已经交差 interchangeable。404 finapphash vs header bundled unbundling 在本页 item 2 续。

怎样写 Finalize 回包余量、怎样挑空根、怎样回证明是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Query proof-anchor not already apphash-aligned ≠ 已经对上 AppHash interchangeable：** 官方把能回证明和已经对上分开。
- **看见有锚 not already keyed-lookup ≠ 已经是按键查 interchangeable：** 官方把有锚和已经是按键查分开。
- **看见能查 not already settled ≠ 已经交差 interchangeable：** 官方把能查和已经交差分开；404 finapphash vs header bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 以后 Query 可以拿这份根当锚回证明 | 不是已经对上 AppHash | 不是 ProofOp.type 就已经是按键查（325） |
| 看见有锚 | 不是已经是按键查 | 不是 events 就已经印进本头（431） |
| 看见能查 | 不是已经交差 | 不是 Code==0 就已经没进块（1102） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事（404 余量），必须分开是不是已经对上 AppHash、是不是已经是按键查、是不是已经交差。可以跳过「看见回了 Finalize 回包余量就已经印进本头」。不要另写怎样写 Finalize 回包余量。404 finapphash vs header bundled unbundling 在本页 item 2 续；续 [`worked-example-fhash-notout-vs-bundled.md`](worked-example-fhash-notout-vs-bundled.md)（不变量 1102 item 3）。

## 本页不抄

- 怎样写 Finalize 回包余量、怎样挑空根、怎样回证明。
- Finalize 回包余量 bundled。那是不变量 404。
- ProofOp.type 就已经是按键查。那是不变量 325。
- events 就已经印进本头。那是不变量 431。
