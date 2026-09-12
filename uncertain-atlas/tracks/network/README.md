# 横向：点对点网络

课：L9.1、L3.4。  
精读：[`worked-example-eclipse.md`](worked-example-eclipse.md)（六个邻居都是对手）；[`worked-example-adjusted-time.md`](worked-example-adjusted-time.md)（调整钟拒收真块 ≠ 日蚀 / 分区）。  
库存三方向：[`worked-example-inventory-quotas.md`](worked-example-inventory-quotas.md)（入站 INV ≠ 入站 GETDATA ≠ 出站待宣布）。  
最大消息 ≠ 接收分配：[`../failure-museum/cve-2015-3641.md`](../failure-museum/cve-2015-3641.md)。  
地址表递增 ID：[`../failure-museum/cve-2024-52919.md`](../failure-museum/cve-2024-52919.md)（限速 ≠ 宽度）。  
无界封禁表：[`../failure-museum/cve-2020-14198.md`](../failure-museum/cve-2020-14198.md)（自动 ban ≠ 有界）。  
局域网打洞辅助 ≠ P2P：[`../failure-museum/cve-2015-20111.md`](../failure-museum/cve-2015-20111.md)（默认关 UPnP 是结构风险决策）。  
出站代理 ≠ 对等节点：[`../failure-museum/cve-2017-18350.md`](../failure-museum/cve-2017-18350.md)（须先配置；明文网上的任意代理本身就可被截获）。  
宣布新块 ≠ 已收到：[`../failure-museum/cve-2024-52922.md`](../failure-museum/cve-2024-52922.md)。  
拼块 ≠ 共识验块：[`worked-example-compact-block.md`](worked-example-compact-block.md)（52922 / 35202 / 52921）。  
分片外层下标 ≠ 证明下标：[`../failure-museum/asa-2025-002.md`](../failure-museum/asa-2025-002.md)（验根通过不是第 i 片已对齐）。  
结构必须先验再传：[`../failure-museum/asa-2025-003.md`](../failure-museum/asa-2025-003.md)（非法 BitArray 先流言会停网）。  
blocksync 目标必须可归因：[`../failure-museum/asa-2025-001.md`](../failure-museum/asa-2025-001.md)（邻居 latest ≠ 全网尖）。  
握手请求 ≠ 已接受邻居：[`../failure-museum/cve-2020-5303.md`](../failure-museum/cve-2020-5303.md)（入站上限不是握手配额；ID 必须先认领、全路径归还）。  
对等历史窗 ≠ 已改共识：[`worked-example-history-window-vs-consensus.md`](worked-example-history-window-vs-consensus.md)（看见对等节点宣布历史窗不是已经删历史；线上无布隆不是已经改共识收据；7642 ≠ 23 ≠ 25 ≠ 195）。  
忽略版本 ≠ 已经在说新协议：[`worked-example-eip8-vs-already-new.md`](worked-example-eip8-vs-already-new.md)（看见能吞多余字段不是已经谈成新线协议；跟 Homestead 一起上不是已经改共识；仍收旧握手不是已经退役旧格式；8 ≠ 2 ≠ 7642）。
分叉标识 ≠ 已经同一条链：[`worked-example-forkid-vs-same-chain.md`](worked-example-forkid-vs-same-chain.md)（看见分叉标识对上不是已经同一条链；通告了下一分叉不是已经兼容；2124 ≠ 8 ≠ 7642 ≠ 7910）。
签过的节点记录 ≠ 已经最新：[`worked-example-enr-vs-newest.md`](worked-example-enr-vs-newest.md)（看见签过的记录不是已经是最新一份；能多写键不是已经换了身份方案；778 ≠ 2124 ≠ 8 ≠ 7642）。
ping 序号 ≠ 已经有当前记录：[`worked-example-enr-request-vs-have.md`](worked-example-enr-request-vs-have.md)（看见 ping 里的记录序号不是已经有当前记录；能发请求不是已经解析；FindNode 找到人不是已经有记录；868 ≠ 778 ≠ 2124 ≠ 8）。
第 2 版传输 ≠ 已经私人：[`worked-example-v2-transport-vs-private.md`](worked-example-v2-transport-vs-private.md)（看见机会主义未认证加密不是已经私人；伪随机字节流不是已经认不出；仍收下第 1 版不是已经退役旧线；324 ≠ 112 ≠ 8 ≠ 868）。
后继地址 ≠ 已经连得上：[`worked-example-addrv2-vs-reachable.md`](worked-example-addrv2-vs-reachable.md)（看见后继地址流言不是已经连得上；发了 sendaddrv2 不是已经只收后继格式；在传某种网上的地址不是已经连上那种网；155 ≠ 324 ≠ 112 ≠ 868）。
头通告偏好 ≠ 已经有块：[`worked-example-sendheaders-vs-have.md`](worked-example-sendheaders-vs-have.md)（看见发了 sendheaders 不是已经改用头通告；用头通告新尖不是已经有块；重组时先发头不是中间块已经在手里；130 ≠ 36 ≠ 155 ≠ compact）。
按 wtxid 通告 ≠ 已经有交易：[`worked-example-wtxidrelay-vs-have.md`](worked-example-wtxidrelay-vs-have.md)（看见按 wtxid 通告不是已经有那笔交易；发了 wtxidrelay 不是已经改口；仍用旧类型要父交易不是旧库存已经退役；339 ≠ 152 ≠ 130 ≠ 133）。
