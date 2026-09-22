# 反模式：把一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事（350 余量）说成已经能再签一张 / 已经是扩展本身 / 已经这一轮能再出一张

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[一轮最多一张 Precommit not already resign ≠ bundled（350）](../../tracks/implementation/worked-example-extend-notresign-vs-bundled.md)。

## 卖法

把正确进程在一轮 *r*、高度 *h* 最多广播一张 Precommit / 到了 Precommit 步 / 到了这一步 写成已经能再签一张 interchangeable / 已经 resign interchangeable / 已经再签交差 interchangeable / 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable；把有一张票 / 广播了一张 Precommit 写成已经是扩展本身 interchangeable / 已经 is-extension interchangeable / 已经票即扩展交差 interchangeable；把还能换轮 / 又能进下一轮 写成已经这一轮能再出一张 interchangeable / 已经 re-emit interchangeable / 已经本轮再出交差 interchangeable，或已经和 350 extendonce bundled / extendonce-sold-as-height interchangeable / 803 extend-notresign interchangeable。

## 为什么错

官方把一轮最多一张 Precommit、不是已经是扩展本身、不是这一轮已经能再出一张写成三件独立的实现事。把它们卖成 already resign interchangeable / already is-extension interchangeable / already re-emit interchangeable，会把 not already resign、not already is-extension、not already re-emit 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮最多一张 Precommit 不是已经能再签一张 not already resign / not already is-extension / not already re-emit 正式三事（350 余量），必须分开 not already resign、not already is-extension、not already re-emit 三件事，不要和 350 / 34 / 338 / 804 / 805 糊成一句。

## 和相邻反模式

- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮一份扩展 bundled 全段，不是本页一轮最多一张 Precommit item 1 单句边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交就已经是块非法（34），不是本页 not already resign 边界。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是同一块不是已经是同一份扩展（338），不是本页 not already is-extension 边界。
