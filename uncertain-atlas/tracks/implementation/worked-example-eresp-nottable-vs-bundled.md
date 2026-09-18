# 例：看见 VerifyVoteExtensionRequest.non_rp_vote_extension is not already vote-ext-table interchangeable / not already skip-verify interchangeable / not already same-copy interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事（418 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事（418 余量）/ not 1084 eresp-nottable interchangeable / not 418 extresp-vs-wrap bundled interchangeable」，不是扩展回包栏 bundled（418），也不是 VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify（415），也不是 Verify 请求栏 non_rp 就已经是 vote_extension（436）。不要另写怎样写扩展回包栏。

## 官方三件事

1. **看见 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空 这份栏 is not already 已经是 vote_extension 表 interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1084 eresp-nottable interchangeable / 1082 eresp-notwrap interchangeable / 418 extresp item 1 vote_extension interchangeable，也不是已经 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事 bundled（418 item 3 余量） interchangeable / 418 extresp item 3 interchangeable。**  
   官方写：non_rp_vote_extension 是应用自己的信息，由 CometBFT 签，可以 0 长。看见可以 0 长，不是已经是 vote_extension 表 interchangeable——本页从 418 item 3 侧钉 not already vote-ext-table 单句。418 extresp vs wrap bundled unbundling 在本页 item 3 完成。

2. **看见由 CometBFT 签 / 看见能空 / 这份栏 is not already 已经跳过 Verify interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1084 eresp-nottable interchangeable / 418 extresp item 2 non_rp interchangeable / 1083 eresp-notraw interchangeable，也不是已经 VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify interchangeable / 415 verifyheight interchangeable。**  
   官方把由 CometBFT 签和已经跳过 Verify 分开。看见由 CometBFT 签，不是已经跳过 Verify interchangeable。本页钉 not already skip-verify 单句。

3. **看见是应用自己的信息 / 看见能空 / 这份栏 is not already 已经和 vote_extension 同一份 interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1084 eresp-nottable interchangeable / 1082 eresp-notwrap interchangeable，也不是已经 Verify 请求栏 non_rp 就已经是 vote_extension interchangeable / 436 verifyreqbar interchangeable。**  
   官方把是应用自己的信息和已经和 vote_extension 同一份分开。看见是应用自己的信息，不是已经和 vote_extension 同一份 interchangeable。418 extresp vs wrap bundled unbundling 在本页 item 3 完成。

怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table ≠ 已经是 vote_extension 表 interchangeable：** 官方把 Verify 请求表上这份第二栏和第一栏分开。
- **看见由 CometBFT 签 not already skip-verify ≠ 已经跳过 Verify interchangeable：** 官方把由 CometBFT 签和已经跳过 Verify 分开。
- **看见是应用自己的信息 not already same-copy ≠ 已经和 vote_extension 同一份 interchangeable：** 官方把是应用自己的信息和已经同一份分开；418 extresp vs wrap bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 | 不是已经是 vote_extension 表 | 不是 VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify（415） |
| 看见由 CometBFT 签 | 不是已经跳过 Verify | 不是 Verify 请求栏 non_rp 就已经是 vote_extension（436） |
| 看见是应用自己的信息 | 不是已经和 vote_extension 同一份 | 不是 vote_extension 就已经会包进 CanonicalVoteExtension（1082） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-ext-table / not already skip-verify / not already same-copy 正式三事（418 余量），必须分开是不是已经是 vote_extension 表、是不是已经跳过 Verify、是不是已经和 vote_extension 同一份。可以跳过「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension」。不要另写怎样写扩展回包栏。418 extresp vs wrap bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension。
- 扩展回包栏 bundled。那是不变量 418。
- VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify。那是不变量 415。
- Verify 请求栏 non_rp 就已经是 vote_extension。那是不变量 436。
