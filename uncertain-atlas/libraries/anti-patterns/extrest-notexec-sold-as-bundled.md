# 反模式：把 ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事（411 余量） 写成已经 已经执行那些交易 / 已经交差 / 已经整块跑了

**层次**：实现 / ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事（411 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extrest-notexec-vs-bundled.md`](../tracks/implementation/worked-example-extrest-notexec-vs-bundled.md)。

把 ExtendVoteRequest.txs not already executed / not already settled / not already whole-block 正式三事（411 余量） 写成已经 已经执行那些交易 / 已经交差 / 已经整块跑了，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 txs 正式三事（411 余量），必须分开 not already executed、not already settled、not already whole-block 三件事，不要和 411 / 408 / 419 / 1035 / 1036 糊成一句。

也不是：

- [extpre-notlate-sold-as-bundled](extpre-notlate-sold-as-bundled.md) 是 ACCEPT 仍未 Verify 过迟到扩展边界（409/1033），不是本页 txs 仍未执行边界。
- Finalize 按应用自己的规则确定地执行 txs 就已经交差是不变量 408，不是本页有交易列表仍未交差边界。
