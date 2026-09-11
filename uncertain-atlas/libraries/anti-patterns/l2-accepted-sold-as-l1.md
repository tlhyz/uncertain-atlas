# 反模式：L2 accepted 被写成 L1 accepted，或程序哈希被写成物理定律

> **事实 / 推断 / 建议** 已分开。
> 真值：[Starknet 滤网](../../protocols/starknet/README.md)、[L7.4](../../courses/level-07-modular/L07-M04-rollup-tenant.md)、[不变式 28](../invariants/README.md#28-有效性证明必须点名被锁程序且两层accepted不得混)。

---

## 一句话

看见「有效性证明」或「ACCEPTED_ON_L2」，就写成「L1 已更新、用户可提、电路永不可改」。

---

## 它看起来像什么

- 「ZK rollup 所以一出块就和以太坊一样最终」
- 「验 STARK = 桥已放行」
- 「程序哈希不能改，所以没有升级风险」
- 「有证明所以不需要状态差 / DA」

---

## 事实

- 官方文档：`ACCEPTED_ON_L2` 是 L2 共识最终的块；`ACCEPTED_ON_L1` 是以太坊上 Starknet 状态高度追上。
- Core 合约登记 SNOS / aggregator 的 program hash；破坏性变更要改登记。
- 证明之外还要能用来重建状态的数据（状态差）。

---

## 正确写法

| 对象 | 能说的句子 |
|------|------------|
| L2 共识已收 | 「ACCEPTED_ON_L2；L1 根尚未必更新」 |
| L1 已更新 | 「ACCEPTED_ON_L1；仍要问桥与 DA」 |
| 验证明 | 「对当前登记程序哈希为真；改哈希是升级」 |

---

## 对不确定的意义（建议）

两个 accepted 词必须分开写。缺程序哈希的「ZK 结算」四个字，这条就红。
