# 反模式：看见进了这一轮会先设 ProposeTimeout 就当成已经填了 TimeoutPropose / 看见收到带上头的提案会先验块头就当成已经跑过 Process / 看见收齐块片才按验证者算法看该不该 prevote 这块或 nil 就当成已经会调 Process

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[进了这一轮会先设 ProposeTimeout ≠ 已经填了 TimeoutPropose](../../tracks/implementation/worked-example-proposetimeout-vs-process.md)。

## 塌法

1. 看见进了这一轮会先设 `ProposeTimeout` / 看见设了定时，就当成已经填了 TimeoutPropose，或当成已经离开关键路径。
2. 看见收到带上头的提案会先验块头 / 看见验了头，就当成已经跑过 Process，或当成已经知道本头哈希。
3. 看见收齐块片才按验证者算法看该不该 prevote 这块或 nil / 看见在看，就当成已经会调 Process，或当成已经还能再 Reject。

## 为什么会出事

官方写：节点 *p* 进了高度 *h*、一轮 *r*，先设定时器 `ProposeTimeout`。收到提议者 *q* 这一轮这一高的 Proposal（里头带上头），*p* 先验块头。收到提案和全部块片之后，*p* 按验证者算法看该不该 prevote 这块，还是 prevote `nil`。看见到了 When，不是已经填了 TimeoutPropose，也不是已经跑过 Process，也不是已经会调 Process。

## 和相邻反模式

- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行就已经离开关键路径，不是本页这种进了这一轮会先设 ProposeTimeout 不是已经填了 TimeoutPropose。
- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 调用是同步的就已经能稍后改裁决，不是本页这种收齐块片才按验证者算法看该不该 prevote 这块或 nil 不是已经会调 Process。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process，不是本页这种收到带上头的提案会先验块头不是已经跑过 Process。
