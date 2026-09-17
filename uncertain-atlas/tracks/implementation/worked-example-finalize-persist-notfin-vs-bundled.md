# 例：看见必须在 Commit 落盘 is not already persisted in Finalize interchangeable / not already unlocked interchangeable / not already settled interchangeable

**层次**：实现 / 必须在 Commit 落盘 not already persisted in Finalize / not already unlocked / not already settled 正式三事（335 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「必须在 Commit 落盘 not already persisted in Finalize / not already unlocked / not already settled 正式三事（335 余量）/ not 903 finalize-persist-notfin interchangeable / not 335 finalize-persist-vs-commit bundled interchangeable」，不是 Finalize 落盘禁令 bundled（335），也不是默认锁已经 RPC 安全（310），也不是 finafter persist 已经 settled（632）。不要另写怎样落盘或怎样写 Commit。

## 官方三件事

1. **看见必须在 `Commit` 落盘 / 看见 `Commit` 前返回 这份落盘 is not already 已经在 Finalize 落了 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 903 finalize-persist-notfin interchangeable / 902 finalize-persist-notdisk interchangeable / 335 finalize-persist item 1 改了状态 interchangeable，也不是已经必须在 Commit 落盘 not already persisted in Finalize / not already unlocked / not already settled 正式三事 bundled（335 item 2 余量） interchangeable / 335 finalize-persist item 2 interchangeable。**  
   官方写：持久化 MUST 在 `Commit` 里做。应用应在 `Commit` 里持久化自己的状态，返回之前做完。看见必须在 Commit 落盘，不是已经在 Finalize 落了 interchangeable——本页从 335 item 2 侧钉 not already persisted in Finalize 单句。335 finalize-persist vs commit bundled unbundling 在本页 item 2 续。

2. **看见返回前写完 / 看见必须在 Commit 落盘 / 这份落盘 is not already 已经解锁 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 903 finalize-persist-notfin interchangeable / 335 finalize-persist item 3 记住高度 interchangeable / 904 finalize-persist-notskip interchangeable，也不是已经默认锁已经 RPC 安全 interchangeable / 310 commit-lock interchangeable。**  
   官方把返回前写完和内存池锁已经放下分开——335 bundled 第二件事常与 310 混成「看见必须在 Commit 落盘就已经解锁或已经能等广播 interchangeable」，本页钉 not already unlocked 单句。

3. **看见 Commit 绿了 / 看见返回前写完 / 这份落盘 is not already 已经交差 interchangeable，也不是已经 Finalize 落盘禁令 bundled（335） interchangeable / 903 finalize-persist-notfin interchangeable / 902 finalize-persist-notdisk interchangeable，也不是已经能在 Commit 里等广播 interchangeable / 310 gossip interchangeable。**  
   官方把 Commit 绿了和已经交差 / 已经能在 Commit 里等广播分开。看见 Commit 绿了，不是已经交差 interchangeable。335 finalize-persist vs commit bundled unbundling 在本页 item 2 续。

怎样落盘、怎样写 `Commit`、怎样做 WAL 旋转是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **必须在 Commit 落盘 not already persisted in Finalize ≠ 已经在 Finalize 落了 interchangeable：** 官方把唯一落盘点和 Finalize 禁令分开。
- **看见返回前写完 not already unlocked ≠ 已经解锁 interchangeable：** 官方把返回前写完和内存池锁已经放下分开。
- **看见 Commit 绿了 not already settled ≠ 已经交差 interchangeable：** 官方把 Commit 绿了和已经交差分开；335 finalize-persist vs commit bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须在 Commit 落盘 | 不是已经在 Finalize 落了 | 不是默认锁已经 RPC 安全（310） |
| 看见返回前写完 | 不是已经解锁 | 不是 finafter persist 已经 settled（632） |
| 看见 Commit 绿了 | 不是已经交差 | 不是 Finalize 改了就已经落盘（902） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须在 Commit 落盘 not already persisted in Finalize / not already unlocked / not already settled 正式三事（335 余量），必须分开是不是已经在 Finalize 落了、是不是已经解锁、是不是已经交差。可以跳过「看见必须在 Commit 落盘就已经在 Finalize 落了」。不要另写怎样落盘或怎样写 Commit。335 finalize-persist vs commit bundled unbundling 在本页 item 2 续；续 [`worked-example-finalize-persist-notskip-vs-bundled.md`](worked-example-finalize-persist-notskip-vs-bundled.md)（不变量 904 item 3）。

## 本页不抄

- 怎样落盘、怎样写 `Commit`、怎样做 WAL 旋转。
- Finalize 落盘禁令 bundled。那是不变量 335。
- Finalize 改了就已经落盘。那是不变量 335 item 1 余量 / 902。
- 默认锁已经 RPC 安全。那是不变量 310。
- finafter persist 已经 settled。那是不变量 632。
