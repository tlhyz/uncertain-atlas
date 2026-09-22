# 模式：把 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事（347 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**例**：[Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only-liveness ≠ bundled（347）](../../tracks/implementation/worked-example-req3-notbyz-vs-bundled.md)。

## 三个名字

1. **Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 不是 already only-liveness：** 看见 Prepare 或 Process（或两边）里有确定 bug / 踩中的人严格算拜占庭 / 有确定 bug，不是已经只是活性问题 interchangeable / 已经 only-liveness interchangeable / 已经只伤活性交差 interchangeable，不是 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable。

2. **算拜占庭 不是 already process-nondet：** 看见算拜占庭 / 踩中的人严格算拜占庭 / 确定 bug 让人算拜占庭，不是已经是 Process 非确定 bug interchangeable / 已经 process-nondet interchangeable / 已经非确定交差 interchangeable，不是 340 processdet interchangeable / 33 four gates interchangeable。

3. **Prepare 也能踩中 不是 already settled：** 看见 Prepare 也能踩中 / Prepare 或 Process 两边都能踩 / 不只是 Process 会踩，不是已经交差 interchangeable / 已经 settled interchangeable / 已经踩中交差 interchangeable，不是 794 req3-notany interchangeable / 796 req3-nottested interchangeable。

官方把确定 bug 算拜占庭、不是已经是非确定 bug、不是已经交差写成三个名字。把它们叫成一个「看见算拜占庭就已经只是活性问题 interchangeable / 就已经是非确定 bug interchangeable / 就已经交差 interchangeable」，会把 not already only-liveness、not already process-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事（347 余量），先数清问的是 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 是不是 already only-liveness / 347 / req3coherence-sold-as-accept，是不是算拜占庭 是不是 already process-nondet，还是 Prepare 也能踩中 是不是 already settled，再决定要不要同一次发布。347 req3 vs accept bundled unbundling 在本页 item 2 续。
