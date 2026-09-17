# 例：看见 Query 连接 is not already ExecuteTxState interchangeable / not already writable interchangeable / not already settled interchangeable

**层次**：实现 / Query 连接 not already ExecuteTxState / not already writable / not already settled 正式三事（314 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Query 连接 not already ExecuteTxState / not already writable / not already settled 正式三事（314 余量）/ not 962 querystate-notexec interchangeable / not 314 querystate-vs-execute bundled interchangeable」，不是 QueryState bundled（314），也不是 CheckTxState 已经是 ExecuteTxState（312），也不是 Query 回了就已经复制（329/938）。不要另写怎样实现 QueryState 或怎样做 state sync。

## 官方三件事

1. **看见 Query 连接 / 看见在答用户查询 这份副本 is not already 已经是 ExecuteTxState interchangeable，也不是已经 QueryState bundled（314） interchangeable / 962 querystate-notexec interchangeable / 963 querystate-notlive interchangeable / 314 querystate item 2 上次 Commit interchangeable，也不是已经 Query 连接 not already ExecuteTxState / not already writable / not already settled 正式三事 bundled（314 item 1 余量） interchangeable / 314 querystate item 1 interchangeable。**  
   官方写：Info（或 Query）连接应维持一份 QueryState。QueryState 是 ExecuteTxState 在上次 Commit 之后的只读副本。看见能查，不是已经是工作状态 interchangeable——本页从 314 item 1 侧钉 not already ExecuteTxState 单句。314 querystate vs execute bundled unbundling 在本页 item 1 启动。

2. **看见连接在 / 看见能查 / 这份副本 is not already 已经能改工作状态 interchangeable，也不是已经 QueryState bundled（314） interchangeable / 962 querystate-notexec interchangeable / 314 querystate item 3 启动对齐 interchangeable / 964 querystate-notsnap interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把能查和已经能写分开——314 bundled 第一件事常与 312 混成「看见能查就已经是工作状态或已经是 CheckTxState interchangeable」，本页钉 not already writable 单句。

3. **看见名字里有 Query / 看见能查 / 这份副本 is not already 已经交差 interchangeable，也不是已经 QueryState bundled（314） interchangeable / 962 querystate-notexec interchangeable / 963 querystate-notlive interchangeable，也不是已经 Query 回了就已经复制 interchangeable / 329/938 query-notrepl interchangeable。**  
   官方把名字里有 Query 和已经和执行那份同一份分开。看见名字里有 Query，不是已经交差 interchangeable。314 querystate vs execute bundled unbundling 在本页 item 1 启动。

怎样实现 QueryState、怎样做 state sync、怎样写四门是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Query 连接 not already ExecuteTxState ≠ 已经是 ExecuteTxState interchangeable：** 官方把只读副本和工作状态分开。
- **看见连接在 not already writable ≠ 已经能改工作状态 interchangeable：** 官方把能查和已经能写分开。
- **看见名字里有 Query not already settled ≠ 已经交差 interchangeable：** 官方把名字里有 Query 和已经同一份分开；314 querystate vs execute bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 连接 | 不是已经是 ExecuteTxState | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 看见连接在 | 不是已经能改工作状态 | 不是 Query 回了就已经复制（329/938） |
| 看见名字里有 Query | 不是已经交差 | 不是上次 Commit 就已经跟上正在跑的块（963） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 连接 not already ExecuteTxState / not already writable / not already settled 正式三事（314 余量），必须分开是不是已经是 ExecuteTxState、是不是已经能写、是不是已经交差。可以跳过「看见能查就已经是工作状态」。不要另写怎样实现 QueryState 或怎样做 state sync。314 querystate vs execute bundled unbundling 在本页 item 1 启动；续 [`worked-example-querystate-notlive-vs-bundled.md`](worked-example-querystate-notlive-vs-bundled.md)（不变量 963 item 2）。

## 本页不抄

- 怎样实现 QueryState、怎样做 state sync、怎样写四门。
- QueryState bundled。那是不变量 314。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- Query 回了就已经复制。那是不变量 329/938。
