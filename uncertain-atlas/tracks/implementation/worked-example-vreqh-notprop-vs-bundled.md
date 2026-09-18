# 例：看见 VerifyVoteExtensionRequest.height is not already proposed-height interchangeable / not already aligned interchangeable / not already will-call interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事（415 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事（415 余量）/ not 1088 vreqh-notprop interchangeable / not 415 verifyheight-vs-extheight bundled interchangeable」，不是 Verify 请求余栏 bundled（415），也不是 ExtendVoteRequest.height 就已经对上了拟议块（410），也不是 Verify When 正式流程就已经跳过 Verify（435）。不要另写怎样写 Verify 请求余栏。

## 官方三件事

1. **看见 VerifyVoteExtensionRequest.height 是块高度（用来对一下） / 看见填了 height 这份栏 is not already 已经是拟议块高度 interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1088 vreqh-notprop interchangeable / 1089 vreqh-notproc interchangeable / 415 verifyheight item 2 hash interchangeable，也不是已经 VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事 bundled（415 item 1 余量） interchangeable / 415 verifyheight item 1 interchangeable。**  
   官方写：height 是块高度，用来对一下。看见填了 height，不是已经是拟议块高度 interchangeable——本页从 415 item 1 侧钉 not already proposed-height 单句。415 verifyheight vs extheight bundled unbundling 在本页 item 1 启动。

2. **看见能对一下 / 看见填了 height / 这份栏 is not already 已经对上了拟议块 interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1088 vreqh-notprop interchangeable / 415 verifyheight item 3 vote_extension interchangeable / 1090 vreqh-notskip interchangeable，也不是已经 ExtendVoteRequest.height 就已经对上了拟议块 interchangeable / 410 extreqhash interchangeable。**  
   官方把能对一下和已经对上了拟议块分开。看见能对一下，不是已经对上了 interchangeable。本页钉 not already aligned 单句。

3. **看见有高度 / 看见填了 height / 这份栏 is not already 已经会调 Verify interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1088 vreqh-notprop interchangeable / 1089 vreqh-notproc interchangeable，也不是已经 Verify When 正式流程就已经跳过 Verify interchangeable / 435 vfwhen interchangeable。**  
   官方把有高度和已经会调 Verify 分开。看见有高度，不是已经会调 Verify interchangeable。415 verifyheight vs extheight bundled unbundling 在本页 item 1 启动。

怎样写 Verify 请求余栏、怎样对高度、怎样填 hash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.height not already proposed-height ≠ 已经是拟议块高度 interchangeable：** 官方把 Verify 请求表上这份块高度和 ExtendVote 请求表上那份拟议块高度分开。
- **看见能对一下 not already aligned ≠ 已经对上了拟议块 interchangeable：** 官方把能对一下和已经对上了分开。
- **看见有高度 not already will-call ≠ 已经会调 Verify interchangeable：** 官方把有高度和已经会调 Verify 分开；415 verifyheight vs extheight bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.height 是块高度（用来对一下） | 不是已经是拟议块高度 | 不是 ExtendVoteRequest.height 就已经对上了拟议块（410） |
| 看见能对一下 | 不是已经对上了拟议块 | 不是 Verify When 正式流程就已经跳过 Verify（435） |
| 看见有高度 | 不是已经会调 Verify | 不是 hash 就已经不保证跑过 Process（1089） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.height not already proposed-height / not already aligned / not already will-call 正式三事（415 余量），必须分开是不是已经是拟议块高度、是不是已经对上了拟议块、是不是已经会调 Verify。可以跳过「看见填了 Verify 请求余栏就已经是拟议块高度」。不要另写怎样写 Verify 请求余栏。415 verifyheight vs extheight bundled unbundling 在本页 item 1 启动；续 [`worked-example-vreqh-notproc-vs-bundled.md`](worked-example-vreqh-notproc-vs-bundled.md)（不变量 1089 item 2）。

## 本页不抄

- 怎样写 Verify 请求余栏、怎样对高度、怎样填 hash。
- Verify 请求余栏 bundled。那是不变量 415。
- ExtendVoteRequest.height 就已经对上了拟议块。那是不变量 410。
- Verify When 正式流程就已经跳过 Verify。那是不变量 435。
