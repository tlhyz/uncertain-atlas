# 反模式：把 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事（370 余量）说成已经是快照重放 / 已经是 QueryState / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[能回 not already statesync ≠ bundled（370）](../../tracks/implementation/worked-example-info-notstatesync-vs-bundled.md)。

## 卖法

把能回 / Info 用来在启动或恢复时让引擎和应用握手对齐 / 能回 Info 写成已经是快照重放 interchangeable / 已经 statesync interchangeable / 已经是快照重放交差 interchangeable / 370 info bundled interchangeable / info-sold-as-handshake interchangeable；把握手了 / 启动或恢复时用这次握手和应用对齐 / 握过手 写成已经是 QueryState interchangeable / 已经 querystate interchangeable / 已经是 QueryState 交差 interchangeable；把对齐了 / 和应用对齐 / 对齐过 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 370 info bundled / info-sold-as-handshake interchangeable / 857 info-notstatesync interchangeable。

## 为什么错

官方把能回、不是已经是 QueryState、不是已经交差写成三件独立的实现事。把它们卖成 already statesync interchangeable / already querystate interchangeable / already settled interchangeable，会把 not already statesync、not already querystate、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事（370 余量），必须分开 not already statesync、not already querystate、not already settled 三件事，不要和 370 / 38 / 314 / 858 / 859 糊成一句。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 info bundled 全段，不是本页能回 item 1 单句边界。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState 就已经是 ExecuteTxState（314），不是本页 not already querystate 单句边界。
- [statesync-sold-as-genesis](statesync-sold-as-genesis.md) 是应用快照就已经从创世重放（38），不是本页 not already statesync 边界。
