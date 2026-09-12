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
**边界：** 存储通论在 L9.3。不抄扩展启用高度。精读：[`../../tracks/implementation/worked-example-crash.md`](../../tracks/implementation/worked-example-crash.md)、[`../../tracks/consensus/worked-example-prepare-process.md`](../../tracks/consensus/worked-example-prepare-process.md)、[`../../tracks/consensus/worked-example-vote-extension.md`](../../tracks/consensus/worked-example-vote-extension.md)。本头 AppHash ≠ 本高度交易已经交差：[`../../tracks/consensus/worked-example-apphash-vs-this-block.md`](../../tracks/consensus/worked-example-apphash-vs-this-block.md)（不变量 147）。扩展快路径不得跳过旧票字段：ASA-2024-011。治理改启用高度必须先过转移谓词：ASA-2024-001。提议者注入的扩展不是投票权：ASA-2024-006。单笔 CheckTx 绿不是整包可提案：ASA-2024-002。外层 `max_tx_bytes` 不是内层解码已有界：ASA-2024-0012 / 0013。可选模块 EndBlocker 出错不是局部失败：ISA-2025-002。停链交易不是链已经停：x/crisis。奖励池溢出可以停链：ISA-2025-005。未初始化被挡账户不是可归属地址：ASA-2024-003。Int/Dec 位宽对不齐不是已对齐：ASA-2024-010。较新线 `FinalizeBlock` 可回 `next_block_delay`：非确定性，不是槽位，见 [`../../tracks/consensus/worked-example-next-block-delay.md`](../../tracks/consensus/worked-example-next-block-delay.md)。写下每条消息 ≠ 已经 fsync；回放时又要签 ≠ 已经双签：[`../../tracks/implementation/worked-example-wal-vs-signed.md`](../../tracks/implementation/worked-example-wal-vs-signed.md)（不变量 298）。不要抄旋转体积。不要写怎样从损坏里恢复。先装证据 ≠ 已经装满交易；两条收交易上限 ≠ 已经同一条：[`../../tracks/consensus/worked-example-evidence-vs-reap.md`](../../tracks/consensus/worked-example-evidence-vs-reap.md)（不变量 299）。不要抄扣减公式。不要写怎样从池里收割。本地 State ≠ 已经进了块；头上的根 ≠ 已经有了 State：[`../../tracks/implementation/worked-example-state-vs-gossip.md`](../../tracks/implementation/worked-example-state-vs-gossip.md)（不变量 300）。不要抄验证者人数上限。不要写怎样拼 State 字段或怎样算头上的根。提案收了 ≠ 已经从池里删掉；本块已 commit ≠ 已经不用再验剩下的：[`../../tracks/mempool/worked-example-proposed-vs-removed.md`](../../tracks/mempool/worked-example-proposed-vs-removed.md)（不变量 301）。不要抄加锁做法。不要写怎样再验。创世 app_state ≠ 已经验过应用状态；进程起来 ≠ 已经过了 genesis_time：[`../../tracks/implementation/worked-example-genesis-vs-app.md`](../../tracks/implementation/worked-example-genesis-vs-app.md)（不变量 303）。不要抄字段表。不要写怎样填创世字段或怎样调 InitChain。同进程 ≠ 已经有套接字隔离；gRPC 最容易 ≠ 已经高性能；一条连接 ≠ 已经够用，也不是已经是四门：[`../../tracks/implementation/worked-example-abci-conn-vs-gates.md`](../../tracks/implementation/worked-example-abci-conn-vs-gates.md)（不变量 307）。默认锁 ≠ 已经 RPC 安全；Commit 前上锁 ≠ 已经解锁；Commit 里等广播 ≠ 已经能往下走：[`../../tracks/implementation/worked-example-commit-lock-vs-rpc.md`](../../tracks/implementation/worked-example-commit-lock-vs-rpc.md)（不变量 310）。Prepare 没有头哈希 ≠ 已经知道本头；候选 ≠ 已经是 ExecuteTxState；丢掉 ≠ 已经永远不用再执行：[`../../tracks/implementation/worked-example-candidate-vs-execute.md`](../../tracks/implementation/worked-example-candidate-vs-execute.md)（不变量 311）。CheckTx 过了 ≠ 已经按 ExecuteTxState 验过；两份同时在改 ≠ 已经同一份；RECHECK ≠ 已经是新交易：[`../../tracks/implementation/worked-example-checktxstate-vs-execute.md`](../../tracks/implementation/worked-example-checktxstate-vs-execute.md)（不变量 312）。内存池去重 ≠ 已经保证不重放；过了 CheckTx ≠ 已经有应用级保护；通常不受欢迎 ≠ 已经没有幂等例外：[`../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md`](../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md)（不变量 313）。QueryState ≠ 已经是 ExecuteTxState；上次 Commit ≠ 已经跟上正在跑的块；启动对齐 ≠ 已经是快照重放：[`../../tracks/implementation/worked-example-querystate-vs-execute.md`](../../tracks/implementation/worked-example-querystate-vs-execute.md)（不变量 314）。MaxGas ≠ 已经在执行；GasUsed ≠ 已经算进共识；已提交块 ≠ 已经按气验过：[`../../tracks/implementation/worked-example-maxgas-vs-enforced.md`](../../tracks/implementation/worked-example-maxgas-vs-enforced.md)（不变量 315）。结果列表 ≠ 已经同一顺序；Code 非零 ≠ 已经没进块；Code / Data ≠ 已经印进本头：[`../../tracks/implementation/worked-example-exectxresult-vs-consensus.md`](../../tracks/implementation/worked-example-exectxresult-vs-consensus.md)（不变量 316）。CheckTx 的 Data ≠ 已经被引擎用了；各节点 Data 不一样 ≠ 已经分叉；Priority ≠ 已经是共识顺序：[`../../tracks/implementation/worked-example-checktxresponse-vs-exec.md`](../../tracks/implementation/worked-example-checktxresponse-vs-exec.md)（不变量 317）。不要抄长度前缀。不要写怎样开套接字或怎样编 protobuf。不要另写怎样加锁或怎样调广播。不要另写怎样缓存候选或怎样算头哈希。不要另写怎样实现 CheckTx 或怎样再验。不要另写怎样实现重放保护或怎样做索引器。不要另写怎样实现 QueryState 或怎样做 state sync。不要另写怎样计量气或怎样在 Prepare 里卡上限。不要另写怎样编回执或怎样建索引。不要另写怎样实现 Priority 或怎样编 Data。InitChain 空名单 ≠ 已经没有集合；同一批重复公钥 ≠ 已经能恢复；power 0 ≠ 已经删掉不在集合里的人：[`../../tracks/implementation/worked-example-validatorupdate-vs-set.md`](../../tracks/implementation/worked-example-validatorupdate-vs-set.md)（不变量 318）。不要另写怎样编 `ValidatorUpdate` 或怎样算总权。InitChain 空参数 ≠ 已经没有参数；Finalize 没回 ≠ 已经清掉；只改一个字段 ≠ 已经只改这一项：[`../../tracks/implementation/worked-example-consensusparams-vs-update.md`](../../tracks/implementation/worked-example-consensusparams-vs-update.md)（不变量 319）。不要另写怎样编 `ConsensusParams` 或怎样选上限。应用高度比引擎高 ≠ 已经允许；块进 store ≠ 已经 Commit；启动 Info 对上 ≠ 已经能跳步：[`../../tracks/implementation/worked-example-crash-steps-vs-commit.md`](../../tracks/implementation/worked-example-crash-steps-vs-commit.md)（不变量 320）。不要另写怎样落盘或怎样写 Commit。Offer 收下 ≠ 已经装完；一块 chunk 收下 ≠ 已经齐；拉失败换一份 ≠ 已经能接着装：[`../../tracks/implementation/worked-example-snapshot-restore-vs-offer.md`](../../tracks/implementation/worked-example-snapshot-restore-vs-offer.md)（不变量 321）。不要另写怎样切块或怎样装。ListSnapshots 回了 ≠ 已经有了全部快照；挑了最高 ≠ 已经收下；Offer 被拒 ≠ 已经停：[`../../tracks/implementation/worked-example-snapshot-discover-vs-offer.md`](../../tracks/implementation/worked-example-snapshot-discover-vs-offer.md)（不变量 322）。不要另写怎样列快照或怎样挑。装完 ≠ 已经有了 ChainID；AppHash 对上 ≠ 已经版本也对上；切进共识 ≠ 已经有完整历史：[`../../tracks/implementation/worked-example-snapshot-switch-vs-history.md`](../../tracks/implementation/worked-example-snapshot-switch-vs-history.md)（不变量 323）。不要另写怎样切到共识或怎样配扩展。拍了这个高度 ≠ 已经交差之后拍的：[`../../tracks/implementation/worked-example-snapshot-take-vs-commit.md`](../../tracks/implementation/worked-example-snapshot-take-vs-commit.md)（不变量 324）。看见没停链不是已经一致。看见只留最近两份不是已经有了全部历史快照。不要另写怎样拍快照或怎样切块。头上有 AppHash ≠ 已经是交易默克尔：[`../../tracks/implementation/worked-example-query-proof-vs-apphash.md`](../../tracks/implementation/worked-example-query-proof-vs-apphash.md)（不变量 325）。看见 Query 回了 Proof 不是已经对上 AppHash。看见一层 ProofOp 的根不是已经对上最终 AppHash。不要另写怎样编证明或怎样种树。发了 addr 过滤查询 ≠ 已经收下这个人：[`../../tracks/implementation/worked-example-peerfilter-vs-query.md`](../../tracks/implementation/worked-example-peerfilter-vs-query.md)（不变量 326）。看见 id 过滤查询绿了不是已经过了 addr。看见有 /store 路径不是已经是引擎在用。不要另写怎样写过滤或怎样配路径。立刻整块执行不是已经离开关键路径：[`../../tracks/implementation/worked-example-prepare-timeout-vs-liveness.md`](../../tracks/implementation/worked-example-prepare-timeout-vs-liveness.md)（不变量 327）。看见填了 TimeoutPropose 不是已经装得下。看见又开一轮不是已经丢了活性。不要另写怎样设 TimeoutPropose 或怎样抄默认秒数。同一高度回了不同码不是已经有了 CheckTxCode：[`../../tracks/implementation/worked-example-checktx-oscillate-vs-stable.md`](../../tracks/implementation/worked-example-checktx-oscillate-vs-stable.md)（不变量 328）。看见还在振荡不是已经过了 h_stable。看见本地不再振荡不是已经各节点同一份 b。不要另写怎样实现 CheckTx 或怎样挑稳定高度。Query 回了不是已经复制到各节点：[`../../tracks/implementation/worked-example-query-vs-replicated.md`](../../tracks/implementation/worked-example-query-vs-replicated.md)（不变量 329）。看见查到了不是已经新鲜。看见实现了 Query 不是已经是正常运转必须有。不要另写怎样写 Query 或怎样配 RPC。到了 H ≠ 已经 Prepare 带了扩展：[`../../tracks/implementation/worked-example-ve-height-vs-prepare.md`](../../tracks/implementation/worked-example-ve-height-vs-prepare.md)（不变量 330）。看见 H+1 带了扩展不是已经是本高度刚签的。看见 h < H 带了扩展不是已经合法。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。填了证据 MaxBytes ≠ 已经落在块上限下面：[`../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md`](../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md)（不变量 331）。看见 > 0 不是已经盖住解绑。看见证据 MaxBytes 不是已经是块 MaxBytes。不要另写怎样设 EvidenceParams.MaxBytes 或怎样算块开销。装完又对上 LastBlockAppHash ≠ 已经在装回当中验过：[`../../tracks/implementation/worked-example-snapshot-verify-vs-early.md`](../../tracks/implementation/worked-example-snapshot-verify-vs-early.md)（不变量 332）。看见增量验了 chunk 不是已经是唯一可信的 AppHash。看见封禁邻居不是已经没有快照 DoS。不要另写怎样做增量默克尔证明或怎样配受信邻居。本高回了 ConsensusParams ≠ 已经在本高生效：[`../../tracks/implementation/worked-example-params-delay-vs-set.md`](../../tracks/implementation/worked-example-params-delay-vs-set.md)（不变量 333）。看见 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票。看见参数更新写了 H+1 不是已经是扩展启用高度那种切换，也不是已经只改填的那一项。不要另写怎样编 ConsensusParams 或怎样选启用高度。四门里有 Snapshot Connection ≠ 已经必须实现快照：[`../../tracks/implementation/worked-example-snapshot-conn-vs-required.md`](../../tracks/implementation/worked-example-snapshot-conn-vs-required.md)（不变量 334）。看见给人快照或给自己装回不是已经必须两头都做。看见应用选择不实现不是已经没有 state sync 这条对象。不要另写怎样实现快照方法或怎样配 state sync。Finalize 改了状态 ≠ 已经落盘：[`../../tracks/implementation/worked-example-finalize-persist-vs-commit.md`](../../tracks/implementation/worked-example-finalize-persist-vs-commit.md)（不变量 335）。看见必须在 Commit 落盘不是已经在 Finalize 落了。看见记住上次成功 Commit 高度不是已经能跳步。不要另写怎样落盘或怎样写 Commit。填了 Precision ≠ 已经是 MessageDelay：[`../../tracks/implementation/worked-example-precision-vs-msgdelay.md`](../../tracks/implementation/worked-example-precision-vs-msgdelay.md)（不变量 336）。看见填了两个不是已经启用 PBTS。看见用于 PBTS 不是已经是永恒常数。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。-1 就按 100 MB 验 ≠ 已经没有上限：[`../../tracks/implementation/worked-example-maxbytes-cap-vs-unlimited.md`](../../tracks/implementation/worked-example-maxbytes-cap-vs-unlimited.md)（不变量 337）。看见应用自己卡体积不是已经引擎不管了。看见必须 -1 或不超过 100 MB 不是已经是默认 21 MB。不要另写怎样设 MaxBytes 或怎样算块开销。Prepare 没有确定性要求不是已经必须确定：[`../../tracks/implementation/worked-example-prepare-nondet-vs-process.md`](../../tracks/implementation/worked-example-prepare-nondet-vs-process.md)（不变量 338）。看见两边 raw 一样不是已经是同一份提案。看见 ExtendVote 没有确定性要求不是已经是同一份扩展。不要另写怎样写 Prepare 或怎样写 ExtendVote。不该验排序相关有效性不是已经该在 CheckTx 里验：[`../../tracks/implementation/worked-example-checktx-weak-vs-process.md`](../../tracks/implementation/worked-example-checktx-weak-vs-process.md)（不变量 339）。看见拜占庭能提案一满块无效交易不是已经被池子挡住。看见 ProcessProposal 对付这种行为不是已经是 CheckTx。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值：[`../../tracks/implementation/worked-example-process-det-vs-prepare.md`](../../tracks/implementation/worked-example-process-det-vs-prepare.md)（不变量 340）。看见两边对任意块同一裁决不是已经只对诚实提案同一裁决。看见 Process 非确定 bug 没有现成解法不是已经丢了安全性。不要另写怎样写 ProcessProposal。Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值：[`../../tracks/implementation/worked-example-verify-det-vs-extend.md`](../../tracks/implementation/worked-example-verify-det-vs-extend.md)（不变量 341）。看见两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决。看见 Verify 非确定会伤活性不是已经丢了安全性。不要另写怎样写 VerifyVoteExtension。Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值：[`../../tracks/implementation/worked-example-finalize-det-vs-prepare.md`](../../tracks/implementation/worked-example-finalize-det-vs-prepare.md)（不变量 342）。看见 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头。看见两边状态机复制不是已经是 Process 对任意块同一裁决。不要另写怎样写 FinalizeBlock。写成 0 不是已经启用 PBTS 不是已经填了 Precision 就是 PBTS：[`../../tracks/implementation/worked-example-pbts-height-vs-params.md`](../../tracks/implementation/worked-example-pbts-height-vs-params.md)（不变量 343）。看见 H 之前仍用 BFT Time 不是已经切到 PBTS。看见启用之后不能关不是已经是扩展启用高度那种切换。不要另写怎样设 PbtsEnableHeight。MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易：[`../../tracks/implementation/worked-example-maxbytes-overhead-vs-full.md`](../../tracks/implementation/worked-example-maxbytes-overhead-vs-full.md)（不变量 344）。看见诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB。看见 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行。不要另写怎样算头和证据开销。整池可见不是已经只能看见装得进一块的子集：[`../../tracks/implementation/worked-example-prepare-return-vs-pool.md`](../../tracks/implementation/worked-example-prepare-return-vs-pool.md)（不变量 345）。看见聚合体积可以超过 max_tx_bytes 不是已经能回超限列表。看见 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁。不要另写怎样裁回包。必须协调升级不是已经只改 VoteExtensionsEnableHeight：[`../../tracks/implementation/worked-example-abci20-upgrade-vs-height.md`](../../tracks/implementation/worked-example-abci20-upgrade-vs-height.md)（不变量 346）。看见 h_e 必须高于当前不是已经能写成当前高度。看见引擎按当前高度决定存什么要什么不是已经按创世配好了。不要另写怎样做协调升级。正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept：[`../../tracks/implementation/worked-example-req3-coherence-vs-accept.md`](../../tracks/implementation/worked-example-req3-coherence-vs-accept.md)（不变量 347）。看见 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题。看见 Req 3 是大量测试和自动验证的目标不是已经测过。不要另写怎样写 Prepare 或 Process。正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept：[`../../tracks/implementation/worked-example-req6-coherence-vs-accept.md`](../../tracks/implementation/worked-example-req6-coherence-vs-accept.md)（不变量 348）。看见 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题。看见会面对和 Req 5 同一类活性问题不是已经丢了安全性。不要另写怎样写 Extend 或 Verify。Prepare 不得改已提交状态不是已经立刻执行就已经交差：[`../../tracks/implementation/worked-example-req9-noside-vs-commit.md`](../../tracks/implementation/worked-example-req9-noside-vs-commit.md)（不变量 349）。看见 Process 不得改已提交状态不是已经 Accept 就已经改了。看见 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态。一轮最多一张 Precommit 不是已经能再签一张：[`../../tracks/implementation/worked-example-extend-once-vs-round.md`](../../tracks/implementation/worked-example-extend-once-vs-round.md)（不变量 350）。看见 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票。看见一轮只能交出一份扩展不是已经是每一高度一份。Process 也会在提议者那边叫不是已经不用再 Process：[`../../tracks/implementation/worked-example-process-also-vs-prepare.md`](../../tracks/implementation/worked-example-process-also-vs-prepare.md)（不变量 351）。看见通常紧跟 Prepare、列表对得上不是已经保证是这一次。看见失败时可能对上更早一次或根本不调不是已经每轮都会叫。+2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过：[`../../tracks/implementation/worked-example-late-extension-vs-verified.md`](../../tracks/implementation/worked-example-late-extension-vs-verified.md)（不变量 352）。看见建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify。看见下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify。空扩展仍会调 Verify 不是已经跳过 Verify：[`../../tracks/implementation/worked-example-verify-when-vs-empty.md`](../../tracks/implementation/worked-example-verify-when-vs-empty.md)（不变量 353）。看见不对本进程自己发出的 Precommit 调用不是已经自己验过。看见请求里的 hash 不是已经对该块跑过 Process。Process 调用是同步的不是已经能在返回之后再改裁决：[`../../tracks/implementation/worked-example-process-when-vs-later.md`](../../tracks/implementation/worked-example-process-when-vs-later.md)（不变量 354）。看见只做基本检查再异步 Process 不是已经还能再 Reject。看见非验证者可以立刻回 ACCEPT 不是已经验过这块。从提案拿掉 tx 不是已经从内存池删掉：[`../../tracks/implementation/worked-example-prepare-drop-vs-mempool.md`](../../tracks/implementation/worked-example-prepare-drop-vs-mempool.md)（不变量 355）。看见往提案加了一笔新的不是已经进了内存池。看见把 t1 改成 t2 不是已经还能按 t1 查到。validValue 非 nil 不是已经还会调 Prepare：[`../../tracks/implementation/worked-example-validvalue-vs-prepare.md`](../../tracks/implementation/worked-example-validvalue-vs-prepare.md)（不变量 356）。看见自己是提议者不是已经每轮都会调 Prepare。看见没调 Prepare 不是已经又装了一份 raw 提案。引擎没有再验重复交易不是已经验过重复：[`../../tracks/implementation/worked-example-prepare-valid-vs-checked.md`](../../tracks/implementation/worked-example-prepare-valid-vs-checked.md)（不变量 357）。看见 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT。看见 Prepare 里产出了事件不是已经交给引擎。vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签：[`../../tracks/implementation/worked-example-nonrp-vs-wrapped.md`](../../tracks/implementation/worked-example-nonrp-vs-wrapped.md)（不变量 358）。看见 non_rp_extension 按原样签不是已经有重放保护。看见应用要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份。Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process：[`../../tracks/implementation/worked-example-prepare-fields-vs-same.md`](../../tracks/implementation/worked-example-prepare-fields-vs-same.md)（不变量 359）。看见 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展。看见 height / time / proposer_address 对上拟议头不是已经知道本头哈希。至少一名非拜占庭验证者跑过 Process 不是已经每个验证者都跑过 Process：[`../../tracks/implementation/worked-example-finalize-vs-processed.md`](../../tracks/implementation/worked-example-finalize-vs-processed.md)（不变量 360）。看见 Finalize 请求把字段再填一遍不是已经不用再给。看见可以套用先前候选不是已经是 ExecuteTxState。+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote：[`../../tracks/implementation/worked-example-extend-when-vs-locked.md`](../../tracks/implementation/worked-example-extend-when-vs-locked.md)（不变量 361）。看见 ExtendVote 调用是同步的不是已经能在返回之后再改扩展。看见回包字节不被共识算法解释不是已经是同一份扩展。+2/3 precommit 同一 id(v) 才决定再调 Finalize 不是已经会调 Finalize：[`../../tracks/implementation/worked-example-finalize-when-vs-decided.md`](../../tracks/implementation/worked-example-finalize-when-vs-decided.md)（不变量 362）。看见先把 v 落成这一高的决定再同步调 Finalize 不是已经交差。看见应用回了 AppHash 和各笔输出不是已经印进本头。Finalize 等价于 ABCI 1.0 那三步不是已经是四门已经结算：[`../../tracks/implementation/worked-example-finalize-equiv-vs-gates.md`](../../tracks/implementation/worked-example-finalize-equiv-vs-gates.md)（不变量 363）。看见可以用 decided_last_commit 和 misbehavior 定奖惩不是已经罚没。看见必须回四列不是已经改了集合。看见 ValidatorUpdate 用公钥认人不是已经改了集合。看见按投票权降序排不是已经进了块。看见全网都删了会永久丢不是已经能从创世再装。看见优先级 0 留给不设道不是已经进了块。看见空快照也至少 1 块不是已经齐。看见扩展关掉则字段全空不是已经到了启用高度。看见 last_block_app_hash / last_block_height 要在 Commit 里落盘不是已经交差。看见 Query 可以对当前或过去高度查不是已经是 QueryState。看见 height 默认 0 回最新已提交不是已经新鲜。看见这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash。看见 Misbehavior.type 只是过错枚举不是已经罚没。看见 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间。看见 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩。看见 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算。看见 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块。看见引擎对回包码不再赋予别的含义不是已经被引擎用了 Data。看见 Flush 要把客户端排队的消息冲到服务端不是已经送到。看见定期 Flush 是为了让异步请求真发出去不是已经是四门。看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走。不要另写怎样写 Flush。看见 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐。看见请求用 height / format / chunk（从 0 起）认这块不是已经是同一份。看见回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB。不要另写怎样写 LoadSnapshotChunk。看见 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算。看见 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差。看见 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决。不要另写怎样写 ProposalStatus。看见 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度。看见 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用。看见规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有。不要另写怎样写 Query 路径。看见应用可以再拉块或封邻居、引擎不自己做不是已经封了。看见 refetch_chunks 不论 result 都再拉再装、按顺序不是已经齐。看见 reject_senders 不论 Result 都拒这些人、已装的不重拉除非点名不是已经能接着装。不要另写怎样写 ApplySnapshotChunk。看见 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version。看见 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上。看见 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐。不要另写怎样写 Info 请求版本。看见 Query 回包 index 是树里这个键的下标不是已经是按键查。看见 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度。看见 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash。不要另写怎样写 Query 回包。看见 CheckTx 回包 codespace 是码的命名空间不是已经是回包码。看见 CheckTx 回包 events 是给索引用的类型键值不是已经交差。看见 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道。不要另写怎样写 CheckTx 回包。看见 syncing_to_height 同步或重放时是目标高、否则等于本高不是已经有完整历史。看见 validator_updates 空则引擎保持当前集合不是已经没有集合。看见 Finalize 回包 events 标成非确定不是已经必须确定。看见 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash。看见 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查。看见 Query 回包 height 是数据来自哪一高不是已经是请求高度。看见 Query 回包 code 是回包码不是已经过了共识。看见 Query 回包 log 是应用日志输出不是已经新鲜。看见 Query 回包 info 是附加信息不是已经是按键查。看见 ConsensusParams.block 限制块大小和块间隔不是已经是 MaxBytes 上限。看见 ConsensusParams.validator 限制验证者公钥类型不是已经带了公钥。看见 ConsensusParams.version 是 ABCI 应用版本不是已经是 app_version 进了头。看见 ConsensusParams.evidence 限制拜占庭证据是否合法不是已经是证据 MaxBytes。看见 ConsensusParams.abci 是 ABCI 相关参数不是已经 Prepare 带了扩展。看见 ConsensusParams.synchrony 定提案时间戳合法界不是已经是 PBTS。看见 InitChain 请求 time 是创世时间不是已经过了 genesis_time。看见 InitChain 请求 chain_id 是链的 ID 不是已经有了 ChainID。看见 InitChain 请求 initial_height 是起步块高度不是已经能跳步。不要另写怎样写 InitChain 请求。
