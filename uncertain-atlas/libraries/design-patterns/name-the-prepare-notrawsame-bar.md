# 模式：把两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事（338 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**例**：[两边 raw 一样 not already same-prepared ≠ bundled（338）](../../tracks/implementation/worked-example-prepare-notrawsame-vs-bundled.md)。

## 三个名字

1. **两边 raw 一样 不是 already same-prepared：** 看见两边 raw 提案一样 / *v_p = v_q* / 同一份 raw，不是已经是同一份 prepared 提案 interchangeable / 已经同一份 prepared 交差 interchangeable，不是 338 preparenondet bundled interchangeable / 327 preparetimeout interchangeable / preparenondet-sold-as-deterministic interchangeable。

2. **同一高度同一轮 不是 already must-same-u：** 看见同一高度、同一轮 / 同一高度同一轮 / 同一轮次，不是已经必须同一份 interchangeable / 已经必须同一份交差 interchangeable，不是 33 four gates interchangeable / 338 preparenondet item 1 interchangeable。

3. **诚实准备 不是 already same-list：** 看见诚实准备 / 诚实 Prepare / 正确进程各自 Prepare，不是已经同一份列表 interchangeable / 已经同一份列表交差 interchangeable，不是 347 req3-coherence interchangeable / 338 preparenondet item 3 interchangeable。

官方把两边 raw 一样单句、already same-prepared、already must-same-u、already same-list 写成三个名字。把它们叫成一个「看见两边 raw 一样就已经是同一份提案 interchangeable / 就已经必须同一份 interchangeable / 就已经同一份列表 interchangeable」，会把 not already same-prepared、not already must-same-u、not already same-list 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两边 raw 一样不是已经是同一份提案 not already same-prepared / not already must-same-u / not already same-list 正式三事（338 余量），先数清问的是两边 raw 一样 是不是 already same-prepared / 338 / preparenondet-sold-as-deterministic，是不是同一高度同一轮 是不是 already must-same-u，还是诚实准备 是不是 already same-list，再决定要不要同一次发布。338 preparenondet vs process bundled unbundling 在本页 item 2 续。
