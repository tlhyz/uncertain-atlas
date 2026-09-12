# Cosmos / CometBFT 协议档案

优先级：必学（「不确定」主骨架）  
完整报告：[`report.md`](report.md)

IBC 不是本档案的共识对象。若对照，客户端 ≠ 连接 ≠ 通道 ≠ 数据包已送达：[`../../tracks/economic/worked-example-ibc-client-vs-packet.md`](../../tracks/economic/worked-example-ibc-client-vs-packet.md)（不变量 146）。源链托管 ≠ 对岸已经铸出原币：[`../../tracks/economic/worked-example-escrow-vs-voucher.md`](../../tracks/economic/worked-example-escrow-vs-voucher.md)（不变量 155）。不另写 19 节。

本头 `AppHash` 不是本高度交易已经交差：[`../../tracks/consensus/worked-example-apphash-vs-this-block.md`](../../tracks/consensus/worked-example-apphash-vs-this-block.md)（不变量 147）。本头 `LastCommit` 不是本高度已经 +2/3：[`../../tracks/consensus/worked-example-lastcommit-vs-this-block.md`](../../tracks/consensus/worked-example-lastcommit-vs-this-block.md)（不变量 148）。

写下每条消息不是已经 fsync：[`../../tracks/implementation/worked-example-wal-vs-signed.md`](../../tracks/implementation/worked-example-wal-vs-signed.md)（不变量 298）。看见回放时又要签不是已经双签。看见 LastSignBytes 对上不是已经换了高度。

先装证据不是已经装满交易：[`../../tracks/consensus/worked-example-evidence-vs-reap.md`](../../tracks/consensus/worked-example-evidence-vs-reap.md)（不变量 299）。看见两条收交易上限不是已经同一条。看见 MaxBytes 写成 -1 不是已经没有上限。

本地 State 不是已经进了块：[`../../tracks/implementation/worked-example-state-vs-gossip.md`](../../tracks/implementation/worked-example-state-vs-gossip.md)（不变量 300）。看见头上的根不是已经有了 State。看见能读本地 State 不是已经进了规范。

提案收了交易不是已经从池里删掉：[`../../tracks/mempool/worked-example-proposed-vs-removed.md`](../../tracks/mempool/worked-example-proposed-vs-removed.md)（不变量 301）。看见本块已 commit 不是已经不用再验剩下的。看见 CheckTx 过了不是已经永远有效。

同一高度换轮不是已经换了集合：[`../../tracks/consensus/worked-example-round-vs-set.md`](../../tracks/consensus/worked-example-round-vs-set.md)（不变量 302）。看见新验证者加进来不是已经能跳到队头。看见优先级差被缩放不是已经按人头轮。

创世 app_state 不是已经验过应用状态：[`../../tracks/implementation/worked-example-genesis-vs-app.md`](../../tracks/implementation/worked-example-genesis-vs-app.md)（不变量 303）。看见节点起来不是已经过了 genesis_time。看见创世 validators 空不是已经没有集合。

票上 Timestamp 不是已经验过：[`../../tracks/consensus/worked-example-vote-ts-vs-checked.md`](../../tracks/consensus/worked-example-vote-ts-vs-checked.md)（不变量 304）。看见冲突提案不是已经有证据。看见非法票被断开不是已经罚了签的人。

InitPeer 不是已经能跟它对说：[`../../tracks/network/worked-example-initpeer-vs-addpeer.md`](../../tracks/network/worked-example-initpeer-vs-addpeer.md)（不变量 305）。看见已经在 Receive 不是已经过了 AddPeer。看见节点已经在跑不是已经能再登记一个反应堆。

Peer 句柄不是已经是那个人：[`../../tracks/network/worked-example-peer-handler-vs-node.md`](../../tracks/network/worked-example-peer-handler-vs-node.md)（不变量 306）。看见 Broadcast 回了通道不是已经送到每一家。看见 StopPeerForError 不是已经对持久邻居也断干净。

同进程不是已经有套接字隔离：[`../../tracks/implementation/worked-example-abci-conn-vs-gates.md`](../../tracks/implementation/worked-example-abci-conn-vs-gates.md)（不变量 307）。看见 gRPC 最容易不是已经高性能。看见一条连接不是已经够用，也不是已经是四门。

NumPeers 不是已经数完所有邻居：[`../../tracks/network/worked-example-numpeers-vs-all.md`](../../tracks/network/worked-example-numpeers-vs-all.md)（不变量 308）。看见能按名字拿到反应堆不是已经独立。看见 PeerState 不是已经验过高度。

HasChannel 为真不是已经入队：[`../../tracks/network/worked-example-send-vs-enqueued.md`](../../tracks/network/worked-example-send-vs-enqueued.md)（不变量 309）。看见 Send 回了假不是已经断开。看见 TrySend 回了假不是已经和 Send 同一把尺。

默认 Go 有全局锁不是已经能把状态直接给 RPC：[`../../tracks/implementation/worked-example-commit-lock-vs-rpc.md`](../../tracks/implementation/worked-example-commit-lock-vs-rpc.md)（不变量 310）。看见 Commit 前锁了内存池不是已经解锁。看见 Commit 里等 broadcast_tx 不是已经能往下走。

立刻执行出候选不是已经是 ExecuteTxState：[`../../tracks/implementation/worked-example-candidate-vs-execute.md`](../../tracks/implementation/worked-example-candidate-vs-execute.md)（不变量 311）。看见 Prepare 里没有头哈希不是已经知道本头。看见丢掉候选不是已经永远不用再执行。

CheckTx 过了不是已经按 ExecuteTxState 验过：[`../../tracks/implementation/worked-example-checktxstate-vs-execute.md`](../../tracks/implementation/worked-example-checktxstate-vs-execute.md)（不变量 312）。看见两份状态同时在改不是已经同一份。看见 Type 是 RECHECK 不是已经是一笔新交易。

内存池会挡重复不是已经保证不重放：[`../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md`](../../tracks/implementation/worked-example-mempool-indexer-vs-replay.md)（不变量 313）。看见过了 CheckTx 不是已经有应用级保护。看见通常不受欢迎不是已经没有幂等例外。

QueryState 不是已经是 ExecuteTxState：[`../../tracks/implementation/worked-example-querystate-vs-execute.md`](../../tracks/implementation/worked-example-querystate-vs-execute.md)（不变量 314）。看见上次 Commit 不是已经跟上正在跑的块。看见启动对齐不是已经是快照重放。

MaxGas 不是已经在执行：[`../../tracks/implementation/worked-example-maxgas-vs-enforced.md`](../../tracks/implementation/worked-example-maxgas-vs-enforced.md)（不变量 315）。看见 GasUsed 不是已经算进共识。看见已提交块不是已经按气验过。

结果列表不是已经同一顺序：[`../../tracks/implementation/worked-example-exectxresult-vs-consensus.md`](../../tracks/implementation/worked-example-exectxresult-vs-consensus.md)（不变量 316）。看见 Code 非零不是已经没进块。看见 Code / Data 不是已经印进本头。

CheckTx 的 Data 不是已经被引擎用了：[`../../tracks/implementation/worked-example-checktxresponse-vs-exec.md`](../../tracks/implementation/worked-example-checktxresponse-vs-exec.md)（不变量 317）。看见各节点 Data 不一样不是已经分叉。看见 Priority 不是已经是共识顺序。

InitChain 空名单不是已经没有集合：[`../../tracks/implementation/worked-example-validatorupdate-vs-set.md`](../../tracks/implementation/worked-example-validatorupdate-vs-set.md)（不变量 318）。看见同一批重复公钥不是已经能恢复。看见 power 写成 0 不是已经删掉不在集合里的人。

InitChain 空参数不是已经没有参数：[`../../tracks/implementation/worked-example-consensusparams-vs-update.md`](../../tracks/implementation/worked-example-consensusparams-vs-update.md)（不变量 319）。看见 Finalize 没回不是已经清掉。看见只改一个字段不是已经只改这一项。

应用高度比引擎高不是已经允许：[`../../tracks/implementation/worked-example-crash-steps-vs-commit.md`](../../tracks/implementation/worked-example-crash-steps-vs-commit.md)（不变量 320）。看见块进了 blockstore 不是已经 Commit。看见启动 Info 对上不是已经能跳步。

Offer 收下不是已经装完：[`../../tracks/implementation/worked-example-snapshot-restore-vs-offer.md`](../../tracks/implementation/worked-example-snapshot-restore-vs-offer.md)（不变量 321）。看见一块 chunk 收下不是已经齐。看见拉失败换一份不是已经能接着装。

ListSnapshots 回了不是已经有了全部快照：[`../../tracks/implementation/worked-example-snapshot-discover-vs-offer.md`](../../tracks/implementation/worked-example-snapshot-discover-vs-offer.md)（不变量 322）。看见挑了最高不是已经收下。看见 Offer 被拒不是已经停。

装完不是已经有了 ChainID：[`../../tracks/implementation/worked-example-snapshot-switch-vs-history.md`](../../tracks/implementation/worked-example-snapshot-switch-vs-history.md)（不变量 323）。看见 Info 的 AppHash 对上不是已经版本也对上。看见切进共识不是已经有从创世的完整历史。

拍了这个高度不是已经交差之后拍的：[`../../tracks/implementation/worked-example-snapshot-take-vs-commit.md`](../../tracks/implementation/worked-example-snapshot-take-vs-commit.md)（不变量 324）。看见没停链不是已经一致。看见只留最近两份不是已经有了全部历史快照。

头上有 AppHash 不是已经是交易默克尔：[`../../tracks/implementation/worked-example-query-proof-vs-apphash.md`](../../tracks/implementation/worked-example-query-proof-vs-apphash.md)（不变量 325）。看见 Query 回了 Proof 不是已经对上 AppHash。看见一层 ProofOp 的根不是已经对上最终 AppHash。

发了 addr 过滤查询不是已经收下这个人：[`../../tracks/implementation/worked-example-peerfilter-vs-query.md`](../../tracks/implementation/worked-example-peerfilter-vs-query.md)（不变量 326）。看见 id 过滤查询绿了不是已经过了 addr。看见有 /store 路径不是已经是引擎在用。

立刻整块执行不是已经离开关键路径：[`../../tracks/implementation/worked-example-prepare-timeout-vs-liveness.md`](../../tracks/implementation/worked-example-prepare-timeout-vs-liveness.md)（不变量 327）。看见填了 TimeoutPropose 不是已经装得下。看见又开一轮不是已经丢了活性。

同一高度回了不同码不是已经有了 CheckTxCode：[`../../tracks/implementation/worked-example-checktx-oscillate-vs-stable.md`](../../tracks/implementation/worked-example-checktx-oscillate-vs-stable.md)（不变量 328）。看见还在振荡不是已经过了 h_stable。看见本地不再振荡不是已经各节点同一份 b。

Query 回了不是已经复制到各节点：[`../../tracks/implementation/worked-example-query-vs-replicated.md`](../../tracks/implementation/worked-example-query-vs-replicated.md)（不变量 329）。看见查到了不是已经新鲜。看见实现了 Query 不是已经是正常运转必须有。

到了 H 不是已经 Prepare 带了扩展：[`../../tracks/implementation/worked-example-ve-height-vs-prepare.md`](../../tracks/implementation/worked-example-ve-height-vs-prepare.md)（不变量 330）。看见 H+1 带了扩展不是已经是本高度刚签的。看见 h < H 带了扩展不是已经合法。

填了证据 MaxBytes 不是已经落在块上限下面：[`../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md`](../../tracks/implementation/worked-example-evidence-maxbytes-vs-block.md)（不变量 331）。看见 > 0 不是已经盖住解绑。看见证据 MaxBytes 不是已经是块 MaxBytes。

装完又对上 LastBlockAppHash 不是已经在装回当中验过：[`../../tracks/implementation/worked-example-snapshot-verify-vs-early.md`](../../tracks/implementation/worked-example-snapshot-verify-vs-early.md)（不变量 332）。看见增量验了 chunk 不是已经是唯一可信的 AppHash。看见封禁邻居不是已经没有快照 DoS。

本高回了 ConsensusParams 不是已经在本高生效：[`../../tracks/implementation/worked-example-params-delay-vs-set.md`](../../tracks/implementation/worked-example-params-delay-vs-set.md)（不变量 333）。看见 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票。看见参数更新写了 H+1 不是已经是扩展启用高度那种切换，也不是已经只改填的那一项。

四门里有 Snapshot Connection 不是已经必须实现快照：[`../../tracks/implementation/worked-example-snapshot-conn-vs-required.md`](../../tracks/implementation/worked-example-snapshot-conn-vs-required.md)（不变量 334）。看见给人快照或给自己装回不是已经必须两头都做。看见应用选择不实现不是已经没有 state sync 这条对象。

Finalize 改了状态不是已经落盘：[`../../tracks/implementation/worked-example-finalize-persist-vs-commit.md`](../../tracks/implementation/worked-example-finalize-persist-vs-commit.md)（不变量 335）。看见必须在 Commit 落盘不是已经在 Finalize 落了。看见记住上次成功 Commit 高度不是已经能跳步。

填了 Precision 不是已经是 MessageDelay：[`../../tracks/implementation/worked-example-precision-vs-msgdelay.md`](../../tracks/implementation/worked-example-precision-vs-msgdelay.md)（不变量 336）。看见填了两个不是已经启用 PBTS。看见用于 PBTS 不是已经是永恒常数。

-1 就按 100 MB 验不是已经没有上限：[`../../tracks/implementation/worked-example-maxbytes-cap-vs-unlimited.md`](../../tracks/implementation/worked-example-maxbytes-cap-vs-unlimited.md)（不变量 337）。看见应用自己卡体积不是已经引擎不管了。看见必须 -1 或不超过 100 MB 不是已经是默认 21 MB。

Prepare 没有确定性要求不是已经必须确定：[`../../tracks/implementation/worked-example-prepare-nondet-vs-process.md`](../../tracks/implementation/worked-example-prepare-nondet-vs-process.md)（不变量 338）。看见两边 raw 一样不是已经是同一份提案。看见 ExtendVote 没有确定性要求不是已经是同一份扩展。

不该验排序相关有效性不是已经该在 CheckTx 里验：[`../../tracks/implementation/worked-example-checktx-weak-vs-process.md`](../../tracks/implementation/worked-example-checktx-weak-vs-process.md)（不变量 339）。看见拜占庭能提案一满块无效交易不是已经被池子挡住。看见 ProcessProposal 对付这种行为不是已经是 CheckTx。

Process 必须只依赖请求和上一份状态不是已经可以像 Prepare 那样依赖其它值：[`../../tracks/implementation/worked-example-process-det-vs-prepare.md`](../../tracks/implementation/worked-example-process-det-vs-prepare.md)（不变量 340）。看见两边对任意块同一裁决不是已经只对诚实提案同一裁决。看见 Process 非确定 bug 没有现成解法不是已经丢了安全性。

Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值：[`../../tracks/implementation/worked-example-verify-det-vs-extend.md`](../../tracks/implementation/worked-example-verify-det-vs-extend.md)（不变量 341）。看见两边对任意扩展同一裁决不是已经只对诚实扩展同一裁决。看见 Verify 非确定会伤活性不是已经丢了安全性。

Finalize 算出的状态必须只依赖上一份状态和决定块不是已经可以像 Prepare 那样依赖其它值：[`../../tracks/implementation/worked-example-finalize-det-vs-prepare.md`](../../tracks/implementation/worked-example-finalize-det-vs-prepare.md)（不变量 342）。看见 Finalize 算出的结果必须只依赖上一份状态和决定块不是已经是 Code/Data 印进本头。看见两边状态机复制不是已经是 Process 对任意块同一裁决。

写成 0 不是已经启用 PBTS 不是已经填了 Precision 就是 PBTS：[`../../tracks/implementation/worked-example-pbts-height-vs-params.md`](../../tracks/implementation/worked-example-pbts-height-vs-params.md)（不变量 343）。看见 H 之前仍用 BFT Time 不是已经切到 PBTS。看见启用之后不能关不是已经是扩展启用高度那种切换。

MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易：[`../../tracks/implementation/worked-example-maxbytes-overhead-vs-full.md`](../../tracks/implementation/worked-example-maxbytes-overhead-vs-full.md)（不变量 344）。看见诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB。看见 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行。

整池可见不是已经只能看见装得进一块的子集：[`../../tracks/implementation/worked-example-prepare-return-vs-pool.md`](../../tracks/implementation/worked-example-prepare-return-vs-pool.md)（不变量 345）。看见聚合体积可以超过 max_tx_bytes 不是已经能回超限列表。看见 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁。

必须协调升级不是已经只改 VoteExtensionsEnableHeight：[`../../tracks/implementation/worked-example-abci20-upgrade-vs-height.md`](../../tracks/implementation/worked-example-abci20-upgrade-vs-height.md)（不变量 346）。看见 h_e 必须高于当前不是已经能写成当前高度。看见引擎按当前高度决定存什么要什么不是已经按创世配好了。

正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept：[`../../tracks/implementation/worked-example-req3-coherence-vs-accept.md`](../../tracks/implementation/worked-example-req3-coherence-vs-accept.md)（不变量 347）。看见 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题。看见 Req 3 是大量测试和自动验证的目标不是已经测过。

正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept：[`../../tracks/implementation/worked-example-req6-coherence-vs-accept.md`](../../tracks/implementation/worked-example-req6-coherence-vs-accept.md)（不变量 348）。看见 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题。看见会面对和 Req 5 同一类活性问题不是已经丢了安全性。

Prepare 不得改已提交状态不是已经立刻执行就已经交差：[`../../tracks/implementation/worked-example-req9-noside-vs-commit.md`](../../tracks/implementation/worked-example-req9-noside-vs-commit.md)（不变量 349）。看见 Process 不得改已提交状态不是已经 Accept 就已经改了。看见 Extend 和 Verify 不得改已提交状态不是已经签了扩展就已经进状态。

一轮最多一张 Precommit 不是已经能再签一张：[`../../tracks/implementation/worked-example-extend-once-vs-round.md`](../../tracks/implementation/worked-example-extend-once-vs-round.md)（不变量 350）。看见 ExtendVote 只在即将广播非 nil Precommit 时才叫不是已经签了 nil 票。看见一轮只能交出一份扩展不是已经是每一高度一份。

Process 也会在提议者那边叫不是已经不用再 Process：[`../../tracks/implementation/worked-example-process-also-vs-prepare.md`](../../tracks/implementation/worked-example-process-also-vs-prepare.md)（不变量 351）。看见通常紧跟 Prepare、列表对得上不是已经保证是这一次。看见失败时可能对上更早一次或根本不调不是已经每轮都会叫。

+2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过：[`../../tracks/implementation/worked-example-late-extension-vs-verified.md`](../../tracks/implementation/worked-example-late-extension-vs-verified.md)（不变量 352）。看见建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify。看见下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify。

空扩展仍会调 Verify 不是已经跳过 Verify：[`../../tracks/implementation/worked-example-verify-when-vs-empty.md`](../../tracks/implementation/worked-example-verify-when-vs-empty.md)（不变量 353）。看见不对本进程自己发出的 Precommit 调用不是已经自己验过。看见请求里的 hash 不是已经对该块跑过 Process。

Process 调用是同步的不是已经能在返回之后再改裁决：[`../../tracks/implementation/worked-example-process-when-vs-later.md`](../../tracks/implementation/worked-example-process-when-vs-later.md)（不变量 354）。看见只做基本检查再异步 Process 不是已经还能再 Reject。看见非验证者可以立刻回 ACCEPT 不是已经验过这块。

从提案拿掉 tx 不是已经从内存池删掉：[`../../tracks/implementation/worked-example-prepare-drop-vs-mempool.md`](../../tracks/implementation/worked-example-prepare-drop-vs-mempool.md)（不变量 355）。看见往提案加了一笔新的不是已经进了内存池。看见把 t1 改成 t2 不是已经还能按 t1 查到。

validValue 非 nil 不是已经还会调 Prepare：[`../../tracks/implementation/worked-example-validvalue-vs-prepare.md`](../../tracks/implementation/worked-example-validvalue-vs-prepare.md)（不变量 356）。看见自己是提议者不是已经每轮都会调 Prepare。看见没调 Prepare 不是已经又装了一份 raw 提案。

一句话：

> 用部分同步下的 BFT 投票 + 锁，为每个高度选出至多一个确定最终的块，并通过 ABCI 把应用状态机和共识引擎分开。
