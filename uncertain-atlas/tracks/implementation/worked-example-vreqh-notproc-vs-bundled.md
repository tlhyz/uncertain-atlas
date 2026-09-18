# 例：看见 VerifyVoteExtensionRequest.hash is not already not-guaranteed-processed interchangeable / not already ext-hash interchangeable / not already settled interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.hash not already not-guaranteed-processed / not already ext-hash / not already settled 正式三事（415 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.hash not already not-guaranteed-processed / not already ext-hash / not already settled 正式三事（415 余量）/ not 1089 vreqh-notproc interchangeable / not 415 verifyheight-vs-extheight bundled interchangeable」，不是 Verify 请求余栏 bundled（415），也不是请求里的 hash 就已经对该块跑过 Process（353），也不是 ExtendVoteRequest.hash 就已经跑过 Process（410）。不要另写怎样写 Verify 请求余栏。

## 官方三件事

1. **看见 VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希 / 看见填了 hash 这份栏 is not already 已经不保证跑过 Process interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1089 vreqh-notproc interchangeable / 1088 vreqh-notprop interchangeable / 415 verifyheight item 1 height interchangeable，也不是已经 VerifyVoteExtensionRequest.hash not already not-guaranteed-processed / not already ext-hash / not already settled 正式三事 bundled（415 item 2 余量） interchangeable / 415 verifyheight item 2 interchangeable。**  
   官方写：hash 是扩展要指的那份拟议块的哈希。看见填了 hash，不是已经不保证跑过 Process interchangeable——本页从 415 item 2 侧钉 not already not-guaranteed-processed 单句。415 verifyheight vs extheight bundled unbundling 在本页 item 2 续。

2. **看见有拟议块哈希 / 看见填了 hash / 这份栏 is not already 已经是 ExtendVoteRequest.hash interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1089 vreqh-notproc interchangeable / 415 verifyheight item 3 vote_extension interchangeable / 1090 vreqh-notskip interchangeable，也不是已经请求里的 hash 就已经对该块跑过 Process interchangeable / 353 verifyusage interchangeable。**  
   官方把有拟议块哈希和已经是 ExtendVoteRequest.hash 分开。看见有拟议块哈希，不是已经是 ExtendVoteRequest.hash interchangeable。本页钉 not already ext-hash 单句。

3. **看见能指 / 看见填了 hash / 这份栏 is not already 已经交差 interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1089 vreqh-notproc interchangeable / 1088 vreqh-notprop interchangeable，也不是已经 ExtendVoteRequest.hash 就已经跑过 Process interchangeable / 410 extreqhash interchangeable。**  
   官方把能指和已经交差分开。看见能指，不是已经交差 interchangeable。415 verifyheight vs extheight bundled unbundling 在本页 item 2 续。

怎样写 Verify 请求余栏、怎样对高度、怎样填 hash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.hash not already not-guaranteed-processed ≠ 已经不保证跑过 Process interchangeable：** 官方把表描述和 Usage 那句不保证已经对该块跑过 Process 分开。
- **看见有拟议块哈希 not already ext-hash ≠ 已经是 ExtendVoteRequest.hash interchangeable：** 官方把 Verify 这份 hash 和 ExtendVote 那份 hash 分开。
- **看见能指 not already settled ≠ 已经交差 interchangeable：** 官方把能指和已经交差分开；415 verifyheight vs extheight bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希 | 不是已经不保证跑过 Process | 不是请求里的 hash 就已经对该块跑过 Process（353） |
| 看见有拟议块哈希 | 不是已经是 ExtendVoteRequest.hash | 不是 ExtendVoteRequest.hash 就已经跑过 Process（410） |
| 看见能指 | 不是已经交差 | 不是 vote_extension 就已经跳过 Verify（1090） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.hash not already not-guaranteed-processed / not already ext-hash / not already settled 正式三事（415 余量），必须分开是不是已经不保证跑过 Process、是不是已经是 ExtendVoteRequest.hash、是不是已经交差。可以跳过「看见填了 Verify 请求余栏就已经是拟议块高度」。不要另写怎样写 Verify 请求余栏。415 verifyheight vs extheight bundled unbundling 在本页 item 2 续；续 [`worked-example-vreqh-notskip-vs-bundled.md`](worked-example-vreqh-notskip-vs-bundled.md)（不变量 1090 item 3）。

## 本页不抄

- 怎样写 Verify 请求余栏、怎样对高度、怎样填 hash。
- Verify 请求余栏 bundled。那是不变量 415。
- 请求里的 hash 就已经对该块跑过 Process。那是不变量 353。
- ExtendVoteRequest.hash 就已经跑过 Process。那是不变量 410。
