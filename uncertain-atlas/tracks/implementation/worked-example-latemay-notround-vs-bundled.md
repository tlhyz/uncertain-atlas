# 例：看见round 0 height h 收到上一高度 CommitRound 的 Precommit不是已经 Verify When 正式流程 bundled；看见round 0 / h-1 / CommitRound不是已经 round r height h；看见round 0 height h 收到上一高度 CommitRound 的 Precommit不是已经 ExtendVote When 正式流程 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When late-arriving MAY 段。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LateMay round0-h-1 not already normal-When / not already this-height / not already ExtendVote-When 正式三事（518 余量）/ not 1323 latemay-notround interchangeable / not 518 verifywhen-latemay-vs-bundled bundled interchangeable」，不是 verifywhen latemay vs bundled bundled（518），也不是已经 Verify When 正式流程（435），也不是已经 ExtendVote When（438）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见round 0 height h 收到上一高度 CommitRound 的 Precommit / 看见round 0 height h 收到上一高度 CommitRound 的 Precommit 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1323 latemay-notround interchangeable / 1322 latemay-notadd interchangeable，也不是已经 LateMay round0-h-1 not already normal-When / not already this-height / not already ExtendVote-When 正式三事 bundled（518 item 2 余量） interchangeable / 518 latemay item 2 interchangeable。**  
   官方把round 0 height h 收到上一高度 CommitRound 的 Precommit和已经 Verify When 正式流程 bundled写成两件。看见round 0 height h 收到上一高度 CommitRound 的 Precommit，不是已经 Verify When 正式流程 bundled。

2. **看见round 0 / h-1 / CommitRound / 看见round 0 height h 收到上一高度 CommitRound 的 Precommit / 这份对象 is not already 已经 round r height h interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1323 latemay-notround interchangeable / 1324 latemay-notcall interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把round 0 / h-1 / CommitRound和已经 round r height h写成两件。看见round 0 / h-1 / CommitRound，不是已经 round r height h。

3. **看见round 0 height h 收到上一高度 CommitRound 的 Precommit / 看见round 0 / h-1 / CommitRound / 这份对象 is not already 已经 ExtendVote When 正式流程 bundled interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1323 latemay-notround interchangeable / 1322 latemay-notadd interchangeable，也不是已经 ExtendVote When interchangeable / 438 ExtendVote When interchangeable。**  
   官方把round 0 height h 收到上一高度 CommitRound 的 Precommit和已经 ExtendVote When 正式流程 bundled写成两件。看见round 0 height h 收到上一高度 CommitRound 的 Precommit，不是已经 ExtendVote When 正式流程 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **round 0 / h-1 / CommitRound 不是正常 When interchangeable：官方把迟到 MAY 前提和正常 When round r height h 分开。**
- **看见上一高度 Precommit 不是已经 Verify When 正式流程：435 钉正常 When 四步，本页钉迟到 MAY 前提。**
- **看见 q ≠ p 不是已经 ExtendVote When 正式流程：438 钉本地 ExtendVote，本页钉收到他人迟到 Precommit。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经 round r height h | 不是已经 round r height h | 不是已经ExtendVote When（438） |
| 已经 ExtendVote When 正式流程 bundled | 不是已经 ExtendVote When 正式流程 bundled | 不是已经1322 latemay-notadd |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LateMay round0-h-1 not already normal-When / not already this-height / not already ExtendVote-When 正式三事（518 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经 round r height h、是不是已经 ExtendVote When 正式流程 bundled。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经又叫了 Verify interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。518 VerifyVoteExtension When latemay bundled unbundling 在本页 item 2 续；续 [`worked-example-latemay-notcall-vs-bundled.md`](worked-example-latemay-notcall-vs-bundled.md)（不变量 1324 item 3）。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
