# 例：看见默认 Go 有全局锁 / 四条连接原则上并发 is not already already RPC safe interchangeable / already no concurrency interchangeable / already changed lock interchangeable

**层次**：实现 / default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事（310 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事（310 余量）/ not 689 commitlock-notrpcsafe interchangeable / not 310 commitlock bundled interchangeable」，不是 Commit lock vs RPC bundled（310），也不是 Commit 前上锁不是已经解锁（690 item 2 余量）或 Commit 里等广播不是已经能往下走（691 item 3 余量）。不要另写怎样加锁、怎样调广播、怎样写四门。

## 官方三件事

规范把 Requirements 里原则上四条 ABCI 连接彼此并发、默认同进程客户端和默认 Go 套接字服务器都用一把全局锁所以**一点也不并发**、直接把应用状态暴露给 RPC 可能不安全、除非另有措施查询都应走 ABCI `Query` 和「已经是有锁就已经能直接给 RPC 读 interchangeable / 已经是默认顺序收就已经没有并发假设 interchangeable / 已经是编进同一个二进制就已经换了这把锁 interchangeable / 已经是 Commit lock vs RPC bundled interchangeable」分开写成三件独立的实现事，不是「看见有锁 就已经 RPC 安全 interchangeable / 就已经没有并发 interchangeable / 就已经换了锁 interchangeable」一件事：

1. **看见默认 Go 有全局锁 / 看见四条连接原则上并发 / 看见有锁 is not already 已经能把状态直接给 RPC interchangeable / 已经 RPC 安全 interchangeable / 已经能直接给 RPC 读 interchangeable / 310 commitlock bundled interchangeable / 307 conn-sold-as-gates interchangeable / 33 four gates interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 689 commitlock-notrpcsafe interchangeable / 310 commitlock item 1 interchangeable，也不是已经 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事 bundled（310 item 1 余量） interchangeable / 310 commitlock item 1 interchangeable，也不是已经 Commit 前上锁不是已经解锁（690） interchangeable / 691 commitlock-notbroadcast interchangeable / 588 finlock interchangeable，也不是已经一条连接已经是四门（307） interchangeable / conn-sold-as-gates interchangeable。**  
   官方写：原则上四条 ABCI 连接彼此并发，应用必须保证状态线程安全。默认同进程客户端和默认 Go 套接字服务器都用一把全局锁。**直接把应用状态暴露给 RPC 可能不安全**；除非另有措施，查询都应走 ABCI `Query`。看见有锁，不是已经能直接给 RPC 读 interchangeable——310 钉 bundled 三事，本页从 item 1 侧钉 not already RPC safe 单句。看见默认全局锁，不是已经一条连接已经是四门（307） interchangeable——307 钉连接 vs 四门，本页钉 RPC 暴露边界单句。看见原则上并发，不是已经 Commit lock vs RPC bundled（310） interchangeable——310 钉 bundled，本页钉 item 1 第一件事。310 commitlock vs RPC bundled unbundling 在本页 item 1 启动。

2. **看见默认顺序收 / 看见所有连接的 ABCI 消息按顺序一次一条 / 看见一点也不并发 is not already 已经没有并发假设 interchangeable / 已经 no concurrency interchangeable / 已经原则上并发已经取消 interchangeable / 310 commitlock bundled interchangeable / 307 conn interchangeable / 309 send interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 689 commitlock-notrpcsafe interchangeable / 310 commitlock item 2 Commit 前上锁 interchangeable / 310 commitlock item 3 Commit 里等广播 interchangeable，也不是已经 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事 bundled（310 item 1 余量） interchangeable / 310 commitlock item 1 interchangeable，也不是已经应用必须保证状态线程安全已经不需要 interchangeable / 已经四条连接彼此并发假设已经关掉 interchangeable。**  
   官方把默认一点也不并发 / 按顺序一次一条 和已经没有并发假设路径分开——原则上四条连接彼此并发，应用必须保证状态线程安全；默认实现一点也不并发，不等于原则上并发假设已经取消。看见默认顺序收，不是已经没有并发假设 interchangeable——本页钉 not already no concurrency 单句。看见一点也不并发，不是已经 Commit 前上锁不是已经解锁（690） interchangeable——690 另钉 item 2，本页钉 item 1 第二件事。看见按顺序一次一条，不是已经 Commit 里等广播不是已经能往下走（691） interchangeable——691 另钉 item 3，本页钉 item 1 第二件事。310 commitlock vs RPC bundled unbundling 在本页 item 1 启动。

3. **看见编进同一个二进制 / 看见默认同进程客户端 / 看见默认 Go 套接字服务器 is not already 已经换了这把锁 interchangeable / 已经 changed lock interchangeable / 已经另有措施 interchangeable / 310 commitlock bundled interchangeable / 307 conn interchangeable，也不是已经 Commit lock vs RPC bundled（310） interchangeable / 689 commitlock-notrpcsafe interchangeable / 310 commitlock item 2 / 310 commitlock item 3，也不是已经 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事 bundled（310 item 1 余量） interchangeable / 310 commitlock item 1 interchangeable，也不是已经 Go 应用把读写都走 ABCI 就已经能直接给 RPC 读 interchangeable / 已经靠这把锁得到线程安全就已经 RPC 安全 interchangeable。**  
   官方把默认同进程 / 默认 Go 套接字服务器用一把全局锁 和编进同一个二进制就已经换了这把锁路径分开——Go 应用若把读写都走 ABCI，可以靠这把锁得到线程安全，不等于已经能直接给 RPC 读，也不等于已经另有措施换了锁。看见编进同一个二进制，不是已经换了这把锁 interchangeable——本页钉 not already changed lock 单句。看见默认同进程客户端，不是已经 RPC 安全（本页第一件事） interchangeable——三件事分开钉。看见默认 Go 套接字服务器，不是已经一条连接已经是四门（307） interchangeable——307 另钉。310 commitlock vs RPC bundled unbundling 在本页 item 1 完成。

怎样加锁、怎样调广播、怎样写四门是规范里的做法，本页不抄。Commit lock vs RPC bundled（310）、Commit 前上锁不是已经解锁（310 item 2 余量 / 690）、Commit 里等广播不是已经能往下走（310 item 3 余量 / 691）、一条连接已经是四门（307）、半写已经原子（5）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **default global lock not already RPC safe ≠ 307 / 310 bundled interchangeable：** 官方把有锁单句和已经能直接给 RPC 读路径分开。
- **默认顺序收 not already no concurrency ≠ 原则上并发已经取消 interchangeable：** 官方把默认一点也不并发单句和已经没有并发假设路径分开。
- **编进同一个二进制 not already changed lock ≠ 已经另有措施 interchangeable：** 官方把默认锁单句和已经换了这把锁路径分开；310 commitlock vs RPC bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 默认 Go 全局锁 | 不是 already RPC safe | 不是一条连接已经是四门（307） |
| 默认顺序收 | 不是 already no concurrency | 不是 Commit 前上锁 alone（690） |
| 编进同一个二进制 | 不是 already changed lock | 不是 Commit 里等广播 alone（691） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事（310 余量），必须分开有锁 是不是 already RPC safe interchangeable / 310 commitlock bundled interchangeable / 307 conn-sold-as-gates interchangeable、默认顺序收 是不是 already no concurrency interchangeable / 原则上并发已经取消 interchangeable、编进同一个二进制 是不是 already changed lock interchangeable / 已经另有措施 interchangeable。可以跳过「看见有锁 就已经能直接给 RPC 读 interchangeable / 就已经没有并发 interchangeable / 就已经换了锁 interchangeable」。不要另写怎样加锁。310 commitlock vs RPC bundled unbundling 在本页 item 1 完成；续 [`worked-example-commitlock-notunlocked-vs-bundled.md`](worked-example-commitlock-notunlocked-vs-bundled.md)（不变量 690 item 2）。

## 本页不抄

- 怎样加锁、怎样调广播、怎样写四门。
- Commit lock vs RPC bundled。那是不变量 310。
- Commit 前上锁不是已经解锁。那是不变量 310 item 2 余量 / 690。
- Commit 里等广播不是已经能往下走。那是不变量 310 item 3 余量 / 691。
- 一条连接已经是四门。那是不变量 307。
- 半写已经原子。那是不变量 5。
- 四门已经结算。那是不变量 33。
