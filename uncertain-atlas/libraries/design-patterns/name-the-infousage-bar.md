# 模式：把 Info Usage 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[Return information about the application state ≠ QueryState](../../tracks/implementation/worked-example-infousage-vs-handshakebundled.md)。

## 三个名字

1. **Return information about the application state 不是 QueryState interchangeable：** 看见 Methods Info Usage 回报状态，不是 QueryState / Info 回包 data interchangeable。
2. **Used to sync during handshake on startup or on recovery 不是 Info 握手 bundled interchangeable：** 看见 startup / recovery handshake，不是 bundled 370 / 已经快照重放 interchangeable。
3. **app_version included in Header of every block 不是 last_block persisted during Commit interchangeable：** 看见 app_version 进 Header，不是 last_block 落盘 / 本头 AppHash interchangeable。

## 为什么要分开叫

官方把 Info Usage 三条核心句、Info 握手 bundled（370）、Info 请求 version 栏（379）、Info 回包 data / version 栏（389）写成三个名字。把它们叫成一个「看见能回 Info 就已经 QueryState、已经握手 bundled 交差、已经 persist 已经落盘」，会把回报状态、handshake sync、app_version 进 Header 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage 正式三事，先数清问的是 Return information about the application state 是不是 QueryState interchangeable / 已经 persisted、Used to sync during handshake on startup or on recovery 是不是 Info 握手 bundled interchangeable / 已经快照重放、app_version included in Header of every block 是不是 last_block persisted during Commit interchangeable / 已经印进本头 AppHash，再决定要不要同一次发布。
