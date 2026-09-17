# 例：看见启动对齐 is not already snapshot-replay interchangeable / not already genesis-replay interchangeable / not already settled interchangeable

**层次**：实现 / 启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事（314 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事（314 余量）/ not 964 querystate-notsnap interchangeable / not 314 querystate-vs-execute bundled interchangeable」，不是 QueryState bundled（314），也不是应用快照已经从创世重放（38），也不是 Snapshot Connection 已经必须实现（334）。不要另写怎样实现 QueryState 或怎样做 state sync。

## 官方三件事

1. **看见启动时对齐 / 看见 state sync 之后对齐 这份对齐 is not already 已经是快照重放 interchangeable，也不是已经 QueryState bundled（314） interchangeable / 964 querystate-notsnap interchangeable / 962 querystate-notexec interchangeable / 963 querystate-notlive interchangeable / 314 querystate item 1 Query 连接 interchangeable，也不是已经启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事 bundled（314 item 3 余量） interchangeable / 314 querystate item 3 interchangeable。**  
   官方写：这条连接有两个用途：一是让应用回答 CometBFT 从用户那里收到的查询；二是在启动或 state sync 之后，让 CometBFT 和应用对齐。看见对齐，不是已经装了快照 interchangeable——本页从 314 item 3 侧钉 not already snapshot-replay 单句。314 querystate vs execute bundled unbundling 在本页 item 3 完成。

2. **看见启动握手 / 看见对齐 / 这份对齐 is not already 已经从创世重放 interchangeable，也不是已经 QueryState bundled（314） interchangeable / 964 querystate-notsnap interchangeable / 314 querystate item 2 上次 Commit interchangeable / 963 querystate-notlive interchangeable，也不是已经应用快照已经从创世重放 interchangeable / 38 apphash-only interchangeable。**  
   官方把启动握手和已经从创世重放分开。看见启动握手，不是已经从创世重放 interchangeable。本页钉 not already genesis-replay 单句。

3. **看见 Query 门 / 看见对齐 / 这份对齐 is not already 已经交差 interchangeable，也不是已经 QueryState bundled（314） interchangeable / 964 querystate-notsnap interchangeable / 962 querystate-notexec interchangeable，也不是已经 Snapshot Connection 已经必须实现 interchangeable / 334 snapshot-conn interchangeable。**  
   官方把 Query 门和已经是 Snapshot 连接分开。看见 Query 门，不是已经交差 interchangeable。314 querystate vs execute bundled unbundling 在本页 item 3 完成。

怎样实现 QueryState、怎样做 state sync、怎样写四门是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **启动对齐 not already snapshot-replay ≠ 已经是快照重放 interchangeable：** 官方把 Query 门上的对齐和 Snapshot 连接分开。
- **看见启动握手 not already genesis-replay ≠ 已经从创世重放 interchangeable：** 官方把启动握手和已经从创世重放分开。
- **看见 Query 门 not already settled ≠ 已经交差 interchangeable：** 官方把 Query 门和已经是 Snapshot 连接分开；314 querystate vs execute bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 启动对齐 | 不是已经是快照重放 | 不是应用快照已经从创世重放（38） |
| 看见启动握手 | 不是已经从创世重放 | 不是 Snapshot Connection 已经必须实现（334） |
| 看见 Query 门 | 不是已经交差 | 不是 Query 连接就已经是 ExecuteTxState（962） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动对齐 not already snapshot-replay / not already genesis-replay / not already settled 正式三事（314 余量），必须分开是不是已经是快照重放、是不是已经从创世重放、是不是已经交差。可以跳过「看见能查就已经是工作状态」。不要另写怎样实现 QueryState 或怎样做 state sync。314 querystate vs execute bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现 QueryState、怎样做 state sync、怎样写四门。
- QueryState bundled。那是不变量 314。
- 应用快照已经从创世重放。那是不变量 38。
- Snapshot Connection 已经必须实现。那是不变量 334。
