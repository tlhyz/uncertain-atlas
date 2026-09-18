# 反模式：把 ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事（421 余量） 写成已经 已经把验过的签交给应用 / 已经有重放保护 / 已经交差

**层次**：实现 / ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事（421 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvicol-notgive-vs-bundled.md`](../tracks/implementation/worked-example-extvicol-notgive-vs-bundled.md)。

把 ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事（421 余量） 写成已经 已经把验过的签交给应用 / 已经有重放保护 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 extension_signature 正式三事（421 余量），必须分开 not already given-to-app、not already replay-protected、not already settled 三件事，不要和 421 / 358 / 369 / 1043 / 1044 糊成一句。

也不是：

- [extvicol-notsign-sold-as-bundled](extvicol-notsign-sold-as-bundled.md) 是 non_rp 仍未按原样签单句边界（1044 item 2），不是本页 extension_signature 仍未交给应用边界。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签是不变量 358，不是本页验过了仍未有重放保护边界。
