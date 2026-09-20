# 模式：把填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事（327 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**例**：[填了 TimeoutPropose not already fits-execution ≠ bundled（327）](../../tracks/implementation/worked-example-preparetimeout-notfit-vs-bundled.md)。

## 三个名字

1. **填了 TimeoutPropose 不是 already fits-execution：** 看见填了 TimeoutPropose / 填了这个值 / 有 TimeoutPropose 初值，不是已经装得下这次 Prepare 执行 interchangeable / 已经装得下交差 interchangeable，不是 327 preparetimeout bundled interchangeable / 33 four gates interchangeable / preparetimeout-sold-as-liveness interchangeable。

2. **同步期 不是 already clock-silent：** 看见同步期 / *p*、*q* 同在一轮 / 网络处在同步期，不是已经 *q* 的提议钟不会响 interchangeable / 已经钟不响交差 interchangeable，不是 47 local-timeout interchangeable / 327 preparetimeout item 1 interchangeable。

3. **钟一响就 prevote nil 不是 already propose-bound：** 看见钟一响就 prevote nil / 提议钟挂钩 / 钟响走 nil，不是已经把这一轮提议绑成必成 interchangeable / 已经提议绑死交差 interchangeable，不是 416 proposetimeout interchangeable / 327 preparetimeout item 3 interchangeable。

官方把填了 TimeoutPropose 单句、already fits-execution、already clock-silent、already propose-bound 写成三个名字。把它们叫成一个「看见填了 TimeoutPropose 就已经装得下 interchangeable / 就已经钟不响 interchangeable / 就已经把提议绑死 interchangeable」，会把 not already fits-execution、not already clock-silent、not already propose-bound 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 TimeoutPropose 不是已经装得下 not already fits-execution / not already clock-silent / not already propose-bound 正式三事（327 余量），先数清问的是填了 TimeoutPropose 是不是 already fits-execution / 327 / preparetimeout-sold-as-liveness，是不是同步期 是不是 already clock-silent，还是钟一响就 prevote nil 是不是 already propose-bound，再决定要不要同一次发布。327 preparetimeout vs liveness bundled unbundling 在本页 item 2 续。
