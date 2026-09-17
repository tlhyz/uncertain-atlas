# 例：看见 ProcessProposalRequest.txs is not already executed interchangeable / not already whole-block interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalRequest.txs not already executed / not already whole-block / not already settled 正式三事（419 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.txs not already executed / not already whole-block / not already settled 正式三事（419 余量）/ not 1025 procreq-notexec interchangeable / not 419 procreq-vs-extreq bundled interchangeable」，不是 Process 请求栏 bundled（419），也不是 ExtendVoteRequest.txs 就已经执行那些交易（411），也不是 ExtendVoteRequest.hash 就已经跑过 Process（410）。不要另写怎样写 Process 请求栏。

## 官方三件事

1. **看见 ProcessProposalRequest.txs 是拟议块的交易列表 / 看见填了 txs 这份栏 is not already 已经执行那些交易 interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1025 procreq-notexec interchangeable / 1026 procreq-notproc interchangeable / 419 procreq item 2 hash interchangeable，也不是已经 ProcessProposalRequest.txs not already executed / not already whole-block / not already settled 正式三事 bundled（419 item 1 余量） interchangeable / 419 procreq item 1 interchangeable。**  
   官方写：txs 是拟议块的交易列表。看见填了 txs，不是已经 ExtendVoteRequest.txs 是扩展要指的那份块的交易列表那种已经执行那些交易 interchangeable——本页从 419 item 1 侧钉 not already executed 单句。419 procreq vs extreq bundled unbundling 在本页 item 1 启动。

2. **看见有交易列表 / 看见填了 txs / 这份栏 is not already 已经整块跑了 interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1025 procreq-notexec interchangeable / 419 procreq item 3 height interchangeable / 1027 procreq-nothead interchangeable，也不是已经 ExtendVoteRequest.txs 就已经执行那些交易 interchangeable / 411 extreqtxs interchangeable。**  
   官方把有交易列表和已经整块跑了分开。看见有交易列表，不是已经整块跑了 interchangeable。本页钉 not already whole-block 单句。

3. **看见能指 / 看见填了 txs / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1025 procreq-notexec interchangeable / 1026 procreq-notproc interchangeable，也不是已经 ExtendVoteRequest.hash 就已经跑过 Process interchangeable / 410 extreqhash interchangeable。**  
   官方把能指和已经交差分开。看见能指，不是已经交差 interchangeable。419 procreq vs extreq bundled unbundling 在本页 item 1 启动。

怎样写 Process 请求栏、怎样填 txs、怎样填 hash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.txs not already executed ≠ 已经执行那些交易 interchangeable：** 官方把 Process 请求表上这份交易列表和 ExtendVote 请求表上那份扩展要指的交易列表分开。
- **看见有交易列表 not already whole-block ≠ 已经整块跑了 interchangeable：** 官方把有交易列表和已经整块跑了分开。
- **看见能指 not already settled ≠ 已经交差 interchangeable：** 官方把能指和已经交差分开；419 procreq vs extreq bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.txs 是拟议块的交易列表 | 不是已经执行那些交易 | 不是 ExtendVoteRequest.txs 就已经执行那些交易（411） |
| 看见有交易列表 | 不是已经整块跑了 | 不是 ExtendVoteRequest.hash 就已经跑过 Process（410） |
| 看见能指 | 不是已经交差 | 不是 hash 就已经跑过 Process（1026） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.txs not already executed / not already whole-block / not already settled 正式三事（419 余量），必须分开是不是已经执行那些交易、是不是已经整块跑了、是不是已经交差。可以跳过「看见填了 Process 请求栏就已经执行那些交易」。不要另写怎样写 Process 请求栏。419 procreq vs extreq bundled unbundling 在本页 item 1 启动；续 [`worked-example-procreq-notproc-vs-bundled.md`](worked-example-procreq-notproc-vs-bundled.md)（不变量 1026 item 2）。

## 本页不抄

- 怎样写 Process 请求栏、怎样填 txs、怎样填 hash。
- Process 请求栏 bundled。那是不变量 419。
- ExtendVoteRequest.txs 就已经执行那些交易。那是不变量 411。
- ExtendVoteRequest.hash 就已经跑过 Process。那是不变量 410。
