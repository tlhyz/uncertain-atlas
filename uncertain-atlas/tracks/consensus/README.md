# 专题：共识

分区精读：[`worked-example-partition.md`](worked-example-partition.md)。  
投票被签字节：[`worked-example-vote-signbytes.md`](worked-example-vote-signbytes.md)（Prevote ≠ Precommit；CL `DomainType`）。  
谁写交易顺序：[`../mempool/worked-example-who-orders.md`](../mempool/worked-example-who-orders.md)（Builder API ≠ `process_block`）。  
ABCI 四门：[`worked-example-prepare-process.md`](worked-example-prepare-process.md)（CheckTx ≠ Prepare ≠ Process ≠ Finalize）。  
Vote extension：[`worked-example-vote-extension.md`](worked-example-vote-extension.md)（拒扩展丢票，不改块规则；`s_h` 不读本高度 *e*）。扩展快路径不得跳过旧票字段：[ASA-2024-011](../failure-museum/asa-2024-011.md)。治理改启用高度必须先过转移谓词：[ASA-2024-001](../failure-museum/asa-2024-001.md)。提议者注入的扩展不是投票权：[ASA-2024-006](../failure-museum/asa-2024-006.md)。  
集合延迟：[`worked-example-validator-delay.md`](worked-example-validator-delay.md)（H 的 `validator_updates`：H+1 Next、H+2 计票、H+3 last_commit）。  
块时间算法：[`worked-example-pbts.md`](worked-example-pbts.md)（PBTS timely 窗 ≠ BFT Time 中位数 ≠ Bitcoin MTP ≠ 调整钟）。复算中位数 ≠ 故障者不能抬高 Time：[CSA-2026-001](../failure-museum/csa-2026-001.md)。  
Bitcoin MTP 三把尺：[`worked-example-mtp.md`](worked-example-mtp.md)（太早 / BIP113 locktime / 太新窗；太新不是 MTP）。  
本地超时：[`worked-example-timeouts.md`](worked-example-timeouts.md)（`timeout_commit` 是 commit 之后再等，不是最终性、不是锁、不是 PBTS）。默认 MaxBytes 不是第一轮活性 SLA：[ASA-2023-002](../failure-museum/asa-2023-002.md)（`timeout_propose` 必须对照块上限）。+2/3 不是其余槽位已签：[CVE-2020-15091](../failure-museum/cve-2020-15091.md)。  
应用回的等待：[`worked-example-next-block-delay.md`](worked-example-next-block-delay.md)（`next_block_delay` 非确定性；不是槽位，不是所有发布线都有）。  
决策表：[`../../libraries/decision-matrix/consensus.md`](../../libraries/decision-matrix/consensus.md)（不确定列空）。  
Quorum Store 批次传播 ≠ 已经写出 L：[`worked-example-quorum-store-vs-order.md`](worked-example-quorum-store-vs-order.md)（不变量 132）。已认证批次不是已经排序。进了提议块不是已经落盘。  
PoH 槽钟 ≠ 账本票：[`worked-example-poh-vs-tower.md`](worked-example-poh-vs-tower.md)（不变量 133）。`processed` ≠ `confirmed` ≠ `finalized`。超多数票不是已经 root。

| 家族 | 最终性 | 分区时 | 领导 | 主要假设 | 档案/课 |
|---|---|---|---|---|---|
| Nakamoto | 概率 | 可两边长 | 矿工竞赛 | 多数算力诚实 | Bitcoin、Zcash、Nervos 变体 |
| CometBFT | 确定 | 倾向停 | 轮值 proposer | <1/3 拜占庭 + 部分同步 | L4 |
| Gasper | 头可摆 + FFG 最终 | 头摆 / 最终延迟 | 质押提议者 | 弱主观性等 | L5.2 |
| Avalanche | 概率固化（样本置信，不是 QC） | 视参数；Preference ≠ LastAccepted | 思想：无传统领袖；产品另有 Snowman++ 出块窗 | 抽样与参数；α ≠ 全集证书 | 档案 + 精读 |
| Algorand | 抽签后还要 soft vote / certify | 视同步假设；超时可进 recovery | VRF 抽签出的提议者 | VRF + online stake；理想条件页 | 档案 + 精读 |
| HotStuff 类 | QC / 线性 view change | 视实现与超时 | 领袖 + QC | <1/3 + 部分同步 | L4.6 |
| 块 DAG | 蓝序/全序变深 | 视图分裂 | 多块并行出 | 仍要全序规则 | L3.8 / Kaspa |
| Nightshade 一条链 | 连续两高度盖上（Nomicon）+ 头上另有 Doomslug 标记 | 缺 chunk 仍「有块」 | 轮值出块者 + chunk 生产者 | <1/3 冲突签 + 分片件够用 | 档案 + 精读 |
| 异步执行（Monad 文档） | 先最终**顺序**；状态根延迟 `D` 块才交差 | 文案把序当余额 | 视其 BFT | 执行滞后 + Reserve Balance | 过滤器 + 精读 |

Avalanche：思想 vs 产品层已有 leader，须分开。抽样 α 多数 ≠ 全集 +2/3 证书；连续 β ≠ 可转发 QC；出块窗 ≠ 已经决定：[`worked-example-snow-sample-vs-qc.md`](worked-example-snow-sample-vs-qc.md)（不变量 131）。  
Algorand 抽签 ≠ Avalanche 抽样。VRF 抽中 ≠ 已经认证；soft vote ≠ 已经 certify：[`worked-example-vrf-sortition-vs-certified.md`](worked-example-vrf-sortition-vs-certified.md)（不变量 134）。  
NEAR 头上两枚最终哈希不是一套装置。Doomslug / `near-final` ≠ Nomicon BFT 谓词 / `final`：[`../finality/worked-example-doomslug-vs-bft.md`](../finality/worked-example-doomslug-vs-bft.md)（不变量 135）。  
官方顺序已定 ≠ 本块状态根已经交差：[`worked-example-order-vs-state.md`](worked-example-order-vs-state.md)（不变量 136）。投票时可以还没执行。投机 `eth_call` 不是协议最终。  
Celestia 排序属 CometBFT 家族，最终的是 DA 承诺不是 rollup 余额。  
Polkadot 中继是 BABE + GRANDPA，不要和每高一 commit 混成一张表。出块 ≠ 最终：[`worked-example-babe-vs-grandpa.md`](worked-example-babe-vs-grandpa.md)（不变量 126）。NPoS 当选 ≠ 共识已经按质押加权：[`worked-example-npos-equal-weight.md`](worked-example-npos-equal-weight.md)（不变量 129）。

安全 / 活性 / 同步模型见 L0.6。锁见 CometBFT 档案与模式 locking-in-bft。
