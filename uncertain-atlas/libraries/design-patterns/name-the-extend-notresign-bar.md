# 模式：把一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事（350 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Requirement 6 之前。  
**例**：[一轮最多一张 Precommit not already resign ≠ bundled（350）](../../tracks/implementation/worked-example-extend-notresign-vs-bundled.md)。

## 三个名字

1. **一轮最多一张 Precommit 不是 already resign：** 看见正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit / 到了 Precommit 步 / 到了这一步，不是已经能再签一张 interchangeable / 已经 resign interchangeable / 已经再签交差 interchangeable，不是 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable。

2. **有一张票 不是 already is-extension：** 看见有一张票 / 广播了一张 Precommit / 这一轮有票，不是已经是扩展本身 interchangeable / 已经 is-extension interchangeable / 已经票即扩展交差 interchangeable，不是 34 voteext interchangeable / 338 preparenondet interchangeable。

3. **还能换轮 不是 already re-emit：** 看见还能换轮 / 又能进下一轮 / 轮次还能走，不是已经这一轮能再出一张 interchangeable / 已经 re-emit interchangeable / 已经本轮再出交差 interchangeable，不是 804 extend-notnil interchangeable / 805 extend-notperheight interchangeable。

官方把一轮最多一张 Precommit、不是已经是扩展本身、不是这一轮已经能再出一张写成三个名字。把它们叫成一个「看见到了 Precommit 就已经能再签一张 interchangeable / 就已经是扩展 interchangeable / 就已经能再出一张 interchangeable」，会把 not already resign、not already is-extension、not already re-emit 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事（350 余量），先数清问的是一轮最多一张 Precommit 是不是 already resign / 350 / extendonce-sold-as-height，是不是有一张票 是不是 already is-extension，还是还能换轮 是不是 already re-emit，再决定要不要同一次发布。350 extendonce vs round bundled unbundling 在本页 item 1 启动。
