# 专题：共识

对照档案：

- [`../../protocols/bitcoin/report.md`](../../protocols/bitcoin/report.md)  
- [`../../protocols/cometbft/report.md`](../../protocols/cometbft/report.md)  
- [`../../protocols/avalanche/report.md`](../../protocols/avalanche/report.md)

| 家族 | 最终性 | 分区时 | 领导 | 主要假设 |
|---|---|---|---|---|
| Nakamoto | 概率 | 可两边长 | 矿工竞赛 | 多数算力诚实 |
| CometBFT | 确定 | 倾向停 | 轮值 proposer | <1/3 拜占庭 + 部分同步 |
| Avalanche | 概率固化 | 视参数 | 思想：无传统领袖；产品可有块生产者 | 抽样与参数 |
| Algorand | 论文下可快速最终（以规范为准） | 视同步假设 | VRF 抽签出的提议者 | VRF + 权益阈值 |

Avalanche 19 节见 [`../../protocols/avalanche/report.md`](../../protocols/avalanche/report.md)（思想 vs 产品层已有 leader，须分开）。Ethereum Gasper 见 L5.2，不要和 CometBFT commit 混成一张表。  
Algorand 抽签见 [`../../protocols/algorand/report.md`](../../protocols/algorand/report.md)，不要和 Avalanche 抽样写成同一种随机。

安全 / 活性 / 同步模型见 L0.6。锁见 CometBFT 档案与模式 locking-in-bft。
