# 例：看见 ProcessProposalRequest.time is not already vote-ts-checked interchangeable / not already header-verified interchangeable / not already settled interchangeable

**层次**：实现 / ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事（420 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事（420 余量）/ not 1029 procrestr-notts interchangeable / not 420 procreqrest-vs-extreq bundled interchangeable」，不是 Process 请求余栏 bundled（420），也不是 ExtendVoteRequest.time 就已经验过票上时间（410），也不是票上 Timestamp 就已经验过（304）。不要另写怎样写 Process 请求余栏。

## 官方三件事

1. **看见 ProcessProposalRequest.time 是拟议块的时间戳 / 看见填了 time 这份栏 is not already 已经验过票上时间 interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1029 procrestr-notts interchangeable / 1028 procrestr-notlocal interchangeable / 420 procreqrest item 1 proposed_last_commit interchangeable，也不是已经 ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事 bundled（420 item 2 余量） interchangeable / 420 procreqrest item 2 interchangeable。**  
   官方写：time 是拟议块的时间戳。看见填了 time，不是已经 ExtendVoteRequest.time 那种已经验过票上时间 interchangeable——本页从 420 item 2 侧钉 not already vote-ts-checked 单句。420 procreqrest vs extreq bundled unbundling 在本页 item 2 续。

2. **看见有拟议块时间戳 / 看见填了 time / 这份栏 is not already 已经 Process 的 height / time 对上拟议块头那种已经验过块头 interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1029 procrestr-notts interchangeable / 420 procreqrest item 3 misbehavior interchangeable / 1030 procrestr-notpunish interchangeable，也不是已经 ExtendVoteRequest.time 就已经验过票上时间 interchangeable / 410 extreqhash interchangeable。**  
   官方把有拟议块时间戳和已经验过块头分开。看见有拟议块时间戳，不是已经验过块头 interchangeable。本页钉 not already header-verified 单句。

3. **看见能指时间 / 看见填了 time / 这份栏 is not already 已经交差 interchangeable，也不是已经 Process 请求余栏 bundled（420） interchangeable / 1029 procrestr-notts interchangeable / 1028 procrestr-notlocal interchangeable，也不是已经票上 Timestamp 就已经验过 interchangeable / 304 votets interchangeable。**  
   官方把能指时间和已经交差分开。看见能指时间，不是已经交差 interchangeable。420 procreqrest vs extreq bundled unbundling 在本页 item 2 续。

怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ProcessProposalRequest.time not already vote-ts-checked ≠ 已经验过票上时间 interchangeable：** 官方把 Process 请求表上这份拟议块时间戳和 ExtendVote 请求表上那份扩展要指的时间戳分开。
- **看见有拟议块时间戳 not already header-verified ≠ 已经验过块头 interchangeable：** 官方把有拟议块时间戳和已经验过块头分开。
- **看见能指时间 not already settled ≠ 已经交差 interchangeable：** 官方把能指时间和已经交差分开；420 procreqrest vs extreq bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProcessProposalRequest.time 是拟议块的时间戳 | 不是已经验过票上时间 | 不是 ExtendVoteRequest.time 就已经验过票上时间（410） |
| 看见有拟议块时间戳 | 不是已经验过块头 | 不是票上 Timestamp 就已经验过（304） |
| 看见能指时间 | 不是已经交差 | 不是 misbehavior 就已经定奖惩（1030） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事（420 余量），必须分开是不是已经验过票上时间、是不是已经验过块头、是不是已经交差。可以跳过「看见填了 Process 请求余栏就已经交差 local_last_commit」。不要另写怎样写 Process 请求余栏。420 procreqrest vs extreq bundled unbundling 在本页 item 2 续；续 [`worked-example-procrestr-notpunish-vs-bundled.md`](worked-example-procrestr-notpunish-vs-bundled.md)（不变量 1030 item 3）。

## 本页不抄

- 怎样写 Process 请求余栏、怎样填 proposed_last_commit、怎样填 time。
- Process 请求余栏 bundled。那是不变量 420。
- ExtendVoteRequest.time 就已经验过票上时间。那是不变量 410。
- 票上 Timestamp 就已经验过。那是不变量 304。
