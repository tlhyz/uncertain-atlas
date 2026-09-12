# Level 3 · Bitcoin 作为完整系统

优先级：必学  
先修：L1 + L2.1  
档案：[`../../protocols/bitcoin/report.md`](../../protocols/bitcoin/report.md)

| 课 | 文件 | 覆盖知识树 | 核心问题 |
|---|---|---|---|
| 3.1 | [L03-M01-nakamoto-finality.md](L03-M01-nakamoto-finality.md) | M3.1 | 概率最终为何仍能结算 |
| 3.2 | [L03-M02-fees-and-standardness.md](L03-M02-fees-and-standardness.md) | M3.3 | 费用与标准性不是共识；策略拒绝 ≠ 共识非法（不变量 144） |
| 3.3 | [L03-M03-conservative-evolution.md](L03-M03-conservative-evolution.md) | M3.4 方向 | 慢升级本身是安全特性 |
| 3.4 | [L03-M04-network-and-eclipse.md](L03-M04-network-and-eclipse.md) | M3.2 | 传播与日蚀；privatebroadcast ≠ IP 已藏 |
| 3.5 | [L03-M05-full-node-and-spv.md](L03-M05-full-node-and-spv.md) | M3.5 | 全节点 / 剪枝 / SPV；修剪合取 ≠ 修剪非法 |
| 3.6 | [L03-M06-testing-and-culture.md](L03-M06-testing-and-culture.md) | M3.6 / M3.7 方法 | 事故如何回流成规则；迁移失败 ≠ 邻居已安全 |
| 3.7 | [L03-M07-segwit-soft-fork.md](L03-M07-segwit-soft-fork.md) | M3.4 结构 | 见证如何软分叉进旧验证；txid ≠ wtxid（不变量 152）；钥匙路径 ≠ 揭树（不变量 153） |
| 3.8 | [L03-M08-block-dag.md](L03-M08-block-dag.md) | Kaspa 对照 | 孤块为何出现、DAG 如何仍要全序 |

Tapscript / Miniscript 操作码仍后置。钥匙路径 ≠ 揭树见不变量 153。2013 分叉七问见博物馆 BIP 50。
