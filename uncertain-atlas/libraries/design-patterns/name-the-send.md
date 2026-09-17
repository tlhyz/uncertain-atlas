# 模式：把对等发送三件事说成三个名字

**层次**：网络 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md)。  
**例**：[HasChannel ≠ 已经入队](../../tracks/network/worked-example-send-vs-enqueued.md)。

## 三个名字

1. **HasChannel 不是已经入队：** 看见对端宣布了通道不是已经入队，也不是已经送到。
2. **Send 回假不是已经断开：** 看见 Send 回了假不是已经断开，也不是已经知道是哪一种理由。
3. **TrySend 不是已经和 Send 同一把尺：** 看见立刻失败不是已经停掉这个人，也不是已经等过同一段时间。

## 为什么要分开叫

官方把有没有通道、能不能进队列、什么时候回假写成三件事。把它们叫成一个「看见能发就已经入队」，会把 Broadcast、NumPeers 和入站配额一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「已经发给对等节点」，先数清问的是 HasChannel 不是已经入队、Send 回假不是已经断开，还是 TrySend 不是已经和 Send 同一把尺，再决定要不要同一次发布。
