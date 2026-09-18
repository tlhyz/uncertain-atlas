# 例：看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo不是已经是 Prepare 的 ExtendedCommitInfo；看见Process CommitInfo Validator is not already Prepare ExtendedCommitInfo不是已经是 local_last_commit 同一份；看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo不是已经带了公钥

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Validator Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ValUse Process CommitInfo Validator not already Prepare ExtendedCommitInfo / not already local_last_commit / not already 364-pubkey 正式三事（449 余量）/ not 1371 valuse-notproc interchangeable / not 449 validatorusage-vs-gates bundled interchangeable」，不是 validatorusage vs gates bundled（449），也不是已经 Validator 用 address 认人就已经带了公钥（364），也不是已经 ExtendedVoteInfo 从本进程抽出（369）。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。

## 官方三件事

1. **看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo / 看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo 这份对象 is not already 已经是 Prepare 的 ExtendedCommitInfo interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1371 valuse-notproc interchangeable / 1372 valuse-notfin interchangeable，也不是已经 ValUse Process CommitInfo Validator not already Prepare ExtendedCommitInfo / not already local_last_commit / not already 364-pubkey 正式三事 bundled（449 item 1 余量） interchangeable / 449 valuse item 1 interchangeable。**  
   官方把Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo和已经是 Prepare 的 ExtendedCommitInfo写成两件。看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo，不是已经是 Prepare 的 ExtendedCommitInfo。

2. **看见Process CommitInfo Validator is not already Prepare ExtendedCommitInfo / 看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo / 这份对象 is not already 已经是 local_last_commit 同一份 interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1371 valuse-notproc interchangeable / 1373 valuse-notprep interchangeable，也不是已经 Validator 用 address 认人就已经带了公钥 interchangeable / 364 Validator 用 address 认人就已经带了公钥 interchangeable。**  
   官方把Process CommitInfo Validator is not already Prepare ExtendedCommitInfo和已经是 local_last_commit 同一份写成两件。看见Process CommitInfo Validator is not already Prepare ExtendedCommitInfo，不是已经是 local_last_commit 同一份。

3. **看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo / 看见Process CommitInfo Validator is not already Prepare ExtendedCommitInfo / 这份对象 is not already 已经带了公钥 interchangeable，也不是已经 validatorusage vs gates bundled（449） interchangeable / 1371 valuse-notproc interchangeable / 1372 valuse-notfin interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出 interchangeable / 369 ExtendedVoteInfo 从本进程抽出 interchangeable。**  
   官方把Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo和已经带了公钥写成两件。看见Process 的 CommitInfo Validator 不是已经 Prepare ExtendedCommitInfo，不是已经带了公钥。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。

## 官方为什么这样拆

- **Process 的 CommitInfo 不是已经 Prepare 的 ExtendedCommitInfo interchangeable：官方把拟议路径和本地路径分开。**
- **看见 VoteInfo 里只有 address 和 power 不是已经 Prepare 路径。**
- **看见 Process 门 不是已经 local_last_commit 同一份。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 Prepare 的 ExtendedCommitInfo | 不是已经是 Prepare 的 ExtendedCommitInfo | 不是已经Validator 用 address 认人就已经带了公钥（364） |
| 已经是 local_last_commit 同一份 | 不是已经是 local_last_commit 同一份 | 不是已经ExtendedVoteInfo 从本进程抽出（369） |
| 已经带了公钥 | 不是已经带了公钥 | 不是已经1372 valuse-notfin |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ValUse Process CommitInfo Validator not already Prepare ExtendedCommitInfo / not already local_last_commit / not already 364-pubkey 正式三事（449 余量），必须分开是不是已经是 Prepare 的 ExtendedCommitInfo、是不是已经是 local_last_commit 同一份、是不是已经带了公钥。可以跳过「看见四门里都有 Validator 就已经同一门」。不要另写 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。449 Validator Usage four-gate mapping bundled unbundling 在本页 item 1 启动；续 [`worked-example-valuse-notfin-vs-bundled.md`](worked-example-valuse-notfin-vs-bundled.md)（不变量 1372 item 2）。

## 本页不抄

- 怎样写 Validator Usage 四门映射正式三事、怎样填 proposed_last_commit / decided_last_commit / local_last_commit。
- 怎样把四门 Validator 写成同一路、怎样拿 CommitInfo 代替 ExtendedCommitInfo、怎样把 decided 写成 proposed。
