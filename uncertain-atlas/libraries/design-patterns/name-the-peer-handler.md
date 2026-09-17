# 模式：把对等句柄三件事说成三个名字

**层次**：网络 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md)。  
**例**：[Peer 句柄 ≠ 已经是那个人](../../tracks/network/worked-example-peer-handler-vs-node.md)。

## 三个名字

1. **句柄不是人：** 看见 Peer 句柄不是已经是那个人。
2. **回通道不是送到：** 看见 Broadcast 回了通道不是已经送到每一家。
3. **踢了还会来：** 看见 StopPeerForError 不是已经对持久邻居也断干净。

## 为什么要分开叫

官方把连接句柄和网上身份、Broadcast 返回值和送到、反应堆要踢和持久重连写成三件事。把它们叫成一个「看见句柄就已经是那个人」，会把 InitPeer 时序和入站配额一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「对等节点已经齐」，先数清问的是句柄不是人、回通道不是送到，还是踢了还会来，再决定要不要同一次发布。
