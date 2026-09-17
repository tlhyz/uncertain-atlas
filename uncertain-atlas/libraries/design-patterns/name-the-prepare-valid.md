# 模式：把 Prepare 回包校验三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[引擎没有再验重复交易 ≠ 已经验过重复](../../tracks/implementation/worked-example-prepare-valid-vs-checked.md)。

## 三个名字

1. **引擎没有再验重复交易不是已经验过重复：** 看见回了提案不是已经有应用级重放保护。
2. **Prepare 回包验不过引擎崩溃不是已经是 Process REJECT：** 看见回包坏了不是已经是 Req 3 必须 Accept。
3. **Prepare 里产出了事件不是已经交给引擎：** 看见先跑了不是已经印进 LastResultsHash。

## 为什么要分开叫

官方把引擎不再做额外有效性检查、回包验不过当应用坏了并崩溃、Prepare 产出的事件必须留到决定后经 Finalize 交回写成三件事。把它们叫成一个「看见回了提案就已经验过重复」，会把内存池去重、Req 3 必须 Accept 和回执印进本头一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了提案就已经验过重复」，先数清问的是引擎没有再验重复交易不是已经验过重复、Prepare 回包验不过引擎崩溃不是已经是 Process REJECT，还是 Prepare 里产出了事件不是已经交给引擎，再决定要不要同一次发布。
