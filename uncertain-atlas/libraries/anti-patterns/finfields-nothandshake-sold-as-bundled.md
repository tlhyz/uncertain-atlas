# 反模式：把 Info 用来回应用状态信息 not handshake 正式三事（407 余量）卖成 finfields bundled / 已经握手对齐 / Info Usage bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info 用来回应用状态信息 not handshake ≠ bundled（407）](../../tracks/implementation/worked-example-finfields-nothandshake-vs-bundled.md)。

## 卖法

- 「看见 Info 用来回应用状态信息 / 看见能回 Info 就已经启动或恢复时握手对齐 interchangeable / 已经快照重放 interchangeable。」
- 「看见能回 Info 就已经 QueryState interchangeable / 已经 ExecuteTxState interchangeable / 已经 persisted interchangeable。」
- 「看见能回 Info 就已经 app_version in Header interchangeable / 已经 last_block persisted interchangeable / 已经 finfields bundled interchangeable。」

## 为什么错

官方把 Info 回报应用状态信息、启动或恢复时握手对齐、QueryState 启动对齐、Info Usage 三句 bundled 写成独立的实现事。把它们卖成 finfields bundled、已经握手对齐、Info Usage bundled，会把 not handshake、not QueryState、not Info Usage bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 用来回应用状态信息 not handshake 正式三事（407 余量），必须分开 not handshake、not QueryState、not Info Usage bundled 三个名字，不要把它们卖成 finfields bundled / 已经握手对齐 / Info Usage bundled。

## 和相邻反模式

- [finfields-sold-as-equiv](finfields-sold-as-equiv.md) 是 407 bundled 三事专用，不是本页 Info 回应用状态信息 单句边界。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 370 Info 握手 bundled 专用，不是本页 407 item 3 余量边界。
- [infousage-sold-as-handshakebundled](infousage-sold-as-handshakebundled.md) 是 494 Info Usage 正式三事专用，不是本页 407 Info 单句边界。
