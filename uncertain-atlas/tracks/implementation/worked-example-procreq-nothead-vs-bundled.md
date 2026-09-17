# 例：看见 ProcessProposalRequest.height is not already header-aligned interchangeable / not already ext-height interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事（419 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事（419 余量）/ not 1027 procreq-nothead interchangeable / not 419 procreq-vs-extreq bundled interchangeable」，不是 Process 请求栏 bundled（419），也不是 Process 的 height / time 对上拟议块头就已经验过块头（417），也不是 ExtendVoteRequest.height 就已经对上了拟议块（410）。不要另写怎样写 Process 请求栏。

## 官方三件事

1. **看见 ProcessProposalRequest.height 是拟议块的高度 / 看见填了 height 这份栏 is not already 已经对上了拟议块头 interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1027 procreq-nothead interchangeable / 1025 procreq-notexec interchangeable / 419 procreq item 1 txs interchangeable，也不是已经 ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事 bundled（419 item 3 余量） interchangeable / 419 procreq item 3 interchangeable。**  
   官方写：height 是拟议块的高度。看见填了 height，不是已经 Process 的 height / time 对上拟议块头那种已经验过块头 interchangeable——本页从 419 item 3 侧钉 not already header-aligned 单句。419 procreq vs extreq bundled unbundling 在本页 item 3 完成。

2. **看见有高度 / 看见填了 height / 这份栏 is not already 已经 ExtendVoteRequest.height 是拟议块高度（用来对一下）那种已经对上了拟议块 interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1027 procreq-nothead interchangeable / 419 procreq item 2 hash interchangeable / 1026 procreq-notproc interchangeable，也不是已经 Process 的 height / time 对上拟议块头就已经验过块头 interchangeable / 417 procheight interchangeable。**  
   官方把有高度和已经 ExtendVoteRequest.height 那种已经对上了拟议块分开。看见有高度，不是已经 ExtendVoteRequest.height 那种已经对上了拟议块 interchangeable。本页钉 not already ext-height 单句。

3. **看见能指 / 看见填了 height / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求栏 bundled（419） interchangeable / 1027 procreq-nothead interchangeable / 1025 procreq-notexec interchangeable，也不是已经 ExtendVoteRequest.height 就已经对上了拟议块 interchangeable / 410 extreqhash interchangeable。**  
   官方把能指和已经交差分开。看见能指，不是已经交差 interchangeable。419 procreq vs extreq bundled unbundling 在本页 item 3 完成。

怎样写 Process 请求栏、怎样填 txs、怎样填 hash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.height not already header-aligned ≠ 已经对上了拟议块头 interchangeable：** 官方把 Process 请求表上这份拟议块高度和 Usage 里那份 height / time 对上拟议块头分开。
- **看见有高度 not already ext-height ≠ 已经 ExtendVoteRequest.height 那种已经对上了拟议块 interchangeable：** 官方把有高度和已经 ExtendVoteRequest.height 那种已经对上了拟议块分开。
- **看见能指 not already settled ≠ 已经交差 interchangeable：** 官方把能指和已经交差分开；419 procreq vs extreq bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.height 是拟议块的高度 | 不是已经对上了拟议块头 | 不是 Process 的 height / time 对上拟议块头就已经验过块头（417） |
| 看见有高度 | 不是已经 ExtendVoteRequest.height 那种已经对上了拟议块 | 不是 ExtendVoteRequest.height 就已经对上了拟议块（410） |
| 看见能指 | 不是已经交差 | 不是 txs 就已经执行那些交易（1025） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.height not already header-aligned / not already ext-height / not already settled 正式三事（419 余量），必须分开是不是已经对上了拟议块头、是不是已经 ExtendVoteRequest.height 那种已经对上了拟议块、是不是已经交差。可以跳过「看见填了 Process 请求栏就已经执行那些交易」。不要另写怎样写 Process 请求栏。419 procreq vs extreq bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Process 请求栏、怎样填 txs、怎样填 hash。
- Process 请求栏 bundled。那是不变量 419。
- Process 的 height / time 对上拟议块头就已经验过块头。那是不变量 417。
- ExtendVoteRequest.hash 就已经跑过 Process。那是不变量 410。
