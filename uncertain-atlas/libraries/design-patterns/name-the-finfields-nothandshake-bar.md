# 模式：把 Info 用来回应用状态信息 not handshake 正式三事（407 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage / FinalizeBlock Usage。  
**例**：[Info 用来回应用状态信息 not handshake ≠ bundled（407）](../../tracks/implementation/worked-example-finfields-nothandshake-vs-bundled.md)。

## 三个名字

1. **Info 用来回应用状态信息 不是 handshake aligned：** 看见能回不是已经启动或恢复时握手对齐，不是 407 bundled interchangeable / 370 bundled interchangeable / 494 Used to sync interchangeable。
2. **Info 用来回应用状态信息 不是 QueryState：** 看见能回不是已经 QueryState / 快照重放，不是 314 QueryState interchangeable / 494 Return information interchangeable。
3. **Info 用来回应用状态信息 不是 Info Usage bundled item 2/3：** 看见能回不是已经 app_version in Header / last_block persisted，不是 494 Info Usage interchangeable / 370 last_block persisted interchangeable / 573 not settled interchangeable。

## 为什么要分开叫

官方把 Info 用来回应用状态信息写成三个名字。把它们叫成一个「看见能回 Info 就已经握手对齐 interchangeable / 已经 QueryState interchangeable / 已经 finfields bundled interchangeable」，会把 not handshake、not QueryState、not Info Usage bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 用来回应用状态信息 not handshake 正式三事（407 余量），先数清问的是 Info 用来回应用状态信息 是不是 already handshake aligned、是不是 already QueryState、是不是 already Info Usage bundled item 2/3，再决定要不要同一次发布。
