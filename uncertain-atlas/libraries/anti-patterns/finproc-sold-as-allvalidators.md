# 反模式：把 FinalizeBlock When calling ProcessProposal guarantee 正式三事卖成已经每个验证者都跑过 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[When calling FinalizeBlock guarantee ≠ 已经每个验证者都跑过 Process](../../tracks/implementation/worked-example-finproc-vs-allvalidators.md)。

## 卖法

- 「看见要 Finalize 了就已经每个验证者都对这块跑过 Process。」
- 「看见提议者这边 Process 过就代表全网都 Process 过。」
- 「看见已经套用 candidate / 先前 Prepare 或 Process 跑过就不需要 Process 保证。」

## 为什么错

官方把 When calling `FinalizeBlock` with a block / consensus algorithm guarantees、at least one non-byzantine validator、has run `ProcessProposal` on that block 写成三件独立的实现事。把它们卖成每个验证者都跑过、提议者 Process 过就代表全网、套用 candidate 就不需要 guarantee，会把 guarantee 范围、至少一名和 ran ProcessProposal 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 前的 Process 保证，必须分开 When calling FinalizeBlock / consensus guarantees、at least one non-byzantine、has run ProcessProposal on that block 三个名字，不要把它们卖成已经每个验证者都跑过 Process。
