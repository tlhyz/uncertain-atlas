# 反模式：把 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事（325 余量）说成已经验过 / 已经是同一棵树 / 已经能证不存在

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了 Proof not already verified ≠ bundled（325）](../../tracks/implementation/worked-example-queryproof-notverified-vs-bundled.md)。

## 卖法

把回了 Proof / QueryResponse.Proof / 回了证明 写成已经验过对上 AppHash interchangeable / 已经 verified interchangeable / 已经用对应块 AppHash 验过交差 interchangeable / 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable；把有 type / ProofOp 有 type / 指定了树类型 写成已经是同一棵树 interchangeable / 已经 same-tree interchangeable；把能证存在 / 存在证明绿了 / 能证这把键在 写成已经能证不存在 interchangeable / 已经 prove-absence interchangeable，或已经和 325 queryproof bundled / queryproof-sold-as-apphash interchangeable / 732 queryproof-notverified interchangeable。

## 为什么错

官方把回了 Proof 单句、already verified、already same-tree、already prove-absence 写成三件独立的实现事。把它们卖成 already verified interchangeable / already same-tree interchangeable / already prove-absence interchangeable，会把 not already verified、not already same-tree、not already prove-absence 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事（325 余量），必须分开 not already verified、not already same-tree、not already prove-absence 三件事，不要和 325 / 33 / 731 / 733 / 147 / 38 / 314 糊成一句。

## 和相邻反模式

- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query Proofs bundled 全段，不是本页回证明 item 2 单句边界。
- [queryproof-nottxmerkle-sold-as-bundled](queryproof-nottxmerkle-sold-as-bundled.md) 是三种锚 item 1，不是本页回证明与验边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 已经是本高度交差（147），不是本页用对应块 AppHash 去验边界。
