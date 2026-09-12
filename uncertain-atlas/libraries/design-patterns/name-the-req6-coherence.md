# 模式：把 Extend–Verify 一致性三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**例**：[正确进程交出的扩展必须被正确接收者 Verify Accept ≠ 已经是任意扩展都会 Accept](../../tracks/implementation/worked-example-req6-coherence-vs-accept.md)。

## 三个名字

1. **正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept：** 看见正确进程之间必须过不是任意扩展已经都会过。
2. **Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题：** 看见 Precommit 被丢掉不是已经是块非法。
3. **会面对和 Req 5 同一类活性问题不是已经丢了安全性：** 看见和 Process 确定性那条同一路不是已经是提案一致性。

## 为什么要分开叫

官方把正确进程之间必须过、确定 bug 丢掉 Precommit、因此面对和 Req 5 同一类活性问题写成三件事。把它们叫成一个「看见必须 Accept 就已经交差」，会把拒收整张预提交、Verify 确定性和提案一致性一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须 Accept 就已经交差」，先数清问的是正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept、Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题，还是会面对和 Req 5 同一类活性问题不是已经丢了安全性，再决定要不要同一次发布。
