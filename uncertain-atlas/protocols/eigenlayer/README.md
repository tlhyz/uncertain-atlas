# EigenLayer — 滤网页（不是 19 节档案）

> **事实 / 推断 / 建议** 已分开。
> 树节点：[M7.5 再质押 / 共享安全](../../index/01-knowledge-tree.md)。
> 对照：[L7.3 共享安全](../../courses/level-07-modular/L07-M03-shared-security.md)、[Polkadot 档案](../polkadot/README.md)、[Babylon 滤网](../babylon/README.md)。
> **不是** 主研究链，**不做** 19 节档案。ELIP / 产品文档 ≠ 以太坊共识规范。

---

## 为什么只开滤网

[M7.5](../../index/01-knowledge-tree.md) 要的独特对象是：**已经质押过的 ETH（或 LST）被再次声明为另一套服务的可罚没抵押**。

EigenLayer 是目前公开文献里把这句说得最清楚的产品名。它 **没有** 一份像 CometBFT 那样的共识规范。本页主文献是 [ELIP-002](https://github.com/eigenfoundation/ELIPs/blob/main/ELIPs/ELIP-002.md)（产品改进提案）和 [官方罚没概念页](https://docs.eigencloud.xyz/eigenlayer/concepts/slashing/slashing-concept)。按资料优先级：能引用这些定义，不能把它们当成「以太坊共识的一部分」。

---

## 独特对象（官方文档，事实）

| 对象 | 文档怎么说 | 它不是 |
|------|------------|--------|
| Restaking | 把 **已经** 为以太坊质押的 ETH 或 LST，再声明为 AVS（Actively Validated Service）的抵押 | 在 EigenLayer 里再铸一条与信标链无关的新质押资产当「以太坊质押」 |
| AVS | 自己定义验证任务和（文档写明）**自己的罚没条件** | 自动继承 Casper 的 surround/double 罚没 |
| 罚没 | ELIP-002 原文：协议提供「最大灵活」的罚没函数，AVS 可对其 Operator Set 内的 Operator **以任何理由**罚没；**不必**客观可归属（链上可证）。官方概念页重复同一句 | Bitcoin UTXO 被比特币脚本锁死；也不是 CometBFT `DuplicateVoteEvidence` 那种协议内证据形状 |
| 以太坊共识 | 仍由信标链验证者跑 | restake 不让你「变成另一个信标最终确定」 |

**事实：** 文档把 restake 写成 **额外的、AVS 定义的可罚没声明**，叠在已有质押之上。

**事实：** 文档 **没有** 声称 AVS 罚没等价于以太坊协议罚没，也没有声称轻客户端可以只看 restake 状态就验证信标头。

---

## 三句对照（建议你记这一张表）

| 产品 | 抵押对象在哪 | 谁定义「作恶」 | 共享的是什么 |
|------|--------------|----------------|--------------|
| Polkadot | 中继链 DOT 质押 | 中继 + 平行链协议（批准/可用性） | 中继验证者对平行链的检查职责 |
| Babylon | **比特币 UTXO 仍在比特币账本** | 比特币脚本 / 其协议声明的罚没路径 | 比特币上的锁，不是「BTC 跑 Cosmos 共识」 |
| EigenLayer | **已为以太坊质押的 ETH/LST** | **AVS**（文档：可为非客观条件） | 同一份质押被第二份罚没声明盯着 |

三句都叫「共享安全」或「再质押」时，抵押对象和罚没定义人不同。

---

## 滤网结论

| 问题 | 答案 |
|------|------|
| 有没有独特协议对象？ | **有**：restake + AVS 自定罚没。够写进 M7.5 对照，不够开 19 节 |
| 有没有共识规范级文献？ | **没有**（官方文档 + 合约，不是 beacon spec） |
| 应不应该抄进不确定 v1？ | **建议：不。** 不确定 v1 是可验证结算机。不要把「同一 ETH 同时服务任意 AVS」当成默认安全模块 |
| 数字 | **禁止** 抄 TVL、restake 总量、AVS 个数（官网会变） |

---

## 对不确定的意义（建议）

- 结算机的罚没条件应尽量 **客观、可上链归因**（见 [证据 ≠ 罚没](../../tracks/economic/worked-example-evidence.md)、[Casper 谓词](../../tracks/economic/worked-example-casper-slashing.md)）。
- 若将来有「再声明同一份抵押」的设计，必须单列：第二份声明的证据形状、谁执行、与第一份冲突时谁先到。
- 不要用 EigenLayer 的文档句冒充以太坊规范句。

---

## 禁句

- 「EigenLayer = 以太坊共享安全」（和 Polkadot / Babylon 糊在一起）
- 「restake 之后轻客户端更安全」
- 「AVS 罚没 = Casper 罚没」
- 任何未标注日期的 TVL / restake 数量
- 把本页升级成 19 节档案（文献等级不够）
