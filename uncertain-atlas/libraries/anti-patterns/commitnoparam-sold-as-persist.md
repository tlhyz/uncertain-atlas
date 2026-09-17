# 反模式：看见 Commit 不带参数就当成已经落盘 / 看见 Echo 回包 Message 是入参那串就当成已经是入参字段 / 看见 Echo 用来测实现就当成已经刷完

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Request / Echo Response / Echo Usage。  
**例**：[Commit 不带参数 ≠ 已经落盘](../../tracks/implementation/worked-example-commitnoparam-vs-persist.md)。

## 塌法

1. 看见 Commit 不带参数 / 看见能叫，就当成已经落盘，或当成已经交差。
2. 看见 Echo 回包 `Message` 是入参那串 / 看见回了 Message，就当成已经是入参字段，或当成已经回显。
3. 看见 Echo 用来测实现 / 看见能测，就当成已经刷完，或当成已经送到。

## 为什么会出事

官方写：Commit 不带参数。回包 `Message` 是入参那串。Echo 用来测 ABCI 客户端/服务端实现。

## 和相邻反模式

- [finalizepersist-sold-as-committed](finalizepersist-sold-as-committed.md) 是 Finalize 改了就已经落盘，不是本页这种 Commit 不带参数不是已经落盘。
- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 Echo 请求 Message 就已经是 Flush，不是本页这种 Echo 回包 Message 是入参那串不是已经是入参字段。
- [flush-sold-as-sent](flush-sold-as-sent.md) 是 Flush 要把客户端排队的消息冲到服务端就已经送到，不是本页这种 Echo 用来测实现不是已经刷完。
