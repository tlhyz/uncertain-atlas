# 例：看见 FinalizeBlockRequest.syncing_to_height is not already full-history interchangeable / not already snapshot-restore interchangeable / not already consensus interchangeable

**层次**：实现 / FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事（429 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事（429 余量）/ not 1066 finend-nothist interchangeable / not 429 finreqend-vs-procreq bundled interchangeable」，不是 Finalize 请求末栏 bundled（429），也不是 syncing_to_height 就已经有完整历史（382），也不是快照重放就已经装回。不要另写怎样写 Finalize 请求末栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高 / 看见填了 syncing_to_height 这份栏 is not already 已经有完整历史 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1066 finend-nothist interchangeable / 1064 finend-notmaking interchangeable / 429 finreqend item 1 proposer interchangeable，也不是已经 FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事 bundled（429 item 3 余量） interchangeable / 429 finreqend item 3 interchangeable。**  
   官方写：节点在同步或重放块时，syncing_to_height 等于目标高度。否则 syncing_to_height 等于本高。看见填了目标高，不是已经有从创世的完整历史 interchangeable——本页从 429 item 3 侧钉 not already full-history 单句。429 finreqend vs procreq bundled unbundling 在本页 item 3 完成。

2. **看见在同步或重放 / 看见填了 syncing_to_height / 这份栏 is not already 已经是快照重放 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1066 finend-nothist interchangeable / 429 finreqend item 2 time interchangeable / 1065 finend-nothead interchangeable，也不是已经 syncing_to_height 就已经有完整历史 interchangeable / 382 finreq interchangeable。**  
   官方把在同步或重放和已经是快照重放分开。看见在同步或重放，不是已经是快照重放 interchangeable。本页钉 not already snapshot-restore 单句。

3. **看见能指同步状态 / 看见填了 syncing_to_height / 这份栏 is not already 已经切进共识 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1066 finend-nothist interchangeable / 1064 finend-notmaking interchangeable，也不是已经快照装回就已经交差 interchangeable。**  
   官方把能指同步状态和已经切进共识分开。看见能指同步状态，不是已经切进共识 interchangeable。429 finreqend vs procreq bundled unbundling 在本页 item 3 完成。

怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.syncing_to_height not already full-history ≠ 已经有完整历史 interchangeable：** 官方把同步高度标记和已经有完整历史分开。
- **看见在同步或重放 not already snapshot-restore ≠ 已经是快照重放 interchangeable：** 官方把在同步或重放和已经是快照重放分开。
- **看见能指同步状态 not already consensus ≠ 已经切进共识 interchangeable：** 官方把能指同步状态和已经切进共识分开；429 finreqend vs procreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.syncing_to_height 同步或重放时是目标高、否则等于本高 | 不是已经有完整历史 | 不是 syncing_to_height 就已经有完整历史（382） |
| 看见在同步或重放 | 不是已经是快照重放 | 不是快照重放就已经装回 |
| 看见能指同步状态 | 不是已经切进共识 | 不是 proposer_address 就已经正在造这份提案（1064） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事（429 余量），必须分开是不是已经有完整历史、是不是已经是快照重放、是不是已经切进共识。可以跳过「看见填了 Finalize 请求末栏就已经正在造这份提案」。不要另写怎样写 Finalize 请求末栏。429 finreqend vs procreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height。
- Finalize 请求末栏 bundled。那是不变量 429。
- syncing_to_height 就已经有完整历史。那是不变量 382。
- 快照重放就已经装回。那是相邻快照页，不是本页。
