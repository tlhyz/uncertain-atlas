# Level 9 · 横向系统与失败方法

优先级：重要；9.1–9.3、9.7、9.9 必学  
先修：L3 + L4 + L5。L6–L8 可并行补。

| 课 | 文件 | 覆盖 | 核心问题 |
|---|---|---|---|
| 9.1 | [L09-M01-p2p.md](L09-M01-p2p.md) | M9.1 | 瓶颈常在网上；后继地址流言 ≠ 已经连得上（不变量 246）；发了 sendheaders ≠ 已经有块（不变量 247）；按 wtxid 通告 ≠ 已经有交易（不变量 248）；对账素描 ≠ 已经有交易（不变量 249）；有限服务位 ≠ 已经能服任意旧块（不变量 250）；带见证的线上序列化 ≠ 已经有见证（不变量 251） |
| 9.2 | [L09-M02-mempool.md](L09-M02-mempool.md) | M9.2 | 未确认池是谁的队列；跳过库存通告 ≠ 已经拒进池（不变量 245）；对账素描 ≠ 已经有交易（不变量 249） |
| 9.3 | [L09-M03-storage.md](L09-M03-storage.md) | M9.3 | 写到一半断电；有限服务位 ≠ 已经能服任意旧块（不变量 250） |
| 9.4 | [L09-M04-upgrades.md](L09-M04-upgrades.md) | M9.4 | 谁能改图纸 |
| 9.5 | [L09-M05-economic-security.md](L09-M05-economic-security.md) | M9.5 | 经济 ≠ 密码学 |
| 9.6 | [L09-M06-light-clients.md](L09-M06-light-clients.md) | M9.6 | 四种「轻」的假设；Mina SNARKed ≠ staged |
| 9.7 | [L09-M07-protocol-testing.md](L09-M07-protocol-testing.md) | M9.7 | 绿条守哪一层 |
| 9.8 | [L09-M08-formal-methods.md](L09-M08-formal-methods.md) | M9.8 | 模型不是主网 |
| 9.9 | [L09-M09-failure-museum-method.md](L09-M09-failure-museum-method.md) | M9.9 | 七问怎么写 |
