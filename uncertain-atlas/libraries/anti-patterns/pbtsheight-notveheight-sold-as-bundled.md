# 反模式：把启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 余量）说成已经是扩展启用高度那种切换 / 已经能关 / 已经 Prepare 带了扩展

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[启用之后不能关 not already veheight-switch ≠ bundled（343）](../../tracks/implementation/worked-example-pbtsheight-notveheight-vs-bundled.md)。

## 卖法

把启用之后不能关 / PBTS 一旦启用就不能关 / 时间戳算法锁死 写成已经是扩展启用高度那种切换 interchangeable / 已经 veheight-switch interchangeable / 已经是到了 H 才叫 ExtendVote 交差 interchangeable / 343 pbtsheight bundled interchangeable / pbtsheight-sold-as-enabled interchangeable；把不能写成当前高度或更矮 / 必须比当前高 写成已经能关 interchangeable / 已经 can-disable interchangeable / 已经能改回 0 交差 interchangeable；把字段锁死 / 启用高度锁死 写成已经 Prepare 带了扩展 interchangeable / 已经 prepare-ext interchangeable / 已经 Prepare 带扩展交差 interchangeable，或已经和 343 pbtsheight bundled / pbtsheight-sold-as-enabled interchangeable / 784 pbtsheight-notveheight interchangeable。

## 为什么错

官方把时间戳算法锁死、必须高于当前高度、字段锁死写成三件独立的实现事。把它们卖成 already veheight-switch interchangeable / already can-disable interchangeable / already prepare-ext interchangeable，会把 not already veheight-switch、not already can-disable、not already prepare-ext 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启用之后不能关不是已经是扩展启用高度那种切换 not already veheight-switch / not already can-disable / not already prepare-ext 正式三事（343 余量），必须分开 not already veheight-switch、not already can-disable、not already prepare-ext 三件事，不要和 343 / 330 / 58 / 782 / 783 糊成一句。

## 和相邻反模式

- [pbtsheight-notzero-sold-as-bundled](pbtsheight-notzero-sold-as-bundled.md) 是写成 0 ≠ 已启用（343 item 1），不是本页启用之后不能关 item 3 单句边界。
- [pbtsheight-notbfttime-sold-as-bundled](pbtsheight-notbfttime-sold-as-bundled.md) 是 H 之前仍用 BFT Time ≠ 已切 PBTS（343 item 2），不是本页 item 3 单句边界。
- [pbtsheight-sold-as-enabled](pbtsheight-sold-as-enabled.md) 是 PbtsEnableHeight bundled 全段，不是本页 item 3 单句边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 不是已经 Prepare 带了扩展（330），不是本页不能关 ≠ 扩展启用高度那种切换 边界。
