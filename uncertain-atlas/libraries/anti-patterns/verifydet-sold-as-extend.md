# 反模式：看见 Verify 必须只依赖扩展、这块和上一份状态就当成已经可以像 ExtendVote 那样依赖其它值 / 看见两边对任意扩展同一裁决就当成已经只对诚实扩展同一裁决 / 看见 Verify 非确定会伤活性就当成已经丢了安全性

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**例**：[Verify 必须只依赖扩展、这块和上一份状态 ≠ 已经可以像 ExtendVote 那样依赖其它值](../../tracks/implementation/worked-example-verify-det-vs-extend.md)。

## 塌法

1. 看见 `VerifyVoteExtension` 必须只依赖扩展、这块和上一份状态 / 看见必须确定，就当成已经可以像 ExtendVote 那样依赖其它值，或当成已经和 ExtendVote 同一把尺。
2. 看见两边对任意扩展同一裁决 / 看见扩展来自拜占庭，就当成已经只对诚实扩展同一裁决，或当成已经是诚实扩展必须被诚实 Verify Accept。
3. 看见 Verify 里有非确定 bug / 看见活性会被伤，就当成已经丢了安全性，或当成已经有协议层补丁。

## 为什么会出事

官方写：Verify 是确定函数，Accept/Reject 只依赖这份扩展、所指那块和上一份已提交状态。所有正确进程对任意扩展同判，用来挡住拜占庭扩展数据。Verify 若不再确定，活性会被伤。通则是 SHOULD Accept。

## 和相邻反模式

- [verify-notlostsafety-sold-as-bundled](verify-notlostsafety-sold-as-bundled.md) 是 Verify 非确定会伤活性不是已经丢了安全性 item 3 单句边界，不是本页 VerifyVoteExtension 确定性 bundled 全段。
- [verify-nothonestonly-sold-as-bundled](verify-nothonestonly-sold-as-bundled.md) 是两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决 item 2 单句边界，不是本页 VerifyVoteExtension 确定性 bundled 全段。
- [verify-notlikeextend-sold-as-bundled](verify-notlikeextend-sold-as-bundled.md) 是 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 item 1 单句边界，不是本页 VerifyVoteExtension 确定性 bundled 全段。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 ExtendVote 没有确定性要求 ≠ 已经必须确定，不是本页这种 Verify 必须确定 ≠ 已经可以像 ExtendVote 那样。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收已经是块非法，不是本页这种对任意扩展同判 ≠ 已经只对诚实扩展。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 Process 非确定 bug 没有现成解法 ≠ 已经丢了安全性，不是本页这种 Verify 非确定会伤活性 ≠ 已经丢了安全性。
