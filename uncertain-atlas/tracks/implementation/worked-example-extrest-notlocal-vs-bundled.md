# 例：看见 ExtendVoteRequest.proposed_last_commit is not already local-settled interchangeable / not already processed interchangeable / not already this-header interchangeable

**层次**：实现 / ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事（411 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事（411 余量）/ not 1035 extrest-notlocal interchangeable / not 411 extreqtxs-vs-fintxs bundled interchangeable」，不是 ExtendVote 请求余栏 bundled（411），也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359），也不是 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit（420）。不要另写怎样写 ExtendVote 请求余栏。

## 官方三件事

1. **看见 ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息 / 看见填了 proposed_last_commit 这份栏 is not already 已经交差 local_last_commit interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1035 extrest-notlocal interchangeable / 1034 extrest-notexec interchangeable / 411 extreqtxs item 1 txs interchangeable，也不是已经 ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事 bundled（411 item 2 余量） interchangeable / 411 extreqtxs item 2 interchangeable。**  
   官方写：proposed_last_commit 是上一份拟议块的 last commit 信息。看见填了 proposed_last_commit，不是已经 Prepare local_last_commit 是上一高度的预提交带扩展那种已经交差 interchangeable——本页从 411 item 2 侧钉 not already local-settled 单句。411 extreqtxs vs fintxs bundled unbundling 在本页 item 2 续。

2. **看见有上一份拟议块的 last commit / 看见填了 proposed_last_commit / 这份栏 is not already 已经字段名对上就已经跑过 Process interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1035 extrest-notlocal interchangeable / 411 extreqtxs item 3 next hash interchangeable / 1036 extrest-nothash interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process interchangeable / 359 samefields interchangeable。**  
   官方把有上一份拟议块的 last commit 和已经字段名对上就已经跑过 Process 分开。看见有上一份拟议块的 last commit，不是已经字段名对上就已经跑过 Process interchangeable。本页钉 not already processed 单句。

3. **看见能指 / 看见填了 proposed_last_commit / 这份栏 is not already 已经是本头 LastCommit interchangeable，也不是已经 ExtendVote 请求余栏 bundled（411） interchangeable / 1035 extrest-notlocal interchangeable / 1034 extrest-notexec interchangeable，也不是已经 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit interchangeable / 420 procreqrest interchangeable。**  
   官方把能指和已经是本头 LastCommit 分开。看见能指，不是已经是本头 LastCommit interchangeable。411 extreqtxs vs fintxs bundled unbundling 在本页 item 2 续。

怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.proposed_last_commit not already local-settled ≠ 已经交差 local_last_commit interchangeable：** 官方把上一份拟议块的 last commit 和 Prepare 已经交差 local_last_commit 分开。
- **看见有上一份拟议块的 last commit not already processed ≠ 已经字段名对上就已经跑过 Process interchangeable：** 官方把有上一份拟议块的 last commit 和已经字段名对上就已经跑过 Process 分开。
- **看见能指 not already this-header ≠ 已经是本头 LastCommit interchangeable：** 官方把能指和已经是本头 LastCommit 分开；411 extreqtxs vs fintxs bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.proposed_last_commit 是上一份拟议块的 last commit 信息 | 不是已经交差 local_last_commit | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| 看见有上一份拟议块的 last commit | 不是已经字段名对上就已经跑过 Process | 不是 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit（420） |
| 看见能指 | 不是已经是本头 LastCommit | 不是 next_validators_hash 就已经是 Finalize 请求栏（1036） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.proposed_last_commit not already local-settled / not already processed / not already this-header 正式三事（411 余量），必须分开是不是已经交差 local_last_commit、是不是已经字段名对上就已经跑过 Process、是不是已经是本头 LastCommit。可以跳过「看见填了 ExtendVote 请求余栏就已经执行那些交易」。不要另写怎样写 ExtendVote 请求余栏。411 extreqtxs vs fintxs bundled unbundling 在本页 item 2 续；续 [`worked-example-extrest-nothash-vs-bundled.md`](worked-example-extrest-nothash-vs-bundled.md)（不变量 1036 item 3）。

## 本页不抄

- 怎样写 ExtendVote 请求余栏、怎样填 txs、怎样填 proposed_last_commit。
- ExtendVote 请求余栏 bundled。那是不变量 411。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit。那是不变量 420。
