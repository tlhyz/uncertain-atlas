# 例：看见 PrepareProposalRequest.time is not already header-aligned interchangeable / not already vote-checked interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事（424 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事（424 余量）/ not 1050 preprestr-notts interchangeable / not 424 prepreqrest-vs-procreq bundled interchangeable」，不是 Prepare 请求余栏 bundled（424），也不是 ProcessProposalRequest.time 就已经验过票上时间（420），也不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359）。不要另写怎样写 Prepare 请求余栏。

## 官方三件事

1. **看见 PrepareProposalRequest.time 是将要提议那块的时间戳 / 看见填了 time 这份栏 is not already 已经对上了拟议块头 interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1050 preprestr-notts interchangeable / 1049 preprestr-notlocal interchangeable / 424 prepreqrest item 1 local_last_commit interchangeable，也不是已经 PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事 bundled（424 item 2 余量） interchangeable / 424 prepreqrest item 2 interchangeable。**  
   官方写：time 是将要提议那块的时间戳。看见填了 time，不是已经 ProcessProposalRequest.time 那种已经验过票上时间 interchangeable——本页从 424 item 2 侧钉 not already header-aligned 单句。424 prepreqrest vs procreq bundled unbundling 在本页 item 2 续。

2. **看见有将要提议的时间戳 / 看见填了 time / 这份栏 is not already 已经验过票上时间 interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1050 preprestr-notts interchangeable / 424 prepreqrest item 3 misbehavior interchangeable / 1051 preprestr-notpunish interchangeable，也不是已经 ProcessProposalRequest.time 就已经验过票上时间 interchangeable / 420 procrestr interchangeable。**  
   官方把有将要提议的时间戳和已经验过票上时间分开。看见有将要提议的时间戳，不是已经验过票上时间 interchangeable。本页钉 not already vote-checked 单句。

3. **看见能指时间 / 看见填了 time / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1050 preprestr-notts interchangeable / 1049 preprestr-notlocal interchangeable，也不是已经 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希 interchangeable / 359 samefields interchangeable。**  
   官方把能指时间和已经交差分开。看见能指时间，不是已经交差 interchangeable。424 prepreqrest vs procreq bundled unbundling 在本页 item 2 续。

怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.time not already header-aligned ≠ 已经对上了拟议块头 interchangeable：** 官方把将要提议那块的时间戳和已经对上了拟议块头分开。
- **看见有将要提议的时间戳 not already vote-checked ≠ 已经验过票上时间 interchangeable：** 官方把有将要提议的时间戳和已经验过票上时间分开。
- **看见能指时间 not already settled ≠ 已经交差 interchangeable：** 官方把能指时间和已经交差分开；424 prepreqrest vs procreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.time 是将要提议那块的时间戳 | 不是已经对上了拟议块头 | 不是 ProcessProposalRequest.time 就已经验过票上时间（420） |
| 看见有将要提议的时间戳 | 不是已经验过票上时间 | 不是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希（359） |
| 看见能指时间 | 不是已经交差 | 不是 misbehavior 就已经定奖惩（1051） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事（424 余量），必须分开是不是已经对上了拟议块头、是不是已经验过票上时间、是不是已经交差。可以跳过「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit」。不要另写怎样写 Prepare 请求余栏。424 prepreqrest vs procreq bundled unbundling 在本页 item 2 续；续 [`worked-example-preprestr-notpunish-vs-bundled.md`](worked-example-preprestr-notpunish-vs-bundled.md)（不变量 1051 item 3）。

## 本页不抄

- 怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time。
- Prepare 请求余栏 bundled。那是不变量 424。
- ProcessProposalRequest.time 就已经验过票上时间。那是不变量 420。
- Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希。那是不变量 359。
