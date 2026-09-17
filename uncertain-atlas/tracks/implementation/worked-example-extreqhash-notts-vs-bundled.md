# 例：看见 ExtendVoteRequest.time is not already vote-ts-checked interchangeable / not already settled interchangeable / not already evidence-time interchangeable

**层次**：实现 / ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事（410 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事（410 余量）/ not 1024 extreqhash-notts interchangeable / not 410 extreqhash-vs-process bundled interchangeable」，不是 ExtendVote 请求栏 bundled（410），也不是票上 Timestamp 就已经验过（304），也不是迟到扩展就已经 Verify（352）。不要另写怎样写 ExtendVote 请求栏。

## 官方三件事

1. **看见 ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳 / 看见填了 time 这份栏 is not already 已经验过票上时间 interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1024 extreqhash-notts interchangeable / 1022 extreqhash-notproc interchangeable / 410 extreq item 1 hash interchangeable，也不是已经 ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事 bundled（410 item 3 余量） interchangeable / 410 extreq item 3 interchangeable。**  
   官方写：time 是扩展要指的那份拟议块的时间戳。看见填了 time，不是已经票上 Timestamp 那种已经验过 interchangeable——本页从 410 item 3 侧钉 not already vote-ts-checked 单句。410 extreqhash vs process bundled unbundling 在本页 item 3 完成。

2. **看见能指时间 / 看见填了 time / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1024 extreqhash-notts interchangeable / 410 extreq item 2 height interchangeable / 1023 extreqhash-notalign interchangeable，也不是已经票上 Timestamp 就已经验过 interchangeable / 304 votets interchangeable。**  
   官方把能指时间和已经交差分开。看见能指时间，不是已经交差 interchangeable。本页钉 not already settled 单句。

3. **看见有时间戳 / 看见填了 time / 这份栏 is not already 已经是过错发生那一高已提交块的时间 interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1024 extreqhash-notts interchangeable / 1022 extreqhash-notproc interchangeable，也不是已经迟到扩展就已经 Verify interchangeable / 352 lateext interchangeable。**  
   官方把有时间戳和已经是过错发生那一高已提交块的时间分开。看见有时间戳，不是已经是过错发生那一高已提交块的时间 interchangeable。410 extreqhash vs process bundled unbundling 在本页 item 3 完成。

怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.time not already vote-ts-checked ≠ 已经验过票上时间 interchangeable：** 官方把扩展要指的时间戳和票上时间已经验过分开。
- **看见能指时间 not already settled ≠ 已经交差 interchangeable：** 官方把能指时间和已经交差分开。
- **看见有时间戳 not already evidence-time ≠ 已经是过错发生那一高已提交块的时间 interchangeable：** 官方把有时间戳和已经是过错发生那一高已提交块的时间分开；410 extreqhash vs process bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳 | 不是已经验过票上时间 | 不是票上 Timestamp 就已经验过（304） |
| 看见能指时间 | 不是已经交差 | 不是迟到扩展就已经 Verify（352） |
| 看见有时间戳 | 不是已经是过错发生那一高已提交块的时间 | 不是 hash 就已经跑过 Process（1022） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.time not already vote-ts-checked / not already settled / not already evidence-time 正式三事（410 余量），必须分开是不是已经验过票上时间、是不是已经交差、是不是已经是过错发生那一高已提交块的时间。可以跳过「看见填了 ExtendVote 请求栏就已经跑过 Process」。不要另写怎样写 ExtendVote 请求栏。410 extreqhash vs process bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度。
- ExtendVote 请求栏 bundled。那是不变量 410。
- 票上 Timestamp 就已经验过。那是不变量 304。
- 迟到扩展就已经 Verify。那是不变量 352。
