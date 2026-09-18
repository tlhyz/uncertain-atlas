# 例：看见上次 Commit / 能读 / 只读 is not already already caught up interchangeable / already CheckTxState interchangeable / already synced interchangeable

**层次**：实现 / 上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事（314 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事（314 余量）/ not 702 querystate-notcaughtup interchangeable / not 314 querystate bundled interchangeable」，不是 QueryState vs ExecuteTxState bundled（314），也不是 Query 连接不是已经是 ExecuteTxState（701 item 1 余量）或启动对齐不是已经是快照重放（703 item 3 余量）。不要另写怎样实现 QueryState 或怎样做 state sync。

## 官方三件事

规范把 Requirements 里这份副本是整块处理完、状态已经提交到盘之后的那一份 和「已经是上次 Commit 就已经跟上正在跑的块 interchangeable / 已经是能读就已经是 CheckTxState interchangeable / 已经是只读就已经和正在改的 ExecuteTxState 同步 interchangeable / 已经是 QueryState vs ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见上次 Commit 就已经跟上 interchangeable / 就已经是 CheckTxState interchangeable / 就已经同步 interchangeable」一件事：

1. **看见上次 Commit / 看见 QueryState / 看见提交到盘之后的副本 is not already 已经跟上正在跑的块 interchangeable / 已经 caught up interchangeable / 已经含本轮还没交差的执行 interchangeable / 314 querystate bundled interchangeable / 312 checktxstate bundled interchangeable / querystate-sold-as-execute interchangeable，也不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable / 702 querystate-notcaughtup interchangeable / 314 querystate item 2 interchangeable，也不是已经上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事 bundled（314 item 2 余量） interchangeable / 314 querystate item 2 interchangeable，也不是已经 Query 连接不是已经是 ExecuteTxState（701） interchangeable / 703 querystate-notsnapshot interchangeable / 310 commitlock interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：这份副本是整块处理完、状态已经提交到盘之后的那一份。看见上次 Commit，不是已经含本轮还没交差的执行 interchangeable——314 钉 bundled 三事，本页从 item 2 侧钉 not already caught up 单句。看见 QueryState，不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable——314 钉 bundled，本页钉 item 2 第一件事。看见提交到盘之后的副本，不是已经 Query 连接不是已经是 ExecuteTxState（701） interchangeable——701 另钉 item 1，本页钉 item 2 第一件事。314 querystate vs execute bundled unbundling 在本页 item 2 续。

2. **看见能读 / 看见可以查 / 看见只读副本能答 is not already 已经是内存池那份 CheckTxState interchangeable / 已经 CheckTxState interchangeable / 已经是 CheckTx 那份 interchangeable / 314 querystate bundled interchangeable / 312 checktxstate bundled interchangeable，也不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable / 702 querystate-notcaughtup interchangeable / 314 querystate item 1 能查 interchangeable / 314 querystate item 3 快照重放 interchangeable，也不是已经上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事 bundled（314 item 2 余量） interchangeable / 314 querystate item 2 interchangeable，也不是已经跟上正在跑的块（本页第一件事） interchangeable。**  
   官方把能读和已经是内存池那份 CheckTxState 路径分开——能读，不等于已经是 CheckTxState。看见能读，不是已经是 CheckTxState interchangeable——本页钉 not already CheckTxState 单句。看见可以查，不是已经 Query 连接不是已经是 ExecuteTxState（701） interchangeable——701 另钉 item 1，本页钉 item 2 第二件事。看见只读副本能答，不是已经启动对齐不是已经是快照重放（703） interchangeable——703 另钉 item 3，本页钉 item 2 第二件事。314 querystate vs execute bundled unbundling 在本页 item 2 续。

3. **看见只读 / 看见只读副本 / 看见 QueryState 只读 is not already 已经和正在改的 ExecuteTxState 同步 interchangeable / 已经 synced interchangeable / 已经跟上执行那份 interchangeable / 314 querystate bundled interchangeable / 33 four gates interchangeable，也不是已经 QueryState vs ExecuteTxState bundled（314） interchangeable / 702 querystate-notcaughtup interchangeable / 314 querystate item 1 / 314 querystate item 3，也不是已经上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事 bundled（314 item 2 余量） interchangeable / 314 querystate item 2 interchangeable，也不是已经跟上正在跑的块（本页第一件事） interchangeable / 已经是 CheckTxState（本页第二件事） interchangeable。**  
   官方把只读和已经和正在改的 ExecuteTxState 同步路径分开——只读，不等于已经同步。看见只读，不是已经和正在改的 ExecuteTxState 同步 interchangeable——本页钉 not already synced 单句。看见只读副本，不是已经跟上正在跑的块（本页第一件事） interchangeable——三件事分开钉。看见 QueryState 只读，不是已经四门已经结算（33） interchangeable——33 另钉。314 querystate vs execute bundled unbundling 在本页 item 2 完成。

怎样实现 QueryState、怎样做 state sync、怎样写四门是规范里的取值或做法，本页不抄。QueryState vs ExecuteTxState bundled（314）、Query 连接不是已经是 ExecuteTxState（314 item 1 余量 / 701）、启动对齐不是已经是快照重放（314 item 3 余量 / 703）、CheckTxState vs ExecuteTxState（312）、默认锁已经 RPC 安全（310）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **上次 Commit not already caught up ≠ 314 / 312 interchangeable：** 官方把提交到盘之后的副本单句和已经跟上正在跑的块路径分开。
- **能读 not already CheckTxState ≠ 已经是 CheckTxState interchangeable：** 官方把能读单句和已经是内存池那份路径分开。
- **只读 not already synced ≠ 已经和正在改的 ExecuteTxState 同步 interchangeable：** 官方把只读单句和已经同步路径分开；314 querystate vs execute bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 上次 Commit | 不是 already caught up | 不是能查 alone（701） |
| 能读 | 不是 already CheckTxState | 不是快照重放 alone（703） |
| 只读 | 不是 already synced | 不是 CheckTxState vs Execute alone（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看上次 Commit 不是已经跟上正在跑的块 not already caught up / not already CheckTxState / not already synced 正式三事（314 余量），必须分开上次 Commit 是不是 already caught up interchangeable / 314 querystate bundled interchangeable / querystate-sold-as-execute interchangeable、能读 是不是 already CheckTxState interchangeable、只读 是不是 already synced interchangeable。可以跳过「看见上次 Commit 就已经跟上 interchangeable / 就已经是 CheckTxState interchangeable / 就已经同步 interchangeable」。不要另写怎样实现 QueryState。314 querystate vs execute bundled unbundling 在本页 item 2 完成；续 [`worked-example-querystate-notsnapshot-vs-bundled.md`](worked-example-querystate-notsnapshot-vs-bundled.md)（不变量 703 item 3，待写）。

## 本页不抄

- 怎样实现 QueryState、怎样做 state sync、怎样写查询字段。
- QueryState vs ExecuteTxState bundled。那是不变量 314。
- Query 连接不是已经是 ExecuteTxState。那是不变量 314 item 1 余量 / 701。
- 启动对齐不是已经是快照重放。那是不变量 314 item 3 余量 / 703。
- CheckTxState vs ExecuteTxState。那是不变量 312。
- 默认锁已经 RPC 安全。那是不变量 310。
- 四门已经结算。那是不变量 33。
