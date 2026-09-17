# 例：看见 ProcessProposalRequest.hash is not already processed interchangeable / not already ext-hash interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事（419 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事（419 余量）/ not 1026 procreq-notproc interchangeable / not 419 procreq-vs-extreq bundled interchangeable」，不是 Process 请求栏 bundled（419），也不是 ExtendVoteRequest.hash 就已经跑过 Process（410），也不是请求里的 hash 不是已经对该块跑过 Process（353）。不要另写怎样写 Process 请求栏。

## 官方三件事

1. **看见 ProcessProposalRequest.hash 是拟议块的哈希 / 看见填了 hash 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1026 procreq-notproc interchangeable / 1025 procreq-notexec interchangeable / 419 procreq item 1 txs interchangeable，也不是已经 ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事 bundled（419 item 2 余量） interchangeable / 419 procreq item 2 interchangeable。**  
   官方写：hash 是拟议块的哈希。看见填了 hash，不是已经 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希那种已经跑过 Process interchangeable——本页从 419 item 2 侧钉 not already processed 单句。419 procreq vs extreq bundled unbundling 在本页 item 2 续。

2. **看见有拟议块哈希 / 看见填了 hash / 这份栏 is not already 已经请求里的 hash 那种不保证已经对该块跑过 Process interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1026 procreq-notproc interchangeable / 419 procreq item 3 height interchangeable / 1027 procreq-nothead interchangeable，也不是已经 ExtendVoteRequest.hash 就已经跑过 Process interchangeable / 410 extreqhash interchangeable。**  
   官方把有拟议块哈希和已经请求里的 hash 那种不保证已经对该块跑过 Process 分开。看见有拟议块哈希，不是已经请求里的 hash 那种不保证已经对该块跑过 Process interchangeable。本页钉 not already ext-hash 单句。

3. **看见能指 / 看见填了 hash / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1026 procreq-notproc interchangeable / 1025 procreq-notexec interchangeable，也不是已经请求里的 hash 不是已经对该块跑过 Process interchangeable / 353 verifyusage interchangeable。**  
   官方把能指和已经交差分开。看见能指，不是已经交差 interchangeable。419 procreq vs extreq bundled unbundling 在本页 item 2 续。

怎样写 Process 请求栏、怎样填 txs、怎样填 hash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.hash not already processed ≠ 已经跑过 Process interchangeable：** 官方把 Process 请求表上这份拟议块哈希和 ExtendVote 请求表上那份扩展要指的头哈希分开。
- **看见有拟议块哈希 not already ext-hash ≠ 已经请求里的 hash 那种不保证已经对该块跑过 Process interchangeable：** 官方把有拟议块哈希和已经请求里的 hash 那种不保证已经对该块跑过 Process 分开。
- **看见能指 not already settled ≠ 已经交差 interchangeable：** 官方把能指和已经交差分开；419 procreq vs extreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.hash 是拟议块的哈希 | 不是已经跑过 Process | 不是 ExtendVoteRequest.hash 就已经跑过 Process（410） |
| 看见有拟议块哈希 | 不是已经请求里的 hash 那种不保证已经对该块跑过 Process | 不是请求里的 hash 不是已经对该块跑过 Process（353） |
| 看见能指 | 不是已经交差 | 不是 height 就已经对上了拟议块头（1027） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.hash not already processed / not already ext-hash / not already settled 正式三事（419 余量），必须分开是不是已经跑过 Process、是不是已经请求里的 hash 那种不保证已经对该块跑过 Process、是不是已经交差。可以跳过「看见填了 Process 请求栏就已经执行那些交易」。不要另写怎样写 Process 请求栏。419 procreq vs extreq bundled unbundling 在本页 item 2 续；续 [`worked-example-procreq-nothead-vs-bundled.md`](worked-example-procreq-nothead-vs-bundled.md)（不变量 1027 item 3）。

## 本页不抄

- 怎样写 Process 请求栏、怎样填 txs、怎样填 hash。
- Process 请求栏 bundled。那是不变量 419。
- ExtendVoteRequest.hash 就已经跑过 Process。那是不变量 410。
- 请求里的 hash 不是已经对该块跑过 Process。那是不变量 353。
