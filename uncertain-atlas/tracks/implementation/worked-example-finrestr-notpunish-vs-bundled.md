# 例：看见 FinalizeBlockRequest.misbehavior is not already rewarded interchangeable / not already process-mis interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（428 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（428 余量）/ not 1062 finrestr-notpunish interchangeable / not 428 finreqrest-vs-procreq bundled interchangeable」，不是 Finalize 请求余栏 bundled（428），也不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363），也不是 ProcessProposalRequest.misbehavior 就已经定奖惩（420）。不要另写怎样写 Finalize 请求余栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.misbehavior 是过错验证者信息列表 / 看见填了 misbehavior 这份栏 is not already 已经定奖惩 interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1062 finrestr-notpunish interchangeable / 1061 finrestr-nothash interchangeable / 428 finreqrest item 1 hash interchangeable，也不是已经 FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事 bundled（428 item 2 余量） interchangeable / 428 finreqrest item 2 interchangeable。**  
   官方写：misbehavior 是过错验证者信息列表。看见填了 misbehavior，不是已经可以用 decided_last_commit 和 misbehavior 定奖惩那种已经罚没 interchangeable——本页从 428 item 2 侧钉 not already rewarded 单句。428 finreqrest vs procreq bundled unbundling 在本页 item 2 续。

2. **看见有过错列表 / 看见填了 misbehavior / 这份栏 is not already 已经是 ProcessProposalRequest.misbehavior interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1062 finrestr-notpunish interchangeable / 428 finreqrest item 3 next_hash interchangeable / 1063 finrestr-notproc interchangeable，也不是已经可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没 interchangeable / 363 finresp interchangeable。**  
   官方把有过错列表和已经是 ProcessProposalRequest.misbehavior 分开。看见有过错列表，不是已经是 ProcessProposalRequest.misbehavior interchangeable。本页钉 not already process-mis 单句。

3. **看见能指过错 / 看见填了 misbehavior / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1062 finrestr-notpunish interchangeable / 1061 finrestr-nothash interchangeable，也不是已经 ProcessProposalRequest.misbehavior 就已经定奖惩 interchangeable / 420 procrestr interchangeable。**  
   官方把能指过错和已经交差分开。看见能指过错，不是已经交差 interchangeable。428 finreqrest vs procreq bundled unbundling 在本页 item 2 续。

怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.misbehavior not already rewarded ≠ 已经定奖惩 interchangeable：** 官方把过错验证者信息列表和已经定奖惩分开。
- **看见有过错列表 not already process-mis ≠ 已经是 ProcessProposalRequest.misbehavior interchangeable：** 官方把有过错列表和已经是 ProcessProposalRequest.misbehavior 分开。
- **看见能指过错 not already settled ≠ 已经交差 interchangeable：** 官方把能指过错和已经交差分开；428 finreqrest vs procreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.misbehavior 是过错验证者信息列表 | 不是已经定奖惩 | 不是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没（363） |
| 看见有过错列表 | 不是已经是 ProcessProposalRequest.misbehavior | 不是 ProcessProposalRequest.misbehavior 就已经定奖惩（420） |
| 看见能指过错 | 不是已经交差 | 不是 next_validators_hash 就已经是 Process 请求末栏（1063） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.misbehavior not already rewarded / not already process-mis / not already settled 正式三事（428 余量），必须分开是不是已经定奖惩、是不是已经是 ProcessProposalRequest.misbehavior、是不是已经交差。可以跳过「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash」。不要另写怎样写 Finalize 请求余栏。428 finreqrest vs procreq bundled unbundling 在本页 item 2 续；续 [`worked-example-finrestr-notproc-vs-bundled.md`](worked-example-finrestr-notproc-vs-bundled.md)（不变量 1063 item 3）。

## 本页不抄

- 怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior。
- Finalize 请求余栏 bundled。那是不变量 428。
- 可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没。那是不变量 363。
- ProcessProposalRequest.misbehavior 就已经定奖惩。那是不变量 420。
