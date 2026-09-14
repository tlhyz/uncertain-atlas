# 例：看见 Info 用来回应用状态信息 / Return information about the application state is not already handshake aligned / not finfields bundled（407） interchangeable / not Info Usage bundled（494） interchangeable

**层次**：实现 / Info 用来回应用状态信息 not handshake 正式三事（407 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage / FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info 用来回应用状态信息 not handshake / not finfields bundled（407） interchangeable / not Info Usage bundled（494） interchangeable」，不是 Info 用来握手对齐 bundled（370），也不是 Info Usage 正式三事（494），也不是 Finalize 字段余量 bundled（407）。不要另写怎样回 Info。

## 官方三件事

规范把 Info Usage 里回报应用状态信息 和「已经是启动或恢复时握手对齐 / 已经是 QueryState / 已经是 finfields bundled interchangeable」分开写成三件独立的实现事，不是「看见能回 Info 就已经握手对齐 interchangeable、已经快照重放 interchangeable、已经 finfields bundled interchangeable」一件事：

1. **看见 Info 用来回应用状态信息 / 看见 Return information about the application state is not already Used to sync during a handshake on startup or on recovery interchangeable / 看见能回 is not already Info 用来握手对齐 bundled（370 余量） interchangeable / 已经握手对齐 interchangeable / 已经快照重放 interchangeable，也不是已经 Info Usage 正式三事 bundled（494 余量） interchangeable / 已经 Used to sync during handshake interchangeable / 已经 QueryState interchangeable，也不是已经 Info 回包 data 是任意信息 bundled（389 余量） interchangeable / 已经回报状态 interchangeable / 已经 persisted interchangeable，也不是已经 Finalize 字段余量 not already settled bundled（573 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 ran Process interchangeable，也不是已经 Finalize 实现必须确定 not like Prepare bundled（574 余量） interchangeable / 已经像 Prepare 那样 interchangeable / 已经 findet bundled interchangeable。**  
   官方 Info Usage 写：Return information about the application state。看见能回应用状态信息，不是已经 Used to sync CometBFT with the application during a handshake that happens on startup or on recovery（370 bundled 第一件事） interchangeable——370 钉 Info 握手 bundled 三事，本页钉 407 item 3 单句。看见回报应用状态，不是已经 Info Usage 正式三事（494） interchangeable——494 钉 Return information / Used to sync / app_version in Header 三事，本页钉 407 Info 回应用状态信息 单句。看见能回 Info，不是已经 finfields bundled（407） interchangeable——407 bundled 第三件事常被写成「看见能回就已经握手对齐」，本页钉 Info 用来回应用状态信息 单句。
2. **看见 Info 用来回应用状态信息 is not already QueryState / ExecuteTxState interchangeable / 看见能回 is not already QueryState 启动对齐就是快照重放 bundled（314 余量） interchangeable / 已经 QueryState interchangeable / 已经 ExecuteTxState interchangeable，也不是已经 Info Usage Return information about the application state bundled（494 第一件事） interchangeable / 已经 persisted interchangeable / 已经 handshake 就等于 persisted interchangeable，也不是已经 Query 可以对当前或过去高度查 bundled（371 余量） interchangeable / 已经 height 默认 0 interchangeable / 已经 QueryState interchangeable，也不是已经 Info 回包 data 是任意信息 bundled（389 余量） interchangeable / 已经握手对齐 interchangeable / 已经快照重放 interchangeable，也不是已经 last_block persisted during Commit bundled（497 余量） interchangeable / 已经 Commit 交差 interchangeable / 已经 Info 握手 bundled interchangeable。**  
   官方把 Info 回报应用状态信息和 QueryState / 启动对齐分开——407 bundled 常与 314 混成「看见能回 Info 就已经 QueryState / 快照重放 interchangeable」，本页钉 Info 用来回应用状态信息 not QueryState 单句。看见 Return information about the application state，不是已经 QueryState 就已经是 ExecuteTxState（314） interchangeable——314 钉 Query 连接 vs ExecuteTxState，本页钉 407 item 3 边界。看见能回信息，不是已经 Info Usage Return information（494 第一件事） interchangeable——494 钉 Usage 三事，本页钉 407 Info 单句。
3. **看见 Info 用来回应用状态信息 is not already app_version included in Header / last_block persisted during Commit interchangeable / 看见能回 is not already Info Usage 正式三事 bundled（494 余量） interchangeable / 已经 app_version in Header interchangeable / 已经 last_block persisted interchangeable，也不是已经 Info 用来握手对齐 bundled（370 余量） interchangeable / 已经 app_version 进每块头 interchangeable / 已经 last_block 要在 Commit 落盘 interchangeable，也不是已经 Info 回包 version 是应用软件语义版本 bundled（389 余量） interchangeable / 已经 app_version interchangeable / 已经印进本头 AppHash interchangeable，也不是已经 Finalize 含刚决定那块的字段 not already settled bundled（573 余量） interchangeable / 已经四门已经结算 interchangeable / 已经 Contains bundled interchangeable，也不是已经 Finalize 实现必须确定 not like Prepare bundled（574 余量） interchangeable / 已经 state machine replication interchangeable / 已经 findet bundled interchangeable。**  
   官方把 Info 回报应用状态信息 和 app_version 进 Header / last_block 要在 Commit 落盘 bundled 分开——407 bundled 常与 494 / 370 混成「看见能回就已经 persist / 已经印进本头 interchangeable」，本页钉 Info 用来回应用状态信息 not Info Usage bundled item 2/3 单句。看见 Return information，不是已经 app_version included in Header of every block（494 第三件事） interchangeable——494 钉 app_version 进 Header，本页钉 407 Info 单句。看见能回应用状态，不是已经 last_block persisted during Commit（370 bundled 第三件事 / 497 余量） interchangeable——370 / 497 钉 Commit 落盘，本页钉 407 item 3 边界。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。Info 用来握手对齐 bundled（370）、Info Usage 正式三事（494）、Finalize 含刚决定那块的字段 not settled（573 余量）、Finalize 实现必须确定 not like Prepare（574 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **Info 用来回应用状态信息 ≠ handshake aligned interchangeable：** 官方把回报应用状态信息和启动或恢复时握手对齐分开。
- **Info 用来回应用状态信息 ≠ QueryState / snapshot replay interchangeable：** 官方把 Info 回报状态和 QueryState 启动对齐分开。
- **Info 用来回应用状态信息 ≠ Info Usage bundled item 2/3 interchangeable：** 官方把回报应用状态信息和 app_version 进 Header / last_block 落盘 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 用来回应用状态信息 | 不是 already handshake aligned | 不是 Info 用来握手对齐 bundled（370） |
| Info 用来回应用状态信息 | 不是 already QueryState | 不是 QueryState 启动对齐（314） |
| Info 用来回应用状态信息 | 不是 already Info Usage bundled | 不是 Info Usage 正式三事（494） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 用来回应用状态信息 not handshake 正式三事（407 余量），必须分开 Info 用来回应用状态信息 是不是 already handshake aligned interchangeable / 407 bundled interchangeable / 370 bundled interchangeable、Info 用来回应用状态信息 是不是 already QueryState interchangeable / 314 snapshot replay interchangeable / 494 Return information interchangeable、Info 用来回应用状态信息 是不是 already Info Usage bundled item 2/3 interchangeable / 494 app_version in Header interchangeable / 370 last_block persisted interchangeable。可以跳过「看见能回 Info 就已经握手对齐 interchangeable」。不要另写怎样回 Info。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Finalize 含刚决定那块的字段 not already settled。那是不变量 573（407 item 1 余量）。
- Finalize 实现必须确定 not like Prepare。那是不变量 574（407 item 2 余量）。
- Info 用来握手对齐 bundled。那是不变量 370。
- Info Usage 正式三事。那是不变量 494。
