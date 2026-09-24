# 反模式：把空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事（367 余量）说成已经选型 / 已经排了优先 / 已经进了块

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[空对空 not already algo ≠ bundled（367）](../../tracks/implementation/worked-example-lane-notalgo-vs-bundled.md)。

## 卖法

把空对空 / `lane_priorities` 空当且仅当 `default_lane` 空 / 空表对空默认 写成已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable / 367 lane bundled interchangeable / lane-sold-as-priority interchangeable；把默认道在表里 / `default_lane` 必须是 `lane_priorities` 里定义过的一个标识 / 默认道是表里标识 写成已经排了优先 interchangeable / 已经 prioritized interchangeable / 已经排了优先交差 interchangeable；把对上了 / 空对空且默认道在表里 / 约束对上 写成已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable，或已经和 367 lane bundled / lane-sold-as-priority interchangeable / 849 lane-notalgo interchangeable。

## 为什么错

官方把空对空、不是已经排了优先、不是已经进了块写成三件独立的实现事。把它们卖成 already algo interchangeable / already prioritized interchangeable / already in-block interchangeable，会把 not already algo、not already prioritized、not already in-block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空表对空默认不是已经选型 not already algo / not already prioritized / not already in-block 正式三事（367 余量），必须分开 not already algo、not already prioritized、not already in-block 三件事，不要和 367 / 312 / 848 / 850 糊成一句。

## 和相邻反模式

- [lane-sold-as-priority](lane-sold-as-priority.md) 是 lane bundled 全段，不是本页空对空 item 2 单句边界。
- [lane-notpriority-sold-as-bundled](lane-notpriority-sold-as-bundled.md) 是没定义 lane_priorities not already prioritized（367 item 1），不是本页 not already algo 边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState 就已经是 ExecuteTxState（312），不是本页 not already prioritized 单句。
- [infousage-notemptyiff-sold-as-bundled](infousage-notemptyiff-sold-as-bundled.md) 是 empty iff vs Info lane bundled（667），不是本页 not already in-block 边界。
