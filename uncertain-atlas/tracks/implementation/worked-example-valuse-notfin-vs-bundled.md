# 例：看见Finalize decided_last_commit 不是已经 Process proposed_last_commit不是已经是 Process proposed_last_commit；看见Finalize decided_last_commit is not already Process proposed_last_commit不是已经交差；看见Finalize decided_last_commit 不是已经 Process proposed_last_commit不是已经可以拿 Prepare Extended 代替

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ValUse Finalize decided_last_commit Validator not already Process proposed / not already settled / not already Prepare-ext 正式三事（449 余量）/ not 1372 valuse-notfin interchangeable / not 449 validatorusage-vs-gates bundled interchangeable」，不是 validatorusage vs gates bundled（449），也不是已经 VoteInfo 能按到场定奖惩就已经罚没（365），也不是已经 Validator address 就已经带公钥（364）。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。

## 官方三件事

1. **看见Finalize decided_last_commit 不是已经 Process proposed_last_commit / 看见Finalize decided_last_commit 不是已经 Process proposed_last_commit 这份对象 is not already 已经是 Process proposed_last_commit interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1372 valuse-notfin interchangeable / 1371 valuse-notproc interchangeable，也不是已经 ValUse Finalize decided_last_commit Validator not already Process proposed / not already settled / not already Prepare-ext 正式三事 bundled（449 item 2 余量） interchangeable / 449 valuse item 2 interchangeable。**  
   官方把Finalize decided_last_commit 不是已经 Process proposed_last_commit和已经是 Process proposed_last_commit写成两件。看见Finalize decided_last_commit 不是已经 Process proposed_last_commit，不是已经是 Process proposed_last_commit。

2. **看见Finalize decided_last_commit is not already Process proposed_last_commit / 看见Finalize decided_last_commit 不是已经 Process proposed_last_commit / 这份对象 is not already 已经交差 interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1372 valuse-notfin interchangeable / 1373 valuse-notprep interchangeable，也不是已经 VoteInfo 能按到场定奖惩就已经罚没 interchangeable / 365 VoteInfo 能按到场定奖惩就已经罚没 interchangeable。**  
   官方把Finalize decided_last_commit is not already Process proposed_last_commit和已经交差写成两件。看见Finalize decided_last_commit is not already Process proposed_last_commit，不是已经交差。

3. **看见Finalize decided_last_commit 不是已经 Process proposed_last_commit / 看见Finalize decided_last_commit is not already Process proposed_last_commit / 这份对象 is not already 已经可以拿 Prepare Extended 代替 interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1372 valuse-notfin interchangeable / 1371 valuse-notproc interchangeable，也不是已经 Validator address 就已经带公钥 interchangeable / 364 Validator address 就已经带公钥 interchangeable。**  
   官方把Finalize decided_last_commit 不是已经 Process proposed_last_commit和已经可以拿 Prepare Extended 代替写成两件。看见Finalize decided_last_commit 不是已经 Process proposed_last_commit，不是已经可以拿 Prepare Extended 代替。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。

## 官方为什么这样拆

- **Finalize decided 不是已经 Process proposed interchangeable：官方把已决块和拟议块分开。**
- **看见 decided 不是已经交差。**
- **看见 Finalize 的 Validator 不是已经可以拿 Prepare Extended 代替。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 Process proposed_last_commit | 不是已经是 Process proposed_last_commit | 不是已经VoteInfo 能按到场定奖惩就已经罚没（365） |
| 已经交差 | 不是已经交差 | 不是已经Validator address 就已经带公钥（364） |
| 已经可以拿 Prepare Extended 代替 | 不是已经可以拿 Prepare Extended 代替 | 不是已经1371 valuse-notproc |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValUse Finalize decided_last_commit Validator not already Process proposed / not already settled / not already Prepare-ext 正式三事（449 余量），必须分开是不是已经是 Process proposed_last_commit、是不是已经交差、是不是已经可以拿 Prepare Extended 代替。可以跳过「看见四门里都有 Validator 就已经同一门」。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。449 Validator Usage four-gate mapping bundled unbundling 在本页 item 2 续；续 [`worked-example-valuse-notprep-vs-bundled.md`](worked-example-valuse-notprep-vs-bundled.md)（不变量 1373 item 3）。

## 本页不抄

- 怎样写 Validator Usage 四门映射正式三事、怎样填 proposed_last_commit / decided_last_commit / local_last_commit。
- 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。
