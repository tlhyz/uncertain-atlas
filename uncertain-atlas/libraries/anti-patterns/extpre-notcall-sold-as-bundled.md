# 反模式：把 ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事（409 余量） 写成已经 已经会调 ExtendVote / 已经只在即将广播非 nil Precommit 时才叫 / 已经交差

**层次**：实现 / ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事（409 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-extpre-notcall-vs-bundled.md`](../tracks/implementation/worked-example-extpre-notcall-vs-bundled.md)。

把 ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事（409 余量） 写成已经 已经会调 ExtendVote / 已经只在即将广播非 nil Precommit 时才叫 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看对应即将发 Precommit 正式三事（409 余量），必须分开 not already will-call、not already non-nil-only、not already settled 三件事，不要和 409 / 350 / 410 / 1032 / 1033 糊成一句。

也不是：

- [procrestr-notpunish-sold-as-bundled](procrestr-notpunish-sold-as-bundled.md) 是 ProcessProposalRequest.misbehavior 仍未定奖惩边界（420/1030），不是本页请求对应仍未会调边界。
- 一轮只能交出一份扩展就已经是每一高度一份是不变量 350，不是本页对上了拟议块仍未只在非 nil Precommit 才叫边界。
