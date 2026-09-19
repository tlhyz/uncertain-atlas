# L4.5 验证者集合何时算数

优先级：必学（知识树 M4.4）  
先修：L4.1–L4.4

---

## A. 先修知识

quorum 按**投票权**不是人头。  
ABCI 应用可以在某高度改验证者集合。两套权重若同时「合法」，相交证明对哪一套算？

---

## B. 核心问题

**集合变更在哪个高度生效？未生效的票算不算？换集时安全证明还成立吗？**

---

## C. 直觉（ELI15）

班级投票权写在黑板上。  
今天表决时，必须用**今天黑板**上的名单。有人把明天的名单提前拿出来拉票，那张票今天无效。

更阴的：一半人以为黑板是旧的，一半人以为是新的。两边都能凑出「2/3」，交点里没有共同的诚实者——因为他们根本不在同一张表上。

---

## D. 正式定义

**Validator set V(h)**

高度 h 的提议、prevote、precommit，只对 `V(h)` 计权。  
`V(h)` 如何从 `V(h-1)` 与应用回调算出，是协议对象，必须唯一。

**生效延迟（事实：CometBFT ABCI++）**

高度 H 的 `FinalizeBlock` 返回 `validator_updates`：H+1 更新 `NextValidatorsHash`，**H+2** 新集合开始投票（`ValidatorsHash`），H+3 的 `*_last_commit` 才带新集合。应用要求原文：处理 H 之后返回的更新只在块 H+2 生效。  
`consensus_param_updates` 是另一条：H 的更新用于 H+1。  
精读：[`../../tracks/consensus/worked-example-validator-delay.md`](../../tracks/consensus/worked-example-validator-delay.md)。

目的：投票过程中集合不动，相交证明有固定 n、f。

**未对齐的两种视图（实现/协议事故）**

客户端 A 认为 `V(h)=Old`，客户端 B 认为 `V(h)=New`。  
两张合法 QC 可能对两个块成立，因为相交假设的前提（同一 n、同一成员）破了。

**事实：** 「2/3」没有集合就没有定义。  
**建议：** 任何升级、惩罚、退出，必须指定：哪一高度的哪一次计票用哪张表；旧票过期怎么删。

---

## E. 最小案例

Old = {A,B,C,D} 各 1 权，f=1，quorum=3。  
New = {A,B,E,F}。  
若 A,B,C 用 Old 给块 X 出 QC，A,B,E 用 New 给块 Y 出 QC，两边都「3 票」。交点 {A,B} 在两套规则里都算诚实也可能同时合法——因为规则本身分叉了。  
这不是拜占庭超过 f，是**集合版本未进规范哈希**。

---

## F. 真实项目

CometBFT + Cosmos SDK staking；Ethereum 验证者登记与 epoch 边界（另一套，见 L5.2，不要直接套 Tendermint 延迟）。  
Polkadot 的 session / era 也是「何时换人」（档案）。当选之后共识是否按质押加权，是另一句：[`../../tracks/consensus/worked-example-npos-equal-weight.md`](../../tracks/consensus/worked-example-npos-equal-weight.md)（不变量 129）。

---

## G. 源码入口

预告：`EndBlock` / 更新验证者的回调、共识把 `LastCommit` 与下一高度 `V` 绑在一起的代码、状态里序列化的 validator hash。  
头里应承诺当前集合哈希，防止两节点各用各的表。

---

## H. 攻击者模型

- 让应用哈希不含 validator hash。  
- 惩罚/退出交易的生效高度含糊，刷短命投票权。  
- 社会层：紧急换人但不走协议对象（治理对手）。

---

## I. 代价

延迟生效：安全证明干净，用户「我已退出为何还被罚」要解释窗口。  
立刻生效：实现简单，投票中途换人，证明变脏。

---

## J. 对「不确定」的意义

后量子时代验证者密钥要轮换。轮换 = 集合变更。  
必须先有 `V(h)` 的精确定义，再谈算法敏捷。  
升级钥匙若能绕过 `V(h)` 直接改规则，见反模式 admin-god-key。

---

## 精密检查

| 层 | 本课 |
|---|---|
| 密码学 | 投票签在哪把验证者钥上 |
| 协议 | V(h) 唯一、生效高度 |
| 实现 | 两客户端同一高度同一表 |
| 部署 | 节点是否加载了含新表的状态 |
| 经济 | 质押进出、惩罚窗口 |

**禁止假学习：** 「验证者名单在网站上。」「2/3 永远是人数的三分之二。」「2/3 永远是质押的三分之二。」「Finalize 改了验证者，下一高度就按新名单投。」「看见同一高度换轮 = 已经换了集合。」「看见新验证者加进来 = 已经能跳到队头。」「看见优先级差被缩放 = 已经按人头轮。」  
**边界：** 不抄 Cosmos 解绑天数。轻客户端的 `trustingPeriod < unbondingPeriod` 与跳过重叠见 [`../../tracks/light-clients/worked-example-bft-skip.md`](../../tracks/light-clients/worked-example-bft-skip.md)。Ethereum 弱主观性是亲戚、不是同一对象：[`../../tracks/finality/worked-example-weak-subjectivity.md`](../../tracks/finality/worked-example-weak-subjectivity.md)。超多数的单位必须点名：NPoS 当选后官方对照写验证者等权，Cosmos 对照写按质押，见 [`../../tracks/consensus/worked-example-npos-equal-weight.md`](../../tracks/consensus/worked-example-npos-equal-weight.md)（不变量 129）。本课仍只钉集合何时算数，不重讲 Phragmén。同一高度换轮 ≠ 已经换了集合；新加入 ≠ 已经能跳到队头：[`../../tracks/consensus/worked-example-round-vs-set.md`](../../tracks/consensus/worked-example-round-vs-set.md)（不变量 302）。不要抄惩罚系数。不要写怎样算优先级或怎样缩放。InitChain 空名单不是已经没有集合 not already no set / not already deleted genesis / not already app empty set 正式三事（318 余量）：[`../../tracks/implementation/worked-example-validatorupdate-notempty-vs-bundled.md`](../../tracks/implementation/worked-example-validatorupdate-notempty-vs-bundled.md)（不变量 713）。InitChain 空名单 ≠ 已经没有集合；同一批重复公钥 ≠ 已经能恢复；power 0 ≠ 已经删掉不在集合里的人：[`../../tracks/implementation/worked-example-validatorupdate-vs-set.md`](../../tracks/implementation/worked-example-validatorupdate-vs-set.md)（不变量 318）。不要另写怎样编 `ValidatorUpdate` 或怎样算总权。
