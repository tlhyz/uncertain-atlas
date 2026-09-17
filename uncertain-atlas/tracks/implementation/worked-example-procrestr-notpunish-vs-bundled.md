# 例：看见 ProcessProposalRequest.misbehavior is not already rewarded interchangeable / not already slashed interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalRequest.misbehavior not already rewarded / not already slashed / not already settled 正式三事（420 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.misbehavior not already rewarded / not already slashed / not already settled 正式三事（420 余量）/ not 1030 procrestr-notpunish interchangeable / not 420 procreqrest-vs-extreq bundled interchangeable」，不是 Process 请求余栏 bundled（420），也不是 ExtendVoteRequest.misbehavior 就已经定奖惩（413），也不是过错枚举就已经罚没（372）。不要另写怎样写 Process 请求余栏。

## 官方三件事

1. **看见 ProcessProposalRequest.misbehavior 是过错验证者信息列表 / 看见填了 misbehavior 这份栏 is not already 已经定奖惩 interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1030 procrestr-notpunish interchangeable / 1028 procrestr-notlocal interchangeable / 420 procreqrest item 1 proposed_last_commit interchangeable，也不是已经 ProcessProposalRequest.misbehavior not already rewarded / not already slashed / not already settled 正式三事 bundled（420 item 3 余量） interchangeable / 420 procreqrest item 3 interchangeable。**  
   官方写：misbehavior 是过错验证者信息列表。看见填了 misbehavior，不是已经 ExtendVoteRequest.misbehavior 那种已经定奖惩 interchangeable——本页从 420 item 3 侧钉 not already rewarded 单句。420 procreqrest vs extreq bundled unbundling 在本页 item 3 完成。

2. **看见有过错列表 / 看见填了 misbehavior / 这份栏 is not already 已经罚没 interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1030 procrestr-notpunish interchangeable / 420 procreqrest item 2 time interchangeable / 1029 procrestr-notts interchangeable，也不是已经 ExtendVoteRequest.misbehavior 就已经定奖惩 interchangeable / 413 extreqmis interchangeable。**  
   官方把有过错列表和已经罚没分开。看见有过错列表，不是已经罚没 interchangeable。本页钉 not already slashed 单句。

3. **看见能指过错 / 看见填了 misbehavior / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1030 procrestr-notpunish interchangeable / 1028 procrestr-notlocal interchangeable，也不是已经过错枚举就已经罚没 interchangeable / 372 misbehavior-vs-enum interchangeable。**  
   官方把能指过错和已经交差分开。看见能指过错，不是已经交差 interchangeable。420 procreqrest vs extreq bundled unbundling 在本页 item 3 完成。

怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.misbehavior not already rewarded ≠ 已经定奖惩 interchangeable：** 官方把 Process 请求表上这份过错列表和 ExtendVote 请求表上那份拟议块里的过错信息分开。
- **看见有过错列表 not already slashed ≠ 已经罚没 interchangeable：** 官方把有过错列表和已经罚没分开。
- **看见能指过错 not already settled ≠ 已经交差 interchangeable：** 官方把能指过错和已经交差分开；420 procreqrest vs extreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.misbehavior 是过错验证者信息列表 | 不是已经定奖惩 | 不是 ExtendVoteRequest.misbehavior 就已经定奖惩（413） |
| 看见有过错列表 | 不是已经罚没 | 不是过错枚举就已经罚没（372） |
| 看见能指过错 | 不是已经交差 | 不是 proposed_last_commit 就已经交差 local_last_commit（1028） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.misbehavior not already rewarded / not already slashed / not already settled 正式三事（420 余量），必须分开是不是已经定奖惩、是不是已经罚没、是不是已经交差。可以跳过「看见填了 Process 请求余栏就已经交差 local_last_commit」。不要另写怎样写 Process 请求余栏。420 procreqrest vs extreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time。
- Process 请求余栏 bundled。那是不变量 420。
- ExtendVoteRequest.misbehavior 就已经定奖惩。那是不变量 413。
- 过错枚举就已经罚没。那是不变量 372。
