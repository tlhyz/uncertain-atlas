# 模式：把 VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage SHOULD Accept default strategy 句。  
**例**：[SHOULD Accept default strategy ≠ bundled](../../tracks/implementation/worked-example-verifyaccept-default-vs-bundled.md)。

## 三个名字

1. **SHOULD Accept default strategy 不是 can't Reject：** 看见 default strategy not can't Reject，不是 457 bundled interchangeable / 527 SHOULD always Accept interchangeable / 433 MUST Accept interchangeable。
2. **REJECT rejects whole vote 不是 can't Reject：** 看见 REJECT path exists，不是 457 bundled interchangeable / 517 When REJECT discard interchangeable / 34 block invalid interchangeable。
3. **default Accept 不是 Verify det SHOULD Accept general rule (341)：** 看见 default Accept，不是 457 bundled interchangeable / 341 nondet liveness interchangeable / 433 response bundled interchangeable。

## 为什么要分开叫

官方把 SHOULD Accept default strategy、REJECT rejects whole vote、default Accept not Verify det general rule、Verify SHOULD Accept bundled（457）、SHOULD always set ACCEPT（527）、unless really know liveness（528）写成三个名字。把它们叫成一个「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」，会把 default strategy、REJECT 路径存在、341 通则三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事，先数清问的是 default strategy 是不是 can't Reject、REJECT rejects whole vote 是不是 can't Reject、default Accept 是不是 Verify 341 general rule，再决定要不要同一次发布。
