# 例：看见 VerifyVoteExtensionRequest.non_rp_vote_extension is not already vote-extension interchangeable / not already skip-verify interchangeable / not already same-object interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事（436 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事（436 余量）/ not 1080 vreqb-notext interchangeable / not 436 verifyreqbar-vs-rest bundled interchangeable」，不是 Verify 请求栏 bundled（436），也不是 VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify（415），也不是空扩展仍会调 Verify 就已经跳过 Verify（353）。不要另写怎样写 Verify 请求栏。

## 官方三件事

1. **看见 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空 这份栏 is not already 已经是 vote_extension interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1080 vreqb-notext interchangeable / 1079 vreqb-notkey interchangeable / 436 verifyreqbar item 1 validator interchangeable，也不是已经 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事 bundled（436 item 2 余量） interchangeable / 436 verifyreqbar item 2 interchangeable。**  
   官方写：non_rp_vote_extension 是应用自己的信息，由 CometBFT 签，可以 0 长。Usage 也写：non_rp_vote_extension 可选，也可以空。看见有第二份，不是已经和 vote_extension 同一对象 interchangeable——本页从 436 item 2 侧钉 not already vote-extension 单句。436 verifyreqbar vs rest bundled unbundling 在本页 item 2 续。

2. **看见能空 / 看见填了 non_rp_vote_extension / 这份栏 is not already 已经跳过 Verify interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1080 vreqb-notext interchangeable / 436 verifyreqbar item 3 raw interchangeable / 1081 vreqb-notraw interchangeable，也不是已经 VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify interchangeable / 415 verifyheight interchangeable。**  
   官方把能空和已经跳过 Verify 分开。看见能空，不是已经跳过 Verify interchangeable。本页钉 not already skip-verify 单句。

3. **看见有第二份 / 看见填了 non_rp_vote_extension / 这份栏 is not already 已经和 vote_extension 同一对象 interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1080 vreqb-notext interchangeable / 1079 vreqb-notkey interchangeable，也不是已经空扩展仍会调 Verify 就已经跳过 Verify interchangeable / 353 verifyusage interchangeable。**  
   官方把有第二份和已经和 vote_extension 同一对象分开。看见有第二份，不是已经和 vote_extension 同一对象 interchangeable。436 verifyreqbar vs rest bundled unbundling 在本页 item 2 续。

怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension ≠ 已经是 vote_extension interchangeable：** 官方把第二份可选字段和第一份 vote_extension 分开。
- **看见能空 not already skip-verify ≠ 已经跳过 Verify interchangeable：** 官方把能空和已经跳过 Verify 分开。
- **看见有第二份 not already same-object ≠ 已经和 vote_extension 同一对象 interchangeable：** 官方把有第二份和已经同一对象分开；436 verifyreqbar vs rest bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 | 不是已经是 vote_extension | 不是 VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify（415） |
| 看见能空 | 不是已经跳过 Verify | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| 看见有第二份 | 不是已经和 vote_extension 同一对象 | 不是 non_rp 就已经按原样签（1081） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.non_rp_vote_extension not already vote-extension / not already skip-verify / not already same-object 正式三事（436 余量），必须分开是不是已经是 vote_extension、是不是已经跳过 Verify、是不是已经和 vote_extension 同一对象。可以跳过「看见填了 Verify 请求栏就已经带了公钥」。不要另写怎样写 Verify 请求栏。436 verifyreqbar vs rest bundled unbundling 在本页 item 2 续；续 [`worked-example-vreqb-notraw-vs-bundled.md`](worked-example-vreqb-notraw-vs-bundled.md)（不变量 1081 item 3）。

## 本页不抄

- 怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp。
- Verify 请求栏 bundled。那是不变量 436。
- VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify。那是不变量 415。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
