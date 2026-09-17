# 例：看见 MUST persist in Commit / before returning from Commit is not already already persisted in Finalize interchangeable / already unlocked interchangeable / Commit green can wait for broadcast interchangeable

**层次**：实现 / MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事（335 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) FinalizeBlock / Commit。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事（335 余量）/ not 684 finpersist-notmustincommit interchangeable / not 335 finpersist-vs-commit bundled interchangeable」，不是 FinalizeBlock 落盘禁令 bundled（335），也不是 FinalizeBlock changed state MUST NOT persist（683 item 1 余量）或默认锁已经 RPC 安全 bundled（310）。不要另写怎样落盘、怎样写 Commit、怎样做 WAL 旋转。

## 官方三件事

规范把 Requirements 里持久化 **MUST** 在 `Commit` 里做、应用应在 `Commit` 里持久化自己的状态 **返回之前** 做完 和「已经是已经在 Finalize 落了 interchangeable / 已经是内存池锁已经放下 interchangeable / 已经是 Commit 绿了就能在 Commit 里等广播 interchangeable / 已经 Signal persist interchangeable」分开写成三件独立的实现事，不是「看见必须在 Commit 落盘 就已经在 Finalize 落了 interchangeable / 就已经解锁 interchangeable / 就已经 Commit 绿了 interchangeable」一件事：

1. **看见持久化 MUST 在 `Commit` 里做 / 看见必须在 Commit 落盘 / 看见应用应在 Commit 里持久化自己的状态 before returning from Commit is not already 已经在 Finalize 落了 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable / 683 finpersist-notmustnot interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable / 680 commitpersist-notfinpersist interchangeable / 481 commitpersist item 1 persist signal interchangeable / 335 finpersist bundled interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 684 finpersist-notmustincommit interchangeable / 335 finpersist-vs-commit bundled interchangeable / 335 finpersist item 2 interchangeable，也不是已经 MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事 bundled（335 item 2 余量） interchangeable / 335 finpersist item 2 interchangeable，也不是已经 Signal the Application to persist application state（481） interchangeable / 645 fincommit-notpersist interchangeable / 497 infousage-persist interchangeable / 467 finpersist interchangeable，也不是已经 Application is expected to persist at end of this call（681） interchangeable / 399 commit-empty-echo bundled interchangeable。**  
   官方 Requirements 写：持久化 **MUST** 在 `Commit` 里做。应用应在 `Commit` 里持久化自己的状态，**返回之前** 做完。看见必须在 Commit 落盘，不是已经在 Finalize 落了 interchangeable——683 钉 MUST NOT persist in Finalize 单句，本页从 335 item 2 侧钉 not already persisted in Finalize 单句。看见 before returning from Commit，不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable——335 钉 bundled 三事，本页钉 MUST persist in Commit 单句。看见 MUST persist in Commit，不是已经 When instruct Application to persist its state（645） interchangeable——645 另钉 When 第 8 步，本页钉 item 2 第一件事。335 finpersist vs commit bundled unbundling 在本页 item 2 启动。

2. **看见 MUST persist in Commit / 看见返回前写完 / 看见 before returning from Commit is not already 已经解锁 interchangeable / 已经内存池锁已经放下 interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable / 310 commit-lock-vs-rpc interchangeable / 629 notsettled interchangeable / 630 notoptional interchangeable / 646 fincommit-notcommitlock interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 684 finpersist-notmustincommit interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable / 335 finpersist item 3 remember last Commit height interchangeable，也不是已经 MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事 bundled（335 item 2 余量） interchangeable / 335 finpersist item 2 interchangeable，也不是已经 When 第 8 步 calls Commit after lock mempool not Commit lock bundled（590 item 3 余量 / 646） interchangeable / 646 fincommit-notcommitlock interchangeable / 631 notcommitlock interchangeable / 403 finafter item 2 interchangeable，也不是已经 Finalize 之后 optional recheck unlock h+1 not Recheck bundled（403 item 3 余量 / 634） interchangeable / 634 notrecheck interchangeable / 591 finrecheck interchangeable / 593 finh1 interchangeable，也不是已经 locks mempool not settled bundled（588 item 1 余量 / 629） interchangeable / 629 notsettled interchangeable / 632 notsettled interchangeable。**  
   官方把 MUST persist in Commit 单句和内存池锁已经放下 / 已经解锁 路径分开——335 bundled 第二件事常与 588 / 310 混成「看见必须在 Commit 落盘 就已经解锁 interchangeable / 就已经内存池锁已经放下 interchangeable / 就已经 When 第 7 步锁完 interchangeable」，本页钉 not already unlocked 单句。看见返回前写完，不是已经 locks the mempool（588 When 第 7 步） interchangeable——588 钉 When 锁内存池，本页钉 Requirements MUST persist in Commit 单句。看见 before returning from Commit，不是已经 optional recheck unlock h+1（634） interchangeable——634 另钉 403 item 3，本页钉 item 2 第二件事。335 finpersist vs commit bundled unbundling 在本页 item 2 启动。

3. **看见 MUST persist in Commit / 看见 Commit 前返回 / 看见 before returning from Commit is not already Commit 绿了就能在 Commit 里等广播 interchangeable / 已经 Commit 里等广播 interchangeable / 已经默认锁已经 RPC 安全 interchangeable / 310 commit-lock-vs-rpc interchangeable / 310 commitlock interchangeable / 588 finlock interchangeable / 481 commitpersist interchangeable / 681 commitpersist-notendofcall interchangeable / 399 commit-empty-echo bundled interchangeable，也不是已经 FinalizeBlock 落盘禁令 bundled（335） interchangeable / 684 finpersist-notmustincommit interchangeable / 335 finpersist item 1 MUST NOT persist in Finalize interchangeable / 335 finpersist item 3 remember last Commit height interchangeable，也不是已经 MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事 bundled（335 item 2 余量） interchangeable / 335 finpersist item 2 interchangeable，也不是已经 Signal the Application to persist application state bundled（481 item 1 余量 / 680） interchangeable / 680 commitpersist-notfinpersist interchangeable / 645 fincommit-notpersist interchangeable / 497 infousage-persist interchangeable，也不是已经 Commit 空请求 bundled（399） interchangeable / 399 commitnoparam interchangeable / 492 echousage bundled interchangeable / 673 flushusage-notimmediatesync interchangeable，也不是已经记住上次成功 Commit 高度 bundled（335 item 3 余量 / 685 余量） interchangeable / 685 finpersist-notrememberheight interchangeable / 320 crash recovery interchangeable。**  
   官方把 MUST persist in Commit 单句和 Commit 绿了就能等广播 / 默认锁已经 RPC 安全 / Signal persist 路径分开——335 bundled 第二件事常与 310 / 481 混成「看见必须在 Commit 落盘 就已经 Commit 绿了 interchangeable / 就已经能在 Commit 里等广播 interchangeable / 就已经 Signal persist interchangeable」，本页钉 not Commit green can wait for broadcast 单句。看见 Commit 前返回，不是已经默认锁已经 RPC 安全（310） interchangeable——310 钉 Commit 锁与 RPC，本页钉 MUST persist in Commit 单句。看见 before returning from Commit，不是已经 Application is expected to persist at end of this call（681） interchangeable——681 另钉 Commit Usage expected persist at end，本页钉 item 2 第三件事。335 finpersist vs commit bundled unbundling 在本页 item 2 完成。

怎样落盘、怎样写 Commit、怎样做 WAL 旋转是规范里的做法，本页不抄。FinalizeBlock 落盘禁令 bundled（335）、FinalizeBlock changed state MUST NOT persist（335 item 1 余量 / 683）、记住上次成功 Commit 高度 not already can skip steps（335 item 3 余量 / 685）、Signal persist application state not Finalize already persisted（481 item 1 余量 / 680）、默认锁已经 RPC 安全 bundled（310）、locks mempool not settled（588）、FinalizeBlock When instruct persist（590 / 645）、Commit Usage persist signal bundled（481）、崩溃恢复三步已经交差（320）是另外那套，本页不抄。

## 官方为什么这样拆

- **MUST persist in Commit not already persisted in Finalize ≠ 683 finpersist-notmustnot interchangeable：** 官方把 Requirements MUST persist in Commit 单句和 MUST NOT persist in Finalize 路径分开。
- **MUST persist in Commit not already unlocked ≠ 588 finlock / 310 commitlock interchangeable：** 官方把 MUST persist in Commit 单句和内存池锁已经放下 / 已经解锁 路径分开。
- **MUST persist in Commit not Commit green can wait for broadcast ≠ 310 commit-lock-vs-rpc interchangeable：** 官方把 MUST persist in Commit 单句和 Commit 绿了就能等广播 / Signal persist 路径分开；335 finpersist vs commit bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MUST persist in Commit | 不是 already persisted in Finalize（683/335 item 1） | 不是 Signal persist alone（481/680） |
| before returning from Commit | 不是 already unlocked（588/592/310） | 不是 When lock mempool alone（588 item 1） |
| 必须在 Commit 落盘 | 不是 Commit green can wait for broadcast（310） | 不是 remember last Commit height（685/335 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MUST persist in Commit not already persisted in Finalize / not already unlocked / not Commit green can wait for broadcast 正式三事（335 余量），必须分开 MUST persist in Commit 是不是 already persisted in Finalize interchangeable / 683 finpersist-notmustnot interchangeable / 680 commitpersist-notfinpersist interchangeable / 481 commitpersist interchangeable、返回前写完 是不是 already unlocked interchangeable / 588 finlock interchangeable / 592 finunlock interchangeable / 310 commitlock interchangeable / 646 fincommit-notcommitlock interchangeable、Commit 前返回 是不是 Commit green can wait for broadcast interchangeable / 310 commit-lock-vs-rpc interchangeable / 681 commitpersist-notendofcall interchangeable / 399 commit-empty-echo bundled interchangeable。可以跳过「看见必须在 Commit 落盘 就已经在 Finalize 落了 interchangeable / 就已经解锁 interchangeable / 就已经 Commit 绿了 interchangeable」。不要另写怎样落盘。335 finpersist vs commit bundled unbundling 在本页 item 2 完成；续 [`worked-example-finpersist-notrememberheight-vs-bundled.md`](worked-example-finpersist-notrememberheight-vs-bundled.md)（不变量 685 item 3）。

## 本页不抄

- 怎样落盘、怎样写 Commit、怎样做 WAL 旋转。
- FinalizeBlock 落盘禁令 bundled。那是不变量 335。
- FinalizeBlock changed state MUST NOT persist。那是不变量 335 item 1 余量 / 683。
- 记住上次成功 Commit 高度 not already can skip steps。那是不变量 335 item 3 余量 / 685。
- Signal persist application state not Finalize already persisted。那是不变量 481 item 1 余量 / 680。
- 默认锁已经 RPC 安全 bundled。那是不变量 310。
- FinalizeBlock When instruct persist。那是不变量 590 / 645。
- 崩溃恢复三步已经交差。那是不变量 320。
