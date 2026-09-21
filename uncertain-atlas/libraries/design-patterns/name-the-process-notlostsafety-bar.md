# 模式：把 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（340 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5。  
**例**：[Process 非确定 bug 没有现成解法 not already lost-safety ≠ bundled（340）](../../tracks/implementation/worked-example-process-notlostsafety-vs-bundled.md)。

## 三个名字

1. **活性不能保证 不是 already lost-safety：** 看见活性不能保证 / Process 里有非确定 bug / 打中的进程无法守 Req 4 或 5，不是已经丢了安全性 interchangeable / 已经丢安全性交差 interchangeable，不是 340 processdet bundled interchangeable / 327 preparetimeout interchangeable / processdet-sold-as-prepare interchangeable。

2. **没有现成解法 不是 already has-patch：** 看见没有现成解法 / 目前没有清楚的解法 / 没有协议层补丁，不是已经有引擎补丁 interchangeable / 已经有补丁交差 interchangeable，不是 33 four gates interchangeable / 340 processdet item 1 interchangeable。

3. **SHOULD Accept 不是 already must-reject：** 看见 SHOULD Accept / 通则是一律 Accept / 建议一律 Accept，不是已经必须拒坏块 interchangeable / 已经必须拒交差 interchangeable，不是 347 req3-coherence interchangeable / 340 processdet item 2 interchangeable。

官方把活性不能保证单句、already lost-safety、already has-patch、already must-reject 写成三个名字。把它们叫成一个「看见活性不能保证就已经丢了安全性 interchangeable / 就已经有补丁 interchangeable / 就必须拒坏块 interchangeable」，会把 not already lost-safety、not already has-patch、not already must-reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 非确定 bug 没有现成解法不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（340 余量），先数清问的是活性不能保证 是不是 already lost-safety / 340 / processdet-sold-as-prepare，是不是没有现成解法 是不是 already has-patch，还是 SHOULD Accept 是不是 already must-reject，再决定要不要同一次发布。340 processdet vs prepare bundled unbundling 在本页 item 3 完成。
