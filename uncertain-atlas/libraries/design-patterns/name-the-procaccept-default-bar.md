# 模式：把 ProcessProposal Usage SHOULD Accept default strategy 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**例**：[SHOULD Accept default strategy ≠ bundled](../../tracks/implementation/worked-example-procaccept-default-vs-bundled.md)。

## 三个名字

1. **SHOULD Accept default strategy 不是 can't Reject：** 看见 default strategy not can't Reject，不是 456 bundled interchangeable / 530 SHOULD always Accept interchangeable / 430 MUST Accept interchangeable。
2. **REJECT assumes not valid 不是 can't Reject：** 看见 REJECT path exists，不是 456 bundled interchangeable / 455 assumes not valid interchangeable / 33 prevote nil interchangeable。
3. **default Accept 不是 Process det SHOULD Accept general rule (340)：** 看见 default Accept，不是 456 bundled interchangeable / 340 nondet liveness interchangeable / 430 response bundled interchangeable。

## 为什么要分开叫

官方把 SHOULD Accept default strategy、REJECT assumes not valid、default Accept not Process det general rule、Process SHOULD Accept bundled（456）、SHOULD always set ACCEPT（530）、unless really know liveness（531）写成三个名字。把它们叫成一个「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」，会把 default strategy、REJECT 路径存在、340 通则三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事，先数清问的是 default strategy 是不是 can't Reject、REJECT assumes not valid 是不是 can't Reject、default Accept 是不是 Process 340 general rule，再决定要不要同一次发布。
