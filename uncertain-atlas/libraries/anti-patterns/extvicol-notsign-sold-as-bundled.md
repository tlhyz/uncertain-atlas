# 反模式：把 ExtendedVoteInfo.non_rp_vote_extension not already signed-as-is / not already replay-protected / not already settled 正式三事（421 余量） 写成已经 已经按原样签 / 已经有重放保护 / 已经交差

**层次**：实现 / ExtendedVoteInfo.non_rp_vote_extension not already signed-as-is / not already replay-protected / not already settled 正式三事（421 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvicol-notsign-vs-bundled.md`](../tracks/implementation/worked-example-extvicol-notsign-vs-bundled.md)。

把 ExtendedVoteInfo.non_rp_vote_extension not already signed-as-is / not already replay-protected / not already settled 正式三事（421 余量） 写成已经 已经按原样签 / 已经有重放保护 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_vote_extension 正式三事（421 余量），必须分开 not already signed-as-is、not already replay-protected、not already settled 三件事，不要和 421 / 418 / 358 / 1043 / 1045 糊成一句。

也不是：

- [extvicol-notextract-sold-as-bundled](extvicol-notextract-sold-as-bundled.md) 是 vote_extension 仍未从本进程抽出单句边界（1043 item 1），不是本页 non_rp 仍未按原样签边界。
- ExtendVoteResponse.non_rp_extension 就已经按原样签是不变量 418，不是本页是应用给的第二份仍未有重放保护边界。
