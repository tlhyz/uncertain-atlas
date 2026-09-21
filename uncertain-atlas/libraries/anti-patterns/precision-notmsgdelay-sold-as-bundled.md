# 反模式：把填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事（336 余量）说成已经是 MessageDelay / 已经延迟有界 / 已经 timely

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了 Precision not already message-delay ≠ bundled（336）](../../tracks/implementation/worked-example-precision-notmsgdelay-vs-bundled.md)。

## 卖法

把填了 Precision / `SynchronyParams.Precision` / 钟偏那一栏 写成已经是 MessageDelay interchangeable / 已经 message-delay interchangeable / 已经填了延迟那一栏交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable；把钟偏有界 / 提议者钟偏有界 / 还能出合法提案的钟偏 写成已经延迟有界 interchangeable / 已经 delay-bounded interchangeable；把能出合法提案 / 仍能出合法提案 / 钟偏有界仍能提案 写成已经 timely interchangeable / 已经 timely interchangeable，或已经和 336 precision bundled / precision-sold-as-msgdelay interchangeable / 761 precision-notmsgdelay interchangeable。

## 为什么错

官方把填了 Precision 单句、already message-delay、already delay-bounded、already timely 写成三件独立的实现事。把它们卖成 already message-delay interchangeable / already delay-bounded interchangeable / already timely interchangeable，会把 not already message-delay、not already delay-bounded、not already timely 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事（336 余量），必须分开 not already message-delay、not already delay-bounded、not already timely 三件事，不要和 336 / 40 / 327 / 330 / 762 / 763 糊成一句。

## 和相邻反模式

- [precision-notpbts-sold-as-bundled](precision-notpbts-sold-as-bundled.md) 是填了两个 ≠ 已经启用 PBTS（336 item 2），不是本页填了 Precision item 1 单句边界。
- [precision-sold-as-msgdelay](precision-sold-as-msgdelay.md) 是 Precision bundled 全段，不是本页填了 Precision item 1 单句边界。
- [pbts-sold-as-mtp](pbts-sold-as-mtp.md) 是块时间必须点名算法（40），不是本页填了 Precision ≠ 已经是 MessageDelay 边界。
- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行 ≠ 已经离开关键路径（327），不是本页钟偏有界边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H ≠ 已经 Prepare 带了扩展（330），不是本页能出合法提案边界。
