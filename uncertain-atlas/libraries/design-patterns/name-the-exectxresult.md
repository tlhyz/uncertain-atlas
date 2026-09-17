# 模式：把 ExecTxResult 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results。  
**例**：[结果列表 ≠ 已经同一顺序](../../tracks/implementation/worked-example-exectxresult-vs-consensus.md)。

## 三个名字

1. **结果列表不是已经同一顺序：** 看见回了列表不是已经和送来的交易对上。
2. **Code 非零不是已经没进块：** 看见标成无效不是已经没进共识，也不是已经建了索引。
3. **Code / Data 不是已经印进本头：** 看见哈希不是已经是本头 LastResultsHash。

## 为什么要分开叫

官方把必须同一顺序、无效仍在块里、下一高度的 LastResultsHash 写成三件事。把它们叫成一个「看见 Finalize 回了就已经交差」，会把四门、气和本头 AppHash 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Finalize 已经回了结果」，先数清问的是列表不是已经同一顺序、Code 非零不是已经没进块，还是 Code / Data 不是已经印进本头，再决定要不要同一次发布。
