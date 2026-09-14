# 模式：把 VerifyVoteExtension Usage SHOULD always set ACCEPT 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage SHOULD always set ACCEPT 句。  
**例**：[SHOULD always set ACCEPT ≠ bundled](../../tracks/implementation/worked-example-verifyaccept-shouldaccept-vs-bundled.md)。

## 三个名字

1. **SHOULD always set ACCEPT 不是 correct process must Accept：** 看见 SHOULD always set to ACCEPT，不是 457 bundled interchangeable / 348 Req 6 must Accept interchangeable / 433 MUST Accept interchangeable。
2. **not already Req 6 tested 不是 Verify SHOULD Accept bundled：** 看见 SHOULD 不是 Req 6 test target，不是 457 bundled interchangeable / 348 Req 6 tested interchangeable / 516 When return ACCEPT interchangeable。
3. **SHOULD is not MUST Accept 不是 Extend–Verify consistency must Accept：** 看见 SHOULD 不是 MUST，不是 457 bundled interchangeable / 348 correct process must Accept interchangeable / 528 unless know liveness interchangeable。

## 为什么要分开叫

官方把 SHOULD always set ACCEPT、not already Req 6 tested、SHOULD is not MUST Accept、Verify SHOULD Accept bundled（457）、Extend–Verify consistency Req 6 must Accept（348）、unless really know liveness（528）写成三个名字。把它们叫成一个「看见写了默认 Accept 就已经 correct process must Accept interchangeable、已经 Requirement 6 已经测过 interchangeable」，会把 SHOULD 建议、Req 6 测试目标、SHOULD vs MUST 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage SHOULD always set ACCEPT 正式三事，先数清问的是 SHOULD always set ACCEPT 是不是 correct process must Accept、not already Req 6 tested 是不是 Verify SHOULD Accept bundled、SHOULD is not MUST Accept 是不是 Extend–Verify consistency must Accept，再决定要不要同一次发布。
