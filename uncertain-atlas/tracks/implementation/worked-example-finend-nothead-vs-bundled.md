# 例：看见 FinalizeBlockRequest.time is not already header-aligned interchangeable / not already prepare-time interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（429 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（429 余量）/ not 1065 finend-nothead interchangeable / not 429 finreqend-vs-procreq bundled interchangeable」，不是 Finalize 请求末栏 bundled（429），也不是 PrepareProposalRequest.time 就已经对上了拟议块头（426），也不是 Finalize 的 height / time 对上拟议块头就已经验过块头。不要另写怎样写 Finalize 请求末栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.time 是已决块的时间戳 / 看见填了 time 这份栏 is not already 已经对上了拟议块头 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1065 finend-nothead interchangeable / 1064 finend-notmaking interchangeable / 429 finreqend item 1 proposer interchangeable，也不是已经 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事 bundled（429 item 2 余量） interchangeable / 429 finreqend item 2 interchangeable。**  
   官方写：time 是已决块的时间戳。看见填了 time，不是已经 Usage 里 height 和 time 值对上拟议块头那种已经验过块头 interchangeable——本页从 429 item 2 侧钉 not already header-aligned 单句。429 finreqend vs procreq bundled unbundling 在本页 item 2 续。

2. **看见有已决块时间戳 / 看见填了 time / 这份栏 is not already 已经是 PrepareProposalRequest.time interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1065 finend-nothead interchangeable / 429 finreqend item 3 syncing interchangeable / 1066 finend-nothist interchangeable，也不是已经 PrepareProposalRequest.time 就已经对上了拟议块头 interchangeable / 426 preprend interchangeable。**  
   官方把有已决块时间戳和已经是 PrepareProposalRequest.time 分开。看见有已决块时间戳，不是已经是 PrepareProposalRequest.time interchangeable。本页钉 not already prepare-time 单句。

3. **看见能指时间戳 / 看见填了 time / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1065 finend-nothead interchangeable / 1064 finend-notmaking interchangeable，也不是已经 Finalize 的 height / time 对上拟议块头就已经验过块头 interchangeable。**  
   官方把能指时间戳和已经交差分开。看见能指时间戳，不是已经交差 interchangeable。429 finreqend vs procreq bundled unbundling 在本页 item 2 续。

怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.time not already header-aligned ≠ 已经对上了拟议块头 interchangeable：** 官方把已决块的时间戳和已经对上了拟议块头分开。
- **看见有已决块时间戳 not already prepare-time ≠ 已经是 PrepareProposalRequest.time interchangeable：** 官方把有已决块时间戳和已经是 PrepareProposalRequest.time 分开。
- **看见能指时间戳 not already settled ≠ 已经交差 interchangeable：** 官方把能指时间戳和已经交差分开；429 finreqend vs procreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.time 是已决块的时间戳 | 不是已经对上了拟议块头 | 不是 PrepareProposalRequest.time 就已经对上了拟议块头（426） |
| 看见有已决块时间戳 | 不是已经是 PrepareProposalRequest.time | 不是 Prepare 请求末栏 time 就已经对上拟议块头（426） |
| 看见能指时间戳 | 不是已经交差 | 不是 syncing_to_height 就已经有完整历史（1066） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（429 余量），必须分开是不是已经对上了拟议块头、是不是已经是 PrepareProposalRequest.time、是不是已经交差。可以跳过「看见填了 Finalize 请求末栏就已经正在造这份提案」。不要另写怎样写 Finalize 请求末栏。429 finreqend vs procreq bundled unbundling 在本页 item 2 续；续 [`worked-example-finend-nothist-vs-bundled.md`](worked-example-finend-nothist-vs-bundled.md)（不变量 1066 item 3）。

## 本页不抄

- 怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height。
- Finalize 请求末栏 bundled。那是不变量 429。
- PrepareProposalRequest.time 就已经对上了拟议块头。那是不变量 426。
- Finalize 的 height / time 对上拟议块头就已经验过块头。那是相邻 Usage 页，不是本页。
