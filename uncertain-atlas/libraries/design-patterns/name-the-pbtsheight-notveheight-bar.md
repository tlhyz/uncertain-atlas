# 模式：把启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / FeatureParams.PbtsEnableHeight。  
**例**：[启用之后不能关 not already veheight-switch ≠ bundled（343）](../../tracks/implementation/worked-example-pbtsheight-notveheight-vs-bundled.md)。

## 三个名字

1. **启用之后不能关 不是 already veheight-switch：** 看见启用之后不能关 / PBTS 一旦启用就不能关 / 时间戳算法锁死，不是已经是扩展启用高度那种切换 interchangeable / 已经 veheight-switch interchangeable / 已经是到了 H 才叫 ExtendVote 交差 interchangeable，不是 343 pbtsheight bundled interchangeable / 330 veheight interchangeable / pbtsheight-sold-as-enabled interchangeable。

2. **必须比当前高 不是 already can-disable：** 看见不能写成当前高度或更矮 / 必须 `PbtsEnableHeight > [当前高度]` / 必须比当前高，不是已经能关 interchangeable / 已经 can-disable interchangeable / 已经能改回 0 交差 interchangeable，不是 58 enable-height interchangeable / 782 pbtsheight-notzero interchangeable。

3. **字段锁死 不是 already prepare-ext：** 看见字段锁死 / 启用高度锁死 / 不能再改回关掉，不是已经 Prepare 带了扩展 interchangeable / 已经 prepare-ext interchangeable / 已经 Prepare 带扩展交差 interchangeable，不是 veheight-sold-as-prepared interchangeable / 330 veheight interchangeable。

官方把时间戳算法锁死、必须高于当前高度、字段锁死写成三个名字。把它们叫成一个「看见启用之后不能关就已经是扩展启用高度那种切换 interchangeable / 就已经能关 interchangeable / 就已经 Prepare 带了扩展 interchangeable」，会把 not already veheight-switch、not already can-disable、not already prepare-ext 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 余量），先数清问的是启用之后不能关 是不是 already veheight-switch / 343 / pbtsheight-sold-as-enabled，是不是必须比当前高 是不是 already can-disable，还是字段锁死 是不是 already prepare-ext，再决定要不要同一次发布。343 pbtsheight vs params bundled unbundling 在本页 item 3 完成。
