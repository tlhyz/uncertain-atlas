# 模式：把 ProcessProposal Response status must exclusively depend 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response status MUST exclusively depend 句。  
**例**：[status must exclusively depend ≠ bundled](../../tracks/implementation/worked-example-procrespstatus-exclusivedep-vs-bundled.md)。

## 三个名字

1. **status MUST exclusively depend 不是 Prepare can depend on other values：** 看见 MUST exclusively depend，不是 430 bundled interchangeable / 338 Prepare nondet interchangeable / 533 valid/invalid interchangeable。
2. **exclusive dependence not Prepare nondet 不是 Process 340 MUST deterministic：** 看见 not Prepare can depend，不是 430 bundled interchangeable / 340 Req 4-5 interchangeable / 338 Prepare MAY nondet interchangeable。
3. **status exclusive dependence 不是 Process 340 same ruling general rule：** 看见 not same ruling，不是 430 bundled interchangeable / 340 same ruling interchangeable / 347 honest proposal must Accept interchangeable。

## 为什么要分开叫

官方把 status MUST exclusively depend、exclusive dependence not Prepare nondet、status exclusive dependence not Process 340 same ruling、Process 回包栏 bundled（430）、Process 340 determinism（340）、status valid/invalid（533）写成三个名字。把它们叫成一个「看见 must exclusively depend 就已经可以像 Prepare 那样依赖其它值 interchangeable」，会把 exclusive dependence、Prepare nondet 边界、340 通则三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Response status must exclusively depend 正式三事，先数清问的是 MUST exclusively depend 是不是 Prepare can depend on other values、exclusive dependence 是不是 Process 340 MUST deterministic、status exclusive dependence 是不是 Process 340 same ruling / 347 honest proposal must Accept，再决定要不要同一次发布。
