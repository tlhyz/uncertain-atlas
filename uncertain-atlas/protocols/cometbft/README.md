# Cosmos / CometBFT 协议档案

优先级：必学（「不确定」主骨架）  
完整报告：[`report.md`](report.md)

IBC 不是本档案的共识对象。若对照，客户端 ≠ 连接 ≠ 通道 ≠ 数据包已送达：[`../../tracks/economic/worked-example-ibc-client-vs-packet.md`](../../tracks/economic/worked-example-ibc-client-vs-packet.md)（不变量 146）。源链托管 ≠ 对岸已经铸出原币：[`../../tracks/economic/worked-example-escrow-vs-voucher.md`](../../tracks/economic/worked-example-escrow-vs-voucher.md)（不变量 155）。不另写 19 节。

本头 `AppHash` 不是本高度交易已经交差：[`../../tracks/consensus/worked-example-apphash-vs-this-block.md`](../../tracks/consensus/worked-example-apphash-vs-this-block.md)（不变量 147）。本头 `LastCommit` 不是本高度已经 +2/3：[`../../tracks/consensus/worked-example-lastcommit-vs-this-block.md`](../../tracks/consensus/worked-example-lastcommit-vs-this-block.md)（不变量 148）。

一句话：

> 用部分同步下的 BFT 投票 + 锁，为每个高度选出至多一个确定最终的块，并通过 ABCI 把应用状态机和共识引擎分开。
