# 例：看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo不是已经是 Process/Finalize 的 CommitInfo；看见Prepare ExtendedCommitInfo Validator is not already Process/Finalize CommitInfo不是已经可以拿 CommitInfo 代替；看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo不是已经从块里抽出

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ValUse Prepare ExtendedCommitInfo Validator not already Process-Finalize CommitInfo / not already interchangeable / not already 369-extract 正式三事（449 余量）/ not 1373 valuse-notprep interchangeable / not 449 validatorusage-vs-gates bundled interchangeable」，不是 validatorusage vs gates bundled（449），也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369），也不是已经 VoteInfo 抽出路径（442）。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。

## 官方三件事

1. **看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo / 看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo 这份对象 is not already 已经是 Process/Finalize 的 CommitInfo interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1373 valuse-notprep interchangeable / 1371 valuse-notproc interchangeable，也不是已经 ValUse Prepare ExtendedCommitInfo Validator not already Process-Finalize CommitInfo / not already interchangeable / not already 369-extract 正式三事 bundled（449 item 3 余量） interchangeable / 449 valuse item 3 interchangeable。**  
   官方把Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo和已经是 Process/Finalize 的 CommitInfo写成两件。看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo，不是已经是 Process/Finalize 的 CommitInfo。

2. **看见Prepare ExtendedCommitInfo Validator is not already Process/Finalize CommitInfo / 看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo / 这份对象 is not already 已经可以拿 CommitInfo 代替 interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1373 valuse-notprep interchangeable / 1372 valuse-notfin interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable / 369 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable。**  
   官方把Prepare ExtendedCommitInfo Validator is not already Process/Finalize CommitInfo和已经可以拿 CommitInfo 代替写成两件。看见Prepare ExtendedCommitInfo Validator is not already Process/Finalize CommitInfo，不是已经可以拿 CommitInfo 代替。

3. **看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo / 看见Prepare ExtendedCommitInfo Validator is not already Process/Finalize CommitInfo / 这份对象 is not already 已经从块里抽出 interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1373 valuse-notprep interchangeable / 1371 valuse-notproc interchangeable，也不是已经 VoteInfo 抽出路径 interchangeable / 442 VoteInfo 抽出路径 interchangeable。**  
   官方把Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo和已经从块里抽出写成两件。看见Prepare ExtendedCommitInfo Validator 不是已经 Process/Finalize CommitInfo，不是已经从块里抽出。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。

## 官方为什么这样拆

- **Prepare ExtendedCommitInfo 不是已经 Process/Finalize CommitInfo interchangeable：官方把 Extended 结构和 CommitInfo 分开写进不同门。**
- **看见可以带扩展 不是已经和 CommitInfo interchangeable。**
- **看见 local process 不是已经 VoteInfo 从块里抽出。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 Process/Finalize 的 CommitInfo | 不是已经是 Process/Finalize 的 CommitInfo | 不是已经ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| 已经可以拿 CommitInfo 代替 | 不是已经可以拿 CommitInfo 代替 | 不是已经VoteInfo 抽出路径（442） |
| 已经从块里抽出 | 不是已经从块里抽出 | 不是已经1371 valuse-notproc |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValUse Prepare ExtendedCommitInfo Validator not already Process-Finalize CommitInfo / not already interchangeable / not already 369-extract 正式三事（449 余量），必须分开是不是已经是 Process/Finalize 的 CommitInfo、是不是已经可以拿 CommitInfo 代替、是不是已经从块里抽出。可以跳过「看见四门里都有 Validator 就已经同一门」。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。449 Validator Usage four-gate mapping bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样写 Validator Usage 四门映射正式三事、怎样填 proposed_last_commit / decided_last_commit / local_last_commit。
- 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。
