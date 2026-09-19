# 反模式：把头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事（325 余量）说成已经是交易默克尔 / 已经是验证者集合锚 / 已经有分开的应用状态

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[头上有 AppHash not already tx-merkle ≠ bundled（325）](../../tracks/implementation/worked-example-queryproof-nottxmerkle-vs-bundled.md)。

## 卖法

把头上有 AppHash / AppHash 字段在 / 头上有应用根 写成已经是交易默克尔 interchangeable / 已经 tx-merkle interchangeable / 已经是 DataHash interchangeable / 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable；把和另外两份并列 / 和 ValidatorsHash、DataHash 并列 / 头上好几份哈希 写成已经是验证者集合锚 interchangeable / 已经 validators-hash interchangeable；把交易在 / 块里有交易 / 相关状态就在交易里 写成已经有分开的应用状态 interchangeable / 已经 separate-app-state interchangeable，或已经和 325 queryproof bundled / queryproof-sold-as-apphash interchangeable / 731 queryproof-nottxmerkle interchangeable。

## 为什么错

官方把头上有 AppHash 单句、already tx-merkle、already validators-hash、already separate-app-state 写成三件独立的实现事。把它们卖成 already tx-merkle interchangeable / already validators-hash interchangeable / already separate-app-state interchangeable，会把 not already tx-merkle、not already validators-hash、not already separate-app-state 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事（325 余量），必须分开 not already tx-merkle、not already validators-hash、not already separate-app-state 三件事，不要和 325 / 33 / 147 / 38 / 314 / 732 / 733 糊成一句。

## 和相邻反模式

- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query Proofs bundled 全段，不是本页三种锚 item 1 单句边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 已经是本高度交差（147），不是本页 DataHash / ValidatorsHash 边界。
- [snapshottake-notretained-sold-as-bundled](snapshottake-notretained-sold-as-bundled.md) 是生产者只留两份（324 item 3），不是本页头上三种锚边界。
