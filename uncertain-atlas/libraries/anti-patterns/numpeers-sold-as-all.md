# 反模式：看见 NumPeers 就当成已经数完 / 看见能按名字拿到反应堆就当成已经独立 / 看见 PeerState 就当成已经验过高度

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md)。  
**例**：[NumPeers ≠ 已经数完](../../tracks/network/worked-example-numpeers-vs-all.md)。

## 塌法

1. 看见 NumPeers / 看见 outbound+inbound，就当成已经数完所有邻居。
2. 看见 dialing / 看见正在拨，就当成已经连上，或当成协议层该看。
3. 看见能按名字拿到另一个反应堆 / 看见 Block Sync 能切到 Consensus，就当成已经独立，或当成已经推荐。
4. 看见 Peer 上有 KV / 看见 Consensus 写了 PeerState，就当成 Evidence / Mempool 已经有了已验证的最后高度。

## 为什么会出事

官方写：无条件邻居不进 NumPeers。`dialing` 不该给协议层看。`Switch.Reactor(name)` 违反反应堆独立，应该避免。KV 里的高度是共识反应堆写下的，不是已经验过。

## 和相邻反模式

- [handler-sold-as-node](handler-sold-as-node.md) 是句柄 ≠ 已经是那个人，不是本页这种查询不是已经数完。
- [initpeer-sold-as-added](initpeer-sold-as-added.md) 是 InitPeer ≠ 已经能交互，不是本页。
