# 例：看见 PrepareProposalRequest.height is not already header-aligned interchangeable / not already header-known interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事（423 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事（423 余量）/ not 1048 prepreqcol-nothead interchangeable / not 423 prepreq-vs-return bundled interchangeable」，不是 Prepare 请求栏 bundled（423），也不是 ProcessProposalRequest.height 就已经对上了拟议块头（419），也不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359）。不要另写怎样写 Prepare 请求栏。

## 官方三件事

1. **看见 PrepareProposalRequest.height 是将要提议的那块的高度 / 看见填了 height 这份栏 is not already 已经对上了拟议块头 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1048 prepreqcol-nothead interchangeable / 1046 prepreqcol-notcap interchangeable / 423 prepreq item 1 max_tx_bytes interchangeable，也不是已经 PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事 bundled（423 item 3 余量） interchangeable / 423 prepreq item 3 interchangeable。**  
   官方写：height 是将要提议的那块的高度。看见填了 height，不是已经 ProcessProposalRequest.height 那种已经对上了拟议块头 interchangeable——本页从 423 item 3 侧钉 not already header-aligned 单句。423 prepreq vs return bundled unbundling 在本页 item 3 完成。

2. **看见有将要提议的高度 / 看见填了 height / 这份栏 is not already 已经知道本头哈希 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1048 prepreqcol-nothead interchangeable / 423 prepreq item 2 txs interchangeable / 1047 prepreqcol-notproc interchangeable，也不是已经 ProcessProposalRequest.height 就已经对上了拟议块头 interchangeable / 419 procreq interchangeable。**  
   官方把有将要提议的高度和已经知道本头哈希分开。看见有将要提议的高度，不是已经知道本头哈希 interchangeable。本页钉 not already header-known 单句。

3. **看见能指高度 / 看见填了 height / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1048 prepreqcol-nothead interchangeable / 1046 prepreqcol-notcap interchangeable，也不是已经 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希 interchangeable / 359 samefields interchangeable。**  
   官方把能指高度和已经交差分开。看见能指高度，不是已经交差 interchangeable。423 prepreq vs return bundled unbundling 在本页 item 3 完成。

怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.height not already header-aligned ≠ 已经对上了拟议块头 interchangeable：** 官方把将要提议的那块的高度和已经对上了拟议块头分开。
- **看见有将要提议的高度 not already header-known ≠ 已经知道本头哈希 interchangeable：** 官方把有将要提议的高度和已经知道本头哈希分开。
- **看见能指高度 not already settled ≠ 已经交差 interchangeable：** 官方把能指高度和已经交差分开；423 prepreq vs return bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.height 是将要提议的那块的高度 | 不是已经对上了拟议块头 | 不是 ProcessProposalRequest.height 就已经对上了拟议块头（419） |
| 看见有将要提议的高度 | 不是已经知道本头哈希 | 不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359） |
| 看见能指高度 | 不是已经交差 | 不是 FinalizeBlockRequest.height 就已经对上了拟议块头（422） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.height not already header-aligned / not already header-known / not already settled 正式三事（423 余量），必须分开是不是已经对上了拟议块头、是不是已经知道本头哈希、是不是已经交差。可以跳过「看见填了 Prepare 请求栏就已经能回超限列表」。不要另写怎样写 Prepare 请求栏。423 prepreq vs return bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs。
- Prepare 请求栏 bundled。那是不变量 423。
- ProcessProposalRequest.height 就已经对上了拟议块头。那是不变量 419。
- Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希。那是不变量 359。
