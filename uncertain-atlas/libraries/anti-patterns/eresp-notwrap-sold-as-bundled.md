# 反模式：把 ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事（418 余量） 写成已经 已经会包进 CanonicalVoteExtension / 已经是同一份扩展 / 已经交差

**层次**：实现 / ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事（418 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-eresp-notwrap-vs-bundled.md`](../tracks/implementation/worked-example-eresp-notwrap-vs-bundled.md)。

把 ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事（418 余量） 写成已经 已经会包进 CanonicalVoteExtension / 已经是同一份扩展 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 正式三事（418 余量），必须分开 not already canonical-wrapped、not already same-ext、not already settled 三件事，不要和 418 / 358 / 338 / 1083 / 1084 糊成一句。

也不是：

- [vreqb-notraw-sold-as-bundled](vreqb-notraw-sold-as-bundled.md) 是 Verify non_rp raw-sign 仍未按原样签边界（436/1081），不是本页 ExtendVote vote_extension 仍未包进 Canonical 边界。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签是不变量 358，不是本页标成非确定仍未是同一份扩展边界。
