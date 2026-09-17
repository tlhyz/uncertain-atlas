# 例：看见 ExtendVoteRequest.height is not already aligned interchangeable / not already will-call interchangeable / not already snapshot-height interchangeable

**层次**：实现 / ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事（410 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事（410 余量）/ not 1023 extreqhash-notalign interchangeable / not 410 extreqhash-vs-process bundled interchangeable」，不是 ExtendVote 请求栏 bundled（410），也不是请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote（409），也不是 Verify 空扩展就已经跳过（353）。不要另写怎样写 ExtendVote 请求栏。

## 官方三件事

1. **看见 ExtendVoteRequest.height 是拟议块高度（用来对一下） / 看见填了 height 这份栏 is not already 已经对上了拟议块 interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1023 extreqhash-notalign interchangeable / 1022 extreqhash-notproc interchangeable / 410 extreq item 1 hash interchangeable，也不是已经 ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事 bundled（410 item 2 余量） interchangeable / 410 extreq item 2 interchangeable。**  
   官方写：height 是拟议块高度，用来对一下。看见填了 height，不是已经 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块那种已经会调 interchangeable——本页从 410 item 2 侧钉 not already aligned 单句。410 extreqhash vs process bundled unbundling 在本页 item 2 续。

2. **看见能对一下 / 看见填了 height / 这份栏 is not already 已经会调 ExtendVote interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1023 extreqhash-notalign interchangeable / 410 extreq item 3 time interchangeable / 1024 extreqhash-notts interchangeable，也不是已经请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote interchangeable / 409 extreq-vs-precommit interchangeable。**  
   官方把能对一下和已经会调 ExtendVote 分开。看见能对一下，不是已经会调 interchangeable。本页钉 not already will-call 单句。

3. **看见有高度 / 看见填了 height / 这份栏 is not already 已经是拍快照的高度 interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1023 extreqhash-notalign interchangeable / 1022 extreqhash-notproc interchangeable，也不是已经 Verify 空扩展就已经跳过 interchangeable / 353 verifyusage interchangeable。**  
   官方把有高度和已经是拍快照的高度分开。看见有高度，不是已经是拍快照的高度 interchangeable。410 extreqhash vs process bundled unbundling 在本页 item 2 续。

怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.height not already aligned ≠ 已经对上了拟议块 interchangeable：** 官方把用来对一下的高度和请求内容已经对应拟议块分开。
- **看见能对一下 not already will-call ≠ 已经会调 ExtendVote interchangeable：** 官方把能对一下和已经会调分开。
- **看见有高度 not already snapshot-height ≠ 已经是拍快照的高度 interchangeable：** 官方把有高度和已经是拍快照的高度分开；410 extreqhash vs process bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.height 是拟议块高度（用来对一下） | 不是已经对上了拟议块 | 不是请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote（409） |
| 看见能对一下 | 不是已经会调 ExtendVote | 不是 Verify 空扩展就已经跳过（353） |
| 看见有高度 | 不是已经是拍快照的高度 | 不是 time 就已经验过票上时间（1024） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.height not already aligned / not already will-call / not already snapshot-height 正式三事（410 余量），必须分开是不是已经对上了拟议块、是不是已经会调 ExtendVote、是不是已经是拍快照的高度。可以跳过「看见填了 ExtendVote 请求栏就已经跑过 Process」。不要另写怎样写 ExtendVote 请求栏。410 extreqhash vs process bundled unbundling 在本页 item 2 续；续 [`worked-example-extreqhash-notts-vs-bundled.md`](worked-example-extreqhash-notts-vs-bundled.md)（不变量 1024 item 3）。

## 本页不抄

- 怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度。
- ExtendVote 请求栏 bundled。那是不变量 410。
- 请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote。那是不变量 409。
- 请求里的 hash 不是已经对该块跑过 Process。那是不变量 353。
