# 例：看见 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经会包进 CanonicalVoteExtension；看见 ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经按原样签；看见 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension 表

**层次**：实现 / 扩展回包栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经会包进 CanonicalVoteExtension / ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经按原样签 / VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension 表」，不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，也不是 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长就已经跳过 Verify。不要另写怎样写扩展回包栏。

## 官方三件事

规范把 ExtendVote Response 表上 `vote_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定、`non_rp_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定、Verify 请求表上 `non_rp_vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长写成三件独立的实现事，不是「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension、已经按原样签、已经是 vote_extension 表」一件事：

1. **看见 `ExtendVoteResponse.vote_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定 / 看见回了扩展 不是已经会包进 CanonicalVoteExtension，也不是已经没有确定性要求。**  
   官方写：`vote_extension` 是 CometBFT 签的信息，可以 0 长。表上 Deterministic = No。看见回了扩展，不是已经 `vote_extension` 会包进 `CanonicalVoteExtension` 那种已经按原样签。看见标成非确定，不是已经 ExtendVote 没有确定性要求那种已经是同一份扩展。看见可以 0 长，不是已经交差。
2. **看见 `ExtendVoteResponse.non_rp_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定 / 看见回了第二份 不是已经按原样签，也不是已经有重放保护。**  
   官方写：`non_rp_extension` 是 CometBFT 签的信息，可以 0 长。表上 Deterministic = No。看见回了第二份，不是已经 `non_rp_extension` 按应用给的字节原样签那种已经有重放保护。看见标成非确定，不是已经按原样签。看见可以 0 长，不是已经必须填。
3. **看见 `VerifyVoteExtensionRequest.non_rp_vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空 不是已经是 vote_extension 表，也不是已经跳过 Verify。**  
   官方写：`non_rp_vote_extension` 是应用自己的信息，由 CometBFT 签，可以 0 长。看见可以 0 长，不是已经 `VerifyVoteExtensionRequest.vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长那种已经跳过 Verify。看见由 CometBFT 签，不是已经要签原样数据可以用 `non_rp` 那种已经和 vote_extension 同一份。看见是应用自己的信息，不是已经交差。

怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension 是规范里的做法，本页不抄。vote_extension 会包进 CanonicalVoteExtension 就已经按原样签是不变量 358，本页不抄。

## 官方为什么这样拆

- **ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 ≠ 已经会包进 CanonicalVoteExtension：** 官方把回包表描述和 Usage 里那份包装分开。
- **ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 ≠ 已经按原样签：** 官方把回包表描述和 Usage 里那份原样签分开。
- **VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 ≠ 已经是 vote_extension 表：** 官方把 Verify 请求表上这份第二栏和第一栏分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 | 不是已经会包进 CanonicalVoteExtension | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |
| ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 | 不是已经按原样签 | 不是 ExtendVote 没有确定性要求就已经是同一份扩展（338） |
| VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长 | 不是已经是 vote_extension 表 | 不是 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长就已经跳过 Verify（415） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension、已经按原样签、已经是 vote_extension 表」，必须分开 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定是不是已经会包进 CanonicalVoteExtension、ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定是不是已经按原样签、VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长是不是已经是 vote_extension 表。可以跳过「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension」。不要另写怎样写扩展回包栏。

## 本页不抄

- 怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- ExtendVote 没有确定性要求就已经是同一份扩展。那是不变量 338。
- VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长就已经跳过 Verify。那是不变量 415。
