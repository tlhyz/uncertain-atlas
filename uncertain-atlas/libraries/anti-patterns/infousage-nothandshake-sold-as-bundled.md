# 反模式：把 Info Usage Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事（494 余量）说成已经 Info 握手 bundled / 已经 QueryState 启动对齐 / 已经 Info 请求 version 栏

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Info Usage Used to sync during handshake not Info 握手 bundled ≠ bundled（494）](../../tracks/implementation/worked-example-infousage-nothandshake-vs-bundled.md)。

## 卖法

把 Used to sync CometBFT with the application during a handshake that happens on startup or on recovery 写成已经 Info 用来握手对齐 bundled（370）第一二件事 interchangeable / 370 info-handshake bundled interchangeable / 已经 Info 握手 bundled 第一二件事 interchangeable / 已经 Info 用来握手对齐不是已经是快照重放 interchangeable / 668 infousage-notquerystate interchangeable；把 startup or on recovery / 启动或恢复时握手对齐 写成已经 QueryState 启动对齐就是快照重放 interchangeable / 314 querystate interchangeable / 已经 QueryState 就已经是 ExecuteTxState interchangeable / 371 queryheight interchangeable / 320 crash recovery interchangeable；把 during a handshake 写成已经 Info 请求 abci_version 是 ABCI 语义版本 interchangeable / 379 info-req-version interchangeable / 已经 Info 请求 version 栏 interchangeable / 已经 handshake 已经验完 interchangeable / 389 info-lane-fields interchangeable，或已经和 494 infousage-vs-handshakebundled bundled / info-sold-as-handshake interchangeable / 669 infousage-nothandshake interchangeable。

## 为什么错

官方把 Info Usage handshake sync 单句、Info 握手 bundled（370）、QueryState vs ExecuteTxState（314）、Info Request version 栏（379）写成三件独立的实现事。把它们卖成 Info 握手 bundled interchangeable / QueryState 启动对齐 interchangeable / Info 请求 version 栏 interchangeable，会把 not Info 握手 bundled、not QueryState snapshot replay、not Info request version handshake verified 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事（494 余量），必须分开 not Info 握手 bundled、not QueryState snapshot replay、not Info request version handshake verified 三件事，不要和 494 / 370 / 314 / 379 / 389 / 668 / 670 / 665 / 497 糊成一句。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 握手 bundled 三事，不是本页 Methods Info Usage handshake sync 单句边界。
- [infousage-notquerystate-sold-as-bundled](infousage-notquerystate-sold-as-bundled.md) 是 494 item 1 Return state 单句边界，不是本页 item 2 handshake sync 单句边界。
