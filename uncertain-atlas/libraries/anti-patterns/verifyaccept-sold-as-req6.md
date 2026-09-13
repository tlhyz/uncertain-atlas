# 反模式：把 VerifyVoteExtension SHOULD Accept 正式三事说成已经 Requirement 6 已经测过

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[应用 SHOULD 总是设 ACCEPT ≠ 已经正确进程交出的扩展必须 Accept](../../tracks/implementation/worked-example-verifyaccept-vs-req6.md)。

## 错在哪里

把 application implementers SHOULD always set VerifyVoteExtensionResponse.status to ACCEPT 写成已经正确进程交出的扩展必须 Accept，或已经是 Requirement 6 已经测过；把 unless they really know liveness implications 写成已经拒整张 Precommit 是免费过滤；把 SHOULD Accept 默认策略写成已经不能 Reject，或已经和 Verify 433 bundled interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension SHOULD Accept 正式三事，必须分开 SHOULD 总是设 ACCEPT、除非真的知道 REJECT 的活性代价、SHOULD Accept 默认策略三件事，不要和 433 / 348 / 34 / 341 糊成一句。
