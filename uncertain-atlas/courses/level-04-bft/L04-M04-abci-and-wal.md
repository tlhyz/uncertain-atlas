# L4.4 ABCI 与 WAL

优先级：必学 / 重要  
先修：L4.3，L0.2

---

## A. 先修知识

共识选出字节串的顺序。`Apply` 算状态。二者不是同一个进程职责。

---

## B. 核心问题

**为什么共识引擎不该懂余额？为什么投票前必须先写日志？**

---

## C. 直觉

两间房子。

前厅（引擎）：只负责「第 9 号决议是不是这份稿」。不懂钱。  
后厅（应用）：只负责「稿上的转账按规则改账」。不懂谁该在第 3 轮提议。

门上的条子叫 ABCI：高度、交易列表、状态哈希来回递。

另外：你要举手之前，先在自己日记本上写「我将对 A 预提交」。写完再举手。断电了，醒来先读日记，不许改口。这本日记叫 WAL。

---

## D. 正式定义

**ABCI（事实，Cosmos/CometBFT）：** 引擎与应用的字节契约。旧接口只在决定时碰应用。ABCI 2.0 在提案创建（`PrepareProposal`）、提案验收（`ProcessProposal`）、precommit 扩展（`ExtendVote` / `VerifyVoteExtension`）再插三处。`CheckTx` 是池预检，不是最终。`FinalizeBlock` / `Commit` 才把高度钉进应用状态。四门精读：[`../../tracks/consensus/worked-example-prepare-process.md`](../../tracks/consensus/worked-example-prepare-process.md)。

应用必须：

- 确定性  
- 对同一高度同一列表返回同一 `AppHash`  
- 崩溃后能恢复到与引擎相同的高度

**WAL：** 先记录将发出的共识消息与内部状态，再对外投票。  
invariant：重启不得发出与已持久化意图矛盾的票。

CheckTx 通过 + 未 Finalize：链上状态未变。Prepare 还可以把这笔从本块名单拿掉（池里未必删）。用户文案不得写成最终。

---

## E. 最小案例

高度 9 commit 块 B。引擎调用应用执行。应用写库写到一半断电。

正确：恢复后要么重放完整高度 9，要么回到高度 8，两端一致。  
错误：应用以为 9 成功，引擎以为 8，下一轮哈希对不上，看起来像「共识坏了」，其实是部署/实现。

投票：节点已 precommit A 并写入 WAL，重启后对 B precommit。这是安全事故，不是「网络抖了一下」。

---

## F. 真实项目

CometBFT + Cosmos SDK。  
Ethereum 的 EL/CL 拆分是亲戚：执行与共识分开，但边界不同，不要叫 ABCI。

---

## G. 源码

预告：ABCI 服务器、`FinalizeBlock`、WAL 的 write-ahead 点。测试里找 crash replay。

---

## H. 攻击者视角

1. 让应用使用时间/map 遍历 → 哈希分裂。  
2. 杀进程专打「票已发出、WAL 未 fsync」。  
3. 用 CheckTx 与 Finalize 的差异做用户欺诈。  
4. 诱使应用把 Process REJECT 或 Verify 扩展 REJECT 当免费过滤器，拖垮活性。

---

## I. Trade-off

分离：可换执行、可换用户签名、好测。  
代价：两套存储对齐；应用不确定则全裂。  
WAL：安全。代价：磁盘延迟；实现复杂。

---

## J. 对「不确定」的意义

**建议：** 第一版就按「引擎不懂钱、应用不懂票、WAL 先写后投」搭。  
后量子换的是应用里的用户 `Verify` 和引擎里的 vote `Verify` 两枚插件，不是推倒重来。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 应用验用户签，引擎验投票签；两插件可换 |
| 协议 | ABCI：共识不知余额，应用不知票 |
| 实现 | CheckTx ≠ Prepare ≠ Process ≠ Finalize；WAL 先写后投 |
| 部署 | 崩溃必须回到原子高度 |
| 经济 | 应用可收费；共识不该按余额改票权，除非经 V(h) |

**禁止假学习：** 「CheckTx 等于已执行。」「Process / Verify 扩展拒绝没有活性代价。」「Finalize 按本高度扩展改状态。」「应用和共识哪个先写磁盘无所谓。」「本头 AppHash = 本块已经入账。」「看见写下每条消息 = 已经 fsync。」「看见回放时又要签 = 已经双签。」「看见 LastSignBytes 对上 = 已经换了高度。」「看见先装证据 = 已经装满交易。」「看见两条收交易上限 = 已经同一条。」「看见 MaxBytes 写成 -1 = 已经没有上限。」「看见 State 对象 = 已经写进块。」「看见头上的根 = 已经有了 State。」「看见能读本地 State = 已经进了规范。」「看见提案收了交易 = 已经从池里删掉。」「看见本块已 commit = 已经不用再验剩下的。」「看见 CheckTx 过了 = 已经永远有效。」「看见创世 app_state = 已经验过应用状态。」「看见节点起来 = 已经过了 genesis_time。」「看见创世 validators 空 = 已经没有集合。」「看见同进程 = 已经有套接字隔离。」「看见 gRPC 最容易 = 已经高性能。」「看见一条 ABCI 连接 = 已经是四门。」「看见默认 Go 有全局锁 = 已经能把状态直接给 RPC。」「看见 Commit 前锁了内存池 = 已经解锁。」「看见 Commit 里等 broadcast_tx = 已经能往下走。」「看见 Prepare 披露了提案 = 已经知道本头哈希。」「看见立刻执行出候选 = 已经是 ExecuteTxState。」「看见丢掉候选 = 已经永远不用再执行。」
**边界：** 存储通论在 L9.3。不抄扩展启用高度。精读：[`../../tracks/implementation/worked-example-crash.md`](../../tracks/implementation/worked-example-crash.md)、[`../../tracks/consensus/worked-example-prepare-process.md`](../../tracks/consensus/worked-example-prepare-process.md)、[`../../tracks/consensus/worked-example-vote-extension.md`](../../tracks/consensus/worked-example-vote-extension.md)。本头 AppHash ≠ 本高度交易已经交差：[`../../tracks/consensus/worked-example-apphash-vs-this-block.md`](../../tracks/consensus/worked-example-apphash-vs-this-block.md)（不变量 147）。扩展快路径不得跳过旧票字段：ASA-2024-011。治理改启用高度必须先过转移谓词：ASA-2024-001。提议者注入的扩展不是投票权：ASA-2024-006。单笔 CheckTx 绿不是整包可提案：ASA-2024-002。外层 `max_tx_bytes` 不是内层解码已有界：ASA-2024-0012 / 0013。可选模块 EndBlocker 出错不是局部失败：ISA-2025-002。停链交易不是链已经停：x/crisis。奖励池溢出可以停链：ISA-2025-005。未初始化被挡账户不是可归属地址：ASA-2024-003。Int/Dec 位宽对不齐不是已对齐：ASA-2024-010。较新线 `FinalizeBlock` 可回 `next_block_delay`：非确定性，不是槽位，见 [`../../tracks/consensus/worked-example-next-block-delay.md`](../../tracks/consensus/worked-example-next-block-delay.md)。写下每条消息 ≠ 已经 fsync；回放时又要签 ≠ 已经双签：[`../../tracks/implementation/worked-example-wal-vs-signed.md`](../../tracks/implementation/worked-example-wal-vs-signed.md)（不变量 298）。不要抄旋转体积。不要写怎样从损坏里恢复。先装证据 ≠ 已经装满交易；两条收交易上限 ≠ 已经同一条：[`../../tracks/consensus/worked-example-evidence-vs-reap.md`](../../tracks/consensus/worked-example-evidence-vs-reap.md)（不变量 299）。不要抄扣减公式。不要写怎样从池里收割。本地 State ≠ 已经进了块；头上的根 ≠ 已经有了 State：[`../../tracks/implementation/worked-example-state-vs-gossip.md`](../../tracks/implementation/worked-example-state-vs-gossip.md)（不变量 300）。不要抄验证者人数上限。不要写怎样拼 State 字段或怎样算头上的根。提案收了 ≠ 已经从池里删掉；本块已 commit ≠ 已经不用再验剩下的：[`../../tracks/mempool/worked-example-proposed-vs-removed.md`](../../tracks/mempool/worked-example-proposed-vs-removed.md)（不变量 301）。不要抄加锁做法。不要写怎样再验。创世 app_state ≠ 已经验过应用状态；进程起来 ≠ 已经过了 genesis_time：[`../../tracks/implementation/worked-example-genesis-vs-app.md`](../../tracks/implementation/worked-example-genesis-vs-app.md)（不变量 303）。不要抄字段表。不要写怎样填创世字段或怎样调 InitChain。同进程 ≠ 已经有套接字隔离；gRPC 最容易 ≠ 已经高性能；一条连接 ≠ 已经够用，也不是已经是四门：[`../../tracks/implementation/worked-example-abci-conn-vs-gates.md`](../../tracks/implementation/worked-example-abci-conn-vs-gates.md)（不变量 307）。默认锁 ≠ 已经 RPC 安全；Commit 前上锁 ≠ 已经解锁；Commit 里等广播 ≠ 已经能往下走：[`../../tracks/implementation/worked-example-commit-lock-vs-rpc.md`](../../tracks/implementation/worked-example-commit-lock-vs-rpc.md)（不变量 310）。Prepare 没有头哈希 ≠ 已经知道本头；候选 ≠ 已经是 ExecuteTxState；丢掉 ≠ 已经永远不用再执行：[`../../tracks/implementation/worked-example-candidate-vs-execute.md`](../../tracks/implementation/worked-example-candidate-vs-execute.md)（不变量 311）。CheckTx 过了 ≠ 已经按 ExecuteTxState 验过；两份同时在改 ≠ 已经同一份；RECHECK ≠ 已经是新交易：[`../../tracks/implementation/worked-example-checktxstate-vs-execute.md`](../../tracks/implementation/worked-example-checktxstate-vs-execute.md)（不变量 312）。内存池去重 ≠ 已经保证不重放；过了 CheckTx ≠ 已经有应用级保护；通常不受欢迎 ≠ 已经没有幂等例外：[`../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md`](../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md)（不变量 313）。QueryState ≠ 已经是 ExecuteTxState；上次 Commit ≠ 已经跟上正在跑的块；启动对齐 ≠ 已经是快照重放：[`../../tracks/implementation/worked-example-querystate-vs-execute.md`](../../tracks/implementation/worked-example-querystate-vs-execute.md)（不变量 314）。MaxGas ≠ 已经在执行；GasUsed ≠ 已经算进共识；已提交块 ≠ 已经按气验过：[`../../tracks/implementation/worked-example-maxgas-vs-enforced.md`](../../tracks/implementation/worked-example-maxgas-vs-enforced.md)（不变量 315）。结果列表 ≠ 已经同一顺序；Code 非零 ≠ 已经没进块；Code / Data ≠ 已经印进本头：[`../../tracks/implementation/worked-example-exectxresult-vs-consensus.md`](../../tracks/implementation/worked-example-exectxresult-vs-consensus.md)（不变量 316）。CheckTx 的 Data ≠ 已经被引擎用了；各节点 Data 不一样 ≠ 已经分叉；Priority ≠ 已经是共识顺序：[`../../tracks/implementation/worked-example-checktxresponse-vs-exec.md`](../../tracks/implementation/worked-example-checktxresponse-vs-exec.md)（不变量 317）。不要抄长度前缀。不要写怎样开套接字或怎样编 protobuf。不要另写怎样加锁或怎样调广播。不要另写怎样缓存候选或怎样算头哈希。不要另写怎样实现 CheckTx 或怎样再验。不要另写怎样实现重放保护或怎样做索引器。不要另写怎样实现 QueryState 或怎样做 state sync。不要另写怎样计量气或怎样在 Prepare 里卡上限。不要另写怎样编回执或怎样建索引。不要另写怎样实现 Priority 或怎样编 Data。InitChain 空名单 ≠ 已经没有集合；同一批重复公钥 ≠ 已经能恢复；power 0 ≠ 已经删掉不在集合里的人：[`../../tracks/implementation/worked-example-validatorupdate-vs-set.md`](../../tracks/implementation/worked-example-validatorupdate-vs-set.md)（不变量 318）。不要另写怎样编 `ValidatorUpdate` 或怎样算总权。InitChain 空参数 ≠ 已经没有参数；Finalize 没回 ≠ 已经清掉；只改一个字段 ≠ 已经只改这一项：[`../../tracks/implementation/worked-example-consensusparams-vs-update.md`](../../tracks/implementation/worked-example-consensusparams-vs-update.md)（不变量 319）。不要另写怎样编 `ConsensusParams` 或怎样选上限。应用高度比引擎高 ≠ 已经允许；块进 store ≠ 已经 Commit；启动 Info 对上 ≠ 已经能跳步：[`../../tracks/implementation/worked-example-crash-steps-vs-commit.md`](../../tracks/implementation/worked-example-crash-steps-vs-commit.md)（不变量 320）。不要另写怎样落盘或怎样写 Commit。
