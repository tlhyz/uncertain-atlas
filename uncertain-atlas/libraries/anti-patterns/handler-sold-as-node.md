# 反模式：看见 Peer 句柄就当成已经是那个人 / 看见 Broadcast 回了通道就当成已经送到每一家 / 看见 StopPeerForError 就当成已经对持久邻居也断干净

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md)。  
**例**：[Peer 句柄 ≠ 已经是那个人](../../tracks/network/worked-example-peer-handler-vs-node.md)。

## 塌法

1. 看见 Peer 句柄 / 看见又一次 InitPeer，就当成已经是同一个人。
2. 看见 Broadcast 回了通道 / 看见通道里有 bool，就当成已经送到每一家，或当成已经知道是谁。
3. 看见 StopPeerForError / 看见反应堆要踢人，就当成已经对持久邻居也断干净。
4. 看见方法还在，就当成已经是现行该用的广播。
5. 看见理由进了，就当成持久名单已经忘了。

## 为什么会出事

官方写：`Peer` 句柄绑的是这一次连接，不是网上那个节点。Broadcast 回的每个 bool 对不上是哪一个人。对持久邻居，`StopPeerForError` 还会试着重连。

## 和相邻反模式

- [initpeer-sold-as-added](initpeer-sold-as-added.md) 是 InitPeer ≠ 已经能交互，不是本页这种句柄不是人。
- [announce-sold-as-received](announce-sold-as-received.md) 是宣布 ≠ 已经收到，不是本页这种回通道不是送到。
