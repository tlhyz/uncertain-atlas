# 模式：把 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事（361 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**例**：[ExtendVote 同步 not already later-revise ≠ bundled（361）](../../tracks/implementation/worked-example-extwhen-notlaterrevise-vs-bundled.md)。

## 三个名字

1. **是同步的 不是 already later-revise：** 看见是同步的 / CometBFT 调 `ExtendVote` 是同步的 / 引擎同步等回包，不是已经能在返回之后再改扩展 interchangeable / 已经 later-revise interchangeable / 已经能稍后改扩展交差 interchangeable，不是 361 extendwhen bundled interchangeable / extendwhen-sold-as-locked interchangeable。

2. **引擎在等 不是 already left-critical：** 看见引擎在等 / 引擎在等回包 / 同步阻塞，不是已经离开关键路径 interchangeable / 已经 left-critical interchangeable / 已经离开关键路径交差 interchangeable，不是 354 processwhen interchangeable / 833 extwhen-notwillcall interchangeable。

3. **回了 不是 already settled：** 看见回了 / 回包回来了 / 同步调用返回了，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 835 extwhen-notsameext interchangeable / 33 fourgates interchangeable。

官方把是同步的、不是已经离开关键路径、不是已经交差写成三个名字。把它们叫成一个「看见是同步的就已经能稍后改扩展 interchangeable / 就已经离开关键路径 interchangeable / 就已经交差 interchangeable」，会把 not already later-revise、not already left-critical、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 调用是同步的不是已经能在返回之后再改扩展 not already later-revise / not already left-critical / not already settled 正式三事（361 余量），先数清问的是是同步的 是不是 already later-revise / 361 / extendwhen-sold-as-locked，是不是引擎在等 是不是 already left-critical，还是回了 是不是 already settled，再决定要不要同一次发布。361 extend-when vs locked bundled unbundling 在本页 item 2 续。
