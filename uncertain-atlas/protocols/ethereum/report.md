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

1. 签名（含 nonce、gas、chain id、数据）。钱包 JSON 里的 chainId 不是已经编进签名哈希；旧六字段签不是已经防跨链重放；EIP-155 不是 EIP-1559。精读：[`../../tracks/crypto/worked-example-chainid-vs-signed.md`](../../tracks/crypto/worked-example-chainid-vs-signed.md)（不变量 161）。类型字节不是已经解开内层；旧式列表不是已经是信封；2718 不是 1559。精读：[`../../tracks/implementation/worked-example-typed-vs-legacy.md`](../../tracks/implementation/worked-example-typed-vs-legacy.md)（不变量 167）。列出地址或槽不是已经访问过；列表外不是已经不能碰。精读：[`../../tracks/implementation/worked-example-listed-vs-accessed.md`](../../tracks/implementation/worked-example-listed-vs-accessed.md)（不变量 168）。本笔第一次碰不是已经热；发送者开跑已在集合不是任意地址已经热。精读：[`../../tracks/implementation/worked-example-cold-vs-warm.md`](../../tracks/implementation/worked-example-cold-vs-warm.md)（不变量 169）。出块者地址开跑时已在热集合不是已经访问过；开跑已热不是 169 那几个预填已经覆盖出块者：[`../../tracks/implementation/worked-example-coinbase-vs-prefill.md`](../../tracks/implementation/worked-example-coinbase-vs-prefill.md)（不变量 187）。钱包 typed data 是 EIP-712，**不是**共识投票域；对照 `tracks/crypto/worked-example-tagged-hash.md`。  
2. RPC 广播。  
3. 进若干 mempool；可被替换（同 nonce 更高费）。  
4. 某 proposer 签入执行块；列表可能由外部 builder 写（域外 Builder API：先签盲头再揭示）。见 [`../../tracks/mempool/worked-example-who-orders.md`](../../tracks/mempool/worked-example-who-orders.md)。不是协议内 PBS。  
5. 执行：扣费、跑 EVM、写存储、出收据与日志。失败交易仍可能消耗 gas、推进 nonce（事实：视失败类型）。用户交易跑完之后，载荷里的提款操作才无条件加余额：不是用户交易，没有 gas，不得失败。精读：[`../../tracks/economic/worked-example-withdrawal-vs-tx.md`](../../tracks/economic/worked-example-withdrawal-vs-tx.md)（不变量 154）。  
6. 共识层把该执行结果纳入头。信标链出队不是执行账户已经加钱。  
7. 头可被 fork choice 摆动；justified / finalized 是更强的等级。justified 不是已经不可逆。精读：[`../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)（不变量 127）。执行层刚处理完一块不是已经改规范头；没有 `POS_FORKCHOICE_UPDATED` 不得改 fork choice。精读：[`../../tracks/finality/worked-example-processed-vs-forkchoice.md`](../../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149）。  
8. 钱包若只显示 head，或 RPC 只用 `latest` / `safe`，语义偏乐观。官方没有把 `safe` 写成 justified。

---

## 5. 状态模型

账户：EOA 与合约。nonce、余额、代码、存储。nonce 顶到规范上限不是已经还能加一；客户端已经用窄整数存 nonce 不是共识已经写了这道上限：[`../../tracks/state-models/worked-example-max-nonce-vs-next.md`](../../tracks/state-models/worked-example-max-nonce-vs-next.md)（不变量 175）。initcode 超界不是已经是部署代码超界；按字收跳转分析费不是已经跑完构造：[`../../tracks/implementation/worked-example-initcode-vs-runtime.md`](../../tracks/implementation/worked-example-initcode-vs-runtime.md)（不变量 176）。创建结束返回的运行时代码超界不是已经是 initcode 超界；这次失败是耗尽气不是已经整笔非法；规范 EIP-170 不是不变量 170：[`../../tracks/implementation/worked-example-returned-vs-initcode.md`](../../tracks/implementation/worked-example-returned-vs-initcode.md)（不变量 185）。新创建要存上链的代码以保留首字节开头不是已经是对象格式已经部署；链上已有以该字节开头的代码不是已经被本页改语义：[`../../tracks/implementation/worked-example-reserved-prefix-vs-eof.md`](../../tracks/implementation/worked-example-reserved-prefix-vs-eof.md)（不变量 188）。看见授权名单不是已经委托成功；代码里是委托指示不是已经是目标合约代码；本笔执行失败不是已经撤回写好的委托：[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)（不变量 190）。出块者地址开跑时已在热集合不是已经访问过；开跑已热不是已经付给出块者：[`../../tracks/implementation/worked-example-coinbase-vs-prefill.md`](../../tracks/implementation/worked-example-coinbase-vs-prefill.md)（不变量 187）。带回剩余气的回滚不是已经像非法指令那样把剩余气烧光：[`../../tracks/implementation/worked-example-revert-vs-invalid.md`](../../tracks/implementation/worked-example-revert-vs-invalid.md)（不变量 177）。静态帧不是已经是高级语言的只读函数：[`../../tracks/implementation/worked-example-static-vs-view.md`](../../tracks/implementation/worked-example-static-vs-view.md)（不变量 178）。空不是已经不存在；死不是已经一种对象：[`../../tracks/state-models/worked-example-empty-vs-dead.md`](../../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）。状态在 Merkle-Patricia 树（未来 Verkle 方向是研究/演进，不当成已完成事实）。见 L2.2。

---

## 6. 共识

合并后：Gasper 家族（LMD-GHOST fork choice + Casper FFG 最终性）。  
头、justified、finalized 是三等。升级只发生在 epoch 边界检查点。一张 attestation 同时带头票与 FFG source/target。精读：[`../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md`](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)（不变量 127）。处理完一块不是已经改规范头；事件里的 head 不是已经 finalized。精读：[`../../tracks/finality/worked-example-processed-vs-forkchoice.md`](../../tracks/finality/worked-example-processed-vs-forkchoice.md)（不变量 149）。看见头里的请求承诺不是已经由共识层处理完；请求不是已经有权单独促成动作：[`../../tracks/finality/worked-example-request-vs-action.md`](../../tracks/finality/worked-example-request-vs-action.md)（不变量 192）。看见执行层退出请求不是已经退出；进了本块请求名单不是已经由共识层办完：[`../../tracks/economic/worked-example-el-exit-vs-withdrawal.md`](../../tracks/economic/worked-example-el-exit-vs-withdrawal.md)（不变量 193）。看见执行层存款日志不是已经由共识层办完；看见存款交易不是已经进了本块请求名单：[`../../tracks/economic/worked-example-el-deposit-vs-eth1data.md`](../../tracks/economic/worked-example-el-deposit-vs-eth1data.md)（不变量 194）。看见合并请求不是已经并成一把；抬高有效余额上限不是已经取消最低激活额：[`../../tracks/economic/worked-example-maxeb-vs-minact.md`](../../tracks/economic/worked-example-maxeb-vs-minact.md)（不变量 196）。看见 calldata 地板不是已经改了执行气；数据为主更贵不是已经让普通转账更贵：[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)（不变量 197）。看见 RLP 编码硬帽不是已经改了气限；共识层流言不传不是已经让执行层非法：[`../../tracks/implementation/worked-example-rlp-cap-vs-gas.md`](../../tracks/implementation/worked-example-rlp-cap-vs-gas.md)（不变量 202）。看见单笔气帽不是已经改了块气限；入池拒掉不是已经验过块：[`../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md`](../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md)（不变量 203）。委员会下标被挪出签名不是已经没有委员会；分叉后第一块可以没有证明不是已经没有 LMD 票：[`../../tracks/finality/worked-example-committee-index-vs-signed.md`](../../tracks/finality/worked-example-committee-index-vs-signed.md)（不变量 198）。  
验证者质押、attestation、slashing。可罚关系是 phase0 `is_slashable_attestation_data` 的 **double**（同 target epoch、不同 data）与 **surround**（`attestation_1` 包住 `attestation_2`，顺序不对称），加上同 slot 双头的 proposer slashing；信标状态执行 `slash_validator`，不是 ABCI 应用裁量。精读：[`../../tracks/economic/worked-example-casper-slashing.md`](../../tracks/economic/worked-example-casper-slashing.md)。不抄现行罚金与验证者人数。  
最终性是协议对象，但仍有弱主观性、长程攻击等 PoS 议题。精读：[`../../tracks/finality/worked-example-weak-subjectivity.md`](../../tracks/finality/worked-example-weak-subjectivity.md)（检查点新鲜度；分发节规范未写完）。  
终局推迟不是高度已经停。Inactivity leak 抽不跟多数走的质押，官方写很贵但没有被 slash。两边都 leak 到 finalized 不是协议已经选出唯一链。精读：[`../../tracks/finality/worked-example-inactivity-leak.md`](../../tracks/finality/worked-example-inactivity-leak.md)（不变量 130）。不抄 epoch 个数 / 罚没天数 / 美元。

与 CometBFT 不同：有单独的 fork choice 头，不一定每个 slot 都像 Tendermint 那样「一高度一 commit」。不要混。

---

## 7. 执行

EVM 字节码、gas、退款、预编译。  
确定性要求：禁止用节点本地时间/随机数当共识输入。  
gas 是资源计量，防无限循环变成网络武器。它不是「手续费市场的全部」。  
信标提款是系统操作，不是用户交易，没有 gas：[`../../tracks/economic/worked-example-withdrawal-vs-tx.md`](../../tracks/economic/worked-example-withdrawal-vs-tx.md)（不变量 154）。看见执行层退出请求不是已经退出；进了本块请求名单不是已经由共识层办完：[`../../tracks/economic/worked-example-el-exit-vs-withdrawal.md`](../../tracks/economic/worked-example-el-exit-vs-withdrawal.md)（不变量 193）。看见执行层存款日志不是已经由共识层办完；看见存款交易不是已经进了本块请求名单：[`../../tracks/economic/worked-example-el-deposit-vs-eth1data.md`](../../tracks/economic/worked-example-el-deposit-vs-eth1data.md)（不变量 194）。看见合并请求不是已经并成一把；抬高有效余额上限不是已经取消最低激活额：[`../../tracks/economic/worked-example-maxeb-vs-minact.md`](../../tracks/economic/worked-example-maxeb-vs-minact.md)（不变量 196）。看见 calldata 地板不是已经改了执行气；数据为主更贵不是已经让普通转账更贵：[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)（不变量 197）。看见 BLS12-381 预编译不是已经在验 BLS 签：[`../../tracks/crypto/worked-example-bls-precompile-vs-verify.md`](../../tracks/crypto/worked-example-bls-precompile-vs-verify.md)（不变量 199）。看见 P256 验签预编译不是已经在验 k1；验绿不是已经不可延展：[`../../tracks/crypto/worked-example-p256-vs-k1.md`](../../tracks/crypto/worked-example-p256-vs-k1.md)（不变量 204）。看见 MODEXP 输入长度帽不是已经改了计价公式；超帽不是已经成功返回：[`../../tracks/implementation/worked-example-modexp-bound-vs-price.md`](../../tracks/implementation/worked-example-modexp-bound-vs-price.md)（不变量 206）。看见对等节点宣布历史窗不是已经改了共识历史；线上收据没有布隆不是已经改了共识收据编码：[`../../tracks/network/worked-example-history-window-vs-consensus.md`](../../tracks/network/worked-example-history-window-vs-consensus.md)（不变量 207）。看见数前导零操作码不是已经更便宜的 ZK 证明；动机写了后量子签不是已经有后量子签名：[`../../tracks/implementation/worked-example-clz-vs-zk.md`](../../tracks/implementation/worked-example-clz-vs-zk.md)（不变量 208）。看见只改 blob 参数的专用分叉不是已经改了执行规则，也不是已经是常规抬日程或 PeerDAS：[`../../tracks/light-clients/worked-example-bpo-vs-hardfork.md`](../../tracks/light-clients/worked-example-bpo-vs-hardfork.md)（不变量 209）。看见分叉配置 RPC 对上了不是已经过多客户端同根；看见 current / next / last 不是已经改了共识：[`../../tracks/implementation/worked-example-config-rpc-vs-aligned.md`](../../tracks/implementation/worked-example-config-rpc-vs-aligned.md)（不变量 210）。看见客户端默认气限不是已经是协议帽；看见绑到硬分叉发布不是已经改了共识：[`../../tracks/implementation/worked-example-default-gas-vs-cap.md`](../../tracks/implementation/worked-example-default-gas-vs-cap.md)（不变量 211）。看见块级访问名单不是已经并行跑完；看见强制名单不是已经是 2930：[`../../tracks/implementation/worked-example-block-list-vs-parallel.md`](../../tracks/implementation/worked-example-block-list-vs-parallel.md)（不变量 212）。看见内存拷贝指令不是已经是身份预编译；看见「像用了中间缓冲」不是已经必须真分配：[`../../tracks/implementation/worked-example-mcopy-vs-identity.md`](../../tracks/implementation/worked-example-mcopy-vs-identity.md)（不变量 216）。看见压零指令不是已经是带立即数的压 0；看见没有立即数不是已经改了跳转目的分析：[`../../tracks/implementation/worked-example-push0-vs-push1.md`](../../tracks/implementation/worked-example-push0-vs-push1.md)（不变量 217）。看见基础费指令不是已经改了费用市场；看见能读本块基础费不是已经给了出块者：[`../../tracks/implementation/worked-example-basefee-opcode-vs-market.md`](../../tracks/implementation/worked-example-basefee-opcode-vs-market.md)（不变量 218）。看见 blob 基础费指令不是已经是执行层基础费指令；看见能读本块 blob 基础费不是已经并成一套气：[`../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md`](../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md)（不变量 219）。看见链号指令不是已经是签进哈希的链号：[`../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md`](../../tracks/implementation/worked-example-chainid-opcode-vs-signed.md)（不变量 220）。看见代码哈希指令不是已经看见代码本身：[`../../tracks/implementation/worked-example-extcodehash-vs-copy.md`](../../tracks/implementation/worked-example-extcodehash-vs-copy.md)（不变量 221）。看见盐创建指令不是已经是按发送者加序号占址：[`../../tracks/implementation/worked-example-create2-vs-created.md`](../../tracks/implementation/worked-example-create2-vs-created.md)（不变量 222）。看见退款削减不是已经没有退款：[`../../tracks/implementation/worked-example-refund-vs-gone.md`](../../tracks/implementation/worked-example-refund-vs-gone.md)（不变量 223）。看见弃用警告不是已经改了共识行为：[`../../tracks/implementation/worked-example-deprecate-vs-changed.md`](../../tracks/implementation/worked-example-deprecate-vs-changed.md)（不变量 224）。看见净计量不是已经是瞬时存储：[`../../tracks/implementation/worked-example-net-meter-vs-transient.md`](../../tracks/implementation/worked-example-net-meter-vs-transient.md)（不变量 225）。看见非零 calldata 降价不是已经没有块大小上限：[`../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md`](../../tracks/implementation/worked-example-calldata-cut-vs-unlimited.md)（不变量 226）。看见模幂重计价不是已经是 198 那道复杂度公式，也不是已经加了输入长度帽：[`../../tracks/implementation/worked-example-modexp-price-vs-bound.md`](../../tracks/implementation/worked-example-modexp-price-vs-bound.md)（不变量 227）。执行头里的父信标根不是当前信标头，也不是已经 finalized：[`../../tracks/light-clients/worked-example-parent-root-vs-head.md`](../../tracks/light-clients/worked-example-parent-root-vs-head.md)（不变量 156）。看见状态里的历史执行哈希不是已经是 BLOCKHASH：[`../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md`](../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md)（不变量 195）。合并后旧 `DIFFICULTY` 指令返回上一块 RANDAO mix，不是工作量，也不是应用级无偏随机：[`../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md`](../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)（不变量 157）。看见 RANDAO 种子已经提前知道不是已经锁死下一纪元出块日程：[`../../tracks/consensus/worked-example-lookahead-vs-randao.md`](../../tracks/consensus/worked-example-lookahead-vs-randao.md)（不变量 205）。EIP-1559 基础费是烧掉的网络费，不是已经给了出块者；弹性块大小不是整套费用市场已经齐；烧掉不是 MEV 已经解决：[`../../tracks/mempool/worked-example-basefee-vs-tip.md`](../../tracks/mempool/worked-example-basefee-vs-tip.md)（不变量 158）。出块者开跑已热不是已经付给出块者：[`../../tracks/implementation/worked-example-coinbase-vs-prefill.md`](../../tracks/implementation/worked-example-coinbase-vs-prefill.md)（不变量 187）。瞬时存储行为几乎像 storage，但交易结束丢掉，不是已经进账户，也不是 memory：[`../../tracks/state-models/worked-example-transient-vs-storage.md`](../../tracks/state-models/worked-example-transient-vs-storage.md)（不变量 159）。后来的 `SELFDESTRUCT` 只转走余额，不删账户；只有创建当笔才保留旧拆户：[`../../tracks/state-models/worked-example-selfdestruct-vs-delete.md`](../../tracks/state-models/worked-example-selfdestruct-vs-delete.md)（不变量 160）。发送者已有代码不是已经能当 EOA 发交易；从该地址发出的交易不是已经合法；块里收了它不是块已经合法；RPC 模拟放行不是共识已经放行：[`../../tracks/state-models/worked-example-code-sender-vs-eoa.md`](../../tracks/state-models/worked-example-code-sender-vs-eoa.md)（不变量 162）。看见授权名单不是已经委托成功；委托指示不是已经是目标代码；委托指示不是已经解除 3607：[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)（不变量 190）。initcode 超界不是已经是部署代码超界；创建交易超界不是已经是 CREATE 指令失败；按字收跳转分析费不是已经跑完构造：[`../../tracks/implementation/worked-example-initcode-vs-runtime.md`](../../tracks/implementation/worked-example-initcode-vs-runtime.md)（不变量 176）。带回剩余气的回滚不是已经像非法指令那样把剩余气烧光；创建里回滚不是已经部署：[`../../tracks/implementation/worked-example-revert-vs-invalid.md`](../../tracks/implementation/worked-example-revert-vs-invalid.md)（不变量 177）。静态帧不是已经是高级语言的只读函数；没转账的普通调用不是已经是静态帧：[`../../tracks/implementation/worked-example-static-vs-view.md`](../../tracks/implementation/worked-example-static-vs-view.md)（不变量 178）。空不是已经不存在；碰到（含零值）不是已经付过钱：[`../../tracks/state-models/worked-example-empty-vs-dead.md`](../../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）。看见签过的自愿退出不是已经永远有效；看见域锁在某次分叉不是已经改了执行层：[`../../tracks/consensus/worked-example-exit-domain-vs-fork.md`](../../tracks/consensus/worked-example-exit-domain-vs-fork.md)（不变量 213）。看见加长证明纳入窗不是已经有确认规则；看见能收到下一纪元末不是已经改了 LMD-GHOST：[`../../tracks/finality/worked-example-inclusion-window-vs-confirm.md`](../../tracks/finality/worked-example-inclusion-window-vs-confirm.md)（不变量 214）。看见激活流失帽不是已经改了奖励曲线；看见入口帽不是已经是出口帽：[`../../tracks/economic/worked-example-activation-churn-vs-rewards.md`](../../tracks/economic/worked-example-activation-churn-vs-rewards.md)（不变量 215）。

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
3. MEV / 域外 Builder API 让「交易生命周期」不再是简单队列；签头 ≠ 本地排序。见 [`../../tracks/mempool/worked-example-who-orders.md`](../../tracks/mempool/worked-example-who-orders.md)。烧掉基础费降低与 MEV 相关的风险，不是 MEV 已经解决：[`../../tracks/mempool/worked-example-basefee-vs-tip.md`](../../tracks/mempool/worked-example-basefee-vs-tip.md)（不变量 158）。  
4. 协议极度复杂，升级协调成本高。  
5. 用户层把浏览器当验证。

---

## 14. Trade-off

| 得到 | 换 |
|---|---|
| 通用计算 | 规范与攻击面爆炸、gas 计量、状态增长 |
| 多客户端 | 必须极硬的规范，否则分裂 |
| PoS 最终性 | 弱主观性、质押政治、惩罚误伤 |
| blobs / L2 扩容 | DA 与结算语义更绕。4844 sidecar ≠ PeerDAS 列抽样 ≠ Celestia DAS；服务窗 4096 epoch。见 [`../../tracks/light-clients/worked-example-blob-vs-das.md`](../../tracks/light-clients/worked-example-blob-vs-das.md)。blob gas ≠ 普通执行 gas：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）。看见抬高 blob 目标/上限 ≠ 已经改了两套气 / 已经是 PeerDAS：[`../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md`](../../tracks/light-clients/worked-example-blob-schedule-vs-4844.md)（不变量 200）。看见 blob 底价 ≠ 已经并成一套气 / 已经改了日程：[`../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md`](../../tracks/light-clients/worked-example-blob-reserve-vs-execution.md)（不变量 201） |

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
