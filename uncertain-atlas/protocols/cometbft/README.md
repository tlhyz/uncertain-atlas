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

一句话：

> 用部分同步下的 BFT 投票 + 锁，为每个高度选出至多一个确定最终的块，并通过 ABCI 把应用状态机和共识引擎分开。
