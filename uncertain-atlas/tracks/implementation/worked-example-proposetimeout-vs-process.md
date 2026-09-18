# 例：看见进了这一轮会先设 ProposeTimeout 不是已经填了 TimeoutPropose；看见收到带上头的提案会先验块头不是已经跑过 Process；看见收齐块片才按验证者算法看该不该 prevote 这块或 nil 不是已经会调 Process

**层次**：实现 / Process 何时调用余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「进了这一轮会先设 ProposeTimeout 不是已经填了 TimeoutPropose / 收到带上头的提案会先验块头不是已经跑过 Process / 收齐块片才按验证者算法看该不该 prevote 这块或 nil 不是已经会调 Process」，不是立刻整块执行就已经离开关键路径，也不是 Process 调用是同步的就已经能稍后改裁决。不要另写怎样写 Process 何时调用余量。

## 官方三件事

规范把进了这一轮会先设 `ProposeTimeout`、收到带上头的提案会先验块头、收齐块片才按验证者算法看该不该 prevote 这块或 nil 写成三件独立的实现事，不是「看见到了 Process 何时调用就已经填了 TimeoutPropose、已经跑过 Process、已经会调 Process」一件事：

1. **看见进了这一轮会先设 `ProposeTimeout` / 看见设了定时 不是已经填了 TimeoutPropose，也不是已经离开关键路径。**  
   官方写：节点 *p* 进了高度 *h*、一轮 *r*，先设定时器 `ProposeTimeout`。看见设了定时，不是已经是立刻整块执行那种填了 `TimeoutPropose` 就已经装得下。看见进了这一轮，不是已经离开关键路径。看见有定时器，不是已经会调 Process。
2. **看见收到带上头的提案会先验块头 / 看见验了头 不是已经跑过 Process，也不是已经知道本头哈希。**  
   官方写：收到提议者 *q* 这一轮这一高的 Proposal（里头带上头），*p* 先验块头。看见验了头，不是已经 Prepare 和 Process / Finalize 同一套字段那种已经跑过 Process。看见提案带上头，不是已经 Finalize 请求 hash 那种已经知道本头哈希。看见先验，不是已经交差。
3. **看见收齐块片才按验证者算法看该不该 prevote 这块或 nil / 看见在看 不是已经会调 Process，也不是已经还能再 Reject。**  
   官方写：收到提案和全部块片之后，*p* 按验证者算法看该不该 prevote 这块，还是 prevote `nil`。看见在看，不是已经 Process 调用是同步的那种已经会调。看见还没调，不是已经只做基本检查再异步 Process 那种已经还能再 Reject。看见有算法，不是已经交差。

怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头是规范里的做法，本页不抄。立刻整块执行就已经离开关键路径是不变量 327，本页不抄。

## 官方为什么这样拆

- **进了这一轮会先设 ProposeTimeout ≠ 已经填了 TimeoutPropose：** 官方把算法里这份定时器和配置里那份 TimeoutPropose 分开。
- **收到带上头的提案会先验块头 ≠ 已经跑过 Process：** 官方把先验块头和已经调过 Process 分开。
- **收齐块片才按验证者算法看该不该 prevote 这块或 nil ≠ 已经会调 Process：** 官方把还在看该不该 prevote 和已经调 Process 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 进了这一轮会先设 ProposeTimeout | 不是已经填了 TimeoutPropose | 不是立刻整块执行就已经离开关键路径（327） |
| 收到带上头的提案会先验块头 | 不是已经跑过 Process | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| 收齐块片才按验证者算法看该不该 prevote 这块或 nil | 不是已经会调 Process | 不是 Process 调用是同步的就已经能稍后改裁决（354） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了 Process 何时调用就已经填了 TimeoutPropose、已经跑过 Process、已经会调 Process」，必须分开进了这一轮会先设 ProposeTimeout 是不是已经填了 TimeoutPropose、收到带上头的提案会先验块头是不是已经跑过 Process、收齐块片才按验证者算法看该不该 prevote 这块或 nil 是不是已经会调 Process。可以跳过「看见到了 Process 何时调用就已经填了 TimeoutPropose」。不要另写怎样写 Process 何时调用余量。416 proposetimeout vs process bundled unbundling 完成（1094 item 1 / 1095 item 2 / 1096 item 3）；精读 [`worked-example-ptime-notcfg-vs-bundled.md`](worked-example-ptime-notcfg-vs-bundled.md)（不变量 1094 item 1）。

## 本页不抄

- 怎样写 Process 何时调用余量、怎样设 ProposeTimeout、怎样验块头。
- 立刻整块执行就已经离开关键路径。那是不变量 327。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
