# 反模式：看见 Flush 要把客户端排队的消息冲到服务端就当成已经送到 / 看见定期 Flush 是为了让异步请求真发出去就当成已经是四门 / 看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步就当成已经能往下走

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[Flush 要把客户端排队的消息冲到服务端 ≠ 已经送到](../../tracks/implementation/worked-example-flush-vs-sent.md)。

## 塌法

1. 看见 Flush 要把客户端排队的消息冲到服务端 / 看见叫了 Flush，就当成已经送到，或当成已经入队。
2. 看见定期 Flush 是为了让异步请求真发出去 / 看见定期在冲，就当成已经是四门，或当成已经交差。
3. 看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步 / 看见立刻叫了，就当成已经能往下走，或当成已经 Commit。

## 为什么会出事

官方写：Flush 表示客户端排队的消息该冲到服务端。客户端实现会定期叫 Flush，好让异步请求真的发出去。立刻叫 Flush 是为了做成同步请求；Flush 回包回来，这次同步才算完。

## 和相邻反模式

- [flushusage-sold-as-echo](flushusage-sold-as-echo.md) 是 Flush Usage 正式三事就等于 Echo 测 implementation，不是本页 Flush bundled 就等于已经送到。
- [send-sold-as-enqueued](send-sold-as-enqueued.md) 是 HasChannel 就已经入队，不是本页这种 Flush 要把客户端排队的消息冲到服务端不是已经送到。
- [conn-sold-as-gates](conn-sold-as-gates.md) 是一条连接就已经是四门，不是本页这种定期 Flush 是为了让异步请求真发出去不是已经是四门。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 里等广播就已经能往下走，不是本页这种立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走。
