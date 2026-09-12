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
- [`worked-example-txid-vs-wtxid.md`](worked-example-txid-vs-wtxid.md) — txid ≠ wtxid；改见证 ≠ 已经改交易身份；头上的 txid Merkle ≠ 已经承诺 wtxid（不变量 152）
- [`worked-example-keypath-vs-scriptpath.md`](worked-example-keypath-vs-scriptpath.md) — 钥匙路径 ≠ 已经揭开脚本树；脚本路径 ≠ 已经揭开全部脚本（不变量 153）
- [`worked-example-typed-vs-legacy.md`](worked-example-typed-vs-legacy.md) — 类型字节 ≠ 已经解开内层；旧式列表 ≠ 已经是信封；2718 ≠ 1559 ≠ 155（不变量 167）
- [`worked-example-listed-vs-accessed.md`](worked-example-listed-vs-accessed.md) — 列出地址或槽 ≠ 已经访问过；列表外 ≠ 已经不能碰；2930 ≠ 2718 ≠ 1559（不变量 168）
- [`worked-example-cold-vs-warm.md`](worked-example-cold-vs-warm.md) — 本笔第一次碰 ≠ 已经热；本笔再碰 ≠ 又是冷访问；2929 ≠ 2930 ≠ 墙钟（不变量 169）
- [`worked-example-versionbit-vs-active.md`](worked-example-versionbit-vs-active.md) — 版本位被置上 ≠ 已经锁定；锁定 ≠ 已经激活；9 ≠ 34 ≠ 被部署的那条规则（不变量 171）
- [`worked-example-valid-vs-der.md`](worked-example-valid-vs-der.md) — ECDSA 验得过 ≠ 已经是严格 DER；库收下 ≠ 共识已经接受；66 ≠ 62 ≠ 146 ≠ 34（不变量 172）
- [`worked-example-coinbase-height-vs-header.md`](worked-example-coinbase-height-vs-header.md) — coinbase 第一项写了高度 ≠ 头上已经有高度字段；34 ≠ 9 ≠ 66（不变量 173）
- [`worked-example-address-vs-utxo.md`](worked-example-address-vs-utxo.md) — 看见 Bech32 地址串 ≠ 链上已经有这笔输出；校验过 ≠ 程序已经上链；173 ≠ 350 ≠ 141 ≠ 13（不变量 174）
- [`worked-example-bech32m-vs-bech32.md`](worked-example-bech32m-vs-bech32.md) — 后继校验过了 ≠ 已经是旧校验那套地址；版本与编码必须配对；350 ≠ 173 ≠ 141（不变量 181）
- [`worked-example-xpub-vs-spendable.md`](worked-example-xpub-vs-spendable.md) — 看见扩展公钥 ≠ 已经能花；硬化 ≠ 已经能从公钥推出；32 ≠ 173 ≠ 174 ≠ 350（不变量 182）
- [`worked-example-mnemonic-vs-seed.md`](worked-example-mnemonic-vs-seed.md) — 看见助记词 ≠ 已经是二进制种子；口令不同 ≠ 已经非法；39 ≠ 32 ≠ 173 ≠ 380（不变量 183）
- [`worked-example-initcode-vs-runtime.md`](worked-example-initcode-vs-runtime.md) — initcode 超界 ≠ 已经是部署代码超界；按字分析费 ≠ 已经跑完构造；3860 ≠ 170 ≠ 1014 ≠ 2681（不变量 176）
- [`worked-example-revert-vs-invalid.md`](worked-example-revert-vs-invalid.md) — 带回剩余气的回滚 ≠ 已经烧光剩余气；不够付自己的费 ≠ 已经留下剩余气；140 ≠ 空账户 OOG ≠ 另一条链的 REVERTED（不变量 177）
- [`worked-example-static-vs-view.md`](worked-example-static-vs-view.md) — 静态帧 ≠ 已经是高级语言只读；没转账 ≠ 已经静态；214 ≠ 140（不变量 178）
- [`worked-example-psbt-vs-broadcast.md`](worked-example-psbt-vs-broadcast.md) — 看见部分签名包 ≠ 已经能广播；有几张签 ≠ 已经凑齐；174 ≠ 173 ≠ 125（不变量 179）

平台宽度尺寸检查：[`../failure-museum/cve-2025-46597.md`](../failure-museum/cve-2025-46597.md)（卡住内存池旋钮 ≠ 固定宽度）。  
外层交易上限 ≠ 内层解码已有界：[`../failure-museum/asa-2024-0012.md`](../failure-museum/asa-2024-0012.md)（`max_tx_bytes` 不管 UnpackAny / 内部消息）。  
可选模块 EndBlocker 出错 ≠ 局部失败：[`../failure-museum/isa-2025-002.md`](../failure-museum/isa-2025-002.md)。  
停链交易 ≠ 已停链：[`../failure-museum/x-crisis-no-halt.md`](../failure-museum/x-crisis-no-halt.md)。  
奖励池溢出 ≠ 只是金额：[`../failure-museum/isa-2025-005.md`](../failure-museum/isa-2025-005.md)。  
未初始化被挡账户 ≠ 可归属地址：[`../failure-museum/asa-2024-003.md`](../failure-museum/asa-2024-003.md)。  
Int/Dec ≠ 位宽已齐：[`../failure-museum/asa-2024-010.md`](../failure-museum/asa-2024-010.md)。  
跨链 ack JSON ≠ 已确定：[`../failure-museum/isa-2025-001.md`](../failure-museum/isa-2025-001.md)。  
授权代发 ≠ 内层已认证：[`../failure-museum/elderflower.md`](../failure-museum/elderflower.md)。  
ValidateBasic 读本地钟 ≠ 已确定：[`../failure-museum/jackfruit.md`](../failure-museum/jackfruit.md)。  
「停链」不是一种事故：[`../failure-museum/worked-example-halt-surfaces.md`](../failure-museum/worked-example-halt-surfaces.md)。

课：L1.4 编码、L1.6 随机与确定性、L4.4 ABCI+WAL、L5.3 多客户端同根、L9.3 存储。  
博物馆：BIP 50、CVE-2010-5139、CVE-2018-17144、CVE-2012-2459、CVE-2024-52912、CVE-2024-52913、CVE-2019-25220（含 52916）。屏蔽池可靠性：CVE-2019-7167。  
模式：canonical-encoding、multi-client-determinism。  
反模式：noncanonical-accepted、half-written-state、impl-limit-as-consensus、local-rng-in-apply、authz-sold-as-validated、local-clock-sold-as-validatebasic。
