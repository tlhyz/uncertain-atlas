# 反模式：域外 Builder API 被写成共识，或盲头被写成本地排序

> **事实 / 推断 / 建议** 已分开。
> 真值：[谁排序](../../tracks/mempool/worked-example-who-orders.md)、[builder-specs README](https://github.com/ethereum/builder-specs/blob/main/README.md)、[不变式 27](../invariants/README.md#27-排序权必须点名谁写列表谁签头)。

---

## 一句话

看见「PBS」或「提议者签了块」，就写成「共识已经拆分排序、验证者自己挑了每一笔」，不指出文献是 builder-specs 还是 consensus-specs，也不指出签的是盲头还是完整载荷。

---

## 它看起来像什么

- 「以太坊共识 = PBS」
- 「用了 MEV-Boost 所以无需信任」
- 「提议者签了所以他审查过交易列表」
- 把研究中的 enshrined PBS 写成已激活

---

## 事实

- Builder API：临时、信任更高、不改基础协议；提议者先签 `ExecutionPayloadHeader`，再等揭示。
- 盲块签名域仍是 `DOMAIN_BEACON_PROPOSER`。
- 信标状态机吃的是完整载荷，不是盲块容器。

---

## 正确写法

| 路径 | 能说的句子 |
|------|------------|
| 本地出块 | 「本 slot 提议者写列表并签完整载荷」 |
| Builder API | 「提议者签了盲头；列表由外部 builder 写，揭示依赖中继」 |
| 将来协议内 PBS | 「以当时信标规范为准；草案不得当已激活」 |

---

## 对不确定的意义（建议）

先写「谁写顺序」。缺这句的「PBS」三个字母，这条就红。
