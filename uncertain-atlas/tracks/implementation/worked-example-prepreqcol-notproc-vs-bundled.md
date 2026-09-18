# 例：看见 PrepareProposalRequest.txs is not already processed interchangeable / not already executed interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事（423 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事（423 余量）/ not 1047 prepreqcol-notproc interchangeable / not 423 prepreq-vs-return bundled interchangeable」，不是 Prepare 请求栏 bundled（423），也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359），也不是 FinalizeBlockRequest.txs 就已经执行那些交易（422）。不要另写怎样写 Prepare 请求栏。

## 官方三件事

1. **看见 PrepareProposalRequest.txs 是挑进拟议块的初步交易列表 / 看见填了 txs 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1047 prepreqcol-notproc interchangeable / 1046 prepreqcol-notcap interchangeable / 423 prepreq item 1 max_tx_bytes interchangeable，也不是已经 PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事 bundled（423 item 2 余量） interchangeable / 423 prepreq item 2 interchangeable。**  
   官方写：txs 是挑进拟议块的初步交易列表。看见填了 txs，不是已经 Prepare 和 Process / Finalize 同一套字段那种已经跑过 Process interchangeable——本页从 423 item 2 侧钉 not already processed 单句。423 prepreq vs return bundled unbundling 在本页 item 2 续。

2. **看见是初步列表 / 看见填了 txs / 这份栏 is not already 已经执行那些交易 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1047 prepreqcol-notproc interchangeable / 423 prepreq item 3 height interchangeable / 1048 prepreqcol-nothead interchangeable，也不是已经 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process interchangeable / 359 samefields interchangeable。**  
   官方把是初步列表和已经执行那些交易分开。看见是初步列表，不是已经执行那些交易 interchangeable。本页钉 not already executed 单句。

3. **看见能指初步交易 / 看见填了 txs / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求栏 bundled（423） interchangeable / 1047 prepreqcol-notproc interchangeable / 1046 prepreqcol-notcap interchangeable，也不是已经 FinalizeBlockRequest.txs 就已经执行那些交易 interchangeable / 422 finreqcol interchangeable。**  
   官方把能指初步交易和已经交差分开。看见能指初步交易，不是已经交差 interchangeable。423 prepreq vs return bundled unbundling 在本页 item 2 续。

怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.txs not already processed ≠ 已经跑过 Process interchangeable：** 官方把挑进拟议块的初步交易列表和已经跑过 Process 分开。
- **看见是初步列表 not already executed ≠ 已经执行那些交易 interchangeable：** 官方把是初步列表和已经执行那些交易分开。
- **看见能指初步交易 not already settled ≠ 已经交差 interchangeable：** 官方把能指初步交易和已经交差分开；423 prepreq vs return bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.txs 是挑进拟议块的初步交易列表 | 不是已经跑过 Process | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| 看见是初步列表 | 不是已经执行那些交易 | 不是 ProcessProposalRequest.txs 就已经执行那些交易（419） |
| 看见能指初步交易 | 不是已经交差 | 不是 FinalizeBlockRequest.txs 就已经执行那些交易（422） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.txs not already processed / not already executed / not already settled 正式三事（423 余量），必须分开是不是已经跑过 Process、是不是已经执行那些交易、是不是已经交差。可以跳过「看见填了 Prepare 请求栏就已经能回超限列表」。不要另写怎样写 Prepare 请求栏。423 prepreq vs return bundled unbundling 在本页 item 2 续；续 [`worked-example-prepreqcol-nothead-vs-bundled.md`](worked-example-prepreqcol-nothead-vs-bundled.md)（不变量 1048 item 3）。

## 本页不抄

- 怎样写 Prepare 请求栏、怎样填 max_tx_bytes、怎样填 txs。
- Prepare 请求栏 bundled。那是不变量 423。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- FinalizeBlockRequest.txs 就已经执行那些交易。那是不变量 422。
