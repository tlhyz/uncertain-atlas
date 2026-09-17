# 例：看见 InitPeer 不是已经能跟它对说；看见已经在 Receive 不是已经过了 AddPeer；看见节点已经在跑不是已经能再登记一个反应堆

**层次**：网络 / 反应堆时序。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Reactor API](https://github.com/cometbft/cometbft/blob/main/spec/p2p/reactor-api/reactor.md)。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「InitPeer 不是已经能交互 / Receive 不是已经 AddPeer / 跑着不是已经能再登记」，不是入站配额已经认领 ID，也不是宣布已经收到。不要另写怎样实现 Receive 并发或怎样发 Envelope。

## 官方三件事

规范把反应堆和 p2p 层的时序写成三件独立的网络事，不是「看见对等节点对象就已经加进去、已经能对说」一件事：

1. **看见 InitPeer / 看见对等节点对象已经交给反应堆 不是已经能跟它对说。**  
   官方写：`InitPeer(Peer)` 被叫时，这个 `Peer` 还没启动，收消息和发消息的例程都没在跑。这一步用来初始化跟这个新人对等节点有关的状态或数据，不要跟它对交互。看见对象在了，不是已经能发。看见状态建了，不是已经加进已连接集合。看见叫了 `InitPeer`，不是已经 `AddPeer`。
2. **看见已经在 Receive / 看见消息已经进来 不是已经过了 AddPeer。**  
   官方写：从一个 `Peer` 收消息的前置条件，是 p2p 层先前已经叫过 `InitPeer(Peer)`，不是已经叫过 `AddPeer`。反应堆必须能在 `AddPeer` 之前收下消息。这是因为收发例程会先启动，而且在把这个人对等节点加进每一个已登记反应堆时，这些例程应该已经在跑。看见 `Receive` 来了，不是已经 `AddPeer`。看见信封在了，不是已经可以按「已加入」去发。看见最常见的是 `AddPeer` 之后才开始收，不是官方禁止更早收。
3. **看见节点已经在跑 / 看见反应堆已经登记过名字 不是已经能再登记一个。**  
   官方写：登记必须用 `Switch.AddReactor`，而且必须发生在节点、尤其是 p2p 层启动之前。运行中的节点不支持再登记一个反应堆；反应堆必须作为节点起步的一部分登记。`OnStart` / `OnStop` 各只能一次。启动前或停了之后，反应堆不要再指望有交互。看见进程起来了，不是已经能热加。看见名字已经占了，不是已经能再占一个。看见停过了，不是已经能再开。

通道号、Quint 模型、ABNF 文法、信封字段表是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **InitPeer ≠ 已经能交互：** 官方把对象已经交给反应堆，和收发例程还没跑分开。
- **Receive ≠ 已经 AddPeer：** 官方把收消息的前置写成先前的 `InitPeer`，不是 `AddPeer`。
- **跑着 ≠ 已经能再登记：** 官方把起步登记和运行中热加分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitPeer | 不是已经能跟它对说 | 不是入站配额已经认领 ID（67） |
| Receive 先于 AddPeer | 不是已经过了 AddPeer | 不是宣布已经收到（36） |
| 运行中再登记 | 不是已经能再加反应堆 | 不是握手请求已经是已接受邻居（67） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「对等节点已经齐」，必须分开 InitPeer 是不是已经能交互、Receive 是不是已经 AddPeer、跑着是不是已经能再登记。可以跳过「看见对等节点对象就已经加进去」。不要另写怎样实现 Receive 并发或怎样发 Envelope。305 initpeer vs addpeer bundled unbundling 完成（1001 item 1 / 1002 item 2 / 1003 item 3）；精读 [`worked-example-initpeer-nottalk-vs-bundled.md`](worked-example-initpeer-nottalk-vs-bundled.md)（不变量 1001 item 1）。

## 本页不抄

- Quint 模型、ABNF 文法、通道号、信封字段表。
- 怎样实现 `Receive` 并发、怎样不阻塞、怎样发 Envelope、怎样编 protobuf。
- 怎样在 `InitPeer` 里认领 ID。那是不变量 67。
