# 模式：把 Commit 锁三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[默认锁 ≠ 已经 RPC 安全](../../tracks/implementation/worked-example-commit-lock-vs-rpc.md)。

## 三个名字

1. **默认锁不是已经 RPC 安全：** 看见默认 Go 有全局锁不是已经能把状态直接给 RPC。
2. **Commit 前上锁不是已经解锁：** 看见能一起更新四份状态不是已经和 Commit 同步做完。
3. **Commit 里等广播不是已经能往下走：** 看见调了 broadcast_tx 并等回执不是已经交差。

## 为什么要分开叫

官方把原则上并发、默认全局锁、直接暴露 RPC 可能不安全、Commit 期间握着内存池锁、等广播会停死，写成三件事。把它们叫成一个「看见有锁就已经安全」，会把四条连接、半写原子和内存池交接一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「ABCI 已经接上」，先数清问的是默认锁不是已经 RPC 安全、Commit 前上锁不是已经解锁，还是 Commit 里等广播不是已经能往下走，再决定要不要同一次发布。
