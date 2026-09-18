# 反模式：把 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事（310 余量）说成已经能直接给 RPC 读 / 已经没有并发 / 已经换了锁

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[default global lock not already RPC safe ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notrpcsafe-vs-bundled.md)。

## 卖法

把默认 Go 有全局锁 / 四条连接原则上并发 / 有锁 写成已经能把状态直接给 RPC interchangeable / 已经 RPC 安全 interchangeable / 已经能直接给 RPC 读 interchangeable / 310 commitlock bundled interchangeable / 307 conn-sold-as-gates interchangeable；把默认顺序收 / 一点也不并发 / 按顺序一次一条 写成已经没有并发假设 interchangeable / 已经原则上并发已经取消 interchangeable；把编进同一个二进制 / 默认同进程客户端 / 默认 Go 套接字服务器 写成已经换了这把锁 interchangeable / 已经另有措施 interchangeable，或已经和 310 commitlock bundled / commitlock-sold-as-rpc interchangeable / 689 commitlock-notrpcsafe interchangeable。

## 为什么错

官方把默认全局锁单句、already RPC safe、already no concurrency、already changed lock 写成三件独立的实现事。把它们卖成 already RPC safe interchangeable / already no concurrency interchangeable / already changed lock interchangeable，会把 not already RPC safe、not already no concurrency、not already changed lock 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事（310 余量），必须分开 not already RPC safe、not already no concurrency、not already changed lock 三件事，不要和 310 / 307 / 690 / 691 / 33 / 588 糊成一句。

## 和相邻反模式

- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit lock vs RPC bundled 全段，不是本页 default global lock item 1 单句边界。
- [conn-sold-as-gates](conn-sold-as-gates.md) 是一条连接 ≠ 已经是四门（307），不是本页有锁 ≠ 已经 RPC 安全边界。
- [finlock-sold-as-settled](finlock-sold-as-settled.md) 是 Finalize When locks mempool ≠ 已经交差（588），不是本页默认全局锁 vs RPC 边界。
