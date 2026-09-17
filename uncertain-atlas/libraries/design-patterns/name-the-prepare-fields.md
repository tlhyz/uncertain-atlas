# 模式：把 Prepare 请求字段三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[Prepare 和 Process / Finalize 同一套字段 ≠ 已经跑过 Process](../../tracks/implementation/worked-example-prepare-fields-vs-same.md)。

## 三个名字

1. **Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process：** 看见字段名对得上不是已经 Finalize。
2. **local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展：** 看见有上一高的票不是已经到了 H 就已经 Prepare 带了扩展。
3. **height / time / proposer_address 对上拟议头不是已经知道本头哈希：** 看见对得上不是已经是候选已经是 ExecuteTxState。

## 为什么要分开叫

官方把 Prepare 请求里那几列和 Process / Finalize 同一套、`local_last_commit` 是上一高度预提交带扩展、`height` / `time` / `proposer_address` 对上拟议头写成三件事。把它们叫成一个「看见字段名对得上就已经跑过 Process」，会把提议者那边也会叫 Process、扩展启用高度和候选状态一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见字段名对得上就已经跑过 Process」，先数清问的是 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process、local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展，还是 height / time / proposer_address 对上拟议头不是已经知道本头哈希，再决定要不要同一次发布。
