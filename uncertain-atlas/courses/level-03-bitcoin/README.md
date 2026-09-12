# Level 3 · Bitcoin 作为完整系统

优先级：必学  
先修：L1 + L2.1  
档案：[`../../protocols/bitcoin/report.md`](../../protocols/bitcoin/report.md)

| 课 | 文件 | 覆盖知识树 | 核心问题 |
|---|---|---|---|
| 3.1 | [L03-M01-nakamoto-finality.md](L03-M01-nakamoto-finality.md) | M3.1 | 概率最终为何仍能结算；进了块的 coinbase ≠ 已经能花（不变量 163）；coinbase 高度 ≠ 头上已经有高度字段（不变量 173）；脚本里的 CLTV ≠ 交易 nLockTime 已经把输出锁住（不变量 164）；脚本里的 CSV ≠ 绝对锁 / ≠ 部署名（不变量 165） |
| 3.2 | [L03-M02-fees-and-standardness.md](L03-M02-fees-and-standardness.md) | M3.3 | 费用与标准性不是共识；策略拒绝 ≠ 共识非法（不变量 144）；进了块的手续费 ≠ 矿工已经能花（不变量 163）；选择加入替换信号 ≠ 已经换掉（不变量 166）；跳过库存通告 ≠ 已经拒进池（不变量 245） |
| 3.3 | [L03-M03-conservative-evolution.md](L03-M03-conservative-evolution.md) | M3.4 方向 | 慢升级本身是安全特性；版本位被置上 ≠ 已经锁定；锁定 ≠ 已经激活（不变量 171）；ECDSA 验得过 ≠ 已经是严格 DER（不变量 172） |
| 3.4 | [L03-M04-network-and-eclipse.md](L03-M04-network-and-eclipse.md) | M3.2 | 传播与日蚀；privatebroadcast ≠ IP 已藏；后继地址流言 ≠ 已经连得上（不变量 246）；发了 sendheaders ≠ 已经有块（不变量 247）；按 wtxid 通告 ≠ 已经有交易（不变量 248）；对账素描 ≠ 已经有交易（不变量 249） |
| 3.5 | [L03-M05-full-node-and-spv.md](L03-M05-full-node-and-spv.md) | M3.5 | 全节点 / 剪枝 / SPV；修剪合取 ≠ 修剪非法 |
| 3.6 | [L03-M06-testing-and-culture.md](L03-M06-testing-and-culture.md) | M3.6 / M3.7 方法 | 事故如何回流成规则；迁移失败 ≠ 邻居已安全；看见部分签名包 ≠ 已经能广播（不变量 179）；看见扩展公钥 ≠ 已经能花（不变量 182）；看见助记词 ≠ 已经是二进制种子（不变量 183）；看见私钥或助记词备份 ≠ 已经知道该看哪种输出脚本（不变量 184）；看见后继版本工作包 ≠ 已经是旧版那份固定未签交易（不变量 186）；看见 Miniscript ≠ 已经是链上脚本（不变量 191） |
| 3.7 | [L03-M07-segwit-soft-fork.md](L03-M07-segwit-soft-fork.md) | M3.4 结构 | 见证如何软分叉进旧验证；txid ≠ wtxid（不变量 152）；按 wtxid 通告 ≠ 已经有交易（不变量 248）；钥匙路径 ≠ 揭树（不变量 153）；走脚本路径 ≠ 已经是 tapscript 语义（不变量 189）；看见 Miniscript ≠ 已经是链上脚本（不变量 191）；付给脚本哈希 ≠ 已经揭开赎回脚本（不变量 170）；看见 Bech32 地址串 ≠ 链上已经有这笔输出（不变量 174）；后继校验过了 ≠ 已经是旧校验那套地址（不变量 181） |
| 3.8 | [L03-M08-block-dag.md](L03-M08-block-dag.md) | Kaspa 对照 | 孤块为何出现、DAG 如何仍要全序 |

Tapscript 叶子语义见不变量 189。Miniscript 见不变量 191。钥匙路径 ≠ 揭树见不变量 153。付给脚本哈希 ≠ 已经揭开赎回脚本见不变量 170。2013 分叉七问见博物馆 BIP 50。
