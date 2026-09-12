# 模式：把 VerifyVoteExtension 确定性三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8 [`VerifyVoteExtension`, determinism]。  
**例**：[Verify 必须只依赖扩展、这块和上一份状态 ≠ 已经可以像 ExtendVote 那样依赖其它值](../../tracks/implementation/worked-example-verify-det-vs-extend.md)。

## 三个名字

1. **Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值：** 看见必须确定不是已经和 ExtendVote 同一把尺。
2. **两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决：** 看见扩展来自拜占庭不是已经可以各判各的。
3. **Verify 非确定会伤活性不是已经丢了安全性：** 看见活性会被伤不是已经有协议层补丁。

## 为什么要分开叫

官方把 Verify 必须确定、对拜占庭扩展也要同一裁决、活性会被伤写成三件事。把它们叫成一个「看见必须确定就已经可以像 ExtendVote 那样」，会把 ExtendVote 可以不确定、验签拒收和 Process 确定性一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须确定就已经可以像 ExtendVote 那样」，先数清问的是 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值、两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决，还是 Verify 非确定会伤活性不是已经丢了安全性，再决定要不要同一次发布。
