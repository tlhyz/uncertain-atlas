# 例：看见能回 / 看见握手了 / 看见对齐了 is not already already statesync interchangeable / already querystate interchangeable / already settled interchangeable

**层次**：实现 / Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事（370 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事（370 余量）/ not 857 info-notstatesync interchangeable / not 370 info bundled interchangeable」，不是 info bundled（370），也不是 app_version 进每块头不是已经印进本头 AppHash（858 item 2 余量）或 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差（859 item 3 余量）。不要另写怎样写 Info 握手。

## 官方三件事

规范把 Methods 里 Info 用来在启动或恢复时让引擎和应用握手对齐 和「已经是能回就已经是快照重放 interchangeable / 已经是握手了就已经是 QueryState interchangeable / 已经是对齐了就已经交差 interchangeable / 已经是 info bundled interchangeable」分开写成三件独立的实现事，不是「看见能回就已经是快照重放 interchangeable / 就已经是 QueryState interchangeable / 就已经交差 interchangeable」一件事：

1. **看见能回 / 看见 Info 用来在启动或恢复时让引擎和应用握手对齐 / 看见能回 Info is not already 已经是快照重放 interchangeable / 已经 statesync interchangeable / 已经是快照重放交差 interchangeable / 370 info bundled interchangeable / 38 genesis-replay interchangeable / info-sold-as-handshake interchangeable，也不是已经 info bundled（370） interchangeable / 857 info-notstatesync interchangeable / 370 info item 1 interchangeable，也不是已经 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事 bundled（370 item 1 余量） interchangeable / 370 info item 1 interchangeable，也不是已经 app_version 进头就已经印进本头 AppHash（858） interchangeable / 859 info-notpersist interchangeable / 314 querystate interchangeable，也不是已经应用快照就已经从创世重放（38） interchangeable。**  
   官方写：Info 用来回报应用状态。启动或恢复时，CometBFT 用这次握手和应用对齐。看见能回，不是已经是快照重放。看见能回，不是已经 statesync interchangeable——370 钉 bundled 三事，本页从 item 1 侧钉 not already statesync 单句。看见 Info 用来在启动或恢复时让引擎和应用握手对齐，不是已经 info bundled（370） interchangeable——370 钉 bundled，本页钉 item 1 第一件事。看见能回，不是已经 app_version 进头就已经印进本头 AppHash（858） interchangeable——858 另钉 item 2。看见能回，不是已经 last_block 要落盘就已经交差（859） interchangeable——859 另钉 item 3。370 info-vs-handshake bundled unbundling 在本页 item 1 启动。

2. **看见握手了 / 看见启动或恢复时用这次握手和应用对齐 / 看见握过手 is not already 已经是 QueryState interchangeable / 已经 querystate interchangeable / 已经是 QueryState 交差 interchangeable / 370 info bundled interchangeable / 314 querystate interchangeable，也不是已经 info bundled（370） interchangeable / 857 info-notstatesync interchangeable / 370 info item 2 进头 interchangeable / 370 info item 3 落盘 interchangeable，也不是已经 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事 bundled（370 item 1 余量） interchangeable / 370 info item 1 interchangeable，也不是已经是快照重放（本页第一件事） interchangeable。**  
   官方写：看见握手了，不是已经是 QueryState。看见启动或恢复时用这次握手和应用对齐，不是已经 querystate interchangeable——本页钉 not already querystate 单句。看见握过手，不是已经是快照重放（本页第一件事） interchangeable——三件事分开钉。370 info-vs-handshake bundled unbundling 在本页 item 1 启动。

3. **看见对齐了 / 看见和应用对齐 / 看见对齐过 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 370 info bundled interchangeable / 33 fourgates interchangeable，也不是已经 info bundled（370） interchangeable / 857 info-notstatesync interchangeable / 370 info item 2 / 370 info item 3，也不是已经 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事 bundled（370 item 1 余量） interchangeable / 370 info item 1 interchangeable，也不是已经是快照重放（本页第一件事） interchangeable / 已经是 QueryState（本页第二件事） interchangeable。**  
   官方写：看见对齐了，不是已经交差。看见和应用对齐，不是已经 settled interchangeable——本页钉 not already settled 单句。看见对齐过，不是已经是 QueryState（本页第二件事） interchangeable——三件事分开钉。370 info-vs-handshake bundled unbundling 在本页 item 1 启动。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。info bundled（370）、app_version 进每块头不是已经印进本头 AppHash（370 item 2 余量 / 858）、last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差（370 item 3 余量 / 859）、QueryState 就已经是 ExecuteTxState（314）、应用快照就已经从创世重放（38）、本头 AppHash 就已经是本高度交差（147）是另外那套，本页不抄。

## 官方为什么这样拆

- **能回 not already statesync ≠ 370 / 38 interchangeable：** 官方把握手对齐和快照重放分开。
- **握手了 not already querystate ≠ 已经是 QueryState interchangeable：** 官方把握手了和已经是 QueryState 分开。
- **对齐了 not already settled ≠ 已经交差 interchangeable：** 官方把对齐了和已经交差分开；370 info-vs-handshake bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 能回 | 不是 already statesync | 不是应用快照就已经从创世重放 alone（38） |
| 握手了 | 不是 already querystate | 不是 QueryState 就已经是 ExecuteTxState alone（314） |
| 对齐了 | 不是 already settled | 不是 app_version 进头 already apphash alone（858） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 用来握手对齐不是已经是快照重放 not already statesync / not already querystate / not already settled 正式三事（370 余量），必须分开能回 是不是 already statesync interchangeable / 370 info bundled interchangeable / info-sold-as-handshake interchangeable、握手了 是不是 already querystate interchangeable、对齐了 是不是 already settled interchangeable。可以跳过「看见能回就已经是快照重放 interchangeable / 就已经是 QueryState interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Info 握手。370 info-vs-handshake bundled unbundling 在本页 item 1 启动；完成 [`worked-example-info-notapphash-vs-bundled.md`](worked-example-info-notapphash-vs-bundled.md)（不变量 858 item 2）；完成 [`worked-example-info-notpersist-vs-bundled.md`](worked-example-info-notpersist-vs-bundled.md)（不变量 859 item 3）。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- info bundled。那是不变量 370。
- app_version 进每块头不是已经印进本头 AppHash。那是不变量 370 item 2 余量 / 858。
- last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差。那是不变量 370 item 3 余量 / 859。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- 应用快照就已经从创世重放。那是不变量 38。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
