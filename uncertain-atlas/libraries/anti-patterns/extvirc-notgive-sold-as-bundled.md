# 反模式：把 ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事（425 余量） 写成已经 已经把验过的签交给应用 / 已经是 extension_signature / 已经交差

**层次**：实现 / ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事（425 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvirc-notgive-vs-bundled.md`](../tracks/implementation/worked-example-extvirc-notgive-vs-bundled.md)。

把 ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事（425 余量） 写成已经 已经把验过的签交给应用 / 已经是 extension_signature / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension_signature 正式三事（425 余量），必须分开 not already given-to-app、not already same-as-extsig、not already settled 三件事，不要和 425 / 421 / 1052 / 1053 糊成一句。

也不是：

- [extvirc-notflag-sold-as-bundled](extvirc-notflag-sold-as-bundled.md) 是 block_id_flag 仍未罚没单句边界（1053 item 2），不是本页 non_rp 签仍未交给应用边界。
- ExtendedVoteInfo.extension_signature 就已经把验过的签交给应用是不变量 421，不是本页验过了仍未是 extension_signature 边界。
