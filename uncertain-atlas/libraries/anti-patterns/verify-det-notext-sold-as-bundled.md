# 反模式：把 Verify 必须只依赖扩展、这块和上一份状态 not already ExtendVote-style other values / not already same ruler as ExtendVote / not already settled 正式三事（341 余量） 卖成 已经可以像 ExtendVote 那样依赖其它值 / 已经和 ExtendVote 同一把尺 / 已经交差

**层次**：实现 / VerifyVoteExtension 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-verify-det-notext-vs-bundled.md](../../tracks/implementation/worked-example-verify-det-notext-vs-bundled.md)。

官方把 Verify 必须只依赖扩展、这块和上一份状态 / 两边对任意扩展同一裁决 / Verify 非确定会伤活性 三条核心句写成三件独立的实现事。把它们卖成已经可以像 ExtendVote 那样依赖其它值 / 已经和 ExtendVote 同一把尺 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 必须只依赖扩展、这块和上一份状态 正式三事（341 余量），必须分开 not already ExtendVote-style other values、not already same ruler as ExtendVote、not already settled 三件事，不要和 341 / 338 / 34 / 891 / 892 糊成一句。

## 和相邻反模式

- [finalize-det-notprep-sold-as-bundled](finalize-det-notprep-sold-as-bundled.md) 是 Finalize 状态必须确定（342/887），不是本页 Verify 确定性边界。
- ExtendVote 没有确定性要求是不变量 338，不是本页 Verify 确定性边界。
