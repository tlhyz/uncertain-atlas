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

**重放：** 同链靠 nonce；跨链靠 chain id 进签名（Ethereum EIP-155）。

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

**禁止假学习：** 「账户模型就是以太坊。」「nonce 能防一切重放。」
**边界：** EVM/gas 在 L5.1。空地址 ≠ 还没有账户类型：博物馆 [Barberry](../../tracks/failure-museum/barberry.md)（不变量 83）。被挡模块账户是另一句：[ASA-2024-003](../../tracks/failure-museum/asa-2024-003.md)。StateDB 可花 ≠ 归属锁定已经从同一笔写回排除：[`../../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md`](../../tracks/failure-museum/cosmos-evm-2026-08-statedb-vesting.md)（不变量 115）。预编译中途出错 ≠ SDK 已写入已经撤回：[`../../tracks/failure-museum/isa-2025-004.md`](../../tracks/failure-museum/isa-2025-004.md)（不变量 117）。内层改过 ≠ 外层已经看见：[`../../tracks/failure-museum/asa-2026-002.md`](../../tracks/failure-museum/asa-2026-002.md)（不变量 118）。正确兑现委托语义 ≠ 预编译信任已经改过：[`../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md`](../../tracks/failure-museum/avalanche-2025-delegatecall-precompile.md)（不变量 119）。不要写怎样委托锁定、怎样调 gas、怎样冒充。
