# 模式：把 ExtendedCommitInfo 轮三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendedCommitInfo / FinalizeBlock Request / Echo Request。  
**例**：[ExtendedCommitInfo.round 是提交轮 ≠ 已经是 CommitInfo.round](../../tracks/implementation/worked-example-extcommitround-vs-commitinfo.md)。

## 三个名字

1. **ExtendedCommitInfo.round 是提交轮不是已经是 CommitInfo.round：** 看见填了 round 不是已经按投票权排过。
2. **Finalize 请求 next_validators_hash 是下一验证者集合默克尔根不是已经是同一套字段：** 看见填了 next_validators_hash 不是已经换了人。
3. **Echo 请求 Message 是要回显的字符串不是已经是 Flush：** 看见填了 Message 不是已经送到。

## 为什么要分开叫

官方把 ExtendedCommitInfo `round` 是提交轮、Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根、Echo 请求 `Message` 是要回显的字符串写成三件事。把它们叫成一个「看见填了 ExtendedCommitInfo 轮就已经是 CommitInfo.round」，会把 CommitInfo.round、同一套字段和 Flush 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendedCommitInfo 轮就已经是 CommitInfo.round」，先数清问的是 ExtendedCommitInfo.round 是提交轮不是已经是 CommitInfo.round、Finalize 请求 next_validators_hash 是下一验证者集合默克尔根不是已经是同一套字段，还是 Echo 请求 Message 是要回显的字符串不是已经是 Flush，再决定要不要同一次发布。
