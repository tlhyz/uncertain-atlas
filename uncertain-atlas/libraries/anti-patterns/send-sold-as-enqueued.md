# 反模式：看见 HasChannel 为真就当成已经入队 / 看见 Send 回了假就当成已经断开 / 看见 TrySend 回了假就当成已经和 Send 同一把尺

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[API for Reactors](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/p2p-api.md)。  
**例**：[HasChannel ≠ 已经入队](../../tracks/network/worked-example-send-vs-enqueued.md)。

## 塌法

1. 看见 HasChannel 为真 / 看见对端宣布了通道，就当成已经入队，或当成已经送到。
2. 看见 Send 回了假 / 看见阻塞过，就当成已经断开，或当成已经知道是哪一种理由。
3. 看见 TrySend 回了假 / 看见立刻失败，就当成已经停掉这个人，或当成已经和 Send 同一把尺。
4. 看见回了假，就当成已经送到，或当成已经是 Broadcast 那条通道。

## 为什么会出事

官方写：HasChannel 只测对端有没有这条通道。Send / TrySend 回的是能不能进发送队列。回假最常见是队列满，也可以是人已经停、通道未登记、或编载荷出错。两条方法的差别是什么时候回假。

## 和相邻反模式

- [handler-sold-as-node](handler-sold-as-node.md) 是 Broadcast 回通道 ≠ 已经送到，不是本页这种单播入队。
- [numpeers-sold-as-all](numpeers-sold-as-all.md) 是查询 ≠ 已经数完，不是本页。
