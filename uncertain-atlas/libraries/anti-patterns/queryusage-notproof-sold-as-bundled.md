# 反模式：把 Query Usage Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事（487 余量）说成已经 prove 栏 / 已经对上 AppHash / 已经 Finalize Query proofs anchored

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Optionally return Merkle proof not prove 栏 ≠ bundled（487）](../../tracks/implementation/worked-example-queryusage-notproof-vs-bundled.md)。

## 卖法

把 Optionally return Merkle proof / 可选回默克尔证明 写成已经 Query 请求 `prove` 那种能回就回 interchangeable / 383 queryproof interchangeable / 已经勾了 prove 就齐 interchangeable / 已经 Query 回包 proof_ops interchangeable；把可选回默克尔证明写成已经 Query 回了 Proof 就对上 AppHash interchangeable / 325 proofop interchangeable / queryproof-sold-as-apphash interchangeable；把看见 optional 写成已经 Finalize Query proofs anchored interchangeable / 475 finmerkle interchangeable / 625 finmerkle-notquery interchangeable / 已经 Later calls to Query can return proofs interchangeable，或已经和 487 queryusage-vs-querystate bundled / queryusage-notproof-sold-as-bundled interchangeable / 678 queryusage-notproof interchangeable。

## 为什么错

官方把 Query Usage optional proof、Request prove 栏、Query 回了 Proof 就对上 AppHash、Finalize Usage 锚句写成三件独立的实现事。把它们卖成 prove 栏 interchangeable / AppHash matched interchangeable / Finalize Query proofs anchored interchangeable，会把 not prove 栏、not AppHash matched、not Finalize Query proofs anchored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事（487 余量），必须分开 not prove 栏、not AppHash matched、not Finalize Query proofs anchored 三件事，不要和 487 / 383 / 325 / 475 / 625 / 677 / 679 糊成一句。

## 和相邻反模式

- [queryusage-sold-as-querystate](queryusage-sold-as-querystate.md) 是 Query Usage 正式三事 bundled（487），不是本页 item 2 单句边界。
- [queryusage-notquerystate-sold-as-bundled](queryusage-notquerystate-sold-as-bundled.md) 是 Query for data at current or past height 单句边界（677 item 1），不是本页 optional proof 边界。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就对上 AppHash，不是本页 Usage optional proof 单句。
