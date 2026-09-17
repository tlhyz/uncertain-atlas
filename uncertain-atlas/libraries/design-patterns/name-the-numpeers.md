# 模式：把反应堆查询三件事说成三个名字

**层次**：网络 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md)。  
**例**：[NumPeers ≠ 已经数完](../../tracks/network/worked-example-numpeers-vs-all.md)。

## 三个名字

1. **NumPeers 不是已经数完：** 看见 outbound+inbound 不是已经数完所有邻居，也不是已经把正在拨的人算进已连接。
2. **按名字拿到不是已经独立：** 看见能按名字拿到另一个反应堆不是已经该当推荐路径。
3. **PeerState 不是已经验过高度：** 看见 Consensus 写了 PeerState 不是已经 Evidence / Mempool 已经有了已验证的最后高度。

## 为什么要分开叫

官方把无条件邻居不进 NumPeers、dialing 不给协议层、反应堆互相拿应避免、KV 里的高度只是共识反应堆写下的，写成三件事。把它们叫成一个「看见能问就已经数完」，会把句柄、InitPeer 时序和入站配额一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「对等节点已经齐」，先数清问的是 NumPeers 不是已经数完、按名字拿到不是已经独立，还是 PeerState 不是已经验过高度，再决定要不要同一次发布。
