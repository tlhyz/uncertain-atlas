# 模式：把 VerifyVoteExtension Response status must exclusively depend 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response status MUST exclusively depend 句。  
**例**：[status must exclusively depend ≠ bundled](../../tracks/implementation/worked-example-verifyrespstatus-exclusivedep-vs-bundled.md)。

## 三个名字

1. **status MUST exclusively depend 不是 ExtendVote can depend on other values：** 看见 MUST exclusively depend，不是 433 bundled interchangeable / 338 ExtendVote nondet interchangeable / 535 valid/invalid interchangeable。
2. **exclusive dependence not ExtendVote nondet 不是 Verify 341 MUST deterministic：** 看见 not ExtendVote can depend，不是 433 bundled interchangeable / 341 Req 7-8 interchangeable / 338 ExtendVote MAY nondet interchangeable。
3. **status exclusive dependence 不是 Verify 341 same ruling general rule：** 看见 not same ruling，不是 433 bundled interchangeable / 341 same ruling interchangeable / 348 correct process must Accept interchangeable。

## 为什么要分开叫

官方把 status MUST exclusively depend、exclusive dependence not ExtendVote nondet、status exclusive dependence not Verify 341 same ruling、Verify 回包栏 bundled（433）、Verify 341 determinism（341）、status valid/invalid（535）写成三个名字。把它们叫成一个「看见 must exclusively depend 就已经可以像 ExtendVote 那样依赖其它值 interchangeable」，会把 exclusive dependence、ExtendVote 边界、341 通则三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Response status must exclusively depend 正式三事，先数清问的是 MUST exclusively depend 是不是 ExtendVote can depend on other values、exclusive dependence 是不是 Verify 341 MUST deterministic、status exclusive dependence 是不是 Verify 341 same ruling / 348 correct process must Accept，再决定要不要同一次发布。
