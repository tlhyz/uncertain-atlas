# 模式：把 FinalizeBlock fill all fields even if Prepare/Process passed 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[fill all fields ≠ 已经 Prepare / Process 给过就不用再 Finalize](../../tracks/implementation/worked-example-finfill-vs-norepeat.md)。

## 三个名字

1. **will fill up all fields in FinalizeBlockRequest 不是已经 Prepare / Process 给过就不用再 Finalize：** 看见 fill up all fields 不是已经交差 interchangeable。
2. **even if already passed via PrepareProposalRequest or ProcessProposalRequest 不是已经字段名对得上就代表已经跑过 Process：** 看见 even if passed 不是已经 Prepare / Process / Finalize 同一套字段 interchangeable。
3. **all fields / 又填一遍 不是已经 decided_last_commit 和 proposed_last_commit 就可以混用：** 看见 all fields 不是已经 decided 和 proposed 语义 interchangeable。

## 为什么要分开叫

官方把 will fill up all fields、even if already passed via Prepare / Process、all fields in FinalizeBlockRequest 写成三个名字。把它们叫成一个「看见 Prepare / Process 已经给过就已经不用再 Finalize、已经字段名对得上就代表已经跑过 Process、decided 和 proposed 字段 interchangeable」，会把再填 Finalize 请求、even if passed 语义和 decided vs proposed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare / Process 已经给过」，先数清问的是 will fill up all fields 是不是已经不用再 Finalize、even if already passed 是不是已经字段名对得上就代表已经跑过 Process，还是 all fields / 又填一遍 是不是已经 decided 和 proposed 就可以混用，再决定要不要同一次发布。
