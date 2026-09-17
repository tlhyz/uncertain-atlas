# Kaspa 协议档案

优先级：进阶（独特思想：区块 DAG 消化孤块）  
完整报告：[`report.md`](report.md)

一句话：

> 允许许多块并行长在 DAG 上，再用 GHOSTDAG 一类规则选出可执行的全序，让「同时出的块」不必像 Bitcoin 那样多数作废。进了某个块不是已经在 selected chain。精读：[`../../tracks/consensus/worked-example-dag-vs-selected-chain.md`](../../tracks/consensus/worked-example-dag-vs-selected-chain.md)（不变量 137）。
