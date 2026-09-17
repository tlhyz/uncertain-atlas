# 例：看见 FinalizeBlockRequest.height is not already header-aligned interchangeable / not already processed interchangeable / not already settled interchangeable

**层次**：实现 / FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事（422 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事（422 余量）/ not 1041 finreqcol-nothead interchangeable / not 422 finreq-vs-procreq bundled interchangeable」，不是 Finalize 请求栏 bundled（422），也不是 ProcessProposalRequest.height 就已经对上了拟议块头（419），也不是 Finalize 的 height / time 对上拟议块头就已经验过块头。不要另写怎样写 Finalize 请求栏。

## 官方三件事

1. **看见 FinalizeBlockRequest.height 是已决块的高度 / 看见填了 height 这份栏 is not already 已经对上了拟议块头 interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1041 finreqcol-nothead interchangeable / 1040 finreqcol-notlocal interchangeable / 422 finreq item 1 decided_last_commit interchangeable，也不是已经 FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事 bundled（422 item 2 余量） interchangeable / 422 finreq item 2 interchangeable。**  
   官方写：height 是已决块的高度。看见填了 height，不是已经 ProcessProposalRequest.height 那种已经对上了拟议块头 interchangeable——本页从 422 item 2 侧钉 not already header-aligned 单句。422 finreq vs procreq bundled unbundling 在本页 item 2 续。

2. **看见有已决块高度 / 看见填了 height / 这份栏 is not already 已经字段名对上就已经跑过 Process interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1041 finreqcol-nothead interchangeable / 422 finreq item 3 txs interchangeable / 1042 finreqcol-notexec interchangeable，也不是已经 ProcessProposalRequest.height 就已经对上了拟议块头 interchangeable / 419 procreq interchangeable。**  
   官方把有已决块高度和已经字段名对上就已经跑过 Process 分开。看见有已决块高度，不是已经字段名对上就已经跑过 Process interchangeable。本页钉 not already processed 单句。

3. **看见能指高度 / 看见填了 height / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 请求栏 bundled（422） interchangeable / 1041 finreqcol-nothead interchangeable / 1040 finreqcol-notlocal interchangeable，也不是已经 Finalize 的 height / time 对上拟议块头就已经验过块头 interchangeable。**  
   官方把能指高度和已经交差分开。看见能指高度，不是已经交差 interchangeable。422 finreq vs procreq bundled unbundling 在本页 item 2 续。

怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockRequest.height not already header-aligned ≠ 已经对上了拟议块头 interchangeable：** 官方把已决块的高度和已经对上了拟议块头分开。
- **看见有已决块高度 not already processed ≠ 已经字段名对上就已经跑过 Process interchangeable：** 官方把有已决块高度和已经字段名对上就已经跑过 Process 分开。
- **看见能指高度 not already settled ≠ 已经交差 interchangeable：** 官方把能指高度和已经交差分开；422 finreq vs procreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockRequest.height 是已决块的高度 | 不是已经对上了拟议块头 | 不是 ProcessProposalRequest.height 就已经对上了拟议块头（419） |
| 看见有已决块高度 | 不是已经字段名对上就已经跑过 Process | 不是 txs 就已经执行那些交易（1042） |
| 看见能指高度 | 不是已经交差 | 不是 decided_last_commit 就已经交差 local_last_commit（1040） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事（422 余量），必须分开是不是已经对上了拟议块头、是不是已经字段名对上就已经跑过 Process、是不是已经交差。可以跳过「看见填了 Finalize 请求栏就已经交差 local_last_commit」。不要另写怎样写 Finalize 请求栏。422 finreq vs procreq bundled unbundling 在本页 item 2 续；续 [`worked-example-finreqcol-notexec-vs-bundled.md`](worked-example-finreqcol-notexec-vs-bundled.md)（不变量 1042 item 3）。

## 本页不抄

- 怎样写 Finalize 请求栏、怎样填 decided_last_commit、怎样填 txs。
- Finalize 请求栏 bundled。那是不变量 422。
- ProcessProposalRequest.height 就已经对上了拟议块头。那是不变量 419。
- Finalize 的 height / time 对上拟议块头就已经验过块头。那是相邻 Usage 页，不是本页。
