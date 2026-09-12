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
