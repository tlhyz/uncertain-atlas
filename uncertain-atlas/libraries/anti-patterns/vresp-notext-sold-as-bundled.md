# 反模式：把 VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事（433 余量） 写成已经 已经可以像 ExtendVote 那样依赖其它值 / 已经和对任意扩展同一裁决一回事 / 已经和 ExtendVote 同一把尺

**层次**：实现 / VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事（433 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-vresp-notext-vs-bundled.md`](../tracks/implementation/worked-example-vresp-notext-vs-bundled.md)。

把 VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事（433 余量） 写成已经 已经可以像 ExtendVote 那样依赖其它值 / 已经和对任意扩展同一裁决一回事 / 已经和 ExtendVote 同一把尺，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 exclusive dependence 正式三事（433 余量），必须分开 not already extend-nondet、not already same-ruling、not already same-ruler 三件事，不要和 433 / 338 / 1076 / 1078 糊成一句。

也不是：

- [vresp-notinvalid-sold-as-bundled](vresp-notinvalid-sold-as-bundled.md) 是 status 仍未当成块非法单句边界（1076 item 1），不是本页 exclusive dependence 仍未可以像 ExtendVote 那样边界。
- ExtendVote 没有确定性要求就已经可以像 ExtendVote 那样是不变量 338，不是本页必须只依赖仍未和对任意扩展同一裁决一回事边界。
