# 例：看见 VerifyVoteExtensionRequest.non_rp raw-sign is not already signed-as-is interchangeable / not already wrapped interchangeable / not already replay-protected interchangeable

**层次**：实现 / VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事（436 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事（436 余量）/ not 1081 vreqb-notraw interchangeable / not 436 verifyreqbar-vs-rest bundled interchangeable」，不是 Verify 请求栏 bundled（436），也不是 non_rp_extension 按应用给的字节原样签就已经有重放保护（358），也不是 vote_extension 会包进 CanonicalVoteExtension 那种已经绑了 Height / Round / ChainID。不要另写怎样写 Verify 请求栏。

## 官方三件事

1. **看见 non_rp 相对 vote_extension 签名时不加额外元信息 / 看见 CometBFT 按原样签 这份栏 is not already 已经按原样签 interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1081 vreqb-notraw interchangeable / 1079 vreqb-notkey interchangeable / 436 verifyreqbar item 1 validator interchangeable，也不是已经 VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事 bundled（436 item 3 余量） interchangeable / 436 verifyreqbar item 3 interchangeable。**  
   官方写：non_rp_vote_extension 用来放应由 CometBFT 按原样签的扩展信息；相对 vote_extension，签名前不再加额外元信息。看见按原样签，不是已经 ExtendVoteResponse.non_rp_extension 那种已经有重放保护 interchangeable——本页从 436 item 3 侧钉 not already signed-as-is 单句。436 verifyreqbar vs rest bundled unbundling 在本页 item 3 完成。

2. **看见不加元信息 / 看见 CometBFT 按原样签 / 这份栏 is not already 已经包进 CanonicalVoteExtension interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1081 vreqb-notraw interchangeable / 436 verifyreqbar item 2 non_rp interchangeable / 1080 vreqb-notext interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension 那种已经绑了 Height / Round / ChainID interchangeable。**  
   官方把不加元信息和已经包进 CanonicalVoteExtension 分开。看见不加元信息，不是已经包进 CanonicalVoteExtension interchangeable。本页钉 not already wrapped 单句。

3. **看见按原样签 / 看见不加元信息 / 这份栏 is not already 已经有重放保护 interchangeable，也不是已经 Verify 请求栏 bundled（436） interchangeable / 1081 vreqb-notraw interchangeable / 1079 vreqb-notkey interchangeable，也不是已经 non_rp_extension 按应用给的字节原样签就已经有重放保护 interchangeable / 358 extresp interchangeable。**  
   官方把按原样签和已经有重放保护分开。看见按原样签，不是已经有重放保护 interchangeable。436 verifyreqbar vs rest bundled unbundling 在本页 item 3 完成。

怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is ≠ 已经按原样签 interchangeable：** 官方把 Verify 请求里这份按原样签和 ExtendVote 回包 Usage 里 non_rp 按原样签分开。
- **看见不加元信息 not already wrapped ≠ 已经包进 CanonicalVoteExtension interchangeable：** 官方把不加元信息和已经包进 CanonicalVoteExtension 分开。
- **看见按原样签 not already replay-protected ≠ 已经有重放保护 interchangeable：** 官方把按原样签和已经有重放保护分开；436 verifyreqbar vs rest bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| non_rp 相对 vote_extension 签名时不加额外元信息 | 不是已经按原样签 | 不是 non_rp_extension 按应用给的字节原样签就已经有重放保护（358） |
| 看见不加元信息 | 不是已经包进 CanonicalVoteExtension | 不是 vote_extension 会包进 CanonicalVoteExtension |
| 看见按原样签 | 不是已经有重放保护 | 不是 validator_address 就已经带了公钥（1079） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事（436 余量），必须分开是不是已经按原样签、是不是已经包进 CanonicalVoteExtension、是不是已经有重放保护。可以跳过「看见填了 Verify 请求栏就已经带了公钥」。不要另写怎样写 Verify 请求栏。436 verifyreqbar vs rest bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Verify 请求栏、怎样填 validator_address、怎样填 non_rp。
- Verify 请求栏 bundled。那是不变量 436。
- non_rp_extension 按应用给的字节原样签就已经有重放保护。那是不变量 358。
- vote_extension 会包进 CanonicalVoteExtension。那是相邻 Canonical 页，不是本页。
