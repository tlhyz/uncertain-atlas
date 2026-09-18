# 反模式：把 VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事（436 余量） 写成已经 已经按原样签 / 已经包进 CanonicalVoteExtension / 已经有重放保护

**层次**：实现 / VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事（436 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应**：[`../tracks/implementation/worked-example-vreqb-notraw-vs-bundled.md`](../tracks/implementation/worked-example-vreqb-notraw-vs-bundled.md)。

把 VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事（436 余量） 写成已经 已经按原样签 / 已经包进 CanonicalVoteExtension / 已经有重放保护，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 raw-sign 正式三事（436 余量），必须分开 not already signed-as-is、not already wrapped、not already replay-protected 三件事，不要和 436 / 358 / 1079 / 1080 糊成一句。

也不是：

- [vreqb-notext-sold-as-bundled](vreqb-notext-sold-as-bundled.md) 是 non_rp 仍未是 vote_extension 单句边界（1080 item 2），不是本页 raw-sign 仍未按原样签边界。
- non_rp_extension 按应用给的字节原样签就已经有重放保护是不变量 358，不是本页不加元信息仍未包进 CanonicalVoteExtension 边界。
