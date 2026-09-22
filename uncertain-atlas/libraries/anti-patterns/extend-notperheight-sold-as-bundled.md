# 反模式：把一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事（350 余量）说成已经是每一高度一份 / 已经这一轮能再交一份 / 已经是 348 必须 Accept

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[一轮只能交出一份扩展 not already per-height ≠ bundled（350）](../../tracks/implementation/worked-example-extend-notperheight-vs-bundled.md)。

## 卖法

把正确进程在一轮 *r*、高度 *h* 只能交出一份扩展 / 交了一份 / 交出扩展 写成已经是每一高度一份 interchangeable / 已经 per-height interchangeable / 已经每高一份交差 interchangeable / 350 extendonce bundled interchangeable / extendonce-sold-as-height interchangeable；把又能换一轮 / 又能进下一轮 写成已经这一轮能再交一份 interchangeable / 已经 re-extend-round interchangeable / 已经本轮再交交差 interchangeable；把交出来了 / 扩展交出来了 写成已经是 348 那种必须被 Verify Accept interchangeable / 已经 req6-accept interchangeable / 已经必须 Accept 交差 interchangeable，或已经和 350 extendonce bundled / extendonce-sold-as-height interchangeable / 805 extend-notperheight interchangeable。

## 为什么错

官方把一轮只能交出一份扩展、不是这一轮已经能再交一份、不是已经是 348 必须 Accept 写成三件独立的实现事。把它们卖成 already per-height interchangeable / already re-extend-round interchangeable / already req6-accept interchangeable，会把 not already per-height、not already re-extend-round、not already req6-accept 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一轮只能交出一份扩展不是已经是每一高度一份 not already per-height / not already re-extend-round / not already req6-accept 正式三事（350 余量），必须分开 not already per-height、not already re-extend-round、not already req6-accept 三件事，不要和 350 / 348 / 34 / 803 / 804 糊成一句。

## 和相邻反模式

- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮一份扩展 bundled 全段，不是本页一轮只能交出一份扩展 item 3 单句边界。
- [extend-notresign-sold-as-bundled](extend-notresign-sold-as-bundled.md) 是一轮最多一张 Precommit not already resign（350 item 1），不是本页 not already per-height 边界。
- [extend-notnil-sold-as-bundled](extend-notnil-sold-as-bundled.md) 是 ExtendVote 非 nil 才叫 not already signed-nil（350 item 2），不是本页 not already per-height 边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept（348），不是本页 not already req6-accept 单句边界。
