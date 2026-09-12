# 模式：把 Process 也会在提议者那边叫三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[Process 也会在提议者那边叫 ≠ 已经不用再 Process](../../tracks/implementation/worked-example-process-also-vs-prepare.md)。

## 三个名字

1. **Process 也会在提议者那边叫不是已经不用再 Process：** 看见自己刚 Prepare 过不是已经交差。
2. **通常紧跟 Prepare、列表对得上不是已经保证是这一次：** 看见 txs 一样不是已经必须一样。
3. **失败时可能对上更早一次或根本不调不是已经每轮都会叫：** 看见进了这一轮不是已经会叫 Process。

## 为什么要分开叫

官方把提议者也会叫 Process、通常对得上、失败时不保证写成三件事。把它们叫成一个「看见自己刚 Prepare 过就已经不用再 Process」，会把四门、Req 3 必须 Accept 和候选状态一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见自己刚 Prepare 过就已经不用再 Process」，先数清问的是 Process 也会在提议者那边叫不是已经不用再 Process、通常紧跟 Prepare、列表对得上不是已经保证是这一次，还是失败时可能对上更早一次或根本不调不是已经每轮都会叫，再决定要不要同一次发布。
