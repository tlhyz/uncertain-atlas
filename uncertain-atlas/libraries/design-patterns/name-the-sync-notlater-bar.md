# 模式：把 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事（354 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[Process 调用是同步的 not already later-revise ≠ bundled（354）](../../tracks/implementation/worked-example-sync-notlater-vs-bundled.md)。

## 三个名字

1. **是同步的 不是 already later-revise：** 看见 Process 调用是同步的 / 是同步的 / 引擎在等回包，不是已经能在返回之后再改裁决 interchangeable / 已经 later-revise interchangeable / 已经稍后改裁决交差 interchangeable，不是 354 processwhen bundled interchangeable / processwhen-sold-as-later interchangeable。

2. **引擎在等 不是 already left-critical：** 看见引擎在等 / 引擎在等回包 / 在等，不是已经离开关键路径 interchangeable / 已经 left-critical interchangeable / 已经离开关键路径交差 interchangeable，不是 327 preparetimeout interchangeable / 33 fourgates interchangeable。

3. **立刻执行 不是 already full-exec：** 看见立刻执行 / 同步立刻执行 / 立刻调，不是已经是立刻整块执行就已经离开关键路径 interchangeable / 已经 full-exec interchangeable / 已经立刻整块离开关键路径交差 interchangeable，不是 816 async-notreject interchangeable / 817 nonval-notverified interchangeable。

官方把是同步的、不是已经离开关键路径、不是已经是立刻整块执行就已经离开关键路径写成三个名字。把它们叫成一个「看见是同步的就已经能稍后改裁决 interchangeable / 就已经离开关键路径 interchangeable / 就已经是立刻整块执行就已经离开关键路径 interchangeable」，会把 not already later-revise、not already left-critical、not already full-exec 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 调用是同步的不是已经能在返回之后再改裁决 not already later-revise / not already left-critical / not already full-exec 正式三事（354 余量），先数清问的是是同步的 是不是 already later-revise / 354 / processwhen-sold-as-later，是不是引擎在等 是不是 already left-critical，还是立刻执行 是不是 already full-exec，再决定要不要同一次发布。354 processwhen vs later bundled unbundling 在本页 item 1 启动。
