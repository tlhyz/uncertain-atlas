# 反模式：把 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事（347 余量）说成已经只是活性问题 / 已经是非确定 bug / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only-liveness ≠ bundled（347）](../../tracks/implementation/worked-example-req3-notbyz-vs-bundled.md)。

## 卖法

把 Prepare 或 Process（或两边）里有确定 bug / 踩中的人严格算拜占庭 / 有确定 bug 写成已经只是活性问题 interchangeable / 已经 only-liveness interchangeable / 已经只伤活性交差 interchangeable / 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable；把算拜占庭 / 踩中的人严格算拜占庭 写成已经是 Process 非确定 bug interchangeable / 已经 process-nondet interchangeable / 已经非确定交差 interchangeable；把 Prepare 也能踩中 / Prepare 或 Process 两边都能踩 写成已经交差 interchangeable / 已经 settled interchangeable / 已经踩中交差 interchangeable，或已经和 347 req3coherence bundled / req3coherence-sold-as-accept interchangeable / 795 req3-notbyz interchangeable。

## 为什么错

官方把确定 bug 算拜占庭、不是已经是非确定 bug、不是已经交差写成三件独立的实现事。把它们卖成 already only-liveness interchangeable / already process-nondet interchangeable / already settled interchangeable，会把 not already only-liveness、not already process-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事（347 余量），必须分开 not already only-liveness、not already process-nondet、not already settled 三件事，不要和 347 / 340 / 33 / 794 / 796 糊成一句。

## 和相邻反模式

- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是 Prepare–Process 一致性 bundled 全段，不是本页确定 bug 算拜占庭 item 2 单句边界。
- [req3-notany-sold-as-bundled](req3-notany-sold-as-bundled.md) 是正确提议者的准备提案必须 Accept not already any-block（347 item 1），不是本页 not already only-liveness 边界。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 Process 必须只依赖请求和上一份状态（340），不是本页算拜占庭 ≠ 非确定 bug 边界。
