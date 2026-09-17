# 例：看见 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希不是已经跑过 Process；看见 ExtendVoteRequest.height 是拟议块高度（用来对一下）不是已经对上了拟议块；看见 ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳不是已经验过票上时间

**层次**：实现 / ExtendVote 请求栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希不是已经跑过 Process / ExtendVoteRequest.height 是拟议块高度（用来对一下）不是已经对上了拟议块 / ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳不是已经验过票上时间」，不是请求里的 hash 不是已经对该块跑过 Process，也不是请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote。不要另写怎样写 ExtendVote 请求栏。

## 官方三件事

规范把 `ExtendVoteRequest.hash` 是扩展要指的那份拟议块头哈希、`height` 是拟议块高度（用来对一下）、`time` 是扩展要指的那份拟议块时间戳写成三件独立的实现事，不是「看见填了 ExtendVote 请求栏就已经跑过 Process、已经对上了拟议块、已经验过票上时间」一件事：

1. **看见 `ExtendVoteRequest.hash` 是扩展要指的那份拟议块头哈希 / 看见填了 hash 不是已经跑过 Process，也不是已经交差。**  
   官方写：`hash` 是扩展要指的那份拟议块的头哈希。看见填了 hash，不是已经 `VerifyVoteExtensionRequest.hash` 那种指一份拟议块、不保证已经对该块跑过 Process。看见有头哈希，不是已经交差。看见能指，不是已经签了。
2. **看见 `ExtendVoteRequest.height` 是拟议块高度（用来对一下） / 看见填了 height 不是已经对上了拟议块，也不是已经会调 ExtendVote。**  
   官方写：`height` 是拟议块高度，用来对一下。看见填了 height，不是已经 `ExtendVoteRequest` 的内容对应共识即将发 Precommit 的那份拟议块那种已经会调。看见能对一下，不是已经对上了。看见有高度，不是已经是拍快照的高度。
3. **看见 `ExtendVoteRequest.time` 是扩展要指的那份拟议块时间戳 / 看见填了 time 不是已经验过票上时间，也不是已经交差。**  
   官方写：`time` 是扩展要指的那份拟议块的时间戳。看见填了 time，不是已经票上 Timestamp 那种已经验过。看见能指时间，不是已经交差。看见有时间戳，不是已经是过错发生那一高已提交块的时间。

怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度是规范里的做法，本页不抄。请求里的 hash 不是已经对该块跑过 Process 是不变量 353，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希 ≠ 已经跑过 Process：** 官方把扩展要指的头哈希和已经对该块跑过 Process 分开。
- **ExtendVoteRequest.height 是拟议块高度（用来对一下） ≠ 已经对上了拟议块：** 官方把用来对一下的高度和请求内容已经对应拟议块分开。
- **ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳 ≠ 已经验过票上时间：** 官方把扩展要指的时间戳和票上时间已经验过分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希 | 不是已经跑过 Process | 不是请求里的 hash 不是已经对该块跑过 Process（353） |
| ExtendVoteRequest.height 是拟议块高度（用来对一下） | 不是已经对上了拟议块 | 不是请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote（409） |
| ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳 | 不是已经验过票上时间 | 不是票上 Timestamp 就已经验过（304） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求栏就已经跑过 Process、已经对上了拟议块、已经验过票上时间」，必须分开 ExtendVoteRequest.hash 是扩展要指的那份拟议块头哈希是不是已经跑过 Process、ExtendVoteRequest.height 是拟议块高度（用来对一下）是不是已经对上了拟议块、ExtendVoteRequest.time 是扩展要指的那份拟议块时间戳是不是已经验过票上时间。可以跳过「看见填了 ExtendVote 请求栏就已经跑过 Process」。不要另写怎样写 ExtendVote 请求栏。

## 本页不抄

- 怎样写 ExtendVote 请求栏、怎样填 hash、怎样对高度。
- 请求里的 hash 不是已经对该块跑过 Process。那是不变量 353。
- 请求内容对应即将发 Precommit 的拟议块就已经会调 ExtendVote。那是不变量 409。
- 票上 Timestamp 就已经验过。那是不变量 304。
