# 模式：把一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事（350 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**例**：[一轮只能交出一份扩展 not already per-height ≠ bundled（350）](../../tracks/implementation/worked-example-extend-notperheight-vs-bundled.md)。

## 三个名字

1. **一轮只能交出一份扩展 不是 already per-height：** 看见正确进程在一轮 *r*、高度 *h* 只能交出一份扩展 / 交了一份 / 交出扩展，不是已经是每一高度一份 interchangeable / 已经 per-height interchangeable / 已经每高一份交差 interchangeable，不是 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable。

2. **又能换一轮 不是 already re-extend-round：** 看见又能换一轮 / 又能进下一轮 / 轮次还能走，不是已经这一轮能再交一份 interchangeable / 已经 re-extend-round interchangeable / 已经本轮再交交差 interchangeable，不是 34 voteext interchangeable / 803 extend-notresign interchangeable。

3. **交出来了 不是 already req6-accept：** 看见交出来了 / 扩展交出来了 / 正确进程交出扩展，不是已经是 348 那种必须被 Verify Accept interchangeable / 已经 req6-accept interchangeable / 已经必须 Accept 交差 interchangeable，不是 348 req6coherence interchangeable / 804 extend-notnil interchangeable。

官方把一轮只能交出一份扩展、不是这一轮已经能再交一份、不是已经是 348 必须 Accept 写成三个名字。把它们叫成一个「看见交了一份就已经是每一高度一份 interchangeable / 就已经能再交一份 interchangeable / 就已经是必须 Accept interchangeable」，会把 not already per-height、not already re-extend-round、not already req6-accept 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事（350 余量），先数清问的是一轮只能交出一份扩展 是不是 already per-height / 350 / extendonce-sold-as-height，是不是又能换一轮 是不是 already re-extend-round，还是交出来了 是不是 already req6-accept，再决定要不要同一次发布。350 extendonce vs round bundled unbundling 在本页 item 3 完成。
