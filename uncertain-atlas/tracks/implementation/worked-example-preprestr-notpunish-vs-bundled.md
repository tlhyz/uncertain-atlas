# 例：看见 PrepareProposalRequest.misbehavior is not already rewarded interchangeable / not already process-mis interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（424 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（424 余量）/ not 1051 preprestr-notpunish interchangeable / not 424 prepreqrest-vs-procreq bundled interchangeable」，不是 Prepare 请求余栏 bundled（424），也不是 ProcessProposalRequest.misbehavior 就已经定奖惩（420），也不是 ExtendVoteRequest.misbehavior 就已经定奖惩（413）。不要另写怎样写 Prepare 请求余栏。

## 官方三件事

1. **看见 PrepareProposalRequest.misbehavior 是过错验证者信息列表 / 看见填了 misbehavior 这份栏 is not already 已经定奖惩 interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1051 preprestr-notpunish interchangeable / 1049 preprestr-notlocal interchangeable / 424 prepreqrest item 1 local_last_commit interchangeable，也不是已经 PrepareProposalRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事 bundled（424 item 3 余量） interchangeable / 424 prepreqrest item 3 interchangeable。**  
   官方写：misbehavior 是过错验证者信息列表。看见填了 misbehavior，不是已经 ProcessProposalRequest.misbehavior 那种已经定奖惩 interchangeable——本页从 424 item 3 侧钉 not already rewarded 单句。424 prepreqrest vs procreq bundled unbundling 在本页 item 3 完成。

2. **看见有过错列表 / 看见填了 misbehavior / 这份栏 is not already 已经是 ProcessProposalRequest.misbehavior interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1051 preprestr-notpunish interchangeable / 424 prepreqrest item 2 time interchangeable / 1050 preprestr-notts interchangeable，也不是已经 ExtendVoteRequest.misbehavior 就已经定奖惩 interchangeable / 413 extmis interchangeable。**  
   官方把有过错列表和已经是 ProcessProposalRequest.misbehavior 分开。看见有过错列表，不是已经是 ProcessProposalRequest.misbehavior interchangeable。本页钉 not already process-mis 单句。

3. **看见能指过错 / 看见填了 misbehavior / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1051 preprestr-notpunish interchangeable / 1049 preprestr-notlocal interchangeable，也不是已经可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没 interchangeable / 363 finresp interchangeable。**  
   官方把能指过错和已经交差分开。看见能指过错，不是已经交差 interchangeable。424 prepreqrest vs procreq bundled unbundling 在本页 item 3 完成。

怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.misbehavior not already rewarded ≠ 已经定奖惩 interchangeable：** 官方把过错验证者信息列表和已经定奖惩分开。
- **看见有过错列表 not already process-mis ≠ 已经是 ProcessProposalRequest.misbehavior interchangeable：** 官方把有过错列表和已经是 ProcessProposalRequest.misbehavior 分开。
- **看见能指过错 not already settled ≠ 已经交差 interchangeable：** 官方把能指过错和已经交差分开；424 prepreqrest vs procreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.misbehavior 是过错验证者信息列表 | 不是已经定奖惩 | 不是 ProcessProposalRequest.misbehavior 就已经定奖惩（420） |
| 看见有过错列表 | 不是已经是 ProcessProposalRequest.misbehavior | 不是 ExtendVoteRequest.misbehavior 就已经定奖惩（413） |
| 看见能指过错 | 不是已经交差 | 不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（424 余量），必须分开是不是已经定奖惩、是不是已经是 ProcessProposalRequest.misbehavior、是不是已经交差。可以跳过「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit」。不要另写怎样写 Prepare 请求余栏。424 prepreqrest vs procreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time。
- Prepare 请求余栏 bundled。那是不变量 424。
- ProcessProposalRequest.misbehavior 就已经定奖惩。那是不变量 420。
- ExtendVoteRequest.misbehavior 就已经定奖惩。那是不变量 413。
