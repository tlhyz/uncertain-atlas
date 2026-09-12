# L5.1 任意程序仍须是确定性状态机

优先级：必学  
先修：L2.2，L0.2

---

## A. 先修知识

账户：余额、nonce、代码、存储。  
发送者已有代码不是已经能当 EOA 发。RPC 绿不是共识已经放行。精读：[`../../tracks/state-models/worked-example-code-sender-vs-eoa.md`](../../tracks/state-models/worked-example-code-sender-vs-eoa.md)（不变量 162）。看见授权名单不是已经委托成功。代码里是委托指示不是已经是目标合约代码。委托指示不是已经解除 3607。本笔执行失败不是已经撤回写好的委托。精读：[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)（不变量 190）。看见状态里的历史执行哈希不是已经是 BLOCKHASH。系统写入父哈希不是已经填满窗口。合约能查更长窗口不是已经改了操作码语义。精读：[`../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md`](../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md)（不变量 195）。看见 calldata 地板不是已经改了执行气。数据为主更贵不是已经让普通转账更贵。预留了地板气限不是已经烧到地板。精读：[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)（不变量 197）。看见 RLP 编码硬帽不是已经改了气限。共识层流言不传不是已经让执行层非法。给信标块留边不是已经并成一份编码。精读：[`../../tracks/implementation/worked-example-rlp-cap-vs-gas.md`](../../tracks/implementation/worked-example-rlp-cap-vs-gas.md)（不变量 202）。看见单笔气帽不是已经改了块气限。入池拒掉不是已经验过块。块里有一笔超帽不是已经只是策略拒绝。精读：[`../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md`](../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md)（不变量 203）。看见 BLS12-381 预编译不是已经在验 BLS 签。加法不查子群不是已经和 MSM/配对同一套谓词。精读：[`../../tracks/crypto/worked-example-bls-precompile-vs-verify.md`](../../tracks/crypto/worked-example-bls-precompile-vs-verify.md)（不变量 199）。看见 P256 验签预编译不是已经在验 k1。验绿不是已经不可延展。空输出不是已经烧光剩余气。精读：[`../../tracks/crypto/worked-example-p256-vs-k1.md`](../../tracks/crypto/worked-example-p256-vs-k1.md)（不变量 204）。看见 MODEXP 输入长度帽不是已经改了计价公式。超帽不是已经成功返回。精读：[`../../tracks/implementation/worked-example-modexp-bound-vs-price.md`](../../tracks/implementation/worked-example-modexp-bound-vs-price.md)（不变量 206）。看见数前导零操作码不是已经更便宜的 ZK 证明；动机写了后量子签不是已经有后量子签名。精读：[`../../tracks/implementation/worked-example-clz-vs-zk.md`](../../tracks/implementation/worked-example-clz-vs-zk.md)（不变量 208）。看见客户端默认气限不是已经是协议帽；看见绑到硬分叉发布不是已经改了共识；看见默认配置齐了不是已经是单笔气帽。精读：[`../../tracks/implementation/worked-example-default-gas-vs-cap.md`](../../tracks/implementation/worked-example-default-gas-vs-cap.md)（不变量 211）。看见块级访问名单不是已经并行跑完；看见强制名单不是已经是 2930；看见事后状态差不是已经不跑交易。精读：[`../../tracks/implementation/worked-example-block-list-vs-parallel.md`](../../tracks/implementation/worked-example-block-list-vs-parallel.md)（不变量 212）。看见内存拷贝指令不是已经是身份预编译；看见「像用了中间缓冲」不是已经必须真分配一块缓冲；看见能重叠拷不是已经是 calldata / 返回数据拷。精读：[`../../tracks/implementation/worked-example-mcopy-vs-identity.md`](../../tracks/implementation/worked-example-mcopy-vs-identity.md)（不变量 216）。看见压零指令不是已经是带立即数的压 0；看见没有立即数不是已经改了跳转目的分析；看见已经部署碰巧用了这个字节不是行为已经不变。精读：[`../../tracks/implementation/worked-example-push0-vs-push1.md`](../../tracks/implementation/worked-example-push0-vs-push1.md)（不变量 217）。看见基础费指令不是已经改了费用市场；看见能读本块基础费不是已经给了出块者；看见跑 EVM 前就已经有这个数不是已经改了头怎么算。精读：[`../../tracks/implementation/worked-example-basefee-opcode-vs-market.md`](../../tracks/implementation/worked-example-basefee-opcode-vs-market.md)（不变量 218）。看见 blob 基础费指令不是已经是执行层基础费指令；看见能读本块 blob 基础费不是已经并成一套气；看见跑 EVM 前就已经有这个数不是已经改了 4844 日程。精读：[`../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md`](../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md)（不变量 219）。nonce 顶到规范上限不是已经还能加一。CREATE / CREATE2 碰到上限不是已经创建。精读：[`../../tracks/state-models/worked-example-max-nonce-vs-next.md`](../../tracks/state-models/worked-example-max-nonce-vs-next.md)（不变量 175）。initcode 超界不是已经是部署代码超界。按字收跳转分析费不是已经跑完构造。精读：[`../../tracks/implementation/worked-example-initcode-vs-runtime.md`](../../tracks/implementation/worked-example-initcode-vs-runtime.md)（不变量 176）。创建结束返回的运行时代码超界不是已经是 initcode 超界。这次失败是耗尽气不是已经整笔非法。规范 EIP-170 不是不变量 170。精读：[`../../tracks/implementation/worked-example-returned-vs-initcode.md`](../../tracks/implementation/worked-example-returned-vs-initcode.md)（不变量 185）。出块者地址开跑时已在热集合不是已经访问过。开跑已热不是已经付给出块者。开跑已热不是 169 那几个预填已经覆盖出块者。精读：[`../../tracks/implementation/worked-example-coinbase-vs-prefill.md`](../../tracks/implementation/worked-example-coinbase-vs-prefill.md)（不变量 187）。新创建要存上链的代码以保留首字节开头不是已经是对象格式已经部署。链上已有以该字节开头的代码不是已经被本页改语义。精读：[`../../tracks/implementation/worked-example-reserved-prefix-vs-eof.md`](../../tracks/implementation/worked-example-reserved-prefix-vs-eof.md)（不变量 188）。带回剩余气的回滚不是已经像非法指令那样把剩余气烧光。不够付这道回滚自己的费不是已经留下剩余气。精读：[`../../tracks/implementation/worked-example-revert-vs-invalid.md`](../../tracks/implementation/worked-example-revert-vs-invalid.md)（不变量 177）。静态帧不是已经是高级语言的只读函数。没转账的普通调用不是已经是静态帧。精读：[`../../tracks/implementation/worked-example-static-vs-view.md`](../../tracks/implementation/worked-example-static-vs-view.md)（不变量 178）。空不是已经不存在。死不是已经一种对象。精读：[`../../tracks/state-models/worked-example-empty-vs-dead.md`](../../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）。
复制状态机：同一 `S`、同一 `T`，所有诚实副本必须得到同一 `S'`。  
L2.2 已讲热点与 nonce。本课问：把「任意计量过的程序」放进去之后，确定性还钉在哪。

---

## B. 核心问题

**EVM 为什么能跑循环和合约，却仍然自称复制状态机？gas 挡的是什么，挡不了什么？**

---

## C. 直觉（ELI15）

教室里每人发同一本练习册。题目可以很难，但标准答案必须唯一。

- 若题目写「看墙上的钟填空」，每个人会填不同时间 → 状态分裂。
- 若题目写「一直加一」，有人算到明年 → 全班停工。

所以规则变成：

1. 只许用练习册里已经写死的数字（交易字节、当前状态），不许看窗外。
2. 每一步消耗「体力券」。券用完就停，即使没算完。

gas 是体力券，不是「越贵越正确」。

---

## D. 正式定义

**状态转移（逻辑级）**

```text
(S, tx)  --StateTransition-->  (S', receipt)  或拒绝入块
```

对已纳入执行块的交易，典型路径（事实，Yellow Paper / 执行规范家族）：

1. 验签名、chain id、nonce、余额是否够付上限费用。交易带了类型号不是已经解开内层；旧式列表不是已经是信封；2718 不是 1559。精读：[`../../tracks/implementation/worked-example-typed-vs-legacy.md`](../../tracks/implementation/worked-example-typed-vs-legacy.md)（不变量 167）。列出地址或槽不是已经访问过；列表外不是已经不能碰。精读：[`../../tracks/implementation/worked-example-listed-vs-accessed.md`](../../tracks/implementation/worked-example-listed-vs-accessed.md)（不变量 168）。本笔第一次碰不是已经热；发送者开跑已在集合不是任意地址已经热。精读：[`../../tracks/implementation/worked-example-cold-vs-warm.md`](../../tracks/implementation/worked-example-cold-vs-warm.md)（不变量 169）。
2. 扣预付 gas 对应的费用（具体扣费顺序以现行规范为准）。
3. 跑 EVM。成功则提交写集；失败（revert 等）则回滚执行写集，**仍可能扣 gas、推进 nonce**。
4. 出收据：成功位、累计 gas、日志。

**确定性禁令（事实）**

共识输入不得包含：节点本地时钟、本地随机数、未在块里承诺的 RPC 数据、磁盘遍历顺序。  
预编译与 gas 表必须是规范对象。两客户端对同一操作码计量不同 = 实现层分叉。

**gas 是什么 / 不是什么**

| 是 | 不是 |
|---|---|
| 对 CPU / 内存 / 存储访问的计量 | 手续费市场的全部（小费、blob 费另算）。blob gas ≠ 普通执行 gas：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145） |
| 防无限循环变成网络武器 | 「付得起 = 交易正确」 |
| 让恶意程序有上界 | 防合约逻辑偷钱 |

**事实：** 一笔「执行失败但仍被包含」的交易，可以是合法块的一部分。钱包显示红色，链上 nonce 已走。  
**推断：** 用户把「失败」理解成「像没发生」，是产品层错觉，不是协议回滚了包含。

---

## E. 最小案例

账户 A：`balance=10 ETH 等值单位, nonce=7`（数字只为讲结构）。

- T1：nonce 7，调用合约，中途 revert。块仍包含 T1。nonce → 8，A 少了一笔 gas 费，合约存储不改。
- T2：nonce 8，普通转账，成功。
- T3：与 T1 同一 nonce 7，后到。不得再被同一账户成功包含。

若某客户端对 revert 不增加 nonce、另一客户端增加：同一块两个状态根。这是 **实现保证** 事故，不是「EVM 数学废了」。

---

## F. 真实项目

Ethereum 执行层。档案：`protocols/ethereum/`。  
对比：Bitcoin Script 故意小；Cosmos 应用自己定义 `Apply`；Solana 程序也必须确定，但锁模型不同（L6）。

---

## G. 源码入口

预告，先规范后实现：

1. 执行规范 / Yellow Paper 的状态转移。
2. 某客户端的 `ApplyTransaction` / `StateTransition`。
3. gas 表与预编译列表。

不要先读钱包 SDK。

---

## H. 攻击者模型

- 让节点用本地时间当合约输入（实现 bug）。
- 找 gas 计量与真实成本严重偏离的操作，做资源攻击（经济/部署）。
- 重放：缺 chain id 的旧签名可跨链重放（历史教训方向；具体 CVE/EIP 以原文为准）。
- 用户层：RPC 返回假收据。密码学与协议仍可对，钱已按假界面被骗走。

---

## I. 代价

得到通用计算：规范爆炸、攻击面变合约语言、状态因「方便写」而胀（下一课与 5.4）。  
计量必须跟实现一起升级；计量错了和状态根错了一样能裂链。

---

## J. 对「不确定」的意义

**建议：** 第一版结算机需要「计量过的 `Apply`」，不需要 EVM。  
偷三样：确定性禁令、失败也有明确 nonce/费语义、同一字节两实现同根。  
不要偷：Solidity 生态、把「能跑任意程序」当成第一版目标。

---

## 精密检查

| 层 | 本课 |
|---|---|
| 密码学 | 签名与 chain id；不决定 EVM 计量 |
| 协议 | 确定性 `Apply`、失败交易的 nonce/费语义 |
| 实现 | 两客户端 gas 表必须同 |
| 部署 | 本地时间不得进共识 |
| 经济 | gas 不是费用市场全部 |

**禁止假学习：** 「执行失败 = 链上没发生。」「gas 贵 = 更安全。」「都叫 gas = 同一本账。」「基础费 = 给矿工。」「烧掉 = MEV 已解决。」「弹性 = 市场已经齐。」「`TSTORE` = 已经进账户。」「瞬时 = memory。」「`SELFDESTRUCT` = 账户已经没了。」「有钥 = 已经能发。」「`eth_call` 绿 = 已经能进块。」「带了类型号 = 已经解开内层。」「2718 = 1559。」「带了访问列表 = 已经访问过。」「没列入 = 已经不能碰。」「开跑 = 任意地址已经热。」「本笔读过 = 下一笔还热。」「2929 = 2930。」「nonce 很大 = 还能加一。」「创建碰到上限 = 已经创建。」「2681 = 155。」「合约大小限制 = 已经管 initcode。」「收了分析费 = 已经创建。」「3860 = 170。」「返回超界 = 已经是 initcode 超界。」「这次失败 = 已经整笔非法。」「规范 170 = 不变量 170。」「开跑已热 = 已经含出块者。」「出块者已热 = 已经访问过。」「出块者已热 = 已经付过。」「3651 = 2929。」「3651 = 1559。」「coinbase = 已经是 163。」「不能用这个开头 = 已经是对象格式。」「已有同首字节 = 已经被改。」「3541 = 170。」「3541 = 3860。」「失败 = 已经烧光剩余气。」「回滚 = 非法指令。」「140 = 103。」「view = 已经静态。」「没转账 = 已经只读。」「214 = 140。」「空 = 已经没了。」「规范 161 = 不变量 161。」「161 = 103。」「看见授权名单 = 已经委托。」「委托指示 = 已经是目标代码。」「7702 = 已经解除 3607。」「本笔失败 = 已经撤回委托。」「7702 = 3607。」「7702 = 2718。」「状态里能读哈希 = 已经改了 BLOCKHASH。」「系统写入父哈希 = 窗口已齐。」「2935 = 4788。」「看见 calldata 地板 = 已经改了执行气。」「数据为主更贵 = 普通转账也更贵。」「预留了地板 = 已经烧到。」「7623 = 4844。」「7623 = 1559。」「7623 = 2028。」「有了 BLS12-381 预编译 = 已经在验 BLS。」「加法不查子群 = MSM 也不查。」「2537 = 196。」「看见 RLP 编码硬帽 = 已经改了气限。」「流言不传 = 执行层已经非法。」「留边 = 已经并编码。」「7934 = 7623。」「7934 = 1559。」「7934 = 96。」「看见单笔气帽 = 已经改了块气限。」「入池拒 = 块已验。」「块里超帽 = 只是策略。」「7825 = 7934。」「7825 = 7623。」「7825 = 96。」「有了 P256 预编译 = 已经在验 k1。」「验绿 = 已经不可延展。」「空输出 = 已经烧光。」「兼容 = 7212 洞已没。」「7951 = 2537。」「7951 = ECRECOVER。」「7951 = 116。」「看见模幂长度帽 = 已经改了计价。」「超帽 = 已经算出。」「有界 = 已经换成 EVM。」「7823 = 198 重定价。」「7823 = 7825。」「7823 = 7951。」「看见数前导零 = 已经更便宜 ZK。」「动机写了后量子 = 已经有后量子签。」「能表达最低位 = 已经有数尾零。」「7939 = 206。」「看见默认气限 = 已经是协议帽。」「绑到硬分叉 = 共识已改。」「默认齐了 = 已经是单笔帽。」「7935 = 203。」「7935 = 202。」「7935 = 96。」「看见块级名单 = 已经并行。」「强制名单 = 已经是 2930。」「事后差 = 已经不跑。」「7928 = 168。」「7928 = 143。」「7928 = 122。」「看见内存拷 = 已经是身份预编译。」「像缓冲 = 必须真分配。」「能重叠拷 = 已经是 calldata 拷。」「5656 = 2929。」「5656 = 208。」「看见压零 = 已经是带立即数的压 0。」「没有立即数 = 已经改了跳转分析。」「旧字节碰巧用了这个码 = 行为已经不变。」「3855 = 5656。」「3855 = 216。」「看见基础费指令 = 已经改了市场。」「能读到 = 已经给了出块者。」「跑之前就有这个数 = 已经改了头。」「3198 = 1559。」「3198 = 158。」「看见 blob 基础费指令 = 已经是 3198。」「能读 blob 价 = 已经并账。」「跑之前就有这个数 = 已经改了 4844。」「7516 = 3198。」「7516 = 218。」  
**边界：** 不讲 Solidity；不把某一硬分叉的 gas 常数当永恒。基础费 ≠ 小费：[`../../tracks/mempool/worked-example-basefee-vs-tip.md`](../../tracks/mempool/worked-example-basefee-vs-tip.md)（不变量 158）。瞬时存储 ≠ 账户持久存储：[`../../tracks/state-models/worked-example-transient-vs-storage.md`](../../tracks/state-models/worked-example-transient-vs-storage.md)（不变量 159）。后来的 SELFDESTRUCT ≠ 账户已经删掉：[`../../tracks/state-models/worked-example-selfdestruct-vs-delete.md`](../../tracks/state-models/worked-example-selfdestruct-vs-delete.md)（不变量 160）。发送者已有代码 ≠ 已经能当 EOA 发交易：[`../../tracks/state-models/worked-example-code-sender-vs-eoa.md`](../../tracks/state-models/worked-example-code-sender-vs-eoa.md)（不变量 162）。nonce 顶到规范上限 ≠ 已经还能加一：[`../../tracks/state-models/worked-example-max-nonce-vs-next.md`](../../tracks/state-models/worked-example-max-nonce-vs-next.md)（不变量 175）。initcode 超界 ≠ 已经是部署代码超界：[`../../tracks/implementation/worked-example-initcode-vs-runtime.md`](../../tracks/implementation/worked-example-initcode-vs-runtime.md)（不变量 176）。创建结束返回的运行时代码超界 ≠ 已经是 initcode 超界：[`../../tracks/implementation/worked-example-returned-vs-initcode.md`](../../tracks/implementation/worked-example-returned-vs-initcode.md)（不变量 185）。出块者地址开跑时已在热集合 ≠ 已经访问过：[`../../tracks/implementation/worked-example-coinbase-vs-prefill.md`](../../tracks/implementation/worked-example-coinbase-vs-prefill.md)（不变量 187）。新创建要存上链的代码以保留首字节开头 ≠ 已经是对象格式已经部署：[`../../tracks/implementation/worked-example-reserved-prefix-vs-eof.md`](../../tracks/implementation/worked-example-reserved-prefix-vs-eof.md)（不变量 188）。带回剩余气的回滚 ≠ 已经烧光剩余气：[`../../tracks/implementation/worked-example-revert-vs-invalid.md`](../../tracks/implementation/worked-example-revert-vs-invalid.md)（不变量 177）。静态帧 ≠ 已经是高级语言只读：[`../../tracks/implementation/worked-example-static-vs-view.md`](../../tracks/implementation/worked-example-static-vs-view.md)（不变量 178）。空 ≠ 已经不存在：[`../../tracks/state-models/worked-example-empty-vs-dead.md`](../../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）。blob gas ≠ 普通执行 gas：[`../../tracks/light-clients/worked-example-blob-fee-vs-gas.md`](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)（不变量 145）。块 gas 上限 ≠ 墙钟已有界：[`../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md`](../../tracks/failure-museum/ethereum-2021-05-state-gas-not-time.md)（不变量 101）。OOG 结束 ≠ 空账户删除已回滚：[`../../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md`](../../tracks/failure-museum/ethereum-2016-11-oog-empty-account.md)（不变量 103）。预编译中途出错 ≠ SDK 已写入已经撤回：[`../../tracks/failure-museum/isa-2025-004.md`](../../tracks/failure-museum/isa-2025-004.md)（不变量 117）。内层改过 ≠ 外层已经看见：[`../../tracks/failure-museum/asa-2026-002.md`](../../tracks/failure-museum/asa-2026-002.md)（不变量 118）。正确兑现委托语义 ≠ 预编译信任已经改过：[`../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md`](../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md)（不变量 119）。类型信封 ≠ 已经解开内层：[`../../tracks/implementation/worked-example-typed-vs-legacy.md`](../../tracks/implementation/worked-example-typed-vs-legacy.md)（不变量 167）。列入访问列表 ≠ 已经访问过：[`../../tracks/implementation/worked-example-listed-vs-accessed.md`](../../tracks/implementation/worked-example-listed-vs-accessed.md)（不变量 168）。本笔第一次碰 ≠ 已经热：[`../../tracks/implementation/worked-example-cold-vs-warm.md`](../../tracks/implementation/worked-example-cold-vs-warm.md)（不变量 169）。看见授权名单 ≠ 已经委托成功：[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)（不变量 190）。看见状态里的历史执行哈希 ≠ 已经是 BLOCKHASH：[`../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md`](../../tracks/light-clients/worked-example-history-hash-vs-blockhash.md)（不变量 195）。看见 calldata 地板 ≠ 已经改了执行气：[`../../tracks/implementation/worked-example-calldata-floor-vs-execution.md`](../../tracks/implementation/worked-example-calldata-floor-vs-execution.md)（不变量 197）。看见 BLS12-381 预编译 ≠ 已经在验 BLS 签：[`../../tracks/crypto/worked-example-bls-precompile-vs-verify.md`](../../tracks/crypto/worked-example-bls-precompile-vs-verify.md)（不变量 199）。不要写怎样冒充。不抄类型取值范围。不写怎样跨类型复用签名。不抄气价。不写怎样生成访问列表。不写怎样灌冷访问。不写怎样构造授权元组。看见 RLP 编码硬帽 ≠ 已经改了气限：[`../../tracks/implementation/worked-example-rlp-cap-vs-gas.md`](../../tracks/implementation/worked-example-rlp-cap-vs-gas.md)（不变量 202）。不要抄编码上限字节。不要写怎样刚好塞进帽下。看见单笔气帽 ≠ 已经改了块气限：[`../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md`](../../tracks/implementation/worked-example-tx-gas-cap-vs-block.md)（不变量 203）。不要抄单笔气帽取值。不要写怎样把一笔拆到帽下。看见 P256 验签预编译 ≠ 已经在验 k1：[`../../tracks/crypto/worked-example-p256-vs-k1.md`](../../tracks/crypto/worked-example-p256-vs-k1.md)（不变量 204）。不要抄预编译地址 / 气价。不要写怎样造可延展签。看见 MODEXP 输入长度帽 ≠ 已经改了计价公式：[`../../tracks/implementation/worked-example-modexp-bound-vs-price.md`](../../tracks/implementation/worked-example-modexp-bound-vs-price.md)（不变量 206）。看见数前导零操作码 ≠ 已经更便宜的 ZK 证明：[`../../tracks/implementation/worked-example-clz-vs-zk.md`](../../tracks/implementation/worked-example-clz-vs-zk.md)（不变量 208）。看见客户端默认气限 ≠ 已经是协议帽：[`../../tracks/implementation/worked-example-default-gas-vs-cap.md`](../../tracks/implementation/worked-example-default-gas-vs-cap.md)（不变量 211）。看见块级访问名单 ≠ 已经并行跑完：[`../../tracks/implementation/worked-example-block-list-vs-parallel.md`](../../tracks/implementation/worked-example-block-list-vs-parallel.md)（不变量 212）。看见内存拷贝指令 ≠ 已经是身份预编译：[`../../tracks/implementation/worked-example-mcopy-vs-identity.md`](../../tracks/implementation/worked-example-mcopy-vs-identity.md)（不变量 216）。看见压零指令 ≠ 已经是带立即数的压 0：[`../../tracks/implementation/worked-example-push0-vs-push1.md`](../../tracks/implementation/worked-example-push0-vs-push1.md)（不变量 217）。看见基础费指令 ≠ 已经改了费用市场：[`../../tracks/implementation/worked-example-basefee-opcode-vs-market.md`](../../tracks/implementation/worked-example-basefee-opcode-vs-market.md)（不变量 218）。看见 blob 基础费指令 ≠ 已经是执行层基础费指令：[`../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md`](../../tracks/implementation/worked-example-blobbasefee-vs-basefee.md)（不变量 219）。不要抄操作码号 / 气价。不要写怎样拼数尾零。不要抄默认取值。不要写怎样抬气限。不要抄条数或地址。不要写怎样造名单。不要写怎样造真缓冲。不要写怎样打重叠拷。不要写怎样在旧字节上赌分叉后行为。不要写怎样设悬赏或做气期货。不要写怎样按 blob 价做产品。
