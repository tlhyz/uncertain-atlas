# 模式：把反应堆时序三件事说成三个名字

**层次**：网络 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md)。  
**例**：[InitPeer ≠ 已经能交互](../../tracks/network/worked-example-initpeer-vs-addpeer.md)。

## 三个名字

1. **还不能对说：** 看见 InitPeer 不是已经能跟它对说。
2. **还没 AddPeer：** 看见已经在 Receive 不是已经过了 AddPeer。
3. **不能热加：** 看见节点已经在跑不是已经能再登记一个反应堆。

## 为什么要分开叫

官方把收发例程还没跑、Receive 可以先于 AddPeer、运行中不能再登记写成三件事。把它们叫成一个「看见对等节点对象就已经加进去」，会把入站配额和宣布已经收到一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「对等节点已经齐」，先数清问的是还不能对说、还没 AddPeer，还是不能热加，再决定要不要同一次发布。
