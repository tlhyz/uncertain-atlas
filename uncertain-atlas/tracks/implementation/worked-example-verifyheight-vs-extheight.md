# 例：看见 VerifyVoteExtensionRequest.height 是块高度（用来对一下）不是已经是拟议块高度；看见 VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希不是已经不保证跑过 Process；看见 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经跳过 Verify

**层次**：实现 / Verify 请求余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.height 是块高度（用来对一下）不是已经是拟议块高度 / VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希不是已经不保证跑过 Process / VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经跳过 Verify」，不是 ExtendVoteRequest.height 就已经对上了拟议块，也不是请求里的 hash 就已经对该块跑过 Process。不要另写怎样写 Verify 请求余栏。

## 官方三件事

规范把 VerifyVoteExtension Request 表上 `height` 是块高度（用来对一下）、`hash` 是扩展要指的那份拟议块哈希、`vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长写成三件独立的实现事，不是「看见填了 Verify 请求余栏就已经是拟议块高度、已经不保证跑过 Process、已经跳过 Verify」一件事：

1. **看见 `VerifyVoteExtensionRequest.height` 是块高度（用来对一下） / 看见填了 height 不是已经是拟议块高度，也不是已经对上了拟议块。**  
   官方写：`height` 是块高度，用来对一下。看见填了 height，不是已经是 `ExtendVoteRequest.height` 那种拟议块高度（用来对一下）。看见能对一下，不是已经对上了。看见有高度，不是已经会调 Verify。
2. **看见 `VerifyVoteExtensionRequest.hash` 是扩展要指的那份拟议块哈希 / 看见填了 hash 不是已经不保证跑过 Process，也不是已经是 ExtendVoteRequest.hash。**  
   官方写：`hash` 是扩展要指的那份拟议块的哈希。看见填了 hash，不是已经是 Usage 那种指一份拟议块、不保证已经对该块跑过 Process。看见有拟议块哈希，不是已经是 `ExtendVoteRequest.hash` 那种扩展要指的那份拟议块头哈希。看见能指，不是已经交差。
3. **看见 `VerifyVoteExtensionRequest.vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空 不是已经跳过 Verify，也不是已经按原样签。**  
   官方写：`vote_extension` 是应用自己的信息，由 CometBFT 签，可以 0 长。看见可以 0 长，不是已经空扩展仍会调 Verify 那种已经跳过 Verify。看见由 CometBFT 签，不是已经 `vote_extension` 会包进 `CanonicalVoteExtension` 那种已经按原样签。看见是应用自己的信息，不是已经交差。

怎样写 Verify 请求余栏、怎样对高度、怎样填 hash 是规范里的做法，本页不抄。ExtendVoteRequest.height 就已经对上了拟议块是不变量 410，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.height 是块高度（用来对一下） ≠ 已经是拟议块高度：** 官方把 Verify 请求表上这份块高度和 ExtendVote 请求表上那份拟议块高度分开。
- **VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希 ≠ 已经不保证跑过 Process：** 官方把表描述和 Usage 那句不保证已经对该块跑过 Process 分开。
- **VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 ≠ 已经跳过 Verify：** 官方把表上可以 0 长和空扩展仍会调 Verify 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.height 是块高度（用来对一下） | 不是已经是拟议块高度 | 不是 ExtendVoteRequest.height 就已经对上了拟议块（410） |
| VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希 | 不是已经不保证跑过 Process | 不是请求里的 hash 就已经对该块跑过 Process（353） |
| VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 | 不是已经跳过 Verify | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Verify 请求余栏就已经是拟议块高度、已经不保证跑过 Process、已经跳过 Verify」，必须分开 VerifyVoteExtensionRequest.height 是块高度（用来对一下）是不是已经是拟议块高度、VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希是不是已经不保证跑过 Process、VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长是不是已经跳过 Verify。可以跳过「看见填了 Verify 请求余栏就已经是拟议块高度」。不要另写怎样写 Verify 请求余栏。

## 本页不抄

- 怎样写 Verify 请求余栏、怎样对高度、怎样填 hash。
- ExtendVoteRequest.height 就已经对上了拟议块。那是不变量 410。
- 请求里的 hash 就已经对该块跑过 Process。那是不变量 353。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
