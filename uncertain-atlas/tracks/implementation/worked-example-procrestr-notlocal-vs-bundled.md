# 例：看见 ProcessProposalRequest.proposed_last_commit is not already local-settled interchangeable / not already ext-commit interchangeable / not already processed interchangeable

**层次**：实现 / ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事（420 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事（420 余量）/ not 1028 procrestr-notlocal interchangeable / not 420 procreqrest-vs-extreq bundled interchangeable」，不是 Process 请求余栏 bundled（420），也不是 ExtendVoteRequest.proposed_last_commit 就已经交差 local_last_commit（411），也不是 ProcessProposalRequest.txs 就已经执行那些交易（419）。不要另写怎样写 Process 请求余栏。

## 官方三件事

1. **看见 ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 / 看见填了 proposed_last_commit 这份栏 is not already 已经交差 local_last_commit interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1028 procrestr-notlocal interchangeable / 1029 procrestr-notts interchangeable / 420 procreqrest item 2 time interchangeable，也不是已经 ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事 bundled（420 item 1 余量） interchangeable / 420 procreqrest item 1 interchangeable。**  
   官方写：proposed_last_commit 是上一份提交信息，从拟议块里的信息拿到。看见填了 proposed_last_commit，不是已经 ExtendVoteRequest.proposed_last_commit 那种已经交差 local_last_commit interchangeable——本页从 420 item 1 侧钉 not already local-settled 单句。420 procreqrest vs extreq bundled unbundling 在本页 item 1 启动。

2. **看见从拟议块拿到 / 看见填了 proposed_last_commit / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1028 procrestr-notlocal interchangeable / 420 procreqrest item 3 misbehavior interchangeable / 1030 procrestr-notpunish interchangeable，也不是已经 ExtendVoteRequest.proposed_last_commit 就已经交差 local_last_commit interchangeable / 411 extreqtxs interchangeable。**  
   官方把从拟议块拿到和已经交差分开。看见从拟议块拿到，不是已经交差 interchangeable。本页钉 not already ext-commit 单句。

3. **看见能指上一份提交 / 看见填了 proposed_last_commit / 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1028 procrestr-notlocal interchangeable / 1029 procrestr-notts interchangeable，也不是已经 ProcessProposalRequest.txs 就已经执行那些交易 interchangeable / 419 procreq interchangeable。**  
   官方把能指上一份提交和已经跑过 Process 分开。看见能指上一份提交，不是已经跑过 Process interchangeable。420 procreqrest vs extreq bundled unbundling 在本页 item 1 启动。

怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.proposed_last_commit not already local-settled ≠ 已经交差 local_last_commit interchangeable：** 官方把 Process 请求表上这份从拟议块拿到的上一份提交和 ExtendVote 请求表上那份上一份拟议块的 last commit 分开。
- **看见从拟议块拿到 not already ext-commit ≠ 已经交差 interchangeable：** 官方把从拟议块拿到和已经交差分开。
- **看见能指上一份提交 not already processed ≠ 已经跑过 Process interchangeable：** 官方把能指上一份提交和已经跑过 Process 分开；420 procreqrest vs extreq bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.proposed_last_commit 是从拟议块里的信息拿到的上一份提交信息 | 不是已经交差 local_last_commit | 不是 ExtendVoteRequest.proposed_last_commit 就已经交差 local_last_commit（411） |
| 看见从拟议块拿到 | 不是已经交差 | 不是 ProcessProposalRequest.txs 就已经执行那些交易（419） |
| 看见能指上一份提交 | 不是已经跑过 Process | 不是 time 就已经验过票上时间（1029） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事（420 余量），必须分开是不是已经交差 local_last_commit、是不是已经交差、是不是已经跑过 Process。可以跳过「看见填了 Process 请求余栏就已经交差 local_last_commit」。不要另写怎样写 Process 请求余栏。420 procreqrest vs extreq bundled unbundling 在本页 item 1 启动；续 [`worked-example-procrestr-notts-vs-bundled.md`](worked-example-procrestr-notts-vs-bundled.md)（不变量 1029 item 2）。

## 本页不抄

- 怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time。
- Process 请求余栏 bundled。那是不变量 420。
- ExtendVoteRequest.proposed_last_commit 就已经交差 local_last_commit。那是不变量 411。
- ProcessProposalRequest.txs 就已经执行那些交易。那是不变量 419。
