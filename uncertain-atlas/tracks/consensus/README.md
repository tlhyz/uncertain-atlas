# 专题：共识

分区精读：[`worked-example-partition.md`](worked-example-partition.md)。  
投票被签字节：[`worked-example-vote-signbytes.md`](worked-example-vote-signbytes.md)（Prevote ≠ Precommit；CL `DomainType`）。  
谁写交易顺序：[`../mempool/worked-example-who-orders.md`](../mempool/worked-example-who-orders.md)（Builder API ≠ `process_block`）。  
ABCI 四门：[`worked-example-prepare-process.md`](worked-example-prepare-process.md)（CheckTx ≠ Prepare ≠ Process ≠ Finalize）。  
Vote extension：[`worked-example-vote-extension.md`](worked-example-vote-extension.md)（拒扩展丢票，不改块规则；`s_h` 不读本高度 *e*）。  
集合延迟：[`worked-example-validator-delay.md`](worked-example-validator-delay.md)（H 的 `validator_updates`：H+1 Next、H+2 计票、H+3 last_commit）。  
块时间算法：[`worked-example-pbts.md`](worked-example-pbts.md)（PBTS timely 窗 ≠ BFT Time 中位数 ≠ Bitcoin MTP ≠ 调整钟）。  
Bitcoin MTP 三把尺：[`worked-example-mtp.md`](worked-example-mtp.md)（太早 / BIP113 locktime / 太新窗；太新不是 MTP）。  
本地超时：[`worked-example-timeouts.md`](worked-example-timeouts.md)（`timeout_commit` 是 commit 之后再等，不是最终性、不是锁、不是 PBTS）。  
应用回的等待：[`worked-example-next-block-delay.md`](worked-example-next-block-delay.md)（`next_block_delay` 非确定性；不是槽位，不是所有发布线都有）。  
决策表：[`../../libraries/decision-matrix/consensus.md`](../../libraries/decision-matrix/consensus.md)（不确定列空）。

| 家族 | 最终性 | 分区时 | 领导 | 主要假设 | 档案/课 |
|---|---|---|---|---|---|
| Nakamoto | 概率 | 可两边长 | 矿工竞赛 | 多数算力诚实 | Bitcoin、Zcash、Nervos 变体 |
| CometBFT | 确定 | 倾向停 | 轮值 proposer | <1/3 拜占庭 + 部分同步 | L4 |
| Gasper | 头可摆 + FFG 最终 | 头摆 / 最终延迟 | 质押提议者 | 弱主观性等 | L5.2 |
| Avalanche | 概率固化 | 视参数 | 思想：无传统领袖；产品可有块生产者 | 抽样与参数 | 档案 |
| Algorand | 论文下可快速最终（以规范为准） | 视同步假设 | VRF 抽签出的提议者 | VRF + 权益阈值 | 档案 |
| HotStuff 类 | QC / 线性 view change | 视实现与超时 | 领袖 + QC | <1/3 + 部分同步 | L4.6 |
| 块 DAG | 蓝序/全序变深 | 视图分裂 | 多块并行出 | 仍要全序规则 | L3.8 / Kaspa |
| Nightshade 一条链 | 连续两高度盖上（Nomicon）+ 头上另有 Doomslug 标记 | 缺 chunk 仍「有块」 | 轮值出块者 + chunk 生产者 | <1/3 冲突签 + 分片件够用 | `protocols/near/` |
| 异步执行（Monad 文档） | 先最终**顺序**；状态根延迟 `D` 块才交差 | 文案把序当余额 | 视其 BFT | 执行滞后 + Reserve Balance | 仅过滤器页 |

Avalanche：思想 vs 产品层已有 leader，须分开。  
Algorand 抽签 ≠ Avalanche 抽样。  
Celestia 排序属 CometBFT 家族，最终的是 DA 承诺不是 rollup 余额。  
Polkadot 中继是 BABE + GRANDPA，不要和每高一 commit 混成一张表。

安全 / 活性 / 同步模型见 L0.6。锁见 CometBFT 档案与模式 locking-in-bft。
