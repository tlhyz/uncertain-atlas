# 模式：把 Process 何时调用余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[进了这一轮会先设 ProposeTimeout ≠ 已经填了 TimeoutPropose](../../tracks/implementation/worked-example-proposetimeout-vs-process.md)。

## 三个名字

1. **进了这一轮会先设 ProposeTimeout 不是已经填了 TimeoutPropose：** 看见设了定时不是已经离开关键路径。
2. **收到带上头的提案会先验块头不是已经跑过 Process：** 看见验了头不是已经知道本头哈希。
3. **收齐块片才按验证者算法看该不该 prevote 这块或 nil 不是已经会调 Process：** 看见在看不是已经还能再 Reject。

## 为什么要分开叫

官方把进了这一轮会先设 `ProposeTimeout`、收到带上头的提案会先验块头、收齐块片才按验证者算法看该不该 prevote 这块或 nil 写成三件事。把它们叫成一个「看见到了 Process 何时调用就已经填了 TimeoutPropose」，会把已经填了 TimeoutPropose、已经跑过 Process 和已经会调 Process 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了 Process 何时调用就已经填了 TimeoutPropose」，先数清问的是进了这一轮会先设 ProposeTimeout 不是已经填了 TimeoutPropose、收到带上头的提案会先验块头不是已经跑过 Process，还是收齐块片才按验证者算法看该不该 prevote 这块或 nil 不是已经会调 Process，再决定要不要同一次发布。
