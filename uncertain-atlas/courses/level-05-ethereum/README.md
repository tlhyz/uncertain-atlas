# Level 5 · Ethereum：可编程与多客户端

优先级：重要  
先修：L2.2 账户、L1.4 规范编码、L4.1 最终性对照（知道 CometBFT commit 长什么样）  
档案：[`../../protocols/ethereum/`](../../protocols/ethereum/README.md)

毕业：能解释「多个独立客户端如何仍对同一交易得到同一状态根」，并能把 head / justified / finalized 分开。

本课不教写 Solidity，不背官网 TPS。

| 课 | 文件 | 核心问题 |
|---|---|---|
| 5.1 | [L05-M01-evm-and-gas.md](L05-M01-evm-and-gas.md) | 任意程序如何仍是确定性状态机 |
| 5.2 | [L05-M02-el-cl-finality.md](L05-M02-el-cl-finality.md) | 执行层和共识层各保证什么；head ≠ justified ≠ finalized |
| 5.3 | [L05-M03-multi-client.md](L05-M03-multi-client.md) | 多实现为什么是药也是刀 |
| 5.4 | [L05-M04-state-blobs-mev.md](L05-M04-state-blobs-mev.md) | 状态胀了、blob、mempool 不再是队列 |

覆盖声明：L5.1→M5.1；L5.2→M5.3；L5.3→M5.4；L5.4→M5.2/M5.5/M5.6；M5.7→L9.9 方法 + 博物馆 CVE-2021-39137（官方 GHSA / postmortem）+ Sepolia 2024-03 Engine API 尺寸（不变量 96）+ 2021-05 状态问题 / gas≠墙钟（不变量 101）+ 2016-11 OOG≠空账户删除已回滚（不变量 103）+ CVE-2025-30147 子群≠在曲线上（不变量 116）+ Avalanche 2025 正确语义≠预编译信任（不变量 119；C-Chain 是 EVM 事故，不是 Snow 抽样）。
