# 例：看见 tx_results Code==0 is not already not-in-block interchangeable / not already header-printed interchangeable / not already settled interchangeable

**层次**：实现 / tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事（404 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事（404 余量）/ not 1102 fhash-notout interchangeable / not 404 finapphash-vs-header bundled interchangeable」，不是 Finalize 回包余量 bundled（404），也不是 Code 非零就已经没进块（316），也不是 tx_results 就已经是 CheckTx 回包（431）。不要另写怎样写 Finalize 回包余量。

## 官方三件事

1. **看见 tx_results[i].Code == 0 只表示第 i 笔完全合法 / 看见回了 0 这份栏 is not already 已经没进块 interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1102 fhash-notout interchangeable / 1100 fhash-notheader interchangeable / 404 finapphash item 1 empty-det interchangeable，也不是已经 tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事 bundled（404 item 3 余量） interchangeable / 404 finapphash item 3 interchangeable。**  
   官方写：FinalizeBlockResponse.tx_results[i].Code == 0 只表示第 i 笔完全合法。看见回了 0，不是已经没进块 interchangeable——本页从 404 item 3 侧钉 not already not-in-block 单句。404 finapphash vs header bundled unbundling 在本页 item 3 完成。

2. **看见这笔合法 / 看见回了 0 / 这份栏 is not already 已经印进本头 interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1102 fhash-notout interchangeable / 404 finapphash item 2 query-anchor interchangeable / 1101 fhash-notalign interchangeable，也不是已经 Code 非零就已经没进块 interchangeable / 316 exectx interchangeable。**  
   官方把这笔合法和已经印进本头分开。看见这笔合法，不是已经印进本头 interchangeable。本页钉 not already header-printed 单句。

3. **看见能回 / 看见回了 0 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 回包余量 bundled（404） interchangeable / 1102 fhash-notout interchangeable / 1100 fhash-notheader interchangeable，也不是已经 tx_results 就已经是 CheckTx 回包 interchangeable / 431 finrespbar interchangeable。**  
   官方把能回和已经交差分开。看见能回，不是已经交差 interchangeable。404 finapphash vs header bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 回包余量、怎样挑空根、怎样回证明是规范里的做法，本页不抄。

## 官方为什么这样拆

- **tx_results Code==0 not already not-in-block ≠ 已经没进块 interchangeable：** 官方把这笔完全合法和 Code 非零就已经没进块分开。
- **看见这笔合法 not already header-printed ≠ 已经印进本头 interchangeable：** 官方把这笔合法和已经印进本头分开。
- **看见能回 not already settled ≠ 已经交差 interchangeable：** 官方把能回和已经交差分开；404 finapphash vs header bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| tx_results[i].Code == 0 只表示第 i 笔完全合法 | 不是已经没进块 | 不是 Code 非零就已经没进块（316） |
| 看见这笔合法 | 不是已经印进本头 | 不是 tx_results 就已经是 CheckTx 回包（431） |
| 看见能回 | 不是已经交差 | 不是空或硬编码就已经印进本头（1100） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 tx_results Code==0 not already not-in-block / not already header-printed / not already settled 正式三事（404 余量），必须分开是不是已经没进块、是不是已经印进本头、是不是已经交差。可以跳过「看见回了 Finalize 回包余量就已经印进本头」。不要另写怎样写 Finalize 回包余量。404 finapphash vs header bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 回包余量、怎样挑空根、怎样回证明。
- Finalize 回包余量 bundled。那是不变量 404。
- Code 非零就已经没进块。那是不变量 316。
- tx_results 就已经是 CheckTx 回包。那是不变量 431。
