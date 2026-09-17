# 例：看见 ProcessProposal 对付这种行为 is not already CheckTx interchangeable / not already Finalize interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposal 对付这种行为 not already CheckTx / not already Finalize / not already settled 正式三事（339 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ProcessProposal 对付这种行为 not already CheckTx / not already Finalize / not already settled 正式三事（339 余量）/ not 931 checktx-weak-notproc interchangeable / not 339 checktx-weak-vs-process bundled interchangeable」，不是弱过滤器 bundled（339），也不是索引器已经保证不重放（313），也不是 CheckTx 振荡就已经稳定（328）。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。

## 官方三件事

1. **看见从 ABCI 1.0 起有 ProcessProposal 对付这种行为 / 看见规范点名 ProcessProposal 这份门 is not already 已经是 CheckTx interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 931 checktx-weak-notproc interchangeable / 929 checktx-weak-notsort interchangeable / 339 checktx-weak item 1 排序 interchangeable，也不是已经 ProcessProposal 对付这种行为 not already CheckTx / not already Finalize / not already settled 正式三事 bundled（339 item 3 余量） interchangeable / 339 checktx-weak item 3 interchangeable。**  
   官方写：从 ABCI 1.0 起，对付这种行为的机制是 ProcessProposal。看见有 ProcessProposal，不是已经是 CheckTx interchangeable——本页从 339 item 3 侧钉 not already CheckTx 单句。339 checktx-weak vs process bundled unbundling 在本页 item 3 完成。

2. **看见点名了这道门 / 看见会拒提案 / 这份门 is not already 已经是 Finalize interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 931 checktx-weak-notproc interchangeable / 339 checktx-weak item 2 拜占庭 interchangeable / 930 checktx-weak-notpool interchangeable，也不是已经索引器已经保证不重放 interchangeable / 313 indexer interchangeable。**  
   官方把点名了这道门和已经 Finalize 分开——339 bundled 第三件事常与 313 混成「看见 ProcessProposal 就已经是 CheckTx 或已经交差 interchangeable」，本页钉 not already Finalize 单句。

3. **看见会拒提案 / 看见有 ProcessProposal / 这份门 is not already 已经交差 interchangeable，也不是已经弱过滤器 bundled（339） interchangeable / 931 checktx-weak-notproc interchangeable / 929 checktx-weak-notsort interchangeable，也不是已经 CheckTx 振荡就已经稳定 interchangeable / 328 checktx-oscillate interchangeable。**  
   官方把会拒提案和已经在池子里挡完 / 已经交差分开。看见会拒提案，不是已经交差 interchangeable。339 checktx-weak vs process bundled unbundling 在本页 item 3 完成。

怎样写 CheckTx、怎样挑哪些检查留给 Process、怎样写 ProcessProposal 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposal 对付这种行为 not already CheckTx ≠ 已经是 CheckTx interchangeable：** 官方把这道门写成对付拜占庭不守 CheckTx 的机制，不是 CheckTx 自己。
- **看见点名了这道门 not already Finalize ≠ 已经是 Finalize interchangeable：** 官方把点名 ProcessProposal 和已经 Finalize 分开。
- **看见会拒提案 not already settled ≠ 已经交差 interchangeable：** 官方把会拒提案和已经在池子里挡完 / 已经交差分开；339 checktx-weak vs process bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposal 对付这种行为 | 不是已经是 CheckTx | 不是索引器已经保证不重放（313） |
| 看见点名了这道门 | 不是已经是 Finalize | 不是 CheckTx 振荡就已经稳定（328） |
| 看见会拒提案 | 不是已经交差 | 不是不该验排序就已经该在 CheckTx 里验（929） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal 对付这种行为 not already CheckTx / not already Finalize / not already settled 正式三事（339 余量），必须分开是不是已经是 CheckTx、是不是已经是 Finalize、是不是已经交差。可以跳过「看见有 ProcessProposal 就已经是 CheckTx」。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。339 checktx-weak vs process bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 CheckTx、怎样挑哪些检查留给 Process、怎样写 ProcessProposal。
- 弱过滤器 bundled。那是不变量 339。
- 不该验排序就已经该在 CheckTx 里验。那是不变量 339 item 1 余量 / 929。
- 索引器已经保证不重放。那是不变量 313。
- CheckTx 振荡就已经稳定。那是不变量 328。
