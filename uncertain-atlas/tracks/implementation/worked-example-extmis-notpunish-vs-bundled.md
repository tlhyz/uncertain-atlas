# 例：看见 ExtendVoteRequest.misbehavior is not already rewarded interchangeable / not already settled interchangeable / not already slashed interchangeable

**层次**：实现 / ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事（413 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事（413 余量）/ not 1037 extmis-notpunish interchangeable / not 413 extreqmis-vs-reward bundled interchangeable」，不是 ExtendVote 请求末栏 bundled（413），也不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363），也不是 ProcessProposalRequest.misbehavior 就已经定奖惩（420）。不要另写怎样写 ExtendVote 请求末栏。

## 官方三件事

1. **看见 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息 / 看见填了 misbehavior 这份栏 is not already 已经定奖惩 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1037 extmis-notpunish interchangeable / 1038 extmis-notheader interchangeable / 413 extreqmis item 2 proposer interchangeable，也不是已经 ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事 bundled（413 item 1 余量） interchangeable / 413 extreqmis item 1 interchangeable。**  
   官方写：misbehavior 是拟议块里那些验证者过错信息。看见填了 misbehavior，不是已经 Finalize 可以用 decided_last_commit 和 misbehavior 定奖惩那种已经罚没 interchangeable——本页从 413 item 1 侧钉 not already rewarded 单句。413 extreqmis vs reward bundled unbundling 在本页 item 1 启动。

2. **看见拟议块里有过错信息 / 看见填了 misbehavior / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1037 extmis-notpunish interchangeable / 413 extreqmis item 3 validator_address interchangeable / 1039 extmis-notkey interchangeable，也不是已经可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没 interchangeable / 363 finresp interchangeable。**  
   官方把拟议块里有过错信息和已经交差分开。看见拟议块里有过错信息，不是已经交差 interchangeable。本页钉 not already settled 单句。

3. **看见能指过错 / 看见填了 misbehavior / 这份栏 is not already 已经定了奖惩 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1037 extmis-notpunish interchangeable / 1038 extmis-notheader interchangeable，也不是已经 ProcessProposalRequest.misbehavior 就已经定奖惩 interchangeable / 420 procreqrest interchangeable。**  
   官方把能指过错和已经定了奖惩分开。看见能指过错，不是已经定了奖惩 interchangeable。413 extreqmis vs reward bundled unbundling 在本页 item 1 启动。

怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.misbehavior not already rewarded ≠ 已经定奖惩 interchangeable：** 官方把拟议块里那些过错信息和已经定奖惩分开。
- **看见拟议块里有过错信息 not already settled ≠ 已经交差 interchangeable：** 官方把拟议块里有过错信息和已经交差分开。
- **看见能指过错 not already slashed ≠ 已经定了奖惩 interchangeable：** 官方把能指过错和已经定了奖惩分开；413 extreqmis vs reward bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.misbehavior 是拟议块里那些过错信息 | 不是已经定奖惩 | 不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363） |
| 看见拟议块里有过错信息 | 不是已经交差 | 不是 ProcessProposalRequest.misbehavior 就已经定奖惩（420） |
| 看见能指过错 | 不是已经定了奖惩 | 不是 proposer_address 就已经知道本头哈希（1038） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事（413 余量），必须分开是不是已经定奖惩、是不是已经交差、是不是已经定了奖惩。可以跳过「看见填了 ExtendVote 请求末栏就已经定奖惩」。不要另写怎样写 ExtendVote 请求末栏。413 extreqmis vs reward bundled unbundling 在本页 item 1 启动；续 [`worked-example-extmis-notheader-vs-bundled.md`](worked-example-extmis-notheader-vs-bundled.md)（不变量 1038 item 2）。

## 本页不抄

- 怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address。
- ExtendVote 请求末栏 bundled。那是不变量 413。
- 可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没。那是不变量 363。
- ProcessProposalRequest.misbehavior 就已经定奖惩。那是不变量 420。
