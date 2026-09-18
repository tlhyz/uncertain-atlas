# 例：看见 FinalizeBlockRequest.proposer_address is not already making interchangeable / not already header-known interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事（429 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事（429 余量）/ not 1064 finend-notmaking interchangeable / not 429 finreqend-vs-procreq bundled interchangeable」，不是 Finalize 请求末栏 bundled（429），也不是 ProcessProposalRequest.proposer_address 就已经正在造这份提案（427），也不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413）。不要另写怎样写 Finalize 请求末栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址 / 看见填了 proposer_address 这份栏 is not already 已经正在造这份提案 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1064 finend-notmaking interchangeable / 1065 finend-nothead interchangeable / 429 finreqend item 2 time interchangeable，也不是已经 FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事 bundled（429 item 1 余量） interchangeable / 429 finreqend item 1 interchangeable。**  
   官方写：proposer_address 是造了这份提案的验证者地址。看见填了 proposer_address，不是已经 PrepareProposalRequest.proposer_address 那种已经正在造 interchangeable——本页从 429 item 1 侧钉 not already making 单句。429 finreqend vs procreq bundled unbundling 在本页 item 1 启动。

2. **看见造了 / 看见填了 proposer_address / 这份栏 is not already 已经知道本头哈希 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1064 finend-notmaking interchangeable / 429 finreqend item 3 syncing interchangeable / 1066 finend-nothist interchangeable，也不是已经 ProcessProposalRequest.proposer_address 就已经正在造这份提案 interchangeable / 427 procend interchangeable。**  
   官方把造了和已经知道本头哈希分开。看见造了，不是已经知道本头哈希 interchangeable。本页钉 not already header-known 单句。

3. **看见能指造了的人 / 看见填了 proposer_address / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 请求末栏 bundled（429） interchangeable / 1064 finend-notmaking interchangeable / 1065 finend-nothead interchangeable，也不是已经 ExtendVoteRequest.proposer_address 就已经知道本头哈希 interchangeable / 413 extmis interchangeable。**  
   官方把能指造了的人和已经交差分开。看见能指造了的人，不是已经交差 interchangeable。429 finreqend vs procreq bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.proposer_address not already making ≠ 已经正在造这份提案 interchangeable：** 官方把造了这份提案的验证者地址和已经正在造这份提案分开。
- **看见造了 not already header-known ≠ 已经知道本头哈希 interchangeable：** 官方把造了和已经知道本头哈希分开。
- **看见能指造了的人 not already settled ≠ 已经交差 interchangeable：** 官方把能指造了的人和已经交差分开；429 finreqend vs procreq bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.proposer_address 是造了这份提案的验证者地址 | 不是已经正在造这份提案 | 不是 ProcessProposalRequest.proposer_address 就已经正在造这份提案（427） |
| 看见造了 | 不是已经知道本头哈希 | 不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413） |
| 看见能指造了的人 | 不是已经交差 | 不是 time 就已经对上了拟议块头（1065） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事（429 余量），必须分开是不是已经正在造这份提案、是不是已经知道本头哈希、是不是已经交差。可以跳过「看见填了 Finalize 请求末栏就已经正在造这份提案」。不要另写怎样写 Finalize 请求末栏。429 finreqend vs procreq bundled unbundling 在本页 item 1 启动；续 [`worked-example-finend-nothead-vs-bundled.md`](worked-example-finend-nothead-vs-bundled.md)（不变量 1065 item 2）。

## 本页不抄

- 怎样写 Finalize 请求末栏、怎样填 proposer_address、怎样填 syncing_to_height。
- Finalize 请求末栏 bundled。那是不变量 429。
- ProcessProposalRequest.proposer_address 就已经正在造这份提案。那是不变量 427。
- ExtendVoteRequest.proposer_address 就已经知道本头哈希。那是不变量 413。
