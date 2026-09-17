# 反模式：看见自己是提议者会先走完 Prepare 那五步就当成已经不用再 Process / 看见 Process 的 height / time 对上拟议块头就当成已经验过块头 / 看见 Finalize 的 height / time 对上拟议块头就当成已经是刚决定那块的字段

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**例**：[自己是提议者会先走完 Prepare 那五步 ≠ 已经不用再 Process](../../tracks/implementation/worked-example-htmatch-vs-header.md)。

## 塌法

1. 看见自己是提议者会先走完 Prepare 那五步 / 看见走完了，就当成已经不用再 Process，或当成已经保证是这一次。
2. 看见 Process 的 `height` / `time` 对上拟议块头 / 看见对上了，就当成已经验过块头，或当成已经跑过 Process。
3. 看见 Finalize 的 `height` / `time` 对上拟议块头 / 看见对上了，就当成已经是刚决定那块的字段，或当成已经知道本头哈希。

## 为什么会出事

官方写：若 *p* 是提议者，*p* 先执行 Prepare 那五步。Process 的 height 和 time 对上拟议块的头。Finalize 的 height 和 time 对上拟议块的头。看见对上了，不是已经不用再 Process，也不是已经验过块头，也不是已经是刚决定那块的字段。

## 和相邻反模式

- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫就已经不用再 Process，不是本页这种自己是提议者会先走完 Prepare 那五步不是已经不用再 Process。
- [proposetimeout-sold-as-process](proposetimeout-sold-as-process.md) 是收到带上头的提案会先验块头就已经跑过 Process，不是本页这种 Process 的 height / time 对上拟议块头不是已经验过块头。
- [finfields-sold-as-equiv](finfields-sold-as-equiv.md) 是 Finalize 含刚决定那块的字段就已经是四门已经结算，不是本页这种 Finalize 的 height / time 对上拟议块头不是已经是刚决定那块的字段。
