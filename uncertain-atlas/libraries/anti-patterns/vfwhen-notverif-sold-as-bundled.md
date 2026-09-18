# 反模式：把 signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事（435 余量） 写成已经 已经验过扩展 / 已经 Accept / 已经不对本进程自己发出的 Precommit 调用

**层次**：实现 / signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事（435 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-vfwhen-notverif-vs-bundled.md`](../tracks/implementation/worked-example-vfwhen-notverif-vs-bundled.md)。

把 signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事（435 余量） 写成已经 已经验过扩展 / 已经 Accept / 已经不对本进程自己发出的 Precommit 调用，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 calls Verify 正式三事（435 余量），必须分开 not already verified、not already accept、not already local-skip 三件事，不要和 435 / 434 / 433 / 1085 / 1087 糊成一句。

也不是：

- [vfwhen-notskip-sold-as-bundled](vfwhen-notskip-sold-as-bundled.md) 是 unsigned discard 仍未跳过 Verify 单句边界（1085 item 1），不是本页会叫 Verify 仍未验过扩展边界。
- VerifyStatus ACCEPT 就已经验过扩展是不变量 434，不是本页会调仍未 Accept 边界。
