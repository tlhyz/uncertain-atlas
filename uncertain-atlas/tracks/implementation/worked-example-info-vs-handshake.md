# 例：看见 Info 用来握手对齐不是已经是快照重放；看见 app_version 进每块头不是已经印进本头 AppHash；看见 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差

**层次**：实现 / Info 握手。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Info 用来握手对齐不是已经是快照重放 / app_version 进每块头不是已经印进本头 AppHash / last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差」，不是 QueryState 就已经是 ExecuteTxState，也不是崩溃三步就已经 Commit。不要另写怎样写 Info 握手。

## 官方三件事

规范把 Info 用来握手对齐、`app_version` 进每块头、`last_block_app_hash` / `last_block_height` 要在 Commit 里落盘写成三件独立的实现事，不是「看见能回 Info 就已经是快照重放、已经印进本头 AppHash、已经交差」一件事：

1. **看见 Info 用来在启动或恢复时让引擎和应用握手对齐 / 看见能回 不是已经是快照重放，也不是已经是 QueryState。**  
   官方写：Info 用来回报应用状态。启动或恢复时，CometBFT 用这次握手和应用对齐。看见能回，不是已经是快照重放。看见握手了，不是已经是 QueryState。看见对齐了，不是已经交差。
2. **看见回的 `app_version` 会写进每一块的头 / 看见有版本 不是已经印进本头 AppHash，也不是已经交差。**  
   官方写：回的 `app_version` 会写进每一块的 Header。看见有版本，不是已经印进本头 AppHash。看见进了头，不是已经是本高度交差。看见字段在，不是已经选型。
3. **看见引擎指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘 / 看见回了这两列 不是已经交差，也不是已经在剪。**  
   官方写：CometBFT 指望 `last_block_app_hash` 和 `last_block_height` 在 `Commit` 里更新并落盘。看见回了这两列，不是已经交差。看见要在 Commit 里落，不是已经是崩溃三步已经 Commit。看见有高度，不是已经在剪。

怎样写 Info 回包、怎样对版本、怎样落盘是规范里的做法，本页不抄。QueryState 就已经是 ExecuteTxState 是不变量 314，本页不抄。

## 官方为什么这样拆

- **Info 用来握手对齐 ≠ 已经是快照重放：** 官方把握手对齐和快照重放分开。
- **app_version 进每块头 ≠ 已经印进本头 AppHash：** 官方把版本进头和本头 AppHash 分开。
- **last_block_app_hash / last_block_height 要在 Commit 里落盘 ≠ 已经交差：** 官方把要落盘和已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 用来握手对齐 | 不是已经是快照重放 | 不是 QueryState 就已经是 ExecuteTxState（314） |
| app_version 进每块头 | 不是已经印进本头 AppHash | 不是本头 AppHash 就已经是本高度交差（147） |
| last_block_app_hash / last_block_height 要在 Commit 里落盘 | 不是已经交差 | 不是崩溃三步就已经 Commit（320） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能回 Info 就已经是快照重放、已经印进本头 AppHash、已经交差」，必须分开 Info 用来握手对齐是不是已经是快照重放、app_version 进每块头是不是已经印进本头 AppHash、last_block_app_hash / last_block_height 要在 Commit 里落盘是不是已经交差。可以跳过「看见能回 Info 就已经是快照重放」。不要另写怎样写 Info 握手。370 info vs handshake bundled unbundling 完成（815 item 1 / 816 item 2 / 817 item 3）；精读 [`worked-example-info-notreplay-vs-bundled.md`](worked-example-info-notreplay-vs-bundled.md)（不变量 815 item 1）。

## 本页不抄

- 怎样写 Info 回包、怎样对版本、怎样落盘。
- QueryState 就已经是 ExecuteTxState。那是不变量 314。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- 崩溃三步就已经 Commit。那是不变量 320。
