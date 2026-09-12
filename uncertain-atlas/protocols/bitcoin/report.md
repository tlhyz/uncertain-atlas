# Bitcoin · 19 节档案（第一版）

资料优先级提醒：白皮书、BIPs、Bitcoin Core、CVE/postmortem 高于任何交易所博客。  
未核对到当前文件名的源码路径标「预告，Level 3 深挖时对照仓库」。

---

## 1. 一句话定义

用 **UTXO 状态** 和 **PoW 最重链规则**，让不认识的节点对「哪些输出已花」达成可独立复验的历史。最终性是概率的，不是委员会 commit。

禁止的句子：「数字黄金」「最快最安全」。

---

## 2. 它解决的问题

上一代电子现金的病：必须有柜员防双花，柜员可以审查、停机、造币。

Bitcoin 的问题陈述（事实，白皮书 2008）：点对点电子现金，用时间戳服务器 + 工作量证明，不靠单一柜员决定花费顺序。

它故意不解决：通用合约平台、秒级确定最终性、隐私默认、低能耗。

---

## 3. 架构图

```text
钱包  →  P2P 广播
           ↓
        mempool（各节点本地策略）
           ↓
        矿工组装候选块 + PoW
           ↓
        块在 P2P 传播（可 compact block）
           ↓
        全节点：验头、验 Merkle、验脚本、更新 UTXO
           ↓
        最重链选择  →  概率最终
           ↓
        磁盘：区块文件 + UTXO 集（chainstate）
```

没有独立的「共识客户端 / 执行客户端」拆分。一台 Bitcoin Core 默认全做。

---

## 4. 一笔交易完整生命周期

1. 钱包选币（哪些 UTXO）、构造输出（收款+找零）、算费、签名。看见部分签名包不是已经是网上能广播的完整交易；里面有几张签不是这一输入已经凑齐：[`../../tracks/implementation/worked-example-psbt-vs-broadcast.md`](../../tracks/implementation/worked-example-psbt-vs-broadcast.md)（不变量 179）。看见扩展公钥不是已经能花；能推子钥不是已经是地址：[`../../tracks/implementation/worked-example-xpub-vs-spendable.md`](../../tracks/implementation/worked-example-xpub-vs-spendable.md)（不变量 182）。看见助记词不是已经是二进制种子；用户自造句子不是已经是本页那种助记词：[`../../tracks/implementation/worked-example-mnemonic-vs-seed.md`](../../tracks/implementation/worked-example-mnemonic-vs-seed.md)（不变量 183）。看见私钥或助记词备份不是已经知道该看哪种输出脚本；看见描述符不是已经是地址：[`../../tracks/implementation/worked-example-descriptor-vs-keys.md`](../../tracks/implementation/worked-example-descriptor-vs-keys.md)（不变量 184）。  
2. 广播到若干对等节点。  
3. 节点按本地策略决定是否进 mempool（脚本、费、标准性）。标准性 ≠ 共识合法性。策略不作用于块内交易：[`../../tracks/mempool/worked-example-policy-vs-consensus.md`](../../tracks/mempool/worked-example-policy-vs-consensus.md)（不变量 144）。选择加入替换信号不是已经换掉；nSequence 示意不是已经是相对锁；钱包看见未确认不是已经当付款：[`../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md`](../../tracks/mempool/worked-example-rbf-signal-vs-replaced.md)（不变量 166）。  
4. 矿工从 mempool 选交易，算 Merkle 根，找 nonce 使头哈希低于目标。头上的 Merkle 用各笔 txid；新规则另要 coinbase 承诺 wtxid 根：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152）。  
5. 新块传播。节点验证：PoW、时间戳窗口、交易列表、脚本、无双花。旧节点看见 txid 不是已经验过见证。  
6. `ConnectBlock`：花输入、造输出，写 UTXO。coinbase 输出进了 UTXO 集，仍不能马上当输入：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)（不变量 163）。coinbase 第一项写了高度不是头上已经有高度字段：[`../../tracks/implementation/worked-example-coinbase-height-vs-header.md`](../../tracks/implementation/worked-example-coinbase-height-vs-header.md)（不变量 173）。  
7. 若随后出现更重的链，可能 disconnect 再 connect（reorg）。  
8. 收款方若只看 1 个确认，仍可能被重组；交易所常用更多确认，这是经济习惯，不是协议 commit。普通确认深度也不是 coinbase 成熟窗。

---

## 5. 状态模型

UTXO 集。见课程 L2.1。

脚本给出花费条件。P2PKH / P2WPKH / P2TR 是包装，不是另一种状态模型。看见 Bech32 地址串不是链上已经有这笔输出；校验过不是见证程序已经在链上：[`../../tracks/implementation/worked-example-address-vs-utxo.md`](../../tracks/implementation/worked-example-address-vs-utxo.md)（不变量 174）。后继校验过了不是已经是旧校验那套地址；更高版本过了旧校验不是已经合法：[`../../tracks/implementation/worked-example-bech32m-vs-bech32.md`](../../tracks/implementation/worked-example-bech32m-vs-bech32.md)（不变量 181）。脚本里的 CLTV 不是交易 nLockTime 已经把输出锁住：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。脚本里的 CSV 不是绝对锁，也不是「CSV 部署」四个字：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。付给脚本哈希不是已经揭开赎回脚本；旧节点 HASH160 EQUAL 通过不是新节点已经再跑赎回：[`../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md`](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)（不变量 170）。

---

## 6. 共识

**Nakamoto / 最重链（事实）：** 在有效链里选累计工作最多的。常见口语「最长链」在难度调整后不精确。

**PoW：** 找头哈希满足难度。假设：多数算力不合作改历史。

**最终性：** 概率。确认数越多，改写期望成本越高，不是「第 N 块后数学禁止」。

**分叉：** 同一高度两个合法块常见于传播延迟。短分叉靠后续工作消解。

没有 Tendermint 式的锁和 +2/3 commit。

**块时间（必须拆开）：** 头不能 `<=` 父块 `GetMedianTimePast`（`time-too-old`）。CSV 软分叉部署之后交易 locktime 也看父 MTP，不看本块 `nTime`（BIP 113）。这里的「CSV」是部署名，不是 CHECKSEQUENCEVERIFY 操作码：[`../../tracks/state-models/worked-example-csv-vs-cltv.md`](../../tracks/state-models/worked-example-csv-vs-cltv.md)（不变量 165）。太新看本节点钟 + 命名宽限（`time-too-new`），不是 MTP。三把尺见 [`../../tracks/consensus/worked-example-mtp.md`](../../tracks/consensus/worked-example-mtp.md)。不要和 PBTS / BFT Time 糊。脚本里的 CLTV 比的是花费交易的 nLockTime，不是墙上现在，也不是 MTP 已经把输出锁住：[`../../tracks/state-models/worked-example-cltv-vs-nlocktime.md`](../../tracks/state-models/worked-example-cltv-vs-nlocktime.md)（不变量 164）。

---

## 7. 执行

不是虚拟机里的 gas 循环。执行 = 脚本解释 + UTXO 规则。

脚本故意非图灵完备（无一般循环），降低「无限跑」的共识风险。Taproot / Tapscript 增加了表达，仍不是 EVM。钥匙路径不是已经揭开有没有脚本树：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153）。

失败的脚本使该交易无效，不能进合法块（共识）。mempool 还会用更严的 standardness 拒绝「共识合法但不受欢迎」的交易。

---

## 8. 网络

无许可 P2P。地址管理、偷听、compact block（BIP152）减传播带宽。最大序列化消息长度 ≠ 读完载荷前的接收分配上限（CVE-2015-3641）。地址表递增 ID 限速 ≠ 宽度已够（CVE-2024-52919）。自动封禁表无界 + GETADDR 二次扫描（CVE-2020-14198）。UPnP 默认关是结构风险决策（CVE-2015-20111 / CVE-2024-52917）。出站 SOCKS 代理不是 P2P 对等节点（CVE-2017-18350；须先配置；明文网上的任意代理本身就可被截获）。付款 URI 远程取单不是共识验证（CVE-2024-52918；修法是删 BIP70）。

攻击面：eclipse（围住一个节点只给他看假图）、延迟块、向轻节点撒谎。

**事实：** 很多性能瓶颈在传播与验证，不在「脚本算得慢」。  
Sybil：身份便宜，抗 Sybil 主要靠算力成本，不是 KYC。

---

## 9. 存储

区块原始数据可剪枝（pruning）但仍要能从创世验证到尖。加速同步是**实现开关**：assumevalid 跳祖先脚本且不强迫链；assumeutxo 先装 UTXO 快照、背景再验。不是弱主观周期，也不是旧 checkpoint。见 [`../../tracks/implementation/worked-example-assumevalid.md`](../../tracks/implementation/worked-example-assumevalid.md)。

UTXO 集在 chainstate。断电必须不出现「半个块」：Bitcoin Core 用库的原子与 flush 策略。具体崩溃语义属部署/实现，Level 9 再对照源码与测试。

归档节点留全历史。剪枝节点不能给别人完整旧块。

---

## 10. 密码学 primitive

| 零件 | 用途 |
|---|---|
| SHA-256 / HASH256 | 块头、txid、Merkle。txid ≠ wtxid：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152） |
| RIPEMD-160 | 地址派生（P2PKH 等） |
| ECDSA secp256k1 | 旧式花费。数学验过不是已经是严格 DER：[`../../tracks/implementation/worked-example-valid-vs-der.md`](../../tracks/implementation/worked-example-valid-vs-der.md)（不变量 172） |
| Schnorr (BIP-340) | Taproot。tagged hash 公式见 `tracks/crypto/worked-example-tagged-hash.md`；标签不是 FIPS `ctx`。钥匙路径 ≠ 揭树：[`../../tracks/implementation/worked-example-keypath-vs-scriptpath.md`](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)（不变量 153） |
| Merkle 树 | 交易承诺、SPV |

没有 BLS，没有默认 zk。

---

## 11. 安全假设

| 假设失效 | 一起失效的保证 |
|---|---|
| 多数算力不诚实 | 重组、审查、双花未确认甚至浅确认 |
| SHA-256 抗碰撞/PoW 预图像被实质打破 | 造假块、改历史成本模型崩 |
| 椭圆曲线签名被破（含量子） | 未花费输出可被盗签 |
| 用户把 RPC/浏览器当验证 | 用户层被骗，协议层可仍健康 |
| 全节点极度稀少 | 验证文化变弱，实现/部署层变脆 |

弱主观性对 Bitcoin 不如长程 PoS 那么中心。创世与旧 checkpoint / 发行默认 assumevalid 仍是社会或实现对象，不要和 Ethereum WS 糊成一句。

---

## 12. 最大结构性优势

**可独立复验的小规则集 + 慢变更。**  
任何人可跑全节点重放。协议进化偏软分叉、偏兼容旧验证者。这与「十年还在」强相关。版本位被置上不是已经锁定；锁定不是已经激活：[`../../tracks/implementation/worked-example-versionbit-vs-active.md`](../../tracks/implementation/worked-example-versionbit-vs-active.md)（不变量 171）。

这是结构，不是市值。

---

## 13. 最大具体缺陷（对结算工程师）

1. 概率最终：深确认之前，商家必须自己承担重组风险。  
2. 吞吐与延迟受块间隔、块权重、传播约束。不是实现没写好那么简单。  
3. 脚本表达力有限；复杂应用外溢到二层。  
4. 隐私弱（链上图谱）。  
5. 挖矿与池导致权力实际集中——经济层，不是白皮书假设自动成立。

---

## 14. Trade-off

| 得到 | 用什么换 |
|---|---|
| 无许可出块、分区时仍能各自长链 | 重组、耗能或等价算力成本、概率最终 |
| 全节点可复验 | 家庭节点要跟带宽与 UTXO 增长 |
| 保守升级 | 新功能极慢 |
| 简单执行 | 不是通用世界计算机 |

---

## 15. 历史事故（抽样，须回原始出处）

| 事件 | 层 | 备注 |
|---|---|---|
| CVE-2018-17144 | 实现 | 重复输入可通胀。见 `tracks/failure-museum/cve-2018-17144.md`；五层对照 `tracks/failure-museum/worked-example-five-layers.md` |
| CVE-2010-5139 | 实现 | 输出求和溢出。见 `tracks/failure-museum/cve-2010-5139.md` |
| CVE-2012-2459 | 协议+实现 | Merkle 奇数复制 ⇒ 同根不同列表。见 `tracks/failure-museum/cve-2012-2459.md` |
| 2013 分叉 | 实现+部署 | BIP 50（BDB 锁上限）。见 `tracks/failure-museum/bip-0050-2013-fork.md` |
| transaction malleability | 协议/实现 | 促使 SegWit；结构课 L3.7。txid ≠ wtxid，不是已经修完所有身份：[`../../tracks/implementation/worked-example-txid-vs-wtxid.md`](../../tracks/implementation/worked-example-txid-vs-wtxid.md)（不变量 152） |
| CVE-2024-52912 | 实现+部署 | 调整钟绕过上限，拒收规范新块。见 `tracks/failure-museum/cve-2024-52912.md` |
| CVE-2024-52913 | 实现+网络 | 有界索取表让节点看不见未确认交易。见 `tracks/failure-museum/cve-2024-52913.md` |
| CVE-2019-25220 | 实现+部署 | 低难度头填爆内存索引；0.14 后检查点几乎只剩反垃圾。见 `tracks/failure-museum/cve-2019-25220.md`。不抄攻击成本 BTC |
| CVE-2024-52914 | 实现 | 孤儿解析二次扫描可卡住数小时。见 `tracks/failure-museum/cve-2024-52914.md` |
| CVE-2015-3641 | 实现+网络 | 最大序列化长度被当成接收分配上限。见 `tracks/failure-museum/cve-2015-3641.md` |
| CVE-2024-52919 | 实现+网络 | 地址表递增 ID 回绕；v22 限速 ≠ v29 改宽度。见 `tracks/failure-museum/cve-2024-52919.md` |
| CVE-2020-14198 | 实现+网络 | 无界封禁表 + GETADDR 二次扫描。见 `tracks/failure-museum/cve-2020-14198.md` |
| CVE-2025-46597 | 实现 | 32-bit 写盘前尺寸检查溢出；卡住 `-maxmempool` ≠ 固定宽度。见 `tracks/failure-museum/cve-2025-46597.md` |
| CVE-2015-20111 | 实现+部署 | UPnP 局域网打洞辅助；0.11.1 默认关以防库洞变结构风险。亲戚 CVE-2024-52917。见 `tracks/failure-museum/cve-2015-20111.md` |
| CVE-2017-18350 | 实现+部署 | 出站 SOCKS 代理不是 P2P 对等节点；须先配置才脆弱。见 `tracks/failure-museum/cve-2017-18350.md` |
| CVE-2024-52918 | 实现+部署 | 支付 URI 远程取单不是共识验证；修法是删 BIP70。见 `tracks/failure-museum/cve-2024-52918.md` |
| 2026-06 privatebroadcast | 实现+部署+网络 | 开关 ≠ IP 已经不暴露；v2 失败后的 v1 重连 ≠ 仍走代理。见 `tracks/failure-museum/bitcoin-2026-06-privatebroadcast-v1-retry.md` |
| 2026-01 wallet migration | 实现+部署 | 迁移失败 ≠ 目录里其它钱包已经安全；现有用户不受影响 ≠ 迁移路径已经安全。见 `tracks/failure-museum/bitcoin-2026-01-wallet-migration-delete.md` |

七问只写有 CVE / 官方披露 / BIP 原文的条目。禁止用传闻填充。

---

## 16. 源码入口（预告，对照当前 Bitcoin Core 树）

建议阅读顺序（名称以上游为准，深挖时打开仓库核对）：

1. **区块连接 / UTXO 更新** — `ConnectBlock` 所在的 validation 路径。为什么：这是 `Apply`。  
2. **最重链选择** — 链状态/工作量比较。为什么：这是 fork choice。  
3. **脚本解释** — interpreter / Taproot 验证。为什么：这是授权。

不要从 `main.cpp` 观光式从头读到尾。

---

## 17. 关键函数（逻辑级）

**`ConnectBlock`（逻辑名）**  
输入：候选块 + 当前 UTXO 视图。  
逻辑：检查头与交易、花输入、造输出、脚本。  
输出：新 UTXO 视图或拒绝。  
invariant：不引入重复花费；coinbase 成熟规则（进了块 ≠ 已经能花：[`../../tracks/economic/worked-example-coinbase-vs-mature.md`](../../tracks/economic/worked-example-coinbase-vs-mature.md)，不变量 163）；供给规则。

**`CheckTxInputs` / 脚本 VerifyScript（逻辑名）**  
输入：交易、被花的输出。  
输出：接受或拒绝。  
invariant：解锁满足锁定；金额守恒（含费）。

**fork choice（逻辑名）**  
输入：已验证的候选尖。  
输出：当前 tip。  
invariant：只在有效链上比工作量。

具体函数名以源码为准。

---

## 18. 如何测试核心协议

Bitcoin Core 传统：大量 functional / unit；fuzz（script、P2P、地址）；有时对比不同实现。

**事实：** fuzz 和保守变更，是其工程哲学的一部分，不是「测试绿了所以永远安全」。CVE-2018-17144 说明实现测试曾漏过通胀不变量。

「不确定」应偷的测试思想：供给/双花这类 invariant 必须有直接断言，不能只靠「常见交易能过」。

---

## 19. 「不确定」适用性

| 档 | 内容 | 理由 |
|---|---|---|
| 强烈建议研究 | 规则少、全节点复验、慢升级、双花/供给 invariant 测试、编码越来越严 | 结算链的寿命来自可验证与克制 |
| 可以参考 | UTXO、mempool 与共识分层（standardness）、compact block、SPV 的假设边界 | 要连假设一起抄 |
| 暂时不需要 | PoW 挖矿市场、地址类型全家桶 | 不服务后量子结算第一问 |
| 不建议采用 | 把概率最终当「已结算」文案；自创哈希；用市值证明协议正确 | 违反五层保证 |

**建议：** 偷哲学，不要偷「我们也要十分钟一块 + 能量竞赛」当默认。
