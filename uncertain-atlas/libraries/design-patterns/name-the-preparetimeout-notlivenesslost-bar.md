# 模式：把又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事（327 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**例**：[又开一轮 not already liveness-lost ≠ bundled（327）](../../tracks/implementation/worked-example-preparetimeout-notlivenesslost-vs-bundled.md)。

## 三个名字

1. **又开一轮 不是 already liveness-lost：** 看见又开一轮 / 再开一轮 / 违反后可能再开一轮，不是已经丢了活性 interchangeable / 已经活性丢掉交差 interchangeable，不是 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable。

2. **TimeoutPropose 只是初值 不是 already timeout-frozen：** 看见 TimeoutPropose 只是初值 / 超时还会涨 / 动态往上调，不是已经超时不再涨 interchangeable / 已经超时冻住交差 interchangeable，不是 416 proposetimeout interchangeable / 327 preparetimeout item 1 interchangeable。

3. **看见初值 不是 already final-tier：** 看见初值 / 不是最后那一档 / 还会再调，不是已经是最后那一档 interchangeable / 已经末档交差 interchangeable，不是 52 next-block-delay interchangeable / 327 preparetimeout item 2 interchangeable。

官方把又开一轮单句、already liveness-lost、already timeout-frozen、already final-tier 写成三个名字。把它们叫成一个「看见又开一轮就已经丢了活性 interchangeable / 就已经超时不再涨 interchangeable / 就已经是最后那一档 interchangeable」，会把 not already liveness-lost、not already timeout-frozen、not already final-tier 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看又开一轮不是已经丢了活性 not already liveness-lost / not already timeout-frozen / not already final-tier 正式三事（327 余量），先数清问的是又开一轮 是不是 already liveness-lost / 327 / preparetimeout-sold-as-liveness，是不是 TimeoutPropose 只是初值 是不是 already timeout-frozen，还是看见初值 是不是 already final-tier，再决定要不要同一次发布。327 preparetimeout vs liveness bundled unbundling 在本页 item 3 完成。
