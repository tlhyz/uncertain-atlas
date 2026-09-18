# 模式：把 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事（310 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[default global lock not already RPC safe ≠ bundled（310）](../../tracks/implementation/worked-example-commitlock-notrpcsafe-vs-bundled.md)。

## 三个名字

1. **有锁 不是 already RPC safe：** 看见默认 Go 有全局锁 / 四条连接原则上并发，不是已经能把状态直接给 RPC interchangeable / 已经能直接给 RPC 读 interchangeable，不是 310 commitlock bundled interchangeable / 307 conn-sold-as-gates interchangeable。

2. **默认顺序收 不是 already no concurrency：** 看见所有连接的 ABCI 消息按顺序一次一条 / 一点也不并发，不是已经没有并发假设 interchangeable / 已经原则上并发已经取消 interchangeable，不是 310 commitlock item 2 interchangeable / 690 commitlock-notunlocked interchangeable。

3. **编进同一个二进制 不是 already changed lock：** 看见默认同进程客户端 / 默认 Go 套接字服务器，不是已经换了这把锁 interchangeable / 已经另有措施 interchangeable，不是 310 commitlock item 3 interchangeable / 691 commitlock-notbroadcast interchangeable。

官方把默认全局锁单句、already RPC safe、already no concurrency、already changed lock 写成三个名字。把它们叫成一个「看见有锁 就已经能直接给 RPC 读 interchangeable / 就已经没有并发 interchangeable / 就已经换了锁 interchangeable」，会把 not already RPC safe、not already no concurrency、not already changed lock 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 default global lock not already RPC safe / not already no concurrency / not already changed lock 正式三事（310 余量），先数清问的是有锁 是不是 already RPC safe / 310 / 307，是不是默认顺序收 是不是 already no concurrency，还是编进同一个二进制 是不是 already changed lock，再决定要不要同一次发布。310 commitlock vs RPC bundled unbundling 在本页 item 1 完成。
