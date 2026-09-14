# 模式：把 ProcessProposal Usage unless really know liveness implications 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage unless really know liveness implications 句。  
**例**：[unless really know liveness implications ≠ bundled](../../tracks/implementation/worked-example-procaccept-liveness-vs-bundled.md)。

## 三个名字

1. **unless really know liveness implications 不是 free filter：** 看见 unless really know，不是 456 bundled interchangeable / 530 SHOULD always Accept interchangeable / 33 prevote nil not free filter interchangeable。
2. **not free filter Process REJECT prevote nil 不是 Process REJECT already settled：** 看见不是免费过滤，不是 456 bundled interchangeable / 33 prevote nil interchangeable / 455 assumes not valid interchangeable。
3. **can Reject not no cost 不是 can't Reject：** 看见可以 Reject 有代价，不是 456 bundled interchangeable / 532 can't Reject interchangeable / 340 nondet liveness interchangeable。

## 为什么要分开叫

官方把 unless really know liveness implications、not free filter Process REJECT prevote nil、can Reject not no cost、Process SHOULD Accept bundled（456）、SHOULD always set ACCEPT（530）、SHOULD Accept default strategy（532）写成三个名字。把它们叫成一个「看见除非真的知道活性代价 就已经 REJECT 是免费过滤 interchangeable」，会把 unless 条件、not free filter、REJECT 有 liveness 代价三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage unless really know liveness implications 正式三事，先数清问的是 unless really know 是不是 free filter、not free filter 是不是 prevote nil already settled (33)、can Reject 是不是 no cost / can't Reject，再决定要不要同一次发布。
