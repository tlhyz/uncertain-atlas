# 例：看见 Return information about the application state is not already QueryState interchangeable / Info response data arbitrary info interchangeable / Used to sync during handshake already persisted interchangeable

**层次**：实现 / Info Usage Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事（494 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info Usage Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事（494 余量）/ not 668 infousage-notquerystate interchangeable / not 494 infousage-vs-handshakebundled interchangeable」，不是 Info Usage 正式三事 bundled（494），也不是 QueryState 就已经是 ExecuteTxState（314）或 Info 用来握手对齐 bundled（370）。不要另写怎样写 Info、怎样对版本、怎样落盘。

## 官方三件事

规范把 Info Usage 里 Return information about the application state 和「已经是 QueryState 就已经是 ExecuteTxState（314） interchangeable / 已经是 Info 回包 data 是任意信息（389） bundled 就代表已经回报状态 interchangeable / 已经是 Used to sync during handshake on startup or on recovery 就等于已经 persisted interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 Return information about application state 就已经 QueryState interchangeable / 就已经 Info data 栏 interchangeable / 就已经 handshake sync 交差 interchangeable」一件事：

1. **看见 Return information about the application state / 看见 Info 用来回报应用状态 is not already 已经 QueryState 就已经是 ExecuteTxState（314） interchangeable / 314 querystate interchangeable / 已经 Query 可以对当前或过去高度查 interchangeable / 已经 QueryState 启动对齐 interchangeable / 已经 ExecuteTxState interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage-vs-handshakebundled interchangeable / 494 infousage item 2 handshake sync interchangeable / 494 infousage item 3 app_version interchangeable，也不是已经 Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事 bundled（494 item 1 余量） interchangeable / 494 infousage item 1 interchangeable，也不是已经 Used to sync during handshake not Info 握手 bundled bundled（494 item 2 余量 / 669） interchangeable / 370 info-handshake bundled interchangeable / 497 infousage-persist interchangeable。**  
   官方 Usage 写：Return information about the application state。看见 return information about application state，不是已经 QueryState 就已经是 ExecuteTxState interchangeable——314 钉 QueryState vs ExecuteTxState，本页从 494 item 1 侧钉 not QueryState 单句。看见回报应用状态，不是已经 Info Usage 正式三事 bundled（494） interchangeable——494 钉 bundled 三事，本页钉 Methods Info Usage Return state 单句。看见能回 Info，不是已经 Used to sync during handshake（494 item 2 余量） interchangeable——669 另钉 item 2，本页钉 item 1 第一件事。494 infousage vs handshake bundled unbundling 在本页 item 1 启动。

2. **看见 Return information about the application state / 回报应用状态 is not already 已经 Info 回包 data 是任意信息（389） bundled 就代表已经回报状态 interchangeable / 389 info-lane-fields interchangeable / 389 info-lane-fields item 1 data interchangeable / 已经 Info Response data 栏 interchangeable / 已经 data 是任意信息 interchangeable / 370 info-handshake bundled interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage item 1 Return state interchangeable / 494 infousage item 3 app_version interchangeable / 497 infousage-persist interchangeable / 666 infousage-notlaneoptional interchangeable，也不是已经 Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事 bundled（494 item 1 余量） interchangeable / 314 querystate interchangeable / 379 info-req-version interchangeable，也不是已经 Info 请求 version 栏（379） bundled interchangeable / 389 info-lane-fields item 2 default_lane interchangeable / 663 infousage-notintable interchangeable。**  
   官方把 Usage Return state 单句和 Info Response data 栏路径分开——494 bundled 第一件事常与 389 混成「看见 Return information about application state 就已经 Info 回包 data 栏 interchangeable / 就已经 data 是任意信息 interchangeable / 就已经回报状态 interchangeable」，本页钉 not Info response data arbitrary info 单句。看见 return information about application state，不是已经 Info 回包 data 是任意信息 interchangeable——389 钉 Response data 栏，本页钉 Usage 回报状态语义。看见能回 Info，不是已经 Info 请求 abci_version 是 ABCI 语义版本（379） interchangeable——379 另钉 Request 栏，本页钉 item 1 第二件事。

3. **看见 Return information about the application state / 看见能回 Info is not already 已经 Used to sync during a handshake on startup or on recovery 就等于已经 persisted interchangeable / 494 infousage item 2 handshake sync interchangeable / 370 info-handshake bundled interchangeable / 370 info-handshake item 1 not snapshot replay interchangeable / 320 crash recovery interchangeable / 481 commitpersist interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 last_block persisted interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage item 3 app_version interchangeable / 494 infousage item 1 Return state interchangeable，也不是已经 Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事 bundled（494 item 1 余量） interchangeable / 314 querystate interchangeable / 389 info-lane-fields interchangeable，也不是已经 Info 用来握手对齐 bundled（370）第一二件事 interchangeable / 669 infousage-nothandshake bundled（494 item 2 余量） interchangeable / 147 apphash-this-block interchangeable。**  
   官方把 Usage Return state 单句和 startup / recovery handshake sync = persisted 路径分开——494 bundled 第一件事常与 370/320 混成「看见 Return information about application state 就已经 handshake sync 交差 interchangeable / 就已经 persisted interchangeable / 就已经 startup or recovery 对齐 interchangeable」，本页钉 not handshake sync already persisted 单句。看见 return information about application state，不是已经 Used to sync during handshake 就等于已经落盘 interchangeable——370 另钉 bundled 握手三事，本页钉 Return state 语境下的 sync≠persisted。看见能回 Info，不是已经 CometBFT expects last_block persisted during Commit interchangeable——665/497 另钉 last_block persist，本页钉 item 1 第三件事。494 infousage vs handshake bundled unbundling 在本页 item 1 启动。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。Info Usage 正式三事 bundled（494）、Used to sync during handshake not Info 握手 bundled（494 item 2 余量 / 669）、app_version included in Header（494 item 3 余量 / 670）、QueryState 就已经是 ExecuteTxState（314）、Info 用来握手对齐 bundled（370）、Info 回包 data / version 栏（389）、Info 请求 version 栏（379）是另外那套，本页不抄。

## 官方为什么这样拆

- **Return information about application state not QueryState ≠ 314 querystate interchangeable：** 官方把 Methods Info Usage Return state 单句和 QueryState vs ExecuteTxState 路径分开。
- **Return state not Info response data arbitrary info ≠ 389 info-lane-fields interchangeable：** 官方把 Usage Return state 单句和 Info Response data 栏路径分开。
- **Return state not handshake sync already persisted ≠ 370 info-handshake bundled interchangeable：** 官方把 Usage Return state 单句和 handshake sync = persisted 路径分开；494 infousage vs handshake bundled unbundling 启动（668 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Return information about application state | 不是 QueryState（314） | 不是 Info response data 栏（389） |
| 回报应用状态 | 不是 Info data 任意信息 | 不是 handshake sync = persisted |
| 能回 Info | 不是 Used to sync during handshake（669/494 item 2） | 不是 app_version in Header（670/494 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage Return information about application state not QueryState / not Info response data arbitrary info / not handshake sync already persisted 正式三事（494 余量），必须分开 Return information about application state 是不是 QueryState interchangeable / 314 querystate interchangeable / 371 queryheight interchangeable、回报应用状态 是不是 Info response data arbitrary info interchangeable / 389 info-lane-fields interchangeable / 379 info-req-version interchangeable、能回 Info 是不是 handshake sync already persisted interchangeable / 370 info-handshake bundled interchangeable / 320 crash recovery interchangeable / 665 infousage-notcommitpersist interchangeable。可以跳过「看见 Return information about application state 就已经 QueryState interchangeable / 就已经 Info data 栏 interchangeable / 就已经 handshake sync 交差 interchangeable」。不要另写怎样写 Info。494 infousage vs handshake bundled unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Info Usage 正式三事 bundled。那是不变量 494。
- Used to sync during handshake not Info 握手 bundled。那是不变量 494 item 2 余量 / 669。
- app_version included in Header of every block。那是不变量 494 item 3 余量 / 670。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- Info 用来握手对齐 bundled。那是不变量 370。
- Info 回包 data / version 栏。那是不变量 389。
- Info 请求 version 栏。那是不变量 379。
- last_block persisted during Commit。那是不变量 497 item 1 余量 / 665。
