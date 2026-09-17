# 工作实例：本头 AppHash 不是本高度交易已经交差

> **事实 / 推断 / 建议** 已分开。
> 对照：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[CometBFT 档案](../../protocols/cometbft/README.md)、[ABCI 四门](worked-example-prepare-process.md)、[顺序 ≠ 状态](worked-example-order-vs-state.md)、[state sync](../implementation/worked-example-statesync.md)。
> 主文献：CometBFT 官方 [data structures](https://github.com/cometbft/cometbft/blob/main/spec/core/data_structures.md)、[ABCI++ FinalizeBlock](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)。资料层级是共识规范。不另写 19 节。
> 本页钉 **本头 AppHash ≠ 本高度交易已经交差**、**DataHash 有这笔 ≠ 效果已经进本头 AppHash**、**FinalizeBlock 回的根 ≠ 已经写进本头**。不抄哈希宽度、ChainID 字节上限、票槽上限。不写怎样伪造 AppHash。

---

## 0. 先修

- [L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md) ABCI：应用不是共识
- [不变量 33](../../libraries/invariants/README.md) 四门
- [不变量 38](../../libraries/invariants/README.md) 快照锚是轻验 AppHash
- [不变量 147](../../libraries/invariants/README.md)

---

## 1. 核心问题

阿比看见高度 H 的头里有 `AppHash`，或看见本块 `DataHash` 里有一笔转账，以为这笔的效果已经写进**这个头**；或看见 `FinalizeBlock` 刚回了一个根，以为本头已经带上它。

官方句（事实）：

- 数据结构规范：`Header.AppHash` 是应用在**执行并提交上一块**之后返回的任意字节。它用来锚应用侧 Merkle 证明，代表**应用状态**，不是区块链自己的状态。第一块的 `AppHash` 来自 `InitChainResponse.app_hash`。引擎**不能**替应用验这个哈希。
- 同一张头表：`DataHash` 是**本块**交易哈希的 Merkle 根。`LastResultsHash` 是上一块交易回执的 Merkle 根（规范按 `DeliverTxResponse` 形状写；`Log` / `Info` / `Codespace` / `Events` 不进树）。第一块的结果根是空输入的 Merkle 根。
- ABCI++：`ResponseFinalizeBlock.app_hash` 是（可选的）应用状态 Merkle 根，写进**下一块**头的 `Header.AppHash`。它可以空或写死，但必须确定：只能是本次 `RequestFinalizeBlock` 参数和上一份已提交状态的函数。
- 规范**没有**把本头 `AppHash` 写成「本高度交易已经交差」，也没有把本块 `DataHash` 写成「效果已经进本头」，也没有把本高度 `FinalizeBlock` 回的根写成「已经印在本头上」。

本头的应用根、本块交易根、本高度 Finalize 刚回的根，是三件东西。

---

## 2. 直觉（ELI15）

今天的会议纪要封面，印的是**昨天**账本合上时的封条。  
今天桌上那叠提案的目录，是另一枚章。  
今天散会后出纳才算出的新封条，要等到**明天**的纪要封面才印上去。

看见今天封面上的封条，不是今天桌上那叠提案已经入账。

---

## 3. 对象

| 名字 | 是什么 | 不是什么 |
|---|---|---|
| 本头 `AppHash` | 上一块 Finalize / Apply 之后的应用根 | 本高度交易已经交差；区块链自己的状态 |
| 本块 `DataHash` | 本块交易哈希的 Merkle 根 | 这些交易的效果已经进本头 `AppHash` |
| `LastResultsHash` | 上一块交易回执根 | 本块 Deliver / Finalize 回执已经进本头 |
| 本高度 `FinalizeBlock.app_hash` | 本高度执行后要交给下一块头的根 | 已经写进本头 |
| 第一块 `AppHash` | `InitChain` 给的根 | 创世交易已经 Apply |

---

## 4. 最小案例

一条 CometBFT 链要对齐「这笔在高度 H 已经入账」。

1. 高度 H 的头带 `AppHash`。规范：那是 H−1 执行并提交之后的应用根。不是 H 的交易已经交差。
2. 高度 H 的 `DataHash` 里有阿安给阿比的转账。规范：那是本块交易目录。不是效果已经进本头 `AppHash`。
3. 引擎对本高度调用 `FinalizeBlock`，应用回了一个新根。ABCI++：这个根进**下一块**头。不是已经印在高度 H 的头上。
4. 有人把这听成 Monad 的「顺序已定、本块根还要再等 D」（不变量 136），或听成四门里 Finalize 等于已结算（不变量 33）。那些是延迟执行管道和门牌。本页是头字段滞后一块。
5. 有人把轻验过的 `AppHash` 听成提议者日程已齐（不变量 56），或听成快照等于从创世重放（不变量 38）。那些是同步。本页是「本头印的是上一块」。

「头上有 AppHash 所以本块已经入账」是假学习。

---

## 5. 五层

| 层 | 本页 |
|---|---|
| 密码学 | AppHash 锚的是应用证明，不是引擎自己的块哈希 |
| 协议 | 必须点名问的是本头根、本块交易根，还是本高度刚回的根 |
| 实现 | ABCI++ 把 Finalize 的根写进下一块；旧 DeliverTx 名字不是另一套语义 |
| 部署 | 浏览器若把本头 AppHash 画成本块余额，运维会把滞后听成分叉 |
| 经济 | 本块目录里有转账 ≠ 对方已经能按本头根兑付 |

**推断：** 产品句若只写「头上有状态根」，读者会把昨天的封条听成今天已经入账。  
**建议：** 若抄 CometBFT 头，必须写清本头 `AppHash` 是上一高度 Finalize。不要发明「本头同时带本块根」却不另写提交规则。不要把 Monad 的 D 抄进本页。

---

## 6. 和另外几句不是同一句

1. **四门**（不变量 33）：CheckTx / Prepare / Process / Finalize。本页是头上印的是哪一块的根。
2. **快照锚**（不变量 38）：轻验 AppHash ≠ 从创世重放。本页不是 state sync。
3. **轻验 ≠ 日程**（不变量 56）：AppHash 对上 ≠ 提议者选择已齐。本页不是 ProposerPriority。
4. **顺序 ≠ 状态**（不变量 136）：官方顺序已定，本块根还要再等。那是异步执行管道。本页是规范把头字段写成上一块。
5. **集合延迟**（不变量 35）：H 的更新进 H+1 / H+2 / H+3。那是验证者集合。本页是 AppHash。
6. **原子高度**（不变量 5）：崩溃后高度对齐。本页不是 WAL。

不要抄哈希宽度、ChainID 上限、票槽上限。不要写怎样伪造 AppHash。不编博物馆页。不另写 19 节。轻客户端跳过、state sync、Monad `D` 标成另一对象。

---

## 7. 「不确定」测试句（建议）

```text
本头 AppHash ≠ 本高度交易已经交差
本块 DataHash 有这笔 ≠ 效果已经进本头 AppHash
本高度 FinalizeBlock 回的根 ≠ 已经写进本头
AppHash 是应用状态 ≠ 区块链自己的状态
第一块 AppHash = InitChain ≠ 创世交易已经 Apply
```

语料：[C151](../../libraries/adversarial-corpus/README.md)。

---

## 精密检查

**禁止假学习：** 「头上有 AppHash = 本块已经入账。」「DataHash 里有这笔 = 余额已经改。」「FinalizeBlock 刚回根 = 本头已经带上。」  
**边界：** 不讲某一版 SDK 的 `LastCommitID` 助手。不抄哈希宽度。不另写 19 节。不写怎样伪造根。Monad 延迟执行、state sync、轻客户端另标。
