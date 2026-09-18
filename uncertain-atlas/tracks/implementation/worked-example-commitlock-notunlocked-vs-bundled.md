# 例：看见 Commit 前锁了内存池 / 能一起更新四份状态 is not already already unlocked interchangeable / already sync done interchangeable / Commit return already released interchangeable

**层次**：实现 / lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事（310 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事（310 余量）/ not 690 commitlock-notunlocked interchangeable / not 310 commitlock bundled interchangeable」，不是 Commit lock vs RPC bundled（310），也不是 default global lock not already RPC safe（689 item 1 余量）或 Commit 里等广播不是已经能往下走（691 item 3 余量）。不要另写怎样加锁、怎样冲内存池、怎样写四门。

## 官方三件事

规范把 Requirements 里调用 `Commit` 之前会锁内存池并冲掉内存池连接、好同时把四条连接的状态更新到最新已提交、在为新块更新完之后才解锁而且这次更新和 `Commit` **异步** 和「已经是锁上了就已经解锁 interchangeable / 已经是能一起更新就已经更新完 interchangeable / 已经是 Commit 回了就已经按同一条路径放下锁 interchangeable / 已经是 Commit lock vs RPC bundled interchangeable」分开写成三件独立的实现事，不是「看见锁上了 就已经解锁 interchangeable / 就已经同步做完 interchangeable / 就已经放下锁 interchangeable」一件事：

1. **看见 Commit 前锁了内存池 / 看见锁上了 / 看见冲掉内存池连接 is not already 已经解锁 interchangeable / 已经 unlocked interchangeable / 已经和 Commit 同步做完 interchangeable / 310 commitlock bundled interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable / 646 fincommit-notcommitlock interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 690 commitlock-notunlocked interchangeable / 310 commitlock item 2 interchangeable，也不是已经 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事 bundled（310 item 2 余量） interchangeable / 310 commitlock item 2 interchangeable，也不是已经 default global lock not already RPC safe（689） interchangeable / 691 commitlock-notbroadcast interchangeable / 403 finafter interchangeable，也不是已经 Finalize When locks mempool 已经交差（588） interchangeable / finlock-sold-as-settled interchangeable。**  
   官方写：调用 `Commit` 之前，CometBFT 会锁内存池并冲掉内存池连接，保证这一步收不到新的内存池消息。看见锁上了，不是已经解锁 interchangeable——310 钉 bundled 三事，本页从 item 2 侧钉 not already unlocked 单句。看见冲掉内存池连接，不是已经 Finalize When locks mempool 已经交差（588） interchangeable——588 钉 Finalize 锁 vs 交差，本页钉 Commit 前上锁单句。看见 Commit 前锁了内存池，不是已经 Commit lock vs RPC bundled（310） interchangeable——310 钉 bundled，本页钉 item 2 第一件事。310 commitlock vs RPC bundled unbundling 在本页 item 2 启动。

2. **看见能一起更新四份状态 / 看见同时把四条连接的状态更新到最新已提交 / 看见好一起更新 is not already 已经更新完 interchangeable / 已经 sync done interchangeable / 已经和 Commit 同步做完 interchangeable / 310 commitlock bundled interchangeable / 5 half-write atomic interchangeable / 301 proposed-removed interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 690 commitlock-notunlocked interchangeable / 310 commitlock item 1 RPC safe interchangeable / 310 commitlock item 3 broadcast interchangeable，也不是已经 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事 bundled（310 item 2 余量） interchangeable / 310 commitlock item 2 interchangeable，也不是已经四门已经结算（33） interchangeable / 403 finafter interchangeable / 已提交状态已经换完 interchangeable。**  
   官方把锁内存池好一起更新四份状态 和已经更新完 / 已经和 Commit 同步做完路径分开——锁上是为了这一步收不到新消息并一起更新，不等于更新已经做完，也不等于和 `Commit` 同步做完。看见能一起更新，不是已经更新完 interchangeable——本页钉 not already sync done 单句。看见四条连接状态更新到最新已提交，不是已经 default global lock not already RPC safe（689） interchangeable——689 另钉 item 1，本页钉 item 2 第二件事。看见好一起更新，不是已经 Commit 里等广播不是已经能往下走（691） interchangeable——691 另钉 item 3，本页钉 item 2 第二件事。310 commitlock vs RPC bundled unbundling 在本页 item 2 启动。

3. **看见 Commit 回了 / 看见 Commit 返回 / 看见应用 Commit 绿了 is not already 已经按同一条路径放下锁 interchangeable / 已经 Commit return already released interchangeable / 已经异步解锁已经做完 interchangeable / 310 commitlock bundled interchangeable / 592 finunlock interchangeable / 646 fincommit-notcommitlock interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 690 commitlock-notunlocked interchangeable / 310 commitlock item 1 / 310 commitlock item 3，也不是已经 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事 bundled（310 item 2 余量） interchangeable / 310 commitlock item 2 interchangeable，也不是已经更新和 Commit 已经同步 interchangeable / 已经内存池锁已经能给 broadcast_tx 用 interchangeable。**  
   官方把为新块更新完之后才解锁、而且这次更新和 `Commit` **异步** 和 Commit 回了就已经按同一条路径放下锁路径分开——`Commit` 返回不等于内存池锁已经放下，也不等于异步解锁已经和返回同路径做完。看见 Commit 回了，不是已经放下锁 interchangeable——本页钉 not Commit return already released 单句。看见 Commit 绿了，不是已经解锁（本页第一件事） interchangeable——三件事分开钉。看见应用 Commit 返回，不是已经能在 Commit 里等 broadcast_tx（691） interchangeable——691 另钉停死警告，本页钉 item 2 第三件事。310 commitlock vs RPC bundled unbundling 在本页 item 2 完成。

怎样加锁、怎样冲内存池、怎样写四门是规范里的做法，本页不抄。Commit lock vs RPC bundled（310）、default global lock not already RPC safe（310 item 1 余量 / 689）、Commit 里等广播不是已经能往下走（310 item 3 余量 / 691）、Finalize When locks mempool（588）、半写已经原子（5）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **lock before Commit not already unlocked ≠ 588 / 592 interchangeable：** 官方把锁上了单句和已经解锁 / Finalize 锁已经交差路径分开。
- **能一起更新 not already sync done ≠ 已经和 Commit 同步做完 interchangeable：** 官方把一起更新意图单句和已经更新完路径分开。
- **Commit 回了 not Commit return already released ≠ 异步解锁已经同路径 interchangeable：** 官方把 Commit 返回单句和放下锁路径分开；310 commitlock vs RPC bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Commit 前锁内存池 | 不是 already unlocked | 不是 default lock alone（689） |
| 能一起更新四份状态 | 不是 already sync done | 不是半写已经原子（5） |
| Commit 回了 | 不是 Commit return already released | 不是 Commit 里等广播 alone（691） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 lock mempool before Commit not already unlocked / not already sync done / not Commit return already released 正式三事（310 余量），必须分开锁上了 是不是 already unlocked interchangeable / 310 commitlock bundled interchangeable / 588 finlock interchangeable、能一起更新 是不是 already sync done interchangeable / 已经和 Commit 同步做完 interchangeable、Commit 回了 是不是 already released interchangeable / 异步解锁已经同路径 interchangeable。可以跳过「看见锁上了 就已经解锁 interchangeable / 就已经同步做完 interchangeable / 就已经放下锁 interchangeable」。不要另写怎样加锁。310 commitlock vs RPC bundled unbundling 在本页 item 2 完成；续 [`worked-example-commitlock-notbroadcast-vs-bundled.md`](worked-example-commitlock-notbroadcast-vs-bundled.md)（不变量 691 item 3）。

## 本页不抄

- 怎样加锁、怎样冲内存池、怎样写四门。
- Commit lock vs RPC bundled。那是不变量 310。
- default global lock not already RPC safe。那是不变量 310 item 1 余量 / 689。
- Commit 里等广播不是已经能往下走。那是不变量 310 item 3 余量 / 691。
- Finalize When locks mempool。那是不变量 588。
- 半写已经原子。那是不变量 5。
- 四门已经结算。那是不变量 33。
