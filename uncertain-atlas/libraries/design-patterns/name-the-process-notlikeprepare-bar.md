# 模式：把 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（340 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 4–5。  
**例**：[Process 必须只依赖请求和上一份状态 not already like-prepare ≠ bundled（340）](../../tracks/implementation/worked-example-process-notlikeprepare-vs-bundled.md)。

## 三个名字

1. **必须确定 不是 already like-prepare：** 看见 ProcessProposal 必须只依赖本次请求和 *s_{h-1}* / 必须确定 / 是确定函数，不是已经可以像 Prepare 那样依赖其它值 interchangeable / 已经可以依赖其它值交差 interchangeable，不是 340 processdet bundled interchangeable / 338 preparenondet interchangeable / processdet-sold-as-prepare interchangeable。

2. **只依赖请求和上一份状态 不是 already same-as-nondet：** 看见只依赖请求和上一份状态 / 只依赖 *u* 和 *s_{h-1}* / 不能另依赖其它值，不是已经和 Prepare 没有确定性要求同一句 interchangeable / 已经和 Prepare / ExtendVote 同一把尺交差 interchangeable，不是 338 preparenondet interchangeable / 340 processdet item 2 interchangeable。

3. **Process 回了 不是 already settled：** 看见 Process 回了 / ProcessProposal 回了 / Accept 或 Reject 回来了，不是已经交差 interchangeable / 已经交差同一句 interchangeable，不是 33 four gates interchangeable / 340 processdet item 3 interchangeable。

官方把必须确定单句、already like-prepare、already same-as-nondet、already settled 写成三个名字。把它们叫成一个「看见必须确定就可以像 Prepare 那样 interchangeable / 就已经和 Prepare nondet 同一句 interchangeable / 就已经交差 interchangeable」，会把 not already like-prepare、not already same-as-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值 not already like-prepare / not already same-as-nondet / not already settled 正式三事（340 余量），先数清问的是必须确定 是不是 already like-prepare / 340 / processdet-sold-as-prepare，是不是只依赖请求和上一份状态 是不是 already same-as-nondet，还是 Process 回了 是不是 already settled，再决定要不要同一次发布。340 processdet vs prepare bundled unbundling 在本页 item 1 启动。
