# 例：看见拜占庭能提案一满块无效交易 is not already pool-blocked interchangeable / not already out-of-consensus interchangeable / not already settled interchangeable

**层次**：实现 / 拜占庭能提案一满块无效交易 not already pool-blocked / not already out-of-consensus / not already settled 正式三事（339 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「拜占庭能提案一满块无效交易 not already pool-blocked / not already out-of-consensus / not already settled 正式三事（339 余量）/ not 930 checktx-weak-notpool interchangeable / not 339 checktx-weak-vs-process bundled interchangeable」，不是弱过滤器 bundled（339），也不是四门已经结算（33），也不是索引器已经保证不重放（313）。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。

## 官方三件事

1. **看见拜占庭可以不在乎 CheckTx / 看见能提案一满块无效交易 这份提案 is not already 已经被池子挡住 interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 930 checktx-weak-notpool interchangeable / 929 checktx-weak-notsort interchangeable / 339 checktx-weak item 1 排序 interchangeable，也不是已经拜占庭能提案一满块无效交易 not already pool-blocked / not already out-of-consensus / not already settled 正式三事 bundled（339 item 2 余量） interchangeable / 339 checktx-weak item 2 interchangeable。**  
   官方写：CheckTx 弱，是因为拜占庭节点可以不在乎 CheckTx；它想的话就能提案一满块无效交易。看见池子会挡，不是拜占庭已经被挡住 interchangeable——本页从 339 item 2 侧钉 not already pool-blocked 单句。339 checktx-weak vs process bundled unbundling 在本页 item 2 续。

2. **看见能提案无效交易 / 看见诚实节点过了 CheckTx / 这份提案 is not already 已经进不了共识 interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 930 checktx-weak-notpool interchangeable / 339 checktx-weak item 3 ProcessProposal interchangeable / 931 checktx-weak-notproc interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把能提案无效交易和已经进不了块分开——339 bundled 第二件事常与 33 混成「看见拜占庭能提案就已经被池子挡住或已经交差 interchangeable」，本页钉 not already out-of-consensus 单句。

3. **看见诚实节点过了 CheckTx / 看见池子会挡 / 这份提案 is not already 已经交差 interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 930 checktx-weak-notpool interchangeable / 929 checktx-weak-notsort interchangeable，也不是已经索引器已经保证不重放 interchangeable / 313 indexer interchangeable。**  
   官方把诚实节点过了 CheckTx 和对手已经守同一把尺 / 已经交差分开。看见诚实节点过了 CheckTx，不是已经交差 interchangeable。339 checktx-weak vs process bundled unbundling 在本页 item 2 续。

怎样写 CheckTx、怎样挑哪些检查留给 Process、怎样写 ProcessProposal 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **拜占庭能提案一满块无效交易 not already pool-blocked ≠ 已经被池子挡住 interchangeable：** 官方把池子弱过滤器和拜占庭可以不守分开。
- **看见能提案无效交易 not already out-of-consensus ≠ 已经进不了共识 interchangeable：** 官方把能提案无效交易和已经进不了块分开。
- **看见诚实节点过了 CheckTx not already settled ≠ 已经交差 interchangeable：** 官方把诚实节点过了 CheckTx 和已经交差分开；339 checktx-weak vs process bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 拜占庭能提案一满块无效交易 | 不是已经被池子挡住 | 不是四门已经结算（33） |
| 看见能提案无效交易 | 不是已经进不了共识 | 不是索引器已经保证不重放（313） |
| 看见诚实节点过了 CheckTx | 不是已经交差 | 不是不该验排序就已经该在 CheckTx 里验（929） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拜占庭能提案一满块无效交易 not already pool-blocked / not already out-of-consensus / not already settled 正式三事（339 余量），必须分开是不是已经被池子挡住、是不是已经进不了共识、是不是已经交差。可以跳过「看见池子会挡就已经挡住拜占庭」。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。339 checktx-weak vs process bundled unbundling 在本页 item 2 续；续 [`worked-example-checktx-weak-notproc-vs-bundled.md`](worked-example-checktx-weak-notproc-vs-bundled.md)（不变量 931 item 3）。

## 本页不抄

- 怎样写 CheckTx、怎样挑哪些检查留给 Process、怎样写 ProcessProposal。
- 弱过滤器 bundled。那是不变量 339。
- 不该验排序就已经该在 CheckTx 里验。那是不变量 339 item 1 余量 / 929。
- 四门已经结算。那是不变量 33。
- 索引器已经保证不重放。那是不变量 313。
