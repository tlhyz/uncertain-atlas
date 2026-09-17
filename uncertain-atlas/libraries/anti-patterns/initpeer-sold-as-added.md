# 反模式：看见 InitPeer 就当成已经能跟它对说 / 看见已经在 Receive 就当成已经过了 AddPeer / 看见节点已经在跑就当成已经能再登记一个反应堆

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md)。  
**例**：[InitPeer ≠ 已经能交互](../../tracks/network/worked-example-initpeer-vs-addpeer.md)。

## 塌法

1. 看见 InitPeer / 看见对等节点对象已经交给反应堆，就当成已经能跟它对说。
2. 看见已经在 Receive / 看见消息已经进来，就当成已经过了 AddPeer。
3. 看见节点已经在跑 / 看见反应堆已经登记过名字，就当成已经能再登记一个。
4. 看见最常见的是 AddPeer 之后才开始收，就当成更早收已经非法。
5. 看见停过了，就当成已经能再开。

## 为什么会出事

官方写：`InitPeer` 被叫时收发例程还没跑，不要跟它对交互。Receive 的前置是先前的 `InitPeer`，不是 `AddPeer`。运行中的节点不支持再登记反应堆。

## 和相邻反模式

- [timestamp-sold-as-checked](timestamp-sold-as-checked.md) 是票上时间戳 ≠ 已经验过，不是本页这种对等时序。
- [wal-sold-as-signed](wal-sold-as-signed.md) 是写下 ≠ 已经 fsync，不是本页这种 InitPeer。
