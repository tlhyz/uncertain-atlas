# 例：看见上次 Commit is not already live interchangeable / not already CheckTxState interchangeable / not already settled interchangeable

**层次**：实现 / 上次 Commit not already live / not already CheckTxState / not already settled 正式三事（314 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「上次 Commit not already live / not already CheckTxState / not already settled 正式三事（314 余量）/ not 963 querystate-notlive interchangeable / not 314 querystate-vs-execute bundled interchangeable」，不是 QueryState bundled（314），也不是默认锁已经 RPC 安全（310），也不是 Offer 收下已经装完（321/959）。不要另写怎样实现 QueryState 或怎样做 state sync。

## 官方三件事

1. **看见 QueryState / 看见上次 Commit 这份副本 is not already 已经跟上正在跑的块 interchangeable，也不是已经 QueryState bundled（314） interchangeable / 963 querystate-notlive interchangeable / 962 querystate-notexec interchangeable / 314 querystate item 1 Query 连接 interchangeable，也不是已经上次 Commit not already live / not already CheckTxState / not already settled 正式三事 bundled（314 item 2 余量） interchangeable / 314 querystate item 2 interchangeable。**  
   官方写：这份副本是整块处理完、状态已经提交到盘之后的那一份。看见上次 Commit，不是已经含本轮还没交差的执行 interchangeable——本页从 314 item 2 侧钉 not already live 单句。314 querystate vs execute bundled unbundling 在本页 item 2 续。

2. **看见能读 / 看见上次 Commit / 这份副本 is not already 已经是 CheckTxState interchangeable，也不是已经 QueryState bundled（314） interchangeable / 963 querystate-notlive interchangeable / 314 querystate item 3 启动对齐 interchangeable / 964 querystate-notsnap interchangeable，也不是已经默认锁已经 RPC 安全 interchangeable / 310 commit-lock interchangeable。**  
   官方把能读和已经是内存池那份 CheckTxState 分开。看见能读，不是已经是 CheckTxState interchangeable。本页钉 not already CheckTxState 单句。

3. **看见只读 / 看见上次 Commit / 这份副本 is not already 已经交差 interchangeable，也不是已经 QueryState bundled（314） interchangeable / 963 querystate-notlive interchangeable / 962 querystate-notexec interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321/959 snapshot-restore-notdone interchangeable。**  
   官方把只读和已经和正在改的 ExecuteTxState 同步分开。看见只读，不是已经交差 interchangeable。314 querystate vs execute bundled unbundling 在本页 item 2 续。

怎样实现 QueryState、怎样做 state sync、怎样写四门是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **上次 Commit not already live ≠ 已经跟上正在跑的块 interchangeable：** 官方把已提交到盘和还在执行的那份分开。
- **看见能读 not already CheckTxState ≠ 已经是 CheckTxState interchangeable：** 官方把能读和内存池那份 CheckTxState 分开。
- **看见只读 not already settled ≠ 已经交差 interchangeable：** 官方把只读和已经与正在改的 ExecuteTxState 同步分开；314 querystate vs execute bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 上次 Commit | 不是已经跟上正在跑的块 | 不是默认锁已经 RPC 安全（310） |
| 看见能读 | 不是已经是 CheckTxState | 不是 Offer 收下已经装完（321/959） |
| 看见只读 | 不是已经交差 | 不是启动对齐就已经是快照重放（964） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看上次 Commit not already live / not already CheckTxState / not already settled 正式三事（314 余量），必须分开是不是已经跟上正在跑的块、是不是已经是 CheckTxState、是不是已经交差。可以跳过「看见能查就已经是工作状态」。不要另写怎样实现 QueryState 或怎样做 state sync。314 querystate vs execute bundled unbundling 在本页 item 2 续；续 [`worked-example-querystate-notsnap-vs-bundled.md`](worked-example-querystate-notsnap-vs-bundled.md)（不变量 964 item 3）。

## 本页不抄

- 怎样实现 QueryState、怎样做 state sync、怎样写四门。
- QueryState bundled。那是不变量 314。
- 默认锁已经 RPC 安全。那是不变量 310。
- Offer 收下已经装完。那是不变量 321/959。
