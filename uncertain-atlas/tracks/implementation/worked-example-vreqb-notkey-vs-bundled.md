# 例：看见 VerifyVoteExtensionRequest.validator_address is not already has-key interchangeable / not already proposer interchangeable / not already can-verify interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事（436 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事（436 余量）/ not 1079 vreqb-notkey interchangeable / not 436 verifyreqbar-vs-rest bundled interchangeable」，不是 Verify 请求栏 bundled（436），也不是 Validator 用 address 认人就已经带了公钥（364），也不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413）。不要另写怎样写 Verify 请求栏。

## 官方三件事

1. **看见 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 / 看见填了 validator_address 这份栏 is not already 已经带了公钥 interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1079 vreqb-notkey interchangeable / 1080 vreqb-notext interchangeable / 436 verifyreqbar item 2 non_rp interchangeable，也不是已经 VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事 bundled（436 item 1 余量） interchangeable / 436 verifyreqbar item 1 interchangeable。**  
   官方写：validator_address 是签了这份扩展的验证者地址。看见填了 validator_address，不是已经 Validator 用 address 认人那种已经带了公钥 interchangeable——本页从 436 item 1 侧钉 not already has-key 单句。436 verifyreqbar vs rest bundled unbundling 在本页 item 1 启动。

2. **看见能指签扩展的人 / 看见填了 validator_address / 这份栏 is not already 已经是造这份提案的 proposer_address interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1079 vreqb-notkey interchangeable / 436 verifyreqbar item 3 raw interchangeable / 1081 vreqb-notraw interchangeable，也不是已经 ExtendVoteRequest.proposer_address 就已经知道本头哈希 interchangeable / 413 extmis interchangeable。**  
   官方把能指签扩展的人和已经是造这份提案的 proposer_address 分开。看见能指签扩展的人，不是已经是造这份提案的 proposer_address interchangeable。本页钉 not already proposer 单句。

3. **看见有地址 / 看见填了 validator_address / 这份栏 is not already 已经能验签 interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1079 vreqb-notkey interchangeable / 1080 vreqb-notext interchangeable，也不是已经 Validator 用 address 认人就已经带了公钥 interchangeable / 364 validator interchangeable。**  
   官方把有地址和已经能验签分开。看见有地址，不是已经能验签 interchangeable。436 verifyreqbar vs rest bundled unbundling 在本页 item 1 启动。

怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.validator_address not already has-key ≠ 已经带了公钥 interchangeable：** 官方把签了这份扩展的验证者地址和已经带了公钥分开。
- **看见能指签扩展的人 not already proposer ≠ 已经是造这份提案的 proposer_address interchangeable：** 官方把能指签扩展的人和已经是造这份提案的 proposer_address 分开。
- **看见有地址 not already can-verify ≠ 已经能验签 interchangeable：** 官方把有地址和已经能验签分开；436 verifyreqbar vs rest bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 | 不是已经带了公钥 | 不是 Validator 用 address 认人就已经带了公钥（364） |
| 看见能指签扩展的人 | 不是已经是造这份提案的 proposer_address | 不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413） |
| 看见有地址 | 不是已经能验签 | 不是 non_rp 就已经是 vote_extension（1080） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事（436 余量），必须分开是不是已经带了公钥、是不是已经是造这份提案的 proposer_address、是不是已经能验签。可以跳过「看见填了 Verify 请求栏就已经带了公钥」。不要另写怎样写 Verify 请求栏。436 verifyreqbar vs rest bundled unbundling 在本页 item 1 启动；续 [`worked-example-vreqb-notext-vs-bundled.md`](worked-example-vreqb-notext-vs-bundled.md)（不变量 1080 item 2）。

## 本页不抄

- 怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp。
- Verify 请求栏 bundled。那是不变量 436。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- ExtendVoteRequest.proposer_address 就已经知道本头哈希。那是不变量 413。
