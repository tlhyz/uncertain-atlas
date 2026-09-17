# 例：看见 ExtendVoteRequest.proposer_address is not already header-known interchangeable / not already processed interchangeable / not already settled interchangeable

**层次**：实现 / ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事（413 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事（413 余量）/ not 1038 extmis-notheader interchangeable / not 413 extreqmis-vs-reward bundled interchangeable」，不是 ExtendVote 请求末栏 bundled（413），也不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359），也不是候选没有头哈希就已经知道本头（311）。不要另写怎样写 ExtendVote 请求末栏。

## 官方三件事

1. **看见 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址 / 看见填了 proposer_address 这份栏 is not already 已经知道本头哈希 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1038 extmis-notheader interchangeable / 1037 extmis-notpunish interchangeable / 413 extreqmis item 1 misbehavior interchangeable，也不是已经 ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事 bundled（413 item 2 余量） interchangeable / 413 extreqmis item 2 interchangeable。**  
   官方写：proposer_address 是造这份提案的验证者地址。看见填了 proposer_address，不是已经 Prepare 那种 height / time / proposer_address 对上拟议头就已经知道本头哈希 interchangeable——本页从 413 item 2 侧钉 not already header-known 单句。413 extreqmis vs reward bundled unbundling 在本页 item 2 续。

2. **看见有造提案的人 / 看见填了 proposer_address / 这份栏 is not already 已经字段名对上就已经跑过 Process interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1038 extmis-notheader interchangeable / 413 extreqmis item 3 validator_address interchangeable / 1039 extmis-notkey interchangeable，也不是已经 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希 interchangeable / 359 samefields interchangeable。**  
   官方把有造提案的人和已经字段名对上就已经跑过 Process 分开。看见有造提案的人，不是已经字段名对上就已经跑过 Process interchangeable。本页钉 not already processed 单句。

3. **看见能指提议者 / 看见填了 proposer_address / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1038 extmis-notheader interchangeable / 1037 extmis-notpunish interchangeable，也不是已经候选没有头哈希就已经知道本头 interchangeable / 311 candidate interchangeable。**  
   官方把能指提议者和已经交差分开。看见能指提议者，不是已经交差 interchangeable。413 extreqmis vs reward bundled unbundling 在本页 item 2 续。

怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.proposer_address not already header-known ≠ 已经知道本头哈希 interchangeable：** 官方把造这份提案的验证者地址和已经知道本头哈希分开。
- **看见有造提案的人 not already processed ≠ 已经字段名对上就已经跑过 Process interchangeable：** 官方把有造提案的人和已经字段名对上就已经跑过 Process 分开。
- **看见能指提议者 not already settled ≠ 已经交差 interchangeable：** 官方把能指提议者和已经交差分开；413 extreqmis vs reward bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.proposer_address 是造这份提案的验证者地址 | 不是已经知道本头哈希 | 不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359） |
| 看见有造提案的人 | 不是已经字段名对上就已经跑过 Process | 不是候选没有头哈希就已经知道本头（311） |
| 看见能指提议者 | 不是已经交差 | 不是 validator_address 就已经带了公钥（1039） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.proposer_address not already header-known / not already processed / not already settled 正式三事（413 余量），必须分开是不是已经知道本头哈希、是不是已经字段名对上就已经跑过 Process、是不是已经交差。可以跳过「看见填了 ExtendVote 请求末栏就已经定奖惩」。不要另写怎样写 ExtendVote 请求末栏。413 extreqmis vs reward bundled unbundling 在本页 item 2 续；续 [`worked-example-extmis-notkey-vs-bundled.md`](worked-example-extmis-notkey-vs-bundled.md)（不变量 1039 item 3）。

## 本页不抄

- 怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address。
- ExtendVote 请求末栏 bundled。那是不变量 413。
- Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希。那是不变量 359。
- 候选没有头哈希就已经知道本头。那是不变量 311。
