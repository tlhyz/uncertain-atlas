# 工作实例：CheckTx 过了，不等于进了提案，更不等于已提交

> **事实 / 推断 / 建议** 已分开。
> 对照：[谁排序](../mempool/worked-example-who-orders.md)、[ABCI 课](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[CometBFT 档案](../../protocols/cometbft/report.md)、[筐](../mempool/worked-example.md)。
> 主文献：[ABCI++ 基本概念](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_basic_concepts.md)、[应用要求](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)、[方法](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)。
> 本页钉 **池预检 / 提案改写 / 提案验收 / 提交执行** 四门。扩展另页：[vote extension](worked-example-vote-extension.md)。不抄默认 `max_tx_bytes`、propose 超时秒数、Cosmos SDK 版本。

---

## 0. 先修

- [L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)
- [L9.2](../../courses/level-09-systems/L09-M02-mempool.md)
- [不变量 27](../../libraries/invariants/README.md#27-排序权必须点名谁写列表谁签头)（Builder API：谁写列表 vs 谁签头）

---

## 1. 核心问题

阿比看见「节点回报 CheckTx OK」，以为这笔已经在本高度的块里，甚至已经改了余额。

在 ABCI 2.0 里，那最多只过了第一扇门。还有三扇：

1. **PrepareProposal**：本轮提议者的应用可以改 raw 列表（改序 / 增 / 删）。
2. **ProcessProposal**：验证者的应用只能验收、不能改；REJECT 等于 prevote `nil`。
3. **FinalizeBlock + Commit**：决定之后才改已提交状态。

旧 ABCI 只在 **decision** 时碰应用。ABCI 2.0 让应用插进提案创建、提案验收、以及 precommit 的 vote extension。`{BeginBlock, DeliverTx, EndBlock}` 收成 `FinalizeBlock`。

「谁排序」三个字不够。必须能指出：池里有谁、提案里剩谁、验收能不能改列表、何时才写 `s_h`。

---

## 2. 直觉（ELI15）

邮局门口的筐（池）盖了「这封看起来能寄」。  
值班班长组班报时，可以把筐里的信重新排队、抽走、塞进筐里没有的信。  
全班验收班报：只能说收或不收，不能自己改名单；说不收等于这轮举手弃权。  
校长盖章之后，才改全校名册。验收时先演练的草稿，盖章前必须能撕掉。

---

## 3. 正式对象（ABCI++ 规范，事实）

### 3.1 四门

| 门 | 谁调用 | 应用能做什么 | 确定性 | 改已提交状态 `s_{h-1}` |
|----|--------|--------------|--------|------------------------|
| `CheckTx` | 进池 / 可配置的 commit 后再检 | 说此刻收不收进**本节点池** | 应用自定；规范另有「最终不再振荡」要求 | 否（池不是账本） |
| `PrepareProposal` | 本轮提议者，且 `validValue` 为 `nil` | 改 raw 列表：改序 / 增 / 删 | **可以不确定** | 否（Req 9） |
| `ProcessProposal` | 准备非空 prevote 之前 | 只验收；**不能改**提案 | **必须确定** | 否（Req 9） |
| `FinalizeBlock` 再 `Commit` | 该高度已决定 | 按列表确定执行并持久化 | 必须确定（Req 11–12） | 这时才替换 |

**事实：** `CheckTx` 的非零 `Code` 只影响内存池（不进池或从池里拿掉）。`FinalizeBlock` 里单笔 `ExecTxResult.Code ≠ 0` 会被记下，**不影响共识**——它已经在已决定的块里。

**事实：** 从池里抽掉一笔，**不会**把它移出 mempool，只是本块不提（推迟）。往提案里塞一笔新的，引擎**不会**把它加进 mempool。

**事实：** 有非空 `validValue` 时，本轮直接用锁住的合法值，**不**再调 `PrepareProposal`。

**事实：** 同一高度里，`PrepareProposal` / `ProcessProposal` / `ExtendVote` / `VerifyVoteExtension` 都可能被叫多次。提议者这边，Process 通常紧跟 Prepare 且列表相同；失败时**不保证**：可能对上更早一次 Prepare，或根本不调 Process。

### 3.2 大小、连贯、立即执行

- **Req 2：** 返回交易的总字节不得超过本次 `PrepareProposalRequest.max_tx_bytes`。引擎可以按配置把**整池**交给应用，整池合计可以大于这个上限；裁剪是应用的义务。本页不抄现行默认上限。
- **Req 3（连贯）：** 诚实进程 *p* 准备出的 *u*，诚实 *q* 的 `ProcessProposal` **必须 Accept**。
- **Req 4–5：** Accept/Reject **只**依赖本次请求与上一高度已提交状态 `s_{h-1}`；两个诚实应用必须同判。
- 规范通则：`ProcessProposal` **SHOULD always ACCEPT**，除非你真的知道 REJECT 的活性代价。部分交易无效时，规范建议仍 Accept，执行时再忽略无效部分。
- **REJECT ⇒ prevote `nil`。** 规范写明这对活性影响很重。同一代码库的确定性 bug 会让大家一起弃权。
- 立即执行（在 Prepare / Process 里先跑块）只许产生**候选**状态。在 `FinalizeBlock` 确认决定并调用 `Commit` 之前，**不得**用候选替换上一提交状态。
- **Req 9（无副作用）：** 高度 *h* 的 Prepare / Process / ExtendVote / VerifyVoteExtension **不得**修改 `s_{h-1}`。
- `FinalizeBlock`：引擎保证至少有一名非拜占庭验证者对这块跑过 `ProcessProposal`。

### 3.3 Vote extension（只点名，不展开）

`ExtendVote` / `VerifyVoteExtension` 挂在 **precommit** 上。扩展字节对共识算法不透明。`ExtendVote` 可以不确定；`VerifyVoteExtension` 必须确定。验失败会让**整张** precommit 被丢掉，同样伤活性；规范通则也是 SHOULD accept。它们的数据可以在下一高度的 Prepare 里被提议者看见，但仍受 Req 9：不得改当前已提交状态。`s_h` 不得依赖本高度收到的扩展（Req 10）。全文：[vote extension](worked-example-vote-extension.md)。

### 3.4 和 Builder API 不是同一根钉子

| | Ethereum Builder API | CometBFT ABCI++ Prepare |
|--|----------------------|-------------------------|
| 谁写列表 | 域外 builder | **本验证者的应用进程**（引擎先给 raw 池列表） |
| 提议者签之前看不看得见表 | 往往只看见 header / `transactions_root` | 提案带完整 `txs` |
| 其他验证者能否改列表 | 不能；他们验完整载荷 | `ProcessProposal` **不能改**，只能 Accept/Reject |
| 文献 | builder-specs（域外、更高信任） | ABCI++ 规范（在引擎↔应用契约里） |

**事实：** 把 Prepare 写成「CometBFT 已经有 PBS」，文献等级错了。Prepare 是**同一进程里的应用回调**，不是域外市场。

**推断：** 审查仍可发生——提议者的应用可以删交易。这不是新的分叉选择，是排序权放在应用侧。

---

## 4. 对照表

| | CheckTx | Prepare | Process | Finalize+Commit |
|--|---------|---------|---------|-----------------|
| 用户常误读成 | 「已经上链」 | 「共识选好了」 | 「又验了一次所以更安全」 | （这才是提交） |
| 实际对象 | 本节点池政策 | 本轮提案字节 | 非空 prevote 前的应用验收 | 已决定块的 `Apply` |
| 失败意味 | 进不了这台池 | 超时/崩溃会换轮（Prepare 在关键路径上） | prevote nil；可能空轮 | 单笔 Code≠0 仍在块里；顶层 error 可让引擎崩 |

Bitcoin 矿工本地选交易、签整块：没有这四扇 ABCI 门。不要把「矿工 / proposer」糊成一句。

Monad「先定序、后交差根」是另一根钉子（定序 ≠ 状态最终）。见过滤器页。

---

## 5. 攻击者

| 攻击 | 机制 | 文献挡的 | 文献挡不住的 |
|------|------|----------|--------------|
| 把 CheckTx 当最终 | 钱包文案 | CheckTx 非零码只动池 | 用户已放货 |
| 把 Prepare 当 PBS | 文案 | Prepare 是应用回调 | 用户以为无需信任排序者 |
| 用 Process REJECT 当免费过滤器 | 应用把无效交易写成 REJECT | 规范：SHOULD Accept；Reject ⇒ nil | 全网活性；同代码库一起卡 |
| 立即执行写进提交库 | 候选当正式 | Req 9；候选必须可丢 | 换轮后根分裂或半状态 |
| 返回超过 `max_tx_bytes` | 整池可见时未裁 | Req 2；响应验不过引擎当应用故障并崩溃 | 本轮提议者宕 |
| 抄默认字节 / 超时当共识 | 配置文件 | — | 数字过期；本页不填 |

---

## 6. 五层

| 层 | 本页能说的 | 不能说的 |
|----|------------|----------|
| 密码学 | 用户签在应用；投票签在引擎；Prepare 不负责换算法 | 「ABCI++ 已经后量子」 |
| 协议 | 四门；Req 2–5、9；Reject ⇒ nil | 「Process 拒了所以共识更硬」 |
| 实现 | 立即执行必须双状态；Prepare 可不确定 | 某 SDK 版本的默认裁剪策略 |
| 部署 | `TimeoutPropose` 必须装得下 Prepare（尤其立即执行）；规范说超时会随轮涨，但靠自适配会慢 | 现行默认秒数、默认块字节 |
| 经济 | 应用可在 Prepare 里重排/删除 = 审查权 | 某链的 MEV 金额 |

---

## 7. 对不确定的意义（建议）

- 若抄 ABCI 分离：文档必须有四门，不能只写 `CheckTx` / `Apply`。
- 默认：`ProcessProposal` 几乎总是 Accept；无效交易留到 Finalize 再标 Code。不要把 REJECT 当成「多一层安全」。
- 若用 Prepare 改列表：写清谁改、改完是否还可追踪原交易哈希；删 ≠ 移出池。
- 立即执行可以要，但必须有候选状态机；崩溃后只承认 `Commit` 过的高度。
- 不要抄域外 Builder API 来「优化」Prepare；也不要把 Prepare 广告成 PBS。
- Vote extension 默认可以不启用；启用则必须守 Req 10，见专页。
- 后量子：Prepare 若做聚合或批量验签，先写配额；数字仍空。

---

## 8. 禁句

- 「CheckTx 过了所以会进本块 / 已经执行」
- 「PrepareProposal = PBS」
- 「Process 拒绝无效交易没有活性代价」
- 「验收时跑过的状态就是已提交状态」
- 「提议者 Process 一定看到自己刚 Prepare 的那份」
- 未标注版本的默认 `max_tx_bytes`、`TimeoutPropose` 秒数、SDK 版本
