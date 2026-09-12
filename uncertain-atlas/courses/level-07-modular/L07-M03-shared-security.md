# L7.3 共享安全

优先级：重要  
先修：L7.1，L7.2，Polkadot 档案

---

## A. 先修知识

小验证者集合 ≈ 便宜的经济攻击。Bitcoin 的教训是安全来自昂贵的攻击，不是来自「我们也是一条链」。

---

## B. 核心问题

**借用大链安全时，你继承了哪一层保证，哪些保证仍然是自己的，哪些新洞被打开？**

---

## C. 直觉

小区请市警察局巡逻，不再自雇三个保安。  
小偷要买通的是市局，不是三个保安。这是借来的**经济安全**。

但：

- 你家门锁坏了，市局不管（应用/runtime bug）。  
- 巡逻协议规定「必须能打开储藏室检查」——储藏室被锁死就是新攻击（数据不可用）。  
- 小区之间传话的信使可能造假（跨链消息）。

所以「我们借用了 Polkadot/以太坊安全」最多说对了一半。

---

## D. 正式定义

**共享安全：** 候选执行的最终性与经济惩罚，绑定到外层验证者集合，而不是绑定到应用链自己的小集合。

必须同时成立：

1. 外层最终  
2. 执行数据可用（否则无法惩罚说谎）  
3. 有复验或有效性证明路径  
4. 跨链消息有自己的域分离与重放规则

缺 2 或 3：外层最终的是「一团无法检查的雾」。

**事实：** Polkadot 用 backing + availability + approval 逼近 2 和 3。Rollup 用 DA 层 + 欺诈/有效性证明。Restaking 是另一条「借经济」路线：抵押对象是**已经**为以太坊质押的 ETH/LST，罚没条件由 AVS 定义、不必客观可归属。思想同类、对象不同。过滤器：[`../../protocols/eigenlayer/README.md`](../../protocols/eigenlayer/README.md)。

---

## E. 最小案例

平行链 collator 对用户说「已上链」。中继尚未最终，可用性未满足。  
用户放货。候选被丢弃。  
错在用户层语义，不是「共享安全没用」，而是**借来的安全还没接到这笔交易上**。

---

## F. 真实项目

Polkadot 平行链；Ethereum rollup；对比：独立小 PoS 链自养安全。

---

## G. 源码

看可用性与争议，不看平行链转账 UI。

---

## H. 攻击者视角

1. 打子协议（不可用、漏审批）。  
2. 打 runtime 升级钥匙。  
3. 打 XCM/桥。  
4. 打「已打包但未最终」的文案。

---

## I. Trade-off

借安全：小链不自养天价验证者。  
换：复杂度、延迟、治理、新协议洞。  
自养：简单，安全随自己变弱。

---

## J. 对「不确定」的意义

**建议：** 第一版做独立结算 L1，把安全假设写短。  
若以后当别人的执行租户或租别人的安全，先把 L7.2 的 DA 测死，再谈借用。  
「挂在大链下」不是设计完成。

---

## 精密检查

| 层 | 本课钉在哪 |
|---|---|
| 密码学 | 借用的是房东的共识 / DA 假设，不是应用电路 |
| 协议 | 共享安全 ≠ 应用正确；Polkadot 要 relay 最终，不是 collator RPC |
| 实现 | 跨链消息编码必须两客户端相同 |
| 部署 | 租户依赖房东在线 |
| 经济 | 桥里的钱 vs 能罚的钱 |

**禁止假学习：** 「共享安全所以应用也安全。」
**边界：** restaking 不因有名写 19 节。过滤器：[`../../protocols/eigenlayer/README.md`](../../protocols/eigenlayer/README.md)。NEAR Nightshade 是一条链上的 chunk，不是本课的「小链借用中继」；见 `protocols/near/`。Babylon 只过过滤器：`protocols/babylon/`。交易解码深度有界 ≠ runtime API 再解整块已安全：[`../../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md`](../../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md)（不变量 97）。组下标 ≠ 票向量下标：[`../../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md`](../../tracks/failure-museum/kusama-2025-08-24-group-index-votes.md)（不变量 98）。Active ≠ Confirmed：[`../../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md`](../../tracks/failure-museum/kusama-2024-02-15-disabled-active-dispute.md)（不变量 99）。链下内存禁用 ≠ 已确认争议已经不参与：[`../../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md`](../../tracks/failure-museum/kusama-2025-05-09-offchain-disable.md)（不变量 100）。改冻结门槛 ≠ 选举地板已经配对：[`../../tracks/failure-museum/polkadot-2026-06-election-score-floor.md`](../../tracks/failure-museum/polkadot-2026-06-election-score-floor.md)（不变量 110）。preserve_origin 为真 ≠ 出站已经带了改 origin 的指令：[`../../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md`](../../tracks/failure-museum/polkadot-2026-03-xcm-preserve-origin.md)（不变量 113）。不要写怎样拼跨链指令。
