# 例：看见 FinalizeBlockRequest.hash is not already process-hash interchangeable / not already processed interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事（428 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事（428 余量）/ not 1061 finrestr-nothash interchangeable / not 428 finreqrest-vs-procreq bundled interchangeable」，不是 Finalize 请求余栏 bundled（428），也不是 ProcessProposalRequest.hash 就已经跑过 Process（419），也不是 ExtendVoteRequest.hash 就已经知道本头哈希（410）。不要另写怎样写 Finalize 请求余栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.hash 是已决块的哈希 / 看见填了 hash 这份栏 is not already 已经是 ProcessProposalRequest.hash interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1061 finrestr-nothash interchangeable / 1062 finrestr-notpunish interchangeable / 428 finreqrest item 2 misbehavior interchangeable，也不是已经 FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事 bundled（428 item 1 余量） interchangeable / 428 finreqrest item 1 interchangeable。**  
   官方写：hash 是已决块的哈希。看见填了 hash，不是已经 ProcessProposalRequest.hash 那种已经跑过 Process interchangeable——本页从 428 item 1 侧钉 not already process-hash 单句。428 finreqrest vs procreq bundled unbundling 在本页 item 1 启动。

2. **看见能指已决块 / 看见填了 hash / 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1061 finrestr-nothash interchangeable / 428 finreqrest item 3 next_hash interchangeable / 1063 finrestr-notproc interchangeable，也不是已经 ProcessProposalRequest.hash 就已经跑过 Process interchangeable / 419 procreq interchangeable。**  
   官方把能指已决块和已经跑过 Process 分开。看见能指已决块，不是已经跑过 Process interchangeable。本页钉 not already processed 单句。

3. **看见字段名对得上 / 看见填了 hash / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 请求余栏 bundled（428） interchangeable / 1061 finrestr-nothash interchangeable / 1062 finrestr-notpunish interchangeable，也不是已经 ExtendVoteRequest.hash 就已经知道本头哈希 interchangeable / 410 extreqhash interchangeable。**  
   官方把字段名对得上和已经交差分开。看见字段名对得上，不是已经交差 interchangeable。428 finreqrest vs procreq bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.hash not already process-hash ≠ 已经是 ProcessProposalRequest.hash interchangeable：** 官方把已决块的哈希和已经是 ProcessProposalRequest.hash 分开。
- **看见能指已决块 not already processed ≠ 已经跑过 Process interchangeable：** 官方把能指已决块和已经跑过 Process 分开。
- **看见字段名对得上 not already settled ≠ 已经交差 interchangeable：** 官方把字段名对得上和已经交差分开；428 finreqrest vs procreq bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.hash 是已决块的哈希 | 不是已经是 ProcessProposalRequest.hash | 不是 ProcessProposalRequest.hash 就已经跑过 Process（419） |
| 看见能指已决块 | 不是已经跑过 Process | 不是 ExtendVoteRequest.hash 就已经知道本头哈希（410） |
| 看见字段名对得上 | 不是已经交差 | 不是 misbehavior 就已经定奖惩（1062） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.hash not already process-hash / not already processed / not already settled 正式三事（428 余量），必须分开是不是已经是 ProcessProposalRequest.hash、是不是已经跑过 Process、是不是已经交差。可以跳过「看见填了 Finalize 请求余栏就已经是 ProcessProposalRequest.hash」。不要另写怎样写 Finalize 请求余栏。428 finreqrest vs procreq bundled unbundling 在本页 item 1 启动；续 [`worked-example-finrestr-notpunish-vs-bundled.md`](worked-example-finrestr-notpunish-vs-bundled.md)（不变量 1062 item 2）。

## 本页不抄

- 怎样写 Finalize 请求余栏、怎样填 hash、怎样填 misbehavior。
- Finalize 请求余栏 bundled。那是不变量 428。
- ProcessProposalRequest.hash 就已经跑过 Process。那是不变量 419。
- ExtendVoteRequest.hash 就已经知道本头哈希。那是不变量 410。
