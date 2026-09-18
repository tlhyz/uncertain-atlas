# 反模式：把候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事（311 余量）说成已经是 ExecuteTxState / 已经能点名本高度最终 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[候选不是已经是 ExecuteTxState ≠ bundled（311）](../../tracks/implementation/worked-example-candidate-notexecute-vs-bundled.md)。

## 卖法

把立刻执行出一份候选 / 跑过了 / Prepare 或 Process 立刻执行了 写成已经是 ExecuteTxState interchangeable / 已经进工作状态 interchangeable / 已经改了 ExecuteTxState interchangeable / 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable；把内存里有状态 / 候选状态留在内存 写成已经能点名本高度最终 interchangeable / 已经 can name this height final interchangeable；把能加快 Finalize / 更快套用内存里那份 写成已经交差 interchangeable / 已经 settled interchangeable，或已经和 311 candidate bundled / candidate-sold-as-execute interchangeable / 693 candidate-notexecute interchangeable。

## 为什么错

官方把立刻执行单句、already ExecuteTxState、already can name this height final、already settled 写成三件独立的实现事。把它们卖成 already ExecuteTxState interchangeable / already can name this height final interchangeable / already settled interchangeable，会把 not already ExecuteTxState、not already can name this height final、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事（311 余量），必须分开 not already ExecuteTxState、not already can name this height final、not already settled 三件事，不要和 311 / 33 / 692 / 694 / 403 / 310 / 5 糊成一句。

## 和相邻反模式

- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选 ≠ ExecuteTxState bundled 全段，不是本页候选 not ExecuteTxState item 2 单句边界。
- [candidate-notheader-sold-as-bundled](candidate-notheader-sold-as-bundled.md) 是 Prepare 没有头哈希 item 1，不是本页立刻执行 ≠ 已经是 ExecuteTxState 边界。
- [finalizeafter-sold-as-commit](finalizeafter-sold-as-commit.md) 是 Finalize 后路径 ≠ 已经 Commit，不是本页能加快 Finalize ≠ 已经交差边界。
