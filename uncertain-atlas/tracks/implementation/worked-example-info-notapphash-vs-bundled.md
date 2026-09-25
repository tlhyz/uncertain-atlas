# 例：看见有版本 / 看见进了头 / 看见字段在 is not already already apphash interchangeable / already settled interchangeable / already algo interchangeable

**层次**：实现 / app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事（370 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事（370 余量）/ not 858 info-notapphash interchangeable / not 370 info bundled interchangeable」，不是 info bundled（370），也不是 Info 用来握手对齐不是已经是快照重放（857 item 1 余量）或 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差（859 item 3 余量）。不要另写怎样写 Info 握手。

## 官方三件事

规范把 Methods 里回的 `app_version` 会写进每一块的 Header 和「已经是有版本就已经印进本头 AppHash interchangeable / 已经是进了头就已经是本高度交差 interchangeable / 已经是字段在就已经选型 interchangeable / 已经是 info bundled interchangeable」分开写成三件独立的实现事，不是「看见有版本就已经印进本头 AppHash interchangeable / 就已经是本高度交差 interchangeable / 就已经选型 interchangeable」一件事：

1. **看见有版本 / 看见回的 `app_version` 会写进每一块的头 / 看见有 app_version is not already 已经印进本头 AppHash interchangeable / 已经 apphash interchangeable / 已经印进本头 AppHash 交差 interchangeable / 370 info bundled interchangeable / 147 apphash interchangeable / info-sold-as-handshake interchangeable，也不是已经 info bundled（370） interchangeable / 858 info-notapphash interchangeable / 370 info item 2 interchangeable，也不是已经 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事 bundled（370 item 2 余量） interchangeable / 370 info item 2 interchangeable，也不是已经握手对齐就已经是快照重放（857） interchangeable / 859 info-notpersist interchangeable / 330 veheight interchangeable，也不是已经本头 AppHash 就已经是本高度交差（147） interchangeable。**  
   官方写：回的 `app_version` 会写进每一块的 Header。看见有版本，不是已经印进本头 AppHash。看见有版本，不是已经 apphash interchangeable——370 钉 bundled 三事，本页从 item 2 侧钉 not already apphash 单句。看见回的 `app_version` 会写进每一块的头，不是已经 info bundled（370） interchangeable——370 钉 bundled，本页钉 item 2 第一件事。看见有版本，不是已经握手对齐就已经是快照重放（857） interchangeable——857 另钉 item 1。看见有版本，不是已经 last_block 要落盘就已经交差（859） interchangeable——859 另钉 item 3。370 info-vs-handshake bundled unbundling 在本页 item 2 续。

2. **看见进了头 / 看见会写进每一块的 Header / 看见进头了 is not already 已经是本高度交差 interchangeable / 已经 settled interchangeable / 已经是本高度交差交差 interchangeable / 370 info bundled interchangeable / 147 apphash interchangeable，也不是已经 info bundled（370） interchangeable / 858 info-notapphash interchangeable / 370 info item 1 握手 interchangeable / 370 info item 3 落盘 interchangeable，也不是已经 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事 bundled（370 item 2 余量） interchangeable / 370 info item 2 interchangeable，也不是已经印进本头 AppHash（本页第一件事） interchangeable。**  
   官方写：看见进了头，不是已经是本高度交差。看见会写进每一块的 Header，不是已经 settled interchangeable——本页钉 not already settled 单句。看见进头了，不是已经印进本头 AppHash（本页第一件事） interchangeable——三件事分开钉。370 info-vs-handshake bundled unbundling 在本页 item 2 续。

3. **看见字段在 / 看见 app_version 字段在 / 看见版本字段在 is not already 已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable / 370 info bundled interchangeable / 389 infover interchangeable，也不是已经 info bundled（370） interchangeable / 858 info-notapphash interchangeable / 370 info item 1 / 370 info item 3，也不是已经 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事 bundled（370 item 2 余量） interchangeable / 370 info item 2 interchangeable，也不是已经印进本头 AppHash（本页第一件事） interchangeable / 已经是本高度交差（本页第二件事） interchangeable。**  
   官方写：看见字段在，不是已经选型。看见 app_version 字段在，不是已经 algo interchangeable——本页钉 not already algo 单句。看见版本字段在，不是已经是本高度交差（本页第二件事） interchangeable——三件事分开钉。370 info-vs-handshake bundled unbundling 在本页 item 2 续。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。info bundled（370）、Info 用来握手对齐不是已经是快照重放（370 item 1 余量 / 857）、last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差（370 item 3 余量 / 859）、本头 AppHash 就已经是本高度交差（147）、QueryState 就已经是 ExecuteTxState（314）、崩溃三步就已经 Commit（320）是另外那套，本页不抄。

## 官方为什么这样拆

- **有版本 not already apphash ≠ 370 / 147 interchangeable：** 官方把版本进头和本头 AppHash 分开。
- **进了头 not already settled ≠ 已经是本高度交差 interchangeable：** 官方把进了头和已经是本高度交差分开。
- **字段在 not already algo ≠ 已经选型 interchangeable：** 官方把字段在和已经选型分开；370 info-vs-handshake bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有版本 | 不是 already apphash | 不是本头 AppHash 就已经是本高度交差 alone（147） |
| 进了头 | 不是 already settled | 不是握手对齐 already statesync alone（857） |
| 字段在 | 不是 already algo | 不是 last_block 要落盘 already settled alone（859） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_version 进每块头不是已经印进本头 AppHash not already apphash / not already settled / not already algo 正式三事（370 余量），必须分开有版本 是不是 already apphash interchangeable / 370 info bundled interchangeable / info-sold-as-handshake interchangeable、进了头 是不是 already settled interchangeable、字段在 是不是 already algo interchangeable。可以跳过「看见有版本就已经印进本头 AppHash interchangeable / 就已经是本高度交差 interchangeable / 就已经选型 interchangeable」。不要另写怎样写 Info 握手。370 info-vs-handshake bundled unbundling 在本页 item 2 续。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- info bundled。那是不变量 370。
- Info 用来握手对齐不是已经是快照重放。那是不变量 370 item 1 余量 / 857。
- last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差。那是不变量 370 item 3 余量 / 859。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- 崩溃三步就已经 Commit。那是不变量 320。
