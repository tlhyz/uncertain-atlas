# 例：看见 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥；看见 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension；看见 non_rp 相对 vote_extension 签名时不加额外元信息不是已经按原样签

**层次**：实现 / Verify 请求栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥 / VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension / non_rp 相对 vote_extension 签名时不加额外元信息不是已经按原样签」，不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希，也不是 ExtendVoteResponse.non_rp_extension 就已经按原样签。不要另写怎样写 Verify 请求栏。

## 官方三件事

规范把 Verify 请求栏上 `validator_address` 是签了这份扩展的验证者地址、`non_rp_vote_extension` 是应用自己的信息、由 CometBFT 签且可选可空、相对 `vote_extension` 签名时不加额外元信息写成三件独立的实现事，不是「看见填了 Verify 请求栏就已经带了公钥、已经是 vote_extension、已经按原样签」一件事：

1. **看见 `VerifyVoteExtensionRequest.validator_address` 是签了这份扩展的验证者地址 / 看见填了 validator_address 不是已经带了公钥，也不是已经是 ExtendVoteRequest.proposer_address 那种造提案的人。**  
   官方写：`validator_address` 是签了这份扩展的验证者地址。看见填了 validator_address，不是已经 `Validator` 用 address 认人那种已经带了公钥。看见能指签扩展的人，不是已经是造这份提案的 proposer_address。看见有地址，不是已经能验签。
2. **看见 `VerifyVoteExtensionRequest.non_rp_vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空 不是已经是 `vote_extension`，也不是已经跳过 Verify。**  
   官方写：`non_rp_vote_extension` 是应用自己的信息，由 CometBFT 签，可以 0 长。Usage 也写：`non_rp_vote_extension` 可选，也可以空。看见有第二份，不是已经和 `vote_extension` 同一对象。看见能空，不是已经空扩展仍会调 Verify 那种已经跳过 Verify。
3. **看见 non_rp 相对 `vote_extension` 签名时不加额外元信息 / 看见 CometBFT 按原样签 不是已经有 Height / Round / ChainID 包装，也不是已经 `non_rp_extension` 按应用给的字节原样签那种已经有重放保护。**  
   官方写：`non_rp_vote_extension` 用来放应由 CometBFT 按原样签的扩展信息；相对 `vote_extension`，签名前不再加额外元信息。看见按原样签，不是已经 `vote_extension` 会包进 `CanonicalVoteExtension` 那种已经绑了 Height / Round / ChainID。看见不加元信息，不是已经 ExtendVoteResponse.non_rp_extension 那种已经有重放保护。

怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp 是规范里的做法，本页不抄。Validator 用 address 认人就已经带了公钥是不变量 364，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 ≠ 已经带了公钥：** 官方把签了这份扩展的验证者地址和 VoteInfo 里 Validator 已经带了公钥分开。
- **VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 ≠ 已经是 vote_extension：** 官方把第二份可选字段和第一份 vote_extension 分开。
- **non_rp 相对 vote_extension 签名时不加额外元信息 ≠ 已经按原样签：** 官方把 Verify 请求里这份按原样签和 ExtendVote 回包 Usage 里 non_rp 按原样签分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 | 不是已经带了公钥 | 不是 ExtendVoteRequest.proposer_address 就已经知道本头哈希（413） |
| VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 | 不是已经是 vote_extension | 不是 VerifyVoteExtensionRequest.vote_extension 就已经跳过 Verify（415） |
| non_rp 相对 vote_extension 签名时不加额外元信息 | 不是已经按原样签 | 不是 non_rp_extension 按应用给的字节原样签就已经有重放保护（358） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Verify 请求栏就已经带了公钥、已经是 vote_extension、已经按原样签」，必须分开 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址是不是已经带了公钥、VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长是不是已经是 vote_extension、non_rp 相对 vote_extension 签名时不加额外元信息是不是已经按原样签。可以跳过「看见填了 Verify 请求栏就已经带了公钥」。不要另写怎样写 Verify 请求栏。

## 本页不抄

- 怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
- VerifyVoteExtensionRequest.height / hash / vote_extension 那三列。那是不变量 415。
- ExtendVoteRequest.proposer_address 就已经知道本头哈希。那是不变量 413。
