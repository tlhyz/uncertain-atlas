# 反模式：看见 Prepare 和 Process / Finalize 同一套字段就当成已经跑过 Process / 看见 local_last_commit 是上一高度的预提交带扩展就当成已经是本高度刚签的扩展 / 看见 height / time / proposer_address 对上拟议头就当成已经知道本头哈希

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[Prepare 和 Process / Finalize 同一套字段 ≠ 已经跑过 Process](../../tracks/implementation/worked-example-prepare-fields-vs-same.md)。

## 塌法

1. 看见 `txs` / `misbehavior` / `height` / `time` / `next_validators_hash` / `proposer_address` 和 Process / Finalize 同一套 / 看见字段名对得上，就当成已经跑过 Process，或当成已经 Finalize。
2. 看见 `local_last_commit` 是上一高度的预提交带扩展 / 看见有上一高的票，就当成已经是本高度刚签的扩展，或当成已经到了 H 就已经 Prepare 带了扩展。
3. 看见 `height` / `time` / `proposer_address` 对上拟议头 / 看见对得上，就当成已经知道本头哈希，或当成已经是候选已经是 ExecuteTxState。

## 为什么会出事

官方写：`PrepareProposalRequest` 的 `txs`、`misbehavior`、`height`、`time`、`next_validators_hash`、`proposer_address` 和 `ProcessProposalRequest`、`FinalizeBlockRequest` 是同一套。`local_last_commit` 是上一高度的预提交，包括促成上一块决定的那些，以及对应的投票扩展。`height`、`time`、`proposer_address` 对上拟议块头里的值。

## 和相邻反模式

- [prepfields-notprocess-sold-as-bundled](prepfields-notprocess-sold-as-bundled.md) 是同一套字段 not already ran-process / not already finalize / not already settled 正式三事（359 item 1），不是本页 bundled 全段 alone。
- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫就已经不用再 Process，不是本页这种 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 就已经 Prepare 带了扩展，不是本页这种 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选已经是 ExecuteTxState，不是本页这种 height / time / proposer_address 对上拟议头不是已经知道本头哈希。
