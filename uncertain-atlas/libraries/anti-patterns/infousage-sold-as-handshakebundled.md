# 反模式：把 Info Usage 正式三事卖成 QueryState interchangeable / Info 握手 bundled interchangeable / 已经 persist 已经落盘

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Return information about the application state ≠ QueryState](../../tracks/implementation/worked-example-infousage-vs-handshakebundled.md)。

## 卖法

- 「看见 Return information about the application state / Info 用来回报应用状态 就已经 QueryState / ExecuteTxState interchangeable / 已经 Info 回包 data 就代表已经回报状态 / 已经 handshake 就等于已经 persisted。」
- 「看见 Used to sync during a handshake on startup or on recovery / 启动或恢复时握手对齐 就已经 Info 握手 bundled（370）第一二件事 interchangeable / 已经是快照重放 / Info 请求 version 栏 bundled interchangeable。」
- 「看见 The returned app_version will be included in the Header of every block / 回的 app_version 会写进每一块 Header 就已经 last_block_app_hash / last_block_height persisted during Commit interchangeable / 已经 Info 回包 version interchangeable / 已经印进本头 AppHash。」

## 为什么错

官方把 Info Usage 三条核心句写成三件独立的实现事。把它们卖成 QueryState interchangeable / Info 握手 bundled interchangeable / 已经 persist 已经落盘，会把回报状态、handshake sync、app_version 进 Header 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage 正式三事，必须分开 Return information about the application state、Used to sync during handshake on startup or on recovery、app_version included in Header of every block 三个名字，不要把它们卖成 QueryState interchangeable / Info 握手 bundled interchangeable / 已经 persist 已经落盘。

## 和相邻反模式

- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 握手 bundled 三事，不是本页 Info Usage 正式三事专用边界。
- [infousage-persist-sold-as-committed](infousage-persist-sold-as-committed.md) 是 Info Usage last_block persisted during Commit / lane_priorities 正式三事 part 2，不是本页 Info Usage 正式三事 part 1 专用边界。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState 就已经是 ExecuteTxState，不是本页 Return information about application state 专用边界。
