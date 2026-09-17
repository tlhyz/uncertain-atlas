# 例：看见 Query for data at current or past height is not already QueryState interchangeable / not already replicated interchangeable / not already QueryState is ExecuteTxState interchangeable

**层次**：实现 / Query Usage Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事（487 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query Usage Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事（487 余量）/ not 677 queryusage-notquerystate interchangeable / not 487 queryusage-vs-querystate bundled interchangeable」，不是 Query Usage 正式三事 bundled（487），也不是 Query Request height 栏 bundled（371）或 Query 证明回包 bundled（383）。不要另写怎样写 Query 路径、怎样勾 prove、怎样编 proof_ops。

## 官方三件事

规范把 Query Usage 里 Query for data from the application at current or past height 和「已经是 QueryState（371 Request bundled） interchangeable / 已经复制到各节点（329） interchangeable / 已经 QueryState 就是 ExecuteTxState（314） interchangeable / 已经能查就已经交差 interchangeable」分开写成三件独立的实现事，不是「看见 Query for data at current or past height 就已经 QueryState interchangeable / 就已经 replicated interchangeable / 就已经 QueryState is ExecuteTxState interchangeable」一件事：

1. **看见 Query for data from the application at current or past height / 看见查应用在当前或过去高度的数据 / at current or past height is not already 已经是 QueryState（371 Request bundled） interchangeable / 371 queryheight interchangeable / 371 queryheight item 2 height 默认 0 interchangeable / 已经 Query Request `height` 默认 0 回最新已提交 interchangeable / 已经是 QueryState 那份只读副本 interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 677 queryusage-notquerystate interchangeable / 678 queryusage-notproof interchangeable / 487 queryusage item 2 Optionally Merkle proof interchangeable，也不是已经 Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事 bundled（487 item 1 余量） interchangeable / 487 queryusage item 1 interchangeable，也不是已经 Optionally return Merkle proof bundled（487 item 2 余量 / 678） interchangeable / 383 queryproof interchangeable / 487 queryusage bundled interchangeable。**  
   官方 Usage 写：Query for data from the application at current or past height。看见 at current or past height，不是已经是 Query Request `height` 默认 0 回最新已提交 interchangeable——371 钉 Request 栏，本页从 487 item 1 侧钉 not QueryState 单句。看见 for data from the application，不是已经是 QueryState 那份只读副本 interchangeable。看见能查，不是已经 Query Usage 正式三事 bundled（487） interchangeable——487 钉 bundled 三事，本页钉 Methods Query Usage 查哪一高度单句。487 queryusage vs querystate bundled unbundling 在本页 item 1 启动。

2. **看见 Query for data from the application at current or past height / 查应用在当前或过去高度 / 看见能查 is not already 已经复制到各节点（329） interchangeable / 329 query-vs-replicated interchangeable / 已经查到了就已经新鲜 interchangeable / 已经实现了 Query 就已经是正常运转必须有 interchangeable / 已经 RPC 回了就代表各节点同一份 interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 677 queryusage-notquerystate interchangeable / 487 queryusage item 1 QueryState interchangeable / 487 queryusage item 3 self-describing type interchangeable，也不是已经 Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事 bundled（487 item 1 余量） interchangeable / 487 queryusage item 1 interchangeable，也不是已经 Merkle proof self-describing type bundled（487 item 3 余量 / 679） interchangeable / 325 proofop interchangeable。**  
   官方把 Usage Query for data at current or past height 单句和 Query 回了就已经复制到各节点路径分开——487 bundled 第一件事常与 329 混成「看见能查 就已经复制到各节点 interchangeable / 就已经新鲜 interchangeable」，本页钉 not replicated 单句。看见 for data from the application，不是已经 Query 回了就已经复制到各节点 interchangeable——329 钉 replicated 全段，本页钉 Usage 查哪一高度语义。看见 at current or past height，不是已经实现了 Query 就已经是正常运转必须有 interchangeable。

3. **看见 Query for data from the application at current or past height / 查当前或过去高度 / 看见 Query 能叫 is not already 已经 QueryState 就是 ExecuteTxState（314） interchangeable / 314 querystate interchangeable / 已经上次 Commit 就已经跟上正在跑的块 interchangeable / 已经启动对齐就已经是快照重放 interchangeable / 已经 QueryState 工作副本 interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 677 queryusage-notquerystate interchangeable / 487 queryusage item 2 Optionally Merkle proof interchangeable / 678 queryusage-notproof interchangeable，也不是已经 Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事 bundled（487 item 1 余量） interchangeable / 371 queryheight interchangeable / 668 infousage-notquerystate interchangeable。**  
   官方把 Usage Query for data at current or past height 单句和 QueryState 就是 ExecuteTxState 路径分开——487 bundled 第一件事常与 314 混成「看见能查 就已经 QueryState 就是 ExecuteTxState interchangeable / 就已经工作副本 interchangeable」，本页钉 not QueryState is ExecuteTxState 单句。看见查应用数据，不是已经 QueryState 就是 ExecuteTxState interchangeable——314 钉 QueryState vs ExecuteTxState，本页钉 Methods Query Usage 查哪一高度。看见 current or past height，不是已经 Info Usage Return application state 就已经 QueryState interchangeable——668 另钉 Info，本页钉 Query Usage item 1。487 queryusage vs querystate bundled unbundling 在本页 item 1 启动。

怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。Query Usage 正式三事 bundled（487）、Optionally return Merkle proof not prove 栏（487 item 2 余量 / 678）、Merkle proof self-describing type not ProofOp（487 item 3 余量 / 679）、Query Request height 栏（371）、Query 回了就已经复制（329）、QueryState 就是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **Query for data at current or past height not QueryState ≠ 371 queryheight interchangeable：** 官方把 Methods Usage 查哪一高度单句和 Query Request height 栏 / QueryState 那份只读副本分开。
- **Query for data at current or past height not replicated ≠ 329 query-vs-replicated interchangeable：** 官方把 Usage 查当前或过去高度单句和 Query 回了就已经复制到各节点路径分开。
- **Query for data at current or past height not QueryState is ExecuteTxState ≠ 314 querystate interchangeable：** 官方把 Usage 查哪一高度单句和 QueryState 就是 ExecuteTxState 路径分开；487 queryusage vs querystate bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query for data at current or past height | 不是 QueryState（371） | 不是 Optionally return Merkle proof（678/487 item 2） |
| 查应用在当前或过去高度 | 不是已经复制到各节点（329） | 不是 Query Request height 栏 bundled（371） |
| 看见能查 | 不是 QueryState 就是 ExecuteTxState（314） | 不是 Merkle proof self-describing type（679/487 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Query for data at current or past height not QueryState / not replicated / not QueryState is ExecuteTxState 正式三事（487 余量），必须分开 Query for data at current or past height 是不是 QueryState interchangeable / 371 queryheight interchangeable / 已经是 QueryState 那份只读副本 interchangeable、查应用在当前或过去高度 是不是已经复制到各节点 interchangeable / 329 query-vs-replicated interchangeable、看见能查 是不是 QueryState 就是 ExecuteTxState interchangeable / 314 querystate interchangeable / 668 infousage-notquerystate interchangeable。可以跳过「看见能查 就已经 QueryState interchangeable / 就已经 replicated interchangeable / 就已经 QueryState is ExecuteTxState interchangeable」。不要另写怎样写 Query。487 queryusage vs querystate bundled unbundling 在本页 item 1 启动；续 [`worked-example-queryusage-notproof-vs-bundled.md`](worked-example-queryusage-notproof-vs-bundled.md)（不变量 678 item 2）。

## 本页不抄

- 怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops。
- Query Usage 正式三事 bundled。那是不变量 487。
- Optionally return Merkle proof not prove 栏。那是不变量 487 item 2 余量 / 678。
- Merkle proof self-describing type not ProofOp。那是不变量 487 item 3 余量 / 679。
- Query Request height 栏 / height 默认 0 / Height-1 提交后的状态。那是不变量 371。
- Query 回了就已经复制到各节点。那是不变量 329。
- QueryState 就是 ExecuteTxState。那是不变量 314。
