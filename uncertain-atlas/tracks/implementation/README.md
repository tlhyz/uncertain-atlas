# 横向：实现保证

协议对，两台诚实机器仍可能算出两个世界。  
目的 A：看见「绿勾」时能指出死的是哪一层。  
目的 B：把确定性写成可测句子，而不是「我们写得很小心」。

精读：

- [`worked-example-encoding.md`](worked-example-encoding.md) — 意思一样、字节不一样
- [`worked-example-crash.md`](worked-example-crash.md) — 写到一半断电
- [`worked-example-assumevalid.md`](worked-example-assumevalid.md) — 跳过签名 ≠ 换共识链；assumevalid ≠ assumeutxo ≠ 旧 checkpoint
- [`worked-example-header-work.md`](worked-example-header-work.md) — 头先够工作量再入库；检查点第三份工作是反垃圾
- [`worked-example-statesync.md`](worked-example-statesync.md) — 应用快照 ≠ 从创世重放；只有轻验 AppHash 可信。亲戚：轻验集合 ≠ 提议者选择，[ASA-2024-009](../failure-museum/asa-2024-009.md)

平台宽度尺寸检查：[`../failure-museum/cve-2025-46597.md`](../failure-museum/cve-2025-46597.md)（卡住内存池旋钮 ≠ 固定宽度）。

课：L1.4 编码、L1.6 随机与确定性、L4.4 ABCI+WAL、L5.3 多客户端同根、L9.3 存储。  
博物馆：BIP 50、CVE-2010-5139、CVE-2018-17144、CVE-2012-2459、CVE-2024-52912、CVE-2024-52913、CVE-2019-25220（含 52916）。屏蔽池可靠性：CVE-2019-7167。  
模式：canonical-encoding、multi-client-determinism。  
反模式：noncanonical-accepted、half-written-state、impl-limit-as-consensus、local-rng-in-apply。
