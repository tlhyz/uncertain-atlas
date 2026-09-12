# Level 8 · 隐私与简洁证明

优先级：进阶  
先修：L1，L2.1，L7.2  
档案：[`../../protocols/zcash/`](../../protocols/zcash/README.md)、[`../../protocols/monero/`](../../protocols/monero/README.md)、[`../../protocols/mina/`](../../protocols/mina/README.md)

毕业：能说明屏蔽池里链知道什么/不知道什么，以及为何仍能防双花；能把环世界和电路世界分开；能把「小证明」和「数据还在」分开。

| 课 | 文件 | 核心问题 |
|---|---|---|
| 8.1 | [L08-M01-what-the-chain-knows.md](L08-M01-what-the-chain-knows.md) | 链上到底看见哪些字段 |
| 8.2 | [L08-M02-ring-vs-zk.md](L08-M02-ring-vs-zk.md) | 环混淆和电路证明差在哪 |
| 8.3 | [L08-M03-succinct-history.md](L08-M03-succinct-history.md) | 小证明如何谈论整条历史 |
| 8.4 | [L08-M04-circuit-as-machine.md](L08-M04-circuit-as-machine.md) | 电路/证人/可靠性（多项式后置） |

覆盖声明：L8.1→M8.1（博物馆 CVE-2019-7167：验证明 ≠ 供给；Solana 2025-05：验绿 ≠ Fiat-Shamir 已绑完；ZIP 257：电路实现 ≠ 已写明的陈述；ZIP 256：跟踪复位 ≠ 闸门 / 归一化 ≠ 编码 / 体拒绝 ≠ 头已绑 / 身份 rk ≠ 已能吃 / 无效 ephemeralKey ≠ 已允许 / coinbase 正余额 ≠ 能重启）；L8.2→M8.2（博物馆 Monero 2025-08：加载 ≠ 出站 TXID 不泄漏）；L8.3→M8.3（小证明 ≠ 数据还在）；L8.4→M8.4 架构层。
