# 例：看见 VerifyVoteExtensionRequest.vote_extension is not already skip-verify interchangeable / not already signed-as-is interchangeable / not already settled interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事（415 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事（415 余量）/ not 1090 vreqh-notskip interchangeable / not 415 verifyheight-vs-extheight bundled interchangeable」，不是 Verify 请求余栏 bundled（415），也不是空扩展仍会调 Verify 就已经跳过 Verify（353），也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358）。不要另写怎样写 Verify 请求余栏。

## 官方三件事

1. **看见 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空 这份栏 is not already 已经跳过 Verify interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1090 vreqh-notskip interchangeable / 1088 vreqh-notprop interchangeable / 415 verifyheight item 1 height interchangeable，也不是已经 VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事 bundled（415 item 3 余量） interchangeable / 415 verifyheight item 3 interchangeable。**  
   官方写：vote_extension 是应用自己的信息，由 CometBFT 签，可以 0 长。看见可以 0 长，不是已经跳过 Verify interchangeable——本页从 415 item 3 侧钉 not already skip-verify 单句。415 verifyheight vs extheight bundled unbundling 在本页 item 3 完成。

2. **看见由 CometBFT 签 / 看见能空 / 这份栏 is not already 已经按原样签 interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1090 vreqh-notskip interchangeable / 415 verifyheight item 2 hash interchangeable / 1089 vreqh-notproc interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签 interchangeable / 358 extresp interchangeable。**  
   官方把由 CometBFT 签和已经按原样签分开。看见由 CometBFT 签，不是已经按原样签 interchangeable。本页钉 not already signed-as-is 单句。

3. **看见是应用自己的信息 / 看见能空 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Verify 请求余栏 bundled（415） interchangeable / 1090 vreqh-notskip interchangeable / 1088 vreqh-notprop interchangeable，也不是已经空扩展仍会调 Verify 就已经跳过 Verify interchangeable / 353 verifyusage interchangeable。**  
   官方把是应用自己的信息和已经交差分开。看见是应用自己的信息，不是已经交差 interchangeable。415 verifyheight vs extheight bundled unbundling 在本页 item 3 完成。

怎样写 Verify 请求余栏、怎样对高度、怎样填 hash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.vote_extension not already skip-verify ≠ 已经跳过 Verify interchangeable：** 官方把表上可以 0 长和空扩展仍会调 Verify 分开。
- **看见由 CometBFT 签 not already signed-as-is ≠ 已经按原样签 interchangeable：** 官方把由 CometBFT 签和已经按原样签分开。
- **看见是应用自己的信息 not already settled ≠ 已经交差 interchangeable：** 官方把是应用自己的信息和已经交差分开；415 verifyheight vs extheight bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 | 不是已经跳过 Verify | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| 看见由 CometBFT 签 | 不是已经按原样签 | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |
| 看见是应用自己的信息 | 不是已经交差 | 不是 height 就已经是拟议块高度（1088） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.vote_extension not already skip-verify / not already signed-as-is / not already settled 正式三事（415 余量），必须分开是不是已经跳过 Verify、是不是已经按原样签、是不是已经交差。可以跳过「看见填了 Verify 请求余栏就已经是拟议块高度」。不要另写怎样写 Verify 请求余栏。415 verifyheight vs extheight bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Verify 请求余栏、怎样对高度、怎样填 hash。
- Verify 请求余栏 bundled。那是不变量 415。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
