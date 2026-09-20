# 反模式：把一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事（325 余量）说成已经交给下一层 / 已经对上最终 AppHash / 已经比对着块哈希

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[一层对上 not already next-layer ≠ bundled（325）](../../tracks/implementation/worked-example-queryproof-notfinalapphash-vs-bundled.md)。

## 卖法

把一层对上 / 这一条 ProofOp 的根对了 / 一层根绿了 写成已经交给下一层 interchangeable / 已经 next-layer interchangeable / 已经是下一条要验的值交差 interchangeable / 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable；把中间根对了 / 对上了 / 某层根绿了 写成已经对上最终 AppHash interchangeable / 已经 final-apphash interchangeable；把能证缺席 / 缺席证明绿了 / 能证这把键不在 写成已经比对着块哈希 interchangeable / 已经 blockhash-compared interchangeable，或已经和 325 queryproof bundled / queryproof-sold-as-apphash interchangeable / 733 queryproof-notfinalapphash interchangeable。

## 为什么错

官方把一层对上单句、already next-layer、already final-apphash、already blockhash-compared 写成三件独立的实现事。把它们卖成 already next-layer interchangeable / already final-apphash interchangeable / already blockhash-compared interchangeable，会把 not already next-layer、not already final-apphash、not already blockhash-compared 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事（325 余量），必须分开 not already next-layer、not already final-apphash、not already blockhash-compared 三件事，不要和 325 / 33 / 731 / 732 / 147 / 38 / 314 糊成一句。

## 和相邻反模式

- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query Proofs bundled 全段，不是本页多层根接值 item 3 单句边界。
- [queryproof-notverified-sold-as-bundled](queryproof-notverified-sold-as-bundled.md) 是回证明 item 2，不是本页最后一条对 AppHash 边界。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 已经是本高度交差（147），不是本页中间根对最终 AppHash 边界。
