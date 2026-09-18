# 例：看见 Query 连接不是已经是 ExecuteTxState；看见上次 Commit 不是已经跟上正在跑的块；看见启动对齐不是已经是快照重放

**层次**：实现 / QueryState。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「QueryState 不是已经是 ExecuteTxState / 上次 Commit 不是已经跟上正在跑的块 / 启动对齐不是已经是快照重放」，不是 CheckTxState 已经是工作状态，也不是默认锁已经 RPC 安全。不要另写怎样实现 QueryState 或怎样做 state sync。

## 官方三件事

规范把 Info/Query 连接上的 QueryState 写成三件独立的实现事，不是「看见能查就已经是工作状态、已经跟上正在跑的块、已经从创世重放」一件事：

1. **看见 Query 连接 / 看见在答用户查询 不是已经是 ExecuteTxState，也不是已经能改工作状态。**  
   官方写：Info（或 Query）连接应维持一份 `QueryState`。`QueryState` 是 *ExecuteTxState* 在上次 `Commit` 之后的**只读副本**。看见能查，不是已经是工作状态。看见连接在，不是已经能写。看见名字里有 Query，不是已经和执行那份同一份。
2. **看见 QueryState / 看见上次 Commit 不是已经跟上正在跑的块，也不是已经是 CheckTxState。**  
   官方写：这份副本是整块处理完、状态已经提交到盘之后的那一份。看见上次 Commit，不是已经含本轮还没交差的执行。看见能读，不是已经是内存池那份 CheckTxState。看见只读，不是已经和正在改的 ExecuteTxState 同步。
3. **看见启动时对齐 / 看见 state sync 之后对齐 不是已经是快照重放，也不是已经从创世重放。**  
   官方写：这条连接有两个用途：一是让应用回答 CometBFT 从用户那里收到的查询；二是在启动或 state sync 之后，让 CometBFT 和应用对齐。看见对齐，不是已经装了快照。看见启动握手，不是已经从创世重放。看见 Query 门，不是已经是 Snapshot 连接。

怎样实现 QueryState、怎样做 state sync、怎样写四门是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **能查 ≠ 已经是 ExecuteTxState：** 官方把只读副本和工作状态分开。
- **上次 Commit ≠ 已经跟上正在跑的块：** 官方把已提交到盘和还在执行的那份分开。
- **启动对齐 ≠ 已经是快照重放：** 官方把 Query 门上的对齐和 Snapshot 连接分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| QueryState 只读副本 | 不是已经是 ExecuteTxState | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 上次 Commit 的副本 | 不是已经跟上正在跑的块 | 不是默认锁已经 RPC 安全（310） |
| 启动 / state sync 对齐 | 不是已经是快照重放 | 不是应用快照已经从创世重放（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Query 已经能查」，必须分开 QueryState 是不是已经是 ExecuteTxState、上次 Commit 是不是已经跟上正在跑的块、启动对齐是不是已经是快照重放。可以跳过「看见能查就已经是工作状态」。不要另写怎样实现 QueryState 或怎样做 state sync。314 querystate vs execute bundled unbundling 续（701 + 702）；精读 [`worked-example-querystate-notexecute-vs-bundled.md`](worked-example-querystate-notexecute-vs-bundled.md)（不变量 701 item 1）；[`worked-example-querystate-notcaughtup-vs-bundled.md`](worked-example-querystate-notcaughtup-vs-bundled.md)（不变量 702 item 2）。

## 本页不抄

- 怎样实现 QueryState、怎样做 state sync、怎样写查询字段。
- 怎样写四门。那是不变量 33。
- 快照怎么装。那是不变量 38。
