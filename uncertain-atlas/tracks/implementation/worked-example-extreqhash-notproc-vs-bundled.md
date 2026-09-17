# 例：看见 ExtendVoteRequest.hash is not already processed interchangeable / not already settled interchangeable / not already signed interchangeable

**层次**：实现 / ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事（410 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事（410 余量）/ not 1022 extreqhash-notproc interchangeable / not 410 extreqhash-vs-process bundled interchangeable」，不是 ExtendVote 请求栏 bundled（410），也不是请求里的 hash 不是已经对该块跑过 Process（353），也不是票上 Timestamp 就已经验过（304）。不要另写怎样写 ExtendVote 请求栏。

## 官方三件事

1. **看见 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希 / 看见填了 hash 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1022 extreqhash-notproc interchangeable / 1023 extreqhash-notalign interchangeable / 410 extreq item 2 height interchangeable，也不是已经 ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事 bundled（410 item 1 余量） interchangeable / 410 extreq item 1 interchangeable。**  
   官方写：hash 是扩展要指的那份拟议块的头哈希。看见填了 hash，不是已经 VerifyVoteExtensionRequest.hash 那种指一份拟议块、不保证已经对该块跑过 Process interchangeable——本页从 410 item 1 侧钉 not already processed 单句。410 extreqhash vs process bundled unbundling 在本页 item 1 启动。

2. **看见有头哈希 / 看见填了 hash / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1022 extreqhash-notproc interchangeable / 410 extreq item 3 time interchangeable / 1024 extreqhash-notts interchangeable，也不是已经请求里的 hash 不是已经对该块跑过 Process interchangeable / 353 verifyusage interchangeable。**  
   官方把有头哈希和已经交差分开。看见有头哈希，不是已经交差 interchangeable。本页钉 not already settled 单句。

3. **看见能指 / 看见填了 hash / 这份栏 is not already 已经签了 interchangeable，也不是已经 ExtendVote 请求栏 bundled（410） interchangeable / 1022 extreqhash-notproc interchangeable / 1023 extreqhash-notalign interchangeable，也不是已经票上 Timestamp 就已经验过 interchangeable / 304 votets interchangeable。**  
   官方把能指和已经签了分开。看见能指，不是已经签了 interchangeable。410 extreqhash vs process bundled unbundling 在本页 item 1 启动。

怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.hash not already processed ≠ 已经跑过 Process interchangeable：** 官方把扩展要指的头哈希和已经对该块跑过 Process 分开。
- **看见有头哈希 not already settled ≠ 已经交差 interchangeable：** 官方把有头哈希和已经交差分开。
- **看见能指 not already signed ≠ 已经签了 interchangeable：** 官方把能指和已经签了分开；410 extreqhash vs process bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希 | 不是已经跑过 Process | 不是请求里的 hash 不是已经对该块跑过 Process（353） |
| 看见有头哈希 | 不是已经交差 | 不是票上 Timestamp 就已经验过（304） |
| 看见能指 | 不是已经签了 | 不是 height 就已经对上了拟议块（1023） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest.hash not already processed / not already settled / not already signed 正式三事（410 余量），必须分开是不是已经跑过 Process、是不是已经交差、是不是已经签了。可以跳过「看见填了 ExtendVote 请求栏就已经跑过 Process」。不要另写怎样写 ExtendVote 请求栏。410 extreqhash vs process bundled unbundling 在本页 item 1 启动；续 [`worked-example-extreqhash-notalign-vs-bundled.md`](worked-example-extreqhash-notalign-vs-bundled.md)（不变量 1023 item 2）。

## 本页不抄

- 怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度。
- ExtendVote 请求栏 bundled。那是不变量 410。
- 请求里的 hash 不是已经对该块跑过 Process。那是不变量 353。
- 票上 Timestamp 就已经验过。那是不变量 304。
