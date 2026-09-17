# 例：看见 Used to sync during a handshake on startup or on recovery is not already Info 握手 bundled（370） interchangeable / QueryState snapshot replay interchangeable / Info request version handshake verified interchangeable

**层次**：实现 / Info Usage Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事（494 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info Usage Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事（494 余量）/ not 669 infousage-nothandshake interchangeable / not 668 infousage-notquerystate interchangeable / not 494 infousage-vs-handshakebundled interchangeable」，不是 Info Usage 正式三事 bundled（494），也不是 Info 用来握手对齐 bundled（370）或 Return information about application state not QueryState（668）。不要另写怎样写 Info、怎样对版本、怎样落盘。

## 官方三件事

规范把 Info Usage 里 Used to sync CometBFT with the application during a handshake that happens on startup or on recovery 和「已经是 Info 用来握手对齐 bundled（370）第一二件事 interchangeable / 已经是 QueryState 启动对齐就是快照重放（314） interchangeable / 已经是 Info 请求 version 栏（379） bundled 就代表 handshake 已经验完 interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 Used to sync during handshake 就已经 Info 握手 bundled interchangeable / 就已经 QueryState 启动对齐 interchangeable / 就已经 Info 请求 version 栏 interchangeable」一件事：

1. **看见 Used to sync CometBFT with the application during a handshake that happens on startup or on recovery / 看见启动或恢复时握手对齐 is not already 已经 Info 用来握手对齐 bundled（370）第一二件事 interchangeable / 370 info-handshake bundled interchangeable / 370 info-handshake item 1 not snapshot replay interchangeable / 370 info-handshake item 2 app_version in Header interchangeable / 已经 Info 握手 bundled 第一二件事 interchangeable / 已经 Info 用来握手对齐不是已经是快照重放 interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 669 infousage-nothandshake interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage item 1 Return state interchangeable / 494 infousage item 3 app_version interchangeable，也不是已经 Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事 bundled（494 item 2 余量） interchangeable / 494 infousage item 2 interchangeable，也不是已经 Return information about application state not handshake sync already persisted bundled（494 item 1 余量 / 668） interchangeable / 497 infousage-persist interchangeable / 665 infousage-notcommitpersist interchangeable。**  
   官方 Usage 写：Used to sync CometBFT with the application during a handshake that happens on startup or on recovery。看见 sync during handshake on startup or on recovery，不是已经 Info 握手 bundled（370）第一二件事 interchangeable——370 钉 bundled 三事，本页从 494 item 2 侧钉 not Info 握手 bundled 单句。看见启动或恢复时握手对齐，不是已经 Info Usage 正式三事 bundled（494） interchangeable——494 钉 bundled 三事，本页钉 Methods Info Usage handshake sync 单句。看见 during a handshake，不是已经 Return information about application state（668/494 item 1） interchangeable——668 另钉 item 1，本页钉 item 2 第一件事。494 infousage vs handshake bundled unbundling 在本页 item 2 续。

2. **看见 Used to sync during a handshake on startup or on recovery / startup or on recovery / 启动或恢复时握手对齐 is not already 已经 QueryState 启动对齐就是快照重放（314） interchangeable / 314 querystate interchangeable / 已经 QueryState 就已经是 ExecuteTxState interchangeable / 已经 Query 可以对当前或过去高度查 interchangeable / 371 queryheight interchangeable / 668 infousage-notquerystate interchangeable / 668 infousage-notquerystate item 1 not QueryState interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 669 infousage-nothandshake interchangeable / 494 infousage item 1 Return state interchangeable / 494 infousage item 3 app_version interchangeable / 320 crash recovery interchangeable，也不是已经 Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事 bundled（494 item 2 余量） interchangeable / 370 info-handshake item 1 not snapshot replay interchangeable / 497 infousage-persist interchangeable，也不是已经 Info 用来握手对齐不是已经是快照重放 interchangeable / 370 info-handshake bundled interchangeable / 389 info-lane-fields interchangeable。**  
   官方把 Usage handshake sync 单句和 QueryState 启动对齐 = 快照重放路径分开——494 bundled 第二件事常与 314 混成「看见 Used to sync during handshake 就已经 QueryState 启动对齐 interchangeable / 就已经 ExecuteTxState interchangeable / 就已经 Query 可以对当前或过去高度查 interchangeable」，本页钉 not QueryState snapshot replay 单句。看见 startup or on recovery，不是已经 QueryState 就已经是 ExecuteTxState interchangeable——314 钉 QueryState vs ExecuteTxState，本页钉 Info Usage sync 语境。看见 sync during handshake，不是已经 Return information about application state not QueryState interchangeable——668 另钉 Return state 路径，本页钉 item 2 第二件事。

3. **看见 Used to sync during a handshake / during a handshake / 启动或恢复时握手对齐 is not already 已经 Info 请求 abci_version 是 ABCI 语义版本（379） bundled 就代表 handshake 已经验完 interchangeable / 379 info-req-version interchangeable / 379 info-req-version item 1 abci_version interchangeable / 已经 Info 请求 version 栏 interchangeable / 已经 Info Request abci_version interchangeable / 389 info-lane-fields item 1 data interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 669 infousage-nothandshake interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage item 3 app_version interchangeable / 494 infousage item 1 Return state interchangeable / 670 infousage-notappversion interchangeable，也不是已经 Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事 bundled（494 item 2 余量） interchangeable / 370 info-handshake bundled interchangeable / 389 info-lane-fields interchangeable / 494 infousage item 3 app_version interchangeable，也不是已经 Info 回包 version 是应用软件语义版本 interchangeable / 389 info-lane-fields item 2 default_lane interchangeable / 663 infousage-notintable interchangeable / 497 infousage-persist interchangeable。**  
   官方把 Usage handshake sync 单句和 Info Request version 栏路径分开——494 bundled 第二件事常与 379 混成「看见 Used to sync during handshake 就已经 Info 请求 version 栏 interchangeable / 就已经 abci_version 是 ABCI 语义版本 interchangeable / 就已经 handshake 已经验完 interchangeable」，本页钉 not Info request version handshake verified 单句。看见 during a handshake，不是已经 Info 请求 abci_version 是 ABCI 语义版本 interchangeable——379 钉 Request 栏，本页钉 Usage sync 语境。看见 startup or on recovery，不是已经 Info 回包 version 是应用软件语义版本 interchangeable——389/670 另钉 Response version / app_version in Header，本页钉 item 2 第三件事。494 infousage vs handshake bundled unbundling 在本页 item 2 续。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。Info Usage 正式三事 bundled（494）、Return information about application state not QueryState（494 item 1 余量 / 668）、app_version included in Header（494 item 3 余量 / 670）、Info 用来握手对齐 bundled（370）、QueryState 就已经是 ExecuteTxState（314）、Info 请求 version 栏（379）、Info 回包 data / version 栏（389）是另外那套，本页不抄。

## 官方为什么这样拆

- **Used to sync during handshake not Info 握手 bundled ≠ 370 info-handshake bundled interchangeable：** 官方把 Methods Info Usage handshake sync 单句和 bundled 370 第一二件事分开。
- **handshake sync not QueryState snapshot replay ≠ 314 querystate interchangeable：** 官方把 Usage handshake sync 单句和 QueryState 启动对齐 = 快照重放路径分开。
- **handshake sync not Info request version handshake verified ≠ 379 info-req-version interchangeable：** 官方把 Usage handshake sync 单句和 Info Request version 栏路径分开；494 infousage vs handshake bundled unbundling 续（669 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Used to sync during handshake | 不是 Info 握手 bundled（370） | 不是 Return state handshake sync = persisted（668/494 item 1） |
| startup or on recovery | 不是 QueryState snapshot replay（314） | 不是 crash recovery already Commit（320） |
| during a handshake | 不是 Info request version verified（379） | 不是 app_version in Header（670/494 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage Used to sync during handshake not Info 握手 bundled / not QueryState snapshot replay / not Info request version handshake verified 正式三事（494 余量），必须分开 Used to sync during handshake 是不是 Info 握手 bundled interchangeable / 370 info-handshake bundled interchangeable / 668 infousage-notquerystate interchangeable / 665 infousage-notcommitpersist interchangeable、startup or on recovery 是不是 QueryState snapshot replay interchangeable / 314 querystate interchangeable / 371 queryheight interchangeable / 320 crash recovery interchangeable、during a handshake 是不是 Info request version handshake verified interchangeable / 379 info-req-version interchangeable / 389 info-lane-fields interchangeable / 670 infousage-notappversion interchangeable。可以跳过「看见 Used to sync during handshake 就已经 Info 握手 bundled interchangeable / 就已经 QueryState 启动对齐 interchangeable / 就已经 Info 请求 version 栏 interchangeable」。不要另写怎样写 Info。494 infousage vs handshake bundled unbundling 在本页 item 2 续。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Info Usage 正式三事 bundled。那是不变量 494。
- Return information about application state not QueryState。那是不变量 494 item 1 余量 / 668。
- app_version included in Header of every block。那是不变量 494 item 3 余量 / 670。
- Info 用来握手对齐 bundled。那是不变量 370。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- Info 请求 version 栏。那是不变量 379。
- Info 回包 data / version 栏。那是不变量 389。
- last_block persisted during Commit。那是不变量 497 item 1 余量 / 665。
