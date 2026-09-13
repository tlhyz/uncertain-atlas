# 反模式：把 FinalizeBlock fill all fields even if Prepare/Process passed 正式三事卖成已经不用再 Finalize

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[fill all fields ≠ 已经 Prepare / Process 给过就不用再 Finalize](../../tracks/implementation/worked-example-finfill-vs-norepeat.md)。

## 卖法

- 「看见 Prepare / Process 已经给过应用，就不用再 Finalize。」
- 「看见字段名对得上，就代表已经跑过 Process / 已经是刚决定那块的字段。」
- 「看见又填一遍，decided_last_commit 和 proposed_last_commit 可以混用。」

## 为什么错

官方把 will fill up all fields in FinalizeBlockRequest、even if already passed via PrepareProposalRequest or ProcessProposalRequest、all fields 写成三件独立的实现事。把它们卖成已经不用再 Finalize、字段名对上就够、decided 和 proposed 可以混用，会把再填 Finalize 请求、even if passed 语义和 decided vs proposed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 请求栏，必须分开 will fill up all fields、even if already passed、all fields 三个名字，不要把它们卖成已经 Prepare / Process 给过就不用再 Finalize。
