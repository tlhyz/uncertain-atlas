# 模式：把 Info Usage Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事（494 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Info Usage Used to sync during handshake not Info 握手 bundled ≠ bundled（494）](../../tracks/implementation/worked-example-infousage-nothandshake-vs-bundled.md)。

## 三个名字

1. **Used to sync during handshake 不是 Info 握手 bundled：** 看见 Used to sync CometBFT with the application during a handshake that happens on startup or on recovery，不是已经 Info 用来握手对齐 bundled（370）第一二件事 interchangeable，不是 370 info-handshake bundled interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage-vs-handshakebundled interchangeable / 669 infousage-nothandshake interchangeable。

2. **startup or on recovery 不是 QueryState 快照重放：** 看见 startup or on recovery / 启动或恢复时握手对齐，不是已经 QueryState 启动对齐就是快照重放 interchangeable，不是 314 querystate interchangeable / 371 queryheight interchangeable / 668 infousage-notquerystate item 1 interchangeable / 320 crash recovery interchangeable。

3. **during a handshake 不是 Info 请求 version 栏就代表验完：** 看见 during a handshake，不是已经 Info 请求 abci_version 是 ABCI 语义版本 interchangeable / 已经 handshake 已经验完 interchangeable，不是 379 info-req-version interchangeable / 389 info-lane-fields interchangeable / 670 infousage-notappversion interchangeable / 494 infousage item 3 app_version interchangeable。

官方把 Info Usage handshake sync 单句、Info 握手 bundled（370）、QueryState vs ExecuteTxState（314）、Info Request version 栏（379）写成三个名字。把它们叫成一个「看见 Used to sync during handshake 就已经 Info 握手 bundled interchangeable / 就已经 QueryState 启动对齐 interchangeable / 就已经 Info 请求 version 栏 interchangeable」，会把 not Info 握手 bundled、not QueryState snapshot replay、not Info request version handshake verified 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事（494 余量），先数清问的是 Used to sync during handshake 是不是 Info 握手 bundled / 370 / 668 / 665，是不是 startup or on recovery 是不是 QueryState snapshot replay / 314 / 371 / 320，还是 during a handshake 是不是 Info request version verified / 379 / 389 / 670，再决定要不要同一次发布。494 infousage vs handshake bundled unbundling 在本页 item 2 续。
