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

一句话：

> 用部分同步下的 BFT 投票 + 锁，为每个高度选出至多一个确定最终的块，并通过 ABCI 把应用状态机和共识引擎分开。
