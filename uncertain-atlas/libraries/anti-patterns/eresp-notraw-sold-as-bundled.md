# 反模式：把 ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事（418 余量） 写成已经 已经按原样签 / 已经有重放保护 / 已经必须填

**层次**：实现 / ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事（418 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-eresp-notraw-vs-bundled.md`](../tracks/implementation/worked-example-eresp-notraw-vs-bundled.md)。

把 ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事（418 余量） 写成已经 已经按原样签 / 已经有重放保护 / 已经必须填，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension 正式三事（418 余量），必须分开 not already signed-as-is、not already replay-protected、not already must-fill 三件事，不要和 418 / 358 / 436 / 1082 / 1084 糊成一句。

也不是：

- [eresp-notwrap-sold-as-bundled](eresp-notwrap-sold-as-bundled.md) 是 vote_extension 仍未包进 Canonical 单句边界（1082 item 1），不是本页 non_rp_extension 仍未按原样签边界。
- non_rp_extension 按应用给的字节原样签就已经有重放保护是不变量 358，不是本页标成非确定仍未有重放保护边界。
