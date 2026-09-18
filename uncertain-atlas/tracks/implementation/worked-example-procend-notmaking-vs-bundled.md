# 例：看见 ProcessProposalRequest.proposer_address is not already making interchangeable / not already header-known interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalRequest.proposer_address not already making / not already header-known / not already settled 正式三事（427 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.proposer_address not already making / not already header-known / not already settled 正式三事（427 余量）/ not 1059 procend-notmaking interchangeable / not 427 procreqend-vs-prepreq bundled interchangeable」，不是 Process 请求末栏 bundled（427），也不是 PrepareProposalRequest.proposer_address 就已经正在造（426），也不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413）。不要另写怎样写 Process 请求末栏。

## 官方三件事

1. **看见 ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址 / 看见填了 proposer_address 这份栏 is not already 已经正在造这份提案 interchangeable，也不是已经 Process 请求末栏 bundled（427） interchangeable / 1059 procend-notmaking interchangeable / 1058 procend-nothash interchangeable / 427 procreqend item 1 next_hash interchangeable，也不是已经 ProcessProposalRequest.proposer_address not already making / not already header-known / not already settled 正式三事 bundled（427 item 2 余量） interchangeable / 427 procreqend item 2 interchangeable。**  
   官方写：proposer_address 是造了这份提案的验证者地址。看见填了 proposer_address，不是已经 PrepareProposalRequest.proposer_address 那种已经正在造 interchangeable——本页从 427 item 2 侧钉 not already making 单句。427 procreqend vs prepreq bundled unbundling 在本页 item 2 续。

2. **看见造了 / 看见填了 proposer_address / 这份栏 is not already 已经知道本头哈希 interchangeable，也不是已经 Process 请求末栏 bundled（427） interchangeable / 1059 procend-notmaking interchangeable / 427 procreqend item 3 resp-txs interchangeable / 1060 procend-notprelim interchangeable，也不是已经 ExtendVoteRequest.proposer_address 就已经知道本头哈希 interchangeable / 413 extmis interchangeable。**  
   官方把造了和已经知道本头哈希分开。看见造了，不是已经知道本头哈希 interchangeable。本页钉 not already header-known 单句。

3. **看见能指造了的人 / 看见填了 proposer_address / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求末栏 bundled（427） interchangeable / 1059 procend-notmaking interchangeable / 1058 procend-nothash interchangeable，也不是已经 PrepareProposalRequest.proposer_address 就已经正在造 interchangeable / 426 preprend interchangeable。**  
   官方把能指造了的人和已经交差分开。看见能指造了的人，不是已经交差 interchangeable。427 procreqend vs prepreq bundled unbundling 在本页 item 2 续。

怎样写 Process 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.proposer_address not already making ≠ 已经正在造这份提案 interchangeable：** 官方把造了这份提案的验证者地址和已经正在造这份提案分开。
- **看见造了 not already header-known ≠ 已经知道本头哈希 interchangeable：** 官方把造了和已经知道本头哈希分开。
- **看见能指造了的人 not already settled ≠ 已经交差 interchangeable：** 官方把能指造了的人和已经交差分开；427 procreqend vs prepreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.proposer_address 是造了这份提案的验证者地址 | 不是已经正在造这份提案 | 不是 PrepareProposalRequest.proposer_address 就已经正在造（426） |
| 看见造了 | 不是已经知道本头哈希 | 不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413） |
| 看见能指造了的人 | 不是已经交差 | 不是 PrepareProposalResponse.txs 就已经是初步交易列表（1060） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.proposer_address not already making / not already header-known / not already settled 正式三事（427 余量），必须分开是不是已经正在造这份提案、是不是已经知道本头哈希、是不是已经交差。可以跳过「看见填了 Process 请求末栏就已经是 Prepare 请求末栏的 next_validators_hash」。不要另写怎样写 Process 请求末栏。427 procreqend vs prepreq bundled unbundling 在本页 item 2 续；续 [`worked-example-procend-notprelim-vs-bundled.md`](worked-example-procend-notprelim-vs-bundled.md)（不变量 1060 item 3）。

## 本页不抄

- 怎样写 Process 请求末栏、怎样填 next_validators_hash、怎样填 proposer_address。
- Process 请求末栏 bundled。那是不变量 427。
- PrepareProposalRequest.proposer_address 就已经正在造。那是不变量 426。
- ExtendVoteRequest.proposer_address 就已经知道本头哈希。那是不变量 413。
