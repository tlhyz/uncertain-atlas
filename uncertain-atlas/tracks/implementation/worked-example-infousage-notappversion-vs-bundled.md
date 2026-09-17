# 例：看见 The returned app_version will be included in the Header of every block is not already last_block persisted during Commit interchangeable / Info response version interchangeable / AppHash in header interchangeable

**层次**：实现 / Info Usage app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事（494 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info Usage app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事（494 余量）/ not 670 infousage-notappversion interchangeable / not 669 infousage-nothandshake interchangeable / not 494 infousage-vs-handshakebundled interchangeable」，不是 Info Usage 正式三事 bundled（494），也不是 Info 用来握手对齐 bundled（370）或 Return information about application state not QueryState（668）。不要另写怎样写 Info、怎样对版本、怎样落盘。

## 官方三件事

规范把 Info Usage 里 The returned `app_version` will be included in the Header of every block 和「已经是 Info 握手 bundled（370）第三件事 last_block persisted during Commit interchangeable / 已经是 Info 回包 version 是应用软件语义版本（389） interchangeable / 已经是印进本头 AppHash（147） interchangeable / 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 app_version included in Header 就已经 last_block persisted interchangeable / 就已经 Info version 栏 interchangeable / 就已经印进 AppHash interchangeable」一件事：

1. **看见 The returned `app_version` will be included in the Header of every block / 看见回的 app_version 会写进每一块 Header is not already 已经 Info 握手 bundled（370）第三件事 last_block persisted during Commit interchangeable / 370 info-handshake bundled interchangeable / 370 info-handshake item 3 last_block persisted interchangeable / 370 info-handshake item 2 app_version in Header interchangeable / 已经 Info 握手 bundled 第三件事 interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 last_block persisted interchangeable / 481 commitpersist interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 670 infousage-notappversion interchangeable / 669 infousage-nothandshake interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage item 1 Return state interchangeable / 494 infousage item 2 handshake sync interchangeable，也不是已经 app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事 bundled（494 item 3 余量） interchangeable / 494 infousage item 3 interchangeable，也不是已经 Used to sync during handshake not Info 握手 bundled bundled（494 item 2 余量 / 669） interchangeable / 320 crash recovery interchangeable / 587 finreturn interchangeable。**  
   官方 Usage 写：The returned `app_version` will be included in the Header of every block。看见 included in Header of every block，不是已经 Info 握手 bundled（370）第三件事 last_block persisted interchangeable——370 钉 bundled 第三件事，本页从 494 item 3 侧钉 not last_block persisted 单句。看见 returned app_version，不是已经 Info Usage 正式三事 bundled（494） interchangeable——494 钉 bundled 三事，本页钉 Methods Info Usage app_version in Header 单句。看见会写进 Header，不是已经 Used to sync during handshake（669/494 item 2） interchangeable——669 另钉 item 2，本页钉 item 3 第一件事。494 infousage vs handshake bundled unbundling 在本页 item 3 完成。

2. **看见 returned app_version / app_version included in Header / 会写进每一块 Header is not already 已经 Info 回包 version 是应用软件语义版本（389） interchangeable / 389 info-lane-fields interchangeable / 389 info-lane-fields item 2 default_lane interchangeable / 389 info-lane-fields item 1 data interchangeable / 379 info-req-version interchangeable / 379 info-req-version item 1 abci_version interchangeable / 已经 Info Response version 栏 interchangeable / 已经 version 是应用软件语义版本 interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 670 infousage-notappversion interchangeable / 669 infousage-nothandshake interchangeable / 668 infousage-notquerystate interchangeable / 494 infousage item 1 Return state interchangeable / 494 infousage item 2 handshake sync interchangeable / 497 infousage-persist interchangeable / 666 infousage-notlaneoptional interchangeable，也不是已经 app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事 bundled（494 item 3 余量） interchangeable / 370 info-handshake item 2 app_version in Header interchangeable / 663 infousage-notintable interchangeable / 664 infousage-notpriorityzero interchangeable，也不是已经 Info 请求 abci_version 是 ABCI 语义版本 interchangeable / 669 infousage-nothandshake item 3 not Info request version interchangeable / 494 infousage item 3 app_version interchangeable。**  
   官方把 Usage app_version in Header 单句和 Info Response version 栏路径分开——494 bundled 第三件事常与 389 混成「看见 app_version included in Header 就已经 Info 回包 version 栏 interchangeable / 就已经 version 是应用软件语义版本 interchangeable / 就已经选型 interchangeable」，本页钉 not Info response version 单句。看见 returned app_version，不是已经 Info 回包 version 是应用软件语义版本 interchangeable——389 钉 Response version 栏，本页钉 Usage app_version 进 Header。看见 included in Header of every block，不是已经 Info 请求 abci_version 是 ABCI 语义版本 interchangeable——379/669 另钉 Request version / handshake verified，本页钉 item 3 第二件事。

3. **看见 app_version will be included in the Header of every block / 会写进每一块 Header is not already 已经印进本头 AppHash（147） interchangeable / 147 apphash-this-block interchangeable / 已经本头 AppHash 就已经是本高度交差 interchangeable / 已经 AppHash 交差 interchangeable / 320 crash recovery interchangeable / 370 info-handshake item 2 app_version in Header interchangeable / 494 infousage item 1 app_version interchangeable，也不是已经 Info Usage 正式三事 bundled（494） interchangeable / 670 infousage-notappversion interchangeable / 669 infousage-nothandshake interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 last_block persisted interchangeable，也不是已经 app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事 bundled（494 item 3 余量） interchangeable / 370 info-handshake bundled interchangeable / 389 info-lane-fields interchangeable / 481 commitpersist interchangeable，也不是已经 last_block persisted during Commit not Info response last_block fields interchangeable / 665 infousage-notcommitpersist item 3 not Info response last_block fields interchangeable / 587 finreturn interchangeable / 335 finpersist interchangeable。**  
   官方把 Usage app_version in Header 单句和本头 AppHash 交差路径分开——494 bundled 第三件事常与 147/320 混成「看见 app_version included in Header 就已经印进本头 AppHash interchangeable / 就已经本高度交差 interchangeable / 就已经 persisted interchangeable」，本页钉 not AppHash in header 单句。看见 included in Header of every block，不是已经本头 AppHash 就已经是本高度交差 interchangeable——147 钉 AppHash 语境，本页钉 Usage app_version 进 Header 规则。看见 returned app_version，不是已经 last_block persisted during Commit interchangeable——665/497 另钉 last_block persist，本页钉 item 3 第三件事。494 infousage vs handshake bundled unbundling 在本页 item 3 完成。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。Info Usage 正式三事 bundled（494）、Return information about application state not QueryState（494 item 1 余量 / 668）、Used to sync during handshake not Info 握手 bundled（494 item 2 余量 / 669）、Info 用来握手对齐 bundled（370）、Info 回包 data / version 栏（389）、Info 请求 version 栏（379）、last_block persisted during Commit（497 item 1 余量 / 665）是另外那套，本页不抄。

## 官方为什么这样拆

- **app_version in Header not last_block persisted during Commit ≠ 370 info-handshake bundled interchangeable：** 官方把 Methods Info Usage app_version in Header 单句和 bundled 370 第三件事分开。
- **app_version in Header not Info response version ≠ 389 info-lane-fields interchangeable：** 官方把 Usage app_version in Header 单句和 Info Response version 栏路径分开。
- **app_version in Header not AppHash in header ≠ 147 apphash-this-block interchangeable：** 官方把 Usage app_version in Header 单句和本头 AppHash 交差路径分开；494 infousage vs handshake bundled unbundling 完成（670 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| app_version included in Header | 不是 last_block persisted during Commit（370/665） | 不是 Used to sync during handshake（669/494 item 2） |
| returned app_version | 不是 Info response version（389） | 不是 Info request abci_version（379/669） |
| 会写进 Header | 不是 AppHash in header（147） | 不是 crash recovery already Commit（320） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info Usage app_version included in Header not last_block persisted during Commit / not Info response version / not AppHash in header 正式三事（494 余量），必须分开 app_version included in Header 是不是 last_block persisted during Commit interchangeable / 370 info-handshake bundled interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist item 1 interchangeable、returned app_version 是不是 Info response version interchangeable / 389 info-lane-fields interchangeable / 379 info-req-version interchangeable / 669 infousage-nothandshake interchangeable、会写进 Header 是不是 AppHash in header interchangeable / 147 apphash-this-block interchangeable / 320 crash recovery interchangeable / 587 finreturn interchangeable。可以跳过「看见 app_version included in Header 就已经 last_block persisted interchangeable / 就已经 Info version 栏 interchangeable / 就已经印进 AppHash interchangeable」。不要另写怎样写 Info。494 infousage vs handshake bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- Info Usage 正式三事 bundled。那是不变量 494。
- Return information about application state not QueryState。那是不变量 494 item 1 余量 / 668。
- Used to sync during handshake not Info 握手 bundled。那是不变量 494 item 2 余量 / 669。
- Info 用来握手对齐 bundled。那是不变量 370。
- Info 回包 data / version 栏。那是不变量 389。
- Info 请求 version 栏。那是不变量 379。
- last_block persisted during Commit。那是不变量 497 item 1 余量 / 665。
- 本头 AppHash 就已经是本高度交差。那是不变量 147（本页钉 not AppHash in header 单句，不抄 147 全文）。
