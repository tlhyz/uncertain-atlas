# 反模式：看见引擎没有再验重复交易就当成已经验过重复 / 看见 Prepare 回包验不过引擎崩溃就当成已经是 Process REJECT / 看见 Prepare 里产出了事件就当成已经交给引擎

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[引擎没有再验重复交易 ≠ 已经验过重复](../../tracks/implementation/worked-example-prepare-valid-vs-checked.md)。

## 塌法

1. 看见引擎没有再验重复交易 / 看见回了提案，就当成已经验过重复，或当成已经有应用级重放保护。
2. 看见 Prepare 回包验不过 / 看见引擎当应用坏了并崩溃，就当成已经是 Process REJECT，或当成已经是正确提议者的准备提案必须被正确接收者 Accept。
3. 看见 Prepare 里产出了块事件或交易事件 / 看见先跑了，就当成已经交给引擎，或当成已经印进 LastResultsHash。

## 为什么会出事

官方写：CometBFT 不再做额外有效性检查，例如查有没有重复交易。若验不过 `PrepareProposalResponse`，就把应用当成故障并崩溃。Prepare 里产出的事件必须留到块决定之后，再经 `FinalizeBlockResponse` 交回。

## 和相邻反模式

- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是内存池去重就已经保证不重放，不是本页这种引擎没有再验重复交易不是已经验过重复。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept，不是本页这种 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Code / Data 就已经印进本头，不是本页这种 Prepare 里产出了事件不是已经交给引擎。
