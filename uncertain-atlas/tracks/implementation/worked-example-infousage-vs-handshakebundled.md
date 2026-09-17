# 例：看见 Return information about the application state 不是已经 QueryState interchangeable；看见 Used to sync during a handshake on startup or on recovery 不是已经 Info 握手 bundled（370）第一二件事 interchangeable；看见 The returned app_version will be included in the Header of every block 不是已经 last_block_app_hash / last_block_height persisted during Commit interchangeable

**层次**：实现 / Info Usage 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Return information about the application state 不是已经 QueryState interchangeable / Used to sync during handshake on startup or on recovery 不是已经 Info 握手 bundled interchangeable / app_version included in Header of every block 不是已经 last_block persisted during Commit interchangeable」，不是 Info 用来握手对齐 bundled 三事（370），也不是 Info 请求 version 栏（379）或 Info 回包 data / version 栏（389）。不要另写怎样写 Info、怎样对版本、怎样落盘。

## 官方三件事

规范把 Info Usage 前三条核心英文句写成三件独立的实现事，不是「看见能回 Info 就已经 QueryState、已经握手 bundled 交差、已经 persist 已经落盘」一件事：

1. **看见 Return information about the application state / 看见 Info 用来回报应用状态 不是已经 QueryState 就已经是 ExecuteTxState（314） interchangeable，也不是已经 Info 回包 data 是任意信息（389） bundled 就代表已经回报状态 interchangeable，也不是已经 Used to sync during handshake 就等于已经 persisted interchangeable。**  
   官方 Usage 写：Return information about the application state。看见 return information about application state，不是已经 Query 可以对当前或过去高度查（371）那种 QueryState interchangeable——371 钉 Query height 栏，本页钉 Methods Info Usage 回报状态单句。看见回报应用状态，不是已经 Info 回包 data 是任意信息 interchangeable——389 钉 Response data 栏，本页钉 Usage 回报状态语义。看见能回 Info，不是已经 startup / recovery handshake 就等于已经落盘 interchangeable。
2. **看见 Used to sync CometBFT with the application during a handshake that happens on startup or on recovery / 看见启动或恢复时握手对齐 不是已经 Info 用来握手对齐 bundled（370）第一二件事 interchangeable，也不是已经 QueryState 启动对齐就是快照重放（314） interchangeable，也不是已经 Info 请求 version 栏（379） bundled 就代表 handshake 已经验完 interchangeable。**  
   官方 Usage 写：Used to sync CometBFT with the application during a handshake that happens on startup or on recovery。看见 sync during handshake on startup or on recovery，不是已经 Info 用来握手对齐不是已经是快照重放（370 bundled 第一件事） interchangeable——370 钉 Info 握手 bundled 三事，本页钉 Methods Info Usage handshake 单句。看见 startup or on recovery，不是已经 QueryState 启动对齐 interchangeable——314 钉 QueryState vs ExecuteTxState，本页钉 Info Usage sync 语境。看见 during a handshake，不是已经 Info 请求 abci_version 是 ABCI 语义版本（379） bundled 就代表已经握手对齐 interchangeable。
3. **看见 The returned `app_version` will be included in the Header of every block / 看见回的 app_version 会写进每一块 Header 不是已经 Info 握手 bundled（370）第三件事 last_block persisted during Commit interchangeable，也不是已经 Info 回包 version 是应用软件语义版本（389） interchangeable，也不是已经印进本头 AppHash（147） interchangeable。**  
   官方 Usage 写：The returned `app_version` will be included in the Header of every block。看见 included in Header of every block，不是已经 CometBFT expects last_block_app_hash and last_block_height updated and persisted during Commit（370 bundled 第三件事） interchangeable——370 钉 last_block 要在 Commit 落盘，本页钉 app_version 进 Header 单句。看见 returned app_version，不是已经 Info 回包 version 是应用软件语义版本 interchangeable——389 钉 Response version 栏，本页钉 Usage app_version 进 Header。看见会写进 Header，不是已经本头 AppHash 就已经是本高度交差（147） interchangeable。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。Info 用来握手对齐 bundled（370）、Info 请求 version 栏（379）、Info 回包 data / version 栏（389）、QueryState 就已经是 ExecuteTxState（314）、没定义 lane_priorities 就已经排了优先（367）是另外那套，本页不抄。

## 官方为什么这样拆

- **Return information about the application state ≠ QueryState interchangeable：** 官方把 Info 回报状态和 QueryState 分开。
- **Used to sync during handshake on startup or on recovery ≠ Info 握手 bundled interchangeable：** 官方把 Usage handshake 单句和 bundled 370 三事分开。
- **app_version included in Header of every block ≠ last_block persisted during Commit interchangeable：** 官方把 app_version 进 Header 和 last_block 要在 Commit 落盘分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Return information about the application state | 不是 QueryState interchangeable | 不是 Info 回包 data 栏（389） |
| Used to sync during handshake on startup or on recovery | 不是 Info 握手 bundled（370） | 不是 QueryState 启动对齐（314） |
| app_version included in Header of every block | 不是 last_block persisted during Commit | 不是本头 AppHash 就已经交差（147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage 正式三事，必须分开 Return information about the application state 是不是 QueryState interchangeable / 已经 persisted、Used to sync during handshake on startup or on recovery 是不是 Info 握手 bundled interchangeable / 已经快照重放、app_version included in Header of every block 是不是 last_block persisted during Commit interchangeable / 已经印进本头 AppHash。可以跳过「看见能回 Info 就已经 QueryState、已经握手 bundled 交差」。不要另写怎样写 Info。494 infousage vs handshake bundled unbundling 在本页 item 1 启动；精读 [`worked-example-infousage-notquerystate-vs-bundled.md`](worked-example-infousage-notquerystate-vs-bundled.md)（不变量 668 item 1）；续 [`worked-example-infousage-nothandshake-vs-bundled.md`](worked-example-infousage-nothandshake-vs-bundled.md)（不变量 669 item 2）；续 app_version included in Header（670 item 3 余量）。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Info 用来握手对齐 bundled。那是不变量 370。
- Info 请求 version 栏。那是不变量 379。
- Info 回包 data / version 栏。那是不变量 389。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
