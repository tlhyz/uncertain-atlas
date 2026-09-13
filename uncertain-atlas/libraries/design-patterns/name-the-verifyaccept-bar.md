# 模式：把 VerifyVoteExtension SHOULD Accept 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**例**：[应用 SHOULD 总是设 ACCEPT ≠ 已经正确进程交出的扩展必须 Accept](../../tracks/implementation/worked-example-verifyaccept-vs-req6.md)。

## 三个名字

1. **SHOULD 总是设 ACCEPT 不是已经正确进程交出的扩展必须 Accept：** 看见 SHOULD always set to ACCEPT 不是已经 Requirement 6 已经测过。
2. **除非真的知道 REJECT 的活性代价不是已经拒整张 Precommit 是免费过滤：** 看见 unless they really know liveness implications 不是已经验签拒收整张 Precommit 就已经是块非法。
3. **SHOULD Accept 默认策略不是已经不能 Reject：** 看见 SHOULD Accept 不是已经 Verify 433 那种 SHOULD Accept 通则 interchangeable。

## 为什么要分开叫

官方把 VerifyVoteExtension SHOULD Accept 写成三个名字。把它们叫成一个「看见写了默认 Accept 就已经正确进程交出的扩展必须 Accept」，会把 SHOULD 建议、REJECT 活性代价和 Requirement 6 测试目标一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见写了默认 Accept 就已经正确进程交出的扩展必须 Accept」，先数清问的是 SHOULD 总是设 ACCEPT 是不是已经正确进程交出的扩展必须 Accept、除非真的知道 REJECT 的活性代价是不是已经拒整张 Precommit 是免费过滤，还是 SHOULD Accept 默认策略是不是已经 Requirement 6 已经测过，再决定要不要同一次发布。
