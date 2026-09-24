# 反模式：把优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事（367 余量）说成已经进了块 / 已经从池里删掉 / 已经是共识顺序

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写了 0 not already in-block ≠ bundled（367）](../../tracks/implementation/worked-example-lane-notinblock-vs-bundled.md)。

## 卖法

把写了 0 / 最低优先级是 1、0 留给应用不设道 / 预留 0 写成已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable / 367 lane bundled interchangeable / lane-sold-as-priority interchangeable；把空 `lane_id` / 对应 `ResponseCheckTx` 里空的 `lane_id` / 不设道空 id 写成已经从池里删掉 interchangeable / 已经 removed interchangeable / 已经从池里删掉交差 interchangeable；把有优先级 / 最低是 1、有道就有优先级 / 写了优先级 写成已经是共识顺序 interchangeable / 已经 consensus-order interchangeable / 已经是共识顺序交差 interchangeable，或已经和 367 lane bundled / lane-sold-as-priority interchangeable / 850 lane-notinblock interchangeable。

## 为什么错

官方把写了 0、不是已经从池里删掉、不是已经是共识顺序写成三件独立的实现事。把它们卖成 already in-block interchangeable / already removed interchangeable / already consensus-order interchangeable，会把 not already in-block、not already removed、not already consensus-order 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级 0 留给不设道不是已经进了块 not already in-block / not already removed / not already consensus-order 正式三事（367 余量），必须分开 not already in-block、not already removed、not already consensus-order 三件事，不要和 367 / 301 / 848 / 849 糊成一句。

## 和相邻反模式

- [lane-sold-as-priority](lane-sold-as-priority.md) 是 lane bundled 全段，不是本页写了 0 item 3 单句边界。
- [lane-notpriority-sold-as-bundled](lane-notpriority-sold-as-bundled.md) 是没定义 lane_priorities not already prioritized（367 item 1），不是本页 not already in-block 边界。
- [lane-notalgo-sold-as-bundled](lane-notalgo-sold-as-bundled.md) 是空表对空默认 not already algo（367 item 2），不是本页 not already removed 边界。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了就已经从池里删掉（301），不是本页 not already consensus-order 单句。
