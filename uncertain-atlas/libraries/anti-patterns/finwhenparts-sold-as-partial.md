# 反模式：把 FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事卖成已经 +2/3 precommit 就会调 Finalize

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Proposal + all block parts ≠ 已经只有 hash](../../tracks/implementation/worked-example-finwhenparts-vs-partial.md)。

## 卖法

- 「看见有 +2/3 precommit 就已经会调 Finalize / 已经决定。」
- 「看见填了 hash / height 就代表已经收齐 all block parts。」
- 「看见 +2/3 prevote 同一 id(v) 就已经够触发 Finalize，和 2f+1 precommit interchangeable。」

## 为什么错

官方把 Proposal + all block parts、2f+1 precommit same id(v)、decides block v 写成三件独立的实现事。把它们卖成已经 +2/3 precommit 就会调 Finalize、已经只有 hash、prevote 和 precommit interchangeable，会把收齐块片、Precommit 门槛、决定 _v_ 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock When 触发条件，必须分开 Proposal + all block parts、2f+1 precommit same id(v)、decides block v 三个名字，不要把它们卖成已经 +2/3 precommit 就会调 Finalize。

## 和相邻反模式

- [finalizewhen-sold-as-decided](../../libraries/anti-patterns/finalizewhen-sold-as-decided.md) 是 +2/3 precommit 就已经会调 Finalize，本页另钉 all block parts / 2f+1 三事。
- [extendwhen-sold-as-locked](../../libraries/anti-patterns/extendwhen-sold-as-locked.md) 是 +2/3 prevote 才 ExtendVote，不是本页 2f+1 precommit 门槛。
- [finproc-sold-as-allvalidators](../../libraries/anti-patterns/finproc-sold-as-allvalidators.md) 是 Process guarantee，不是本页 Proposal + parts 触发。
