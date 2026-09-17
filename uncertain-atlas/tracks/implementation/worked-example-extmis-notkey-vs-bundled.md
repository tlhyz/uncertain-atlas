# 例：看见 VerifyVoteExtensionRequest.validator_address is not already has-key interchangeable / not already can-verify interchangeable / not already settled interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事（413 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事（413 余量）/ not 1039 extmis-notkey interchangeable / not 413 extreqmis-vs-reward bundled interchangeable」，不是 ExtendVote 请求末栏 bundled（413），也不是 Validator 用 address 认人就已经带了公钥（364），也不是空扩展仍会调 Verify 就已经跳过（353）。不要另写怎样写 ExtendVote 请求末栏。

## 官方三件事

1. **看见 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 / 看见填了 validator_address 这份栏 is not already 已经带了公钥 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1039 extmis-notkey interchangeable / 1037 extmis-notpunish interchangeable / 413 extreqmis item 1 misbehavior interchangeable，也不是已经 VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事 bundled（413 item 3 余量） interchangeable / 413 extreqmis item 3 interchangeable。**  
   官方写：validator_address 是签了这份扩展的验证者地址。看见填了 validator_address，不是已经 Validator 用 address 认人那种已经带了公钥 interchangeable——本页从 413 item 3 侧钉 not already has-key 单句。413 extreqmis vs reward bundled unbundling 在本页 item 3 完成。

2. **看见能指签扩展的人 / 看见填了 validator_address / 这份栏 is not already 已经能验签 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1039 extmis-notkey interchangeable / 413 extreqmis item 2 proposer interchangeable / 1038 extmis-notheader interchangeable，也不是已经 Validator 用 address 认人就已经带了公钥 interchangeable / 364 validator interchangeable。**  
   官方把能指签扩展的人和已经能验签分开。看见能指签扩展的人，不是已经能验签 interchangeable。本页钉 not already can-verify 单句。

3. **看见有地址 / 看见填了 validator_address / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求末栏 bundled（413） interchangeable / 1039 extmis-notkey interchangeable / 1037 extmis-notpunish interchangeable，也不是已经空扩展仍会调 Verify 就已经跳过 interchangeable / 353 verifyusage interchangeable。**  
   官方把有地址和已经交差分开。看见有地址，不是已经交差 interchangeable。413 extreqmis vs reward bundled unbundling 在本页 item 3 完成。

怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.validator_address not already has-key ≠ 已经带了公钥 interchangeable：** 官方把签了这份扩展的验证者地址和已经带了公钥分开。
- **看见能指签扩展的人 not already can-verify ≠ 已经能验签 interchangeable：** 官方把能指签扩展的人和已经能验签分开。
- **看见有地址 not already settled ≠ 已经交差 interchangeable：** 官方把有地址和已经交差分开；413 extreqmis vs reward bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 | 不是已经带了公钥 | 不是 Validator 用 address 认人就已经带了公钥（364） |
| 看见能指签扩展的人 | 不是已经能验签 | 不是空扩展仍会调 Verify 就已经跳过（353） |
| 看见有地址 | 不是已经交差 | 不是 misbehavior 就已经定奖惩（1037） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.validator_address not already has-key / not already can-verify / not already settled 正式三事（413 余量），必须分开是不是已经带了公钥、是不是已经能验签、是不是已经交差。可以跳过「看见填了 ExtendVote 请求末栏就已经定奖惩」。不要另写怎样写 ExtendVote 请求末栏。413 extreqmis vs reward bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendVote 请求末栏、怎样填 misbehavior、怎样填 proposer_address。
- ExtendVote 请求末栏 bundled。那是不变量 413。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
