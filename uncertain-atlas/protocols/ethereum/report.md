# Ethereum · 19 节档案（第一版）

合并后的执行层 + 共识层。细节以 Yellow Paper / 共识规范 / 客户端为准。本版钉结构，不写生态项目。

---

## 1. 一句话定义

对账户树做确定性 `Apply`（EVM + gas），交易由执行层打包；共识层（PoS）决定 canonical 头与最终性。多个独立客户端必须对同一块算出同一状态根。

---

## 2. 它解决的问题

Bitcoin 脚本不够做通用程序。Ethereum 要把「任意（计量过的）计算」放进复制状态机。  
后来又要解决：PoW 能耗、状态膨胀、单客户端风险、L1 容量。这些是成功之后的新病，不是创世就有的答案。

---

## 3. 架构图

```text
钱包 --tx--> RPC
              ↓
         mempool / 构建者（PBS 后更绕）
              ↓
         执行层：排序、EVM、状态根、收据
              ↓
         共识层：slot、proposer、attestation、fork choice、finality
              ↓
         磁盘：状态树 + 块 + 日志
```

用户仍看见「一条链」。内部已是两套软件。

---

## 4. 一笔交易完整生命周期

1. 签名（含 nonce、gas、chain id、数据）。钱包 typed data 是 EIP-712，**不是**共识投票域；对照 `tracks/crypto/worked-example-tagged-hash.md`。  
2. RPC 广播。  
3. 进若干 mempool；可被替换（同 nonce 更高费）。  
4. 某 proposer 签入执行块；列表可能由外部 builder 写（域外 Builder API：先签盲头再揭示）。见 [`../../tracks/mempool/worked-example-who-orders.md`](../../tracks/mempool/worked-example-who-orders.md)。不是协议内 PBS。  
5. 执行：扣费、跑 EVM、写存储、出收据与日志。失败交易仍可能消耗 gas、推进 nonce（事实：视失败类型）。  
6. 共识层把该执行结果纳入头。  
7. 头可被 fork choice 摆动；justified / finalized 是更强的等级。justified 不是已经不可逆。精读：[`../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)（不变量 127）。  
8. 钱包若只显示 head，或 RPC 只用 `latest` / `safe`，语义偏乐观。官方没有把 `safe` 写成 justified。

---

## 5. 状态模型

账户：EOA 与合约。nonce、余额、代码、存储。状态在 Merkle-Patricia 树（未来 Verkle 方向是研究/演进，不当成已完成事实）。见 L2.2。

---

## 6. 共识

合并后：Gasper 家族（LMD-GHOST fork choice + Casper FFG 最终性）。  
头、justified、finalized 是三等。升级只发生在 epoch 边界检查点。一张 attestation 同时带头票与 FFG source/target。精读：[`../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)（不变量 127）。  
验证者质押、attestation、slashing。可罚关系是 phase0 `is_slashable_attestation_data` 的 **double**（同 target epoch、不同 data）与 **surround**（`attestation_1` 包住 `attestation_2`，顺序不对称），加上同 slot 双头的 proposer slashing；信标状态执行 `slash_validator`，不是 ABCI 应用裁量。精读：[`../../tracks/economic/worked-example-casper-slashing.md`](../../tracks/economic/worked-example-casper-slashing.md)。不抄现行罚金与验证者人数。  
最终性是协议对象，但仍有弱主观性、长程攻击等 PoS 议题。精读：[`../../tracks/finality/worked-example-weak-subjectivity.md`](../../tracks/finality/worked-example-weak-subjectivity.md)（检查点新鲜度；分发节规范未写完）。  
终局推迟不是高度已经停。Inactivity leak 抽不跟多数走的质押，官方写很贵但没有被 slash。两边都 leak 到 finalized 不是协议已经选出唯一链。精读：[`../../tracks/finality/worked-example-inactivity-leak.md`](../../tracks/finality/worked-example-inactivity-leak.md)（不变量 130）。不抄 epoch 个数 / 罚没天数 / 美元。

与 CometBFT 不同：有单独的 fork choice 头，不一定每个 slot 都像 Tendermint 那样「一高度一 commit」。不要混。

---

## 7. 执行

EVM 字节码、gas、退款、预编译。  
确定性要求：禁止用节点本地时间/随机数当共识输入。  
gas 是资源计量，防无限循环变成网络武器。它不是「手续费市场的全部」。

---

## 8. 网络

devp2p / discv5 等。块与 blob（EIP-4844 后）传播是新带宽账。  
审查可发生在构建者/中继，不只在「验证者人数」。

---

## 9. 存储

状态树是主痛。全节点、归档节点成本差一个数量级。  
断电与数据库实现（多数客户端用某种 KV + 恢复）属实现/部署。状态膨胀是协议成功的经济后果。

---

## 10. 密码学

secp256k1 ECDSA、Keccak-256、树哈希；共识层 BLS 聚合投票；blobs 涉及 KZG（EIP-4844）。  
CL 的 `DomainType`（proposer ≠ attester；Altair 另加 `DOMAIN_SYNC_COMMITTEE = 0x07000000`）与 `compute_signing_root` 见 [`../../tracks/consensus/worked-example-vote-signbytes.md`](../../tracks/consensus/worked-example-vote-signbytes.md)；不要和 EIP-712 混名。同步委员会轻客户端验证的是 **512 抽样**，不是 Casper 全集合：[`../../tracks/light-clients/worked-example-sync-committee.md`](../../tracks/light-clients/worked-example-sync-committee.md)。  
用户账户默认仍非后量子。

---

## 11. 安全假设

| 假设 | 失效 |
|---|---|
| 质押诚实与惩罚有效 | 审查、重组、最终性延迟或失效 |
| 各客户端忠实同一规范 | 实现分歧停链或分叉 |
| 椭圆曲线 | 账户可被盗签 |
| 用户不盲信 RPC | 用户被骗 |
| 轻客户端跟同步委员会 | 验证的是 512 抽样的信标头，不是 FFG 全集合，也不是执行层余额 |
| 构建者市场不彻底卡特尔 | 审查与 MEV 抽取 |

---

## 12. 最大结构性优势

**把「规范必须精确到两个实现不能偷偷不一致」做成文化。**  
多客户端 + 可执行规范 + 差分测试，是实现保证的药。EVM 生态是结果，不是本档案要吹的优点。

---

## 13. 最大具体缺陷

1. 状态膨胀与无状态未完成。  
2. 账户热点，默认并行弱。  
3. MEV / 域外 Builder API 让「交易生命周期」不再是简单队列；签头 ≠ 本地排序。见 [`../../tracks/mempool/worked-example-who-orders.md`](../../tracks/mempool/worked-example-who-orders.md)。  
4. 协议极度复杂，升级协调成本高。  
5. 用户层把浏览器当验证。

---

## 14. Trade-off

| 得到 | 换 |
|---|---|
| 通用计算 | 规范与攻击面爆炸、gas 计量、状态增长 |
| 多客户端 | 必须极硬的规范，否则分裂 |
| PoS 最终性 | 弱主观性、质押政治、惩罚误伤 |
| blobs / L2 扩容 | DA 与结算语义更绕。4844 sidecar ≠ PeerDAS 列抽样 ≠ Celestia DAS；服务窗 4096 epoch。见 [`../../tracks/light-clients/worked-example-blob-vs-das.md`](../../tracks/light-clients/worked-example-blob-vs-das.md)。blob gas ≠ 普通执行 gas：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145） |

---

## 15. 历史事故

| 事件 | 层 | 备注 |
|---|---|---|
| CVE-2021-39137 | 实现 | Geth RETURNDATA 别名导致错根、主网少数分叉。见 `tracks/failure-museum/cve-2021-39137.md`；官方 GHSA + geth postmortem |
| Sepolia 2024-03 | 实现+协议+部署 | Engine API 沿用各家 HTTP RPC 尺寸；单笔低于入池上限 ≠ 拼块已被所有客户端接受。见 `tracks/failure-museum/ethereum-2024-03-sepolia-engine-rpc.md` |
| 2021-05 状态问题 | 协议+实现+部署 | 官方威胁披露（非已停机）：块 gas 上限 ≠ 墙钟已有界；状态访问常数 gas ≠ 磁盘已是 O(1)。见 `tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md` |
| 2016-11-24 OOG 空账户 | 实现+协议 | journaling 在 OOG 时没撤回空账户删除，网络分叉。见 `tracks/failure-museum/ethereum-2016-11-oog-empty-account.md` |
| CVE-2025-30147 | 密码+实现 | Besu 子群检查不是点已经在曲线上；原生加速不是两家已经同根。见 `tracks/failure-museum/cve-2025-30147.md` |

其它方向（须回官方 postmortem 再填七问）：共识客户端最终性/头问题、应用层合约与桥。不拿社交媒体列表充数。

---

## 16. 源码入口（预告）

1. 执行层 `ApplyTransaction` / `StateTransition`。  
2. 共识规范里的 fork choice 与 finality 处理。  
3. 状态树更新与根校验。

客户端：geth、nethermind、lighthouse、prysm 等。先读规范再读一家。

---

## 17. 关键函数（逻辑级）

**StateTransition**  
输入：pre-state、tx。输出：post-state、收据或拒绝。  
invariant：gas 计量、nonce、确定性。

**fork choice**  
输入：最新认证与块。输出：head。  
invariant：与最终性规则不矛盾（具体以规范为准）。

---

## 18. 如何测试

可执行规范、多客户端差分、hive 类套件、共识测试向量。  
「不确定」应偷：**同一交易两实现必须同根**，而不是抄 EVM。

---

## 19. 「不确定」适用性

| 档 | 内容 |
|---|---|
| 强烈建议研究 | 多客户端纪律、gas 式计量思想、chain id、状态根 |
| 可以参考 | 执行/共识拆分、收据与日志 |
| 暂时不需要 | EVM 兼容、Solidity 生态、PBS 全套 |
| 不建议采用 | 第一版就当世界计算机；用 TVL 证明协议正确 |
