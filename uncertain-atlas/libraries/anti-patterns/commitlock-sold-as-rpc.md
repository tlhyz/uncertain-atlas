# 反模式：看见默认 Go 有全局锁就当成已经能把状态直接给 RPC / 看见 Commit 前锁了内存池就当成已经解锁 / 看见 Commit 里等 broadcast_tx 就当成已经能往下走

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[默认锁 ≠ 已经 RPC 安全](../../tracks/implementation/worked-example-commit-lock-vs-rpc.md)。

## 塌法

1. 看见四条连接原则上并发 / 看见默认 Go 有全局锁，就当成已经能把状态直接给 RPC，或当成已经没有并发。
2. 看见 Commit 前锁了内存池 / 看见能一起更新四份状态，就当成已经解锁，或当成已经和 Commit 同步做完。
3. 看见 Commit 里调了 broadcast_tx 并等回执，就当成已经能往下走，或当成已经交差。

## 为什么会出事

官方写：默认同进程客户端和默认 Go 套接字服务器用一把全局锁，一点也不并发；直接把状态暴露给 RPC 可能不安全。Commit 前锁内存池，解锁在为新块更新完之后，而且和 Commit 异步。Commit 里等广播回执会停死。

## 和相邻反模式

- [conn-sold-as-gates](conn-sold-as-gates.md) 是一条连接 ≠ 已经是四门，不是本页这种锁不是已经 RPC 安全。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是 CheckTx ≠ 已经进提案，不是本页。
