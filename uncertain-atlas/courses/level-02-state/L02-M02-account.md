# L2.2 账户模型

优先级：必学  
先修：L2.1

---

## A. 先修知识

UTXO 把钱当成支票。  
账户模型把钱当成「这个名字下的一个数，外加一格存储」。

---

## B. 核心问题

**账户 + nonce 让钱包和合约好写，却为什么会制造热点和重放政策？**

---

## C. 直觉（ELI15）

银行存折：阿安 = 10。转 4 给阿比，阿安变 6，阿比加 4。  
所有动阿安的交易，都要改**同一格**。这一格就是锁。

为了防止同一张已签字的「转 4」被兑两次，账户常带一个序号 nonce：用过 7，下一张必须是 8。

好处：人好懂，合约好写，一笔就能「从余额扣」。  
坏处：热门账户（交易所、热门合约）变成单行道；序号管理让用户和钱包互相折磨。

---

## D. 正式定义（本科计算机）

账户对象通常包括：余额、nonce、代码（可空）、存储。

`Apply` 对发送者：检查签名、nonce、余额/gas，然后改这些字段。  
对合约：再跑代码，可能改很多存储槽。  
发送者已有代码不是已经能当 EOA 发。RPC 绿不是共识已经放行。精读：[`../../tracks/state-models/worked-example-code-sender-vs-eoa.md`](../../tracks/state-models/worked-example-code-sender-vs-eoa.md)（不变量 162）。看见授权名单不是已经委托成功。代码里是委托指示不是已经是目标合约代码。委托指示不是已经解除 3607。本笔执行失败不是已经撤回写好的委托。精读：[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)（不变量 190）。nonce 顶到规范上限不是已经还能加一。客户端已经用窄整数存 nonce 不是共识已经写了这道上限。精读：[`../../tracks/state-models/worked-example-max-nonce-vs-next.md`](../../tracks/state-models/worked-example-max-nonce-vs-next.md)（不变量 175）。空不是已经不存在。死不是已经一种对象。精读：[`../../tracks/state-models/worked-example-empty-vs-dead.md`](../../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）。看见代码哈希指令不是已经看见代码本身。看见返回 0 不是已经是没代码的账户。看见空数据哈希不是已经是账户不存在。精读：[`../../tracks/implementation/worked-example-extcodehash-vs-copy.md`](../../tracks/implementation/worked-example-extcodehash-vs-copy.md)（不变量 221）。看见盐创建指令不是已经是按发送者加序号占址。看见算出来的盐地址不是已经创建。看见本页让碰撞变得可能不是已经覆盖已有代码。精读：[`../../tracks/implementation/worked-example-create2-vs-created.md`](../../tracks/implementation/worked-example-create2-vs-created.md)（不变量 222）。看见弃用警告不是已经改了共识行为。看见本页不是已经改了客户端。看见「以后可能变」不是已经变了。精读：[`../../tracks/implementation/worked-example-deprecate-vs-changed.md`](../../tracks/implementation/worked-example-deprecate-vs-changed.md)（不变量 224）。

**重放：** 同链靠 nonce；跨链靠 chain id 进签名（Ethereum EIP-155）。JSON 里有 chainId 不是已经编进哈希；旧六字段签不是已经防跨链。精读：[`../../tracks/crypto/worked-example-chainid-vs-signed.md`](../../tracks/crypto/worked-example-chainid-vs-signed.md)（不变量 161）。

**事实：** Ethereum 是账户模型 + EVM 的代表。状态在树上，不是「一个 SQL 的 users 表」那么简单，但用户概念是账户。  
**事实：** 两笔交易若写同一账户或同一存储槽，不能随便并行；要锁、要串行、或乐观执行后回滚。

---

## E. 最小案例

```text
Account A: {balance:10, nonce:7}
T1: A→B 4, nonce 7
T2: A→C 4, nonce 8
T3: A→D 1, nonce 7   // 与 T1 抢同一 nonce
```

T1 与 T3 冲突。T1 成功后 T2 才合法。  
T2 不能抢在 T1 前执行（缺 nonce 7）。这就是账户模型的串行味道。

热点：所有人付费给同一个合约槽，等于所有人挤同一扇门。

---

## F. 真实项目

- **Ethereum（事实）**：EOA + 合约账户。  
- **Solana（事实）**：也是账户，但交易必须列出将碰到的账户，相当于提前声明锁。这是为并行，不是纯 Ethereum 味道。Level 6。  
- **「不确定」（建议）**：若第一版只做结算，账户模型的热点和 nonce 体验可能是多余复杂度；若第一版就上通用合约，账户几乎躲不开。

---

## G. 源码入口

geth：`StateTransition` / `ApplyTransaction`、账户 trie。预告。

---

## H. 攻击者视角

1. nonce 空洞：卡住后面所有交易。  
2. 替换交易（更高费、同 nonce）让商家看到的那笔消失。  
3. 打热门合约，让全网 TPS 数字变得无意义。  
4. 跨链重放旧交易（忘记 chain id 的年代）。

---

## I. Trade-off

| 得到 | 失去 |
|---|---|
| 编程与钱包直觉、一笔改多处状态 | 冲突隐式、热点、nonce 体验、并行要额外发明 |
| 易做复杂合约 | 状态膨胀、证明「一个账户的值」依赖树 |

---

## J. 对「不确定」的意义

后量子验签已经贵。再让所有结算挤一个热账户，是把自己的 CPU 卖给攻击者。  
读 Solana 的「声明账户」和 Sui 的「所有权」之前，先承认：账户模型的默认并行度是低的。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 授权仍是签；账户 nonce ≠ 签名随机数 k |
| 协议 | 余额 + nonce；重放窗口由规则定义 |
| 实现 | nonce 空洞 / 卡死是实现与产品问题 |
| 部署 | 热账户把 CPU / 锁集中在少数键 |
| 经济 | 热点可被费市场与审查瞄准 |

**禁止假学习：** 「账户模型就是以太坊。」「nonce 能防一切重放。」「nonce 很大 = 还能加一。」「客户端已经窄 = 共识已写上限。」「2681 = 155。」「空 = 已经没了。」「死 = 一种对象。」「规范 161 = 不变量 161。」「看见 chainId = 已经签进哈希。」「`TSTORE` = 已经进账户。」「交易结束丢掉 = 本笔里从未存在。」「`SELFDESTRUCT` = 账户已经没了。」「有钥 = 已经能发。」「`eth_call` 绿 = 已经能进块。」「看见授权名单 = 已经委托。」「委托指示 = 已经是目标代码。」「7702 = 已经解除 3607。」「本笔失败 = 已经撤回委托。」「7702 = 3607。」「看见代码哈希指令 = 已经看见代码。」「返回 0 = 没代码。」「空数据哈希 = 不存在。」「1052 = 161。」「CREATE2 = 已经创建。」「能算出盐地址 = 已经有代码。」「碰撞变得可能 = 已经覆盖。」「1014 = 3860。」「6049 = 已经改了行为。」「6049 = 6780。」「弃用 = 客户端已经改。」
**边界：** EVM/gas 在 L5.1。nonce 顶到规范上限 ≠ 已经还能加一：[`../../tracks/state-models/worked-example-max-nonce-vs-next.md`](../../tracks/state-models/worked-example-max-nonce-vs-next.md)（不变量 175）。空 ≠ 已经不存在：[`../../tracks/state-models/worked-example-empty-vs-dead.md`](../../tracks/state-models/worked-example-empty-vs-dead.md)（不变量 180）。看见代码哈希指令 ≠ 已经看见代码本身：[`../../tracks/implementation/worked-example-extcodehash-vs-copy.md`](../../tracks/implementation/worked-example-extcodehash-vs-copy.md)（不变量 221）。看见盐创建指令 ≠ 已经是按发送者加序号占址：[`../../tracks/implementation/worked-example-create2-vs-created.md`](../../tracks/implementation/worked-example-create2-vs-created.md)（不变量 222）。看见弃用警告 ≠ 已经改了共识行为：[`../../tracks/implementation/worked-example-deprecate-vs-changed.md`](../../tracks/implementation/worked-example-deprecate-vs-changed.md)（不变量 224）。JSON 里的 chainId ≠ 已经编进签名哈希：[`../../tracks/crypto/worked-example-chainid-vs-signed.md`](../../tracks/crypto/worked-example-chainid-vs-signed.md)（不变量 161）。瞬时存储 ≠ 账户持久存储：[`../../tracks/state-models/worked-example-transient-vs-storage.md`](../../tracks/state-models/worked-example-transient-vs-storage.md)（不变量 159）。后来的 SELFDESTRUCT ≠ 账户已经删掉：[`../../tracks/state-models/worked-example-selfdestruct-vs-delete.md`](../../tracks/state-models/worked-example-selfdestruct-vs-delete.md)（不变量 160）。发送者已有代码 ≠ 已经能当 EOA 发交易：[`../../tracks/state-models/worked-example-code-sender-vs-eoa.md`](../../tracks/state-models/worked-example-code-sender-vs-eoa.md)（不变量 162）。空地址 ≠ 还没有账户类型：博物馆 [Barberry](../../tracks/failure-museum/barberry.md)（不变量 83）。被挡模块账户是另一句：[ASA-2024-003](../../tracks/failure-museum/asa-2024-003.md)。StateDB 可花 ≠ 归属锁定已经从同一笔写回排除：[`../../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md`](../../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md)（不变量 115）。预编译中途出错 ≠ SDK 已写入已经撤回：[`../../tracks/failure-museum/isa-2025-004.md`](../../tracks/failure-museum/isa-2025-004.md)（不变量 117）。内层改过 ≠ 外层已经看见：[`../../tracks/failure-museum/asa-2026-002.md`](../../tracks/failure-museum/asa-2026-002.md)（不变量 118）。正确兑现委托语义 ≠ 预编译信任已经改过：[`../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md`](../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md)（不变量 119）。看见授权名单 ≠ 已经委托成功：[`../../tracks/state-models/worked-example-delegation-vs-code.md`](../../tracks/state-models/worked-example-delegation-vs-code.md)（不变量 190）。不要写怎样委托锁定、怎样调 gas、怎样冒充。不抄 nonce 上限取值。不写怎样把序号推到上限。不写怎样构造授权元组。
