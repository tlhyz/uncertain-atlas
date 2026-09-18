# 模式：点名 vresp-notext 杠

**层次**：实现 / VerifyVoteExtensionResponse.status exclusive dependence not already extend-nondet / not already same-ruling / not already same-ruler 正式三事（433 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-vresp-notext-vs-bundled.md`](../tracks/implementation/worked-example-vresp-notext-vs-bundled.md)。

- **exclusive dependence 不是已经可以像 ExtendVote 那样：** 看见回了 status，不是已经可以像 ExtendVote 那样依赖其它值 interchangeable / 1077 vresp-notext interchangeable。
- **看见必须只依赖 不是已经和对任意扩展同一裁决一回事：** 看见必须只依赖，不是已经和对任意扩展同一裁决一回事 interchangeable。
- **看见有确定要求 不是已经和 ExtendVote 同一把尺：** 看见有确定要求，不是已经和 ExtendVote 同一把尺 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 exclusive dependence 正式三事（433 余量），先数清问的是是不是已经可以像 ExtendVote 那样、是不是已经和对任意扩展同一裁决一回事、还是看见有确定要求是不是已经和 ExtendVote 同一把尺，再决定要不要同一次发布。433 verifyresp vs status bundled unbundling 在本页 item 2 续。
